# Prompt - Analisi repository per proposta commerciale / business case

Usa questo prompt quando devi analizzare un repository software e ricavare le informazioni utili per creare una presentazione commerciale o un business case secondo la pipeline di questo repo PowerPoint.

## Obiettivo

Analizza il repository indicato e produci un pacchetto informativo grounded per costruire una presentazione aziendale executive-ready, con focus su:

- contesto e razionale del progetto;
- AS IS tecnico/operativo;
- TO BE proposto;
- piano di lavoro e project plan stimato;
- economics, effort, benefici e assunzioni.

Il risultato non deve essere ancora un deck PowerPoint. Deve essere un dossier strutturato da usare come input per la pipeline deck.

Se il repository rappresenta una POC, un prototipo, un acceleratore o una capability tecnica esistente, il dossier deve rendere esplicito il ponte narrativo che servirà al deck:

- cosa fa oggi la POC/sistema;
- come lo fa, a livello comprensibile per CEO/CTO;
- cosa produce di osservabile o misurabile;
- quali limiti ha oggi;
- in cosa può evolvere.

Non limitarti a dire che "esiste una POC" o a descrivere solo l'architettura: il lettore deve capire quale asset si propone di evolvere.

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
   - `docs/gantt.pdf`, se presente, come riferimento per il formato del macropiano di lavoro
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

- cosa fa oggi il prodotto/POC/sistema;
- quali input prende e quali output produce;
- quali step operativi compie;
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

Per POC/prototipi, aggiungi una sottosezione obbligatoria:

#### Cosa fa oggi e come funziona

Rispondi in modo sintetico a:

- input gestiti;
- funzioni principali;
- flusso operativo;
- output e artifact prodotti;
- risultati osservabili o metriche disponibili;
- cosa non copre ancora.

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

Per POC/prototipi, chiarisci esplicitamente il percorso evolutivo:

- da POC a servizio/core capability;
- da output tecnico a dato/processo utilizzabile dal business;
- da caso singolo a business case cliente o capability replicabile;
- nuove funzioni possibili, ad esempio workflow, fascicoli, compliance, dashboard, integrazioni o automazioni.

### 6. Piano di lavoro e project plan stimato

Produci una proposta di project plan stimato, adatta a una proposta commerciale/business case per sviluppo software.

La stima deve essere utile per discutere il progetto con management, ma non deve sembrare un commitment. Usa sempre range, assunzioni e driver di variazione.

Questa sezione deve produrre **due viste distinte**:

1. una **roadmap evolutiva**, che spiega la strategia di evoluzione del prodotto/capability;
2. un **macropiano Gantt-like**, ispirato a `docs/gantt.pdf` quando disponibile, che mostra fasi attuabili, range stimati, milestone e rilasci.

Non fonderle in una sola tabella: la roadmap risponde a "dove vogliamo arrivare e in quale logica evolutiva"; il Gantt macro risponde a "come potremmo attuarlo, con quali fasi e tempi indicativi".

Includi prima una vista sintetica delle opzioni di delivery:

| Opzione | Obiettivo | Scope incluso | Size stimata | Timeline stimata | Trade-off |
|---|---|---|---|---:|---|

Quando utile, usa tre livelli:

- **MVP / quick win:** minimo per validare valore e rischio.
- **Core replicabile:** soluzione governabile e riusabile.
- **Full scope / business case cliente:** estensione completa con integrazioni, workflow, UI o processi cliente.

Poi costruisci una roadmap evolutiva con:

- capability o release evolutive;
- obiettivo strategico di ciascun passo;
- valore generato;
- prerequisiti o dipendenze;
- condizioni di passaggio al passo successivo;
- relazione tra core comune e business case cliente.

Includi questa tabella:

| Step evolutivo | Obiettivo strategico | Capability abilitate | Valore atteso | Prerequisiti / gate | Note e assunzioni |
|---|---|---|---|---|---|

Poi costruisci il macropiano attuativo con:

- 3-4 lane/fasi macro, ad esempio `Studio`, `Realizzazione`, `A regime`, adattate al progetto;
- asse temporale indicativo per mesi, sprint o trimestri; se le durate sono incerte, usa `Mese 1 ... Mese n` oppure range come `Mese 2-3`;
- 6-10 macro-attività massimo, non singole attività operative;
- milestone decisionali;
- release incrementali;
- eventuali momenti di ripianificazione;
- eventuale application maintenance o run a regime, solo se rilevante;
- dipendenze e assunzioni principali.

Non scendere nel dettaglio di ogni singola attività. Evita task granulari, sotto-task, checklist implementative, daily/weekly plan o dettaglio da project manager operativo. Il piano deve restare leggibile come slide executive, con range stimati e assunzioni chiare.

Includi questa tabella come base per una futura slide Gantt:

| Lane/Fase | Macro-attività | Tipo | Inizio indicativo | Fine indicativa | Output / milestone | Dipendenze | Assunzioni |
|---|---|---|---:|---:|---|---|---|

Usa `Tipo` per distinguere almeno:

- `Barra`: macro-attività o fase;
- `Milestone`: punto decisionale o validazione;
- `Release`: rilascio incrementale;
- `Run`: attività a regime / maintenance, se rilevante;
- `Ripianificazione`: punto di revisione piano, se rilevante.

Apri la sezione con una nota simile a questa, adattandola al caso:

> Le tempistiche sono indicative e costruite su esperienza TXT Novigo in progetti analoghi; il piano definitivo va consolidato all'avvio della fase di sviluppo.

Includi anche una vista per milestone:

| Milestone | Quando | Evidenza di completamento | Decisione abilitata |
|---|---:|---|---|

Regole:

- Le durate devono essere **stime motivate**, non impegni.
- Se il repository non basta per stimare, proponi una stima preliminare marcata come **guess da validare**.
- Esplicita i driver che possono cambiare timeline: scope, integrazioni, dati disponibili, validazione utente/SME, sicurezza, compliance, deployment, qualità dei test, migrazioni, dipendenze cliente.
- Non trasformare effort o timeline in prezzo.
- Se lo scope e' troppo ambiguo, indica quali domande sono bloccanti prima di usare la stima in offerta.

### 7. Effort e team

Prima dell'effort per ruolo, assegna una **delivery size** qualitativa al progetto o alle opzioni di delivery.

Usa questa scala, adattandola al contesto e marcandola come **stima da validare**:

| Size | Indicazione orientativa | Quando usarla |
|---|---|---|
| XS | Intervento molto piccolo / spike / assessment rapido | Analisi, tuning puntuale, prototipo circoscritto |
| S | Piccolo progetto controllato | MVP limitato, pochi componenti, poche dipendenze |
| M | Progetto medio | Più componenti, qualche integrazione, test e hardening base |
| L | Progetto ampio | Core riusabile, integrazioni, governance, sicurezza, rollout progressivo |
| XL | Programma complesso | Più stream, più stakeholder, integrazioni rilevanti, change/processo |
| XXL | Programma enterprise o trasformazione | Multi-cliente/multi-paese, compliance forte, migrazioni o piattaforma critica |

Produci una tabella di sizing:

| Ambito/opzione | Size stimata | Rationale | Driver che possono aumentare/diminuire la size | Confidenza |
|---|---|---|---|---|

Regole per la size:

- La size non e' un prezzo.
- La size non sostituisce effort e timeline: li sintetizza per confronto executive.
- Se mancano dati, usa `Confidenza: bassa` e marca la size come guess da validare.
- Considera questi driver: numero componenti, integrazioni, UI, dati/migrazioni, AI/ML, sicurezza/privacy, compliance, deployment, test/QA, stakeholder, change management, dipendenze cliente.

Proponi una stima di effort in range:

| Profilo | Coinvolgimento stimato | Fase | Note |
|---|---:|---|---|

Se possibile, aggiungi anche una stima aggregata per fase:

| Fase | Effort stimato | Profili principali | Driver di variazione |
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

- size stimata come proxy executive di complessita' e ordine di grandezza;
- driver di costo;
- variabili da stimare;
- range preliminari se motivabili;
- domande aperte per arrivare a offerta o business case.

Includi una sintesi economics/sizing:

| Opzione | Size | Driver principali | Implicazione economics | Dati mancanti |
|---|---|---|---|---|

Tabella richiesta:

| Voce | Tipo costo | Driver | Range/guess | Fonte o assunzione |
|---|---|---|---:|---|

Non convertire automaticamente la size in prezzo. Usala per spiegare ordine di grandezza, complessita' e priorita' decisionale.

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

Se la storyline nasce da una POC/repo software, includi prima di roadmap/economics almeno una slide, o due se serve, che spieghi:

- cosa fa la POC;
- come funziona;
- cosa produce;
- quali limiti ha;
- in cosa può evolvere.

Non comprimere questa parte fino a renderla implicita.

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
