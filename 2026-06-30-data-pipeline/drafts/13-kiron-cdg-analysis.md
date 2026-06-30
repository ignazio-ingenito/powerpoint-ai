# Kiron CDG Analysis

## Scopo

Sintetizzare i materiali trovati in `source-materials/cdg-kiron/` e aggiornare il grounding del caso Kiron CDG per la presentazione `Data Pipeline Blueprint`.

## Fonti

- `2025_KIR_004 - Analisi funzionale.docx`
- `Campi Input.xlsx`
- `Campi Output.xlsx`
- `Campi Tabelle e Regole.xlsx`
- `Kiron CDG - Import struttura Jira_esempio.xlsx`
- `Kiron CDG - Piano di lavoro.xlsx`

## Sintesi Funzionale

Kiron CDG e' un caso documentato di Controllo di Gestione orientato a Direzione, Actual e Forecast.

La soluzione descritta mira a produrre:

- ricavi e costi Actual con periodicita' mensile;
- valori Forecast periodici a partire dagli actual;
- base dati strutturata per strumenti di BI direzionale.

Dimensioni principali:

- Periodo;
- Prodotto;
- Rete;
- Istituto.

Fonti principali:

- Campus;
- Campus 2.0;
- Zucchetti Infinity.

## Componenti Di Pipeline

### Ingestion / Estrazioni

- Campus alimenta dati gestionali come Erogato, PayIn, Payout, Coordinamento rete e Payout progetto giovani.
- Campus 2.0 alimenta dati di incentivazione e anagrafiche/prodotti.
- Zucchetti Infinity alimenta dati contabili, costi di struttura, altri ricavi e voci da riconciliare.

### Normalizzazione E Tabelle Guida

Il modello usa tabelle guida e dizionari:

- TG1 anagrafica prodotti;
- TG2 anagrafica istituti;
- TG3 anagrafica reti/agenti;
- TG4 mappatura bilancio;
- TG5 voci con standard;
- TG6 dati propedeutici forecast.

### Regole

Il materiale distingue:

- regole di ribaltamento `RIB`;
- regole di proiezione Forecast `STEP`;
- standard e parametri modificabili dalla Direzione.

### Output

Output documentati:

- `O1.1` DB Actual gestionale;
- `O1.2` DB Actual;
- `O2` DB Forecast.

Il forecast produce viste temporali mensili, trimestrali e annuali che integrano dati actual consolidati e valori previsionali.

## Implicazioni Per La Blueprint

Kiron rafforza il pattern CDG-like:

```text
Sorgenti gestionali/contabili
  -> ingestion periodica
  -> riconciliazione e normalizzazione
  -> tabelle guida e regole
  -> ribaltamenti / standard / conguagli
  -> Actual
  -> Forecast
  -> base dati BI-ready
```

Per la presentazione, Kiron puo' essere usato come caso documentato, non piu' solo come beneficiario target.

## Piano E WBS

I due documenti aggiunti rafforzano anche la parte piano:

- `Kiron CDG - Import struttura Jira_esempio.xlsx` contiene una struttura importabile in Jira con epic `Kiron CDG`, processi, story e task.
- `Kiron CDG - Piano di lavoro.xlsx` contiene un piano con fasi AFU, VAL, ATE, ESE, TEST, RIL e UAT.

Processi/aree emerse:

- Project Management e coordinamento;
- Actual;
- Forecast;
- Web App;
- Data import;
- Configurator;
- Data management;
- Data output;
- DevOps;
- UAT.

Attivita' rilevanti per la blueprint:

- connettori automatici per acquisizione dati da Campus;
- connettori automatici per acquisizione dati da Zucchetti Infinity;
- sezione per impostare regole di normalizzazione e standard/proxy mensili;
- motore di calcolo per normalizzazione, standard e ribaltamenti;
- interfacce di monitoraggio esecuzione processi e risultati elaborati;
- DB di frontiera per integrazione/pubblicazione verso Oracle BI;
- estensione Forecast con regole/parametri, motore di calcolo e output dedicati.

Nota: il piano contiene effort in giorni, ma non vanno usati nel deck come stime o commitment senza validazione commerciale e progettuale.

## Gap Residui

- Alcune regole e modalita' operative sono marcate nel documento come da definire o da rivedere con Kiron.
- Va chiarito quanto della soluzione prevista su OutSystems vada trattato come vincolo applicativo e quanto come pattern funzionale trasferibile nella blueprint.
- Va verificato se BI Oracle resta vincolo cliente o semplice riferimento della soluzione descritta.
- Va validato se il piano di lavoro e la struttura Jira sono ancora correnti prima di usarli per economics o planning formale.

## grill-with-docs

- La sintesi usa solo materiali presenti in `source-materials/cdg-kiron/`.
- Kiron viene promosso a caso documentato, ma non vengono inventati dettagli oltre analisi funzionale e workbook.
- Gli open point del materiale sorgente restano espliciti.

## Review

- Fonti, componenti, output, piano e gap sono separati.
- Non sono stati introdotti prezzi, effort, date o claim tecnologici non supportati.
- Il contenuto e' coerente con il deck neutrale: Kiron serve a discutere la blueprint, non a chiudere una scelta.

## Humanize

Kiron e' utile perche' assomiglia al CDG interno nella logica di controllo economico, ma porta un contesto cliente esterno, fonti diverse e una forte enfasi su regole configurabili, Actual e Forecast. Questo lo rende un buon caso per verificare quanto la blueprint sia davvero riusabile.
