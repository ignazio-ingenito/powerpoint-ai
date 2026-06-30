# Data Layer Architecture

## Overview

Questa piattaforma implementa una pipeline dati moderna basata su:

* Ingestion (dlt)
* Storage (MariaDB)
* Modeling (dbt)
* Orchestrazione (Dagster)
* BI (Metabase)
* Data management (NocoDB)

---

## Data Layer Architecture

Struttura logica a 4 layer. Nell'istanza MariaDB disponibile esiste un solo database, quindi i layer sono rappresentati da prefissi tabella:

* `raw_`
* `ref_`
* `stg_`
* `mart_`

### raw

Dati grezzi dalle sorgenti (Jira, DB, file).

* immutabili
* auditabili

### ref

Tabelle di riferimento:

* mapping
* domini
* override

Gestite via NocoDB.

### stg

Normalizzazione tecnica:

* tipi coerenti
* rename colonne
* parsing JSON

### mart

Layer finale:

* KPI
* join business
* dataset per BI

---

## Data Flow

```text
sorgenti -> dlt in Dagster -> raw -> dbt stg -> dbt mart
                                       ^
                                       ref
```

Regola architetturale:

* `dlt` gestisce solo ingestion/API verso `raw`
* `dbt` gestisce normalizzazione, join, controlli e dataset `mart`

Stato implementativo attuale: le prime trasformazioni `stg_jira_issues`,
`stg_tempo_accounts` e `mart_fact_issue_accounts` sono ancora mantenute come
script SQL in `init/002_stg_jira_views.sql` e
`init/003_tempo_issue_account_mart.sql`. Dagster può eseguirle con
`sql_transformations_job` senza rilanciare l'ingestion, oppure con
`jira_tempo_mart_job` dopo l'ingestion Jira/Tempo. La migrazione a modelli dbt
resta il target architetturale per versioning, lineage e test di qualità.

---

## Naming Convention

### Regole generali

* `snake_case`
* inglese
* nomi espliciti

### raw

`raw_<source>_<entity>`  
es: `raw_jira_issues`

### ref

`ref_<domain>_<type>`  
es: `ref_status_mapping`

### stg

`stg_<source>_<entity>`  
es: `stg_jira_issues`

### mart

`mart_<type>_<entity>`

Tipi:

* `fact_`
* `dim_`
* `agg_`
* `rpt_`

es:

* `mart_fact_issues`
* `mart_dim_projects`

---

## Column Naming

### ID

`<entity>_id`

### Date

`<event>_at` (timestamp)  
`<event>_date` (date)

### Boolean

`is_<flag>`  
`has_<flag>`

### Metriche

`<name>_<unit>`  
es: `lead_time_days`

---

## Versioning

Usare:

`<table>_v2` solo se breaking change.

Preferire:

* git
* dbt versioning

---

## Esempio Jira

### raw

`raw_jira_issues`

### ref

`ref_status_mapping`

### stg

`stg_jira_issues`

### mart

`mart_fact_issues`

---

## Best Practices

* Non usare raw per BI
* Non mettere logica business in stg
* Non usare ref come dump
* Esporre solo mart a Metabase

---

## Stack Tecnologico

* dlt (ingestion)
* MariaDB (storage)
* dbt (transform)
* Dagster (orchestrazione)
* Metabase (BI)
* NocoDB (data management)

Nota: `dlt` non richiede un servizio dedicato. Viene eseguito come libreria Python dentro Dagster e scrive nel database logico `raw` di MariaDB.

La logica di importazione custom deve restare in `dlt`:

* autenticazione verso sorgenti
* gestione della comunicazione con le sorgenti
* finestre incrementali
* selezione esplicita dei dataset da caricare

La logica di trasformazione deve restare in `dbt`:

* parsing e normalizzazione del raw
* join tra dataset
* controlli qualità
* esposizione dei modelli `mart`

---

## Obiettivo

Separare chiaramente:

* ingestione
* trasformazione
* logica business
* consumo dati

Per ottenere:

* pipeline robuste
* manutenzione semplice
* scalabilità
