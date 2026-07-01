# Blueprint And Project WBS

## Scopo

Questo documento separa due livelli che nel deck rischiano di sovrapporsi:

- **WBS della blueprint:** lavoro necessario per creare un modello riusabile di data pipeline, indipendente dal singolo cliente.
- **WBS dei progetti:** lavoro necessario per applicare la blueprint a ProSIGNAL, Kiron CDG e CDG interno.

La logica resta quella richiesta da Gianfranco: primo livello per **processi**, secondo livello per **funzioni**. La WBS non deve diventare una lista di tool. I tool servono solo a spiegare come alcuni processi possono essere realizzati nei due scenari TO BE.

## Assunzioni usate

- La blueprint non sceglie ancora una tecnologia vincente tra Dagster/dbt/Metabase su AWS e Talend/Qlik.
- ProSIGNAL e Kiron CDG restano i casi prioritari perché clienti esterni.
- CDG interno resta la reference implementation più documentata e utile per validare standard, convenzioni e riuso.
- Per ProSIGNAL, dove mancano esempi reali di file/tracciati/output, le voci restano basate sui materiali disponibili e su pattern comuni di file ingestion e controlli regolamentari.
- Nessuna voce WBS contiene effort, date o commitment economici.

## WBS generica della blueprint

Questa WBS descrive il lavoro per costruire la **capability riusabile**. Non è la WBS di un progetto cliente.

```text
Data Pipeline Blueprint
  1. Governo e modello di adozione
    1.1 Definizione obiettivi della blueprint
    1.2 Criteri di confronto tra scenari AWS e Qlik/Talend
    1.3 Regole di riuso tra progetti
    1.4 Ruoli, ownership e responsabilità operative
    1.5 Registro assunzioni, gap e decisioni aperte

  2. Capability model comune
    2.1 Mappa componenti pipeline
    2.2 Separazione tra componenti comuni e adattamenti progetto
    2.3 Standard per sorgenti, ingestion, qualità, mart e presentation
    2.4 Pattern per file, API, database e sistemi applicativi
    2.5 Criteri di fit per casi CDG-like e file-processing

  3. Data contract e metadata governance
    3.1 Template data contract per fonte
    3.2 Versionamento campi, tracciati e dizionari
    3.3 Ownership di campi, regole e mapping
    3.4 Reference data e tabelle guida
    3.5 Regole di storicizzazione e retention

  4. Ingestion e raw layer riusabile
    4.1 Pattern connettori API, file e database
    4.2 Landing/raw source-faithful
    4.3 Registro file, run e caricamenti
    4.4 Gestione file grandi e processing asincrono
    4.5 Standard per errori tecnici e retry

  5. Quality gates e audit
    5.1 Controlli formato e struttura
    5.2 Controlli funzionali e quadrature
    5.3 Gestione scarti e anomalie
    5.4 Quality report e audit trail
    5.5 Run history, lineage e verificabilità degli esiti

  6. Transform, mart e data product
    6.1 Parsing e normalizzazione
    6.2 Mapping e arricchimento semantico
    6.3 Regole business e calcoli di dominio
    6.4 Mart/output BI-ready
    6.5 Pattern di export e output operativi

  7. Presentation, workflow e consumo
    7.1 Dashboard e analytics
    7.2 Export per processi operativi o regolamentari
    7.3 Workflow utente e gestione eccezioni
    7.4 Accessi, profili e publishing
    7.5 Separazione tra motore dati e layer applicativo

  8. Test, run e riuso progressivo
    8.1 Test tecnici e funzionali
    8.2 UAT e parallel run
    8.3 Runbook e monitoraggio operativo
    8.4 Packaging asset riusabili
    8.5 Backlog evolutivo della blueprint
```

### Sintesi visuale per slide

Per una slide executive, evitare di mostrare tutti i livelli. Usare 8 blocchi principali:

1. Governo
2. Capability model
3. Data contract
4. Ingestion/raw
5. Quality/audit
6. Transform/mart
7. Presentation/workflow
8. Run/riuso

Messaggio: **la blueprint è il kit riusabile che separa standard comuni e adattamenti progetto.**

## WBS progetto - ING ProSIGNAL

ProSIGNAL applica la blueprint al caso più diverso dai CDG: file grandi, tracciati fixed-column, controlli e output regolamentari.

```text
ING ProSIGNAL
  1. Intake e tracciati
    1.1 Upload manuale iniziale
    1.2 Registro file ricevuti
    1.3 Gestione formato DOS / non UNIX
    1.4 Definizione tracciati fixed-column
    1.5 Versionamento campi e tipi

  2. Ingestion e gestione file grandi
    2.1 Landing file originale
    2.2 Gestione file fino a volumi elevati
    2.3 Processing asincrono
    2.4 Run log caricamenti
    2.5 Retention selettiva input/output

  3. Parsing e validazione tecnica
    3.1 Parsing per range colonne
    3.2 Controllo lunghezza record
    3.3 Header record checks
    3.4 Tail record checks
    3.5 Numero righe e formato

  4. Controlli funzionali
    4.1 Aggregazioni per forma tecnica
    4.2 Quantità, importi e numero operazioni
    4.3 Scostamento andamentale
    4.4 Controlli incrociati file decadali
    4.5 Audit regole applicate

  5. Manipolazione e output
    5.1 Filtri e ordinamenti
    5.2 Modifiche massive controllate
    5.3 Import e merge dati
    5.4 Export output regolamentari
    5.5 Storicizzazione esiti

  6. Operatività e governance
    6.1 Dashboard controllo esiti
    6.2 Gestione errori e scarti
    6.3 Workflow utente
    6.4 Runbook operativo
    6.5 Backlog verifiche su tracciati reali
```

### Lettura per il comitato

ProSIGNAL è lo stress test della blueprint su file processing, performance, controlli e audit. Se la blueprint regge questo caso, aumenta la fiducia sulla sua riusabilità oltre i progetti CDG-like.

## WBS progetto - Kiron CDG

Kiron CDG applica la blueprint a un caso cliente esterno CDG-like, con Actual, Forecast, tabelle guida e integrazione BI.

```text
Kiron CDG
  1. Project management e coordinamento
    1.1 Gestione progetto e SAL
    1.2 Coordinamento cliente e stakeholder
    1.3 Gestione open point funzionali
    1.4 Allineamento piano e WBS

  2. Actual
    2.1 Set up e analisi funzionale
    2.2 Acquisizione fonti Campus, Campus 2.0 e Zucchetti
    2.3 Normalizzazione dati gestionali e contabili
    2.4 Regole di ribaltamento, standard e conguagli
    2.5 Output DB Actual gestionale e DB Actual

  3. Configurator e tabelle guida
    3.1 Anagrafiche prodotti, istituti e reti
    3.2 Mapping bilancio e voci con standard
    3.3 Parametri modificabili dalla Direzione
    3.4 Regole RIB e STEP
    3.5 Validazione regole e ownership

  4. Forecast
    4.1 Regole e parametri forecast
    4.2 Motore calcolo forecast
    4.3 Viste mensili, trimestrali e annuali
    4.4 Output DB Forecast
    4.5 Validazione processo Forecast

  5. Presentation e integrazione BI
    5.1 DB di frontiera
    5.2 Pubblicazione verso BI direzionale
    5.3 Monitor esecuzione processi
    5.4 Monitor risultati elaborati
    5.5 Gestione rettifiche e controlli utente

  6. UAT e rilascio
    6.1 Test interno
    6.2 UAT cliente
    6.3 Rilascio Actual
    6.4 Rilascio Forecast
    6.5 Runbook e hypercare
```

### Lettura per il comitato

Kiron è il caso CDG-like esterno più utile per verificare quanto la blueprint sia trasferibile da una reference interna a un contesto cliente, con fonti, regole e BI diverse.

## WBS progetto - CDG interno

CDG interno resta la reference implementation più documentata. La WBS è analoga a Kiron, ma le funzioni sono ancorate ai processi P1-P6.

```text
CDG interno
  1. Project management e coordinamento
    1.1 Gestione progetto e SAL interni
    1.2 Coordinamento owner CDG
    1.3 Validazione processi P1-P6
    1.4 Gestione open point e backlog

  2. Fonti e data contract
    2.1 Jira e Tempo
    2.2 SAP
    2.3 CDG app
    2.4 Organico e file forecast
    2.5 Dizionari campi e tabelle guida

  3. Actual ore e controlli inframensili
    3.1 P1 Actual Ore Mensile
    3.2 P2 Actual Ore Inframensile
    3.3 Linked issue e account checks
    3.4 WBS chiuse e controlli di coerenza
    3.5 Storicizzazione output actual

  4. Economics e integrazione ore
    4.1 P3 Linked Issue / Ore secondarie
    4.2 P4 Actual Economics
    4.3 P5 Ore SAP per Economics
    4.4 Ribaltamenti costi e margini
    4.5 Output mart BI-ready

  5. Forecast
    5.1 P6 Forecast
    5.2 Normalizzazione iniziative
    5.3 Versioni e probabilità
    5.4 Storicizzazione forecast
    5.5 Viste forecast per analisi direzionale

  6. BI, governance e run
    6.1 Dashboard CDG
    6.2 Dashboard tecnica
    6.3 Logging e monitoraggio
    6.4 Profili e matrice accessi
    6.5 Parallel run, runbook e hypercare
```

### Lettura per il comitato

CDG interno serve a ridurre il rischio della blueprint: è il caso più documentato, ha processi P1-P6 già descritti e permette di consolidare convenzioni prima di applicarle su clienti esterni.

## Matrice di relazione Blueprint / Progetti

| Processo blueprint | ProSIGNAL | Kiron CDG | CDG interno |
|---|---|---|---|
| Governo e modello di adozione | priorità cliente esterno, fit file processing | priorità cliente esterno, fit CDG-like | reference interna e riuso |
| Capability model | file ingestion e controlli regolamentari | Actual / Forecast / BI | P1-P6, actual, economics, forecast |
| Data contract | tracciati fixed-column, versioni, DOS/non UNIX | Campus, Campus 2.0, Zucchetti, TG/RIB/STEP | Jira, Tempo, SAP, CDG app, tabelle guida |
| Ingestion/raw | file grandi, upload, landing | connettori gestionali e contabili | API/file/report e raw/ref/stg/mart |
| Quality/audit | header/tail, righe, scostamenti, controlli cross-file | riconciliazioni e regole direzionali | linked issue, WBS chiuse, quadrature |
| Transform/mart | parsing, aggregazioni, export regolamentari | ribaltamenti, Actual, Forecast | P1-P6, economics, ore SAP, forecast |
| Presentation/workflow | dashboard esiti, gestione scarti, workflow utente | BI direzionale e monitor processi | dashboard CDG e tecnica |
| Run/riuso | runbook su file e tracciati | runbook Actual/Forecast | convenzioni e asset riusabili |

## Prompt per generare immagini WBS

### Prompt comune di stile

```text
Crea un'infografica 16:9 in stile corporate consulenziale Novigo/TXT.
Sfondo bianco, molto spazio vuoto, look minimal, font sans-serif moderno.
Usa palette azzurro, turchese e verde acqua con gradiente coerente Novigo.
Non modificare o ridisegnare loghi. Se serve indicare branding, lascia spazio neutro in alto a sinistra.
Usa bordi sottili arrotondati, icone outline semplici, linee leggere e gerarchia chiara.
La struttura deve sembrare una WBS / mind map / XMind executive: primo livello processi, secondo livello funzioni.
Evita paragrafi lunghi. Usa etichette brevi e leggibili.
Non inventare effort, date, costi o tecnologie non indicate.
Lingua: italiano, tono C-level, chiaro e non tecnico.
```

### Immagine 1 - WBS generica blueprint

```text
Usa il prompt comune di stile.

Titolo: "WBS generica della Data Pipeline Blueprint"
Messaggio: "La blueprint è il kit riusabile che separa standard comuni e adattamenti progetto."

Struttura visuale consigliata:
Nodo centrale: "Data Pipeline Blueprint"
Otto rami principali, disposti a mappa radiale o a due righe da quattro card:
1. Governo
   - obiettivi
   - criteri scenario
   - ownership
   - decisioni aperte
2. Capability model
   - componenti pipeline
   - standard comuni
   - pattern file/API/DB
   - fit CDG-like e file-processing
3. Data contract
   - template fonte
   - versioni campi/tracciati
   - reference data
   - retention
4. Ingestion/raw
   - connettori
   - landing/raw
   - run log
   - file grandi
5. Quality/audit
   - controlli formato
   - quadrature
   - scarti
   - audit trail
6. Transform/mart
   - parsing
   - mapping
   - regole business
   - data product
7. Presentation/workflow
   - dashboard
   - export
   - workflow
   - accessi
8. Run/riuso
   - test
   - UAT
   - runbook
   - asset riusabili
```

### Immagine 2 - WBS ProSIGNAL

```text
Usa il prompt comune di stile.

Titolo: "WBS ING ProSIGNAL"
Messaggio: "ProSIGNAL stressa la blueprint su file grandi, tracciati, controlli e output regolamentari."

Nodo centrale: "ING ProSIGNAL"
Sei rami principali:
1. Intake e tracciati
   - upload manuale
   - registro file
   - formato DOS
   - tracciati fixed-column
2. Ingestion file grandi
   - landing originale
   - processing asincrono
   - run log
   - retention selettiva
3. Parsing e validazione
   - range colonne
   - lunghezza record
   - header/tail
   - righe e formato
4. Controlli funzionali
   - forma tecnica
   - quantità/importi/operazioni
   - scostamenti
   - controlli cross-file
5. Manipolazione e output
   - filtri
   - merge
   - export regolamentari
   - storicizzazione esiti
6. Operatività
   - dashboard esiti
   - errori/scarti
   - workflow utente
   - runbook
```

### Immagine 3 - WBS Kiron CDG

```text
Usa il prompt comune di stile.

Titolo: "WBS Kiron CDG"
Messaggio: "Kiron applica la blueprint a un caso CDG-like esterno con Actual, Forecast e BI direzionale."

Nodo centrale: "Kiron CDG"
Sei rami principali:
1. PM e coordinamento
   - progetto e SAL
   - stakeholder
   - open point
   - piano e WBS
2. Actual
   - setup e analisi
   - Campus / Campus 2.0 / Zucchetti
   - normalizzazione
   - DB Actual
3. Configurator
   - prodotti
   - istituti e reti
   - mapping bilancio
   - regole RIB/STEP
4. Forecast
   - parametri forecast
   - motore calcolo
   - viste temporali
   - DB Forecast
5. BI e monitoraggio
   - DB frontiera
   - BI direzionale
   - monitor processi
   - gestione rettifiche
6. UAT e rilascio
   - test interno
   - UAT cliente
   - rilascio Actual/Forecast
   - runbook e hypercare
```

### Immagine 4 - WBS CDG interno

```text
Usa il prompt comune di stile.

Titolo: "WBS CDG interno"
Messaggio: "CDG interno consolida la reference implementation della blueprint sui processi P1-P6."

Nodo centrale: "CDG interno"
Sei rami principali:
1. PM e coordinamento
   - SAL interni
   - owner CDG
   - processi P1-P6
   - backlog
2. Fonti e data contract
   - Jira/Tempo
   - SAP
   - CDG app
   - tabelle guida
3. Actual ore
   - P1 mensile
   - P2 inframensile
   - linked issue checks
   - storicizzazione
4. Economics e ore
   - P3 ore secondarie
   - P4 economics
   - P5 ore SAP
   - ribaltamenti e margini
5. Forecast
   - P6 forecast
   - iniziative
   - versioni e probabilità
   - viste forecast
6. BI e run
   - dashboard CDG
   - dashboard tecnica
   - logging
   - parallel run e runbook
```

## grill-with-docs

- **Termine "blueprint":** nei materiali non indica un tool o una singola architettura, ma un modello riusabile di componenti, standard, criteri e asset. La WBS generica deve quindi produrre capability e regole, non implementare ProSIGNAL/Kiron/CDG.
- **Termine "WBS":** in coerenza con Gianfranco, il primo livello deve essere per processi, non per tecnologie. Per questo le tecnologie compaiono solo come possibili modalità di realizzazione dentro i processi.
- **Confine blueprint/progetto:** la blueprint definisce standard e kit riusabile; i progetti applicano quel kit a fonti, regole, output e vincoli specifici.
- **Scenario concreto:** se domani arriva un quarto progetto data-intensive, la WBS blueprint resta valida; si crea una nuova WBS progetto mappata sugli stessi processi comuni.
- **Nessun ADR necessario:** la distinzione è una scelta di presentazione e metodo per questo deck, non una decisione architetturale hard-to-reverse del repository.

## Critic

- Rischio: la WBS blueprint potrebbe sembrare troppo astratta. Mitigazione: ogni processo include funzioni concrete e deliverable impliciti, come template data contract, run log, quality report, runbook e asset riusabili.
- Rischio: le WBS specifiche potrebbero sembrare troppo diverse tra loro. Mitigazione: la matrice Blueprint/Progetti mostra il filo comune.
- Rischio: ProSIGNAL contiene ancora ipotesi. Mitigazione: il documento dichiara che mancano esempi reali di file, tracciati e output.
- Rischio: tool-driven narrative. Mitigazione: le WBS sono organizzate per processi e funzioni, non per Dagster, dbt, Metabase, Talend o Qlik.
- Rischio: commitment implicito. Mitigazione: nessuna durata, effort, costo o data è introdotta.

## Review

- La WBS generica della blueprint è presente e separata dalle WBS progetto.
- Le tre WBS specifiche sono presenti: ProSIGNAL, Kiron CDG, CDG interno.
- La struttura rispetta il criterio processo/funzioni richiesto.
- Il contenuto resta neutrale rispetto ai due scenari TO BE.
- I prompt per immagini sono pronti per ChatGPT o per un tool visuale.
- Le assunzioni e i limiti sono espliciti.

## Humanize

La WBS deve aiutare il comitato a capire una cosa semplice: non stiamo proponendo tre progetti scollegati. Stiamo proponendo una blueprint comune, che poi viene adattata a tre casi diversi. ProSIGNAL testa la robustezza su file e controlli regolamentari; Kiron testa il riuso su un cliente CDG-like; CDG interno consolida la reference implementation.
