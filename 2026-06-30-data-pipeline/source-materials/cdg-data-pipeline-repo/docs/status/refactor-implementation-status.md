# Stato di Implementazione del Refactoring

Questo documento traccia lo stato operativo del refactoring della piattaforma dati.

Contiene:

- avanzamento già completato
- backlog operativo ordinato per priorità
- prossimi step tecnici
- configurazione attualmente rilevante

## Stato aggiornato

### Completato

- [x] Migrazione principale a MariaDB remoto per dati business (`p-cdgapp`)
- [x] Deploy ECS NocoDB (`cdg-nocodb`) con endpoint Express attivo
- [x] Deploy ECS Metabase (`cdg-metabase`) con endpoint Express attivo
- [x] Separazione DB applicativi: `p-cdgapp`, `p-cdgapp-metabase`, `p_cdgapp_nocodb`
- [x] Rimozione da docker-compose locale di MariaDB e Metabase
- [x] Ingestion Jira e Tempo su Dagster e dlt attiva (`raw_jira_fields`, `raw_jira_issues`, `raw_tempo_accounts`)
- [x] Validazione del campo Jira `Account` (`customfield_10101`)
- [x] Ingestion dei campi Jira operativi aggiuntivi (`assignee`, `reporter`, `priority`, `resolution`, `labels`, `due_date`, stime e priorità cliente)
- [x] Ingestion estesa ai campi Jira/Service Desk richiesti per il mart (`organizations`, `linked_issues`, `resolved_at`, categorie, processi/prodotti, ODA/SOW, BPO, satisfaction e SLA)
- [x] View `stg_jira_issues` aggiornata con i nuovi campi Jira
- [x] View `mart_fact_issue_accounts` aggiornata con i campi Jira operativi e Service Desk richiesti
- [x] Job Dagster `sql_transformations_job` per refresh solo SQL di `stg_*`/`mart_*`
- [x] Job Dagster `jira_tempo_mart_job` per ingestion Jira/Tempo più refresh SQL end-to-end
- [x] Ingestion Excel con mapping YAML, sia singolo sia da indice (`input/config/xls_mappings_index.yaml`)
- [x] Supporto per sorgenti Excel locali e su S3
- [x] Skip dei file invariati tramite tabella di stato `dlt_ref_file_state`
- [x] Job Dagster per Excel: `excel_ingestion_by_file_job`, `excel_ingestion_all_job`
- [x] Cleanup della configurazione legacy (`docs/resource_organization_mapping.yaml` rimosso)
- [x] Aggiornamento del mapping di default a `input/config/xls_mappings_index.yaml`

## Backlog operativo

### P1 - Bloccanti

- [ ] Verifica end-to-end di `excel_ingestion_all_job` dopo le ultime correzioni su path e normalizzazione header
- [ ] Conferma nei log per ogni mapping di `status`, `table`, `source`, `rows`
- [ ] Verifica dei permessi utente Dagster su `p-cdgapp` per `_dlt_*` e `dlt_ref_file_state`, evitando errori `1142`

### P2 - Importanti

- [ ] Definire una policy per `truncate_before_load` nei mapping, chiarendo quando usare `replace` e quando `append`
- [ ] Creare un runbook operativo per l'ingestion Excel con errori comuni e query diagnostiche
- [ ] Migrare le trasformazioni SQL attuali verso il primo set dbt: `stg_` per Jira, Tempo ed Excel, `ref_` e il primo `mart_`
- [ ] Aggiungere test dbt minimi: `not null`, `unique`, `referential`, `freshness`

### P3 - Miglioramenti

- [ ] Valutare l'esclusione dal batch `excel_ingestion_all_job` dei mapping non ancora business-ready
- [ ] Preparare l'hardening del deploy Dagster su ECS, con osservabilità e allineamento di secret ed env

## Prossimi step tecnici

- [ ] Riavviare Dagster locale
- [ ] Eseguire `docker compose up -d --build dagster-webserver dagster-daemon`
- [ ] Eseguire `sql_transformations_job` per aggiornare solo `stg_*`/`mart_*` dopo una ingestion già completata
- [ ] Eseguire `jira_tempo_mart_job` quando serve aggiornare raw Jira/Tempo e poi ricostruire le view SQL
- [ ] Eseguire `excel_ingestion_all_job`
- [ ] Validare output delle tabelle `raw_xls_*` e log finali per ogni file

## Configurazione attuale rilevante

Variabili principali:

```text
MARIADB_HOST
MARIADB_PORT
MARIADB_DATABASE
MARIADB_USER
MARIADB_PASSWORD
JIRA_BASE_URL
JIRA_EMAIL
JIRA_API_TOKEN
TEMPO_API_TOKEN
TEMPO_BASE_URL
JIRA_ISSUE_JQL
JIRA_MAX_RESULTS
JIRA_PAGE_SIZE
JIRA_REQUEST_TIMEOUT
REF_MAPPING_CONFIG
REF_MAPPING_DIR
```

Default Excel:

- `REF_MAPPING_CONFIG=input/config/xls_mappings_index.yaml`
- `REF_MAPPING_DIR=input/config`

Esempio di run config per `excel_ingestion_by_file_job`:

```yaml
ops:
  run_excel_ingestion_by_file_op:
    config:
      mapping_file: account_category_mapping.yaml
```
