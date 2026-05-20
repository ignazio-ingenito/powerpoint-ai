# AGENTS.md

## Scopo

Questo repository serve a creare presentazioni commerciali e PMO, preferibilmente in formato PowerPoint.

Codex deve usare il repository come ambiente di produzione per deck:

- `docs/` definisce metodo, storyline e regole contenutistiche.
- `docs/ui/` fornisce riferimenti visivi e di layout.
- la root del progetto è la destinazione dei deliverable finali.

## Agent OS / Codex OS

Questo repository adotta Agent OS / COS a livello **A3 Workflow-aware** per la produzione di deck.

Prima di lavori non banali, Codex deve leggere:

- `.codex/adoption.md`
- `.codex/routing.md`
- `.codex/authority.md`
- `.codex/execution.md`
- `.codex/knowledge-map.md`
- `.codex/deck-pipeline.md`
- `CONTEXT.md`

Usare questi file per scegliere route, autorità delle fonti, policy di esecuzione, quality gate e handoff.

Le skill locali in `.codex/skills/` definiscono la pipeline operativa per proposte commerciali e business case:

- `.codex/skills/proposal-intake/SKILL.md`
- `.codex/skills/repo-to-deck-brief/SKILL.md`
- `.codex/skills/business-case-storyline/SKILL.md`
- `.codex/skills/software-delivery-estimation/SKILL.md`
- `.codex/skills/executive-slide-writing/SKILL.md`
- `.codex/skills/deck-visual-grounding/SKILL.md`
- `.codex/skills/pptx-template-extraction/SKILL.md`
- `.codex/skills/powerpoint-manipulation/SKILL.md`
- `.codex/skills/pptx-package-validation/SKILL.md`
- `.codex/skills/commercial-deck-quality-review/SKILL.md`

Per proposte/business case di sviluppo software, usare una pipeline quality-first:

1. intake e inventario materiali;
2. grounding e gap assessment;
3. storyline sulle cinque sezioni cardine;
4. grounding visuale su `docs/template.pptx`, `docs/ui/` e deck sorgente;
5. manipolazione/produzione PowerPoint editabile;
6. review qualità;
7. handoff con assunzioni, verifiche e rischi residui.

Se mancano informazioni critiche su valore, perimetro, economics, impegni, date o contenuti cliente, fermarsi e chiedere chiarimenti. Se mancano dettagli minori, procedere solo marcandoli come assunzioni o punti da validare.

Quando Codex procede usando assunzioni, deve renderlo noto esplicitamente anche nella conversazione, non solo nel documento generato. Il messaggio deve indicare:

- quali assunzioni sono state usate per proseguire;
- perche' non sono state considerate bloccanti;
- quali domande restano da porre prima del passaggio successivo.

Non inserire in un deliverable domande formulate come "approval questions" se non sono state effettivamente poste all'utente. Usare invece una sezione esplicita come "Domande da porre prima del prossimo step" o "Assunzioni usate per procedere".

## Lettura Obbligatoria

Prima di creare o modificare una presentazione, leggere i file rilevanti in `docs/`.

Partire sempre da:

- tutti i file `docs/reference*.md`

Rileggere sempre il contenuto aggiornato delle cartelle di riferimento prima di lavorare. Non basarsi su letture precedenti, memoria della sessione o assunzioni su versioni passate, perché `docs/` e `docs/ui/` possono essere aggiornate nel tempo.

Considerare `docs/` come fonte primaria per struttura, metodo e contenuti della presentazione. Non inventare fatti, impegni, costi, date, perimetro progettuale, tecnologie, claim commerciali, esempi, dettagli cliente o dettagli implementativi che non siano presenti nei materiali sorgente o chiaramente forniti dall'utente.

Se un contenuto manca, è ambiguo o non è sufficientemente specificato, chiedere all'utente prima di colmare il vuoto. Fare assunzioni o creare contenuti placeholder solo quando l'utente lo chiede esplicitamente. Quando le assunzioni sono richieste, dichiararle in modo esplicito e facilmente verificabile nel documento e nel messaggio di handoff.

## Storyline Standard

Ogni proposta o business case dovrebbe includere queste cinque sezioni cardine, salvo diversa richiesta esplicita dell'utente:

1. Contesto ed esigenza/obiettivi
2. AS IS
3. TO BE
4. Piano di lavoro
5. Economics

Usare i file `docs/reference*.md` come interpretazione di base di queste sezioni.

La storyline può essere adattata in base a dimensione e complessità del progetto, ma le cinque sezioni cardine non devono sparire senza un motivo chiaro.

## Riferimenti Visivi

Usare `docs/ui/` solo come area di riferimento visivo e di layout.

Prima di creare o modificare un deck, rileggere sempre il contenuto aggiornato di `docs/ui/` e verificare quali file di riferimento sono disponibili.

I file in `docs/ui/` possono includere PDF, immagini esportate da slide, screenshot o altri esempi che mostrano lo stile desiderato della presentazione. Usarli per dedurre:

- formato e proporzioni delle slide
- posizionamento dei titoli
- stile delle slide divisorie
- scala tipografica
- palette colori
- spaziature e griglia
- convenzioni di header e footer
- densità del testo
- trattamento di diagrammi, architetture, processi, tabelle, roadmap ed economics

Non scrivere deliverable generati dentro `docs/ui/`.

Quando si usano deck di riferimento, seguire il loro linguaggio visivo e il sistema di layout. Non copiare contenuti riservati o specifici di un cliente, salvo richiesta esplicita dell'utente.

## Regole di Output

Salvare i deliverable finali nella root del progetto.

Output finali preferiti:

- `.pptx` come deliverable primario e modificabile
- `.pdf` come export per revisione o distribuzione, quando richiesto

Export opzionali, solo quando richiesti esplicitamente:

- immagini pagina per pagina, ad esempio `.png`
- asset di anteprima
- screenshot intermedi

Usare nomi file chiari e descrittivi, ad esempio:

- `2026_CLIENTE_001 - Cliente - Titolo proposta.pptx`
- `2026_CLIENTE_001 - Cliente - Titolo proposta.pdf`

Non posizionare output finali generati dentro `docs/` o `docs/ui/`.

## Generazione PowerPoint

Preferire la creazione di file PowerPoint modificabili rispetto a output solo statici.

Quando si implementa una pipeline di generazione, aggiungere una dipendenza solo se serve davvero al task. Se serve generare `.pptx` via script, preferire `pptxgenjs` salvo che il progetto usi già in modo consolidato un altro strumento. Tenere script e logica riutilizzabile fuori da `docs/` e `docs/ui/`, ad esempio sotto `scripts/`.

I deck generati dovrebbero rimanere modificabili in PowerPoint quando possibile:

- usare vere caselle di testo invece di immagini con testo rasterizzato
- usare forme PowerPoint per diagrammi semplici e callout
- usare tabelle quando ci si aspetta che siano modificabili
- usare immagini solo per asset che devono rimanere visuali

## Stile dei Contenuti

Scrivere con tono commerciale, chiaro, sintetico e adatto a interlocutori C-level.

Il linguaggio deve essere comprensibile a lettori executive che devono cogliere rapidamente valore di business, impatto operativo, rischi, tempi ed economics. Evitare gergo tecnico non necessario; quando i dettagli tecnici servono, spiegarne la rilevanza business.

Preferire titoli slide che comunichino il messaggio della slide, non etichette generiche. Ad esempio, preferire un titolo che esprima l'implicazione business rispetto a un titolo che dica solo "TO BE" o "Architecture".

Mantenere il testo delle slide breve e leggibile. Evitare di trasformare le slide in documenti densi.

Quando utile, separare:

- contenuti di sintesi executive
- contenuti di dettaglio delivery o implementativi
- assunzioni e punti aperti
- economics e note commerciali

## Checklist Qualità

Prima di considerare una presentazione completa, verificare che:

- le cinque sezioni cardine siano presenti o adattate intenzionalmente
- il deck usi `docs/` come fonte contenutistica e metodologica
- il deck usi `docs/ui/` solo come riferimento layout
- i deliverable finali siano salvati nella root del progetto
- le assunzioni siano esplicite
- i titoli slide comunichino il messaggio
- il testo non sia sovraccarico
- diagrammi, tabelle e roadmap siano leggibili
- contenuti riservati provenienti da deck di riferimento non siano stati copiati accidentalmente

## Strumenti e Skill Utili

Usare GitNexus solo se il repository cresce con script, generatori riutilizzabili, template o altro codice di cui è necessario capire relazioni e impatto.

Comandi GitNexus tipici:

```bash
npx gitnexus analyze
npx gitnexus --help
```

Usare Playwright solo quando servono anteprime browser-based o controlli visuali.

Usare image generation solo per asset bitmap come illustrazioni, texture, sfondi o mockup visuali. Non usare immagini generate come sostituto della struttura modificabile in PowerPoint.

Se è disponibile un plugin di verifica o grounding documentale come `grill-with-docs`, usarlo per controllare che il contenuto del deck generato resti fedele a `docs/` e ai materiali sorgente forniti dall'utente.

## Regole di Fedeltà Visuale

Quando si modifica un deck esistente, preferire interventi conservativi:
- riusare master, layout, font, palette, header/footer e loghi del file originale;
- non inventare loghi, immagini, icone o elementi decorativi;
- non deformare o ricreare loghi;
- non cambiare famiglia font se non richiesto;
- non ricostruire da zero slide che possono essere adattate;
- creare nuove slide copiando layout esistenti simili e modificando solo contenuto necessario.

## GitNexus

Non usare GitNexus per questo repository nelle attività ordinarie di produzione, revisione o configurazione dei deck.

Questo repository contiene materiali PowerPoint, documenti di riferimento e immagini UI, non una codebase applicativa.
La review delle presentazioni deve basarsi su:
- `docs/`
- `docs/ui/`
- contenuto estratto dal `.pptx`
- eventuali plugin di grounding documentale come `grill-with-docs`

Usare GitNexus solo se in futuro vengono introdotti script, generatori o codice riutilizzabile da analizzare.
