# PowerPoint Deck Workflow

Questo repository serve a produrre presentazioni commerciali e business case, preferibilmente in formato PowerPoint editabile, seguendo una pipeline quality-first per progetti software.

## Quando Usare Questo Workflow

Usalo quando devi creare una presentazione a partire da:

- repository software;
- appunti o documenti testuali;
- immagini e reference visuali;
- transcript di riunioni;
- deck sorgenti o template PowerPoint.

Output tipico:

- dossier grounded in Markdown;
- storyline executive;
- visual plan;
- deck `.pptx` in root;
- eventuale export `.pdf` quando richiesto.

## Regole Base

- Non inventare fatti, costi, date, scope, commitment o benefici.
- Segna sempre cosa e' **fatto confermato**, **inferenza**, **stima**, **assunzione** o **domanda aperta**.
- Se procedi usando assunzioni, dichiarale anche nel messaggio all'utente: quali sono, perche' non bloccano lo step corrente e quando vanno validate.
- Non chiamare "approval questions" domande che non sono state ancora poste. Usa "domande aperte" o "domande da porre prima del prossimo step".
- Mantieni le cinque sezioni cardine:
  1. Contesto ed esigenza/obiettivi
  2. AS IS
  3. TO BE
  4. Piano di lavoro
  5. Economics
- Per deck CEO o portfolio, ogni iniziativa deve chiarire: valore, risultati visibili, sizing, prossimi passi, owner/funding e decisioni richieste.
- Usa `docs/ui/` e `docs/template.pptx` come riferimento visuale, non come fonte di contenuti cliente.

## Struttura Dei File

| Path | Uso |
|---|---|
| `AGENTS.md` | Regole operative principali per Codex |
| `.codex/deck-pipeline.md` | Pipeline end-to-end |
| `.codex/skills/` | Skill locali da usare nelle varie fasi |
| `CONTEXT.md` | Glossario del dominio deck |
| `docs/reference*.md` | Metodo commerciale e storyline standard |
| `docs/ui/` | Reference visive |
| `docs/template.pptx` | Template/base PowerPoint |
| `prompt.repo-analysis-for-deck.md` | Prompt riusabile per analizzare repository software |
| root | Destinazione deliverable finali e working draft |

## Workflow End-To-End

### 1. Intake

Obiettivo: capire input, audience, decisione da abilitare e gap critici.

Materiali da raccogliere:

- path del repo o cartella sorgente;
- nome progetto;
- cliente/sponsor;
- audience;
- tipo deck;
- obiettivo business;
- vincoli noti;
- immagini, documenti, transcript, appunti.

Prompt breve:

```text
Voglio creare una proposta/business case per <progetto>.
Materiali disponibili: <lista>.
Audience: <audience>.
Decisione che il deck deve abilitare: <decisione>.
Usa la pipeline del repo PowerPoint e fammi prima le domande bloccanti.
```

### 2. Repo Analysis / Grounded Brief

Obiettivo: trasformare un repository software in un dossier commerciale grounded.

Skill coinvolte:

- `repo-to-deck-brief`
- `software-delivery-estimation`

Prompt consigliato:

```text
Analizza il repository <path_repo> usando prompt.repo-analysis-for-deck.md.
Produci un dossier grounded per proposta commerciale/business case.
Includi contesto, AS IS, TO BE, piano, effort, benefici, economics driver, rischi e domande.
Non creare ancora il PowerPoint.
```

Output atteso:

```text
<Nome progetto> - Repo to Deck Brief.md
```

Controlli:

- tutte le fonti lette sono elencate;
- i PDF o dati sensibili non sono letti se non necessari;
- eventuali metriche sono aggregate e non esposte come claim non validati;
- stime e benefici sono marcati come tali.

### 3. Executive Storyline

Obiettivo: comprimere il dossier in una scaletta C-level.

Skill coinvolte:

- `business-case-storyline`
- `executive-slide-writing`

Prompt consigliato:

```text
Usa <Nome progetto> - Repo to Deck Brief.md per creare una executive storyline.
Mantieni le cinque sezioni cardine.
Usa titoli slide che comunichino il messaggio.
Applica il CEO-readiness check: risultati visibili, sizing, economics, owner, decisioni.
```

Output atteso:

```text
<Nome progetto> - Executive Storyline v1.md
```

Controlli:

- ogni slide ha un ruolo distinto;
- i tecnicismi sono tradotti in impatto business;
- economics e benefici non sono promesse non supportate;
- le domande non ancora poste sono marcate come open question prima del PPTX.

### 4. Visual Grounding

Obiettivo: scegliere layout e pattern prima di generare slide.

Skill coinvolte:

- `deck-visual-grounding`
- `pptx-template-extraction`

Comandi utili:

```bash
find docs/ui -maxdepth 1 -type f | sort
unzip -l docs/template.pptx | sed -n '1,80p'
```

Prompt consigliato:

```text
Crea il visual plan slide-by-slide per <Nome progetto>.
Usa docs/template.pptx e docs/ui/ come reference visuali.
Mantieni il deck editabile in PowerPoint.
Non generare ancora il PPTX.
```

Output atteso:

```text
<Nome progetto> - Visual Plan.md
```

Controlli:

- ogni slide ha layout, contenuto visuale e note di esecuzione;
- non vengono copiati contenuti cliente dalle reference;
- testo e diagrammi saranno PowerPoint-native.

### 5. PPTX Generation

Obiettivo: creare il deck editabile.

Skill coinvolte:

- `powerpoint-manipulation`
- `pptx-package-validation`

Prompt consigliato:

```text
Genera una prima versione PPTX editabile usando:
- <Nome progetto> - Repo to Deck Brief.md
- <Nome progetto> - Executive Storyline v1.md
- <Nome progetto> - Visual Plan.md

Usa docs/template.pptx e docs/ui/ come baseline visuale.
Salva il file in root.
Non sovrascrivere file esistenti.
```

Output atteso:

```text
YYYY_CLIENTE_001 - Cliente - Titolo proposta.pptx
```

### 6. Validation

Obiettivo: verificare qualità contenutistica, visuale e integrità del pacchetto.

Skill coinvolte:

- `commercial-deck-quality-review`
- `pptx-package-validation`

Comandi utili:

```bash
unzip -t "<deck>.pptx"
```

Checklist:

- le cinque sezioni cardine sono presenti;
- titoli slide sono messaggi, non label;
- assunzioni e open point sono espliciti;
- baseline e metriche non sono presentate come accuratezza validata se non lo sono;
- sizing/economics sono range o driver se non ci sono dati definitivi;
- slide non duplicate;
- elementi principali editabili;
- package PPTX integro.

### 7. Handoff

Obiettivo: chiudere la fase con file, verifiche e rischi residui chiari.

Il riepilogo finale deve includere:

- path output;
- principali decisioni contenutistiche;
- assunzioni rimaste;
- domande aperte;
- verifiche eseguite;
- rischi residui o controlli manuali PowerPoint.

## Prompt Completo Per Avviare Un Nuovo Deck Da Repository

```text
Voglio creare una presentazione business case/proposta commerciale a partire da questo repository:
<path_repo>

Obiettivo business:
<obiettivo>

Audience:
<audience>

Cliente/sponsor:
<cliente o sponsor, se noto>

Vincoli:
<vincoli privacy, economici, tecnici, commerciali>

Usa il workflow di questo repo PowerPoint:
1. leggi AGENTS.md, .codex/deck-pipeline.md, CONTEXT.md, docs/reference*.md;
2. usa prompt.repo-analysis-for-deck.md;
3. crea prima il Repo to Deck Brief;
4. poi crea Executive Storyline;
5. poi Visual Plan;
6. aspetta approvazione prima di generare il PPTX.

Non inventare dati, costi, date, benefici o commitment.
Se usi assunzioni per procedere, dichiarale nella risposta prima di generare l'artefatto.
Se mancano informazioni critiche, chiedi.
```

## Convenzione Nomi File

Working draft Markdown:

```text
<Nome progetto> - Repo to Deck Brief.md
<Nome progetto> - Executive Storyline v1.md
<Nome progetto> - Visual Plan.md
```

Deliverable finali:

```text
2026_CLIENTE_001 - Cliente - Titolo proposta.pptx
2026_CLIENTE_001 - Cliente - Titolo proposta.pdf
```

## Note Operative

- I file finali vanno in root.
- `docs/ui/` non deve contenere output generati.
- `docs/template.pptx` non va sovrascritto.
- Non installare dipendenze se non servono davvero.
- Se si aggiunge una pipeline generativa riusabile, tenere script e logica sotto `scripts/`.
