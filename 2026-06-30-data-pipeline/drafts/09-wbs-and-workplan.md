# WBS And Workplan

## Scopo

Definire una prima WBS per i tre casi target e un piano di lavoro comune derivato.

La WBS e' organizzata per processi e funzioni, in stile XMind. Dove mancano fonti, le voci sono marcate come best practice / ipotesi di lavoro.

Per i casi CDG-like, la WBS Kiron puo' essere usata come modello operativo anche per il CDG interno: cambiano fonti, regole e output specifici, ma la struttura di delivery resta analoga.

## Priorita' Casi Target

1. **ING ProSIGNAL** - cliente esterno, priorita' alta.
2. **Kiron CDG** - cliente esterno, priorita' alta, con analisi funzionale, dizionari, struttura Jira e piano di lavoro disponibili.
3. **CDG interno** - reference implementation e caso sorgente documentato.

## WBS - ING ProSIGNAL

Fonte: appunti ProSignal + best practice / ipotesi di lavoro.

```text
ING ProSIGNAL
  1. Intake e gestione file
    1.1 Upload manuale iniziale
    1.2 Registro file ricevuti
    1.3 Gestione formato DOS / non UNIX
    1.4 Gestione file grandi
  2. Tracciati e metadati
    2.1 Definizione tracciati fixed-column
    2.2 Versionamento tracciati
    2.3 Mapping campi e tipi
    2.4 Gestione tracciati Lease e Conto Arancio
  3. Parsing e validazione
    3.1 Parsing per range colonne
    3.2 Validazione lunghezza record
    3.3 Header record checks
    3.4 Tail record checks
    3.5 Controlli numero righe
  4. Controlli funzionali
    4.1 Aggregazioni per forma tecnica
    4.2 Quantita'
    4.3 Importo
    4.4 Numero operazioni
    4.5 Scostamento andamentale
    4.6 Controlli incrociati file decadali
  5. Manipolazione ed export
    5.1 Filtri e ordinamenti
    5.2 Modifiche massive
    5.3 Import & merge
    5.4 Export output
  6. Output regolamentari
    6.1 Preparazione output per segnalazioni
    6.2 Storicizzazione output
    6.3 Audit output generati
  7. Presentation e operativita'
    7.1 Dashboard controllo esiti
    7.2 Log elaborazioni
    7.3 Gestione errori/scarti
    7.4 Workflow utente
```

## WBS - Kiron CDG

Fonte: `source-materials/cdg-kiron/` (`Analisi funzionale`, `Campi Input`, `Campi Output`, `Campi Tabelle e Regole`, import struttura Jira, piano di lavoro).

```text
Kiron CDG
  1. Project management e coordinamento
    1.1 Gestione e coordinamento progettuale
    1.2 SAL interni e con cliente
  2. Actual
    2.1 Set up e analisi
      2.1.1 Analisi funzionale
      2.1.2 Validazione AFU
      2.1.3 Analisi tecnica
    2.2 Web App / base dati
      2.2.1 Configurazione sezione Kiron CDG su Campus 2.0
      2.2.2 Disegno e realizzazione base dati
      2.2.3 DevOps
      2.2.4 Monitor esecuzione processi
      2.2.5 Monitor risultati elaborazione e modifica manuale
    2.3 Data import
      2.3.1 Connettori automatici da Campus
      2.3.2 Connettori automatici da Zucchetti Infinity
      2.3.3 Test interno
    2.4 Configurator
      2.4.1 Regole di normalizzazione
      2.4.2 Standard/proxy mensili in assenza di consuntivo
      2.4.3 Test interno
    2.5 Data management
      2.5.1 Regole di normalizzazione e standard
      2.5.2 Ribaltamento costi su Area, Prodotto, Istituto
      2.5.3 Test interno
    2.6 Data output
      2.6.1 DB di frontiera per integrazione/pubblicazione verso Oracle BI
      2.6.2 Test interno
      2.6.3 Rilascio e validazione processo Actual
  3. Forecast
    3.1 Configurator forecast
      3.1.1 Regole e parametri forecast
      3.1.2 Test interno
    3.2 Data management forecast
      3.2.1 Motore calcolo regole e parametri forecast
      3.2.2 Test interno
    3.3 Data output forecast
      3.3.1 Tabelle forecast nel DB di frontiera
      3.3.2 Test interno
      3.3.3 Rilascio e validazione processo Forecast
  4. UAT e rilascio
    4.1 UAT cliente
    4.2 Gestione rilascio/deploy
    4.3 Open point UI/UX e UAT separata
```

## WBS - CDG Interno

Fonte: `04-internal-cdg-analysis.md`, `cdg-data-pipeline-docs`, repo `cdg-data-pipeline`.

La WBS del CDG interno puo' essere presentata con la stessa ossatura Kiron:

```text
CDG interno
  1. Project management e coordinamento
    1.1 Gestione e coordinamento progettuale
    1.2 SAL interni e stakeholder CDG
  2. Actual
    2.1 Set up e analisi
      2.1.1 Analisi funzionale processi P1-P5
      2.1.2 Validazione regole e output con owner CDG
      2.1.3 Analisi tecnica su repo/pipeline esistente
    2.2 Applicazione / base dati
      2.2.1 Configurazione fonte Jira/Tempo/Excel/SAP/CDG app
      2.2.2 Disegno e realizzazione layer raw/ref/stg/mart
      2.2.3 DevOps e orchestrazione job
      2.2.4 Monitor esecuzione processi
      2.2.5 Monitor risultati e gestione rettifiche/reference data
    2.3 Data import
      2.3.1 Ingestion Jira e Tempo
      2.3.2 Ingestion Excel/SAP/CDG app dove applicabile
      2.3.3 Test interno
    2.4 Configurator
      2.4.1 Tabelle guida e mapping CDG
      2.4.2 Regole di normalizzazione e ribaltamento
      2.4.3 Test interno
    2.5 Data management
      2.5.1 Normalizzazione ore, WBS, team, account
      2.5.2 Economics, ribaltamenti e integrazione ore/economics
      2.5.3 Test interno
    2.6 Data output
      2.6.1 Output P1-P5 e mart BI-ready
      2.6.2 Test interno
      2.6.3 Rilascio e validazione processi Actual
  3. Forecast
    3.1 Configurator forecast
      3.1.1 Regole e parametri P6 Forecast
      3.1.2 Test interno
    3.2 Data management forecast
      3.2.1 Motore calcolo e storicizzazione forecast
      3.2.2 Test interno
    3.3 Data output forecast
      3.3.1 Output P6 e viste forecast
      3.3.2 Test interno
      3.3.3 Rilascio e validazione Forecast
  4. UAT e rilascio
    4.1 UAT owner CDG
    4.2 Parallel run / confronto con processo corrente
    4.3 Rilascio, runbook e hypercare
```

Vista funzionale CDG interno da mantenere come dettaglio o appendice della WBS:

```text
CDG interno - processi e output
  1. P1 Actual Ore Mensile
    1.1 Normalizzazione rilevazioni
    1.2 Arricchimento risorsa/team/WBS
    1.3 Storicizzazione output mensile
  2. P2 Actual Ore Inframensile
    2.1 Controlli linked issue/account
    2.2 Controlli WBS chiuse
    2.3 Output non storicizzato
  3. P3 Linked Issue / Ore secondarie
    3.1 Analisi storico actual
    3.2 Calcolo ore secondarie
  4. P4 Actual Economics
    4.1 Ricavi/costi/fatturato per WBS
    4.2 Ribaltamento costi
    4.3 Margine, EBITDA LOB, EBITDA
  5. P5 Ore SAP per Economics
    5.1 Raggruppamento ore SAP
    5.2 Integrazione ore/economics
  6. P6 Forecast
    6.1 Storico forecast
    6.2 Normalizzazione iniziative
    6.3 Versioni e probabilita'
```

## Piano Di Lavoro Comune

Il piano e' espresso in fasi comuni. Le durate non sono indicate per evitare stime non fondate.

| Fase | Obiettivo | Attivita' comuni | Output | Note |
|---|---|---|---|---|
| 1. Assessment e perimetro | Capire fonti, processi, output e vincoli | interviste, inventario fonti, mappa output, gap tecnici | perimetro e source inventory | priorita' a ProSIGNAL/Kiron |
| 2. Blueprint e criteri scenario | Definire componenti comuni e criteri di scelta | capability map, data contracts, criteri confronto | blueprint logica | include scelta scenario |
| 3. Architettura target | Disegnare scenario selezionato o pilot comparativo | schema cloud, runtime, DB, presentation, sicurezza | architecture brief | AWS ECS/EC2 o Qlik/Talend |
| 4. Data contracts e mapping | Stabilire tracciati, mapping, ownership | schema campi, tabelle guida, versioning | data contracts | critico per riuso |
| 5. Ingestion e landing/raw | Acquisire dati in modo auditabile | connettori, upload, landing, run log | raw/source-faithful layer | API e file |
| 6. Validazione e quality gates | Intercettare errori prima dei mart | controlli formato, header/tail, quadrature, scarti | quality report | specifico per progetto |
| 7. Transform e mart/output | Produrre data product utilizzabili | normalizzazione, arricchimento, calcoli, mart | output/mart | CDG P1-P6 o ProSignal outputs |
| 8. Presentation e workflow | Rendere fruibili output e controlli | dashboard, export, workflow utente | presentation layer | Metabase o Qlik |
| 9. Test e parallel run | Validare con utenti e dati campione | UAT, riconciliazione, confronto manuale | verbale validazione | riduce rischio go-live |
| 10. Go-live e run | Stabilizzare operativita' | scheduling, monitoraggio, runbook, hypercare | runbook e backlog | prepara riuso |

## Piano Per Priorita'

1. **ProSIGNAL:** avviare discovery mirata su file/tracciati e vincoli grandi volumi; decidere scenario su base fit file-processing + Qlik/Talend availability.
2. **Kiron CDG:** usare i materiali specifici come secondo caso CDG-like esterno; non trasformare gli effort del piano in commitment senza validazione.
3. **CDG interno:** usare una WBS delivery analoga a Kiron, innestandovi i processi P1-P6 e la reference implementation esistente.

## Economics Come Range

Per questa fase conviene usare tre viste:

- **Setup blueprint:** lavoro comune non ripetibile per ogni cliente.
- **Implementazione progetto:** effort per adattare sorgenti, mapping, controlli e output.
- **Run e licenze:** cloud/runtime, DB, BI/licensing, manutenzione.

Ipotesi iniziale da usare per lo scenario Qlik/Talend:

- piano 50 GB stimato dall'utente tra **30-50k EUR**;
- trattarlo come range di discussione, non come prezzo impegnativo;
- verificare periodo, IVA, sconti, utenti, capacity add-on, bundle e capability Talend/Qlik incluse prima di metterlo in una slide economica finale.

Range consigliato in slide:

```text
S / M / L
oppure
Basso / Medio / Alto
```

Usare il range 30-50k EUR solo come baseline provvisoria dichiarata. Non aggiungere altri valori economici fino a verifica licenze, hosting e perimetro.

## grill-with-docs

- La WBS CDG interno usa una struttura delivery analoga a Kiron e mantiene i processi P1-P6 come vista funzionale di dettaglio.
- La WBS Kiron e' ora source-grounded sui materiali `cdg-kiron`; ProSIGNAL mantiene best practice dichiarate dove mancano dettagli.
- Il piano comune rispetta il metodo Gianfranco: analisi, realizzazione, validazione, go-live/hypercare.

## Review

- Le tre WBS sono presenti.
- Il piano comune deriva dalle WBS e non introduce date o effort inventati.
- La convergenza Kiron/CDG interno e' esplicita: stesso modello di delivery, contenuti funzionali diversi.
- Le priorita' esterne ProSIGNAL/Kiron sono rispettate.
- Le assunzioni sono visibili.

## Humanize

La WBS non deve sembrare una lista tecnica fine a se stessa: serve a mostrare che Kiron e CDG interno possono condividere una struttura di lavoro molto simile, mentre ProSIGNAL resta lo stress test su file e controlli regolamentari.
