# Handoff - Image-Based Final PDF

## Obiettivo

Produrre una versione finale in PDF della presentazione `Data Pipeline Blueprint`, partendo dalle slide PDF già generate e da eventuali PDF aggiuntivi messi dall'utente in una cartella di input.

Il risultato deve essere un PDF costruito da immagini slide-by-slide. La priorità è migliorare resa grafica, chiarezza executive e fedeltà al look Novigo, anche se l'output non sarà PowerPoint editabile.

## Prima domanda da fare

Prima di iniziare chiedere all'utente:

```text
Quale cartella devo usare come input per i PDF delle slide da rielaborare?
```

Accettare un path assoluto o relativo al repository. Se la cartella non esiste, è vuota o non contiene PDF leggibili, fermarsi e chiedere all'utente di fornire il materiale. Non ricostruire contenuti mancanti per inferenza.

## Input principali

Usare come fonte primaria la versione più recente disponibile:

- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Explained v0.8.pdf`

Usare le altre versioni solo per arricchire contesto, recuperare scelte grafiche o capire evoluzioni precedenti:

- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Explained v0.7.pdf`
- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Template Faithful v0.6.pdf`
- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Template Faithful v0.5.pdf`
- `2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Visual Draft v0.4.pdf`
- `2026-06-30-data-pipeline/attempts/2026_TXT_001 - Data Pipeline Blueprint - Scenari TO BE v0.3.pdf`

Se nella cartella input sono presenti PDF più recenti, usarli come fonte primaria e trattare la v0.8 come contesto.

## Reference visuali obbligatorie

Usare come riferimento visuale primario:

- `docs/template.pdf`
- `docs/template2.pdf`

`docs/template.pdf` contiene 16 pagine 16:9. `docs/template2.pdf` contiene 10 pagine 16:9 ed è stato indicato come riferimento aggiuntivo. Se `docs/template2.pdf` non è tracciato o non è disponibile nella sessione di lavoro, segnalarlo e chiedere all'utente di ripristinarlo prima di finalizzare.

Non copiare contenuti riservati dai template. Usarli solo per ricavare layout, proporzioni, ritmo grafico, densità, header/footer, palette, trattamento dei diagrammi e stile delle slide.

## Vincoli visuali

Mantenere lo stile grafico originale Novigo:

- branding invariato;
- logo e marchi non deformati, non ridisegnati, non sostituiti;
- gradiente azzurro, turchese e verde coerente con i template;
- font sans-serif moderno, pulito e leggibile;
- look minimal corporate;
- stile consulenziale, vicino a presentazioni McKinsey, Bain o Deloitte;
- bordi arrotondati sottili;
- icone outline, preferibilmente vettoriali;
- schemi, mappe, matrici e infografiche al posto di lunghi blocchi testuali;
- densità da executive deck: contenuto sufficiente a spiegare, ma senza effetto documento.

Evitare:

- palette nuove;
- gradienti diversi da quelli Novigo;
- elementi decorativi generici;
- icone piene o troppo illustrative;
- slide piene di testo;
- linguaggio tecnico non necessario;
- claim non supportati dai materiali;
- loghi, immagini o riferimenti inventati.

## Regole di contenuto

La presentazione deve restare neutrale tra i due scenari:

- Dagster / dbt / Metabase su AWS;
- Talend / Qlik.

Il messaggio deve rimanere orientato a CEO, Gianfranco, CTO e Tech Committee. Non deve sembrare una specifica tecnica. Deve aiutare il comitato a discutere:

- perché serve una blueprint;
- quali componenti deve avere una buona pipeline;
- cosa resta comune tra i due scenari;
- cosa cambia davvero tra scenario AWS e scenario Qlik/Talend;
- benefici, limiti, costi, blocker e riuso;
- applicazione a ProSIGNAL, Kiron CDG e CDG interno;
- WBS per processi e funzioni;
- piano comune derivato dalla WBS.

Se un'informazione non è presente nei materiali sorgente o nelle richieste utente, non inventarla. Se serve per chiudere una slide, marcarla come assunzione oppure chiedere chiarimento.

## Humanize obbligatorio

Ogni testo visibile deve passare da una revisione `humanize`:

- frasi naturali, non meccaniche;
- grammatica e punteggiatura corrette;
- lessico comprensibile da un pubblico C-level;
- niente gergo tecnico se non serve alla decisione;
- evitare formule ripetitive, tono promozionale e frasi gonfiate;
- preferire frasi brevi, concrete e verificabili;
- mantenere i nomi tecnici quando sono oggetto del confronto, ma spiegare l'impatto business.

Esempio di tono:

```text
La scelta non riguarda solo gli strumenti. Definisce come vogliamo governare dati, controlli, costi e riuso sui prossimi progetti.
```

## Workflow operativo

1. Controllare `git status --short --branch --untracked-files=all` e non toccare file non correlati.
2. Chiedere all'utente la cartella input dei PDF.
3. Inventariare i PDF disponibili nella cartella input e nel progetto.
4. Stabilire la fonte primaria: ultimo PDF disponibile, con priorità alla v0.8 se non ci sono versioni successive.
5. Estrarre le pagine dei PDF sorgente come immagini in una cartella di lavoro sotto:

   ```text
   2026-06-30-data-pipeline/generated-assets/final-image-pdf/
   ```

6. Estrarre o rileggere il testo dei PDF e dei draft principali per evitare perdita di contenuto:

   - `drafts/03-use-case-synthesis.md`
   - `drafts/04-internal-cdg-analysis.md`
   - `drafts/07-to-be-scenario-storyline.md`
   - `drafts/09-wbs-and-workplan.md`
   - `drafts/10-architecture-brief.md`
   - `drafts/13-kiron-cdg-analysis.md`
   - `drafts/19-explained-v0.8-context-review.md`

7. Creare uno storyboard slide-by-slide con:

   - messaggio della slide;
   - contenuto obbligatorio;
   - visual principale;
   - testo humanized;
   - riferimento template più vicino;
   - note su assunzioni o fonti mancanti.

8. Generare le slide come immagini ad alta risoluzione, mantenendo anche i sorgenti ricostruibili:

   - sorgenti HTML/SVG/asset in `generated-assets/final-image-pdf/sources/`;
   - immagini slide finali in `generated-assets/final-image-pdf/slides/`;
   - eventuali icone vettoriali in `generated-assets/final-image-pdf/icons/`;
   - manifest fonti e asset in `generated-assets/final-image-pdf/manifest.md`.

9. Comporre il PDF finale dalle immagini slide-by-slide.
10. Generare una contact sheet o preview delle pagine finali.
11. Eseguire i gate finali: Critic, Review, Humanize.
12. Salvare un report di review in `drafts/`.

## Output attesi

Output finale:

```text
2026-06-30-data-pipeline/2026_TXT_001 - Data Pipeline Blueprint - Image Final v1.0.pdf
```

Asset ricostruibili:

```text
2026-06-30-data-pipeline/generated-assets/final-image-pdf/
```

Review:

```text
2026-06-30-data-pipeline/drafts/21-image-final-v1-review.md
```

Se vengono prodotti tentativi intermedi, salvarli in:

```text
2026-06-30-data-pipeline/attempts/
```

## Quality gate

Prima della consegna verificare:

- il PDF si apre correttamente;
- dimensione 16:9 coerente con i template;
- tutte le slide hanno branding, header/footer e stile Novigo coerenti;
- nessun logo è stato modificato o deformato;
- colori e gradiente restano azzurro, turchese e verde;
- font e scala tipografica sono coerenti;
- testi leggibili anche su schermo non grande;
- nessun testo si sovrappone a icone, diagrammi o footer;
- le slide complesse usano schemi o infografiche, non paragrafi lunghi;
- il linguaggio è C-level e non tecnico;
- WBS, architetture, scenari, benefici/limiti, proiezione sui casi, piano ed economics restano presenti;
- le assunzioni sono esplicite;
- eventuali documenti mancanti sono segnalati, non sostituiti con contenuti inventati.

## Critic

Domande da farsi prima di chiudere:

- La slide spiega davvero il concetto o lo sta solo nominando?
- Un CEO capisce perché questa decisione impatta costi, tempi, rischio e riuso?
- La grafica aiuta la comprensione o decora soltanto?
- Le WBS sono ancora abbastanza ricche per processi e funzioni?
- I due scenari sono trattati in modo neutrale?
- Abbiamo introdotto dettagli non supportati?

## Review

Il deck finale deve rispettare le regole del repository:

- cartella progetto dedicata;
- output finali nella cartella `2026-06-30-data-pipeline/`;
- asset generati salvati e ricostruibili;
- riferimento visuale a `docs/template.pdf` e `docs/template2.pdf`;
- niente contenuti inventati;
- passaggio finale Critic / Review / Humanize documentato.

## Nota finale

Questo handoff privilegia la qualità visuale del PDF finale. Se in seguito servirà una versione PowerPoint editabile, usare questo PDF come visual target e ricostruire le slide con shape, testi e icone native in PowerPoint.
