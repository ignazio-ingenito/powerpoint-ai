# CDG Data Pipeline

Pipeline dati per integrare Jira, Tempo e file Excel in MariaDB, orchestrata con Dagster.

## Scopo del progetto

Questo repository serve a:

- acquisire dati operativi da Jira e Tempo
- acquisire file Excel di mapping/reference
- caricare i dati nel database business (`p-cdgapp`) con convenzioni di naming coerenti
- preparare il terreno per trasformazioni dbt (`stg_`, `mart_`)

In sintesi: ingestion affidabile e tracciabile nel layer raw/ref, con orchestrazione centralizzata.

## Architettura (alto livello)

- **Dagster**: orchestrazione job e logging run
- **dlt**: estrazione + load verso MariaDB
- **MariaDB remoto**:
  - `p-cdgapp` -> dati business + metadati tecnici pipeline
  - `p-cdgapp-metabase` -> metadati Metabase
  - `p_cdgapp_nocodb` -> metadati NocoDB
- **Metabase / NocoDB**: UI analytics e no-code app (deploy ECS)

## Convenzioni tabelle

Nel DB `p-cdgapp`:

- `raw_*` sorgenti grezze API / file
- `ref_*` tabelle di riferimento
- `stg_*` normalizzazione (dbt)
- `mart_*` modelli business (dbt)
- `_dlt_*` tabelle tecniche dlt (eccezione tecnica)

## Job Dagster disponibili

- `jira_ingestion_job`
- `tempo_ingestion_job`
- `jira_tempo_ingestion_job`
- `sql_transformations_job`
- `jira_tempo_mart_job`
- `excel_ingestion_by_file_job`
- `excel_ingestion_all_job`

### Jira, Tempo e mart

- `jira_tempo_ingestion_job`: aggiorna solo il layer raw Jira/Tempo.
- `sql_transformations_job`: riesegue solo gli script SQL di trasformazione
  `init/002_stg_jira_views.sql` e `init/003_tempo_issue_account_mart.sql`.
  Usarlo quando l'ingestion è già stata eseguita e serve solo aggiornare
  `stg_*`/`mart_*`.
- `jira_tempo_mart_job`: esegue ingestion Jira/Tempo e poi refresh delle view
  `stg_*`/`mart_*`.

Il mart `mart_fact_issue_accounts` espone i campi Jira operativi e Service Desk
richiesti per reporting, inclusi `organizations`, `linked_issues`,
`resolved_at`, campi di categoria/processo/prodotto, riferimenti ODA/SOW,
campi BPO, satisfaction e SLA. Quando si aggiungono nuovi field Jira, serve
rilanciare l'ingestion Jira/Tempo prima del refresh SQL, così `raw_jira_issues`
viene ricreato con le nuove colonne.

### Excel ingestion

- `excel_ingestion_by_file_job`: esegue un solo mapping (`mapping_file` in run config)
- `excel_ingestion_all_job`: esegue tutti i mapping definiti in `REF_MAPPING_CONFIG`

Esempio run config:

```yaml
ops:
  run_excel_ingestion_by_file_op:
    config:
      mapping_file: account_category_mapping.yaml
```

## Rilevazione file cambiati (Excel)

La pipeline ricarica un mapping solo se cambia qualcosa:

- fingerprint file sorgente (locale: size/mtime, S3: ETag/size/lastModified)
- fingerprint del contenuto YAML di mapping
- presenza tabella target

Stato salvato in tabella: `dlt_ref_file_state`.

## Configurazione

Partire da `.env.example` e valorizzare almeno:

- `MARIADB_HOST`
- `MARIADB_PORT`
- `MARIADB_DATABASE`
- `MARIADB_USER`
- `MARIADB_PASSWORD`
- `DAGSTER_MYSQL_SSL_DISABLED` (default: `true`; set `false` only when the MariaDB endpoint requires TLS)
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `TEMPO_API_TOKEN`
- `JIRA_ISSUE_JQL`
- `REF_MAPPING_CONFIG` (default: `input/config/xls_mappings_index.yaml`)
- `REF_MAPPING_DIR` (default: `input/config`)

If the MariaDB password contains URL-reserved characters, set `DAGSTER_MYSQL_URL`
explicitly with URL-encoded credentials instead of relying on the Compose default.

## Avvio locale (Dagster)

```bash
docker compose build dagster-webserver dagster-daemon
docker compose up -d dagster-webserver dagster-daemon
```

UI Dagster: `http://localhost:3001`

## Avvio locale Metabase

Valorizzare in `.env` anche `METABASE_ENCRYPTION_SECRET_KEY` con la stessa
chiave del servizio Metabase deployato, poi avviare:

```bash
docker compose -f docker-compose.metabase.yaml --env-file .env up -d
```

UI Metabase: `http://localhost:3000`

## Deploy ECS

Configurazioni deploy:

- `deploy/ecs/metabase`
- `deploy/ecs/nocodb`

Workflow CI/CD:

- `.github/workflows/deploy-metabase-ecs.yml`
- `.github/workflows/deploy-nocodb-ecs.yml`

## Documentazione utile

- `docs/index.md`
- `docs/architecture/data-layer-architecture.md`
- `docs/specs/refactor-foundations.md`
- `docs/specs/jira-tempo-pipeline.md`
- `docs/status/refactor-implementation-status.md`
- `docs/legacy/index.md`

## Pubblicazione su Confluence

La pubblicazione su Confluence non fa parte del set documentale da pubblicare. Le istruzioni operative restano nel repository.

Set attuale:

- spazio Confluence: `OPI`
- lingua pubblicata: italiano
- documenti sorgente per la pubblicazione:
  - `docs/index.md`
  - `docs/specs/refactor-foundations.md`
  - `docs/status/refactor-implementation-status.md`
  - `docs/legacy/*.md`
- manifest: `scripts/confluence_publish.json`
- script: `scripts/publish_confluence.py`

Variabili richieste:

- `CONFLUENCE_BASE_URL`
- `CONFLUENCE_EMAIL`
- `CONFLUENCE_API_TOKEN`

Variabile opzionale per Mermaid:

- `MERMAID_RENDER_CMD`
  - comando completo con placeholder `{input}` e `{output}`
  - esempio: `MERMAID_RENDER_CMD="mmdc -i {input} -o {output} -b transparent"`
- `MERMAID_IMAGE_WIDTH`
  - larghezza di visualizzazione in Confluence per i diagrammi Mermaid renderizzati
  - default: `1400`

Esecuzione con `uv`:

```bash
uv run --env-file .env python3 scripts/publish_confluence.py --dry-run
uv run --env-file .env python3 scripts/publish_confluence.py
```

Note operative:

- il publisher crea o aggiorna pagine, non cartelle Confluence
- i documenti nel repository sono il set pubblicabile
- il manifest in `scripts/confluence_publish.json` definisce l'albero delle pagine
- i link Markdown locali tra pagine pubblicate vengono convertiti in link pagina Confluence dal publisher
- i blocchi Mermaid vengono pubblicati come immagini SVG allegate quando è disponibile un renderer; in caso contrario il publisher mantiene il blocco code e stampa un warning

## File storico

Il README precedente è stato preservato in:

- `README.legacy.md`
