# First Deck Build Review

## Output

- PPTX corrente: `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Scenari TO BE v0.3.pptx`
- PDF di controllo: `2026-06-30-data-pipeline/attempts/2026_TXT_001 - Data Pipeline Blueprint - Scenari TO BE v0.3.pdf`
- Script ricostruibile: `2026-06-30-data-pipeline/generated-assets/build_data_pipeline_deck.py`
- Asset template usato: `2026-06-30-data-pipeline/generated-assets/txt-novigo-logo-from-template.png`

## Strategia

Prima bozza PowerPoint editabile, generata con `python-pptx` e forme native:

- testi come caselle PowerPoint;
- diagrammi come forme e connettori;
- tabelle/matrici come shape editabili;
- nessun testo rasterizzato;
- palette e pattern ispirati a `docs/template.pdf` e `docs/ui/`.

Le versioni precedenti sono state conservate in `attempts/` come prove tecniche.

## Critic

- Il deck e' una prima bozza: copre la discussione strategica ma non ancora tutto il dettaglio operativo dei tre casi.
- La fedelta' al template e' buona come linguaggio generale, ma non e' una ricostruzione stretta dei master PowerPoint originali: e' stata scelta una base pulita per evitare elementi master indesiderati.
- Le slide mapping/comparison sono leggibili ma ancora dense: possono essere alleggerite quando si sceglie cosa lasciare nel deck executive e cosa spostare in appendix.
- Economics: il range Qlik/Talend 50 GB 30-50k EUR e' presente come ipotesi utente, non come prezzo ufficiale o quotazione.

## Review

- `Contesto / Esigenza / Obiettivi` e' esplicito.
- L'AS IS autonomo e' saltato come richiesto dall'utente; il deck parte dal TO BE comparativo.
- I due scenari sono entrambi rappresentati con componenti, mapping, architettura logica, benefici/limiti e criteri comparativi.
- ProSIGNAL e Kiron hanno priorita' rispetto al CDG interno.
- Kiron e ProSIGNAL mantengono i gap dichiarati: non sono stati inventati tracciati, output o regole non disponibili.
- La WBS e il piano sono sintetici e orientati al deck; il dettaglio resta nei draft.
- Le assunzioni commerciali e tecniche restano visibili.

## Humanize

La bozza deve funzionare come supporto alla discussione, non come documento tecnico completo. I testi sono stati tenuti brevi, con titoli che esprimono il messaggio della slide e non solo l'etichetta della sezione.

## Validazione

- `unzip -t` sul PPTX v0.3: OK.
- Parse XML su tutti i `.xml` e `.rels`: OK.
- Content types: nessun override mancante.
- Relazioni interne: nessun target mancante.
- Negative extents: non rilevate.
- Export PDF con LibreOffice: OK.
- Anteprima visiva PDF: controllate cover, contesto, scenario AWS, economics e contact sheet complessiva.

## Rischi Residui

- Verifica manuale in PowerPoint ancora consigliata per confermare apertura senza repair e resa identica a LibreOffice.
- La versione e' adatta a iniziare revisione contenuti/layout, non ancora a distribuzione formale.
- Prima di una versione finale servono conferme su entitlement Qlik/Talend, economics, periodo/IVA/bundle e limiti tecnici sui casi piu' esigenti.
