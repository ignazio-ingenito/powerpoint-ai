# Data Pipeline Blueprint - Source Inventory

## Scope

Prima raccolta materiali per una presentazione sulla blueprint di data pipeline riusabile per Kiron CDG, Internal CDG e ProSIGNAL.

Questa inventory non e' ancora una storyline e non contiene claim commerciali definitivi.

## Materiali Raccolti

| Fonte | Tipo | Path locale nella cartella progetto | Cosa contiene | Autorita' | Note |
|---|---|---|---|---|---|
| `cdg-data-pipeline` | Repository software | `source-materials/cdg-data-pipeline-repo/` | Pipeline Jira/Tempo/Excel su MariaDB con Dagster, dlt, Metabase, NocoDB e target dbt | Alta per AS IS tecnico CDG | Repo sorgente locale sporco: usato in sola lettura |
| `cdg-data-pipeline/docs/architecture/data-layer-architecture.md` | Documento architetturale | `source-materials/cdg-data-pipeline-repo/docs/architecture/data-layer-architecture.md` | Layer `raw/ref/stg/mart`, separazione ingestion/transform/business/BI | Alta | Base per blueprint architetturale |
| `cdg-data-pipeline/docs/specs/jira-tempo-pipeline.md` | Specifica funzionale/tecnica | `source-materials/cdg-data-pipeline-repo/docs/specs/jira-tempo-pipeline.md` | Logica Jira -> Tempo, dynamic field discovery, JQL controllata, responsabilita' dlt/dbt | Alta | Base per pattern ingestion API e mart |
| `cdg-data-pipeline/docs/status/refactor-implementation-status.md` | Stato implementativo | `source-materials/cdg-data-pipeline-repo/docs/status/refactor-implementation-status.md` | Completato, backlog, prossimi step e configurazione rilevante | Alta ma temporale | Da riverificare prima di usarlo come stato aggiornato |
| `cdg-data-pipeline/dagster/` | Codice orchestrazione/ingestion | `source-materials/cdg-data-pipeline-repo/dagster/` | Job Dagster, ingestion Jira/Tempo/Excel, mapping dinamici | Alta per capability corrente | Non ancora analizzato riga per riga |
| `cdg-data-pipeline/init/` | SQL schema/stg/mart | `source-materials/cdg-data-pipeline-repo/init/` | Schema `ref_*`, view `stg_jira_issues`, mart `mart_fact_issue_accounts` | Alta per data model corrente | Utile per derivare pattern raw-to-mart |
| `cdg-data-pipeline/input/config/` | Mapping YAML | `source-materials/cdg-data-pipeline-repo/input/config/` | Mapping Excel/reference table: account, team, KPI, WBS, organizzazione, ecc. | Alta per processo CDG | Non copiare valori in slide senza controllo confidenzialita' |
| `cdg-data-pipeline-docs` | Materiali storici/funzionali | `source-materials/cdg-data-pipeline-docs/` | Analisi funzionale, project plan, campi output/tabelle, XMind, deck process reengineering | Media/alta per contesto legacy | Da ispezionare con conversione mirata nei prossimi step |
| `cdg-data-pipeline-docs/v2/Analisi funzionale processi CDG.docx` | Analisi funzionale Internal CDG | `source-materials/cdg-data-pipeline-docs/v2/Analisi funzionale processi CDG.docx` | Processi actual/forecast, input Jira/Tempo/SAP/CDG app, tabelle guida, output P1-P6 | Alta per Internal CDG | Analizzato in `drafts/04-internal-cdg-analysis.md` |
| `cdg-data-pipeline-docs/v2/*.xlsx` | Dizionari e sequenze operative Internal CDG | `source-materials/cdg-data-pipeline-docs/v2/` | Sequenza file, campi output, campi tabelle guida, project plan | Alta per processi/output | Analizzati via estrazione XML, non convertiti in derived source |
| `cdg-data-pipeline-docs/v2/*.xmind` | Mappe processo Internal CDG | `source-materials/cdg-data-pipeline-docs/v2/` | Processi P1-P6, reengineering, economics, integrazione ore/economics | Alta per TO BE e piano | Analizzati via `content.json` |
| `cdg-kiron` | Analisi funzionale, dizionari e piano Kiron CDG | `source-materials/cdg-kiron/` | Analisi funzionale Kiron CDG, campi input, campi output, tabelle guida/regole, struttura Jira, piano di lavoro | Alta per Kiron CDG | Analizzato in `drafts/13-kiron-cdg-analysis.md` |
| `tools` | Materiali di piano e supporto | `source-materials/cdg-tools/` | Project plan CDG, output Gantt, script xls2gantt, confronto Rundeck/Dagster | Media/alta per piano e scelta orchestratore | Copia selettiva; `README.md` vuoto non copiato |
| Obsidian TXT Novigo - CDG | Appunti operativi | `source-materials/obsidian-txt-novigo/CDG/` | Processo estrazioni Jira/Tempo/Excel/gestionali, campi Jira, task infra, note preparazione slide | Media/alta per AS IS operativo | Fonte appunti; da validare prima di usare in slide formali |
| Obsidian TXT Novigo - ProSignal | Appunti di analisi aggiornati nel vault | `source-materials/obsidian-txt-novigo/ProSignal/` | File fixed-column, grandi volumi, controlli, output regolamentari, retention, requisiti editor/testo, piano ripresa contatto/formazione | Media/alta per use case candidato | Materiali trovati nel vault indicato dall'utente; il contenuto funzionale storico dichiara comunque analisi da riconsiderare |
| Obsidian TXT Novigo - context | Appunti trasversali | `source-materials/obsidian-txt-novigo/context/` | Spunti AWS Summit, TODO Operations, nota DevOPS con riferimento Kiron | Media/bassa | Utile per principi architetturali e lead; non fonte funzionale primaria |
| Chat/memorie locali Codex | Evidenze operative e lead di materiali | `drafts/02-chat-memory-findings.md` | Pattern raw/stg/mart, metadata-driven ingestion, job modes, lead su ProSignal/CDG nel vault TXT Novigo | Media; da riverificare su fonti primarie | Utile per guidare la prossima ricerca e la narrativa, non come fonte finale autonoma |

## Evidenze Iniziali

- **Fatto confermato:** il progetto CDG integra Jira, Tempo e file Excel in MariaDB, con orchestrazione Dagster.
- **Fatto confermato:** la documentazione descrive una separazione a layer `raw_`, `ref_`, `stg_`, `mart_`.
- **Fatto confermato:** dlt e' responsabile dell'ingestion/API verso `raw`; dbt e' il target architetturale per trasformazioni, join, controlli e mart.
- **Fatto confermato:** Metabase consuma principalmente il layer `mart`; NocoDB supporta mapping manuali/reference table.
- **Fatto confermato:** esistono job distinti per ingestion Jira, Tempo, Jira+Tempo, refresh SQL, mart Jira/Tempo, ingestion Excel singola e ingestion Excel completa.
- **Fatto confermato:** in `../tools` esiste un piano CDG convertito in Gantt con fasi: avvio/perimetro, assessment AS-IS, disegno TO-BE, setup ambienti, normalizzazione, elaborazioni, dashboard/output, test/parallel run, go-live/hypercare, evolutive opzionali.
- **Fatto confermato:** `cdg-data-pipeline-docs` contiene una vera analisi Internal CDG: processi actual/forecast, input Jira/Tempo/SAP/CDG app, tabelle guida, output P1-P6 e piano di reengineering.
- **Fatto confermato:** Internal CDG produce sei output principali: Tabella A Mensile Actual, Tabella A Inframensile Actual, Tabella Linked Issue Actual, Economic plus Actual, Ore SAP per integrazione Economics, Storico forecast completo.
- **Fatto confermato:** `source-materials/cdg-kiron/` contiene materiale specifico Kiron CDG: analisi funzionale, dizionari input/output e regole/tabelle. Kiron non va piu' trattato come caso solo ipotetico.
- **Fatto confermato:** Kiron CDG copre Actual mensile e Forecast periodico su dimensioni Periodo, Prodotto, Rete e Istituto, con fonti Campus, Campus 2.0 e Zucchetti Infinity.
- **Fatto confermato:** gli output Kiron documentati includono base dati Actual gestionale, base dati Actual e base dati Forecast.
- **Fatto confermato:** sono disponibili anche una struttura Jira di esempio e un piano di lavoro Kiron con fasi AFU, VAL, ATE, ESE, TEST, RIL e UAT. I valori di effort presenti nel piano non vanno usati come commitment senza validazione.
- **Fatto confermato:** gli appunti Obsidian CDG descrivono un AS IS con estrazioni Jira, Tempo, organico, WBS e dati gestionali SharePoint, oltre a task infra su token API Jira, DB per Power BI e macchina Docker.
- **Fatto confermato:** gli appunti ProSignal descrivono file testuali posizionali/fixed-column, anche di grandi dimensioni, con controlli, aggregazioni, output per segnalazioni di vigilanza e necessita' di aprire/modificare file in modalita' testo/colonne.
- **Fatto confermato:** per ProSignal la prima fase ipotizzata include upload manuale, controlli su header/tail dove disponibili, controlli di scostamento andamentale e retention piu' orientata agli output che agli input.
- **Fatto confermato:** nel vault indicato dall'utente sono presenti tre note ProSignal (`ProSignal.md`, `2026-05-25.md`, `2026-06-23.md`), gia' copiate in `source-materials/obsidian-txt-novigo/ProSignal/`. La copia locale mantiene redatti i link SharePoint presenti nell'appunto originale.
- **Fatto confermato:** un appunto AWS Summit suggerisce, per progetti come ProSignal, di evitare soluzioni troppo applicative e usare storage scalabile, processing asincrono, audit, monitoraggio e qualita' del dato.
- **Fatto storico superato:** prima dell'arrivo di `source-materials/cdg-kiron/`, Kiron compariva solo come riferimento debole; la documentazione specifica e' ora disponibile.
- **Inferenza ragionata:** la blueprint riusabile puo' essere organizzata intorno a pattern: sorgenti, ingestion, raw/ref, staging, mart, BI, governance mapping, orchestrazione, osservabilita'.
- **Inferenza ragionata:** Internal CDG e' il caso sorgente principale per la blueprint; ProSignal e' il caso di stress test su file-processing/regulatory-control con volumi e tracciati variabili.
- **Evidenza da chat/memoria confermata da file:** ProSignal e CDG risultano presenti nel vault Obsidian TXT Novigo e i markdown pertinenti sono stati copiati in `source-materials/obsidian-txt-novigo/`.
- **Evidenza da chat/memoria:** le conversazioni precedenti su CDG rafforzano i pattern `raw_*` source-faithful, `stg_*` come livello di pulizia semantica e `mart_*` come livello BI-ready.

## Materiali Non Copiati

- `.env` e segreti runtime.
- `.git/` e cache.
- Output live, log runtime e dati estratti da database.
- File Excel operativi del repo `cdg-data-pipeline/input/xls/`: non copiati in questa prima passata per evitare di portare dentro dati potenzialmente sensibili senza selezione.
- Materiali `cantieri-protetti-ai`: trovati dalla ricerca su "pipeline", ma non pertinenti alla blueprint data pipeline CDG.
- Materiali `ai-orchestrator`: potenzialmente utili solo come reference di deck/prompt o orchestrazione AI, non copiati per evitare rumore.
- Materiali `guber`, `guber-xlsx-import`, `os-ao-report`, `polaris`, `recupero`, `tfm-aws-agos-ivass`: trovati nella ricerca estesa ma non copiati perche' non direttamente legati a CDG/Kiron/ProSIGNAL data pipeline.

## Materiali Da Recuperare Dopo

- Confronto puntuale tra documentazione Internal CDG e implementazione corrente del repo `cdg-data-pipeline`.
- Kiron: nessun altro chiarimento atteso dall'utente ora; eventuali regole ancora marcate come da definire/open point nel materiale sorgente vanno dichiarate come rischi/assunzioni.
- ProSIGNAL: nessun altro esempio disponibile ora; esempi file, tracciati, output attesi, allegati SharePoint autorizzati, limiti OutSystems su file grandi e vincoli tecnici aggiornati restano materiali mancanti da non inventare.
- Eventuali deck o appunti gia' esistenti su CDG/Kiron/ProSIGNAL.
- Screenshot o export Metabase/NocoDB/Dagster autorizzati, se servono come evidenza visuale.
- Eventuali materiali in repository o cartelle con naming specifico Kiron: la ricerca in `../` e nel vault Obsidian TXT Novigo non ha trovato cartelle o file dedicati con quel nome.
- Eventuali allegati SharePoint citati dagli appunti Obsidian: non scaricati in questa passata.

## Domande Aperte Prima Della Storyline

Queste domande sono state in larga parte risolte nella direzione successiva:

- il deck serve a presentare due ipotesi al CEO/Gianfranco, CTO e Tech Committee;
- il deck resta neutrale e abilita una discussione, senza chiudere la scelta;
- ProSIGNAL e Kiron hanno priorita' rispetto al CDG interno;
- Kiron non ha altri chiarimenti disponibili ora;
- ProSIGNAL non ha altri esempi disponibili ora.
4. Vogliamo includere effort/economics o limitarci a principi, roadmap e capability?
5. Possiamo usare contenuti del deck `CDG Process Reengineering.pptx` come reference/contesto, o solo come materiale interno da sintetizzare?
