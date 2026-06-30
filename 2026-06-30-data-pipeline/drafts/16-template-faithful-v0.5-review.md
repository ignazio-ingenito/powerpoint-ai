# Template Faithful v0.5 - Review

## Output

- PDF: `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Template Faithful v0.5.pdf`
- Sorgente HTML: `2026-06-30-data-pipeline/generated-assets/data-pipeline-template-faithful-v0.5.html`
- Asset template estratti:
  - `novigo-header-logo-template.png`
  - `template-cover-wave.png`
  - `txt-star-mark-template.png`

## Obiettivo

Rispondere al gap visuale segnalato: la v0.4 era piu' ordinata della v0.3, ma ancora non abbastanza vicina a:

- `docs/2026_EDQ_003 - Edilquattro - Proposta nuova infrastruttura server.pdf`
- `docs/template.pdf`

## Cosa E' Stato Allineato

- Logo/header reale estratto dal template, non ricostruito manualmente.
- Grafica a linee della cover estratta dal template.
- Cover con grande spazio bianco, titolo basso a sinistra e wave laterale.
- Header interni con logo a sinistra, titolo grigio, numero pagina a destra e barre teal/azzurro.
- Slide `Contesto / Esigenza / Obiettivi` con colonna visuale a sinistra e tre blocchi numerati.
- Slide scenario con schema a sinistra e testo sintetico a destra.
- Tabella confronto in stile `Confronto soluzioni`.
- Slide costi con card e box di sintesi.
- Chiusura con visual wave e messaggio istituzionale.

## Critic

- Non e' ancora un clone PowerPoint pixel-perfect: e' un PDF generato da HTML.
- La fedelta' e' molto piu' alta, ma per uguaglianza piena servirebbe ricostruire direttamente nel `.pptx` copiando layout, master e shape dal template.
- Alcuni diagrammi sono semplificati rispetto al deck Edilquattro: mantengono il linguaggio visivo ma non la stessa ricchezza iconografica.
- Non sono stati copiati contenuti cliente da Edilquattro/Bernardelli.

## Review Regole Gianfranco

- `Contesto / Esigenza / Obiettivi`: presente e visibile in slide 2.
- `AS IS`: saltato come sezione autonoma per richiesta esplicita dell'utente.
- `TO BE`: coperto da capability map, due scenari e architetture.
- `Piano di lavoro`: presente a livello manageriale, senza date o effort inventati.
- `Economics / Costi`: presente come driver e range, non come offerta definitiva.
- WBS: sintetizzata per processi/funzioni e coerente con i tre casi target.

## Humanize

Il linguaggio resta intenzionalmente semplice: la presentazione deve aprire una discussione su due modelli operativi, non descrivere una specifica tecnica. I termini tecnici sono tenuti solo dove servono a distinguere responsabilita', costi, riuso e blocker.

## Validazione

- PDF esportato con Chromium headless.
- 15 pagine 16:9.
- Testo totale estratto: circa 1.043 parole.
- Anteprime generate con `pdftoppm`.
- Contact sheet verificato contro i pattern Edilquattro/template.

## Prossimo Passo Consigliato

Se questa direzione visuale e' approvata, il passo successivo e' ricostruire una versione `.pptx` usando questa v0.5 come riferimento e copiando i layout dal template PowerPoint, non ripartendo dal wireframe v0.3.
