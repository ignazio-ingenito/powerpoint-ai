# Explained v0.8 - Slide 2 Context Review

## Output

- Source HTML: `generated-assets/data-pipeline-explained-v0.8.html`
- PDF export: `2026_TXT_001 - Data Pipeline Blueprint - Explained v0.8.pdf`

## Modifica

La slide 2 e' stata arricchita su `Contesto` ed `Esigenza`, mantenendo lo stesso layout visuale della v0.7.

Il testo ora chiarisce che il tema non e' solo creare dashboard, ma governare dati, regole, anomalie e output affidabili su ProSIGNAL, Kiron CDG e CDG interno. L'esigenza e' formulata come necessita' di una blueprint condivisa per evitare di ricostruire ogni volta tracciati, mapping, controlli, log e gestione degli scarti.

## Grounding

Riletti e usati come riferimento:

- `drafts/03-use-case-synthesis.md`
- `drafts/04-internal-cdg-analysis.md`
- `drafts/07-to-be-scenario-storyline.md`
- `drafts/09-wbs-and-workplan.md`
- `drafts/10-architecture-brief.md`
- `drafts/13-kiron-cdg-analysis.md`

Punti incorporati:

- i tre casi condividono esigenze ricorrenti su fonti, mapping, controlli, output, audit e riuso;
- ProSIGNAL e Kiron restano prioritari come casi esterni;
- Kiron e CDG interno sono CDG-like, ma con contesti e fonti differenti;
- ProSIGNAL resta il caso piu' utile per stressare file, tracciati, controlli e output regolamentari;
- la presentazione resta neutrale tra Dagster/dbt/Metabase su AWS e Talend/Qlik.

## Humanize

Il testo e' stato semplificato per un pubblico C-level:

- meno gergo tecnico;
- frasi piu' dirette;
- collegamento esplicito tra dato, fiducia, governance, riuso e costi;
- nessun claim nuovo non supportato dai materiali.

## Verifica

- PDF esportato con Chromium headless.
- `pdfinfo` conferma 16 pagine.
- Preview visiva della pagina 2 generata da PDF e controllata: testo leggibile, nessuna sovrapposizione, layout coerente con v0.7.

## Rischi residui

- Il contenuto resta volutamente a livello executive: eventuali dettagli piu' specifici su ProSIGNAL richiedono esempi reali di tracciati/file/output.
- La slide non introduce una scelta tra i due scenari; la decisione resta oggetto della discussione del comitato.
