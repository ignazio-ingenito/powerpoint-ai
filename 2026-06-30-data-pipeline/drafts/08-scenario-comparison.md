# Scenario Comparison - Dagster/dbt/Metabase vs Talend/Qlik

## Scopo

Confrontare in modo neutrale le due ipotesi TO BE per la Data Pipeline Blueprint.

Questo documento prepara le slide comparative. Non contiene una raccomandazione finale.

## Scenari

### Scenario A - Dagster + dbt + Metabase su AWS

**Decisioni utente:**

- cloud target: AWS;
- compute: ECS o EC2;
- escluso EKS;
- database: RDS oppure database del cliente;
- presentation: Metabase.

**Posizionamento:** scenario modulare, data-engineering oriented, con componenti componibili e controllo architetturale elevato.

**Riscontro Context7 / documentazione Dagster e Metabase:**

- Dagster documenta software-defined assets, job, schedule, sensor e asset check per orchestrare e controllare pipeline dati.
- Dagster documenta integrazione con dbt, inclusa osservabilita' degli asset dbt, run history e orchestrazione di esecuzioni dbt dentro pipeline piu' ampie.
- Dagster documenta deployment AWS su ECS o EC2; su ECS puo' avviare ogni run come task ECS tramite `EcsRunLauncher`.
- Metabase documenta funzionalita' di analytics self-service: query builder, SQL/native queries, visualizzazioni, dashboard, metriche, alert, export e data modeling.
- Metabase documenta dashboard interattive, subscription, auto-refresh ed embedding; per il deck va comunque posizionato come presentation/BI layer, non come motore di orchestrazione o trasformazione.

### Scenario B - Talend + Qlik Cloud Analytics Premium

**Decisioni utente:**

- Qlik Cloud Analytics Premium come target presentation/analytics;
- Talend come opzione di data integration;
- ipotesi da verificare: Talend potrebbe essere compreso nella licenza Qlik.

**Posizionamento:** scenario enterprise/product-oriented, con forte copertura su integrazione dati e analytics gestita.

**Riscontro Context7 / documentazione Qlik:**

- Qlik Help descrive Qlik Cloud come combinazione di data integration e analytics per portare dati enterprise da fonti on-prem/cloud verso analytics self-service Qlik o altri ambienti analytics.
- Qlik Help descrive Qlik Talend Cloud come pacchetto unificato di data integration e data quality per pipeline che producono dati trusted.
- Qlik Automate viene documentato come interfaccia no-code per automatizzare workflow analytics e data workflow.
- Qlik Developer documenta API per task, task chain, run, log, reload e automazioni, utili per operationalization e monitoraggio.
- Non risulta verificato da Context7 che Talend sia incluso nella licenza Qlik Cloud Analytics Premium: resta un punto commerciale/contrattuale da confermare.

## Parti Comuni

| Componente comune | Descrizione | Rilevanza |
|---|---|---|
| Data contracts | Definizione fonti, tracciati, formati, frequenze, ownership | Evita ambiguita' a monte |
| Ingestion | Acquisizione da API, file, DB o sistemi applicativi | Base comune per CDG, ProSIGNAL, Kiron |
| Validazione dati | Controlli formato, presenza campi, header/tail, coerenza base | Riduce errori prima delle trasformazioni |
| Mapping/reference data | Tabelle guida, mapping account/WBS, tracciati, regole di dominio | Cuore della governance |
| Preparazione e trasformazione | Normalizzazione, arricchimento, parsing, calcoli | Produce dati semanticamente utilizzabili |
| Mart/output | Output controllati per BI, vigilanza, economics, forecast | Trasforma pipeline in valore operativo |
| Data quality | Scarti, anomalie, quadrature, test, run log | Rende il dato difendibile |
| Presentation | Dashboard, export, report o interfacce operative | Porta il risultato agli utenti |
| Audit e storicizzazione | Storico input/output, run, versioni, controlli | Necessario per controllo e tracciabilita' |

## Mapping Componenti

| Componente | Dagster + dbt + Metabase | Talend + Qlik |
|---|---|---|
| Ingestion | Dagster job/asset e connettori custom o librerie dedicate | Talend job/connettori data integration |
| Orchestrazione | Dagster | Talend orchestration/runtime, da verificare nel dettaglio |
| Trasformazioni | dbt + SQL/Python dove necessario | Talend transformations e/o layer database/Qlik, da definire |
| Data quality | dbt tests, controlli custom, Dagster asset checks dove applicabile | Talend/Qlik data integration e data quality capabilities documentate, packaging e fit da verificare |
| Storage/database | RDS, DB cliente, warehouse o object storage su AWS | DB/warehouse/storage da definire + Qlik Cloud come analytics layer |
| Mart/output | dbt models / database views / mart | output Talend + data model Qlik / DB intermedio |
| Presentation | Metabase dashboard, query, metriche, alert, export | Qlik Cloud Analytics Premium |
| Governance tecnica | repository, CI/CD, Dagster asset graph, run history, logs, asset checks | tenant governance, automazioni, task/run/log API Qlik; dettagli Qlik/Talend da verificare |
| Deployment | ECS o EC2, no EKS | runtime Talend + Qlik Cloud, modello da chiarire |

## Benefici E Limiti

### Scenario A - Benefici

- Alto controllo architetturale e componibilita'.
- Buon fit con reference implementation CDG gia' orientata a Dagster/dbt/Metabase.
- Potenziale riuso tramite asset/job, modelli dbt, convenzioni raw/stg/mart.
- Buona osservabilita' tecnica su run, asset, controlli e dipendenze della pipeline.
- Costi di licenza potenzialmente contenuti, da verificare rispetto a run/infrastruttura.
- Adatto quando il team vuole controllo su codice, pipeline e deployment.

### Scenario A - Limiti / blocker

- Richiede competenze data engineering, AWS e gestione operativa.
- Richiede setup e manutenzione di infrastruttura/runtime.
- Metabase puo' essere meno adatto se il cliente richiede funzionalita' enterprise BI gia' standardizzate su Qlik.
- Costi reali dipendono da hosting, database, run, monitoraggio e manutenzione.
- La scelta ECS vs EC2 non e' dirimente per la blueprint: impatta soprattutto costi, operation e preferenze di gestione.
- La scelta RDS/DB cliente va decisa caso per caso.

### Scenario B - Benefici

- Potenziale fit enterprise se Qlik Cloud Analytics Premium e' gia' scelto o disponibile.
- Possibile riduzione del lavoro custom su ingestion/data integration se Talend copre i connettori necessari.
- Forte posizionamento su analytics/presentation.
- Potenzialmente piu' rapido se licenze, tenant e competenze sono gia' disponibili.
- Puo' essere piu' leggibile per clienti che preferiscono stack BI/integration consolidati.

### Scenario B - Limiti / blocker

- Licensing/package Talend + Qlik da verificare prima di qualunque claim.
- Possibile lock-in maggiore sullo stack prodotto.
- Runtime, deployment, costi e governance Talend devono essere chiariti.
- Riuso cross-cliente potrebbe dipendere da configurazioni tenant/licenze/progetti.
- Potrebbe essere meno flessibile per logiche custom molto specifiche o file processing pesante, da verificare.

## Matrice Comparativa Qualitativa

| Criterio | Scenario A: Dagster/dbt/Metabase | Scenario B: Talend/Qlik |
|---|---|---|
| Riuso | Alto se si standardizzano asset, modelli, template e convenzioni | Alto se connettori/job/template sono riusabili tra tenant/progetti |
| Scalabilita' | Buona, legata a design AWS, database e orchestrazione | Buona, ma dipendente da limiti/licensing/runtime Qlik/Talend |
| Costi | Più infrastruttura/run/competenze; licenze potenzialmente minori | Più licensing/subscription; minore custom se stack gia' disponibile |
| Rapidita' iniziale | Rapida se si riusa CDG; piu' lenta se serve setup completo | Rapida se licenze/tenant/connettori sono pronti; altrimenti da verificare |
| Complessita' | Maggiore lato engineering e operations | Maggiore lato prodotto/licensing/governance vendor |
| Skill richieste | Data engineering, AWS, SQL/dbt, Python, BI | Talend, Qlik, data integration, BI governance |
| Lock-in | Medio-basso, componenti sostituibili | Medio-alto, dipendente da Qlik/Talend |
| Fit ProSIGNAL | Buono per file processing custom e controlli specifici | Da verificare su file grandi, tracciati fixed-column e processing pesante |
| Fit Kiron CDG | Buono per un caso CDG-like documentato con fonti Campus/Campus 2.0/Zucchetti, regole TG/RIB/STEP e output Actual/Forecast | Potenzialmente buono se cliente preferisce Qlik/BI enterprise e se Talend copre integrazione/regole con sufficiente trasparenza |
| Fit CDG interno | Molto buono per continuita' con implementazione corrente | Possibile, ma implica ripensare parte della reference implementation |

## Economics: Consiglio Di Impostazione

Per una blueprint non conviene entrare subito in un dettaglio economico di offerta.

Suggerimento:

- usare range qualitativi o t-shirt size;
- separare costi di:
  - setup iniziale;
  - licenze/subscription;
  - infrastruttura/cloud;
  - delivery;
  - run/manutenzione;
  - evolutive;
- mostrare cosa guida il costo, non il prezzo finale.

Possibile scala:

```text
Basso / Medio / Alto
oppure
S / M / L
oppure
Range da stimare in discovery
```

## Proiezione Sui Tre Casi

| Caso | Priorita' | Scenario A | Scenario B | Nota |
|---|---|---|---|---|
| ING ProSIGNAL | Alta | Forte se servono processing custom, file grandi, controlli specifici | Forte se Qlik/Talend copre ingestion/quality e analytics con minor custom | Materiali vault acquisiti; mancano esempi file/tracciati/output |
| Kiron CDG | Alta | Buono: caso documentato con Actual, Forecast, riconciliazione e output BI-ready | Buono se lo stack Qlik e' preferito o disponibile per cliente | Restano da chiarire eventuali open point sulle regole |
| CDG interno | Media | Molto coerente con lavoro esistente | Possibile scenario alternativo, ma meno allineato allo stato corrente | Utile come reference implementation |

## grill-with-docs

- Il confronto resta neutrale e orientato alla discussione del comitato, senza raccomandazione finale.
- La priorita' esterna ProSIGNAL/Kiron e' rispettata; Kiron e' ora supportato da materiali specifici.
- L'economics e' trattato come range/driver, coerente con una blueprint e non come offerta.

## Review

- Tutti i criteri richiesti dall'utente sono coperti.
- Le informazioni non verificate su licensing e deployment sono marcate come gap.
- Non ci sono prezzi, date o effort inventati.

## Humanize

Il confronto deve aiutare a vedere due strade credibili: una piu' componibile e controllabile su AWS, l'altra piu' orientata a piattaforma enterprise e analytics gestita. La decisione non e' quale tool sia migliore in assoluto, ma quale modello conviene adottare come blueprint riusabile.
