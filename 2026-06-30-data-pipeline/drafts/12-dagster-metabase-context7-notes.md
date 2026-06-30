# Dagster And Metabase Context7 Notes

## Scopo

Annotare i riscontri ottenuti tramite Context7 sulla documentazione Dagster e Metabase, da usare come materiale di supporto per lo scenario Dagster + dbt + Metabase su AWS.

Queste note non sostituiscono una verifica architetturale finale su sizing, deployment, sicurezza, costi o modello operativo.

## Fonti Context7

### Dagster

Context7 library: `/websites/dagster_io`

Riscontri utili:

- Dagster viene documentato come orchestratore per asset e pipeline dati.
- Dagster supporta software-defined assets, job, schedule e sensor.
- Dagster supporta asset checks per controlli di qualita' e salute degli asset.
- Dagster documenta l'integrazione con dbt, inclusa osservabilita' degli asset dbt, run history e orchestrazione di run dbt dentro pipeline piu' ampie.
- Dagster documenta deployment AWS su ECS o EC2.
- Per ECS, Dagster documenta `EcsRunLauncher`, che puo' avviare un task ECS per ogni run.
- Nelle architetture containerizzate Dagster distingue webserver, daemon, storage metadati/eventi e user code.

### Metabase

Context7 library: `/websites/metabase`

Riscontri utili:

- Metabase viene documentato come piattaforma di BI/self-service analytics.
- La documentazione copre query builder, SQL/native queries, visualizzazioni, dashboard, metriche, alert ed export.
- La documentazione copre data modeling: modelli, metriche, metadata, tipi e segmenti.
- La documentazione copre dashboard interattive, subscription, auto-refresh e embedding.
- Metabase puo' connettersi a database applicativi e usare PostgreSQL come database applicativo di produzione per Metabase stesso.

## Implicazioni Per Lo Scenario A

Lo scenario Dagster + dbt + Metabase puo' essere rappresentato come:

```text
Sorgenti
  -> Dagster ingestion / orchestration
  -> raw / landing
  -> dbt transform / stg / mart
  -> Dagster asset checks / run history / observability
  -> Metabase dashboard / query / metriche / alert / export
```

## Claim Utilizzabili Nel Deck

- Dagster puo' essere presentato come orchestratore data-engineering con asset graph, job, schedule, sensor, run history e asset checks.
- Dagster + dbt puo' sostenere una separazione chiara tra orchestrazione della pipeline e trasformazioni/modellazione dei dati.
- Dagster e' coerente con un deployment AWS su ECS o EC2, in linea con i vincoli utente.
- Metabase puo' essere presentato come layer BI/self-service per dashboard, query, metriche, alert ed export sopra mart/output.

## Claim Da Non Fare Senza Verifica

- Non affermare che ECS sia preferibile a EC2 o viceversa: per questa blueprint e' una variante AWS con impatto soprattutto su costi, operation e modello di gestione.
- Non affermare performance, volumi o SLA senza sizing.
- Non affermare costi cloud o run senza stima.
- Non posizionare Metabase come motore di orchestrazione, data quality o trasformazione.
- Non trasformare l'assunzione di accettazione Metabase in un claim cliente: per questa fase lo consideriamo accettabile, ma requisiti di governance, accessi, embedding/export e policy vanno chiariti se diventano rilevanti.

## Gap Da Verificare

- Impatto costi/operation della variante ECS vs EC2.
- RDS vs database cliente.
- Necessita' di S3/landing object storage.
- Sizing di run, storage, frequenze e retention.
- Requisiti di access control, pubblicazione BI, embedding/export e governance per clienti esterni, se rilevanti.

## grill-with-docs

- I riscontri rafforzano lo scenario A senza trasformarlo in raccomandazione finale.
- Il confronto resta neutrale rispetto allo scenario Qlik/Talend.
- I punti non confermati restano marcati come gap.

## Review

- Le note distinguono capability documentate e scelte architetturali da decidere.
- Non sono stati introdotti prezzi, SLA o limiti quantitativi non supportati.
- I risultati sono coerenti con i draft `08-scenario-comparison.md` e `10-architecture-brief.md`.

## Humanize

Dagster/dbt/Metabase puo' essere raccontato come una strada piu' componibile e controllabile: Dagster governa la pipeline, dbt costruisce il modello dati, Metabase espone il risultato agli utenti. Il vantaggio e' il controllo; il costo da gestire e' l'ownership tecnica dello stack.
