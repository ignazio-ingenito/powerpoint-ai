# Template Faithful v0.6 - Review

## Output

- PDF: `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Template Faithful v0.6.pdf`
- Sorgente HTML: `2026-06-30-data-pipeline/generated-assets/data-pipeline-template-faithful-v0.6.html`

## Correzione Richiesta

La v0.5 aveva due limiti:

- `Contesto / Esigenza / Obiettivi` era troppo scarno rispetto al ruolo della slide.
- La WBS era troppo compressa: mostrava macro-aree, ma non rispettava abbastanza la logica Gianfranco "processi al primo livello, funzioni per ogni processo".

## Modifiche Applicate

### Contesto / Esigenza / Obiettivi

- Il contesto ora spiega che ProSIGNAL, Kiron CDG e CDG interno cambiano per fonti/output, ma condividono la stessa esigenza di pipeline.
- L'esigenza chiarisce il rischio di ripartire da zero su tracciati, mapping, controlli, log e anomalie.
- Gli obiettivi sono formulati come discussione di comitato: confrontare scenari, capire parti comuni e decidere verifiche prima di adottare una strada.

### WBS

- La WBS non e' piu' una singola slide sintetica.
- Sono state create due slide:
  - `WBS | Processi e funzioni CDG`, basata sul modello Kiron e adattabile al CDG interno.
  - `WBS | Processi e funzioni ProSIGNAL`, basata su processi file/tracciati/controlli/output.
- Ogni slide mostra processi di primo livello e funzioni sotto ciascun processo.

## grill-with-docs

- Le regole di Gianfranco richiedono WBS nuova o sezione modificata con evidenza di processi e funzioni gestiti.
- La struttura Kiron nei materiali e in `09-wbs-and-workplan.md` conferma il pattern:
  - Project management e coordinamento;
  - Actual;
  - Forecast;
  - UAT e rilascio.
- Il CDG interno puo' riusare la stessa ossatura Kiron, con P1-P5 Actual e P6 Forecast come contenuti funzionali specifici.
- ProSIGNAL richiede una WBS distinta, perche' i processi principali sono ingestion file, tracciati, parsing, controlli funzionali e output regolamentari.

## Review

- La sezione `Contesto / Esigenza / Obiettivi` e' ora piu' completa senza diventare tecnica.
- La WBS rispetta meglio il criterio processi/funzioni.
- La storyline continua a saltare AS IS come sezione autonoma per richiesta esplicita dell'utente.
- TO BE, Piano di lavoro e Costi restano presenti.
- Non sono stati introdotti nuovi commitment, date, effort o prezzi.

## Humanize

Il testo resta semplice e leggibile. L'aumento di dettaglio e' stato concentrato dove serve al metodo di Gianfranco: nella WBS. Le slide di scenario rimangono sintetiche per non trasformare la presentazione in una specifica tecnica.

## Validazione

- PDF esportato con Chromium headless.
- 16 pagine 16:9.
- Testo totale estratto: circa 1.238 parole.
- Anteprime generate con `pdftoppm`.
- Controllo visuale su contesto, WBS CDG, WBS ProSIGNAL, piano di lavoro e contact sheet completo.

## Rischi Residui

- La WBS resta una vista manageriale, non un piano di dettaglio Jira.
- Per versione finale PowerPoint servira' ricostruire queste due slide in `.pptx` usando il template PowerPoint, non solo il PDF.
