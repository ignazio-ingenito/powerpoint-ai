# Architecture Brief

## Scopo

Definire le componenti logiche della pipeline e gli schemi architetturali testuali per i due scenari.

Questo documento prepara infografiche e slide architetturali PowerPoint-editable.

## Componenti Logiche Di Una Buona Pipeline

```text
Sorgenti
  -> Ingestion / landing
  -> Verifica formato e data contracts
  -> Raw / source-faithful layer
  -> Parsing e manipolazione
  -> Normalizzazione e preparazione
  -> Data quality e controlli
  -> Transform / business rules
  -> Mart / output data product
  -> Audit, run history, lineage
  -> Presentation / dashboard / export
  -> Governance operativa
```

## Componenti Da Visualizzare

| Componente | Significato | Esempi dai casi |
|---|---|---|
| Sorgenti | Sistemi/file/API di origine | Jira, Tempo, SAP, CDG app, Excel, fixed-column files |
| Ingestion | Acquisizione controllata | API job, upload file, connettori |
| Data contracts | Regole su tracciati, campi, frequenza | campi Jira, tracciati ProSignal, tabelle guida |
| Raw/source-faithful | Dati fedeli alla fonte | raw Jira, file originali, landing |
| Parsing/manipolazione | Lettura e trasformazioni tecniche iniziali | fixed-column parsing, merge, export |
| Preparation/staging | Pulizia semantica e normalizzazione | stg views, tipi campo, chiavi |
| Quality gates | Controlli e scarti | header/tail, WBS chiuse, quadrature |
| Business transform | Regole di dominio | ribaltamento costi, forecast, aggregazioni |
| Mart/output | Data product consumabili | P1-P6, output ProSignal, dashboard datasets |
| Presentation | BI/report/export | Metabase, Qlik Cloud, Power BI se richiesto |
| Governance | Ownership, accessi, monitoraggio | runbook, audit, profili, logging |

## Scenario A - Dagster + dbt + Metabase Su AWS

### Schema Testuale

```text
[Sorgenti cliente / TXT]
  Jira / Tempo / SAP / Excel / SharePoint / Fixed files
        |
        v
[AWS Ingestion Compute]
  ECS task oppure EC2
  Dagster orchestration
  schedules / sensors / asset checks
        |
        v
[Landing / Raw Zone]
  S3 o DB landing, da definire
  Raw/source-faithful data
        |
        v
[Database / Warehouse]
  RDS oppure DB cliente
  ref / stg / mart
        |
        v
[Transform Layer]
  dbt models
  SQL/Python custom dove necessario
  data quality checks
        |
        v
[Mart / Output Data Products]
  CDG P1-P6
  ProSignal outputs
  Kiron CDG outputs
        |
        v
[Presentation]
  Metabase
  Export / dashboard / reports
        |
        v
[Monitoring & Governance]
  Dagster run history
  asset graph
  asset checks
  logs
  audit
  runbook
```

### Zone Architetturali

- **Source zone:** sistemi e file origine.
- **Compute zone:** ECS/EC2 per ingestion/orchestrazione.
- **Storage/data zone:** S3, RDS o database cliente, da decidere.
- **Transform zone:** dbt e logiche custom.
- **Serving zone:** mart/output e Metabase.
- **Governance zone:** logging, audit, run history, asset graph, asset checks, accessi.

### Note Visuali

- Usare uno schema a layer orizzontali.
- Evidenziare AWS come contenitore esterno.
- Mostrare ECS/EC2 come variante di deployment AWS, non come scelta strategica tra le due soluzioni.
- Segnalare che ECS vs EC2 impatta soprattutto costi, operation e modello di gestione.
- Mostrare RDS/DB cliente come bivio.
- Tenere Metabase come presentation layer, non come motore dati.
- Mostrare Dagster come orchestratore e layer di osservabilita' tecnica della pipeline, includendo schedule, sensor, run history e asset checks.
- Mostrare Metabase come BI self-service su mart/output: dashboard, query, metriche, alert ed export.

## Scenario B - Talend + Qlik Cloud Analytics Premium

### Schema Testuale

```text
[Sorgenti cliente / TXT]
  Jira / Tempo / SAP / Excel / SharePoint / Fixed files
        |
        v
[Talend Data Integration / Runtime]
  ingestion
  parsing
  transformations
  data quality
        |
        v
[Storage / Database / Data Mart]
  DB cliente o storage/warehouse da definire
  output curated
        |
        v
[Qlik Cloud Analytics Premium]
  semantic/analytics layer
  dashboard
  exploration
  reports
  reload/task automation APIs
        |
        v
[Governance & Operations]
  tenant governance
  data refresh
  access control
  monitoring
```

### Zone Architetturali

- **Source zone:** sistemi e file origine.
- **Integration zone:** Talend runtime / data integration.
- **Data zone:** DB, storage o warehouse da definire.
- **Analytics zone:** Qlik Cloud Analytics Premium.
- **Automation/API zone:** Qlik Automate, webhooks, task chain, reload, run log e API operative documentate da Qlik Developer.
- **Governance zone:** accessi, refresh, monitoraggio, catalogo, da verificare.

### Note Visuali

- Usare uno schema a zone verticali, con Qlik Cloud evidenziato come cloud presentation/analytics.
- Mostrare Talend come integration/data quality layer, ma segnare runtime e packaging come da verificare.
- Evitare di scrivere che Talend e' incluso nella licenza Qlik finche' non verificato.
- Mostrare le automazioni/API Qlik come supporto operativo per reload, task chain e run log, non come sostituto automatico di un orchestratore data engineering.

## Architettura Logica Comune

Per evitare una presentazione troppo tool-driven, prima dei due schemi usare una slide comune:

```text
Source -> Ingest -> Validate -> Prepare -> Transform -> Quality -> Serve -> Govern
```

Etichette consigliate:

- Acquire
- Verify
- Prepare
- Model
- Control
- Serve
- Govern

Versione italiana:

- Acquisire
- Verificare
- Preparare
- Modellare
- Controllare
- Esporre
- Governare

## Asset Da Produrre

Preferire asset PowerPoint-editable o vettoriali:

- diagramma pipeline logica;
- schema AWS scenario A;
- schema Talend/Qlik scenario B;
- matrice di confronto;
- WBS in stile mindmap/XMind.

Salvare eventuali SVG, diagrammi Mermaid, immagini o sorgenti in:

- `generated-assets/` per asset finalizzabili;
- `attempts/` per prove.

## Gap Tecnici

- Stimare l'impatto costi/operation della variante ECS vs EC2, senza trattarla come decisione bloccante di blueprint.
- Confermare RDS vs DB cliente per ogni progetto.
- Confermare se serve S3/landing object storage.
- Confermare runtime/deployment Talend.
- Confermare packaging/licenza Talend con Qlik Cloud Analytics Premium.
- Confermare limiti Qlik/Talend per file grandi e fixed-column.
- Assumere Metabase accettabile come layer BI per clienti esterni; dettagliare solo requisiti di access control, publishing, embedding/export e governance se emergono vincoli specifici.

## Riscontri Context7 Su Qlik

Fonti consultate:

- Qlik Help (`/websites/help_qlik`): data integration, Qlik Talend Cloud, Qlik Automate.
- Qlik Developer (`/websites/qlik_dev`): Tasks API, task chaining, automazioni, reload e log.

Implicazioni per il deck:

- Qlik/Talend puo' essere rappresentato come scenario piattaforma per data integration, data quality e analytics.
- Qlik Cloud puo' essere rappresentato come analytics/presentation layer con capability operative di automazione, reload e task chain.
- La componente Talend va comunque trattata come opzione da verificare su licenza, runtime, deployment e limiti tecnici.
- Per ProSIGNAL resta da verificare il fit su file molto grandi, tracciati fixed-column e controlli cross-file.

## Riscontri Context7 Su Dagster E Metabase

Fonti consultate:

- Dagster docs (`/websites/dagster_io`): asset checks, schedule, sensor, integrazione dbt, deployment AWS ECS/EC2.
- Metabase docs (`/websites/metabase`): analytics, dashboard, query, metriche, alert, data modeling, embedding.

Implicazioni per il deck:

- Dagster puo' essere rappresentato come orchestratore data-engineering con asset graph, job, schedule, sensor, run history e asset checks.
- L'integrazione Dagster/dbt puo' sostenere il messaggio di separazione tra orchestrazione e trasformazioni SQL/modellazione.
- Su AWS, Dagster e' coerente sia con ECS sia con EC2; ECS e' documentato anche con run lanciati come task dedicati.
- Metabase va rappresentato come layer BI/self-service sopra mart/output, con dashboard, query, metriche, alert, export ed eventuale embedding.
- Metabase non va presentato come componente di data quality, orchestrazione o trasformazione.

## grill-with-docs

- L'architettura resta a livello blueprint e non diventa una specifica implementativa.
- Le zone aiutano a produrre slide pulite e coerenti con il pubblico C-level/Tech Committee.
- I punti non verificati sono marcati come gap, non come claim.

## Review

- Entrambi gli scenari hanno uno schema architetturale.
- Le componenti comuni sono esplicite.
- I vincoli utente AWS, ECS/EC2 come variante non dirimente, no EKS, RDS/DB cliente e Qlik Cloud sono rispettati.
- Gli asset richiesti sono tracciati e salvati in cartelle corrette.

## Humanize

La slide architetturale deve far capire il percorso del dato senza obbligare il lettore a leggere una specifica tecnica. Prima si mostra la logica comune della pipeline, poi si mostra come cambia la realizzazione nei due scenari.
