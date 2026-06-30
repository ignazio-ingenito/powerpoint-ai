# Visual Draft v0.4 - Review

## Output

- PDF visuale: `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Visual Draft v0.4.pdf`
- Sorgente ricostruibile: `2026-06-30-data-pipeline/generated-assets/data-pipeline-visual-draft-v0.4.html`

Questa versione nasce per rispondere al gap della v0.3: la bozza PowerPoint editabile era utile come wireframe, ma non abbastanza aderente ai layout visuali forniti.

## Grounding Visuale

Pattern usati da `docs/ui/`:

- cover ariosa con accento laterale, ispirata a `bernadelli-01`;
- slide `Contesto / Esigenza / Obiettivi` con colonna visuale e tre blocchi numerati, ispirata a `bernadelli-02`;
- slide scenario con schema a sinistra e sintesi a destra, ispirate a `bernadelli-06` e `bernadelli-07`;
- confronto scenari con tabella a due colonne, ispirato a `bernadelli-08`;
- economics con card e box di sintesi, ispirata a `bernadelli-10`;
- chiusura istituzionale coerente con `bernadelli-11`.

## Critic

- La versione v0.4 e' piu' fedele alle reference, ma non e' un PowerPoint editabile: e' un PDF visuale prodotto da sorgente HTML.
- Il logo e' ricostruito in modo semplificato per evitare distorsioni; per una versione finale PowerPoint conviene sostituirlo con asset ufficiale.
- Alcune slide architetturali restano volutamente sintetiche: il dettaglio completo rimane nei draft e puo' diventare appendice se serve.
- La slide economics resta a livello di driver/range: il range 50 GB / 30-50k EUR e' baseline fornita dall'utente, non quotazione ufficiale.

## Review Regole Gianfranco

- `Contesto / Esigenza / Obiettivi`: presente e reso esplicito in slide 2.
- `AS IS`: non presente come sezione autonoma per richiesta esplicita dell'utente; l'adattamento e' documentato.
- `TO BE`: coperto da componenti logiche, introduzione ai due scenari e slide dedicate a Scenario A/B.
- `Piano di lavoro`: presente in slide 12, a livello manageriale, senza date o effort inventati.
- `Economics`: presente in slide 13 come driver e range di discussione, coerente con una blueprint.
- WBS/processi/funzioni: presente in slide 11, sintetica e coerente con i tre casi target.

## Review Contenuti

- Il deck resta neutrale tra le due opzioni.
- I testi sono stati ridotti e riscritti in linguaggio C-level.
- Le parti tecniche sono legate a impatti di riuso, controllo, costi, scalabilita' e blocker.
- Non sono stati introdotti nuovi fatti, prezzi, date, commitment o dettagli cliente.
- I punti non confermati restano dichiarati: entitlement Talend/Qlik, limiti capacity, DB cliente/RDS, economics completi.

## Humanize

La nuova bozza non chiede al comitato di leggere una specifica tecnica. Porta la discussione su tre domande semplici:

1. quale modello operativo vogliamo riusare;
2. quale scenario accelera ProSIGNAL e Kiron senza chiudere opzioni future;
3. quali verifiche servono prima di trasformare la blueprint in piano esecutivo.

## Validazione

- PDF esportato con Chromium headless.
- 15 pagine 16:9.
- Anteprime generate con `pdftoppm`.
- Controllo visuale manuale su cover, contesto, scenari, confronto, proiezione casi ed economics.

## Rischi Residui

- Per consegna formale serve una passata finale su logo/font aziendali ufficiali.
- Se il deliverable deve tornare editabile, conviene ricostruire il PDF in PowerPoint seguendo questa v0.4 come riferimento visuale.
- Prima di una versione cliente vanno confermati licensing/capacity Qlik/Talend e range economici completi.
