# Fondamenti del Refactoring

Questo documento riassume le scelte architetturali e di processo alla base del refactoring dalla workflow legacy basata su Excel, Power Query e Power BI alla piattaforma attuale basata su Dagster, dbt e Metabase.

## Obiettivo

Il refactoring serve a sostituire un processo di reporting manuale e centrato sui file con una piattaforma dati governata che:

- ingestisca le sorgenti in modo ripetibile
- separi la normalizzazione tecnica dalla logica business
- renda esplicite le dipendenze
- supporti output ufficiali di chiusura mese tracciabili
- ricostruisca il layer BI su dataset di warehouse invece che su logiche nei workbook

## Perché il processo legacy richiedeva un refactoring

Il processo legacy ricostruito nella [Documentazione del Processo Legacy](../legacy/index.md) presentava questi limiti strutturali:

- la logica business era distribuita tra molti workbook Excel e catene Power Query
- le dipendenze erano difficili da tracciare e facili da rompere
- gli output di chiusura mese dipendevano da una sequenza manuale e da controlli umani
- mapping, override e tabelle di corrispondenza erano incorporati nei file invece di essere gestiti centralmente
- Power BI dipendeva da output Excel curati e non da un layer modellato in warehouse

## Scelte della piattaforma target

Lo stack target corrente è:

- `Dagster` per l'orchestrazione
- `dlt` per l'ingestion
- `MariaDB` per lo storage
- `dbt` per le trasformazioni
- `Metabase` per la BI
- `NocoDB` per le tabelle di riferimento e i mapping manuali governati

Queste scelte sono approfondite ulteriormente in:

- il documento di architettura del data layer
- la specifica della pipeline Jira e Tempo

I documenti di dettaglio restano nel repository come documentazione tecnica di riferimento.

## Decisioni architetturali principali

### Separare ingestion e trasformazione

- `dlt` e Dagster gestiscono estrazione, comunicazione con API, ingestion da file, logiche incrementali e metadati tecnici di caricamento
- `dbt` gestisce normalizzazione, join, controlli qualità e mart pronti per il business

### Sostituire la logica dei workbook con layer modellati

Il warehouse target usa quattro layer logici:

- `raw`
- `ref`
- `stg`
- `mart`

Questo sostituisce formule nascoste e catene di query nei workbook con modelli SQL espliciti e dati di riferimento governati.

### Mantenere i mapping manuali business, ma fuori dalla logica Excel

Il processo legacy contiene molte tabelle di corrispondenza, override e file lookup. Restano necessari, ma devono vivere in tabelle `ref` governate tramite NocoDB o input versionati, non come logica sparsa nei workbook.

### Trattare gli output di chiusura mese come deliverable di primo livello

Il processo legacy distingue tra run di controllo intramensili e output ufficiali storicizzati di fine mese. Il refactoring deve quindi prevedere:

- logiche di snapshot per le chiusure ufficiali
- separazione chiara tra output provvisori e output certificati
- logiche ricostruibili e tracciabili per il reporting storico

## Principio di migrazione

La migrazione non deve riprodurre meccanicamente ogni workbook. Deve preservare il risultato business ricostruendo gli stessi output semantici in forma nativa di warehouse:

- ingestion in `raw`
- standardizzazione tecnica in `stg`
- join business e KPI in `mart`
- dashboard finali in Metabase

## Ambito del refactoring corrente

L'attuale repository copre già una parte della transizione:

- ingestion Jira e Tempo in Dagster e dlt
- ingestion Excel tramite mapping guidati da YAML
- MariaDB remoto come storage centrale
- stack operativo iniziale per NocoDB e Metabase

Il lavoro principale ancora da completare è:

- completare la copertura ingestion per tutto il set di sorgenti legacy
- costruire i model dbt di staging e mart che sostituiscano il layer semantico legacy
- reimplementare gli output di dashboard in Metabase
- aggiungere runbook operativi e controlli qualità

## Nota di pubblicazione

Questo documento fa parte del set pubblicabile su Confluence e viene mantenuto direttamente nel repository come fonte di verità.
