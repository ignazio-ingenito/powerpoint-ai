# Use Case Synthesis - Data Pipeline Blueprint

## Obiettivo Della Sintesi

Trasformare i materiali raccolti in una prima mappa ragionata dei casi d'uso e dei requisiti comuni della blueprint.

Questa non e' ancora la storyline del deck: serve a separare fatti, inferenze e gap prima di scrivere slide o creative handoff.

## Casi D'Uso Emersi

### CDG / Internal CDG

**Fonte principale:** repo `cdg-data-pipeline`, `cdg-data-pipeline-docs`, appunti Obsidian CDG.

CDG/Internal CDG e' il caso piu' concreto e meglio documentato. Descrive una pipeline gestionale che integra sorgenti diverse:

- Jira, con campi custom e query controllate;
- Tempo, per account/report e timesheet;
- Excel/file gestionali;
- dati SharePoint e output economici;
- mapping manuali/reference data gestiti da applicazione o tabelle dedicate.

Il bisogno ricorrente non e' solo "caricare dati", ma ricostruire un processo affidabile di controllo di gestione:

- storicizzare dati e/o fotografare dati alla data;
- normalizzare input eterogenei;
- gestire raccordi tra sistemi, account, WBS, organico e dati gestionali;
- produrre mart e output BI;
- rendere il processo ripetibile e governabile.

La documentazione Internal CDG descrive sei processi/output principali:

- P1 Actual Ore Mensile;
- P2 Actual Ore Inframensile;
- P3 Linked Issue / Ore secondarie;
- P4 Actual Economics;
- P5 Ore SAP per integrazione Economics;
- P6 Forecast.

**Implicazione blueprint:** Internal CDG e' il caso base per spiegare la catena `source -> ingestion -> raw/ref -> stg -> mart/output -> BI`, con processi P1-P6 come asset/job logici.

### ProSignal

**Fonte principale:** appunti Obsidian ProSignal nel vault indicato dall'utente, copiati in `source-materials/obsidian-txt-novigo/ProSignal/`.

ProSignal e' diverso da CDG e per questo e' utile per testare la riusabilita' della blueprint.

Il caso riguarda file testuali posizionali/fixed-column, anche molto grandi, ricevuti dall'ufficio Finance ING. Gli utenti fanno controlli sui file, spesso passando da Excel, e producono output che alimentano segnalazioni di vigilanza.

Requisiti emersi:

- tracciati modificabili: campi, tipi e versioni;
- file molto grandi, con riferimento a un massimo di 7 GB in crescita;
- upload manuale come prima fase;
- gestione di header e tail record quando presenti;
- controlli di integrita' o scostamento andamentale;
- aggregazioni per forma tecnica: quantita', importo, numero operazioni;
- controlli incrociati tra piu' file per i file decadali;
- output piu' importanti degli input ai fini retention;
- necessita' di apertura/modifica come testo puro, column mode, filtri e ordinamenti;
- vincolo formato DOS, non UNIX.

**Implicazione blueprint:** ProSignal forza la blueprint a coprire file ingestion, schema registry/tracciati, storage scalabile, processing asincrono, data quality, audit e retention. Non basta un pattern Jira/Tempo.

### Kiron CDG

**Fonte principale:** `source-materials/cdg-kiron/2025_KIR_004 - Analisi funzionale.docx`, `Campi Input.xlsx`, `Campi Output.xlsx`, `Campi Tabelle e Regole.xlsx`.

Kiron CDG e' ora un caso documentato. Il materiale descrive una soluzione di Controllo di Gestione per la Direzione Kiron, articolata in:

- **Actual:** produzione mensile di ricavi e costi consuntivi;
- **Forecast:** produzione periodica di valori previsionali a partire dagli actual;
- dimensioni di analisi: Periodo, Prodotto, Rete, Istituto;
- fonti: Campus, Campus 2.0 e Zucchetti Infinity;
- tabelle guida e regole: TG, RIB e STEP;
- output: base dati Actual gestionale, base dati Actual e base dati Forecast;
- consumo BI: base dati strutturata per strumenti di analisi direzionale, nel materiale indicata anche come BI Oracle.

**Implicazione blueprint:** Kiron rafforza la blueprint sul caso CDG economico-gestionale: ingestion da sistemi applicativi e contabili, riconciliazione, normalizzazione, regole configurabili, ribaltamenti, forecast e base dati BI-ready.

## Requisiti Comuni Della Blueprint

La blueprint dovrebbe essere disegnata come piattaforma leggera e componibile, con questi blocchi:

| Blocco | Perche' serve | Evidenza CDG | Evidenza ProSignal |
|---|---|---|---|
| Source adapters | Collegare sorgenti eterogenee senza riscrivere tutta la pipeline | Jira, Tempo, Excel, SharePoint | File fixed-column, file decadali, possibili elaborazioni esterne |
| Metadata/schema registry | Governare campi, custom field, tracciati e versioni | Jira field metadata e mapping YAML | Tracciati modificabili, Lease/Conto Arancio da verificare |
| Raw/source-faithful layer | Conservare audit e diagnosi senza perdere dettaglio | `raw_*`, payload e campi originali | File originali o rappresentazione fedele per controlli e retention selettiva |
| Staging semantic layer | Pulire e rendere leggibili i dati | `stg_*`, view Jira | Parsing fixed-column, header/tail, normalizzazione tipi |
| Mart/output layer | Esporre dati consumabili da BI/processo | `mart_*`, Metabase/Power BI | Excel di verifica, output per segnalazioni, aggregati |
| Reference data governance | Mantenere raccordi manuali e ownership | account, WBS, organico, mapping CDG | tracciati, regole di controllo, mapping forme tecniche |
| Orchestrazione | Distinguere ingestion, refresh e backfill | Dagster jobs e refresh SQL-only | upload manuale iniziale, processing asincrono, run decadali/mensili |
| Data quality & audit | Rendere spiegabili errori, scostamenti e drift | SLA error object, campi mancanti, drift schema | header/tail, scostamenti andamentali, controlli incrociati |
| Consumption & workflow | Separare UI/workflow da motore dati | Metabase/NocoDB/Power BI | OutSystems utile per UI/workflow, non per processing di file enormi |

Kiron aggiunge un'ulteriore evidenza CDG-like: Campus/Campus 2.0/Zucchetti come fonti, tabelle guida TG, regole RIB/STEP, output Actual/Forecast e integrazione verso BI.

## Principio Architetturale Da Portare Nel Deck

OutSystems, Power BI, Metabase o NocoDB possono essere ottimi layer di esperienza, workflow, configurazione o consumo.

La blueprint pero' deve evitare che il layer applicativo diventi il motore principale di ingestion e trasformazione per file grandi o processi dati ricorrenti. Il motore dati deve essere separato, osservabile, tracciabile e scalabile.

## Prime Ipotesi Di Storyline

1. **Perche' serve una blueprint:** CDG e ProSignal mostrano bisogni diversi ma ricorrenti: dati eterogenei, controlli, tracciati, output, audit e riuso.
2. **AS IS:** oggi ogni iniziativa rischia di ricostruire sorgenti, mapping, controlli e output in modo specifico.
3. **TO BE:** una pipeline blueprint con componenti riusabili e punti di estensione per sorgenti, tracciati, controlli e mart.
4. **Piano:** usare Internal CDG e Kiron come casi CDG-like documentati, validare ProSignal come stress test sui file grandi, e discutere quale blueprint regga entrambi i pattern.
5. **Economics/benefici:** riduzione effort ripetitivo, maggiore auditabilita', minore rischio operativo, accelerazione nuove iniziative.

## Gap Da Chiudere

- Confronto tra documentazione Internal CDG e implementazione corrente del repo `cdg-data-pipeline`.
- Chiarimenti Kiron su regole ancora marcate come da definire/open point nel materiale sorgente.
- Esempi file/tracciati/output ProSignal, soprattutto Lease e Conto Arancio, se disponibili e autorizzati.
- Limiti tecnici OutSystems sul caricamento file grandi, se il deck deve entrare nel disegno applicativo.
- Decisione se includere una parte economics oppure limitarsi a blueprint e roadmap.
