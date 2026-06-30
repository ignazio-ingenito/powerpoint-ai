# Prompt recuperato v2 - TXT Novigo Document Intelligence Core 14 slide

Questo prompt riparte dal risultato migliore visto in `../attempts/txt-novigo-slides/` e lo aggiorna con le decisioni successive:

- deck a 14 slide;
- slide dedicata alla Final Decision;
- roadmap evolutiva separata dal macropiano attuativo;
- Gantt macro con range stimati;
- economics senza prezzi;
- Cantieri Protetti e Guber citati come use case candidati.

## Prompt

Crea una presentazione executive-ready in italiano, in stile corporate TXT/Novigo, per CEO e CTO.

Titolo della presentazione:

`TXT Novigo Document Intelligence Core`

Sottotitolo:

`Da POC Cantieri Protetti AI a capability replicabile`

Obiettivo del deck:

Spiegare perche' la POC Cantieri Protetti AI puo' diventare il primo nucleo di un core di intelligenza documentale riusabile su futuri business case cliente.

Il deck deve essere sintetico, visuale, leggibile a livello C-level. Non deve essere tecnico in modo eccessivo, ma deve far capire concretamente:

- cosa fa oggi la POC;
- come funziona a livello di pipeline;
- come viene presa la decisione finale;
- cosa produce;
- quali limiti ha;
- come puo' evolvere;
- quali casi d'uso futuri abilita;
- quale roadmap evolutiva seguire;
- quale macropiano attuativo ipotizzare;
- quali competenze servono;
- quali driver decisionali/economics considerare;
- quali decisioni servono per procedere.

## Guardrail

- Non inventare prezzi.
- Non dichiarare ROI o benefici garantiti.
- Non dichiarare date contrattuali o commitment di delivery.
- Non dichiarare scope cliente gia' contrattualizzato.
- Cantieri Protetti e Guber sono use case candidati, non clienti gia' in scope.
- Le metriche della baseline sono operative, non accuratezza validata.
- Il progetto e' R&D: serve a costruire un core replicabile, non una singola applicazione cliente definitiva.
- Il Gantt e' un'ipotesi di macropiano, non un piano operativo approvato.

## Stile visuale

Usa uno stile corporate pulito, vicino al risultato in `../attempts/txt-novigo-slides/`:

- sfondo bianco;
- testo nero/grigio scuro;
- accenti teal/azzurro;
- font moderno simile a Poppins;
- icone lineari;
- card leggere;
- diagrammi semplici;
- molto spazio bianco;
- layout 16:9;
- logo TXT/Novigo in basso;
- numerazione slide evidente in alto a sinistra;
- look consulenziale, non SaaS dashboard.

Usa visual e diagrammi per evitare slide solo testuali:

- flow per la POC;
- pipeline numerata;
- flow decisionale per la Final Decision;
- KPI board per output e baseline;
- matrice limiti;
- illustrazione di evoluzione;
- card per casi d'uso;
- roadmap evolutiva;
- Gantt macro;
- diagramma circolare o capability map per competenze;
- driver economics con icone;
- checklist finale per decisioni.

## Struttura richiesta: 14 slide

### 1. TXT Novigo Document Intelligence Core

Messaggio: da POC Cantieri Protetti AI a capability replicabile.

Contenuto:

- progetto R&D per costruire un core di intelligenza documentale riusabile;
- riferimento a POC Cantieri Protetti AI;
- nessuna promessa commerciale definitiva.

Visual: cover con illustrazione astratta di document intelligence / stack dati / AI core.

### 2. Contesto e bisogno operativo

Messaggio: oggi le aziende gestiscono documenti eterogenei, frammentati e costosi da controllare.

Contenuto:

- grandi volumi di documenti eterogenei legati a cantieri, sicurezza, personale e adempimenti;
- informazione frammentata;
- ricerca lenta e manuale;
- rischi di non conformita' e scadenze mancate;
- dati non strutturati e non riutilizzabili;
- bisogno: trasformare documenti in informazioni affidabili, tracciabili e utilizzabili.

Visual: testo a sinistra, lista di pain point con icone a destra.

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

Visual: griglia di capability con icone.

### 4. Come funziona oggi: la pipeline

Messaggio: la POC e' una pipeline modulare, non uno script isolato.

Contenuto pipeline:

1. PDF in ingresso da API o CLI.
2. Lettura testo nativo.
3. OCR selettivo sulle pagine critiche.
4. Catalogo YAML con keyword, soglie e policy.
5. Estrazione date e filtri rumore.
6. Final Decision conservativa e tracciabile.
7. Storage e report.

Visual: pipeline orizzontale numerata con icone.

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

Visual: flow decisionale executive, non diagramma tecnico troppo ramificato. Struttura consigliata: baseline deterministica -> gate LLM -> gate conservativo -> output auditabile. Inserire un callout: "Ogni esito conserva autorita' decisionale, evidenze e warning."

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

Nota: non e' accuratezza validata, ma baseline operativa.

Visual: due colonne, output per singola estrazione + KPI baseline.

### 7. Limiti attuali: perimetro R&D

Messaggio: i limiti sono espliciti e definiscono il percorso di evoluzione.

Contenuto:

- lavora su singolo PDF, non su fascicolo completo;
- non esegue compliance check;
- non calcola scadenze normative derivate;
- facts previsti ma non popolati nella baseline aggregata;
- persistenza da POC, non ancora production-grade;
- campioni disponibili non ground truth validata.

Visual: matrice o griglia con icone warning leggere e callout: "Limiti espliciti, per un percorso di evoluzione credibile."

### 8. Evoluzione possibile

Messaggio: il core resta separato dai business case cliente.

Percorso:

- da POC extraction a core service;
- da date/evidenze a facts strutturati;
- da run tecniche a knowledge store governato;
- da classificazione operativa a KPI validati con SME;
- da singolo documento a layer cliente per fascicoli, scadenze, compliance e workflow.

Visual: evoluzione illustrata come crescita progressiva, maturity ladder o percorso da seme ad albero.

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

Visual: due card cliente sopra un core comune.

### 10. Roadmap evolutiva: da POC a core e business case

Messaggio: l'evoluzione deve separare POC, core governato e futuri business case cliente.

Step:

- R0 - Baseline validata: risultati, limiti e KPI operativi visibili.
- R1 - MVP core: primo servizio controllabile su documenti prioritari.
- R2 - Feedback e KPI: label, report e tuning per miglioramento misurabile.
- R3 - Core governato: privacy, storage, osservabilita', audit e API readiness.
- R4 - Business case cliente: fascicoli, scadenze, workflow e integrazioni solo dopo approvazione.

Visual: roadmap evolutiva o capability ladder. Non fare un Gantt in questa slide.

### 11. Macropiano attuativo: fasi e range stimati

Messaggio: la roadmap puo' essere tradotta in un'ipotesi attuativa leggibile, senza scendere nella WBS.

Gantt macro:

- Studio: avvio, perimetro, KPI target e baseline operativa, indicativamente Mese 1.
- Realizzazione: MVP core, feedback/KPI, hardening e release core replicabile, indicativamente Mese 2-6.
- A regime: business case cliente foundation e maintenance/miglioramento continuo, indicativamente Mese 7-n.
- Milestone/release: baseline validata, Release R1 MVP core, ripianificazione business case, Release R2 core replicabile.

Nota visibile:

`Tempistiche indicative; piano definitivo da consolidare all'avvio della fase di sviluppo.`

Visual: Gantt macro executive con lane Studio / Realizzazione / A regime, range mensili, poche barre, milestone e release. Non creare un elenco task.

### 12. Competenze e tecnologia

Messaggio: il progetto richiede competenze integrate, non solo sviluppo.

Competenze:

- AI & NLP: OCR, LLM, classificazione;
- Ingegneria software: API, pipeline, integrazione;
- Data & Knowledge: modelli dati, facts, governance;
- Cloud & DevOps: sicurezza, osservabilita', qualita';
- Dominio & SME: validazione, regole, KPI.

Visual: capability wheel / cerchio centrale `Document Intelligence Core` con aree intorno: sicurezza, governance, qualita', osservabilita'.

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

Visual: 4 colonne con icone e breve descrizione + box "Dati necessari per business case numerico".

### 14. Decisioni richieste

Messaggio: la POC e' l'inizio; il core e' l'asset; i business case sono la destinazione.

Decisioni:

- confermare il percorso R&D per la costruzione del core;
- nominare un owner del progetto R&D;
- scegliere document type prioritari per MVP core;
- definire KPI target: accuratezza validata, tempi, copertura, riduzione effort manuale;
- chiarire policy privacy, retention e uso LLM;
- prioritizzare i business case cliente, inclusi Cantieri Protetti e Guber.

Visual: checklist executive + quote/callout finale + icona target.
