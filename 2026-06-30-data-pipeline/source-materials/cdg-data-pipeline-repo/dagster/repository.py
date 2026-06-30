import os
import re
from pathlib import Path

import yaml
from dagster import Definitions, In, Nothing, OpExecutionContext, job, multiprocess_executor, op

from ingestion import (
    DEFAULT_REF_MAPPING_CONFIG,
    DEFAULT_REF_MAPPING_DIR,
    run_sql_transformations,
    run_jira_ingestion,
    run_jira_tempo_ingestion,
    run_ref_excel_ingestion,
    run_tempo_ingestion,
)


@op
def run_jira_ingestion_op(context: OpExecutionContext):
    load_info = run_jira_ingestion(logger=context.log)
    context.log.info(str(load_info))


@job
def jira_ingestion_job():
    run_jira_ingestion_op()


@op
def run_tempo_ingestion_op(context: OpExecutionContext):
    load_info = run_tempo_ingestion(logger=context.log)
    context.log.info(str(load_info))


@job
def tempo_ingestion_job():
    run_tempo_ingestion_op()


@op
def run_jira_tempo_ingestion_op(context: OpExecutionContext):
    load_info = run_jira_tempo_ingestion(logger=context.log)
    context.log.info(str(load_info))


@op(ins={"after_ingestion": In(Nothing)})
def run_sql_transformations_op(context: OpExecutionContext):
    executed_files = run_sql_transformations(logger=context.log)
    context.log.info(f"Applied SQL transformation files: {executed_files}")


@job
def jira_tempo_ingestion_job():
    run_jira_tempo_ingestion_op()


@job
def sql_transformations_job():
    run_sql_transformations_op()


@job
def jira_tempo_mart_job():
    run_sql_transformations_op(run_jira_tempo_ingestion_op())


@op(config_schema={"mapping_file": str})
def run_excel_ingestion_by_file_op(context: OpExecutionContext):
    mapping_file = context.op_config["mapping_file"]
    load_info = run_ref_excel_ingestion(mapping_config_path=mapping_file, logger=context.log)
    context.log.info(str(load_info))


@job
def excel_ingestion_by_file_job():
    run_excel_ingestion_by_file_op()


def _resolve_mapping_paths_for_jobs() -> list[str]:
    config_path = os.getenv("REF_MAPPING_CONFIG", DEFAULT_REF_MAPPING_CONFIG)
    if config_path.startswith("s3://"):
        return [config_path]

    base_path = Path(config_path)
    if not base_path.is_absolute():
        cwd_path = (Path.cwd() / base_path).resolve()
        if cwd_path.exists():
            base_path = cwd_path
        else:
            mapping_dir = Path(os.getenv("REF_MAPPING_DIR", DEFAULT_REF_MAPPING_DIR))
            if not mapping_dir.is_absolute():
                mapping_dir = (Path.cwd() / mapping_dir).resolve()
            base_path = (mapping_dir / base_path).resolve()
    if not base_path.exists():
        return [str(base_path)]

    config = yaml.safe_load(base_path.read_text(encoding="utf-8"))
    if isinstance(config, dict) and isinstance(config.get("mappings"), list):
        mapping_paths: list[str] = []
        for item in config["mappings"]:
            if not isinstance(item, str):
                continue
            if item.startswith("s3://"):
                mapping_paths.append(item)
                continue
            item_path = Path(item)
            if item_path.is_absolute():
                mapping_paths.append(str(item_path))
                continue

            # Prefer project-root relative entries (e.g. input/config/foo.yaml),
            # then fallback to index-file relative entries.
            cwd_item_path = (Path.cwd() / item_path).resolve()
            if cwd_item_path.exists():
                mapping_paths.append(str(cwd_item_path))
                continue

            mapping_paths.append(str((base_path.parent / item_path).resolve()))
        return mapping_paths or [str(base_path)]

    return [str(base_path)]


def _slug_from_mapping_path(mapping_path: str, used: set[str]) -> str:
    stem = Path(mapping_path).stem
    if stem.endswith("_mapping"):
        stem = stem[: -len("_mapping")]
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", stem).strip("_").lower()
    if not slug:
        slug = "mapping"
    original = slug
    suffix = 2
    while slug in used:
        slug = f"{original}_{suffix}"
        suffix += 1
    used.add(slug)
    return slug


def _build_excel_mapping_op(mapping_path: str, slug: str):
    op_name = f"run_excel_ingestion_{slug}_op"

    @op(name=op_name)
    def _run_mapping_op(context: OpExecutionContext):
        load_info = run_ref_excel_ingestion(mapping_config_path=mapping_path, logger=context.log)
        context.log.info(str(load_info))

    return _run_mapping_op


def _build_excel_ops() -> list:
    mapping_paths = _resolve_mapping_paths_for_jobs()
    used_slugs: set[str] = set()
    ops: list = []
    for mapping_path in mapping_paths:
        slug = _slug_from_mapping_path(mapping_path, used_slugs)
        mapping_op = _build_excel_mapping_op(mapping_path, slug)
        ops.append(mapping_op)
    return ops


EXCEL_MAPPING_OPS = _build_excel_ops()


@job(name="excel_ingestion_all_job", executor_def=multiprocess_executor)
def excel_ingestion_all_job():
    for mapping_op in EXCEL_MAPPING_OPS:
        mapping_op()


defs = Definitions(
    jobs=[
        jira_ingestion_job,
        tempo_ingestion_job,
        jira_tempo_ingestion_job,
        sql_transformations_job,
        jira_tempo_mart_job,
        excel_ingestion_by_file_job,
        excel_ingestion_all_job,
    ]
)
