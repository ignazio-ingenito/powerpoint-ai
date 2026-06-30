import json
import logging
import os
import time
import hashlib
from io import BytesIO
from pathlib import Path
from collections.abc import Iterator
from datetime import datetime, timezone
from typing import Any
from urllib.parse import quote_plus

import boto3
import dlt
import pandas as pd
import requests
import sqlalchemy as sa
import yaml
from dlt.destinations import sqlalchemy as dlt_sqlalchemy


DEFAULT_JIRA_PAGE_SIZE = 100
DEFAULT_JIRA_REQUEST_TIMEOUT = 180
DEFAULT_API_REQUEST_RETRIES = 3
DEFAULT_API_RETRY_BACKOFF_SECONDS = 10
DEFAULT_TEMPO_BASE_URL = "https://api.tempo.io/4"
LOGGER = logging.getLogger(__name__)
RUN_LOGGER = LOGGER
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
REQUIRED_JIRA_ENV = (
    "JIRA_BASE_URL",
    "JIRA_EMAIL",
    "JIRA_API_TOKEN",
    "JIRA_ISSUE_JQL",
)
REQUIRED_TEMPO_ENV = (
    "TEMPO_API_TOKEN",
)
REQUIRED_DATABASE_ENV = (
    "MARIADB_HOST",
    "MARIADB_PORT",
    "MARIADB_USER",
    "MARIADB_PASSWORD",
    "MARIADB_DATABASE",
)
DEFAULT_REF_MAPPING_CONFIG = "input/config/xls_mappings_index.yaml"
DEFAULT_REF_MAPPING_DIR = "input/config"
REF_MAPPING_STATE_TABLE = "dlt_ref_file_state"
DEFAULT_SQL_TRANSFORMATION_FILES = (
    "init/002_stg_jira_views.sql",
    "init/003_tempo_issue_account_mart.sql",
)
JIRA_ISSUE_STANDARD_FIELDS = (
    "assignee",
    "created",
    "duedate",
    "issuetype",
    "issuelinks",
    "key",
    "labels",
    "parent",
    "priority",
    "project",
    "reporter",
    "resolution",
    "resolutiondate",
    "status",
    "summary",
    "updated",
)
JIRA_ISSUE_CUSTOM_FIELDS = {
    "Organizations": "organizations",
    "Attività su DB": "attivita_su_db",
    "Categoria": "categoria",
    "Categoria SQL": "categoria_sql",
    "Comando SQL": "comando_sql",
    "Data TK Axel": "data_tk_axel",
    "Data stima approvata": "data_stima_approvata",
    "Impatto incident": "impatto_incident",
    "KPI Breached": "kpi_breached",
    "ODA - Ordine di Acquisto": "oda_ordine_di_acquisto",
    "Presa in carico": "presa_in_carico",
    "Processi": "processi",
    "Prodotti": "prodotti",
    "Satisfaction": "satisfaction",
    "Satisfaction date": "satisfaction_date",
    "SLA AMCO": "sla_amco",
    "SLA ING": "sla_ing",
    "SLA SB": "sla_sb",
    "Stima approvata": "stima_approvata",
    "Stima intervento in ore": "stima_intervento_ore",
    "Priorità Cliente": "priorita_cliente",
    "Sla_ticket": "sla_ticket",
    "Tempo di presa in carico": "tempo_di_presa_in_carico",
    "Service Desk time": "service_desk_time",
    "Tipo Attività": "tipo_attivita",
    "BPO AMCO": "bpo_amco",
    "BPO AMPRE": "bpo_ampre",
    "BPO JJ TATOOINE": "bpo_jj_tatooine",
    "SOW - Statement of Work": "sow_statement_of_work",
    "Data presa in carico": "data_presa_in_carico",
    "SLA KPI Presa in carico": "sla_kpi_presa_in_carico",
    "SLA ELAPSED": "sla_elapsed",
}
RAW_JIRA_ISSUE_OPTIONAL_COLUMNS = (
    "assignee",
    "reporter",
    "priority",
    "resolution",
    "labels",
    "linked_issues",
    "resolved_at",
    "due_date",
    *JIRA_ISSUE_CUSTOM_FIELDS.values(),
)


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def _optional_int_env(name: str, default: int | None = None) -> int | None:
    value = os.getenv(name)
    if not value:
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise RuntimeError(f"{name} must be an integer, got: {value}") from exc


def _validate_required_env(names: tuple[str, ...]) -> None:
    missing = [name for name in names if not os.getenv(name)]
    if missing:
        missing_names = ", ".join(missing)
        raise RuntimeError(f"Missing required environment variables: {missing_names}")

    _optional_int_env("JIRA_MAX_RESULTS")
    _optional_int_env("JIRA_PAGE_SIZE", DEFAULT_JIRA_PAGE_SIZE)
    _optional_int_env("JIRA_REQUEST_TIMEOUT", DEFAULT_JIRA_REQUEST_TIMEOUT)
    _optional_int_env("API_REQUEST_RETRIES", DEFAULT_API_REQUEST_RETRIES)
    _optional_int_env("API_RETRY_BACKOFF_SECONDS", DEFAULT_API_RETRY_BACKOFF_SECONDS)


def _loaded_at() -> str:
    return datetime.now(timezone.utc).isoformat()


def _as_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def _set_run_logger(logger: Any | None) -> None:
    global RUN_LOGGER
    RUN_LOGGER = logger or LOGGER


def _log_info(message: str) -> None:
    RUN_LOGGER.info(message)


def _normalize_base_url(value: str) -> str:
    base_url = value.strip().rstrip("/")
    if not base_url.startswith(("http://", "https://")):
        base_url = f"https://{base_url}"
    return base_url


def _normalize_jql_for_guard(jql: str) -> str:
    return " ".join(jql.lower().split())


def _validate_jira_jql_scope(jql: str, max_results: int | None) -> None:
    if max_results is not None:
        return

    normalized_jql = _normalize_jql_for_guard(jql)
    unbounded_jqls = {
        "project is not empty",
        "project is not empty order by updated desc",
    }
    if normalized_jql in unbounded_jqls:
        raise RuntimeError(
            "JIRA_ISSUE_JQL is too broad for an unlimited run. "
            "Use a business-bounded JQL, or set JIRA_MAX_RESULTS only for technical tests."
        )


def _jira_session() -> tuple[requests.Session, str]:
    base_url = _normalize_base_url(_required_env("JIRA_BASE_URL"))
    email = _required_env("JIRA_EMAIL")
    token = _required_env("JIRA_API_TOKEN")

    session = requests.Session()
    session.auth = (email, token)
    session.headers.update(
        {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )
    return session, base_url


def _tempo_session() -> requests.Session:
    token = _required_env("TEMPO_API_TOKEN")

    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        }
    )
    return session


def _tempo_accounts_url() -> str:
    base_url = _normalize_base_url(os.getenv("TEMPO_BASE_URL", DEFAULT_TEMPO_BASE_URL))
    return f"{base_url}/accounts"


def _parse_jira_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None

    normalized_value = value.removesuffix("Z") + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized_value)
    except ValueError:
        return None


def _jira_issue_updated_at(issue: dict[str, Any]) -> datetime | None:
    issue_fields = issue.get("fields") or {}
    if not isinstance(issue_fields, dict):
        return None
    return _parse_jira_datetime(issue_fields.get("updated"))


def _is_newer_jira_issue(
    new_updated_at: datetime | None,
    existing_updated_at: datetime | None,
) -> bool:
    if new_updated_at is None:
        return existing_updated_at is None
    if existing_updated_at is None:
        return True
    return new_updated_at > existing_updated_at


def _build_dlt_connection_string() -> str:
    host = _required_env("MARIADB_HOST")
    port = _required_env("MARIADB_PORT")
    user = quote_plus(_required_env("MARIADB_USER"))
    password = quote_plus(_required_env("MARIADB_PASSWORD"))
    database = _required_env("MARIADB_DATABASE")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"


def _sql_statements_from_file(path: Path) -> list[str]:
    sql_text = path.read_text(encoding="utf-8")
    return [statement.strip() for statement in sql_text.split(";") if statement.strip()]


def _ensure_raw_jira_issue_optional_columns(conn: sa.Connection) -> None:
    existing_columns = set(
        conn.execute(
            sa.text(
                """
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = DATABASE()
                  AND table_name = 'raw_jira_issues'
                """
            )
        ).scalars()
    )
    missing_columns = [
        column_name
        for column_name in RAW_JIRA_ISSUE_OPTIONAL_COLUMNS
        if column_name not in existing_columns
    ]
    for column_name in missing_columns:
        conn.execute(sa.text(f"ALTER TABLE raw_jira_issues ADD COLUMN `{column_name}` TEXT NULL"))

    if missing_columns:
        _log_info(
            "Added missing nullable raw_jira_issues columns before SQL transformations: "
            + ", ".join(missing_columns)
        )


def run_sql_transformations(
    sql_paths: tuple[str, ...] = DEFAULT_SQL_TRANSFORMATION_FILES,
    logger: Any | None = None,
) -> list[str]:
    _set_run_logger(logger)
    _validate_required_env(REQUIRED_DATABASE_ENV)
    engine = sa.create_engine(_build_dlt_connection_string())
    executed_files: list[str] = []

    with engine.begin() as conn:
        _ensure_raw_jira_issue_optional_columns(conn)

        for sql_path in sql_paths:
            path = Path(sql_path)
            if not path.is_absolute():
                path = (Path.cwd() / path).resolve()
            if not path.exists():
                raise RuntimeError(f"SQL transformation file not found: {path}")

            statements = _sql_statements_from_file(path)
            for statement in statements:
                conn.execute(sa.text(statement))

            executed_files.append(str(path))
            _log_info(f"Applied SQL transformation file: {path} ({len(statements)} statement(s))")

    return executed_files


def _parse_s3_uri(uri: str) -> tuple[str, str]:
    if not uri.startswith("s3://"):
        raise RuntimeError(f"Invalid s3 URI: {uri}")
    path = uri.removeprefix("s3://")
    if "/" not in path:
        raise RuntimeError(f"Invalid s3 URI (missing object key): {uri}")
    bucket, key = path.split("/", 1)
    return bucket, key


def _resolve_source_path(base_path: str, referenced_path: str) -> str:
    if referenced_path.startswith("s3://"):
        return referenced_path

    if base_path.startswith("s3://"):
        bucket, base_key = _parse_s3_uri(base_path)
        base_prefix = base_key.rsplit("/", 1)[0] if "/" in base_key else ""
        key = referenced_path.lstrip("/")
        if base_prefix:
            key = f"{base_prefix}/{key}"
        return f"s3://{bucket}/{key}"

    candidate = Path(referenced_path)
    if candidate.is_absolute():
        return str(candidate)

    # Prefer project-root relative paths (cwd), then fallback to mapping-file relative.
    cwd_candidate = (Path.cwd() / candidate).resolve()
    if cwd_candidate.exists():
        return str(cwd_candidate)

    return str((Path(base_path).parent / candidate).resolve())


def _resolve_mapping_config_path(mapping_config_path: str) -> str:
    if mapping_config_path.startswith("s3://"):
        return mapping_config_path

    candidate = Path(mapping_config_path)
    if candidate.is_absolute():
        return str(candidate)

    cwd_candidate = (Path.cwd() / candidate).resolve()
    if cwd_candidate.exists():
        return str(cwd_candidate)

    mapping_dir = os.getenv("REF_MAPPING_DIR", DEFAULT_REF_MAPPING_DIR)
    base_dir = Path(mapping_dir)
    if not base_dir.is_absolute():
        base_dir = (Path.cwd() / base_dir).resolve()
    return str((base_dir / candidate).resolve())


def _read_source_bytes(source_path: str) -> bytes:
    if source_path.startswith("s3://"):
        bucket, key = _parse_s3_uri(source_path)
        response = boto3.client("s3").get_object(Bucket=bucket, Key=key)
        body = response.get("Body")
        if body is None:
            raise RuntimeError(f"Empty S3 object body for {source_path}")
        return body.read()

    local_path = Path(source_path)
    if not local_path.is_absolute():
        local_path = Path.cwd() / local_path
    if not local_path.exists():
        raise RuntimeError(f"Source file not found: {local_path}")
    return local_path.read_bytes()


def _source_fingerprint(source_path: str) -> str:
    if source_path.startswith("s3://"):
        bucket, key = _parse_s3_uri(source_path)
        metadata = boto3.client("s3").head_object(Bucket=bucket, Key=key)
        etag = str(metadata.get("ETag", "")).strip('"')
        size = int(metadata.get("ContentLength", 0))
        last_modified = metadata.get("LastModified")
        last_modified_text = (
            last_modified.isoformat() if hasattr(last_modified, "isoformat") else str(last_modified)
        )
        return f"s3:{bucket}:{key}:{etag}:{size}:{last_modified_text}"

    local_path = Path(source_path)
    if not local_path.is_absolute():
        local_path = (Path.cwd() / local_path).resolve()
    if not local_path.exists():
        raise RuntimeError(f"Source file not found: {local_path}")
    stat = local_path.stat()
    return f"file:{local_path}:{stat.st_size}:{stat.st_mtime_ns}"


def _normalize_cell(value: Any) -> Any:
    if pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date()
    return value


def _load_ref_mapping_config(config_path: str) -> dict[str, Any]:
    config_bytes = _read_source_bytes(config_path)
    mapping = yaml.safe_load(config_bytes)
    if not isinstance(mapping, dict):
        raise RuntimeError(f"Invalid mapping config: {config_path}")
    return mapping


def _list_ref_mapping_paths(config_path: str) -> list[str]:
    config = _load_ref_mapping_config(config_path)
    mappings = config.get("mappings")
    if isinstance(mappings, list):
        mapping_paths: list[str] = []
        for item in mappings:
            if not isinstance(item, str):
                raise RuntimeError(f"Invalid mapping entry in {config_path}: {item}")
            mapping_paths.append(_resolve_source_path(config_path, item))
        if not mapping_paths:
            raise RuntimeError(f"No mapping files listed in {config_path}")
        return mapping_paths
    return [config_path]


def _mapping_fingerprint(mapping: dict[str, Any]) -> str:
    encoded = yaml.safe_dump(mapping, sort_keys=True, allow_unicode=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _mapping_path_hash(mapping_path: str) -> str:
    return hashlib.sha256(mapping_path.encode("utf-8")).hexdigest()


def _mapped_excel_rows(mapping: dict[str, Any]) -> tuple[list[dict[str, Any]], str, str]:
    source = mapping.get("source") or {}
    target = mapping.get("target") or {}
    columns = mapping.get("columns") or {}
    load_options = mapping.get("load_options") or {}

    source_file = source.get("file")
    source_sheet = source.get("sheet")
    target_table = target.get("table")

    if not source_file or not isinstance(source_file, str):
        raise RuntimeError("Mapping config source.file is required")
    if not source_sheet or not isinstance(source_sheet, str):
        raise RuntimeError("Mapping config source.sheet is required")
    if not target_table or not isinstance(target_table, str):
        raise RuntimeError("Mapping config target.table is required")
    if not isinstance(columns, dict) or not columns:
        raise RuntimeError("Mapping config columns must be a non-empty object")

    if not isinstance(source_file, str):
        raise RuntimeError("Mapping config source.file must be a string")

    excel_bytes = _read_source_bytes(source_file)
    data_frame = pd.read_excel(BytesIO(excel_bytes), sheet_name=source_sheet)
    def _normalize_header_name(value: Any) -> str:
        if value is None:
            return ""
        text = str(value).replace("\u00a0", " ")
        return " ".join(text.split()).strip()

    normalized_actual_columns: dict[str, Any] = {}
    for actual in data_frame.columns:
        key = _normalize_header_name(actual)
        if key and key not in normalized_actual_columns:
            normalized_actual_columns[key] = actual

    resolved_source_columns: dict[str, Any] = {}
    missing_columns: list[str] = []
    for source_name in columns:
        if source_name in data_frame.columns:
            resolved_source_columns[source_name] = source_name
            continue
        normalized_source = _normalize_header_name(source_name)
        if normalized_source in normalized_actual_columns:
            resolved_source_columns[source_name] = normalized_actual_columns[normalized_source]
            continue
        missing_columns.append(source_name)

    if missing_columns:
        missing = ", ".join(missing_columns)
        raise RuntimeError(f"Excel source is missing mapped columns: {missing}")

    required_columns = load_options.get("required_columns") or []
    selected = data_frame.loc[:, [resolved_source_columns[name] for name in columns.keys()]]
    selected = selected.where(pd.notna(selected), None)

    records: list[dict[str, Any]] = []
    for _, row in selected.iterrows():
        record: dict[str, Any] = {}
        for source_name, target_name in columns.items():
            resolved_source_name = resolved_source_columns[source_name]
            record[str(target_name)] = _normalize_cell(row[resolved_source_name])
        records.append(record)

    if required_columns:
        for required in required_columns:
            if not any(record.get(required) not in (None, "") for record in records):
                raise RuntimeError(f"Required column has no values: {required}")

    return records, target_table, source_file


def _ref_excel_source_from_records(
    records: list[dict[str, Any]], target_table: str, write_disposition: str = "replace"
):
    _log_info(f"Preparing ref Excel load for table {target_table}: {len(records)} rows")

    @dlt.resource(name=target_table, write_disposition=write_disposition)
    def ref_excel_resource() -> Iterator[dict[str, Any]]:
        for record in records:
            yield record

    @dlt.source(name=f"ref_{target_table}")
    def ref_excel_source():
        return [ref_excel_resource()]

    return ref_excel_source()


def _ref_excel_source(mapping: dict[str, Any]):
    records, target_table, _ = _mapped_excel_rows(mapping)
    load_options = mapping.get("load_options") or {}
    write_disposition = "replace" if load_options.get("truncate_before_load", True) else "append"
    return _ref_excel_source_from_records(records, target_table, write_disposition)


def _raise_for_response(response: requests.Response, context: str) -> None:
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        body = response.text[:1000]
        raise RuntimeError(f"{context} failed: {response.status_code} {body}") from exc


def _request_with_retries(
    session: requests.Session,
    method: str,
    url: str,
    context: str,
    *,
    timeout: int,
    **kwargs: Any,
) -> requests.Response:
    retries = _optional_int_env("API_REQUEST_RETRIES", DEFAULT_API_REQUEST_RETRIES)
    backoff_seconds = _optional_int_env(
        "API_RETRY_BACKOFF_SECONDS",
        DEFAULT_API_RETRY_BACKOFF_SECONDS,
    )
    if retries is None or retries < 0:
        raise RuntimeError("API_REQUEST_RETRIES must be greater than or equal to 0")
    if backoff_seconds is None or backoff_seconds < 0:
        raise RuntimeError("API_RETRY_BACKOFF_SECONDS must be greater than or equal to 0")

    for attempt in range(1, retries + 2):
        try:
            response = session.request(method, url, timeout=timeout, **kwargs)
            if response.status_code not in RETRYABLE_STATUS_CODES:
                _raise_for_response(response, context)
                return response

            if attempt > retries:
                _raise_for_response(response, context)

            wait_seconds = backoff_seconds * attempt
            _log_info(
                f"{context} attempt {attempt} failed with HTTP {response.status_code}; "
                f"retrying in {wait_seconds}s"
            )
        except (requests.Timeout, requests.ConnectionError) as exc:
            if attempt > retries:
                raise

            wait_seconds = backoff_seconds * attempt
            _log_info(
                f"{context} attempt {attempt} failed with {exc.__class__.__name__}; "
                f"retrying in {wait_seconds}s"
            )

        time.sleep(wait_seconds)

    raise RuntimeError(f"{context} failed after {retries + 1} attempts")


def _get_jira_fields() -> list[dict[str, Any]]:
    session, base_url = _jira_session()
    response = _request_with_retries(
        session,
        "GET",
        f"{base_url}/rest/api/3/field",
        "Jira fields request",
        timeout=30,
    )
    fields = response.json()
    if not isinstance(fields, list):
        raise RuntimeError("Jira fields response is not a list")
    return fields


def _find_account_field(fields: list[dict[str, Any]]) -> dict[str, Any]:
    matches = [field for field in fields if field.get("name") == "Account"]
    if not matches:
        raise RuntimeError("Jira custom field named 'Account' was not found")
    if len(matches) > 1:
        ids = ", ".join(str(field.get("id")) for field in matches)
        raise RuntimeError(f"Multiple Jira fields named 'Account' found: {ids}")
    return matches[0]


def _find_jira_fields_by_name(
    fields: list[dict[str, Any]],
    field_names: tuple[str, ...] | list[str],
) -> dict[str, dict[str, Any]]:
    matches: dict[str, list[dict[str, Any]]] = {field_name: [] for field_name in field_names}
    for field in fields:
        field_name = field.get("name")
        if field_name in matches:
            matches[field_name].append(field)

    resolved: dict[str, dict[str, Any]] = {}
    for field_name, field_matches in matches.items():
        if not field_matches:
            _log_info(f"Jira field named '{field_name}' was not found; related issue column will be null")
            continue
        if len(field_matches) > 1:
            ids = ", ".join(str(field.get("id")) for field in field_matches)
            raise RuntimeError(f"Multiple Jira fields named '{field_name}' found: {ids}")
        resolved[field_name] = field_matches[0]
    return resolved


def _jira_named_value(value: Any) -> Any:
    if not isinstance(value, dict):
        return value
    for key in ("displayName", "name", "value", "id"):
        if value.get(key) is not None:
            return value.get(key)
    return _as_json(value)


def _jira_scalar_field_value(value: Any) -> Any:
    if isinstance(value, list):
        return _as_json(value)
    return _jira_named_value(value)


@dlt.resource(name="raw_jira_fields", write_disposition="replace")
def jira_fields() -> Iterator[dict[str, Any]]:
    fields = _get_jira_fields()
    account_field = _find_account_field(fields)
    account_field_id = account_field.get("id")
    loaded_at = _loaded_at()

    _log_info(f"Fetched Jira fields page 1: {len(fields)} rows, total={len(fields)}")

    for field in fields:
        field_id = field.get("id")
        yield {
            "field_id": field_id,
            "field_name": field.get("name"),
            "is_custom": bool(field.get("custom")),
            "is_account_field": field_id == account_field_id,
            "raw_payload": _as_json(field),
            "_loaded_at": loaded_at,
        }


@dlt.resource(name="raw_jira_issues", write_disposition="replace")
def jira_issues() -> Iterator[dict[str, Any]]:
    session, base_url = _jira_session()
    jql = _required_env("JIRA_ISSUE_JQL")
    max_results = _optional_int_env("JIRA_MAX_RESULTS")
    _validate_jira_jql_scope(jql, max_results)
    page_size = _optional_int_env("JIRA_PAGE_SIZE", DEFAULT_JIRA_PAGE_SIZE)
    request_timeout = _optional_int_env("JIRA_REQUEST_TIMEOUT", DEFAULT_JIRA_REQUEST_TIMEOUT)
    if page_size is None or page_size < 1 or page_size > 100:
        raise RuntimeError("JIRA_PAGE_SIZE must be between 1 and 100")
    if request_timeout is None or request_timeout < 1:
        raise RuntimeError("JIRA_REQUEST_TIMEOUT must be greater than 0")

    fields = _get_jira_fields()
    account_field = _find_account_field(fields)
    account_field_id = account_field["id"]
    custom_fields_by_name = _find_jira_fields_by_name(
        fields,
        list(JIRA_ISSUE_CUSTOM_FIELDS.keys()),
    )
    custom_field_ids = [
        field["id"]
        for field in custom_fields_by_name.values()
        if isinstance(field.get("id"), str)
    ]

    next_page_token: str | None = None
    seen_page_tokens: set[str] = set()
    remaining = max_results
    loaded_at = _loaded_at()
    page_number = 0
    extracted_count = 0
    duplicate_issue_ids: set[str] = set()
    issue_records: dict[str, tuple[datetime | None, dict[str, Any]]] = {}
    issue_records_without_id: list[dict[str, Any]] = []

    while True:
        current_page_size = page_size if remaining is None else min(remaining, page_size)
        if current_page_size <= 0:
            break

        request_body: dict[str, Any] = {
            "jql": jql,
            "maxResults": current_page_size,
            "fields": list(JIRA_ISSUE_STANDARD_FIELDS) + [account_field_id, *custom_field_ids],
        }
        if next_page_token:
            if next_page_token in seen_page_tokens:
                raise RuntimeError(
                    "Jira pagination returned a repeated nextPageToken; aborting to avoid an infinite loop"
                )
            seen_page_tokens.add(next_page_token)
            request_body["nextPageToken"] = next_page_token

        page_number += 1
        _log_info(f"Fetching Jira issues page {page_number} with page_size={current_page_size}")
        response = _request_with_retries(
            session,
            "POST",
            f"{base_url}/rest/api/3/search/jql",
            "Jira issues search request",
            json=request_body,
            timeout=request_timeout,
        )
        payload = response.json()
        issues = payload.get("issues")
        if not isinstance(issues, list):
            raise RuntimeError("Jira issues response does not contain an issues list")

        extracted_count += len(issues)
        _log_info(f"Fetched Jira issues page {page_number}: {len(issues)} rows, total={extracted_count}")

        for issue in issues:
            issue_fields = issue.get("fields") or {}
            account_value = issue_fields.get(account_field_id)
            account_id = account_value.get("id") if isinstance(account_value, dict) else None
            labels = issue_fields.get("labels")
            linked_issues = issue_fields.get("issuelinks")
            record = {
                "issue_id": issue.get("id"),
                "issue_key": issue.get("key"),
                "summary": issue_fields.get("summary"),
                "status": _jira_named_value(issue_fields.get("status")),
                "created": issue_fields.get("created"),
                "assignee": _jira_named_value(issue_fields.get("assignee")),
                "reporter": _jira_named_value(issue_fields.get("reporter")),
                "priority": _jira_named_value(issue_fields.get("priority")),
                "resolution": _jira_named_value(issue_fields.get("resolution")),
                "updated": issue_fields.get("updated"),
                "due_date": issue_fields.get("duedate"),
                "resolved_at": issue_fields.get("resolutiondate"),
                "account_field_id": account_field_id,
                "account_id": account_id,
                "labels": _as_json(labels) if isinstance(labels, list) else labels,
                "linked_issues": _as_json(linked_issues) if isinstance(linked_issues, list) else linked_issues,
                "raw_payload": _as_json(issue),
                "_loaded_at": loaded_at,
            }
            for field_name, column_name in JIRA_ISSUE_CUSTOM_FIELDS.items():
                field = custom_fields_by_name.get(field_name)
                field_id = field.get("id") if field else None
                record[column_name] = (
                    _jira_scalar_field_value(issue_fields.get(field_id))
                    if isinstance(field_id, str)
                    else None
                )

            issue_id = record["issue_id"]
            if not issue_id:
                issue_records_without_id.append(record)
                continue

            updated_at = _jira_issue_updated_at(issue)
            existing_record = issue_records.get(issue_id)
            if existing_record is not None:
                duplicate_issue_ids.add(str(issue_id))

            if existing_record is None or _is_newer_jira_issue(updated_at, existing_record[0]):
                issue_records[issue_id] = (updated_at, record)

        if remaining is not None:
            remaining -= len(issues)

        next_page_token = payload.get("nextPageToken")
        if not issues or not next_page_token or payload.get("isLast"):
            break

    if duplicate_issue_ids:
        duplicate_count = extracted_count - len(issue_records) - len(issue_records_without_id)
        _log_info(
            "Deduplicated Jira issues within one extraction: "
            f"{len(duplicate_issue_ids)} issue ids, {duplicate_count} duplicate rows skipped"
        )

    for _, record in issue_records.values():
        yield record

    for record in issue_records_without_id:
        yield record


@dlt.resource(name="raw_tempo_accounts", write_disposition="replace")
def tempo_accounts() -> Iterator[dict[str, Any]]:
    session = _tempo_session()
    url = _tempo_accounts_url()
    params: dict[str, Any] | None = {"limit": 500}
    loaded_at = _loaded_at()
    page_number = 0
    extracted_count = 0

    while url:
        page_number += 1
        _log_info(f"Fetching Tempo accounts page {page_number}")
        response = _request_with_retries(
            session,
            "GET",
            url,
            "Tempo accounts request",
            params=params,
            timeout=60,
        )
        payload = response.json()

        if isinstance(payload, list):
            accounts = payload
            next_url = None
        else:
            accounts = payload.get("results") or payload.get("accounts") or []
            metadata = payload.get("metadata") or {}
            next_url = metadata.get("next") or payload.get("next")

        if not isinstance(accounts, list):
            raise RuntimeError("Tempo accounts response does not contain an account list")

        extracted_count += len(accounts)
        _log_info(f"Fetched Tempo accounts page {page_number}: {len(accounts)} rows, total={extracted_count}")

        for account in accounts:
            yield {
                "account_id": account.get("id"),
                "account_key": account.get("key"),
                "account_name": account.get("name"),
                "raw_payload": _as_json(account),
                "_loaded_at": loaded_at,
            }

        url = next_url
        params = None


@dlt.source(name="jira_tempo")
def jira_tempo_source():
    return [jira_fields(), jira_issues(), tempo_accounts()]


@dlt.source(name="jira")
def jira_source():
    return [jira_fields(), jira_issues()]


@dlt.source(name="tempo")
def tempo_source():
    return [tempo_accounts()]


def _run_source(
    source: Any,
    pipeline_name: str,
    required_env: tuple[str, ...],
    logger: Any | None = None,
) -> Any:
    _set_run_logger(logger)
    _validate_required_env(required_env + REQUIRED_DATABASE_ENV)
    connection_string = _build_dlt_connection_string()
    dataset_name = _required_env("MARIADB_DATABASE")
    pipeline = dlt.pipeline(
        pipeline_name=pipeline_name,
        destination=dlt_sqlalchemy(
            credentials=connection_string,
            dataset_name=dataset_name,
            enable_dataset_name_normalization=False,
        ),
    )
    return pipeline.run(source)


def run_jira_tempo_ingestion(logger: Any | None = None) -> Any:
    return _run_source(
        jira_tempo_source(),
        "jira_tempo_raw",
        REQUIRED_JIRA_ENV + REQUIRED_TEMPO_ENV,
        logger,
    )


def run_jira_ingestion(logger: Any | None = None) -> Any:
    return _run_source(jira_source(), "jira_raw", REQUIRED_JIRA_ENV, logger)


def run_tempo_ingestion(logger: Any | None = None) -> Any:
    return _run_source(tempo_source(), "tempo_raw", REQUIRED_TEMPO_ENV, logger)


def _state_table_qualified_name() -> str:
    return f"`{_required_env('MARIADB_DATABASE')}`.`{REF_MAPPING_STATE_TABLE}`"


def _ensure_ref_mapping_state_table(engine: sa.Engine) -> None:
    ddl = f"""
    CREATE TABLE IF NOT EXISTS {_state_table_qualified_name()} (
        mapping_path_hash CHAR(64) NOT NULL PRIMARY KEY,
        mapping_path VARCHAR(1024) NOT NULL,
        source_path VARCHAR(1024) NOT NULL,
        target_table VARCHAR(255) NOT NULL,
        source_fingerprint VARCHAR(1024) NOT NULL,
        mapping_fingerprint CHAR(64) NOT NULL,
        loaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        rows_loaded INT NOT NULL DEFAULT 0
    )
    """
    with engine.begin() as conn:
        conn.execute(sa.text(ddl))


def _table_exists(engine: sa.Engine, table_name: str) -> bool:
    sql = """
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = :database_name
      AND table_name = :table_name
    LIMIT 1
    """
    with engine.connect() as conn:
        row = conn.execute(
            sa.text(sql),
            {"database_name": _required_env("MARIADB_DATABASE"), "table_name": table_name},
        ).first()
    return row is not None


def _get_state_row(engine: sa.Engine, mapping_path: str) -> dict[str, Any] | None:
    mapping_path_hash = _mapping_path_hash(mapping_path)
    sql = f"""
    SELECT source_fingerprint, mapping_fingerprint
    FROM {_state_table_qualified_name()}
    WHERE mapping_path_hash = :mapping_path_hash
    """
    with engine.connect() as conn:
        row = conn.execute(sa.text(sql), {"mapping_path_hash": mapping_path_hash}).mappings().first()
    return dict(row) if row else None


def _upsert_state_row(
    engine: sa.Engine,
    mapping_path: str,
    source_path: str,
    target_table: str,
    source_fingerprint: str,
    mapping_fingerprint: str,
    rows_loaded: int,
) -> None:
    mapping_path_hash = _mapping_path_hash(mapping_path)
    sql = f"""
    INSERT INTO {_state_table_qualified_name()} (
        mapping_path_hash, mapping_path, source_path, target_table, source_fingerprint, mapping_fingerprint, rows_loaded
    )
    VALUES (
        :mapping_path_hash, :mapping_path, :source_path, :target_table, :source_fingerprint, :mapping_fingerprint, :rows_loaded
    )
    ON DUPLICATE KEY UPDATE
        mapping_path = VALUES(mapping_path),
        source_path = VALUES(source_path),
        target_table = VALUES(target_table),
        source_fingerprint = VALUES(source_fingerprint),
        mapping_fingerprint = VALUES(mapping_fingerprint),
        rows_loaded = VALUES(rows_loaded),
        loaded_at = CURRENT_TIMESTAMP
    """
    with engine.begin() as conn:
        conn.execute(
            sa.text(sql),
            {
                "mapping_path_hash": mapping_path_hash,
                "mapping_path": mapping_path,
                "source_path": source_path,
                "target_table": target_table,
                "source_fingerprint": source_fingerprint,
                "mapping_fingerprint": mapping_fingerprint,
                "rows_loaded": rows_loaded,
            },
        )


def run_ref_excel_ingestion(mapping_config_path: str | None = None, logger: Any | None = None) -> Any:
    _set_run_logger(logger)
    config_path = _resolve_mapping_config_path(
        mapping_config_path or os.getenv("REF_MAPPING_CONFIG", DEFAULT_REF_MAPPING_CONFIG)
    )
    _validate_required_env(REQUIRED_DATABASE_ENV)
    mapping_paths = _list_ref_mapping_paths(config_path)
    connection_string = _build_dlt_connection_string()
    engine = sa.create_engine(connection_string)
    _ensure_ref_mapping_state_table(engine)

    summary: list[dict[str, Any]] = []
    for mapping_path in mapping_paths:
        mapping = _load_ref_mapping_config(mapping_path)
        source = mapping.get("source") or {}
        target = mapping.get("target") or {}
        source_file = source.get("file")
        target_table = target.get("table")
        if not isinstance(source_file, str):
            raise RuntimeError(f"Mapping source.file is required in {mapping_path}")
        if not isinstance(target_table, str) or not target_table:
            raise RuntimeError(f"Mapping target.table is required in {mapping_path}")
        resolved_source = _resolve_source_path(mapping_path, source_file)
        mapping.setdefault("source", {})["file"] = resolved_source
        mapping_hash = _mapping_fingerprint(mapping)
        source_hash = _source_fingerprint(resolved_source)
        state_row = _get_state_row(engine, mapping_path)
        unchanged = (
            state_row is not None
            and state_row.get("source_fingerprint") == source_hash
            and state_row.get("mapping_fingerprint") == mapping_hash
            and _table_exists(engine, target_table)
        )
        if unchanged:
            _log_info(f"Skipping unchanged mapping: {mapping_path} -> {target_table}")
            summary.append(
                {
                    "mapping": mapping_path,
                    "source": resolved_source,
                    "table": target_table,
                    "status": "skipped",
                    "rows": 0,
                }
            )
            continue

        _log_info(f"Loading mapping: {mapping_path} -> {target_table}")
        rows, _, _ = _mapped_excel_rows(mapping)
        write_disposition = "replace" if (mapping.get("load_options") or {}).get("truncate_before_load", True) else "append"
        load_info = _run_source(
            _ref_excel_source_from_records(rows, target_table, write_disposition),
            f"ref_excel_{target_table}",
            tuple(),
            logger,
        )
        _upsert_state_row(
            engine,
            mapping_path=mapping_path,
            source_path=resolved_source,
            target_table=target_table,
            source_fingerprint=source_hash,
            mapping_fingerprint=mapping_hash,
            rows_loaded=len(rows),
        )
        summary.append(
            {
                "mapping": mapping_path,
                "source": resolved_source,
                "table": target_table,
                "status": "loaded",
                "rows": len(rows),
                "load_info": str(load_info),
            }
        )

    for item in summary:
        _log_info(
            "Excel mapping result | "
            f"status={item.get('status')} | "
            f"table={item.get('table')} | "
            f"source={item.get('source')} | "
            f"mapping={item.get('mapping')} | "
            f"rows={item.get('rows')}"
        )
    _log_info(f"Ref Excel ingestion completed: {len(summary)} mapping(s) evaluated")
    return summary
