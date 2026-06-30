# Cantieri Protetti AI - Executive Storyline 14 slide

Status: variante 14 slide CEO/CTO, pronta per generazione PPTX
Fonte: `Cantieri Protetti AI - Repo to Deck Brief.md`
Tipo deck: proposta progetto R&D per futuro business case
Audience: CEO, CTO
Output: scaletta executive prima della generazione PowerPoint

## Chiarimenti Recepiti

- **Audience:** CEO e CTO.
- **Tipo deck:** proposta progetto R&D per futuro business case.
- **Economics:** solo driver, nessun prezzo.
- **Baseline:** inclusa ma marcata come metrica operativa, non accuratezza validata.
- **Use case citati:** Cantieri Protetti e Guber.
- **Perimetro:** percorso progressivo; il progetto R&D deve disegnare una soluzione core replicabile su business case cliente.
- **Formato deck:** 14 slide.
- **Livello:** CEO ready, con spazio dedicato alla POC, alla Final Decision, al TO BE, alla roadmap evolutiva, al macropiano attuativo e agli economics.

## Intento Del Deck

**Messaggio guida:** la POC Cantieri Protetti AI puo' diventare la base di un progetto R&D per disegnare un core di Document Intelligence replicabile su futuri business case cliente.

**Decisione che il deck deve abilitare:** approvare un percorso R&D progressivo per trasformare una POC misurabile in una capability core riusabile, distinguendo il lavoro sul core dai futuri business case cliente.

**Nome deck confermato dall'utente:** `TXT Novigo Document Intelligence Core`.

## Razionale Della Variante 14 Slide

Questa e' la variante target. La struttura a 14 slide serve a:

- distinguere architettura core e applicazioni cliente;
- spiegare la Final Decision come gate visuale, non come dettaglio tecnico nascosto;
- separare roadmap evolutiva, macropiano attuativo e competenze/team;
- rendere piu' chiara la transizione dalla POC alla capability replicabile;
- evitare che TO BE, piano ed economics diventino troppo densi.

## Executive Narrative

1. I documenti di cantiere e compliance sono eterogenei, sensibili e spesso non strutturati: la gestione manuale limita controllo, scalabilita' e tracciabilita'.
2. La POC non e' solo una demo tecnica: prende PDF eterogenei e restituisce classificazione, date, evidenze, diagnostica e run tracciabili.
3. Il funzionamento e' gia' impostato come pipeline riusabile: testo/OCR, catalogo, regole/LLM policy, final decision, report e storage sono separati.
4. La Final Decision e' un gate di governance: parte da una baseline deterministica, consente verifica/adjudication LLM solo entro regole conservative e mantiene evidenze, confidenza, authority e warning.
5. I risultati sono misurabili: 96 run, 69 classificazioni, 12 uncertain, 15 unknown, 95/96 con testo estratto e 84/96 con date rilevate.
6. Il gap e' esplicito: facts a zero, accuratezza non validata, scope single-PDF e assenza di fascicolo/compliance delimitano il lavoro R&D.
7. Il target e' trasformare la POC in un core governato, misurabile e integrabile, separato dai futuri layer applicativi cliente.
8. I business case cliente potranno applicare regole, fascicoli, scadenze e workflow sopra il core solo dopo aver validato la base comune.
9. La decisione raccomandata e' procedere per fasi: baseline validata, MVP core, feedback/metriche, hardening e applicazione a business case cliente.

## Slide Outline 14 Slide

| # | Sezione | Titolo messaggio | Contenuto executive | Visual suggerito | Fonte | Note |
|---:|---|---|---|---|---|---|
| 1 | Copertina | TXT Novigo Document Intelligence Core | Sottotitolo: "Dalla POC Cantieri Protetti AI a una capability replicabile per futuri business case cliente" | Copertina TXT/Novigo con titolo ampio | Dossier + utente | Nome confermato dall'utente |
| 2 | Contesto / Esigenza / Obiettivi | Contesto, esigenza e obiettivi chiariscono perche' serve un core R&D | Documenti eterogenei, esigenza di controllo/tracciabilita', obiettivo di core riusabile per Cantieri Protetti e Guber | Layout reference con colonna laterale e blocchi numerati | Dossier, AGENTS target, docs/reference.1 | Sezione cardine esplicita |
| 3 | POC | La POC trasforma PDF eterogenei in esiti tracciabili | PDF -> classificazione -> date/evidenze -> run/report | Flow orizzontale | README, extraction-process | Spiega cosa fa e cosa produce |
| 4 | POC | La POC funziona come pipeline riusabile, non come script isolato | Testo/OCR, catalogo, regole/LLM, final decision, report, storage | Mappa pipeline | Codice, docs processo | Spiega come funziona a livello executive |
| 5 | POC / Governance | La Final Decision rende ogni classificazione conservativa, motivata e auditabile | Baseline deterministica, policy LLM, rami accettati/bloccati, decision authority, warning e suggestion | Flow decisionale, non testo | `final_decision.py`, extraction-process, final-decision.mmd, test_llm | Nuova slide richiesta; spiega il gate decisionale |
| 6 | AS IS | La baseline mostra risultati concreti e aree precise di tuning | 96 run; 69 classified; 12 uncertain; 15 unknown; 84 con date; facts 0 | Dashboard KPI | DB aggregato | Non chiamarla accuratezza |
| 7 | AS IS | I limiti della POC definiscono il perimetro R&D | Single PDF, no compliance, no fascicolo, facts da estendere, storage POC | Matrice "oggi / gap / lavoro R&D" | AGENTS, docs processo | Gap come controllo investimento |
| 8 | TO BE | L'evoluzione e' trasformare la POC in un core governato e integrabile | POC extraction, core governato, governance/API readiness | Architettura 3 layer tecnica/business | Dossier + utente | Focus sul percorso evolutivo |
| 9 | TO BE | I business case cliente applicano regole e workflow sopra il core | Cantieri Protetti e Guber usano layer specifici: fascicoli, scadenze, compliance, workflow | Stack: core comune + layer cliente | Dossier + utente | Citazione esplicita confermata |
| 10 | Roadmap evolutiva | La roadmap spiega come la POC diventa core e poi business case cliente | R0 baseline, R1 MVP core, R2 feedback/KPI, R3 core governato, R4 business case cliente | Roadmap evolutiva / capability ladder | Stima delivery | Strategia, non Gantt |
| 11 | Piano attuativo | Il macropiano traduce la roadmap in fasi attuabili e range stimati | Studio, Realizzazione, A regime; range mese; milestone/release | Gantt macro ispirato a `../../docs/gantt.pdf` | Stima delivery + `../../docs/gantt.pdf` | Non e' WBS |
| 12 | Team / Governance | Il piano richiede competenze software, AI/OCR, dominio e privacy | Delivery lead, backend, AI/OCR, SME, QA, DevOps/security, governance privacy | Role map / swimlane competenze | Stima delivery | Nessun commitment di staffing |
| 13 | Economics | Gli economics restano driver per decidere l'investimento R&D | Cost driver, benefit driver, dati necessari per futuri business case | Tabella driver + box dati necessari | Dossier + utente | Nessun prezzo |
| 14 | Decisioni | Le decisioni chiave sono MVP R&D, KPI, owner e use case prioritari | Owner, document types, KPI, policy, target deploy, use case Cantieri/Guber | Checklist decisionale | Dossier + utente | Gate per approvare next step |

## Slide Drafts

### 1. TXT Novigo Document Intelligence Core

- **Key message:** dalla POC Cantieri Protetti AI a una capability replicabile per futuri business case cliente.
- **Body:** nome progetto R&D, audience CEO/CTO, data, livello di riservatezza.
- **Visual suggestion:** copertina sobria TXT/Novigo, titolo forte, sottotitolo breve.
- **Decisione recepita:** nome definitivo in copertina `TXT Novigo Document Intelligence Core`.
- **Source basis:** dossier + chiarimento utente.

### 2. Contesto, esigenza e obiettivi chiariscono perche' serve un core R&D

- **Contesto:** documenti di cantiere, sicurezza, personale e adempimenti aziendali sono eterogenei, spesso non strutturati e in parte scansionati.
- **Esigenza:** ridurre manualita', aumentare controllo e rendere verificabili evidenze e decisioni.
- **Obiettivi:** disegnare un Document Intelligence Core riusabile, governato e applicabile a casi come Cantieri Protetti e Guber.
- **Visual suggestion:** layout `Contesto / Esigenza / Obiettivi` con colonna laterale e blocchi numerati, coerente con `../visual-references/cantieri-protetti-02`.
- **Source basis:** AGENTS e CONTEXT del repo target.

### 3. La POC trasforma PDF eterogenei in esiti tracciabili

- Prende PDF di cantiere, sicurezza, personale e adempimenti, anche scansionati.
- Produce classificazione, date, evidenze, confidenza, diagnostica e run.
- Rende visibile cosa e' stato riconosciuto, cosa resta incerto e dove serve tuning.
- Il valore nasce dalla tracciabilita' dell'esito, non solo dall'automazione della lettura.
- **Visual suggestion:** flusso "PDF -> classificazione -> date/evidenze -> run/report".
- **Source basis:** README, schemas, extraction-process, chiarimento utente.

### 4. La POC funziona come pipeline riusabile, non come script isolato

- Testo/OCR gestiscono documenti nativi e scansioni.
- Catalogo, regole e policy LLM governano classificazione e casi incerti.
- La final decision e' il gate di controllo; la logica completa viene spiegata nella slide successiva.
- Report e storage permettono baseline, diagnostica e tuning progressivo.
- **Visual suggestion:** mappa pipeline Input / Extraction / Decision / Output / Persistenza.
- **Source basis:** README, api.py, cli.py, pipeline.py, ADR.

### 5. La Final Decision rende ogni classificazione conservativa, motivata e auditabile

- La POC crea prima una decisione deterministica da catalogo YAML: candidati, soglie, confidenza ed evidenze.
- La policy LLM decide se verificare: `disabled` salta il passaggio; `always`, `on_uncertain` e `on_ocr` lo attivano nei casi previsti.
- Il LLM puo' confermare la regola, scegliere un candidato gia' emerso dalle regole o proporre `unknown`.
- Se propone un tipo fuori catalogo, un tipo non candidato, una categoria incoerente o una confidenza sotto soglia, la proposta resta suggestion non accettata.
- L'output conserva `decision_authority`, motivazione, evidenze, rejected candidates, warning e suggestion: la decisione resta spiegabile.
- **Visual suggestion:** flow orizzontale: baseline deterministica -> policy LLM -> gate di accettazione -> final decision / suggestion bloccata.
- **Source basis:** `final_decision.py`, `docs/extraction-process.md`, `docs/diagrams/final-decision.mmd`, `tests/test_llm.py`, `CONTEXT.md`.

### 6. La baseline mostra risultati concreti e aree precise di tuning

- 96 run totali registrate su 68 documenti distinti.
- 95/96 run hanno testo estratto; 84/96 contengono date estratte.
- 69 run classificate; 12 uncertain e 15 unknown.
- 1.140 date estratte; facts strutturati ancora a zero.
- 125 warning di testo insufficiente indicano OCR/qualita' scansioni come driver di tuning.
- **Visual suggestion:** dashboard executive con KPI grandi e box "metrica operativa, non accuratezza certificata".
- **Source basis:** query aggregate su `db/extractions.sqlite`.

### 7. I limiti della POC definiscono il perimetro R&D

- La POC tratta un PDF alla volta, non un fascicolo completo.
- Non esegue compliance check ne' calcola scadenze normative derivate.
- I facts sono previsti ma non ancora valorizzati nella baseline.
- Persistenza e osservabilita' sono adeguate alla POC, non ancora a produzione.
- **Visual suggestion:** matrice "oggi / gap / lavoro R&D".
- **Source basis:** AGENTS, extraction-process, DB aggregato.

### 8. L'evoluzione e' trasformare la POC in un core governato e integrabile

- **POC Extraction:** PDF, OCR/testo, classificazione, date, evidenze e run.
- **Core governato:** facts, KPI, feedback, privacy, audit e API readiness.
- **Governance:** retention, osservabilita', policy LLM e deployment target.
- Il passaggio chiave e' trasformare output tecnici tracciabili in una capability governata per processi cliente.
- **Visual suggestion:** architettura a 3 layer con core al centro.
- **Source basis:** dossier + chiarimento utente.

### 9. I business case cliente applicano regole e workflow sopra il core

- Il core comune evita di ricostruire ogni volta la stessa capability di estrazione.
- Ogni business case cliente aggiunge regole, fascicoli, scadenze, compliance e workflow specifici.
- Cantieri Protetti e Guber sono citati esplicitamente come use case cliente, non come scope gia' contrattualizzato.
- Questo mantiene il progetto R&D distinto da future offerte cliente.
- **Visual suggestion:** stack con core comune sotto 2-3 layer cliente.
- **Source basis:** chiarimento utente.

### 10. La roadmap spiega come la POC diventa core e poi business case cliente

- **R0 - Baseline validata:** rendere visibili risultati, limiti e KPI operativi.
- **R1 - MVP core:** portare la POC a primo servizio controllabile su documenti prioritari.
- **R2 - Feedback/KPI:** introdurre label, report e tuning per miglioramento misurabile.
- **R3 - Core governato:** consolidare privacy, storage, osservabilita', audit e API readiness.
- **R4 - Business case cliente:** aggiungere fascicoli, scadenze, workflow e integrazioni solo dopo approvazione.
- **Visual suggestion:** roadmap evolutiva / capability ladder, non Gantt; mettere in evidenza capability abilitate, valore e gate.
- **Source basis:** software delivery estimate nel dossier.

### 11. Il macropiano traduce la roadmap in fasi attuabili e range stimati

- **Studio:** avvio, perimetro, KPI target e baseline operativa; indicativamente Mese 1.
- **Realizzazione:** MVP core, feedback/KPI, hardening e release core replicabile; indicativamente Mese 2-6.
- **A regime:** business case cliente foundation e maintenance/miglioramento continuo; indicativamente Mese 7-n.
- **Milestone/release:** baseline validata, Release R1 MVP core, ripianificazione business case, Release R2 core replicabile.
- **Nota:** tempistiche indicative; piano definitivo da consolidare all'avvio della fase di sviluppo.
- **Visual suggestion:** Gantt macro executive ispirato a `../../docs/gantt.pdf`, con lane `Studio / Realizzazione / A regime`, range per mese, milestone e release.
- **Source basis:** macro project plan nel dossier + `../../docs/gantt.pdf`.

### 12. Il piano richiede competenze software, AI/OCR, dominio e privacy

- Delivery owner per scope, KPI, rischi e stakeholder.
- Backend e solution architecture per API, storage, hardening e integrazioni future.
- AI/OCR engineering per tuning, facts, evaluation e casi uncertain/unknown.
- SME e QA per label, ground truth, test e criteri di accettazione.
- DevOps/security/privacy per deployment target, retention, audit e osservabilita'.
- **Visual suggestion:** mappa competenze per fase o role chips.
- **Source basis:** effort estimate nel dossier.

### 13. Gli economics restano driver per decidere l'investimento R&D

- Costi one-off: sviluppo API, facts, storage, hardening, eventuale UI cliente.
- Costi operativi: OCR, LLM verification, storage documenti, monitoraggio.
- Benefici potenziali: riduzione pre-analisi manuale, tracciabilita', riuso del core, base dati per futuri business case.
- Dati mancanti per business case cliente: volumi, baseline manuale, tariffe, SLA, retention e policy LLM.
- **Visual suggestion:** tabella driver economics + box "dati necessari per business case cliente".
- **Source basis:** economics drivers del dossier + chiarimento utente.

### 14. Le decisioni chiave sono MVP R&D, KPI, owner e use case prioritari

- Nominare owner del progetto R&D.
- Scegliere document types prioritari per MVP core.
- Definire KPI: accuratezza validata, tempi, copertura e riduzione effort manuale.
- Chiarire policy privacy, retention e uso LLM.
- Prioritizzare use case cliente: Cantieri Protetti, Guber o altri candidati.
- **Visual suggestion:** checklist decisionale / next steps.
- **Source basis:** chiarimenti utente + domande residue del dossier.

## Compression Notes

| Tecnico | C-level |
|---|---|
| OCR selettivo | Lettura automatica anche di PDF scansionati |
| Rule-based baseline | Baseline auditabile e misurabile |
| Configuration Catalog YAML | Regole configurabili e versionate |
| LLM verification/adjudication | Verifica intelligente dei casi incerti o conflittuali |
| Final Decision | Esito tracciabile della classificazione |
| SQLite/filesystem | Storico POC delle run e delle evidenze |
| 69 classified / 12 uncertain / 15 unknown | Baseline operativa per decidere dove investire nel tuning |
| Facts a zero | Gap funzionale esplicito per il prossimo rilascio |
| Single PDF scope | Primo nucleo controllato, da riusare nei business case cliente |

## CEO Readiness Check

- **No ripetizioni:** ogni slide ha un ruolo distinto nella sequenza POC, governance, baseline, TO BE, piano, economics e decisioni.
- **Risultati visibili:** slide 6 mostra numeri reali e limiti.
- **Governance tecnica leggibile:** slide 5 mostra la Final Decision come gate visuale e non come dettaglio implementativo testuale.
- **Sizing:** slide 11 include range e fasi; slide 12 esplicita competenze senza pricing.
- **Economics:** slide 13 separa driver, benefici e dati mancanti, senza prezzo.
- **Decisioni:** slide 14 porta owner, KPI e use case prioritari al tavolo CEO/CTO.
- **Contesto/esigenza/obiettivi:** slide 2 esplicita la sezione cardine richiesta dai reference.
- **POC narrative bridge:** slide 3-5 spiegano cosa fa la POC, come funziona, cosa produce e come decide; slide 7-8 chiariscono limiti ed evoluzione.
- **Tecnico tradotto:** dettagli tecnici spostati in notes o convertiti in impatto business.

## Decisioni Recepiti Prima Del PPTX

1. Nome in copertina: `TXT Novigo Document Intelligence Core`.
2. Citare esplicitamente `Cantieri Protetti` e `Guber`.
