# Prompt - Analisi repository per proposta commerciale / business case

Usa questo prompt quando devi analizzare un repository software e ricavare le informazioni utili per creare una presentazione commerciale o un business case secondo la pipeline di questo repo PowerPoint.

## Obiettivo

Analizza il repository indicato e produci un pacchetto informativo grounded per costruire una presentazione aziendale executive-ready, con focus su:

- contesto e razionale del progetto;
- AS IS tecnico/operativo;
- TO BE proposto;
- piano di lavoro;
- economics, effort, benefici e assunzioni.

Il risultato non deve essere ancora un deck PowerPoint. Deve essere un dossier strutturato da usare come input per la pipeline deck.

## Repository da analizzare

- `<REPO_PATH_O_URL>`:
- `<NOME_PROGETTO>`:
- `<CLIENTE_O_SPONSOR>`:
- `<TIPO_DECK>`: proposta commerciale / business case / assessment / proposta evolutiva
- `<AUDIENCE>`: CEO/C-level / IT management / business owner / steering committee
- `<OBIETTIVO_BUSINESS>`:
- `<VINCOLI_NOTI>`:

## Fonti e regole da seguire

Prima di iniziare:

1. Leggi le istruzioni del repository analizzato, se presenti: `AGENTS.md`, `README*`, docs architetturali, ADR, specs, roadmap, issue template.
2. Nel repo PowerPoint, leggi:
   - `AGENTS.md`
   - `.codex/adoption.md`
   - `.codex/deck-pipeline.md`
   - `.codex/authority.md`
   - `CONTEXT.md`
   - tutti i file `docs/reference*.md`
   - `.codex/skills/repo-to-deck-brief/SKILL.md`
   - `.codex/skills/software-delivery-estimation/SKILL.md`
3. Non inventare fatti come se fossero confermati.
4. Puoi produrre stime, ipotesi di piano, benefici attesi e rischi, ma devi marcarli chiaramente come **stima**, **ipotesi** o **guess da validare**.
5. Se un’informazione è critica per scope, economics, tempi, impegni o benefici, e non è ricavabile dal repo, elencala come domanda aperta.

## Analisi richiesta

### 1. Executive Summary

Sintetizza in massimo 10 bullet:

- cosa fa il prodotto/sistema;
- per chi crea valore;
- quali problemi sembra risolvere;
- quale opportunità commerciale o progettuale emerge;
- quali elementi sono confermati dal repository;
- quali elementi sono dedotti.

### 2. Inventario delle fonti

Elenca le fonti lette:

| Fonte | Tipo | Cosa contiene | Autorità | Note |
|---|---|---|---|---|

Segnala file non letti o non ispezionabili.

### 3. Contesto ed esigenza / obiettivi

Ricostruisci:

- contesto di business o operativo;
- problema attuale;
- obiettivi espliciti;
- obiettivi impliciti ragionevoli;
- stakeholder probabili;
- vincoli o driver di urgenza.

Se non presenti nel repo, formula ipotesi marcate come tali.

### 4. AS IS

Descrivi la situazione attuale:

- architettura applicativa;
- componenti principali;
- flussi/processi supportati;
- integrazioni;
- dati e storage;
- deployment/runtime;
- automazioni;
- punti di forza;
- criticità, debito tecnico, rischi o limiti.

Collega ogni criticità a impatto business/operativo quando possibile.

### 5. TO BE

Proponi una possibile evoluzione:

- strategia di soluzione;
- architettura target;
- componenti da mantenere, evolvere, sostituire o creare;
- processi/funzioni gestiti;
- integrazioni future;
- governance, sicurezza, monitoraggio, scalabilità;
- quick win e release successive.

Se il TO BE non è esplicito nel repo, trattalo come proposta ragionata e non come fatto.

### 6. Piano di lavoro

Produci una proposta di project plan con:

- fasi;
- obiettivi di fase;
- deliverable;
- dipendenze;
- rischi;
- criteri di uscita.

Includi una tabella:

| Fase | Durata stimata | Attività principali | Deliverable | Dipendenze | Assunzioni |
|---|---:|---|---|---|---|

Le durate devono essere stime motivate, non impegni.

### 7. Effort e team

Proponi una stima di effort in range:

| Profilo | Coinvolgimento stimato | Fase | Note |
|---|---:|---|---|

Considera, se rilevante:

- PM / delivery lead;
- business analyst;
- solution architect;
- frontend;
- backend;
- data/AI engineer;
- DevOps/cloud;
- QA/tester;
- security/privacy;
- change management o training.

Marca chiaramente assunzioni, incertezze e driver che possono cambiare effort.

### 8. Benefici attesi

Stima possibili benefici:

- efficienza operativa;
- riduzione tempi/costi;
- riduzione rischio;
- miglioramento qualità;
- scalabilità;
- compliance/governance;
- time-to-market;
- riuso tecnologico o funzionale.

Usa questa tabella:

| Beneficio | Meccanismo | Evidenza dal repo | Stima/guess | Come validarlo |
|---|---|---|---|---|

Non presentare benefici non supportati come promesse.

### 9. Economics

Se il repo contiene dati sufficienti, proponi una struttura economics.

Se non contiene dati sufficienti, prepara solo:

- driver di costo;
- variabili da stimare;
- range preliminari se motivabili;
- domande aperte per arrivare a offerta o business case.

Tabella richiesta:

| Voce | Tipo costo | Driver | Range/guess | Fonte o assunzione |
|---|---|---|---:|---|

### 10. Rischi e punti aperti

Classifica:

- rischi tecnici;
- rischi delivery;
- rischi organizzativi;
- rischi commerciali;
- rischi dati/sicurezza;
- dipendenze esterne;
- punti da chiarire con cliente/sponsor.

### 11. Storyline deck proposta

Proponi una struttura slide-by-slide secondo le cinque sezioni:

| # | Sezione | Titolo messaggio | Contenuto chiave | Fonte | Assunzioni |
|---|---|---|---|---|---|

I titoli devono essere C-level e comunicare il messaggio, non solo l’etichetta della sezione.

### 12. Domande per completare il deck

Chiudi con le domande minime da fare prima di creare la presentazione.

Dividile in:

- bloccanti;
- utili ma non bloccanti;
- domande per migliorare economics e benefici.

## Output atteso

Produci un unico documento Markdown con sezioni ordinate come sopra.

Nel documento distingui sempre:

- **Fatti confermati**
- **Inferenze ragionate**
- **Stime**
- **Assunzioni**
- **Domande aperte**

Non creare ancora il PowerPoint.
