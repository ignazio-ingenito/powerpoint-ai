# Jira → Tempo Pipeline Specification (v2)

## Riferimento

Questo documento estende e completa:

- [Data Layer Architecture](../architecture/data-layer-architecture.md)

Questo documento serve come **contesto persistente** per le prossime chat e definisce:

- obiettivo funzionale della pipeline
- traduzione della logica legacy PowerShell nel nuovo stack
- convenzioni di naming e layering
- limiti architetturali
- anti-pattern da evitare
- dataset finali attesi


## Obiettivo Funzionale

L'obiettivo della pipeline **non** è semplicemente importare Jira.

L'obiettivo reale è costruire un dataset affidabile che permetta di associare:

**Issue Jira → Account Tempo**

Questa è la logica di business principale ereditata dallo script PowerShell legacy.

Il comportamento atteso è:

1. identificare il custom field Jira che rappresenta l'`Account`
2. recuperare l'anagrafica completa degli account Tempo
3. estrarre le issue Jira rilevanti
4. estrarre da ogni issue l'account associato
5. fare il join tra issue e account Tempo
6. produrre un dataset BI-ready per reporting e analisi


## Stack Tecnologico

- **dlt** → ingestion
- **MariaDB** → storage
- **dbt** → trasformazioni
- **Dagster** → orchestrazione
- **Metabase** → BI
- **NocoDB** → mapping manuali e reference tables

### Scelta del componente di ingestion

Il componente di ingestion scelto per questa pipeline è **dlt**.

La scelta è guidata dal vincolo principale del progetto: preservare la logica di importazione già definita, inclusi:

- recupero dinamico del custom field Jira `Account`
- recupero completo dell'anagrafica account Tempo
- JQL/finestra temporale configurabile per evitare full history iniziale
- caricamento separato di issue Jira, campi Jira e account Tempo
- scrittura tracciabile nel layer `raw`

`dlt` è compatibile con questi vincoli perché permette di implementare sorgenti REST/API custom in Python, gestire lo stato di caricamento e scrivere su MariaDB tramite destinazione SQLAlchemy/MySQL. Se la sorgente o il metodo scelto richiede paginazione, questa resta una responsabilità dell'ingestion e non di dbt. Inoltre `dlt` si integra naturalmente con Dagster, che resta il componente di orchestrazione della piattaforma.

### Confine tra `dlt` e `dbt`

Assunzione architetturale per il proseguo:

- `dlt` contiene la logica di importazione custom necessaria a parlare con Jira e Tempo
- `dbt` contiene la logica di trasformazione, normalizzazione, join e produzione dei dataset analitici

#### Responsabilità di `dlt`

- autenticazione verso Jira e Tempo
- chiamate API REST
- gestione della paginazione solo se richiesta dalla sorgente o dal metodo scelto
- gestione retry/rate limit se necessaria
- JQL/finestra temporale configurabile
- recupero dinamico dei campi Jira
- caricamento separato di `raw_jira_issues`, `raw_jira_fields` e `raw_tempo_accounts`
- gestione dello stato di caricamento/incremental cursor dove applicabile
- aggiunta di metadati tecnici di caricamento, ad esempio timestamp di load

`dlt` non deve costruire il dataset finale issue-account e non deve contenere join business.

#### Responsabilità di `dbt`

- parsing e normalizzazione del payload `raw`
- estrazione tecnica dell'`account_id` dalle issue Jira
- costruzione dei modelli `stg`
- join tra issue Jira e account Tempo
- produzione di `mart_fact_issue_accounts`
- test qualità e flag di controllo, incluso `account_found_flag`

`dbt` non deve chiamare API esterne, gestire dettagli di comunicazione con le sorgenti o compensare una ingestion troppo ampia.

## Data Flow

```text
Jira / Tempo -> dlt in Dagster -> raw -> stg -> mart -> Metabase
                                                ^
                                                ref
```


## Traduzione della Logica Legacy PowerShell

Lo script legacy PowerShell implementava implicitamente questa logica:

### Step 1 — Recupero dinamico del custom field Jira `Account`

Lo script **non** hardcodava l'ID del custom field, ma lo ricavava interrogando:

- `GET /rest/api/3/field`

e filtrando per:

- `field.name == "Account"`

### Decisione architetturale nel nuovo stack

Questa logica va **preservata**.

Il sistema non deve assumere che il custom field sia sempre, ad esempio, `customfield_12345`.

### Regola

- l'identificazione dell'ID del campo `Account` deve essere dinamica
- il mapping `field_name -> field_id` deve essere tracciabile
- se il campo non viene trovato, la pipeline deve fallire esplicitamente

### Possibili implementazioni nel nuovo stack

Opzioni accettabili:

1. estrazione diretta tramite sorgente `dlt` / raw payload se il campo è già presente
2. tabella tecnica dedicata:
   - `raw_jira_fields`
   - oppure `stg_jira_fields`
3. logica parametrica in dbt solo a partire dai dati già caricati in `raw_jira_fields`

### Vincolo

Il progetto **non deve dipendere da un ID hardcodato del campo Account**.

dbt non deve chiamare l'API Jira per scoprire il campo. La chiamata API resta responsabilità di `dlt`/Dagster.


### Step 2 — Recupero account Tempo

Lo script chiamava l'API Tempo Accounts per costruire un'anagrafica account:

- endpoint concettuale: `Tempo Accounts API`
- campi usati:
  - `id`
  - `key`

La paginazione non è un vincolo architetturale. È un dettaglio tecnico da gestire solo se richiesto dall'API o dalla modalità di ingestion scelta.

### Obiettivo funzionale

Costruire una tabella master account che rappresenti il riferimento ufficiale degli account Tempo.

### Output logico atteso

- `account_id`
- `account_key`
- `account_name` (se disponibile)
- eventuali attributi descrittivi aggiuntivi

### Decisione nel nuovo stack

Gli account Tempo devono essere ingestiti come dataset separato e mantenuti indipendenti dalle issue Jira.


### Step 3 — Estrazione issue Jira con perimetro controllato

Lo script legacy usava una JQL con questa logica:

- include tutte le issue **non Done**
- include le issue **Done** solo da una certa finestra temporale

Forma logica:

- issue aperte / attive → sempre incluse
- issue chiuse → incluse solo se relativamente recenti

### Significato business

Questa scelta evita:

- full history iniziale troppo pesante
- importazione di issue chiuse vecchie e irrilevanti
- costi inutili di ingestione

### Regola da mantenere

La pipeline **non deve** scaricare indiscriminatamente tutto lo storico Jira.

Quando `JIRA_MAX_RESULTS` è vuoto, la pipeline deve scaricare **tutte le issue comprese nella JQL configurata**, non tutte le issue dell'istanza Jira. Il limite tecnico deve quindi rimanere separato dal perimetro funzionale:

- `JIRA_ISSUE_JQL` definisce quali issue sono nel perimetro business
- `JIRA_MAX_RESULTS` è solo un limite tecnico di test/debug
- in produzione `JIRA_MAX_RESULTS` può essere vuoto solo se la JQL è già sufficientemente vincolata

### Regola operativa

La JQL deve essere:

- esplicita
- configurabile
- documentata
- coerente con la logica legacy:
  - issue non Done sempre incluse
  - issue Done incluse solo entro una finestra temporale concordata

Esempio concettuale:

```jql
statusCategory != Done OR resolved >= -180d
```

La forma esatta può cambiare in base ai campi Jira disponibili, ma deve mantenere questo principio.

### Anti-pattern

Non usare come JQL ordinaria:

```jql
project IS NOT EMPTY ORDER BY updated DESC
```

Questa JQL è utile solo per prove tecniche molto controllate con `JIRA_MAX_RESULTS` valorizzato. Con `JIRA_MAX_RESULTS` vuoto equivale a uno scarico troppo ampio rispetto alla specifica.

### Nota

La JQL legacy va trattata come **baseline**, non come verità immutabile.

Va mantenuto il principio, non la stringa hardcodata.


### Step 4 — Estrazione del riferimento account dalla issue Jira

Per ogni issue, lo script leggeva:

- `issue.id`
- `issue.key`
- `issue.fields[account_field_id].id`

Quindi il dato realmente usato come chiave di join non era il `key` account, ma l'`id` dell'account associato alla issue.

### Regola da mantenere

Nel nuovo stack, il campo di join principale deve essere:

- `issue.account_id`
  join
- `tempo_accounts.account_id`

### Regola tecnica

- il join deve usare l'ID tecnico, non il codice descrittivo
- `account_key` e `account_name` sono attributi derivati, non chiavi primarie di join


### Step 5 — Join tra issue e account Tempo

Lo script legacy costruiva il mapping:

- issue
- account_id
- account_key

e produceva un output finale equivalente a:

- `issue_id`
- `issue_key`
- `account_id`
- `account_key`

### Regola da mantenere

Il nuovo stack deve produrre almeno un dataset finale equivalente a questo mapping.

### Dataset finale minimo richiesto

- `issue_id`
- `issue_key`
- `project_key`
- `account_id`
- `account_key`
- `account_name`
- `created_at`
- `updated_at`


## Disegno dei Layer

### RAW

Il layer `raw` contiene la copia fedele delle sorgenti.

Il caricamento nel layer `raw` è responsabilità di `dlt`, eseguito da Dagster.

Tabelle attese:

- `raw_jira_issues`
- `raw_jira_projects`
- `raw_jira_users`
- `raw_jira_fields` *(se necessario per custom fields)*
- `raw_tempo_accounts`

Regole:

- nessuna modifica manuale
- nessuna logica business
- nessuna join
- nessun uso diretto per dashboard


### REF

Il layer `ref` contiene mapping e correzioni controllate.

Tabelle possibili:

- `ref_account_mapping`
- `ref_team_mapping`
- `ref_project_mapping`
- `ref_account_override`

Uso ammesso:

- classificazioni business
- override controllati
- domini e mapping

Uso vietato:

- correzione diretta del raw
- dumping di dati temporanei
- sostituzione di trasformazioni che devono stare in `stg` o `mart`


### STG

Il layer `stg` contiene normalizzazione tecnica e preparazione dei dati.

#### `stg_jira_issues`

Responsabilità:

- estrazione del custom field account
- standardizzazione date e timestamp
- rename colonne
- gestione null
- pulizia tipi
- normalizzazione attributi tecnici

Output atteso minimo:

- `issue_id`
- `issue_key`
- `summary`
- `assignee`
- `reporter`
- `priority`
- `resolution`
- `labels`
- `linked_issues`
- `organizations`
- `project_key`
- `account_id`
- `resolved_at`
- `due_date`
- `attivita_su_db`
- `categoria`
- `categoria_sql`
- `comando_sql`
- `data_tk_axel`
- `data_stima_approvata`
- `impatto_incident`
- `kpi_breached`
- `oda_ordine_di_acquisto`
- `presa_in_carico`
- `processi`
- `prodotti`
- `satisfaction`
- `satisfaction_date`
- `sla_amco`
- `sla_ing`
- `sla_sb`
- `stima_approvata`
- `stima_intervento_ore`
- `priorita_cliente`
- `sla_ticket`
- `tempo_di_presa_in_carico`
- `service_desk_time`
- `tipo_attivita`
- `bpo_amco`
- `bpo_ampre`
- `bpo_jj_tatooine`
- `sow_statement_of_work`
- `data_presa_in_carico`
- `sla_kpi_presa_in_carico`
- `created_at`
- `updated_at`
- `status_name`
- `is_done`

#### `stg_tempo_accounts`

Responsabilità:

- pulizia dell'anagrafica account
- standardizzazione nomi chiave
- deduplica tecnica se necessaria

Output atteso minimo:

- `account_id`
- `account_key`
- `account_name`

#### `stg_jira_fields` *(opzionale ma consigliato se utile)*

Responsabilità:

- mappare campi Jira
- rendere rintracciabile il custom field `Account`

Output atteso minimo:

- `field_id`
- `field_name`
- `is_custom`
- `is_account_field`

### Regola importante per `stg`

`stg` deve contenere logica **tecnica**, non logica business pesante.


### MART

Il layer `mart` contiene dataset BI-ready.

#### Dataset minimo richiesto

- `mart_fact_issue_accounts`

Responsabilità:

- join issue ↔ account
- arricchimento dei dati
- esposizione per dashboard e reporting

Output atteso minimo:

- `issue_id`
- `issue_key`
- `summary`
- `assignee`
- `reporter`
- `priority`
- `resolution`
- `labels`
- `linked_issues`
- `organizations`
- `project_key`
- `account_id`
- `account_key`
- `account_name`
- `resolved_at`
- `due_date`
- `attivita_su_db`
- `categoria`
- `categoria_sql`
- `comando_sql`
- `data_tk_axel`
- `data_stima_approvata`
- `impatto_incident`
- `kpi_breached`
- `oda_ordine_di_acquisto`
- `presa_in_carico`
- `processi`
- `prodotti`
- `satisfaction`
- `satisfaction_date`
- `sla_amco`
- `sla_ing`
- `sla_sb`
- `stima_approvata`
- `stima_intervento_ore`
- `priorita_cliente`
- `sla_ticket`
- `tempo_di_presa_in_carico`
- `service_desk_time`
- `tipo_attivita`
- `bpo_amco`
- `bpo_ampre`
- `bpo_jj_tatooine`
- `sow_statement_of_work`
- `data_presa_in_carico`
- `sla_kpi_presa_in_carico`
- `created_at`
- `updated_at`
- `status_name`
- `is_done`
- `account_found_flag`

### Regole

- Metabase deve leggere principalmente da `mart`
- il dataset finale deve essere stabile e leggibile
- i nomi devono essere orientati all'uso analytics


## Logica di Join Ufficiale

Join principale:

```text
stg_jira_issues.account_id
    LEFT JOIN
stg_tempo_accounts.account_id
```

### Regole

- usare `LEFT JOIN`
- issue senza account → mantenute
- account non trovato → mantenuto il record issue con flag dedicato
- non eliminare righe per effetto di join mancanti

### Campo derivato obbligatorio

- `account_found_flag`

Valori attesi:

- `true` → account risolto correttamente
- `false` → account_id presente ma non trovato nel master Tempo
- opzionale distinzione per issue senza account assegnato


## Convenzioni di Naming

Le naming convention generali seguono quanto definito in:

- [Data Layer Architecture](../architecture/data-layer-architecture.md)

Riepilogo essenziale:

### Schemi

- `raw`
- `ref`
- `stg`
- `mart`

### Tabelle

- `raw_<source>_<entity>`
- `ref_<domain>_<type>`
- `stg_<source>_<entity>`
- `mart_<type>_<entity>`

### Tabelle previste per questa pipeline

- `raw_jira_issues`
- `raw_jira_projects`
- `raw_jira_users`
- `raw_jira_fields`
- `raw_tempo_accounts`

- `stg_jira_issues`
- `stg_jira_projects`
- `stg_jira_users`
- `stg_jira_fields`
- `stg_tempo_accounts`

- `mart_fact_issue_accounts`
- `mart_rpt_issue_account_overview` *(opzionale in una fase successiva)*

### Colonne

- ID: `<entity>_id`
- timestamp: `<event>_at`
- date: `<event>_date`
- boolean: `is_<flag>` oppure `has_<flag>`
- flag di controllo: `<name>_flag`


## Limiti e Vincoli Architetturali

### 1. Nessun hardcoding del custom field `Account`

Non è accettabile dipendere stabilmente da:

- `customfield_XXXXX`

La pipeline deve poter localizzare il campo in modo dinamico oppure avere un meccanismo tecnico tracciato per gestirlo.


### 2. Niente full history non filtrata

La prima ingestione deve essere limitata dal perimetro funzionale espresso in JQL.

Motivi:

- performance
- tempi di sync
- riduzione complessità iniziale
- verifica più rapida del modello dati

`JIRA_MAX_RESULTS` non è il meccanismo corretto per definire il perimetro business: serve solo per prove tecniche. Il controllo funzionale deve stare nella JQL.


### 3. Nessuna logica business in `raw`

`raw` è solo replica della sorgente.


### 4. Nessun utilizzo diretto di `raw` in Metabase

Metabase deve leggere `mart`, non `raw`.

Eccezioni eventuali:

- debugging tecnico
- analisi temporanee riservate a utenti tecnici


### 5. `ref` non sostituisce le trasformazioni

Le tabelle `ref` servono per:

- mapping
- override
- classificazioni

Non servono per:

- correggere a mano il raw
- compensare pipeline sbagliate
- introdurre logica di calcolo che deve stare nei modelli


### 6. La chiave di join ufficiale è `account_id`

Non usare come chiave primaria di matching:

- `account_key`
- `account_name`

Questi attributi sono descrittivi.


### 7. La pipeline deve preservare i casi problematici

Devono emergere chiaramente:

- issue senza account
- issue con account_id non risolto nel master Tempo
- campi account mancanti o non valorizzati

I dati sporchi non vanno nascosti.


## Anti-Pattern Vietati

- usare `raw` per dashboard
- mettere logica business in `stg`
- hardcodare il custom field `Account`
- usare loop applicativi per lookup massivi invece di join su DB
- usare `ref` come discarica di eccezioni
- scartare issue senza account senza tracciarle
- fare affidamento su output file CSV come layer strutturale permanente


## Performance e Qualità

### Performance

Nel nuovo stack la risoluzione issue → account deve avvenire via database, non via loop applicativo.

Quindi:

- sì a join SQL
- no a ricerche O(n²) in memoria come nello script PowerShell legacy

### Qualità dati minima attesa

Devono essere previsti test o controlli almeno per:

- `issue_id` non nullo
- `issue_key` non nullo
- unicità issue a livello del dataset finale
- tracciamento di issue senza account
- tracciamento di account non risolti


## Evoluzione Futura Prevista

Dopo la prima versione della pipeline, gli step successivi possibili sono:

- aggiunta `worklog`
- aggiunta `changelog`
- KPI come:
  - lead time
  - cycle time
  - aging
- arricchimenti con:
  - team
  - dominio
  - progetto
  - classificazioni manuali via `ref`


## Stato del Documento

- **Versione**: v1
- **Scopo**: baseline architetturale e funzionale della pipeline Jira → Tempo
- **Ruolo**: documento da usare come input per prossime chat e per la progettazione dbt / Dagster / dlt
