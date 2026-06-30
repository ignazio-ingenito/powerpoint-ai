# Specifica di Migrazione da Dagster a dbt a Metabase

## Obiettivo

Sostituire la catena legacy Excel/Power Query/Power BI con uno stack manutenibile di tipo warehouse:

- Dagster per l'orchestrazione
- dlt/custom ingestion per l'acquisizione dei dati raw
- MariaDB come warehouse
- dbt per trasformazioni, test e semantic marts
- Metabase per il consumo BI

L'obiettivo non è solo tecnico. L'obiettivo è preservare gli output business oggi utilizzati in:

- `Output All (A+B).xlsx`
- `PQ Report ITOPS.xlsx`
- `Power Query Base Dati AM.xlsx`
- `Power Query Analisi Servizi.xlsx`
- `PQ Ricavi.xlsx`
- `PQ Costi ribaltati.xlsx`
- `PQ Integrazione ore e economics.xlsx`
- i report Power BI `Dashboard TXT Novigo_V2`

## Principi di design

### Preservare il significato business, non la struttura dei workbook

Nomi workbook come `A`, `B`, `E`, `Def`, `Controlli` non vanno copiati tali e quali nel warehouse. Devono essere tradotti in modelli dimensionali e fact chiari.

### Separare ingestion da logica business

Dagster/dlt deve fare solo:

- extraction
- landing nel raw
- cattura di metadati di base

dbt deve fare:

- normalizzazione
- join
- logica storica
- classificazioni
- KPI
- controlli QA

### Codificare i controlli come data test

Le tab dei controlli legacy devono diventare:

- test dbt
- audit models
- exception marts
- alert di freshness/volume in Dagster

### Rendere parametrizzati i processi mensili, non manuali

La pipeline legacy si basa su cambio manuale del periodo e refresh manuali dei workbook. Il nuovo design deve eseguire per periodo configurato o tramite logica incrementale automatica.

Il design target deve anche preservare le due modalità operative visibili nel processo legacy:

- run inframensili di controllo
- run di chiusura mensile storicizzati

Queste non vanno collassate in un unico pattern generico di refresh.

## Perimetro del warehouse target

## Layer raw

### API e sorgenti operative

Nuove raw table richieste:

- `raw_jira_fields`
- `raw_jira_issues`
- `raw_tempo_accounts`
- `raw_tempo_worklogs`
- `raw_jira_issue_additional_fields`
- `raw_cdgapp_account_wbs_bridge`
- `raw_axel_commesse`
- `raw_axel_ore`
- `raw_hr_organico`
- `raw_hr_timbrature`
- `raw_sap_wbs`
- `raw_sap_costi`
- `raw_sap_ricavi`
- `raw_sap_fatturato`
- `raw_sap_fatture`
- `raw_budget`
- `raw_contracts_sla_kpi`
- `raw_forecast_wcs`

### Sorgenti manuali / di riferimento

Queste dovrebbero essere caricate come `ref_*` oppure come landing raw Excel più ref models:

- `ref_issue_account_history`
- `ref_account_category`
- `ref_team_pm`
- `ref_it_ops_gruppi_assignee`
- `ref_period`
- `ref_gruppo_cliente`
- `ref_wbs_category`
- `ref_eccezioni_wbs_new_org`
- `ref_customers_organization`
- `ref_programmi_r_and_d`
- `ref_kpi_target`
- `ref_service_desk_projects`
- `ref_validita_raccordo`
- `ref_sintesi_storico_sd`

## Backlog Dagster immediato

### 1. Completare la copertura reference già parzialmente preparata

Decommentare e rendere operative queste mapping in `xls_mappings_index.yaml` una volta validate:

- `corrispondeza_validita_raccordo_mapping.yaml`
- `issue_e_account_mapping.yaml`
- `kpi_target_mapping.yaml`
- `sintesi_storico_sd_mapping.yaml`

Al momento mancano nel batch standard pur essendo importanti per la logica legacy.

### 2. Aggiungere l'ingestion dei worklog

Questo è il gap a più alto valore. Senza i worklog non esiste sostituzione per:

- `Report ore new`
- `A-Report ore new raggruppato`
- analytics mensile delle ore
- lineage storica issue-account
- logica di billing T&M

Target raccomandato:

- ingest dei worklog Tempo a grana dettagliata
- persistenza dei timestamp originali e dei timestamp di estrazione
- aggiunta di source month / accounting month
- supporto all'estrazione incrementale per timestamp di aggiornamento dove l'API lo consente

### 3. Aggiungere l'ingestion del bridge CDG APP

Il bridge account-to-WBS è una dipendenza business centrale. Non dovrebbe più essere una dipendenza solo Excel aggiornata manualmente.

### 4. Aggiungere ingestion SAP e Axel

Anche se la prima delivery si concentrasse su ore e reporting servizi, la parità economics con Power BI non è possibile senza:

- WBS
- costi
- ricavi
- billing/fatturato
- commesse / ore Axel

### 5. Aggiungere ingestion dell'anagrafica HR

Team, area, tipo risorsa, stato occupazionale e cessati sono tutti arricchimenti centrali nel processo legacy.

### 6. Aggiungere esplicitamente l'ingestion del budget

Il materiale di review identifica `Budget.xlsx` come input della dashboard. Il budget deve quindi essere modellato come dipendenza di ingestion e di mart di primo livello, non rimandato come enhancement opzionale.

## Architettura modelli dbt

## Modelli staging

### Staging Jira/Tempo

- `stg_jira_fields`
- `stg_jira_issues`
- `stg_tempo_accounts`
- `stg_tempo_worklogs`
- `stg_jira_issue_additional_fields`

Responsabilità:

- normalizzare i nomi colonna
- fare parsing del raw payload JSON
- esporre ID tecnici e chiavi business
- standardizzare date / status / campi account

### Staging SAP/Axel/HR

- `stg_sap_wbs`
- `stg_sap_costs`
- `stg_sap_revenues`
- `stg_sap_invoicing`
- `stg_axel_commesse`
- `stg_axel_hours`
- `stg_hr_resources`
- `stg_hr_attendance`

### Staging reference

- `stg_ref_issue_account_history`
- `stg_ref_account_category`
- `stg_ref_team_pm`
- `stg_ref_period`
- `stg_ref_wbs_category`
- `stg_ref_validita_raccordo`
- `stg_ref_gruppo_cliente`
- `stg_ref_eccezioni_wbs_new_org`
- `stg_ref_customers_organization`

## Modelli intermedi business core

Questi sostituiscono la catena di workbook Power Query.

### Ore e lineage issue

- `int_issue_account_lineage`
- `int_issue_enriched`
- `int_worklog_grouped`
- `int_resource_master`
- `int_account_master`
- `int_account_wbs_validity`
- `int_worklog_wbs_assignment`

Questi modelli sostituiscono la logica dietro:

- `PQ Issue e account`
- `Account Jira elaborato`
- `Organico elaborato`
- `A-Report ore new raggruppato elaborato`
- `B-Ticket elaborato`

### Logica linked-issue e servizi

- `int_linked_issue_relationships`
- `int_service_desk_issue_lineage`
- `int_service_desk_hours`
- `int_service_perimeter`

Questi sostituiscono la logica dietro:

- `Linked Issue`
- `Linked issue SD`
- `Linked issue SD elaborato`
- `Power Query Base Dati AM`
- `Power Query Analisi Servizi`

### Logica economics

- `int_wbs_economics_actual`
- `int_wbs_economics_forecast`
- `int_cost_allocation_rules`
- `int_wbs_costs_allocated`
- `int_hours_economics_bridge`

Questi sostituiscono la logica dietro:

- `PQ Ricavi`
- `PQ Costi ribaltati`
- `PQ Integrazione ore e economics`

## Mart finali

### Dimensioni

- `mart_dim_period`
- `mart_dim_account`
- `mart_dim_customer`
- `mart_dim_wbs`
- `mart_dim_project`
- `mart_dim_issue`
- `mart_dim_resource`
- `mart_dim_team`
- `mart_dim_area`
- `mart_dim_activity_type`
- `mart_dim_issue_category`

### Fact

- `mart_fact_worklogs`
- `mart_fact_hours_monthly`
- `mart_fact_issue_status`
- `mart_fact_service_backlog`
- `mart_fact_economics_actual`
- `mart_fact_economics_forecast`
- `mart_fact_budget`
- `mart_fact_profitability_monthly`
- `mart_fact_project_monitoring`
- `mart_fact_tm_billing_support`

### Reporting marts

- `mart_rpt_output_all_hours`
- `mart_rpt_it_ops_service`
- `mart_rpt_it_ops_effort`
- `mart_rpt_am_service`
- `mart_rpt_service_analysis`
- `mart_rpt_economics_overview`
- `mart_rpt_economics_clients`
- `mart_rpt_forecast_overview`
- `mart_rpt_forecast_clients`
- `mart_rpt_budget_vs_actual`
- `mart_rpt_monitoraggio_progetti`

Questi mart devono essere progettati come sostituti stabili del dataset Power BI, non come repliche dei fogli.

## Mapping dagli artefatti legacy ai mart target

### `Output All (A+B).xlsx`

Sostituzione target:

- `mart_rpt_output_all_hours`
- più dimensioni/fact riusabili sottostanti

### `PQ Report ITOPS.xlsx`

Sostituzione target:

- `mart_rpt_it_ops_service`
- `mart_rpt_it_ops_effort`

### `Power Query Base Dati AM.xlsx`

Sostituzione target:

- `mart_rpt_am_service`

### `Power Query Analisi Servizi.xlsx`

Sostituzione target:

- `mart_rpt_service_analysis`
- `mart_fact_service_backlog`

### `PQ Ricavi.xlsx` e `PQ Costi ribaltati.xlsx`

Sostituzione target:

- `mart_fact_economics_actual`
- `mart_fact_economics_forecast`
- `mart_fact_profitability_monthly`
- `mart_rpt_economics_overview`
- `mart_rpt_economics_clients`

### `PQ Integrazione ore e economics.xlsx`

Sostituzione target:

- `mart_rpt_economics_overview`
- `mart_fact_profitability_monthly`

### `PQ fatturazione T&M new.xlsx`

Sostituzione target:

- `mart_fact_tm_billing_support`

## Struttura target delle dashboard Metabase

Replicare inizialmente l'architettura informativa di Power BI, poi migliorarla.

### Collection 1: Giorni

Equivalente alle pagine attuali:

- `1.1-Giorni - Overview`
- `1.2-Giorni - Account e WBS`
- `1.3-Giorni - Trend`
- `1.4-Giorni - Focus R&D`

Alimentata da:

- `mart_rpt_output_all_hours`
- `mart_fact_hours_monthly`

### Collection 2: Economics Actual

Equivalente a:

- `2.1-Economics actual - Overview`
- `2.2-Economics actual - Team commessa attività cliente`
- `2.3-Economics actual - Clienti`

Alimentata da:

- `mart_rpt_economics_overview`
- `mart_rpt_economics_clients`

### Collection 3: Economics Forecast

Equivalente a:

- `2.4-Economics forecast - Ricavi overview`
- `2.5-Economics forecast - Ricavi clienti`

Alimentata da:

- `mart_fact_economics_forecast`
- `mart_rpt_forecast_overview`
- `mart_rpt_forecast_clients`

### Collection 4: Monitoraggio Progetti

Equivalente a:

- `3.1.1 overview company`
- `3.1.2 overview team`
- `3.2 gantt`
- `3.3 focus progetto`
- `3.4 capacity plan`

Alimentata da:

- `mart_fact_project_monitoring`
- dimensioni di supporto per progetti/risorse/team/periodi

### Collection 5: Budget and Variance

Anche se il Budget è visivamente integrato nelle pagine Power BI attuali, il warehouse dovrebbe modellarlo in modo esplicito.

Alimentata da:

- `mart_fact_budget`
- `mart_rpt_budget_vs_actual`

## Migrazione dei controlli e della data quality

I controlli presenti in `Power Query Output All - Controlli.xlsx` devono diventare controlli di primo livello nel warehouse.

## Test dbt

Esempi:

- issue key not null
- account key not null per issue con worklog dove previsto
- period valido nella period dimension
- univocità delle chiavi tecniche
- integrità referenziale da issue-account lineage ad account master
- consistenza degli intervalli di validità WBS

## Audit marts

Raccomandati:

- `mart_audit_issue_without_account`
- `mart_audit_account_not_mapped_to_wbs`
- `mart_audit_linked_issue_account_conflicts`
- `mart_audit_open_issue_on_closed_account`
- `mart_audit_accounts_without_recent_hours`
- `mart_audit_customer_organization_conflicts`

Questi dovrebbero essere interrogabili direttamente in Metabase e, opzionalmente, notificati tramite sensori Dagster.

Inoltre, la piattaforma dovrebbe distinguere tra:

- mart operativi di controllo usati durante la review inframensile
- output certificati di chiusura mensile usati come baseline storiche

## Fasi di implementazione suggerite

## Fase 0: stabilizzare l'ingestion già presente nel repo

- validare `excel_ingestion_all_job`
- caricare le mapping reference oggi commentate dopo validazione schema
- standardizzare gli attuali target name da `raw_xls_*` verso una policy raw/ref più pulita

Deliverable:

- copertura completa del landing reference per le tabelle di corrispondenza già note

Requisito trasversale fin dall'inizio:

- definire come un run diventa uno snapshot certificato di chiusura mensile

## Fase 1: sostituire il backbone legacy delle ore

- aggiungere `raw_tempo_worklogs`
- aggiungere `raw_hr_resources`
- aggiungere `raw_cdgapp_account_wbs_bridge`
- aggiungere `raw_axel_commesse`
- creare modelli dbt per:
  - issue-account lineage
  - ore mensili raggruppate
  - arricchimento risorsa/account/WBS
  - mart sostitutivo di output-all

Deliverable:

- primo sostituto warehouse del dominio ore di `Output All (A+B)`

## Fase 2: sostituire la logica servizi / IT OPS / AM

- ingest delle reference mancanti su service perimeter e issue extractions
- costruzione dei modelli linked-issue
- costruzione dei mart service desk e AM
- migrazione dei controlli workbook in dbt e Metabase

Deliverable:

- sostituzione di `PQ Report ITOPS`, `Power Query Base Dati AM`, `Power Query Analisi Servizi`

## Fase 3: sostituire gli economics actual

- aggiungere ingestion degli actual SAP
- costruire i fact WBS/economics actual
- replicare le metriche di margine ed EBITDA

Deliverable:

- sostituzione della sezione economics actual di Power BI

## Fase 4: sostituire forecast e cost allocations

- ingest di input forecast e budget
- modellazione della logica avviate/potenziali
- implementazione dei ribaltamenti come modelli di allocazione espliciti in dbt

Deliverable:

- sostituzione delle pagine forecast e delle viste di profittabilità

## Fase 5: sostituire monitoraggio progetti e supporto fatturazione T&M

- costruzione dei mart di monitoraggio progetti
- costruzione del mart di supporto billing T&M
- decisione se il supporto billing rimane in Metabase, in un export warehouse, o in entrambi

## Miglioramenti rispetto al processo legacy

### 1. Un solo semantic layer canonico

Oggi lo stesso concetto è duplicato in molti workbook. Il warehouse dovrebbe fornire un solo modello canonico per:

- issue
- account
- worklog
- WBS
- customer
- team
- economics

### 2. Lineage tecnica invece di lineage da workbook

Ogni mart dovrebbe dichiarare le proprie dipendenze upstream in dbt invece di dipendere dal fatto che un operatore si ricordi quale workbook aggiornare per primo.

### 3. Ingestion incrementale invece di sostituzione mensile del file dove possibile

Usare API e load incrementali controllati per:

- issue
- worklog
- account

### 4. Modelli storici espliciti

Codificare la history con:

- snapshot table dove necessario
- validity range
- monthly close markers

invece di preservare la logica solo tramite file archiviati in `Save/`.

Questo è particolarmente importante perché i documenti di review confermano che la storicizzazione mensile di `A+B` fa parte del processo ufficiale, non di un archivio accidentale di file.

### 5. Test invece di tab di controllo manuali

Mantenere tabelle di eccezione per la remediation operativa, ma rendere i controlli eseguibili e ripetibili.

### 6. Naming più pulito

Sostituire etichette legacy come `A`, `B`, `D`, `E` con nomi di modello espliciti legati alla grana business.

## Candidati al cleanup

Questi dovrebbero essere rivisti e probabilmente ridotti durante la migrazione.

### Clutter di file / archivi

Cartelle verosimilmente non parte della catena produttiva target:

- `TMP MARY`
- gran parte di `Save/old`
- copie duplicate dei PBIX in `power BI/save`
- copie temporanee locali come `- Copia`, `old`, `OK`, `ULTIMAOK`

Sono utili come storico forense, ma non come dipendenze di produzione.

### Tabelle reference attualmente escluse dall'ingestion

Queste dovrebbero essere promosse oppure ritirate esplicitamente:

- `Issue e account`
- `Corrispondeza validità raccordo`
- `KPI Target`
- `Sintesi storico SD`

Al momento sono in uno stato ambiguo.

### Colonne da mettere in discussione

Diversi estratti legacy includono campi placeholder come:

- `CAMPO 1`
- `CAMPO 2`
- `CAMPO 3`
- `CAMPO 4`
- `CAMPO 5`

Questi devono essere classificati come:

- necessari e rinominati
- deprecati e rimossi
- temporaneamente preservati ma documentati

### Workbook-specific manual formulas

`Analisi ore file con formule.xlsx` è un forte candidato all'eliminazione una volta che le formule saranno tradotte in modelli dbt o calcoli Metabase.

### Strategia di estrazione issue duplicata

La coesistenza di:

- `Ticket light`
- `Ticket`
- `Issue dati aggiuntivi`

suggerisce che il contratto di estrazione dalle sorgenti dovrebbe essere ridisegnato. Il nuovo stack dovrebbe definire un unico issue model chiaro con scope incrementale e un piccolo numero di raw table purpose-specific, non tre estratti Excel parzialmente sovrapposti.

## Rischi e punti aperti

### Rischio di parità storica

Parte della parità degli output potrebbe dipendere da formule workbook o decisioni manuali implicite non pienamente visibili nei metadati. Queste dovranno essere validate durante il backtesting dbt.

### Rischio di parità API

Alcuni estratti legacy arrivano da plugin Jira o export UI Tempo. L'equivalenza API va confermata prima di eliminare l'ingestion file-based.

### Semantica della chiusura contabile

Il vecchio processo assume che, una volta chiuso il mese, i worklog siano di fatto congelati. La nuova pipeline deve preservare esplicitamente quel comportamento contabile.

### Semantica dei run operativi vs run di chiusura

Il processo legacy distingue i run inframensili di controllo dai run storicizzati di fine mese. Se la nuova piattaforma ignora questa distinzione, gli utenti possono perdere la possibilità di fare quality control ad hoc senza contaminare la baseline storica ufficiale.

### Dettaglio delle allocazioni costi

`PQ Costi ribaltati.xlsx` probabilmente contiene regole di allocazione non banali. Queste vanno validate con Finance prima della reimplementazione.

## Azioni immediate raccomandate

1. Completare la copertura Dagster per i file reference attualmente omessi.
2. Dare priorità all'ingestion `raw_tempo_worklogs` prima di qualunque build dbt più ampia.
3. Definire le grane canoniche dei mart sostitutivi:
   - worklog
   - issue-month
   - account-period
   - WBS-period
   - customer-period
4. Costruire il primo slice dbt attorno alla sola logica ore di `Output All`.
5. Fare backtest dei mart risultanti rispetto a uno o due output mensili salvati in `Save/`.
6. Solo dopo aver raggiunto una parità accettabile sulle ore, passare a IT OPS / AM e poi agli economics.

## Risultato atteso

Se implementata in questo modo, la nuova piattaforma sostituirà una fragile catena di workbook con:

- ingestion ripetibile
- modelli business espliciti
- regole qualità testabili
- lineage più chiara
- manutenzione BI più semplice
- meno sforzo manuale mensile

preservando al tempo stesso gli output analitici già usati dal management e dalle operations.
