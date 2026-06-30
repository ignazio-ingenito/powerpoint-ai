# Cantieri Protetti AI - Creative Handoff

Status: handoff per modello/tool di generazione slide
Fonte contenuti: `Cantieri Protetti AI - Repo to Deck Brief.md`, `Cantieri Protetti AI - Executive Storyline 14 slide.md`
Audience: CEO, CTO
Tipo deck: proposta progetto R&D per futuro business case
Nome deck: `TXT Novigo Document Intelligence Core`

## Obiettivo del deck

Il deck deve spiegare perché la POC Cantieri Protetti AI può diventare un progetto R&D credibile: non una demo isolata, ma il primo nucleo di un Document Intelligence Core riusabile su business case cliente.

Il lettore deve uscire con quattro idee chiare:

- quale esigenza operativa giustifica il progetto;
- cosa fa oggi la POC e come lo fa;
- quali risultati e limiti sono già misurabili;
- quale percorso serve per trasformarla in un core governato, poi applicabile a casi come Cantieri Protetti e Guber.

## Guardrail contenutistici

- Non inventare prezzi, commitment, date contrattuali, sponsor o benefici garantiti.
- Economics: solo driver decisionali, nessun prezzo.
- Baseline: metrica operativa, non accuratezza validata.
- Cantieri Protetti e Guber: use case candidati/futuri business case, non scope già contrattualizzato.
- Perimetro: progetto R&D progressivo per disegnare una capability core replicabile.

## Cosa fa oggi il prodotto

La POC prende in input documenti PDF legati a cantieri, sicurezza, personale e adempimenti aziendali. Può lavorare su PDF con testo nativo e su PDF scansionati, usando OCR quando il testo disponibile non è sufficiente.

Oggi la POC abilita queste capacità:

- acquisisce un singolo PDF alla volta tramite API o CLI;
- estrae testo dal PDF, con fallback OCR sulle pagine più critiche;
- classifica il documento rispetto a un catalogo configurabile di tipologie documentali;
- estrae date e conserva evidenze utili a spiegare l'esito;
- assegna un esito finale tracciabile, con confidenza e diagnostica;
- distingue casi `classified`, `uncertain` e `unknown`;
- persiste run, payload e diagnostica quando richiesto;
- produce report aggregati utili per capire dove il sistema funziona e dove va migliorato.

Il punto executive: la POC non si limita a "leggere PDF". Trasforma documenti eterogenei in esiti controllabili: cosa è stato riconosciuto, con quali evidenze, con quali warning e con quale decisione finale.

## Come funziona oggi

Il flusso attuale è pensato come pipeline riusabile:

1. Il PDF entra da API (`POST /pdf/extract`) o da CLI.
2. Il motore legge il testo nativo disponibile.
3. Se il testo è scarso, entra in gioco l'OCR selettivo.
4. Il catalogo YAML applica keyword, soglie e policy per riconoscere la tipologia documento.
5. Il sistema estrae date e applica regole di filtro/rumore coerenti con il tipo documento.
6. La `Final Decision` produce un esito conservativo e tracciabile.
7. La policy LLM può essere usata per verifica/adjudication, ma nella baseline misurata l'autorità risulta deterministica.
8. Storage e report salvano run, diagnostica, payload e metriche aggregate.

Questa architettura è importante per CEO/CTO perché separa componenti che in futuro possono evolvere senza rifare tutto: OCR, catalogo, policy LLM, final decision, storage, report e API.

## Cosa produce oggi

Output operativo della singola estrazione:

- classificazione del documento;
- esito finale e confidenza;
- date rilevate;
- evidenze e diagnostica;
- warning tecnici o funzionali;
- payload strutturato;
- run persistita, se richiesto.

Output aggregato della baseline:

- 96 run totali;
- 68 documenti distinti;
- 69 run `classified`;
- 12 run `uncertain`;
- 15 run `unknown`;
- 95/96 run con testo estratto;
- 84/96 run con date rilevate;
- 0 facts strutturati nella baseline.

Questi numeri non sono accuratezza validata. Sono una baseline operativa: servono a decidere dove investire in tuning, label, facts e validazione SME.

## Limiti attuali da non nascondere

- Lavora su singolo PDF, non su fascicolo completo.
- Non esegue compliance check.
- Non calcola scadenze normative derivate.
- I facts sono previsti dallo schema, ma non popolati nella baseline aggregata.
- La persistenza è da POC, non ancora production-grade.
- I campioni disponibili non sono una ground truth validata.

Il deck deve trattare questi limiti come perimetro R&D, non come difetti da mascherare.

## Evoluzione possibile

Il percorso proposto è:

- da POC extraction a core service;
- da date/evidenze a facts strutturati;
- da run tecniche a knowledge store governato;
- da classificazione operativa a KPI validati con SME;
- da API/CLI a capability integrabile;
- da singolo documento a layer cliente per fascicoli, scadenze, compliance e workflow.

Il core deve restare separato dai business case cliente. Prima si valida la capability comune; poi si costruiscono layer specifici per Cantieri Protetti, Guber o altri casi.

## Direzione creativa

Reference primarie: `../../docs/template.pdf`, `../../template-references/*.png` e `../visual-references/cantieri-protetti-*.png`.

Reference visuali estratte da `../../docs/template.pdf`:

- `../../template-references/template-01-cover.png`: copertina, logo, spazio bianco, linee organiche teal/azzurro.
- `../../template-references/template-02-card-grid.png`: card leggere con bordo sottile, icone minimali e griglia ariosa.
- `../../template-references/template-06-roadmap.png`: roadmap pulita a fasi, con titolo executive e blocchi sobri.
- `../../template-references/template-07-three-column-value.png`: pattern iniziativa con tre colonne e fascia bassa `Valore generato`.
- `../../template-references/template-09-initiative-three-column.png`: variante tre colonne con densita' contenuto piu' alta.
- `../../template-references/template-16-closing.png`: chiusura istituzionale con gradiente/fondo leggero e blocco contatti.

Reference per il project plan:

- `../../docs/gantt.pdf`: macropiano Gantt executive con lane `Studio / Realizzazione / A regime`, timeline per mesi, macro-barre, milestone, release incrementali, ripianificazione e maintenance. Usalo come riferimento di struttura per la slide di piano; non copiarne contenuti specifici.

Vincoli visuali da rispettare:

- Font: usare lo stesso font del template, cioe' **Poppins** nelle varianti Regular, SemiBold e Bold. Non sostituire con Calibri/Inter/Arial salvo elementi legali o fallback tecnico inevitabile.
- Palette: mantenere la palette del template: sfondo bianco, testo nero/grigio scuro, accenti teal/azzurro, bordi sottili teal/azzurro. Non introdurre palette alternative.
- Gradienti: riusare il linguaggio dei gradienti del template, soprattutto curve/onde leggere teal-azzurro e fondi molto chiari della cover/closing. Non usare gradienti generici, scuri, viola, blu notte o marketing.
- Forme: usare card sottili, linee pulite, icone minimali, tanto spazio bianco. Evitare card pesanti, ombre marcate e dashboard SaaS generiche.
- Se il tool usa `../../docs/template.pptx`, riusare master/theme/font/palette esistenti invece di ricrearli manualmente.

Fedelta' visuale da verificare contro `../../docs/template.pdf`:

- formato 16:9 con ampio spazio bianco;
- header ricorrente con logo Novigo/TXT a sinistra, titolo sezione in alto e numero pagina;
- uso di teal/azzurro su linee sottili, bordi, titoli e accenti;
- card leggere con bordo sottile e angoli contenuti, non card decorative pesanti;
- pattern a tre colonne `Stato attuale / Risultati ottenuti / Prossimi passi` per slide di iniziativa o piano operativo;
- fascia o callout `Valore generato` nella parte bassa quando la slide deve esplicitare l'impatto;
- roadmap pulite a fasi, con pochi blocchi e molto spazio;
- chiusura istituzionale coerente con la pagina finale del template.

Tono visuale:

- corporate TXT/Novigo;
- pulito, arioso, commerciale;
- bianco, grigio/nero, teal/azzurro;
- font Poppins coerente con `template.pdf`;
- gradienti e linee organiche coerenti con cover/closing del template;
- header/footer coerenti con le reference;
- somiglianza concreta con `../../docs/template.pdf`, non solo con una palette generica;
- abbastanza densità per spiegare la POC, senza diventare documento tecnico.

Da evitare:

- dashboard generiche;
- troppe card decorative;
- layout stock;
- testo tecnico non tradotto in valore;
- testo rasterizzato;
- elementi non editabili.

Da preferire:

- strutture editoriali;
- processi leggibili;
- diagrammi a layer;
- card a tre colonne e fascia `Valore generato` quando il contenuto e' comparabile alle slide iniziativa del template;
- tabelle pulite;
- callout sobri;
- alternative visuali libere sulle slide `High` e `Medium`.

## Slide brief

### 1. TXT Novigo Document Intelligence Core

- Ruolo nella storia: aprire il deck e posizionare il progetto come evoluzione da POC a capability replicabile.
- Deve comunicare: nome deck, POC Cantieri Protetti AI, capability replicabile, futuri business case cliente.
- Deve includere: `TXT Novigo Document Intelligence Core`; riferimento a Cantieri Protetti AI; natura R&D.
- Contenuti opzionali: data, riservatezza, audience CEO/CTO.
- Non deve dichiarare: offerta cliente già approvata o scope contrattuale.
- Fonti: chiarimenti utente, executive storyline.
- Direzione creativa: copertina TXT/Novigo sobria.
- Forme visuali possibili: cover istituzionale, titolo ampio, elemento grafico laterale coerente.
- Reference/guardrail: `../../template-references/template-01-cover.png`, `../visual-references/cantieri-protetti-01`, `../../docs/ui/bernadelli-01`.
- Libertà creativa: Low.

### 2. Contesto, esigenza e obiettivi chiariscono perché serve un core R&D

- Ruolo nella storia: esplicitare perché il tema merita attenzione CEO/CTO.
- Deve comunicare: documenti eterogenei; bisogno di controllo e tracciabilità; obiettivo di core riusabile.
- Deve includere: tre blocchi riconoscibili `Contesto`, `Esigenza`, `Obiettivi`.
- Contenuti opzionali: citazione Cantieri Protetti e Guber negli obiettivi.
- Non deve dichiarare: riduzioni effort non validate.
- Fonti: brief, AGENTS target, reference commerciali.
- Direzione creativa: seguire da vicino il pattern con label laterali.
- Forme visuali possibili: layout a tre blocchi con linea verticale.
- Reference/guardrail: `../visual-references/cantieri-protetti-02`, `../visual-references/cantieri-protetti-09`.
- Libertà creativa: Low.

### 3. La POC trasforma PDF eterogenei in esiti tracciabili

- Ruolo nella storia: spiegare cosa fa il prodotto oggi, in termini di capacità.
- Deve comunicare: da PDF a esito controllabile.
- Deve includere:
  - input: PDF di cantiere, sicurezza, personale, adempimenti;
  - capacità: lettura testo/OCR, classificazione, estrazione date, evidenze, diagnostica;
  - output: esito classified/uncertain/unknown, payload, run/report;
  - valore: rende il documento verificabile e riusabile come dato.
- Contenuti opzionali: esempi di famiglie documentali, se aiutano la comprensione.
- Non deve dichiarare: fascicolo completo, compliance check o calcolo scadenze già disponibili.
- Fonti: README, extraction-process, repo brief.
- Direzione creativa: far vedere il passaggio documento -> dato -> esito.
- Forme visuali possibili: flow, before/after, document-to-data diagram, pipeline sintetica.
- Reference/guardrail: `../../template-references/template-02-card-grid.png`, `../visual-references/cantieri-protetti-04`, `../visual-references/cantieri-protetti-11`.
- Libertà creativa: High.

### 4. La POC funziona come una pipeline governabile

- Ruolo nella storia: spiegare come funziona la POC senza entrare in dettaglio da sviluppatori.
- Deve comunicare: il meccanismo è modulare e quindi evolvibile; la decisione finale merita una slide dedicata subito dopo.
- Deve includere:
  - ingresso API/CLI;
  - lettura testo nativo;
  - OCR selettivo;
  - catalogo YAML con keyword/soglie/policy;
  - estrazione date;
  - final decision come nodo di controllo, senza spiegarne tutti i rami in questa slide;
  - eventuale LLM verification/adjudication;
  - storage e report aggregati.
- Contenuti opzionali: evidenziare che API e CLI condividono lo stesso core.
- Non deve dichiarare: production readiness completa o LLM authority validata nella baseline.
- Fonti: codice, ADR, repo brief.
- Direzione creativa: architettura semplice, orientata al flusso operativo.
- Forme visuali possibili: pipeline a blocchi, layer diagram, system map, capability map.
- Reference/guardrail: `../../template-references/template-02-card-grid.png`, `../visual-references/cantieri-protetti-12`, `../visual-references/cantieri-protetti-16`.
- Libertà creativa: Medium.

### 5. La Final Decision rende ogni classificazione conservativa, motivata e auditabile

- Ruolo nella storia: spiegare come la POC decide il risultato finale senza lasciare l'esito a una black box.
- Deve comunicare: la decisione finale parte sempre da una baseline deterministica; il LLM può confermare o scegliere tra candidati già emersi, ma non può trasformare liberamente una proposta in risultato accettato.
- Deve includere:
  - baseline rule-based da catalogo YAML: keyword, soglie, candidati e confidenza;
  - costruzione della `Final Decision` deterministica con evidenze, reason e rejected candidates;
  - verifica LLM solo se la policy la richiede (`always`, `on_uncertain`, `on_ocr`; `disabled` la salta);
  - tre esiti accettabili: regola confermata dal LLM, `unknown` via adjudication, oppure scelta LLM di un candidato deterministico gia' presente;
  - rami di blocco: tipo fuori catalogo, tipo non candidato, categoria incoerente, confidenza sotto soglia;
  - quando il ramo e' bloccato, la proposta resta `llm_suggestion` non accettata e la decisione deterministica rimane valida con warning.
- Contenuti opzionali: indicare che nella baseline misurata tutte le 96 run hanno `decision_authority = deterministic_rule`.
- Non deve dichiarare:
  - che il LLM decide sempre;
  - che il LLM possa creare nuovi document type ufficiali;
  - che una suggestion LLM sia una classificazione accettata;
  - che `llm_verification` sia oggi authority effettiva nella baseline.
- Fonti: `/home/iingenito/projects/txt/cantieri-protetti-ai/src/txt_doc_ai_extraction/final_decision.py`, `docs/extraction-process.md`, `docs/diagrams/final-decision.mmd`, `tests/test_llm.py`, `CONTEXT.md`.
- Direzione creativa: far progettare il diagramma a DesignerGPT come flow decisionale visuale, non come lista testuale e non come diagramma tecnico Mermaid. Usare pochi nodi grandi, frecce chiare e colori sobri: baseline deterministica a sinistra, verifica/adjudication al centro, esito finale a destra.
- Forme visuali possibili: flowchart orizzontale, decision tree semplificato, swimlane `Regole` / `LLM` / `Governance`, pipeline con gate. La forma finale va scelta da DesignerGPT in base alla leggibilita' executive.
- Reference/guardrail: `../../template-references/template-07-three-column-value.png`; usare stile `template.pdf` con card sottili e fascia bassa `Valore generato`; evitare diagramma tecnico troppo ramificato.
- Libertà creativa: Medium.

Prompt di contenuto per DesignerGPT:

```text
Progetta una slide executive in stile TXT Novigo/template.pdf che spieghi come la POC prende la Final Decision.

Obiettivo visuale:
Mostrare un flow decisionale semplice, leggibile a CEO/CTO, con pochi nodi e frecce. Non deve sembrare un diagramma tecnico da documentazione; deve sembrare una slide di governance del processo.

Flow logico da rappresentare:
1. PDF + testo/OCR
2. Baseline deterministica da catalogo YAML: keyword, soglie, candidati, confidenza
3. Final Decision iniziale: evidenze, reason, rejected candidates
4. Gate: la policy LLM richiede verifica?
5. Se no: esito deterministico classified / uncertain / unknown
6. Se si: verifica LLM con output JSON validato
7. Gate conservativo:
   - conferma regola -> rule_confirmed_by_llm
   - sceglie candidato deterministico valido -> llm_adjudication
   - propone unknown -> unknown via adjudication
   - fuori catalogo / non candidato / categoria incoerente / bassa confidenza -> suggestion non accettata + warning
8. Output finale auditabile: decision_authority, evidenze, confidenza, motivazione, warning, suggestion non accettate

Vincoli:
- Non dichiarare che il LLM decide sempre.
- Non dichiarare che il LLM puo' creare nuovi document type ufficiali.
- Non presentare le suggestion LLM come classificazioni accettate.
- Evitare molto testo nei box: usare label brevi e un callout basso "Valore generato".
- Stile visuale: `../../template-references/template-07-three-column-value.png`, Poppins, card sottili, accenti teal/azzurro, molto spazio bianco, header coerente.
```

- Valore generato: la classificazione non e' una scelta opaca; ogni esito conserva autorita' decisionale, evidenze, confidenza, motivazione, rejected candidates e suggestion non accettate.

### 6. La baseline mostra risultati concreti e aree precise di tuning

- Ruolo nella storia: dare evidenza misurabile senza trasformarla in claim di accuratezza.
- Deve comunicare: esiste una base dati operativa per decidere il prossimo investimento.
- Deve includere: 96 run, 68 documenti, 69 classified, 12 uncertain, 15 unknown, 95/96 testo estratto, 84/96 date, facts 0.
- Contenuti opzionali: warning OCR/testo come driver di tuning.
- Non deve dichiarare: accuratezza certificata o performance garantita.
- Fonti: DB aggregato nel repo brief.
- Direzione creativa: numeri leggibili, pochi KPI principali, nota di cautela visibile.
- Forme visuali possibili: KPI board sobria, table+callout, evidence strip.
- Reference/guardrail: `../../template-references/template-09-initiative-three-column.png`, stile Cantieri, evitare dashboard SaaS generica.
- Libertà creativa: Medium.

### 7. I limiti della POC definiscono il perimetro R&D

- Ruolo nella storia: trasformare i limiti attuali in lavoro progettuale governabile.
- Deve comunicare: ciò che manca oggi diventa la roadmap R&D.
- Deve includere: single PDF, no fascicolo, no compliance check, no scadenze derivate, facts non popolati, production readiness da costruire.
- Contenuti opzionali: matrice oggi/gap/lavoro R&D.
- Non deve dichiarare: che i gap siano già risolti.
- Fonti: repo brief, AGENTS target, extraction-process.
- Direzione creativa: limiti ordinati, non difensivi.
- Forme visuali possibili: matrice, issue-to-action map, risk-to-work-package table.
- Reference/guardrail: `../../template-references/template-09-initiative-three-column.png`, `../visual-references/cantieri-protetti-10`, `../visual-references/cantieri-protetti-18`.
- Libertà creativa: Medium.

### 8. L'evoluzione è trasformare la POC in un core governato e integrabile

- Ruolo nella storia: mostrare il passaggio da asset corrente a target R&D.
- Deve comunicare: POC extraction -> core governato -> layer cliente.
- Deve includere:
  - facts strutturati;
  - KPI validati;
  - feedback SME;
  - privacy/audit;
  - API readiness;
  - knowledge store.
- Contenuti opzionali: distinzione visiva tra core comune e layer cliente.
- Non deve dichiarare: prodotto già pronto per tutti i clienti.
- Fonti: repo brief, chiarimenti utente.
- Direzione creativa: visualizzare evoluzione, non solo architettura statica.
- Forme visuali possibili: maturity ladder, layered architecture, before/target bridge, capability stack.
- Reference/guardrail: `../../template-references/template-02-card-grid.png`, `../visual-references/cantieri-protetti-13`, `../visual-references/cantieri-protetti-14`, `../visual-references/cantieri-protetti-16`.
- Libertà creativa: High.

### 9. I business case cliente applicano regole e workflow sopra il core

- Ruolo nella storia: chiarire come Cantieri Protetti e Guber entrano nella logica commerciale futura.
- Deve comunicare: il core comune evita di ricostruire ogni volta la capability di extraction.
- Deve includere: Cantieri Protetti e Guber come use case candidati; layer cliente per fascicoli, scadenze, compliance, workflow.
- Contenuti opzionali: altri clienti futuri come categoria, senza inventare nomi.
- Non deve dichiarare: scope contrattualizzato.
- Fonti: chiarimenti utente, repo brief.
- Direzione creativa: distinguere core comune e applicazioni cliente.
- Forme visuali possibili: stack core+client layer, two-lane use case map, platform-to-use-cases diagram.
- Reference/guardrail: `../../template-references/template-02-card-grid.png`, `../visual-references/cantieri-protetti-14`, `../visual-references/cantieri-protetti-16`.
- Libertà creativa: High.

### 10. La roadmap spiega come la POC diventa core e poi business case cliente

- Ruolo nella storia: spiegare la strategia evolutiva, prima del piano attuativo.
- Deve comunicare: la POC evolve in core governato e solo dopo abilita business case cliente.
- Deve includere: R0 baseline, R1 MVP core, R2 feedback/KPI, R3 core governato, R4 business case cliente.
- Contenuti opzionali: capability abilitate, valore atteso e gate di passaggio.
- Non deve dichiarare: commitment temporale definitivo.
- Fonti: software delivery estimation, repo brief.
- Direzione creativa: roadmap evolutiva/capability ladder, non Gantt.
- Forme visuali possibili: capability ladder, roadmap a release, percorso da POC a core a business case cliente.
- Reference/guardrail: `../../template-references/template-06-roadmap.png`, `../visual-references/cantieri-protetti-18`, `../visual-references/cantieri-protetti-19`.
- Anti-pattern: evitare piano di progetto operativo o dettaglio attività.
- Libertà creativa: Medium.

### 11. Il macropiano traduce la roadmap in fasi attuabili e range stimati

- Ruolo nella storia: trasformare la roadmap in un'ipotesi attuativa con range stimati.
- Deve comunicare: sequenza eseguibile, fasi macro, milestone, release e ripianificazione.
- Deve includere: lane `Studio / Realizzazione / A regime`, timeline `Mese 1 ... Mese n`, macro-barre, baseline validata, Release R1, ripianificazione business case, Release R2, run/maintenance se rilevante.
- Contenuti opzionali: range per mese dal brief, se resta leggibile.
- Non deve dichiarare: commitment temporale definitivo o piano operativo approvato.
- Fonti: macro project plan nel repo brief, `../../docs/gantt.pdf`.
- Direzione creativa: macropiano Gantt executive, non WBS di dettaglio.
- Forme visuali possibili: Gantt macro con poche barre leggibili, milestone/release e nota di piano indicativo.
- Reference/guardrail: `../../docs/gantt.pdf`, `../../template-references/template-06-roadmap.png`.
- Nota obbligatoria: le tempistiche sono indicative e il piano definitivo va consolidato all'avvio della fase di sviluppo.
- Anti-pattern: evitare elenco di task, sotto-attivita' o piano settimanale.
- Libertà creativa: Medium.

### 12. Il piano richiede competenze software, AI/OCR, dominio e privacy

- Ruolo nella storia: chiarire che il progetto richiede governance integrata, non solo sviluppo.
- Deve comunicare: servono competenze tecniche, dominio e controllo privacy/security.
- Deve includere: owner R&D/PM, backend/architecture, AI/OCR, SME/QA, DevOps/security/privacy.
- Contenuti opzionali: mappa competenze per fase.
- Non deve dichiarare: team assegnato o effort definitivo.
- Fonti: effort estimate.
- Direzione creativa: ruolo/competenza, non organigramma rigido.
- Forme visuali possibili: role map, swimlane, capability team matrix.
- Reference/guardrail: `../../template-references/template-09-initiative-three-column.png`, stile Cantieri, evitare organigrammi pesanti.
- Libertà creativa: High.

### 13. Gli economics restano driver per decidere l'investimento R&D

- Ruolo nella storia: dare criteri decisionali senza pricing.
- Deve comunicare: quali voci guidano investimento e rischio.
- Deve includere: sviluppo core, AI/OCR tuning, governance, futuri business case cliente; nessun prezzo.
- Contenuti opzionali: benefici potenziali come driver, non promesse.
- Non deve dichiarare: ROI o risparmi certi.
- Fonti: economics drivers del brief, chiarimenti utente.
- Direzione creativa: tabella/offerta formale, sobria.
- Forme visuali possibili: economics table, driver matrix, summary boxes.
- Reference/guardrail: `../../template-references/template-07-three-column-value.png`, `../visual-references/cantieri-protetti-20`, `../../docs/ui/bernadelli-10`.
- Libertà creativa: Low.

### 14. Le decisioni chiave sono MVP R&D, KPI, owner e use case prioritari

- Ruolo nella storia: chiudere con decisioni richieste e next steps.
- Deve comunicare: cosa serve decidere per partire.
- Deve includere: owner, document types prioritari, KPI, privacy/LLM, priorità Cantieri/Guber.
- Contenuti opzionali: open question utili per versione successiva.
- Non deve dichiarare: approvazione già ottenuta.
- Fonti: storyline, repo brief, chiarimenti utente.
- Direzione creativa: chiusura decisionale pulita.
- Forme visuali possibili: checklist, decision board, next-step table.
- Reference/guardrail: `../../template-references/template-16-closing.png`, `../visual-references/cantieri-protetti-22`, `../visual-references/cantieri-protetti-23`.
- Libertà creativa: Medium.

## Quality checklist per il modello che genera le slide

- Il deck non salta da problema a roadmap: spiega la POC.
- Slide 3 deve far capire cosa fa oggi il prodotto.
- Slide 4 deve far capire come funziona oggi la pipeline.
- Slide 5 deve far capire come viene presa la final decision, con flow visuale e non come elenco testuale.
- Le metriche sono baseline operativa, non accuratezza validata.
- Cantieri Protetti e Guber sono use case candidati.
- Gli economics non contengono prezzi.
- Le slide `Low` rispettano più da vicino le reference.
- Le slide `High` e `Medium` possono essere creative, ma non devono perdere contenuti obbligatori e guardrail.
- Il risultato deve restare modificabile in PowerPoint.
