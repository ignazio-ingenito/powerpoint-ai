# Explained v0.7 - Review

## Output

- PDF: `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Explained v0.7.pdf`
- Sorgente HTML: `2026-06-30-data-pipeline/generated-assets/data-pipeline-explained-v0.7.html`

## Correzione Richiesta

La v0.6 era graficamente piu' vicina al template, ma risultava ancora troppo povera:

- poco testo esplicativo;
- poche infografiche che spiegassero davvero la pipeline;
- alcune slide dicevano il messaggio, ma non mostravano abbastanza il funzionamento.

## Modifiche Applicate

- Slide `TO BE | Componenti`: sostituito il flusso minimale con una infografica a livelli:
  - Source;
  - Contract;
  - Prepare;
  - Model;
  - Control.
- Slide `TO BE | Due scenari`: trasformata in una mappa a tre colonne:
  - parti comuni;
  - Scenario A AWS;
  - Scenario B Qlik.
- Slide `Scenario A`: architettura resa come schema a zone con governance trasversale.
- Slide `Scenario B`: architettura resa come schema a zone con tenant/capacity/entitlement evidenziati.
- Slide `Piano di lavoro`: aggiunti output attesi per ogni fase, legando il piano alla WBS.

## Critic

- La v0.7 e' molto piu' esplicativa della v0.6, ma resta un PDF: non e' ancora un `.pptx` editabile.
- Alcune slide sono piu' dense: la scelta e' intenzionale per rispondere alla necessita' di spiegare, ma in fase PowerPoint finale si potranno usare note relatore o appendice se serve alleggerire.
- Le infografiche sono coerenti con il template, ma non sono ancora oggetti PowerPoint nativi.

## Review Regole Gianfranco

- `Contesto / Esigenza / Obiettivi`: presente, piu' sostanzioso e leggibile.
- `AS IS`: saltato come sezione autonoma per richiesta esplicita dell'utente.
- `TO BE`: rafforzato con componenti logiche, parti comuni, scenari e architetture.
- `WBS`: mantiene processi e funzioni, con vista CDG e ProSIGNAL.
- `Piano di lavoro`: ora collega fasi, WBS e output attesi.
- `Costi`: mantiene driver e range, senza inventare quotazioni.

## Humanize

Il testo e' stato ampliato senza cambiare tono: resta diretto, manageriale e leggibile. Le parti tecniche spiegano perche' una scelta impatta controllo, riuso, costi, governance e blocker, non solo quale tool viene usato.

## Validazione

- PDF esportato con Chromium headless.
- 16 pagine 16:9.
- Testo totale estratto: circa 1.563 parole.
- Anteprime generate con `pdftoppm`.
- Controllo visuale su componenti, due scenari, architetture Scenario A/B, piano e contact sheet completo.

## Rischi Residui

- Per consegna finale servira' una versione PowerPoint editabile.
- Il prossimo miglioramento dovrebbe concentrarsi su una maggiore ricchezza iconografica delle architetture, copiando direttamente shape e stile da `docs/template.pptx`.
