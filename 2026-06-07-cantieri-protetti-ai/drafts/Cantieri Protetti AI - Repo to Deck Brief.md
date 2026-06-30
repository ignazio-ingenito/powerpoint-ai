# Cantieri Protetti AI - Repo To Deck Brief

Status: Rigenerato dopo aggiornamento pipeline
Fonte principale: `/home/iingenito/projects/txt/cantieri-protetti-ai`
Creato: 2026-06-05
Output atteso: dossier grounded per proposta progetto R&D propedeutica a futuri business case cliente, non ancora deck PowerPoint

## Repository Analizzato

- **REPO_PATH_O_URL:** `/home/iingenito/projects/txt/cantieri-protetti-ai`
- **NOME_PROGETTO:** Cantieri Protetti AI / TXT Document AI Extraction
- **CLIENTE_O_SPONSOR:** **Fatto confermato dall'utente** - progetto R&D interno con possibili use case futuri per clienti come Cantieri Protetti e Guber
- **TIPO_DECK:** **Fatto confermato dall'utente** - proposta progetto R&D per futuro business case
- **AUDIENCE:** **Fatto confermato dall'utente** - CEO e CTO
- **OBIETTIVO_BUSINESS:** **Fatto confermato dall'utente** - disegnare una soluzione core replicabile su futuri business case cliente
- **NOME_DECK:** **Fatto confermato dall'utente** - `TXT Novigo Document Intelligence Core`
- **USE_CASE_DA_CITARE:** **Fatto confermato dall'utente** - `Cantieri Protetti` e `Guber`
- **VINCOLI_NOTI:** privacy su dati personali/sanitari/aziendali; POC single-PDF; no compliance check; no fascicolo; no calcolo scadenze normative derivate

## 1. Executive Summary

- **Fatto confermato:** il repository implementa una POC FastAPI/CLI per Document Extraction da PDF relativi a cantieri, sicurezza, personale e adempimenti aziendali.
- **Fatto confermato:** l'endpoint target e' `POST /pdf/extract`; accetta un PDF e restituisce payload strutturato con classificazione, date, facts previsti da schema, evidenze, confidenza, diagnostica e run persistita quando richiesto.
- **Fatto confermato:** API e CLI condividono `ExtractionPipeline.extract`; questo rende la POC gia' impostata come nucleo riusabile, non come script di discovery isolato.
- **Fatto confermato:** la pipeline usa testo nativo, OCR selettivo, classificazione rule-based conservativa, catalogo YAML, LLM verification/adjudication configurabile e persistenza SQLite/filesystem.
- **Fatto confermato:** il database locale contiene una baseline operativa di 96 run: 69 classified, 12 uncertain, 15 unknown; 95/96 run hanno testo estratto e 84/96 contengono date.
- **Fatto confermato:** la baseline e' metrica di esito pipeline, non accuratezza validata: i PDF campione sono regression/discovery fixture, non ground truth forte.
- **Fatto confermato:** `extraction.facts` esiste nello schema ma oggi risulta non popolato nella baseline aggregata.
- **Fatto confermato dall'utente:** la baseline puo' essere inclusa, ma deve restare marcata come metrica operativa e non come accuratezza validata.
- **Fatto confermato dall'utente:** gli economics devono restare solo driver, senza prezzo.
- **Inferenza ragionata:** il valore R&D e' progettare una capability core di Document Intelligence riusabile, validabile su casi come Cantieri Protetti e poi replicabile su business case cliente.
- **Inferenza ragionata:** l'evoluzione naturale e' un percorso per fasi: core service, knowledge store, poi layer applicativo per business case cliente.
- **Stima da validare:** il percorso R&D richiede 6-10 settimane per MVP core, 12-20 settimane per core replicabile con metriche e feedback, 24-36+ settimane se include applicazione cliente completa.

## 2. Inventario Fonti

| Fonte | Tipo | Cosa contiene | Autorita | Note |
|---|---|---|---|---|
| `AGENTS.md` target | Policy repo | Obiettivo POC, scope, API contract, privacy, OCR/LLM, catalogo, classificazione | Alta | Fonte primaria per intent e vincoli |
| `README.md` target | Uso tecnico | Docker, API, CLI, report-summary, smoke test | Alta | Conferma operativita' e comandi |
| `CONTEXT.md` target | Glossario dominio | Document Extraction, Final Decision, Batch Summary Report, Business Application | Alta | Da usare per linguaggio deck |
| `docs/extraction-process.md` | Processo/architettura | Mappa sistema, flusso, final decision, persistenza, payload, punti aperti | Alta | Fonte piu' utile per AS IS e TO BE |
| `docs/adr/*.md` target | Decisioni | LLM, OCR sostituibile, privacy, SQLite, fixture set | Alta | Razionale architetturale |
| `pyproject.toml` | Manifest | Python/FastAPI/PyMuPDF/Typer/SQLAlchemy/ReportLab | Media | Conferma stack |
| `src/txt_doc_ai_extraction/*.py` | Codice | API, CLI, pipeline, storage, catalogo, final decision | Alta | Letti moduli principali |
| `config/catalog.yaml` | Configurazione dominio | Tassonomia, soglie, keyword, date noise policy | Alta | Mostra copertura e configurabilita' |
| `db/extractions.sqlite` | Baseline POC | Aggregati su run, classificazioni, decisioni, diagnostica, date/facts | Media | Letti solo conteggi aggregati |
| `db/reports/extraction-summary.pdf` | Report aggregato | Esistenza di report PDF prodotto dalla CLI | Media | Non letto nel contenuto |
| `tests/*.py` | Test | Copertura su catalogo, classificazione, OCR, pipeline, privacy, storage | Media | Inventariati, non letti integralmente |

### File Non Letti O Non Ispezionati

- **PDF sotto `docs/`:** non ispezionati nel contenuto per evitare esposizione di dati potenzialmente sensibili.
- **Payload/evidenze nel DB:** non letti; sono stati usati solo aggregati statistici.
- **Artifact debug:** non letti perche' non necessari al dossier commerciale.
- **Test suite completa:** non letta integralmente; usata come indicatore di aree coperte.

## 3. Contesto Ed Esigenza / Obiettivi

### Fatti Confermati

- Il dominio riguarda documenti PDF di cantiere, sicurezza, personale e adempimenti aziendali.
- Le macro-categorie gestite includono identita, amministrativi azienda, contratti e polizze, piani e valutazioni sicurezza, nomine ruoli sicurezza, formazione, sorveglianza sanitaria, DPI e abilitazioni attrezzature.
- La POC opera su un singolo PDF alla volta e separa Document Extraction da Compliance Check e Business Application.
- Il payload deve essere strutturato, auditabile e privacy-aware.
- I risultati vengono persistiti in SQLite e originali opzionalmente su filesystem, con deduplica per file content ID.

### Inferenze Ragionate

- Il problema operativo e' la gestione manuale di PDF eterogenei, spesso scansionati o semi-strutturati.
- Il bisogno non e' solo "leggere PDF", ma creare una base dati affidabile per tracciabilita', tuning, review e processi downstream.
- Il valore per CEO/CTO e' valutare un investimento R&D che possa diventare capability replicabile su piu' clienti, riducendo rischio tecnico prima di una proposta commerciale specifica.

### Obiettivi Impliciti Ragionevoli

- Ridurre tempi di pre-analisi e smistamento documentale.
- Rendere visibili evidenze, confidenza, diagnostica e decision authority.
- Creare metriche operative per tuning e prioritizzazione.
- Separare motore tecnico da regole business future.
- Abilitare un percorso PMO/prodotto dopo la POC.

### Stakeholder Probabili

- **Fatto confermato dall'utente:** audience primaria CEO e CTO.
- **Inferenza ragionata:** IT/digital owner responsabile di API, integrazioni, privacy e deployment.
- **Inferenza ragionata:** HSE/operations/back office documentale come SME e validatori.
- **Inferenza ragionata:** PMO o R&D owner per governare roadmap, KPI e riusabilita' della soluzione core.

## 4. AS IS

### Architettura Applicativa Confermata

- API FastAPI con `GET /health` e `POST /pdf/extract`.
- CLI Typer con `process-file`, `process-folder`, `report-summary`, `serve`.
- Core unico `ExtractionPipeline.extract` richiamabile da API e CLI.
- Componenti separati: `PdfEngine`, `OcrEngine`, `LlmClient`, classificazione, date extraction, final decision, storage.
- Configurazione via `Settings` e catalogo YAML versionato.
- Persistenza POC con SQLite `db/extractions.sqlite`, originali deduplicati su filesystem, artifact debug solo con `debug=true`.

### Pipeline Confermata

1. Lettura PDF e testo nativo.
2. OCR selettivo su pagine senza testo sufficiente.
3. Classificazione rule-based conservativa da Configuration Catalog.
4. Estrazione date e applicazione date noise policy per document type.
5. Final Decision deterministica.
6. LLM verification/adjudication secondo policy configurabile.
7. Persistenza run, payload, diagnostica e originale quando `persist=true`.
8. Report summary JSON/PDF con sole metriche aggregate.

### Logica Di Final Decision Confermata Dal Codice

- **Fatto confermato:** `build_deterministic_final_decision` crea sempre una decisione iniziale dalla classificazione rule-based, con `document_type`, `status`, `confidence`, `decision_authority`, reason, evidenze e rejected candidates.
- **Fatto confermato:** `apply_llm_final_decision` applica l'output LLM solo se disponibile e conforme allo schema strutturato; in assenza di output o di decisione classificativa valida, la decisione deterministica resta l'autorita'.
- **Fatto confermato:** il LLM puo' confermare una baseline classificata, producendo `rule_confirmed_by_llm`.
- **Fatto confermato:** il LLM puo' produrre `llm_adjudication` solo in casi conservativi: proposta `unknown`, oppure scelta di un document type gia' presente tra i candidati deterministici, coerente con il catalogo e sopra soglia quando lo status e' `classified`.
- **Fatto confermato:** se il LLM propone un tipo fuori catalogo, un tipo catalogato ma non candidato, una categoria incoerente o una confidenza sotto soglia, la proposta resta `llm_suggestion` non accettata e viene aggiunto un warning.
- **Fatto confermato:** i test coprono i casi principali: policy LLM disabilitata, conferma LLM, degradazione a `unknown`, scelta di candidato alternativo, suggestion fuori catalogo, mismatch di categoria e confidenza sotto soglia.
- **Lettura executive:** la Final Decision non e' una black box: e' un gate di governance che conserva autorita' decisionale, evidenze, motivazione e diagnostica. Questo merita una slide visuale dedicata nel deck.

### Baseline Operativa Disponibile

**Fonte:** query aggregate su `db/extractions.sqlite`, senza lettura di testo, evidenze, filename o PDF.

| Metrica | Valore | Lettura executive |
|---|---:|---|
| Run totali registrate | 96 | Esiste una base misurabile per tuning e decisioni |
| Documenti distinti registrati | 68 | Campione POC non banale, ma ancora non ground truth |
| Run completate | 47 | Quasi meta' chiude senza warning |
| Run completate con warning | 48 | I warning sono materiale utile per miglioramento |
| Run parziali | 1 | Il flusso quasi sempre arriva a risultato |
| Testo estratto | 95/96 | Primo step tecnico robusto sul campione |
| Classificazioni `classified` | 69/96, 71,9% | Base positiva da industrializzare |
| Classificazioni `uncertain` | 12/96, 12,5% | Casi candidati per LLM/review |
| Classificazioni `unknown` | 15/96, 15,6% | Area prioritaria per catalogo/OCR |
| Run con date estratte | 84/96 | Date extraction gia' utile su gran parte del campione |
| Date totali estratte | 1.140 | Potenziale per scadenze future nella Business Application |
| Facts estratti | 0 | Gap funzionale chiaro per il prossimo step |
| Decision authority | 96 deterministic_rule | La baseline misurata e' deterministica; LLM non risulta authority nella baseline |

### Breakdown Per Prioritizzazione

| Evidenza aggregata | Valore | Implicazione |
|---|---:|---|
| Tipi piu' riconosciuti | `durc` 11, `carta_identita` 9, `attestato_formazione` 8 | Buoni candidati per MVP dimostrabile |
| Weak category piu' stabile | `identita` 100%, `sorveglianza_sanitaria` 100%, `amministrativi_azienda` 92,6% | Famiglie su cui costruire quick win |
| Weak category fragile | `abilitazioni_attrezzature` 0%, `nomine_ruoli_sicurezza` 36,4% | Tuning prioritario prima di promessa commerciale |
| Warning piu' frequente | `page_insufficient_text` 125 | Qualita' scansioni/OCR e' driver di effort |
| Page limit OCR | 1 warning | Limiti tecnici gia' tracciati |

**Nota di qualita':** questi numeri descrivono esiti operativi della pipeline. Non misurano accuratezza rispetto a label umane. Per usarli in offerta servono Evaluation Label, SME review e criteri target.

### Punti Di Forza

- Core unico API/CLI, quindi meno duplicazione e migliore readiness evolutiva.
- Privacy e debug separati in modo esplicito.
- OCR e LLM modellati come componenti sostituibili.
- Catalogo YAML versionato con soglie, keyword e policy per date.
- Report batch aggregato gia' disponibile e coerente con uso discovery/tuning.
- ADR e documentazione processo gia' presenti.

### Criticita / Limiti Attuali

- **Fatto confermato:** scope POC limitato a singolo PDF, non fascicolo.
- **Fatto confermato:** nessun compliance check o calcolo scadenze normative derivate.
- **Fatto confermato:** facts previsti ma baseline a 0 facts.
- **Fatto confermato:** persistenza POC con `metadata.create_all()`, non migrazioni production-grade.
- **Fatto confermato:** sample PDF non sono training dataset ne' ground truth.
- **Inferenza ragionata:** passaggio a produzione richiede sicurezza, retention, audit, osservabilita', KPI validati e processo di feedback umano.
- **Inferenza ragionata:** i casi unknown/uncertain vanno trattati come punto di governo, non come errore da nascondere.

## 5. TO BE

### Strategia Proposta

**Fatto confermato dall'utente:** il progetto R&D ha il compito di disegnare una soluzione core replicabile su futuri business case cliente.

**Inferenza ragionata:** evolvere la POC in una capability a tre livelli:

1. **Reusable Document Intelligence Core**
   - API stabile per classificare PDF, estrarre date/facts, produrre evidenze, confidenza e diagnostica.
2. **Document Knowledge Store**
   - storico run, final decision, metriche, label SME, versioni catalogo, feedback e audit.
3. **Client Business Case Layer**
   - fascicoli, scadenze, completezza documentale, compliance, dashboard e workflow review.

### Componenti Da Mantenere

- `ExtractionPipeline` come core condiviso.
- Configuration Catalog versionato.
- Payload `poc-1` come base contrattuale da evolvere con governance.
- OCR sostituibile e LLM backend configurabile.
- CLI batch/report per regressione, discovery e tuning.

### Componenti Da Evolvere

- Facts strutturati oltre alle date.
- KPI di accuratezza con Evaluation Label e SME review.
- Human feedback loop e gestione manual_label.
- Migrazioni DB, retention, masking e audit.
- Osservabilita' e monitoraggio runtime.
- API production readiness: auth, limiti, error handling, contract review, SLA.
- Eventuale UI o applicazione cliente solo nei business case successivi.

### Roadmap Evolutiva

| Step evolutivo | Obiettivo strategico | Capability abilitate | Valore atteso | Prerequisiti / gate | Note e assunzioni |
|---|---|---|---|---|---|
| R0 - Baseline validata | Rendere la POC misurabile e discutibile con CEO/CTO | Report, KPI operativi, distinzione tra classificazione/uncertain/unknown | Visibilita' su risultati e limiti reali | Campione e run condivisi | Baseline operativa, non accuratezza certificata |
| R1 - MVP core extraction | Trasformare la POC in primo servizio controllabile | API/CLI robuste, catalogo mirato, facts minimi, evidenze | Primo nucleo riusabile di Document Intelligence | SME e KPI target | Scope ristretto a capability core |
| R2 - Feedback e metriche | Creare ciclo di miglioramento misurabile | Label manuali, report KPI, tuning catalogo/OCR, gestione uncertain/unknown | Miglioramento guidato da dati e review SME | Processo review | Accuratezza da validare su ground truth |
| R3 - Core governato | Portare il core verso uso operativo controllato | Privacy/storage, audit, osservabilita', API readiness | Capability integrabile e governabile | Policy cliente e target deploy | Cloud/on-prem da chiarire |
| R4 - Business case cliente | Applicare il core a use case cliente specifici | Fascicoli, scadenze, compliance, dashboard, workflow | Valore business su Cantieri Protetti, Guber o altro caso prioritario | Regole business e UX cliente definite | Fuori scope R&D core, da approvare |

## 6. Piano Di Lavoro

### Delivery Options

| Option | Positioning | Scope | Timeline range | Main trade-off |
|---|---|---|---:|---|
| MVP R&D / quick win | Validare una core capability misurabile su documenti prioritari | API/CLI, catalogo mirato, facts minimi, report, hardening base | 6-10 settimane | Velocita' alta, copertura limitata |
| Core replicabile | Costruire servizio riusabile e governabile | MVP + label, KPI, feedback, privacy/storage, observability | 12-20 settimane | Miglior equilibrio valore/rischio |
| Business case cliente | Applicare il core a un use case cliente | Estrazione + fascicolo + scadenze/compliance + UI + integrazioni | 24-36+ settimane | Valore maggiore, molte dipendenze cliente |

### Macro Project Plan

Le tempistiche sono indicative e costruite su esperienza TXT Novigo in progetti analoghi; il piano definitivo va consolidato all'avvio della fase di sviluppo.

| Lane/Fase | Macro-attività | Tipo | Inizio indicativo | Fine indicativa | Output / milestone | Dipendenze | Assunzioni |
|---|---|---|---:|---:|---|---|---|
| Studio | Avvio, perimetro e KPI target | Barra | Mese 1 | Mese 1 | Scope MVP, sponsor, criteri di successo | Sponsor/SME | Perimetro decidibile in workshop brevi |
| Studio | Baseline operativa validata | Milestone | Mese 1 | Mese 1 | Report baseline e distinzione tra metrica operativa e accuratezza validata | Campione e run disponibili | Si parte dalle 96 run gia' osservate |
| Realizzazione | MVP core extraction | Barra | Mese 2 | Mese 3 | API/CLI piu' robuste, document type prioritari, facts minimi | SME e KPI target | Nessun cambio radicale di architettura |
| Realizzazione | Release R1 - MVP core | Release | Mese 3 | Mese 3 | Primo servizio R&D controllabile | MVP core extraction | Scope limitato a capability core |
| Realizzazione | Feedback, KPI e tuning | Barra | Mese 3 | Mese 5 | Label SME, report KPI, tuning catalogo/OCR e gestione uncertain/unknown | Processo review SME | Label e criteri accettazione definiti |
| Realizzazione | Hardening e readiness | Barra | Mese 4 | Mese 6 | Privacy/storage, audit, osservabilita', API readiness | Policy cliente e target deploy | Cloud/on-prem da chiarire |
| Realizzazione | Ripianificazione business case cliente | Ripianificazione | Mese 6 | Mese 6 | Decisione su Cantieri Protetti, Guber o altro use case prioritario | KPI core e owner | Business case cliente non ancora contrattualizzato |
| Realizzazione | Release R2 - Core replicabile | Release | Mese 6 | Mese 6 | Capability core pronta per valutazione business case | Hardening e KPI | Validazione da completare con sponsor/SME |
| A regime | Business case cliente foundation | Barra | Mese 7 | Mese n | Fascicoli, scadenze, compliance, dashboard/workflow su use case approvato | Regole business/UX cliente | Fuori scope R&D core, da approvare |
| A regime | Application maintenance / miglioramento continuo | Run | Mese 7 | Mese n | Monitoraggio, tuning, backlog evolutivo | Deploy target e ownership | Da dimensionare dopo decisione di go-live |

## 7. Effort E Team Estimate

| Profilo | Coinvolgimento stimato | Fase | Note |
|---|---:|---|---|
| Delivery Lead / PM | 15-35 gg | Tutte | Governance, scope, stakeholder, rischi |
| Business Analyst / Domain SME | 15-45 gg | Assessment, labels, processi | Critico per KPI e ground truth |
| Solution Architect | 10-25 gg | Assessment, hardening, readiness | Confini servizio, deploy, security, storage |
| Backend Python Engineer | 45-100 gg | Stabilizzazione, facts, API, storage | Core principale e API sono Python |
| AI/OCR Engineer | 20-60 gg | OCR/LLM/facts/evaluation | Dipende da qualita' PDF e target accuratezza |
| QA/Test Engineer | 15-40 gg | Regressione, API, privacy | Aumenta con produzione e compliance |
| DevOps/Platform | 10-35 gg | Docker, deploy, observability | Dipende da cloud/on-prem |
| UX/Product Designer | 0-30 gg | Business case cliente | Necessario solo se si include UI |

**Stima da validare:** MVP R&D API/CLI: 2-4 FTE per 2-3 mesi. Core replicabile: 3-5 FTE per 3-5 mesi. Business case cliente con applicazione completa: team cross-funzionale per 6-9+ mesi.

### Driver Che Possono Cambiare Effort

- Numero di document types prioritari.
- Percentuale di PDF scansionati o rumorosi.
- Accuracy target per classificazione/date/facts.
- Necessita' LLM e scelta backend.
- Policy privacy/retention/audit.
- Presenza di UI e integrazioni cliente.
- Disponibilita' SME per label e validazione.

## 8. Benefici Attesi

| Beneficio | Meccanismo | Evidenza dal repo | Stima/guess | Come validarlo |
|---|---|---|---|---|
| Riduzione lavoro manuale | Classificazione e date automatiche | 69/96 classified; 84/96 con date | **Guess:** 30-60% su pre-analisi documenti ricorrenti | Time study manuale vs pipeline |
| Maggiore tracciabilita' | Evidenze, confidenza, final decision, diagnostica | Payload, storage, ADR privacy | **Inferenza:** audit piu' semplice | Review SME su campioni |
| Scalabilita' operativa | Batch CLI e API condividono core | `process-folder`, `report-summary` | **Guess:** batch ricorrenti senza lettura puntuale iniziale | Batch su set piu' ampio |
| Miglioramento continuo | Baseline, warning, catalogo, label future | 96 run e diagnostica OCR | **Fatto/inferenza:** tuning misurabile | KPI per release |
| Riduzione rischio tecnico | OCR/LLM sostituibili, catalogo versionato | ADR 0001/0002/0005 | **Inferenza:** minore lock-in | Test backend alternativi |
| Base per compliance futura | Date e final decision persistite | SQLite, payload, report | **Inferenza:** abilita fascicolo/scadenze in business case cliente | Prototipo su use case cliente |

## 9. Economics Drivers

Il repository non contiene tariffe, budget, prezzi o baseline manuale. Gli economics vanno quindi presentati come driver e ordini di grandezza, non come offerta.

| Voce | Tipo costo | Driver | Range/guess | Fonte o assunzione |
|---|---|---|---:|---|
| Sviluppo backend/API | One-off | Facts, API hardening, storage, test | Da effort delivery | Stima da validare |
| AI/OCR tuning | One-off + operativo | Unknown/uncertain, warning testo insufficiente, PDF scansionati | Variabile | 125 warning `page_insufficient_text` |
| LLM verification | Operativo variabile | Policy, modello, casi uncertain/OCR, volumi | Dipende da volumi | Backend configurabile |
| Storage e retention | Operativo + governance | Originali PDF, run, artifact, retention | Dipende da policy | SQLite/filesystem POC |
| Privacy/security hardening | One-off + governance | Dati personali/sanitari/aziendali | Medio/alto se produzione | ADR privacy |
| SME validation | One-off + ricorrente | Label, review, feedback | Dipende da campione | Necessaria per KPI |
| Applicazione cliente | One-off | UI, fascicoli, scadenze, workflow, integrazioni | Scope separato | Fuori scope R&D core |

### Dati Necessari Per Un Business Case Numerico

- Volumi documenti/mese e pagine medie.
- Tempo manuale attuale per documento/fascicolo.
- Costo medio profili coinvolti.
- Errori/ritardi con impatto economico o compliance.
- Accuracy minima accettabile e livello di review umana.
- Target deployment e policy LLM.

## 10. Rischi E Punti Aperti

| Categoria | Rischio | Impatto | Probabilita | Mitigazione | Input necessario |
|---|---|---|---|---|---|
| Tecnico | PDF scansionati/rumorosi riducono qualita' estrazione | Alto | Media/alta | OCR tuning, warning dashboard, review | Campione reale e KPI |
| Tecnico | Accuracy non ancora validata da ground truth | Alto | Alta | Evaluation Label, SME review | Processo label |
| Tecnico | Facts non implementati nella baseline | Medio/alto | Alta | Prioritizzare facts per document type | Set facts MVP |
| Dati/sicurezza | Dati sensibili in log/debug/artifact | Alto | Media | Retention, masking, debug controls | Policy cliente |
| Delivery | Scope creep verso compliance completa o progetto cliente prima del core | Alto | Alta | Separare core R&D da business case cliente | Decisione scope |
| Commerciale | Economics senza baseline manuale | Medio/alto | Alta | Time study e volumi | Sponsor/operations |
| Organizzativo | Risultati POC non resi visibili a stakeholder | Medio | Media | Dashboard KPI e narrative CEO | Owner comunicazione |
| Operativo | Manca owner continuativo del servizio | Medio/alto | Media | Modello governance e runbook | Owner/sponsor |
| Dipendenza esterna | LLM backend/provider da definire | Medio | Media | Backend configurabile, fallback policy | Scelta provider |

## 11. Storyline Deck Proposta

La struttura target e' una sola: **14 slide CEO/CTO**.

| # | Sezione | Titolo messaggio | Contenuto chiave | Fonte | Assunzioni |
|---|---|---|---|---|---|
| 1 | Copertina | TXT Novigo Document Intelligence Core | Titolo, sottotitolo, sponsor, data | Repo + utente | Nome confermato |
| 2 | Contesto / Esigenza / Obiettivi | Contesto, esigenza e obiettivi chiariscono perche' serve un core R&D | Documenti eterogenei, esigenza di controllo/tracciabilita', obiettivo di core riusabile | AGENTS/CONTEXT/reference.1 | Impatto operativo da quantificare |
| 3 | POC | La POC trasforma PDF eterogenei in esiti tracciabili | PDF -> classificazione -> date/evidenze -> run/report | README/docs processo | Riuso su business case cliente |
| 4 | POC | La POC funziona come pipeline riusabile, non come script isolato | Testo/OCR, catalogo, regole/LLM, final decision, report, storage | Codice/docs processo | Nessuna |
| 5 | POC / Governance | La Final Decision rende ogni classificazione conservativa, motivata e auditabile | Baseline deterministica, policy LLM, gate conservativo, suggestion non accettate, output auditabile | `final_decision.py`, extraction-process, tests | Slide flow visuale, non testo |
| 6 | AS IS | La baseline mostra risultati concreti e aree precise di tuning | 96 run, 69 classified, 12 uncertain, 15 unknown, 84 con date | DB aggregato | Non e' accuratezza validata |
| 7 | AS IS | I limiti sono chiari: singolo PDF, facts a zero, no fascicolo, no compliance | Gap funzionali e production readiness | AGENTS/docs processo/DB | Priorita' da validare |
| 8 | TO BE | L'evoluzione e' trasformare la POC in un core governato e integrabile | POC extraction, core governato, governance/API readiness | Repo + utente | Scope MVP da approvare |
| 9 | TO BE | I business case cliente applicano regole e workflow sopra il core | Layer cliente per Cantieri Protetti e Guber: fascicoli, scadenze, compliance e workflow | Repo + utente | Citazione esplicita confermata |
| 10 | Roadmap evolutiva | La roadmap spiega come la POC diventa core e poi business case cliente | Strategia R0-R4, capability e gate | Stima delivery | Timeline da validare |
| 11 | Piano attuativo | Il macropiano traduce la roadmap in fasi attuabili e range stimati | Gantt macro con Studio, Realizzazione, A regime | Stima delivery + `../../docs/gantt.pdf` | Non e' WBS |
| 12 | Team / governance | Il piano richiede competenze software, AI/OCR, dominio e privacy | Team mix e governance | Stima delivery | Staffing non vincolante |
| 13 | Economics | Gli economics restano driver per decidere l'investimento R&D | Driver costi, benefici, dati necessari | Repo + utente | Nessun prezzo |
| 14 | Decisioni | Le decisioni chiave sono MVP R&D, KPI, owner e use case prioritari | Decision asks e open point | Dossier + utente | Gate prima del PPTX |

## 12. Domande Da Porre Dopo La Prima Generazione PPTX

Nome e citazioni cliente sono stati confermati. Le domande seguenti restano utili per una revisione successiva o per una versione piu' impegnativa verso cliente, ma non bloccano la prima generazione PPTX.

### Da Validare Per Una Versione Successiva

1. Chi sara' owner/sponsor interno del progetto R&D?
2. Quali document types sono prioritari per MVP?
3. Quali KPI target vogliamo proporre: accuratezza, tempo elaborazione, riduzione effort, copertura documentale?

### Utili Ma Non Bloccanti Per Il Primo PPTX

1. Volumi attesi: PDF/mese, pagine medie, quota scansionati.
2. Target deployment: cloud, on-prem, container cliente, SaaS interno.
3. Necessita' UI o API-only nel primo step.
4. Sistemi da integrare: DMS, ERP, HSE, portale fornitori, workflow approvativo.
5. Policy di retention, masking, audit e uso LLM.

### Domande Per Economics E Benefici

1. Quanto tempo richiede oggi la verifica manuale di un documento/fascicolo?
2. Quali profili lavorano oggi sul processo e con quale costo medio?
3. Quali errori o ritardi generano rischio economico o compliance?
4. Quale livello di review umana resta necessario anche dopo automazione?
5. Esistono tariffe/profili da usare per valorizzare effort e range?

## CEO Readiness Applicata Al Dossier

- **Risultati visibili:** baseline 96 run, classificazioni, date, warning e facts a zero.
- **Sizing:** timeline e effort sono presenti come range da validare.
- **Benefici:** formulati come meccanismo + evidenza + validazione, non come promessa.
- **Decisioni:** MVP R&D, KPI, owner, deployment, policy privacy/LLM, business case cliente.
- **Tecnico -> business:** OCR, LLM, SQLite e catalogo sono tradotti in rischio, controllo, scalabilita' e economics.
