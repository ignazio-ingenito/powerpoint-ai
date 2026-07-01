# WBS del progetto

## 1. Sintesi del perimetro

Il progetto riguarda la definizione di una **Data Pipeline Blueprint** riusabile su più iniziative data-intensive: ING ProSIGNAL, Kiron CDG, CDG interno e progetti analoghi futuri.

La documentazione disponibile descrive tre casi con natura diversa:

- **CDG interno:** caso più documentato, con processi P1-P6, fonti Jira/Tempo/SAP/CDG app, tabelle guida, output actual/economics/forecast, dashboard e governance operativa.
- **Kiron CDG:** caso cliente esterno CDG-like, con Actual, Forecast, fonti Campus/Campus 2.0/Zucchetti, regole TG/RIB/STEP, DB Actual, DB Forecast e integrazione verso BI.
- **ING ProSIGNAL:** caso file-processing/regolamentare, basato su file fixed-column anche grandi, tracciati versionati, controlli tecnici/funzionali, output regolamentari e audit.

Il perimetro non è la realizzazione immediata di una singola pipeline cliente. È un programma di lavoro per produrre:

- una blueprint comune;
- criteri di scelta tra due scenari TO BE, AWS/Dagster/dbt/Metabase e Qlik/Talend;
- standard riusabili per dati, tracciati, ingestion, controlli, mart, dashboard, run e governance;
- WBS specifiche per i tre casi di applicazione;
- base utilizzabile per stima effort, responsabilità, roadmap, Gantt e piano di collaudo.

La WBS copre il 100% del lavoro oggi identificabile sulla base della documentazione disponibile. Gli elementi necessari ma non ancora supportati da fonti sufficienti sono separati in assunzioni, aree mancanti o rischi, invece di essere trattati come deliverable certi.

## 2. Assunzioni

- La WBS rappresenta il lavoro necessario per completare la **blueprint e la preparazione dei tre stream di applicazione**, non una delivery contrattuale già approvata per ogni cliente.
- La scelta tra scenario AWS e scenario Qlik/Talend non è ancora chiusa; la WBS include quindi deliverable di confronto e criteri decisionali.
- ProSIGNAL e Kiron CDG hanno priorità perché sono casi cliente esterni.
- CDG interno viene usato come reference implementation e caso più documentato.
- Per ProSIGNAL mancano esempi reali completi di file, tracciati e output; le voci specifiche restano nei limiti dei materiali disponibili e vanno confermate.
- Non sono inserite date, durate, effort, costi o commitment.
- Gli elementi finali della WBS sono formulati come deliverable o work package verificabili, non come attività operative.
- Dove un elemento è necessario ma non pienamente documentato, viene indicato nelle note o nelle aree da chiarire.

## 3. WBS principale

| Codice WBS | Livello | Nome elemento | Descrizione | Deliverable atteso | Note |
| ---------- | ------: | ------------- | ----------- | ------------------ | ---- |
| 1 | 1 | Governance e perimetro blueprint | Definizione del quadro di governo del programma blueprint | Framework di governance blueprint | Include regole di adozione, ownership e decisioni aperte |
| 1.1 | 2 | Perimetro e obiettivi confermati | Sintesi del bisogno comune tra ProSIGNAL, Kiron e CDG interno | Documento di perimetro approvabile | Basato su intake, storyline e sintesi casi d'uso |
| 1.1.1 | 3 | Mappa stakeholder e audience | Identificazione di CEO, Gianfranco, CTO, Tech Committee, owner progetto e owner dati | Mappa stakeholder | Utile per RACI successiva |
| 1.1.1.1 | 4 | Registro stakeholder e ruoli decisionali | Elenco ruoli, responsabilità decisionali e punti di validazione | Registro stakeholder | Work package stimabile |
| 1.1.2 | 3 | Registro assunzioni e gap | Separazione tra fatti, ipotesi e punti da validare | Registro assunzioni/gap | Deve restare vivo durante roadmap |
| 1.1.2.1 | 4 | Log decisioni aperte | Tracciamento di scenario, licensing, DB cliente/RDS, file ProSIGNAL, BI e run | Decision log iniziale | Non sostituisce un ADR tecnico |
| 1.2 | 2 | Criteri di adozione blueprint | Regole per decidere quando e come usare la blueprint su nuovi progetti | Modello di adozione blueprint | Serve a evitare soluzioni una tantum |
| 1.2.1 | 3 | Criteri di riuso | Condizioni per riusare componenti, template, controlli e convenzioni | Criteri di riuso documentati | Applicabile anche a progetti futuri |
| 1.2.1.1 | 4 | Checklist di applicabilità progetto | Checklist per classificare un progetto come CDG-like, file-processing o misto | Checklist applicabilità | Work package stimabile |
| 2 | 1 | Analisi funzionale e informativa | Consolidamento dei requisiti funzionali, informativi e organizzativi | Dossier funzionale blueprint | Area analisi, distinta da architettura e sviluppo |
| 2.1 | 2 | Perimetro funzionale comune | Identificazione delle capability comuni della pipeline | Capability map funzionale | Fonte: 03-use-case-synthesis e 10-architecture-brief |
| 2.1.1 | 3 | Componenti pipeline comuni | Source, ingestion, contract, raw, prepare, quality, transform, mart, presentation, governance | Mappa componenti comuni | Deve restare tool-neutral |
| 2.1.1.1 | 4 | Catalogo capability blueprint | Catalogo capability con descrizione, output e criteri di verifica | Catalogo capability | Work package stimabile |
| 2.2 | 2 | Requisiti informativi e output | Raccolta output attesi per ProSIGNAL, Kiron e CDG interno | Inventario output/data product | Necessario per stima e test |
| 2.2.1 | 3 | Data product CDG-like | Output Actual, Economics, Forecast, BI-ready | Catalogo data product CDG-like | Basato su CDG interno e Kiron |
| 2.2.1.1 | 4 | Schede data product P1-P6 / Actual / Forecast | Schede sintetiche per output CDG e Kiron | Schede data product | Work package stimabile |
| 2.2.2 | 3 | Data product ProSIGNAL | Output regolamentari, dashboard esiti, log e audit | Catalogo output ProSIGNAL | Da confermare con esempi reali |
| 2.2.2.1 | 4 | Schede output ProSIGNAL preliminari | Schede per output regolamentari e controlli disponibili | Schede output preliminari | Marcate come da validare |
| 3 | 1 | Architettura e scenari TO BE | Definizione della blueprint architetturale e confronto scenari | Blueprint architetturale e scenario pack | Area architettura |
| 3.1 | 2 | Architettura logica comune | Descrizione tool-neutral del percorso del dato | Architettura logica comune | Source -> Govern |
| 3.1.1 | 3 | Layer dati e responsabilità | Separazione raw/source-faithful, staging, mart/output, presentation | Schema layer dati | Supporta stima tecnica |
| 3.1.1.1 | 4 | Diagramma architettura logica | Diagramma executive con layer, output e governance | Diagramma architetturale | Work package stimabile |
| 3.2 | 2 | Scenario AWS | Rappresentazione dello scenario Dagster/dbt/Metabase su AWS | Scheda scenario AWS | ECS/EC2 non deciso; no EKS |
| 3.2.1 | 3 | Mappa componenti AWS | Mapping tra componenti blueprint e runtime/orchestrazione/storage/presentation | Matrice componenti AWS | Non è ancora design esecutivo |
| 3.2.1.1 | 4 | Scheda decisioni AWS | Decisioni aperte su ECS/EC2, RDS/DB cliente, landing, operation | Scheda decisioni AWS | Work package stimabile |
| 3.3 | 2 | Scenario Qlik/Talend | Rappresentazione dello scenario Talend/Qlik Cloud Analytics Premium | Scheda scenario Qlik/Talend | Entitlement da verificare |
| 3.3.1 | 3 | Mappa componenti Qlik/Talend | Mapping tra integration, quality, data layer, analytics e governance | Matrice componenti Qlik/Talend | Non assumere licenza Talend piena |
| 3.3.1.1 | 4 | Scheda decisioni Qlik/Talend | Decisioni aperte su tenant, capacity, runtime, capability incluse | Scheda decisioni Qlik/Talend | Work package stimabile |
| 3.4 | 2 | Confronto scenari | Valutazione neutrale di riuso, scalabilità, costi, velocità, complessità, blocker | Matrice comparativa scenari | Base per discussione comitato |
| 3.4.1 | 3 | Criteri di scelta | Criteri manageriali e tecnici per scegliere lo scenario | Criteri di scelta documentati | Non chiude la scelta |
| 3.4.1.1 | 4 | Scheda trade-off per comitato | Scheda sintetica per decisione/discussione | Scheda trade-off | Work package stimabile |
| 4 | 1 | Data governance e data contract | Standard riusabili per tracciati, campi, mapping e reference data | Framework data governance | Area dati/migrazione |
| 4.1 | 2 | Data contract template | Modello comune per descrivere fonti, campi, formati, frequenze, owner e versioni | Template data contract | Necessario per tutti gli stream |
| 4.1.1 | 3 | Contract per fonti CDG-like | Struttura per Jira, Tempo, SAP, CDG app, Campus, Zucchetti | Template fonti CDG-like | Da specializzare per progetto |
| 4.1.1.1 | 4 | Modello scheda fonte CDG-like | Scheda standard fonte con campi, ownership, controlli e output | Scheda fonte standard | Work package stimabile |
| 4.1.2 | 3 | Contract per file ProSIGNAL | Struttura per tracciati fixed-column, formato, header/tail, versioni | Template tracciato ProSIGNAL | Da validare con file reali |
| 4.1.2.1 | 4 | Modello scheda tracciato fixed-column | Scheda standard tracciato con range colonne, tipi, vincoli e controlli | Scheda tracciato standard | Work package stimabile |
| 4.2 | 2 | Reference data framework | Modello per tabelle guida, mapping e regole configurabili | Framework reference data | Basato su CDG T1-T13, Kiron TG/RIB/STEP |
| 4.2.1 | 3 | Ownership reference data | Regole di ownership, validità temporale, versionamento e modifica | Schema ownership reference data | Evita ambiguità operative |
| 4.2.1.1 | 4 | Registro reference data | Registro iniziale di tabelle guida e mapping per i tre casi | Registro reference data | Work package stimabile |
| 5 | 1 | Ingestion, landing e raw layer | Standard per acquisire dati in modo controllato e auditabile | Framework ingestion/raw | Area sviluppo/configurazione e integrazioni |
| 5.1 | 2 | Pattern ingestion riusabili | Pattern per API, database, file e upload manuale | Catalogo pattern ingestion | Deve coprire CDG-like e file-processing |
| 5.1.1 | 3 | Pattern API/database | Acquisizione da sistemi applicativi e contabili | Pattern connettori API/DB | Rilevante per CDG e Kiron |
| 5.1.1.1 | 4 | Scheda pattern connettore | Modello con input, output, run log, errori e controlli minimi | Scheda connettore | Work package stimabile |
| 5.1.2 | 3 | Pattern file grandi | Acquisizione file, registro, landing, processing asincrono, retention | Pattern file ingestion | Rilevante per ProSIGNAL |
| 5.1.2.1 | 4 | Scheda pattern file ingestion | Modello con upload, formato, dimensione, run log e retry | Scheda file ingestion | Work package stimabile |
| 5.2 | 2 | Raw/source-faithful layer | Convenzioni per conservare dato fedele alla fonte | Standard raw layer | Supporta audit e diagnosi |
| 5.2.1 | 3 | Convenzioni raw/staging | Naming, metadati tecnici, run id, timestamp, fonte, versione | Convenzioni raw/staging | Necessario per riuso |
| 5.2.1.1 | 4 | Convenzioni di naming e metadata | Documento operativo per layer raw e staging | Standard naming/metadata | Work package stimabile |
| 6 | 1 | Quality, audit e controllo del dato | Standard per rendere verificabili errori, anomalie e output | Framework quality/audit | Area testing/collaudo e governance dati |
| 6.1 | 2 | Quality gates comuni | Catalogo controlli tecnici e funzionali riusabili | Catalogo quality gates | Include controlli formato, quadrature, scarti |
| 6.1.1 | 3 | Controlli tecnici | Formato, campi obbligatori, header/tail, record count, schema drift | Libreria controlli tecnici | Tool-neutral |
| 6.1.1.1 | 4 | Schede controlli tecnici | Schede controllo con input, regola, esito, severità | Schede controlli tecnici | Work package stimabile |
| 6.1.2 | 3 | Controlli funzionali | WBS chiuse, linked issue, quadrature, scostamenti, cross-file checks | Libreria controlli funzionali | Alcuni specifici per progetto |
| 6.1.2.1 | 4 | Schede controlli funzionali | Schede controllo con razionale business e soglie da definire | Schede controlli funzionali | Work package stimabile |
| 6.2 | 2 | Audit trail e run history | Tracciabilità di esecuzioni, errori, scarti e output generati | Modello audit/run history | Essenziale per governance |
| 6.2.1 | 3 | Modello log esecuzioni | Campi minimi per run, fonte, stato, errore, output e owner | Modello run log | Base per dashboard tecnica |
| 6.2.1.1 | 4 | Specifica run log | Specifica dei campi run log e stati operativi | Specifica run log | Work package stimabile |
| 7 | 1 | Transform, mart e data product | Standard per produrre output business utilizzabili | Framework transform/mart | Area sviluppo/configurazione |
| 7.1 | 2 | Pattern trasformazione | Regole comuni per parsing, normalizzazione, mapping e arricchimento | Catalogo pattern trasformazione | Include varianti CDG-like e ProSIGNAL |
| 7.1.1 | 3 | Pattern CDG-like | Actual, Economics, Forecast, ribaltamenti, standard, mart BI-ready | Pattern trasformazione CDG-like | Basato su CDG/Kiron |
| 7.1.1.1 | 4 | Scheda pattern Actual/Forecast | Scheda standard per output Actual/Forecast e relative regole | Scheda pattern CDG-like | Work package stimabile |
| 7.1.2 | 3 | Pattern ProSIGNAL | Parsing fixed-column, aggregazioni, controlli, output regolamentari | Pattern trasformazione ProSIGNAL | Da validare con esempi reali |
| 7.1.2.1 | 4 | Scheda pattern output regolamentare | Scheda per output, controlli e audit ProSIGNAL | Scheda output regolamentare | Work package stimabile |
| 7.2 | 2 | Mart/output standard | Convenzioni per data product, mart, viste e export | Standard mart/output | Necessario per BI e processi |
| 7.2.1 | 3 | Catalogo data product | Elenco data product e criteri di accettazione | Catalogo data product | Collegato a 2.2 |
| 7.2.1.1 | 4 | Schede accettazione data product | Schede con output, controlli, owner e uso business | Schede accettazione | Work package stimabile |
| 8 | 1 | Presentation, workflow e consumo | Standard per dashboard, export, workflow utente e accessi | Framework presentation/workflow | Area presentation e operatività |
| 8.1 | 2 | Presentation layer blueprint | Linee guida per Metabase, Qlik o altro layer BI sopra output controllati | Modello presentation layer | Non deve essere motore dati |
| 8.1.1 | 3 | Dashboard business e tecniche | Distinzione tra dashboard business, esiti, tecnica e monitoraggio | Catalogo dashboard | CDG: business/tecnica; ProSIGNAL: esiti |
| 8.1.1.1 | 4 | Wireframe dashboard tipo | Wireframe o scheda dashboard per business e controllo tecnico | Schede dashboard | Work package stimabile |
| 8.2 | 2 | Workflow utente ed eccezioni | Modello di gestione anomalie, rettifiche, export e approvazioni | Modello workflow/eccezioni | Dettagli cliente da confermare |
| 8.2.1 | 3 | Gestione scarti e rettifiche | Categorie scarto, presa in carico, rettifica, ri-esecuzione | Modello gestione scarti | Rilevante per tutti i casi |
| 8.2.1.1 | 4 | Scheda processo gestione scarti | Scheda work package con stati, ruoli e output | Scheda gestione scarti | Work package stimabile |
| 9 | 1 | Stream applicativo ProSIGNAL | Applicazione blueprint al caso ING ProSIGNAL | WBS applicativa ProSIGNAL | Cliente esterno, priorità alta |
| 9.1 | 2 | Pacchetto requisiti ProSIGNAL | Perimetro dati, tracciati, output e controlli confermati | Dossier requisiti ProSIGNAL | Oggi parzialmente documentato |
| 9.1.1 | 3 | Tracciati e file inventory | Inventario file, dimensioni, formato, header/tail, versioni | Inventario tracciati/file | Richiede materiale cliente |
| 9.1.1.1 | 4 | Scheda file/tracciato validata | Scheda per ogni tracciato disponibile | Schede tracciato validate | Da chiarire se file non forniti |
| 9.2 | 2 | Pipeline ProSIGNAL target | Applicazione di ingestion, parsing, controlli, output e dashboard al caso | Disegno pipeline ProSIGNAL | Non ancora implementazione certa |
| 9.2.1 | 3 | Output e controlli ProSIGNAL | Output regolamentari, aggregazioni, scostamenti, cross-file checks | Catalogo controlli/output ProSIGNAL | Basato su appunti |
| 9.2.1.1 | 4 | Piano di collaudo ProSIGNAL preliminare | Casi test per tracciati, file grandi, controlli e output | Piano collaudo preliminare | Work package stimabile |
| 10 | 1 | Stream applicativo Kiron CDG | Applicazione blueprint al caso Kiron CDG | WBS applicativa Kiron | Cliente esterno, priorità alta |
| 10.1 | 2 | Pacchetto requisiti Kiron | Perimetro Actual, Forecast, fonti, tabelle guida e output | Dossier requisiti Kiron | Source-grounded su materiali cdg-kiron |
| 10.1.1 | 3 | Fonti e dizionari Kiron | Campus, Campus 2.0, Zucchetti, campi input/output, TG/RIB/STEP | Inventario fonti e regole Kiron | Alcuni open point da validare |
| 10.1.1.1 | 4 | Schede fonti e regole Kiron | Schede per fonte, tabella guida e regola documentata | Schede Kiron validate | Work package stimabile |
| 10.2 | 2 | Pipeline Kiron target | Applicazione blueprint ad Actual, Forecast e BI | Disegno pipeline Kiron | Scenario tecnico da decidere |
| 10.2.1 | 3 | Data product Kiron | DB Actual gestionale, DB Actual, DB Forecast | Catalogo data product Kiron | Basato su materiali Kiron |
| 10.2.1.1 | 4 | Piano di collaudo Kiron preliminare | Casi test per Actual, Forecast, regole e output BI | Piano collaudo preliminare | Work package stimabile |
| 11 | 1 | Stream applicativo CDG interno | Applicazione e consolidamento blueprint su reference interna | WBS applicativa CDG interno | Reference implementation |
| 11.1 | 2 | Pacchetto requisiti CDG interno | Perimetro P1-P6, fonti, tabelle guida, output e dashboard | Dossier requisiti CDG interno | Fonte più completa |
| 11.1.1 | 3 | Processi P1-P6 | Actual ore, inframensile, linked issue, economics, ore SAP, forecast | Catalogo processi P1-P6 | Basato su docs CDG |
| 11.1.1.1 | 4 | Schede processo P1-P6 | Schede per ciascun processo con input, output, controlli e owner | Schede P1-P6 | Work package stimabile |
| 11.2 | 2 | Pipeline CDG interno target | Applicazione blueprint a raw/ref/stg/mart, controlli, dashboard e run | Disegno pipeline CDG interno | Deve verificare attualità repo |
| 11.2.1 | 3 | Data product CDG interno | Output P1-P6, mart BI-ready, dashboard CDG e tecnica | Catalogo data product CDG interno | Source-grounded |
| 11.2.1.1 | 4 | Piano di collaudo CDG interno preliminare | Casi test per P1-P6, quadrature e parallel run | Piano collaudo preliminare | Work package stimabile |
| 12 | 1 | Test, collaudo e readiness | Standard di verifica e preparazione al rilascio per blueprint e stream | Piano di collaudo e readiness | Area testing/collaudo e rilascio |
| 12.1 | 2 | Strategia di test blueprint | Strategia comune per test tecnici, funzionali, UAT e parallel run | Strategia di test | Non include date |
| 12.1.1 | 3 | Criteri di accettazione comuni | Criteri per dati accettati/scartati, output, log, dashboard e runbook | Criteri accettazione | Base per stima test |
| 12.1.1.1 | 4 | Test catalog blueprint | Catalogo test riusabili per i tre stream | Test catalog | Work package stimabile |
| 12.2 | 2 | Readiness rilascio | Condizioni minime per passare da blueprint a delivery/pilot | Checklist release readiness | Area rilascio |
| 12.2.1 | 3 | Checklist go-live/hypercare | Runbook, monitoraggio, ownership, gestione anomalie, backlog | Checklist go-live | Da adattare per progetto |
| 12.2.1.1 | 4 | Pacchetto readiness progetto | Set di checklist e criteri per ogni stream | Pacchetto readiness | Work package stimabile |
| 13 | 1 | Documentazione e handover | Pacchetto documentale per riuso, responsabilità e roadmap | Pacchetto documentazione/handover | Area documentazione/governance |
| 13.1 | 2 | Documentazione blueprint | Documento blueprint, standard, pattern, template e decision log | Handbook blueprint | Serve a rendere la blueprint riusabile |
| 13.1.1 | 3 | Libreria template e schede | Data contract, fonte, controllo, data product, runbook, dashboard | Libreria template | Deriva dai work package precedenti |
| 13.1.1.1 | 4 | Repository artifact blueprint | Cartella/indice degli artifact riusabili | Indice artifact blueprint | Work package stimabile |
| 13.2 | 2 | Roadmap e stima readiness | Preparazione della base per effort, RACI, roadmap, Gantt e milestone | Pacchetto PMO readiness | Non contiene ancora stime |
| 13.2.1 | 3 | Mapping WBS-to-estimate | Mappa work package -> profilo, effort da stimare, dipendenze, rischio | Template stima effort | Base per economics |
| 13.2.1.1 | 4 | Foglio stima e RACI preliminare | Struttura pronta per stima e assegnazione responsabilità | Template stima/RACI | Work package stimabile |

## 4. Vista gerarchica

```text
1. Governance e perimetro blueprint
  1.1 Perimetro e obiettivi confermati
    1.1.1 Mappa stakeholder e audience
      1.1.1.1 Registro stakeholder e ruoli decisionali
    1.1.2 Registro assunzioni e gap
      1.1.2.1 Log decisioni aperte
  1.2 Criteri di adozione blueprint
    1.2.1 Criteri di riuso
      1.2.1.1 Checklist di applicabilità progetto

2. Analisi funzionale e informativa
  2.1 Perimetro funzionale comune
    2.1.1 Componenti pipeline comuni
      2.1.1.1 Catalogo capability blueprint
  2.2 Requisiti informativi e output
    2.2.1 Data product CDG-like
      2.2.1.1 Schede data product P1-P6 / Actual / Forecast
    2.2.2 Data product ProSIGNAL
      2.2.2.1 Schede output ProSIGNAL preliminari

3. Architettura e scenari TO BE
  3.1 Architettura logica comune
    3.1.1 Layer dati e responsabilità
      3.1.1.1 Diagramma architettura logica
  3.2 Scenario AWS
    3.2.1 Mappa componenti AWS
      3.2.1.1 Scheda decisioni AWS
  3.3 Scenario Qlik/Talend
    3.3.1 Mappa componenti Qlik/Talend
      3.3.1.1 Scheda decisioni Qlik/Talend
  3.4 Confronto scenari
    3.4.1 Criteri di scelta
      3.4.1.1 Scheda trade-off per comitato

4. Data governance e data contract
  4.1 Data contract template
    4.1.1 Contract per fonti CDG-like
      4.1.1.1 Modello scheda fonte CDG-like
    4.1.2 Contract per file ProSIGNAL
      4.1.2.1 Modello scheda tracciato fixed-column
  4.2 Reference data framework
    4.2.1 Ownership reference data
      4.2.1.1 Registro reference data

5. Ingestion, landing e raw layer
  5.1 Pattern ingestion riusabili
    5.1.1 Pattern API/database
      5.1.1.1 Scheda pattern connettore
    5.1.2 Pattern file grandi
      5.1.2.1 Scheda pattern file ingestion
  5.2 Raw/source-faithful layer
    5.2.1 Convenzioni raw/staging
      5.2.1.1 Convenzioni di naming e metadata

6. Quality, audit e controllo del dato
  6.1 Quality gates comuni
    6.1.1 Controlli tecnici
      6.1.1.1 Schede controlli tecnici
    6.1.2 Controlli funzionali
      6.1.2.1 Schede controlli funzionali
  6.2 Audit trail e run history
    6.2.1 Modello log esecuzioni
      6.2.1.1 Specifica run log

7. Transform, mart e data product
  7.1 Pattern trasformazione
    7.1.1 Pattern CDG-like
      7.1.1.1 Scheda pattern Actual/Forecast
    7.1.2 Pattern ProSIGNAL
      7.1.2.1 Scheda pattern output regolamentare
  7.2 Mart/output standard
    7.2.1 Catalogo data product
      7.2.1.1 Schede accettazione data product

8. Presentation, workflow e consumo
  8.1 Presentation layer blueprint
    8.1.1 Dashboard business e tecniche
      8.1.1.1 Wireframe dashboard tipo
  8.2 Workflow utente ed eccezioni
    8.2.1 Gestione scarti e rettifiche
      8.2.1.1 Scheda processo gestione scarti

9. Stream applicativo ProSIGNAL
  9.1 Pacchetto requisiti ProSIGNAL
    9.1.1 Tracciati e file inventory
      9.1.1.1 Scheda file/tracciato validata
  9.2 Pipeline ProSIGNAL target
    9.2.1 Output e controlli ProSIGNAL
      9.2.1.1 Piano di collaudo ProSIGNAL preliminare

10. Stream applicativo Kiron CDG
  10.1 Pacchetto requisiti Kiron
    10.1.1 Fonti e dizionari Kiron
      10.1.1.1 Schede fonti e regole Kiron
  10.2 Pipeline Kiron target
    10.2.1 Data product Kiron
      10.2.1.1 Piano di collaudo Kiron preliminare

11. Stream applicativo CDG interno
  11.1 Pacchetto requisiti CDG interno
    11.1.1 Processi P1-P6
      11.1.1.1 Schede processo P1-P6
  11.2 Pipeline CDG interno target
    11.2.1 Data product CDG interno
      11.2.1.1 Piano di collaudo CDG interno preliminare

12. Test, collaudo e readiness
  12.1 Strategia di test blueprint
    12.1.1 Criteri di accettazione comuni
      12.1.1.1 Test catalog blueprint
  12.2 Readiness rilascio
    12.2.1 Checklist go-live/hypercare
      12.2.1.1 Pacchetto readiness progetto

13. Documentazione e handover
  13.1 Documentazione blueprint
    13.1.1 Libreria template e schede
      13.1.1.1 Repository artifact blueprint
  13.2 Roadmap e stima readiness
    13.2.1 Mapping WBS-to-estimate
      13.2.1.1 Foglio stima e RACI preliminare
```

## 5. Aree mancanti o ambigue

- **ProSIGNAL:** mancano file campione, tracciati reali completi, esempi output e regole di accettazione cliente.
- **ProSIGNAL:** il fit su file molto grandi, fixed-column e controlli cross-file va validato tecnicamente.
- **Kiron CDG:** alcune regole e modalità operative risultano da definire o da rivedere con Kiron.
- **Kiron CDG:** va chiarito se Oracle BI è vincolo cliente o semplice riferimento nel materiale analizzato.
- **Kiron CDG:** va chiarito quanto della soluzione prevista su OutSystems sia vincolo applicativo e quanto pattern trasferibile.
- **CDG interno:** va verificato quanto il materiale CDG sia ancora allineato al repository/pipeline corrente.
- **Scenari tecnologici:** non è confermato quale scenario sarà adottato; la WBS mantiene deliverable di confronto.
- **Qlik/Talend:** entitlement, capacity, runtime, capability incluse e limiti contrattuali non sono confermati.
- **AWS:** RDS vs database cliente, ECS vs EC2 e presenza di landing object storage restano decisioni aperte.
- **Governance BI:** access control, publishing, embedding/export e modello operativo vanno dettagliati se emergono vincoli cliente.

## 6. Rischi e attenzioni da Senior PM / Senior Analyst

- **Scope creep:** la blueprint può facilmente diventare la somma di tre delivery complete. Va mantenuta la distinzione tra standard riusabile e implementazione specifica.
- **Duplicazioni:** data contract, quality gates, run log e dashboard non devono essere riscritti tre volte; vanno prodotti come standard e poi specializzati.
- **Deliverable impliciti:** runbook, test catalog, data product catalog, ownership reference data e decision log non erano sempre espliciti, ma sono necessari per stimare e governare il lavoro.
- **Dipendenze critiche:** la scelta scenario influenza competenze, costi, operation, licensing, collaudo e piano di rilascio.
- **Documentazione disomogenea:** CDG interno e Kiron sono molto più documentati di ProSIGNAL. La stima ProSIGNAL avrà un margine di incertezza maggiore.
- **Tecnologia vs processo:** il rischio è presentare Dagster/dbt/Metabase o Qlik/Talend come WBS. La WBS deve restare orientata a deliverable e risultati.
- **Collaudo sottostimato:** controlli dati, quadrature, UAT, parallel run e gestione scarti sono centrali; non devono essere trattati come attività finali minori.
- **Economics prematuri:** il range Qlik 50 GB / 30k-50k EUR è un'ipotesi di discussione, non una quotazione. Non va usato per stime definitive.
- **Ownership dati:** senza owner chiari per campi, mapping, tabelle guida e controlli, la blueprint rischia di essere tecnicamente corretta ma difficile da esercire.
- **Riuso non automatico:** il riuso richiede template, naming, runbook, test catalog e criteri di adozione. Non basta usare gli stessi tool.

## 7. Suggerimenti per la fase successiva

- **Stima effort:** usare i work package di livello 4 come unità base di stima. Per ciascuno indicare profilo richiesto, complessità, incertezza e dipendenze.
- **Matrice responsabilità:** costruire una RACI per macro-area WBS, distinguendo owner business, owner dati, architect, data engineer, BI owner, QA/UAT e PM.
- **Roadmap:** trasformare i livelli 1-2 in stream di roadmap: blueprint core, scenario decision, data governance, ingestion, quality, data product, project stream, test/readiness.
- **Gantt:** derivare sequenza e dipendenze solo dopo la stima. La WBS non contiene date, ma evidenzia i deliverable da schedulare.
- **Milestone:** proporre milestone legate a deliverable verificabili: perimetro approvato, architettura approvata, data contract baseline, quality framework, stream readiness, test catalog, pacchetto stima/RACI.
- **Piano di collaudo:** partire da `12.1.1.1 Test catalog blueprint`, poi specializzare casi test per ProSIGNAL, Kiron e CDG interno.
- **Economics:** usare `13.2.1.1 Foglio stima e RACI preliminare` come base per range economici, separando setup blueprint, implementazione progetto e run/licenze.

## Grill-with-docs / Critic / Review

- **Grill-with-docs:** il termine "blueprint" resta coerente con il glossario e con i draft: non è un tool, ma un modello riusabile di standard, template, pattern, controlli e criteri di adozione.
- **Grill-with-docs:** la WBS ora parte dai macro-deliverable e non da una cronologia di attività. Le fasi temporali saranno derivate dopo, in roadmap/Gantt.
- **Critic:** la WBS è più adatta alla stima, ma resta ampia. Prima di stimare conviene congelare il perimetro: blueprint core soltanto, oppure blueprint più predisposizione dei tre stream.
- **Critic:** ProSIGNAL è ancora il punto più debole per grounding. La WBS lo segnala come rischio invece di trasformare ipotesi in certezze.
- **Review:** i deliverable finali sono verificabili, numerati e tracciabili. Non sono state introdotte date, effort o costi.
- **Humanize:** la WBS deve aiutare il comitato a vedere cosa stiamo comprando davvero: non tre pipeline isolate, ma un kit riusabile che poi viene adattato ai tre casi.
