# Analisi della Pipeline Legacy e della BI

## Ambito ed evidenze

Questo documento ricostruisce il funzionamento della pipeline legacy e dello stack BI a partire dall'area SharePoint:

- `/mnt/c/Users/iingenito/TXT e-solutions S.p.A/SharePoint - TXT Novigo - Dati gestionali (PQ e report)`

L'analisi si basa su:

- metadati di dipendenza delle cartelle di lavoro (`connections.xml`, fogli workbook)
- note di processo e documenti di review
- workbook di sequenza `Analisi sequenza file.xlsx`
- mappe xmind che descrivono le dipendenze delle Power Query
- layout dei report Power BI e guida utente
- stato attuale del repository Dagster

Dove il codice Power Query M effettivo è incorporato nei file Excel binari, la logica sotto è stata inferita da mappe di dipendenza, nomi dei workbook, output, controlli e documentazione di processo. La ricostruzione è sufficientemente solida per la progettazione della migrazione, ma alcuni dettagli a livello di formula dovranno comunque essere validati durante l'implementazione dbt.

## Sintesi esecutiva

Il sistema legacy non è una singola pipeline. È una catena di estrazioni manuali, tabelle di riferimento, trasformazioni Power Query, workbook di QA e report Power BI.

L'artefatto centrale è:

- `Output/Output All (A+B).xlsx`

Questo workbook è il layer semantico operativo per tutta la reportistica sulle ore. La maggior parte dei workbook downstream dipende direttamente da lui.

Il processo ha due domini principali:

1. `Ore / Jira / Tempo / Axel / HR / SAP WBS`
2. `Economics / SAP actuals / forecast / ribaltamenti / budget`

Questi vengono integrati in seguito per la BI finale.

Il materiale di review rende anche esplicita una seconda distinzione:

1. estrazioni e trasformazioni inframensili usate per i controlli
2. processing di fine mese con storicizzazione formale di `Output All (A+B)`

Questa distinzione è importante perché il processo legacy non è solo un refresh periodico. Ha sia run operativi usa-e-getta sia una baseline di chiusura mensile.

Il progetto Dagster attuale copre solo un sottoinsieme piccolo ma utile del perimetro legacy:

- campi Jira
- issue Jira
- account Tempo
- alcune tabelle Excel di corrispondenza

La logica business principale legacy è ancora fuori dalla pipeline attuale, in particolare:

- estrazione mensile dei worklog (`Report ore new.xlsx`)
- riconciliazione storica issue-account
- logica di derivazione di output-all
- calcoli economics actual / forecast
- analytics dei servizi
- workflow di billing/T&M

## Architettura legacy

## Principali famiglie di sorgenti

### Jira / Tempo

Estratti operativi principali:

- `Input/input jira/Report ore new.xlsx`
- `Input/input jira/account jira.xlsx`
- `Input/input jira/Ticket light.xlsx`
- `Input/input jira/Ticket.xlsx`
- `Input/input jira/Issue dati aggiuntivi.xlsx`

Regole di estrazione documentate:

- `Report ore new.xlsx` è mensile ed è esportato da Tempo Logged Time
- `Account Jira` è esportato dai dati account Jira/Tempo
- `Ticket light.xlsx` è un estratto issue Jira alleggerito usato per i controlli inframensili
- `Ticket.xlsx` è il dataset issue più completo, costruito in parte combinando dati storici issue con `Ticket light`
- `Issue dati aggiuntivi.xlsx` è un add-on mirato per attributi extra non disponibili in modo stabile nel flusso principale

Nota business critica da `Analisi per API da Jira.docx`:

- la corrispondenza issue-account è affidabile solo passando dalla storia dei worklog
- un estratto completo delle issue non fornisce da solo una mappatura tecnica pulita dell'account
- i nomi account non sono una chiave di join stabile a causa di differenze di encoding / caratteri

Questo spiega perché il processo legacy costruisce e mantiene `Issue e account.xlsx`.

### CDG APP / Axel / SAP / HR

Altri input core:

- `Input/scarico cdg app/Tabella di raccordo.xlsx`
- `Input/input axel/commesse.xlsx`
- `Input/input axel/ore axel.xlsx`
- `Input/input sap/wbs.xlsx`
- `Input/input sap/costi sap.xlsx`
- `Input/input sap/ricavi sap.xlsx`
- `Input/input sap/fatturato sap.xlsx`
- `Input/input risorse/Organico.xlsx`
- `Input/input risorse/PQ Anagrafica risorse.xlsx`

Ruolo di ciascuna sorgente:

- `Tabella di raccordo`: ponte tra account Jira e WBS SAP con date di validità
- `commesse`: anagrafica ordini/commesse Axel
- `ore axel`: output ore orientato SAP/Axel
- `wbs`: struttura WBS ufficiale e ancoraggio della classificazione business
- `costi/ricavi/fatturato`: actual economics da SAP
- `Organico`: anagrafica risorse per arricchimento team/area/tipo risorsa

### Tabelle di riferimento e corrispondenza

Il processo legacy è fortemente guidato da regole. Tra i file di riferimento più importanti ci sono:

- `Issue e account.xlsx`
- `Account Category.xlsx`
- `Team e PM.xlsx`
- `IT OPS gruppi assignee.xlsx`
- `Period e anno.xlsx`
- `Gruppo cliente.xlsx`
- `Eccezioni wbs new org.xlsx`
- `WBS Category.xlsx`
- `Customers - Organization.xlsx`
- `KPI Target.xlsx`
- `IT OPS progetti Service Desk.xlsx`
- `Programmi R&D.xlsx`

Queste sono tabelle di mapping mantenute dal business. In pratica funzionano come motore di regole per l'assegnazione delle categorie, l'attribuzione dei team, la normalizzazione WBS, il perimetro servizi e le eccezioni QA.

## Processo legacy end-to-end

## 1. Fase pre-Output-All

L'ordine del processo è documentato in `Analisi sequenza file.xlsx`.

La nota di review aggiunge un'importante distinzione operativa:

- i run inframensili sono usati per i controlli
- i run di fine mese producono la baseline storicizzata `A+B`

Quindi la sequenza sotto va letta come backbone del processo ufficiale di chiusura, non solo come ordine pratico di refresh.

### Step 1.1 Account Jira

- sorgente: Jira/Tempo
- output: `Account Jira`
- ruolo: anagrafica account con chiavi, nomi, clienti, categorie e stato

### Step 1.2 Report ore new

- sorgente: Tempo Logged Time
- output: `Report ore new.xlsx`
- ruolo: dataset mensile dei worklog
- nota: è manuale e perimetrato al mese

Questa è la singola sorgente più importante per i fatti ore.

### Step 1.3 Ticket light

- sorgente: plugin Jira
- output: `Ticket light.xlsx`
- ruolo: estratto operativo issue alleggerito
- logica filtro: issue aperte più issue create/aggiornate di recente

### Step 1.4 Ticket

- output: `Ticket.xlsx`
- ruolo: vista issue storica/completa
- logica: una Power Query combina `Ticket light` con lo stock storico delle issue

### Step 1.5 Issue dati aggiuntivi

- sorgente: plugin Jira + Power Query
- ruolo: arricchimento delle issue con attributi come stime, campi legati alla fatturazione, campi SLA
- nota: estratto in blocchi semestrali e poi accodato via query

### Step 1.6 Tabella di raccordo

- sorgente: CDG APP
- ruolo: ponte tra account Jira, ordine Axel e WBS SAP, comprese date di validità e stato

### Step 1.7 PQ Issue e account

- workbook: `PQ Issue e account.xlsx`
- input: `Report ore new` + storico `Output All (A+B)`
- output: `Issue e account`

Questo ricostruisce una relazione persistente issue-account a partire dallo storico dei worklog e dai dati del mese corrente.

### Step 1.8 Issue e account

- workbook / output di riferimento usato poi nelle trasformazioni successive

### Step 1.9 Power Query Output all - Def

- workbook: `Power Query Output all - Def.xlsx`
- ruolo: workbook di trasformazione principale del dominio ore

Questo è il cuore della pipeline legacy.

### Step 1.10 PQ Anagrafica risorse

- sorgente: `Organico`
- ruolo: anagrafica risorse normalizzata usata per arricchire ore e issue

## 2. Cosa produce Output All

La mappa delle dipendenze compressa e i metadati del workbook mostrano i principali output:

- `A-Report ore new raggruppato elaborato`
- `B-Ticket elaborato`
- `C-Report ore new acc int`
- `D-Ore Axel`
- `Linked Issue SD`
- `E-Economics plus`
- `E+A+D raggruppati`

### A. `A-Report ore new raggruppato elaborato`

Costruito a partire da:

- worklog raggruppati
- anagrafica account
- organico normalizzato
- ponte di validità
- WBS
- Team e PM
- Period e anno

Significato business:

- fact curato delle ore
- chiavi a livello issue/persona/periodo/account/WBS
- fondazione per la maggior parte delle analisi time-based

### B. `B-Ticket elaborato`

Costruito a partire da:

- `Ticket`
- regole di grouping degli assignee
- `Issue e account`
- arricchimenti account
- organico

Significato business:

- ibrido dimensione/fatto sulle issue
- contiene classificazione issue, categoria, attributi linked issue e attributi di servizio

### C. `C-Report ore new acc int`

Derivato da worklog + arricchimento account.

Significato business:

- slice delle ore su account interni

### D. `D-Ore Axel`

Costruito a partire da:

- `Ore Axel`
- organico
- WBS

Significato business:

- ore rimodellate per riconciliazione SAP/Axel

### Linked Issue SD

Costruito a partire da dati di linked issue, ticket elaborato e arricchimento account.

Significato business:

- relazioni padre/figlio per logiche Service Desk e T&M
- usato nei controlli e nelle lavorazioni T&M

### E. `E-Economics plus`

Visibile nel `Output All (A+B).xlsx` finale e riusato a valle.

Significato business:

- actual economics arricchiti da logiche WBS/periodo/team/grouping

## 3. Controlli su Output-All

`Power Query Output All - Controlli.xlsx` è il workbook operativo di data quality. Contiene controlli come:

- issue senza account
- incoerenza tra issue type, categoria e account category
- incoerenze tra customer e organization
- incoerenze di stato padre/figlio nelle linked issue
- issue aperte su account chiusi
- account aperti senza ore recenti
- account non raccordati
- controlli di validità rispetto a CDG APP e Axel

Questo è importante dal punto di vista architetturale: il sistema legacy non è fatto solo di trasformazioni, ma di trasformazioni più QA operativa esplicita.

## 4. Workbook downstream post-Output-All

Dopo l'aggiornamento di `Output All (A+B)`, vengono aggiornati diversi workbook specializzati.

La review inquadra anche `Output All (A+B)` come artefatto mensile storicizzato. Questo è confermato dalle copie mensili salvate in `Save/`, che vanno trattate come output ufficiali di chiusura e non come archivi accidentali.

### `PQ Report ITOPS.xlsx`

Input:

- `A-Report ore new raggruppato`
- `B-Ticket elaborato`
- `Linked Issue`
- `E-Economics`
- tabelle perimetrali del servizio
- gruppi assignee
- account category

Output:

- base report service
- base report effort
- recap per periodo
- effort unito agli economics

Ruolo business:

- mart analitico di Service Desk / IT OPS pre-Power BI

### `Power Query Base Dati AM.xlsx`

Input:

- `Output All (A+B)`
- `Issue dati aggiuntivi`
- tabelle di riferimento
- `Organico`
- `AM - Eccezioni account Jira`

Output:

- `Issue arricchito`
- `Ore arricchito`
- `Filiera completa con ore`
- `Filiera SD con ore`
- controlli sulle eccezioni account

Ruolo business:

- modello servizi per Application Management
- riconcilia i problemi issue/account e costruisce la filiera di servizio

### `Power Query Analisi Servizi.xlsx`

Input:

- `Power Query Base Dati AM`
- file contratti/SLA/KPI

Output:

- `Analisi servizi`
- `Backlog_fine_periodo`
- `Perimetro_analisi_servizi`

Ruolo business:

- analisi dei servizi e metriche di backlog

### `PQ Ricavi.xlsx`

Input:

- `ricavi`, `fatturato`, `costi`, `wbs` da SAP
- storici forecast
- grouping clienti
- regole WBS
- team/PM

Output:

- actual per WBS/cliente
- forecast avviate / potenziali
- dataset storici forecast
- economics plus

Ruolo business:

- mart ricavi e forecast

### `PQ Costi ribaltati.xlsx`

Input:

- economics plus
- costi / fatturato / ricavi per WBS

Logica:

- unpivot di costi/ricavi/fatturato
- derivazione di allocazioni proporzionali
- ribaltamento dei costi di struttura sui WBS

Ruolo business:

- produrre viste di profittabilità in stile EBITDA oltre i costi diretti

### `PQ Integrazione ore e economics.xlsx`

Input:

- ore raggruppate da A
- ore Axel/SAP D
- economics E
- regole WBS/team/grouping

Output:

- `E+A+D`
- dataset integrato raggruppato

Ruolo business:

- ponte finale tra reporting operativo delle ore e reporting economics

### `PQ fatturazione T&M new.xlsx`

Input:

- `Output All (A+B)`
- linked issue
- account jira
- WBS

Ruolo business:

- supporto alla fatturazione mensile T&M
- separazione tra ore principali e secondarie
- filtri di chiusura mensile e controlli ODA/SOW

Questo workbook è fortemente parametrizzato sul mese e rimane manuale.

### `Analisi ore file con formule.xlsx`

Ruolo business:

- post-processing e controlli sulle ore di output-all
- contiene formule manuali

### `R&S dati gestionali.xlsx`

Ruolo business:

- estrae solo i campi orientati alle ore per analisi R&D

## Layer BI legacy

## Report Power BI

Report principale:

- `power BI/Dashboard TXT Novigo_V2.pbix`

Versione estesa:

- `power BI/Dashboard TXT Novigo_V2 - con monitoraggio progetti.pbix`

Add-on monitoraggio progetti:

- `power BI/Dashboard Monitoraggio progetti.pbix`

### Pagine del report

`Dashboard TXT Novigo_V2.pbix` contiene:

- `0-Legenda`
- `1.1-Giorni - Overview`
- `1.2-Giorni - Account e WBS`
- `1.3-Giorni - Trend`
- `1.4-Giorni - Focus R&D`
- `2.1-Economics actual - Overview`
- `2.2-Economics actual - Team commessa attività cliente`
- `2.3-Economics actual - Clienti`
- `2.4-Economics forecast - Ricavi overview`
- `2.5-Economics forecast - Ricavi clienti`

La versione con monitoraggio aggiunge:

- `3.1.1-Monitoraggio progetti - Overview company`
- `3.1.2-Monitoraggio progetti - Overview team`
- `3.2-Monitoraggio progetti - Gantt`
- `3.3-Monitoraggio progetti - Focus progetto`
- `3.4-Monitoraggio progetti - Capacity plan`

### Significato funzionale

Dalla guida utente, la dashboard copre tre aree analitiche:

1. giorni / effort da Jira e worklog
2. economics actual e forecast
3. monitoraggio progetti

La nota di review rende esplicita l'architettura prevista:

- `Power BI solo presentation`

Quindi Power BI va inteso come layer di presentazione sopra dataset semantici costruiti nei workbook, non come il punto in cui viene scritta la logica principale di trasformazione.

Dimensioni business chiave esplicitamente descritte:

- team commessa
- team risorsa
- area
- cliente
- tipo attività
- categoria issue
- WBS
- periodo

Misure chiave esplicitamente descritte:

- giorni lavorati
- ricavi
- costi diretti
- margine
- EBITDA LOB
- EBITDA
- forecast vs actual vs budget

Il materiale di review elenca inoltre esplicitamente `Budget.xlsx` come input di Power BI. Il budget è quindi una sorgente dashboard di primo livello, non solo un file ausiliario di planning.

## Regole business importanti del legacy

## Regola 1: la lineage issue-account è storica, non solo anagrafica

Il sistema non si fida di una semplice join sull'account name corrente derivato dall'anagrafica issue. Ricostruisce invece la corrispondenza issue-account dalla storia dei worklog e dall'output storico.

## Regola 2: i worklog mensili chiusi sono storia append-only

`Report ore new` è mensile e poi diventa parte dello stock storico. Questo significa che il fact delle ore è di fatto accodato mese per mese.

## Regola 3: la validità conta

Il ponte tra account Jira e WBS SAP è basato su validità temporale. Lo stesso account può mappare in modo diverso nel tempo oppure avere più relazioni attive che richiedono controlli.

## Regola 4: la logica di servizio dipende dalle linked issue

La reportistica Service Desk e T&M dipende dalle relazioni padre/figlio tra issue, non solo dagli attributi della singola issue.

## Regola 5: molte classificazioni sono logica manuale di reference

L'assegnazione delle categorie non è nativa nei sistemi sorgente. Viene derivata da:

- regole account category
- regole WBS category
- mapping team/PM
- grouping degli assignee
- grouping clienti
- eccezioni esplicite

## Regola 6: i controlli qualità fanno parte del processo

Il workbook dei controlli non è opzionale. Il processo presuppone review operativa e correzione delle anomalie prima del consumo finale.

## Copertura attuale Dagster vs perimetro legacy

## Già coperto nel repository

Ingestion API:

- `raw_jira_fields`
- `raw_jira_issues`
- `raw_tempo_accounts`

Mapping Excel attualmente modellati:

- account category
- customers organization
- eccezioni WBS
- etichette issue
- gruppo cliente
- IT OPS gruppi assignee
- IT OPS progetti service desk
- period e anno
- programmi R&D
- team e PM
- WBS category

## Presenti nei mapping file ma esclusi dall'indice batch

Questi esistono come YAML mapping ma sono commentati in `input/config/xls_mappings_index.yaml`:

- `corrispondeza_validita_raccordo`
- `issue_e_account`
- `kpi_target`
- `sintesi_storico_sd`

Questo è rilevante perché questi quattro non sono marginali:

- il bridge di validità è centrale per la lineage account-WBS
- la history issue-account è centrale per l'arricchimento ticket
- i KPI target sono necessari per la BI
- la sintesi storica SD è probabilmente necessaria per continuità di backlog e trend

## Non ancora coperto in Dagster

Ingestion mancanti principali:

- worklog Tempo / export logged time
- ricostruzione attuale della lineage issue-account
- estrazione dominio `Ticket light` / `Ticket` con tutte le colonne business richieste
- estrazione campi aggiuntivi issue
- estrazione bridge CDG APP
- `commesse` e `ore axel`
- `wbs`, `costi`, `ricavi`, `fatturato`, `fatture` da SAP
- anagrafica risorse HR e timbrature
- input budget / forecast
- file contratti / SLA / KPI servizi

Trasformazioni mancanti principali:

- semantic layer output-all
- mart IT OPS
- mart AM / servizi
- mart economics actual / forecast
- mart billing/T&M
- modelli QA di controllo

## Pain point del design legacy

### Estrazione manuale e cambio parametri manuale

Diversi file richiedono esplicitamente filtri mese o setup manuale del refresh.

### Logica distribuita su molti workbook

La logica business è frammentata tra:

- estrazioni sorgente
- file di corrispondenza
- trasformazioni Power Query
- workbook con formule
- workbook di QA
- layer semantico/report in Power BI

### Copie ripetute e varianti storiche

La tree SharePoint contiene molte copie e archivi:

- `Save/old`
- `TMP MARY`
- più copie dei PBIX
- varianti ripetute dei workbook

Questo indebolisce lineage e ownership.

Fa eccezione lo storico mensile di `Output All (A+B)`: il materiale di review indica che fa parte del processo ufficiale di storicizzazione di chiusura e non va trattato come semplice clutter.

### Naming ambiguo

Esempi:

- `A`, `B`, `C`, `D`, `E`
- `Def`, `Controlli`, `plus`, `old`, `new`
- nomi query duplicati

Questi nomi funzionano nell'operatività manuale, ma sono deboli per un impianto ingegneristico manutenibile.

### I controlli qualità sono separati dai modelli di produzione

I controlli esistono, ma sono per lo più workbook-based invece che codificati come test di primo livello.

### Gli output sono file-centric invece che model-centric

La verità operativa è dispersa su fogli Excel invece che su modelli warehouse stabili.

## Implicazioni per la migrazione

La migrazione target non dovrebbe cercare di riprodurre la catena dei workbook uno per uno.

La traduzione corretta è:

- estrazioni sorgente in `raw_*`
- regole business e mapping manuali in `ref_*`
- normalizzazione curata in `stg_*`
- mart stabili che sostituiscano `Output All`, `PQ Report ITOPS`, `Power Query Base Dati AM`, `Power Query Analisi Servizi`, `PQ Ricavi`, `PQ Costi ribaltati`, `PQ Integrazione ore e economics`
- domande e dashboard Metabase che sostituiscano il layer di presentazione Power BI

Il documento successivo definisce questa specifica target.
