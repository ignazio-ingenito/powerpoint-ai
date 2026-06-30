# Prompt DesignerGPT - TXT Novigo Document Intelligence Core

Genera una presentazione executive-ready in italiano per CEO/CTO.

Il deck deve avere **14 slide** e titolo:

`TXT Novigo Document Intelligence Core`

Sottotitolo:

`Da POC Cantieri Protetti AI a capability replicabile`

## Fonti contenutistiche

Usa come fonti principali:

- `../drafts/Cantieri Protetti AI - Repo to Deck Brief.md`
- `../drafts/Cantieri Protetti AI - Executive Storyline 14 slide.md`
- `../drafts/Cantieri Protetti AI - Creative Handoff.md`
- `prompt.cantieri-protetti-ai-recovered-v2-14slide.md`

Non usare `../attempts/txt-novigo-slides/` come reference visuale. Quel materiale serve solo come memoria interna del tentativo migliore, ma non deve condizionare composizione, layout o immagini del nuovo run.

## Output richiesto

Produci:

1. un PDF con tutte le 14 slide;
2. un file ZIP scaricabile con tutti gli asset e le specifiche necessarie a replicare le slide in PowerPoint.

Il file ZIP deve includere almeno:

- immagini e illustrazioni sorgente usate nelle slide;
- icone in formato vettoriale o comunque riutilizzabile;
- eventuali loghi o asset brand;
- palette colori con codici HEX/RGB;
- specifica font: famiglia, pesi e fallback;
- gradienti, sfondi, pattern o texture usati;
- eventuali diagrammi sorgente o specifiche per ricrearli;
- specifiche layout: formato slide, griglia, margini, header/footer, dimensioni e posizionamento ricorrente degli elementi;
- note su quali elementi sono ricostruibili come oggetti PowerPoint e quali restano raster.

Non produrre un PPTX. L'obiettivo e' ottenere un PDF di alta qualita' e un pacchetto asset/spec che consenta di ricostruire manualmente le slide in PowerPoint se necessario.

## Obiettivo narrativo

Il deck deve spiegare perche' la POC Cantieri Protetti AI puo' diventare il primo nucleo di un core di intelligenza documentale riusabile su futuri business case cliente.

Il lettore deve capire:

- quale bisogno operativo giustifica il progetto;
- cosa fa oggi la POC;
- come funziona;
- come viene presa la decisione finale;
- cosa produce;
- quali limiti ha;
- come puo' evolvere;
- quali use case futuri abilita;
- quale roadmap evolutiva seguire;
- quale macropiano attuativo ipotizzare;
- quali decisioni servono per procedere.

## Guardrail contenutistici

- Non inventare prezzi.
- Non dichiarare ROI o benefici garantiti.
- Non dichiarare date contrattuali o commitment di delivery.
- Non dichiarare scope cliente gia' contrattualizzato.
- Cantieri Protetti e Guber sono use case candidati, non clienti gia' in scope.
- Le metriche della baseline sono operative, non accuratezza validata.
- Il progetto e' R&D: serve a costruire un core replicabile, non una singola applicazione cliente definitiva.
- Il Gantt e' un'ipotesi di macropiano, non un piano operativo approvato.

## Stile visuale da ricreare

Non usare un template allegato e non copiare layout da slide precedenti. Ricrea uno stile corporate TXT/Novigo usando solo queste regole.

### Palette

- Background principale: bianco `#FFFFFF`.
- Background secondario molto leggero: `#F7F7F7`, `#F3F6F7`, `#EBEFF5`.
- Testo primario: quasi nero `#050505` / `#080808`.
- Testo secondario: grigio medio `#5F5F5F` / `#666666`.
- Linee neutre e separatori: grigio chiaro `#A0A0A0`, `#A7A7A7`, `#EBEFF5`.
- Accento teal principale: `#52AB9F` / `#51AA9F`.
- Accento teal scuro: `#4FA7A8`.
- Accento azzurro: `#368BD6`, `#307FE2`, `#4D9CCA`.
- Accento azzurro chiaro: `#9FCCDB`, `#99CCCC`.

Usa teal e azzurro come accenti, non come sfondo dominante.

### Tipografia

- Usa un font moderno simile a **Poppins**.
- Titoli: semi-bold/bold, neri, grandi ma non eccessivi.
- Body: regular, grigio scuro, poche righe per slide.
- Numerazione slide: evidente ma sobria, in teal/azzurro.
- Evita testi piccoli, dense note e paragrafi lunghi.

### Linee, card e forme

- Linee sottili, pulite, in teal/azzurro o grigio chiaro.
- Card leggere con bordo sottile, sfondo bianco o grigio chiarissimo.
- Angoli moderati, non card troppo arrotondate.
- Ombre assenti o molto leggere.
- Icone lineari, coerenti, non decorative.
- Usa molto spazio bianco.

### Gradienti

- Usa gradienti solo come accento leggero, non come sfondo pieno.
- Preferisci gradienti molto chiari teal -> azzurro, con opacita' bassa.
- Ammessi elementi organici o linee leggere teal/azzurro in cover e chiusura.
- Evita gradienti scuri, viola, blu notte, marketing o SaaS dashboard.

### Visual

Il deck deve essere visuale e vario, non monotono. Evita di usare la stessa struttura a card su troppe slide consecutive. Ogni slide dovrebbe avere una composizione riconoscibilmente diversa, coerente con il messaggio.

Usa:

- flow per la POC;
- pipeline numerata;
- flow decisionale per la Final Decision;
- KPI board per output e baseline;
- matrice limiti;
- illustrazione astratta di evoluzione;
- card per casi d'uso;
- roadmap evolutiva;
- Gantt macro;
- capability wheel o mappa competenze;
- driver economics con icone;
- checklist finale per decisioni.

### Varieta' compositiva obbligatoria

Distribuisci le composizioni in modo vario:

- 1 cover illustrata;
- 1 slide split narrative + pain point iconici;
- 1 griglia capability;
- 1 pipeline orizzontale;
- 1 flow decisionale;
- 1 KPI board;
- 1 matrice limiti;
- 1 illustrazione di evoluzione / maturity;
- 1 mappa use case;
- 1 roadmap;
- 1 Gantt macro;
- 1 capability wheel o mappa competenze;
- 1 driver matrix economics;
- 1 checklist/decision board finale.

Usa illustrazioni astratte, diagrammi e immagini solo quando rendono la lettura piu' facile. Devono sembrare parte del sistema visuale corporate, non immagini stock decorative. Evita ripetitivita': non creare 14 slide tutte con lo stesso header + tre card + icone.

## Struttura 14 slide

### 1. TXT Novigo Document Intelligence Core

Messaggio: da POC Cantieri Protetti AI a capability replicabile.

Contenuto:

- progetto R&D per costruire un core di intelligenza documentale riusabile;
- riferimento a POC Cantieri Protetti AI;
- nessuna promessa commerciale definitiva.

Visual: cover illustrata con un elemento centrale astratto di document intelligence / stack dati / AI core. Usare profondita' leggera, linee sottili teal/azzurro e molto spazio bianco.

### 2. Contesto e bisogno operativo

Messaggio: oggi le aziende gestiscono documenti eterogenei, frammentati e costosi da controllare.

Contenuto:

- grandi volumi di documenti eterogenei legati a cantieri, sicurezza, personale e adempimenti;
- informazione frammentata;
- ricerca lenta e manuale;
- rischi di non conformita' e scadenze mancate;
- dati non strutturati e non riutilizzabili;
- bisogno: trasformare documenti in informazioni affidabili, tracciabili e utilizzabili.

Visual: layout split. A sinistra breve testo narrativo; a destra pain point iconici in una colonna o orbita leggera. Non usare una semplice griglia di card.

### 3. Cosa fa oggi la POC Cantieri Protetti AI

Messaggio: trasforma documenti eterogenei in esiti controllabili.

Contenuto:

- input PDF via API o CLI;
- estrazione testo, con OCR se necessario;
- classificazione rispetto a catalogo configurabile;
- estrazione date con evidenze;
- final decision tracciabile con confidenza;
- esiti: classified, uncertain, unknown;
- persistenza run, payload e diagnostica;
- report aggregati per analisi e miglioramento.

Visual: griglia di capability con icone lineari, ma diversa dalla slide 2: più operativa, con blocchi piccoli e un flusso implicito input -> output.

### 4. Come funziona oggi: la pipeline

Messaggio: la POC e' una pipeline modulare, non uno script isolato.

Pipeline:

1. PDF in ingresso da API o CLI.
2. Lettura testo nativo.
3. OCR selettivo sulle pagine critiche.
4. Catalogo YAML con keyword, soglie e policy.
5. Estrazione date e filtri rumore.
6. Final Decision conservativa e tracciabile.
7. Storage e report.

Visual: pipeline orizzontale numerata con icone e linee sottili. Deve sembrare un processo end-to-end, non una lista.

### 5. Come decide: Final Decision conservativa e auditabile

Messaggio: la classificazione finale non e' una black box.

Contenuto:

- prima viene costruita una baseline deterministica da catalogo YAML;
- il catalogo produce candidati, soglie, confidenza ed evidenze;
- la Final Decision iniziale conserva reason, evidenze e rejected candidates;
- il LLM puo' essere usato solo come verifica/adjudication regolata;
- il LLM puo' confermare una regola o scegliere un candidato deterministico valido;
- se propone un tipo fuori catalogo, non candidato, incoerente o sotto soglia, resta una suggestion non accettata;
- l'output finale conserva decision_authority, evidenze, confidenza, motivazione e warning.

Vincoli:

- non dire che il LLM decide sempre;
- non dire che il LLM puo' creare nuovi document type ufficiali;
- non presentare le suggestion LLM come classificazioni accettate.

Visual: flow decisionale executive. Struttura consigliata: baseline deterministica -> gate LLM -> gate conservativo -> output auditabile. Inserire callout: "Ogni esito conserva autorita' decisionale, evidenze e warning."

### 6. Output della POC

Messaggio: la POC produce output operativi e una baseline utile al tuning.

Per ogni estrazione:

- classificazione del documento;
- esito finale e confidenza;
- date rilevate;
- evidenze e diagnostica;
- warning tecnici o funzionali;
- payload strutturato;
- run persistita.

Baseline aggregata:

- 96 run totali;
- 68 documenti distinti;
- 69 run classified;
- 12 run uncertain;
- 15 run unknown;
- 95/96 run con testo estratto;
- 84/96 run con date rilevate;
- 0 facts strutturati nella baseline.

Nota visibile: non e' accuratezza validata, ma baseline operativa.

Visual: composizione ibrida: a sinistra checklist output per singola estrazione, a destra KPI board con numeri grandi. Evitare otto card uguali.

### 7. Limiti attuali: perimetro R&D

Messaggio: i limiti sono espliciti e definiscono il percorso di evoluzione.

Contenuto:

- lavora su singolo PDF, non su fascicolo completo;
- non esegue compliance check;
- non calcola scadenze normative derivate;
- facts previsti ma non popolati nella baseline aggregata;
- persistenza da POC, non ancora production-grade;
- campioni disponibili non ground truth validata.

Visual: matrice `Limite attuale -> Implicazione R&D`, con icone warning leggere e callout basso: "Limiti espliciti, per un percorso di evoluzione credibile."

### 8. Evoluzione possibile

Messaggio: il core resta separato dai business case cliente.

Percorso:

- da POC extraction a core service;
- da date/evidenze a facts strutturati;
- da run tecniche a knowledge store governato;
- da classificazione operativa a KPI validati con SME;
- da singolo documento a layer cliente per fascicoli, scadenze, compliance e workflow.

Visual: illustrazione di evoluzione, maturity ladder o percorso POC -> core -> layer cliente. Usare una metafora visiva sobria, non solo box testuali.

### 9. Casi d'uso candidati

Messaggio: Cantieri Protetti e Guber sono business case candidati sopra il core.

Cantieri Protetti:

- gestione documenti di cantiere;
- sicurezza e formazione;
- personale e qualifiche;
- adempimenti e verifiche;
- scadenze e rinnovi.

Guber:

- governance documentale;
- compliance e controlli;
- processi amministrativi;
- tracciabilita' e audit;
- workflow strutturati.

Nota: use case candidati; scope e requisiti saranno definiti e validati con il cliente in fasi successive.

Visual: mappa use case: core comune al centro o alla base, con due applicazioni cliente distinte. Le card cliente possono esserci, ma devono essere integrate in una mappa, non isolate.

### 10. Roadmap evolutiva: da POC a core e business case

Messaggio: l'evoluzione deve separare POC, core governato e futuri business case cliente.

Step:

- R0 - Baseline validata: risultati, limiti e KPI operativi visibili.
- R1 - MVP core: primo servizio controllabile su documenti prioritari.
- R2 - Feedback e KPI: label, report e tuning per miglioramento misurabile.
- R3 - Core governato: privacy, storage, osservabilita', audit e API readiness.
- R4 - Business case cliente: fascicoli, scadenze, workflow e integrazioni solo dopo approvazione.

Visual: roadmap evolutiva o capability ladder con gate visibili. Non fare un Gantt in questa slide e non ripetere la pipeline.

### 11. Macropiano attuativo: fasi e range stimati

Messaggio: la roadmap puo' essere tradotta in un'ipotesi attuativa leggibile, senza scendere nella WBS.

Gantt macro:

- Studio: avvio, perimetro, KPI target e baseline operativa, indicativamente Mese 1.
- Realizzazione: MVP core, feedback/KPI, hardening e release core replicabile, indicativamente Mese 2-6.
- A regime: business case cliente foundation e maintenance/miglioramento continuo, indicativamente Mese 7-n.
- Milestone/release: baseline validata, Release R1 MVP core, ripianificazione business case, Release R2 core replicabile.

Nota visibile:

`Tempistiche indicative; piano definitivo da consolidare all'avvio della fase di sviluppo.`

Visual: Gantt macro executive con lane Studio / Realizzazione / A regime, range mensili, poche barre, milestone e release. Non creare un elenco task e non usare lo stesso layout della roadmap.

### 12. Competenze e tecnologia

Messaggio: il progetto richiede competenze integrate, non solo sviluppo.

Competenze:

- AI & NLP: OCR, LLM, classificazione;
- Ingegneria software: API, pipeline, integrazione;
- Data & Knowledge: modelli dati, facts, governance;
- Cloud & DevOps: sicurezza, osservabilita', qualita';
- Dominio & SME: validazione, regole, KPI.

Visual: capability wheel / cerchio centrale `Document Intelligence Core` con aree intorno: sicurezza, governance, qualita', osservabilita'. Deve differenziarsi nettamente da roadmap e Gantt.

### 13. Economics: driver decisionali

Messaggio: nessun prezzo nel deck; focus su valore e priorita' di investimento.

Driver:

- efficienza operativa: riduzione tempi di ricerca, controllo e gestione documentale;
- qualita' e conformita': informazioni piu' affidabili per decisioni e riduzione rischio non conformita';
- scalabilita': capability riusabile su piu' processi e business case;
- time to value: si parte da quick win e si cresce per layer.

Dati necessari per un business case numerico:

- volumi documenti;
- tempi manuali attuali;
- SLA;
- policy retention;
- target deployment;
- policy LLM.

Visual: driver matrix con icone e un box separato "Dati necessari per business case numerico". Usare colonne solo se restano leggere; alternativa preferita: 2x2 driver + callout dati.

### 14. Decisioni richieste

Messaggio: la POC e' l'inizio; il core e' l'asset; i business case sono la destinazione.

Decisioni:

- confermare il percorso R&D per la costruzione del core;
- nominare un owner del progetto R&D;
- scegliere document type prioritari per MVP core;
- definire KPI target: accuratezza validata, tempi, copertura, riduzione effort manuale;
- chiarire policy privacy, retention e uso LLM;
- prioritizzare i business case cliente, inclusi Cantieri Protetti e Guber.

Visual: decision board finale con checklist executive e callout forte: "La POC e' l'inizio. Il core e' l'asset. I business case sono la destinazione." Usare icona target o percorso, non una semplice lista.
