# ChatGPT Findings — Blueprint Data Pipeline 2026-06-30

> Origine: sintesi da memoria ChatGPT, Gmail disponibile nella sessione e riferimenti File Library emersi nelle conversazioni.  
> Validità: materiale preparatorio per storyline, da riverificare prima di una presentazione ufficiale.

## 1. Fatti confermati da file/documenti

### CDG / Internal CDG

- Esiste un assessment strutturato `CDG_Requirements_Gap_Assessment_v0.1.xlsx` con executive summary, registro fonti, processi P1-P6, requisiti, gap, domande, impatto stima, gate architetturali e piano workshop.
- L’assessment dice che la baseline non è pronta per congelare architettura o stima: scope, regole P4/P5, data contract, NFR e riuso multi-cliente non risultano chiusi.
- Processi CDG censiti: P1 Actual ore mensile; P2 Actual ore inframensile; P3 Linked issue / ore secondarie; P4 Economics plus Actual; P5 Ore SAP / integrazione economics; P6 Forecast.
- Fonti/logiche CDG citate: Jira/Tempo, SAP, organico, tabelle guida, Excel/Power Query, mapping account→WBS, team/profit center, ricodifiche, forecast e output downstream.
- Architettura emersa nei materiali precedenti: Dagster → dbt/NocoDB → MariaDB → Metabase. Gap tecnico: manca una landing/raw immutabile, schema registry, replay, backup/DR e separazione chiara tra ingestion, serving e BI.
- Il documento chiede un modello riusabile: connector/adaptor separati dal core transformation e dalla configurazione cliente; regole comuni e override cliente versionati; decisione tenancy/deploy da chiudere.
- `CDG_Questionario_Analisti_Blueprint_v0.3.xlsx` traduce i gap in domande operative su perimetro, output esistenti, reporting/accessi, fonti ufficiali, Click, ticket collegati, mapping nel tempo, ribaltamento costi, forecast, rettifiche manuali, chiusura, controlli bloccanti, riuso e volumi.

### ProSIGNAL

- Gli appunti ProSIGNAL descrivono un AS-IS basato su UltraEdit per file testuali posizionali inviati da sistemi bancari e controllati prima dell’invio a Banca d’Italia.
- UltraEdit è usato come editor operativo: apre file grandi, seleziona colonne, copia blocchi, fa somme, verifica formato e prepara dati da importare in Excel.
- Volume/struttura: circa 70 file complessivi; estensioni `.txt`, `.inp`, `.dat`; header non sempre presente; record di coda di norma analogo al record di testa quando presente; record dati posizionali classici o struttura record + codice dato + valore; file legacy/non standard.
- Due flussi pilota: Servizi di pagamento come caso limite per dimensione/performance; Segnalazione decadale come caso limite per complessità controlli e numero fonti.
- Servizi di pagamento: fino a circa 17 milioni di righe e 7 GB; ZIP di riferimento circa 159 MB; column mode su blocchi oltre 1 milione di righe; import Excel a blocchi, macro, file appoggio, subtotalizzazione, totalizzazione per FT e confronto andamentale con soglie.
- Segnalazione decadale: circa 7/8 file di input per prodotto bancario; verifiche incrociate tra sistemi, bilancio, fornitori terzi e qualità credito; foglio Excel con colori per origine del dato; output verso Banca d’Italia e confronto con totali Nexen.
- Requisiti confermati: caricamento qualsiasi file testuale, anche non noto a priori; supporto ZIP; conversione Unix/DOS; funzionalità tipo UltraEdit; controlli qualità/formato dati; dashboard operativa; profili Finance e Audit/lettore; MFA/integration corporate da chiarire; retention storica orientata a output/evidenze; parallel run con UltraEdit.

### Kiron CDG

- Kiron compare soprattutto come riferimento nominale/target o come appunto email `Kiron CDG Set up`.
- Non è stato trovato un documento Kiron CDG equivalente all’assessment CDG o agli appunti ProSIGNAL.
- Kiron va trattato per ora come beneficiario target del blueprint, non come fonte requisiti autonoma già documentata.

## 2. Evidenze da chat/memoria

- Nelle conversazioni precedenti è stata cercata una stima/presentazione/mail su una data pipeline per reingegnerizzazione del controllo di gestione, con uso di Dagster e dbt.
- Il lavoro precedente includeva Kiron CDG, Internal CDG e ProSIGNAL come casi di applicazione, ma alcuni dettagli erano dentro email o presentazioni non sempre ritrovate.
- È emersa una raccomandazione: non sommare in modo acritico OutSystems + Dagster + dbt + NocoDB, perché lo stack rischia ridondanza e complessità inutile.
- Stack ricorrenti: Dagster per orchestration, dlt per ingestion, dbt per trasformazioni/test, NocoDB per configurazioni/rettifiche, Metabase o Power BI per BI, MariaDB/Postgres come serving/warehouse da validare.
- Obiettivo riusabile: separare adapter, modello canonico, regole, configurazioni cliente e data products.

## 3. Inferenze ragionate

- La blueprint dovrebbe essere presentata non come “soluzione CDG”, ma come piattaforma modulare per pipeline dati regolabili per dominio: ingestion/source contracts, raw immutable landing, normalization/ref layer, staging/business rules, marts/output certificati, data quality e controls, audit/lineage/replay, dashboard/serving, manual adjustment ledger, deployment/tenant model.
- CDG e ProSIGNAL sono casi complementari: CDG stressa mapping, regole economiche, forecast, rettifiche e BI; ProSIGNAL stressa file grandi, fixed-column, controlli formali, workflow operativo e output regolamentari.
- Kiron può essere usato come prova di riuso commerciale/operativo, ma non come fonte di requisiti finché non arrivano appunti, deck o piano specifici.
- Storyline suggerita: “stesso motore, domini diversi”. Rischio principale: vendere un’architettura prima di chiudere data contract, workload e NFR.

## 4. Gap

### Gap CDG

- Baseline documentale non formalmente approvata.
- P5 ambiguo: semplice output ore SAP oppure dataset integrato economics+ore con rettifiche e redistribuzioni.
- Output downstream Power Query non tutti mappati nel TO-BE.
- Fonte Click citata solo in alcuni materiali.
- Grana, business key, primary key, cardinalità e datatype fisici non chiusi.
- Retention, backfill, freeze, riapertura e restatement non definiti.
- Data quality da trasformare in catalogo controlli, severità, soglie, owner e comportamento su fallimento.
- Governance rettifiche manuali e NocoDB/write-back non chiusa.
- BI requirements insufficienti per scegliere Metabase/Qlik/Power BI.
- NFR operativi, sicurezza/privacy, CI/CD e DR insufficienti.

### Gap ProSIGNAL

- Mancano file campione reali, tracciati aggiornati, template Excel, macro/VB, esempi Nexen e output finali.
- Da chiarire encoding, layout record, variabilità tracciati, DOS vs Unix e regole di conversione.
- Da chiarire quali controlli sono automatici, quali restano manuali e quali devono bloccare il processo.
- Da chiarire se il template Excel decadale resta motore di calcolo o se le formule vengono migrate.
- Da definire retention distinta per input grandi, output, analisi ed evidenze.
- Da definire benchmark: throughput, restart, idempotenza, memoria, query p95, recovery e storico realistico.

### Gap Kiron

- Nessun documento operativo Kiron CDG trovato nella ricognizione.
- Esiste solo riferimento a setup/piano/struttura Jira, da recuperare.
- Mancano processi, fonti, volumi, output, owner, stima e requisiti di riuso specifici.

## 5. Domande aperte prima della storyline

1. Qual è la fonte autorevole per CDG: assessment, analisi funzionale, XMind, deck o piano?
2. Per CDG, il perimetro della presentazione è blueprint generale o caso Internal CDG completo P1-P6?
3. Kiron deve comparire come caso reale con contenuto, o solo come destinatario target della blueprint?
4. ProSIGNAL va raccontato come pipeline fixed-column/regulatory o come sostituzione UltraEdit con workflow Finance?
5. La blueprint deve proporre uno stack preferito o solo gate decisionali per confrontare Dagster/dlt/dbt/Metabase/NocoDB/Power BI/Talend/Qlik/OutSystems?
6. Quali materiali originali possono essere copiati nel repo dopo review di confidenzialità?

## 6. Materiale utile per prossima fase

- Matrice `case-study vs capability`: CDG = Jira/Tempo, Excel, SAP, mapping, forecast, BI, adjustments; ProSIGNAL = fixed-column, file grandi, ZIP, header/tail, controlli regolamentari, workflow 4-eyes, retention output; Kiron = TBD.
- Slide “Blueprint layers”: source contracts, landing/raw immutable, ref/normalized, staging/business rules, mart/outputs, controls/DQ/quarantine, audit/lineage/replay, manual adjustment ledger, BI/serving, operations/CI/CD/security/tenancy.
- Slide “Decision gates before build”: baseline scope, data contracts, workload/NFR, tool option assessment, benchmark ProSIGNAL, reuse/tenant model, estimate bottom-up.
