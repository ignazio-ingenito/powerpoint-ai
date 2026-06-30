# Internal CDG Analysis

## Scope

Analisi mirata del materiale in `../cdg-data-pipeline-docs`, con focus su Internal CDG.

Questa nota corregge e approfondisce l'inventory iniziale: in `cdg-data-pipeline-docs` esistono effettivamente materiali ricchi sul controllo di gestione interno TXT Novigo.

## Fonti Analizzate

| Fonte | Tipo | Contenuto rilevante |
|---|---|---|
| `v2/Analisi funzionale processi CDG.docx` | Analisi funzionale | Processi actual/forecast, input, tabelle guida, output e logiche di arricchimento/ribaltamento |
| `v2/Analisi sequenza file.xlsx` | Sequenza operativa | Ordine di estrazioni/elaborazioni, fonti, campi, dipendenze tra file |
| `v2/Campi output.xlsx` | Dizionario output | Campi per output P1-P6 e mapping fonti |
| `v2/Campi tabelle.xlsx` | Dizionario tabelle guida | Tabelle T1-T11 per PM, team, account category, costi, tipo commessa e attivita' |
| `v2/Processi CDG.xmind` | Mappa processi | Sei processi principali P1-P6 |
| `v2/CDG Process Reengineering.xmind` | Roadmap/process design | Perimetro, assessment, TO BE, ambienti, normalizzazione, elaborazioni, dashboard, test e go-live |
| `v2/Processo Economics plus ribaltato.xmind` | Processo economics | Input SAP, tabelle, ribaltamenti, calcolo margine/EBITDA |
| `v2/Processo Integrazione economics e ore.xmind` | Integrazione ore/economics | Integrazione ore Jira/SAP ed economics ribaltato |
| `v2/CDG Process Reengineering.pptx` | Deck sorgente | Contesto/esigenza, AS IS/TO BE, macropiano, benefici, effort e slide architettura |

## Cosa Significa Internal CDG

Il materiale descrive il controllo di gestione interno TXT Novigo.

Il processo deve rilevare e storicizzare:

- costi;
- ricavi;
- ore lavorate che incidono sui costi;
- commesse cliente autorizzate/avviate;
- controlli inframensili ante contabilizzazione di fine mese;
- forecast ricavi di fine anno su commesse avviate e potenziali.

Nel deck sorgente il contesto e' espresso in modo chiaro: TXT Novigo gestisce il controllo di gestione interno tramite un processo mensile che consolida dati granulari fino al conto economico di commessa, abilitando confronto consuntivi vs budget e forecast vs budget.

## Input E Sorgenti

Le sorgenti principali sono:

- **Jira/Tempo**
  - lista issue e attributi;
  - analitico rilevazioni mese;
  - account e attributi;
  - report ore;
  - ticket light;
  - issue dati aggiuntivi.
- **Organico**
  - dipendenti, consulenti e risorse di gruppo che rilevano in Jira;
  - informazioni su CID, nome SAP, tipo risorsa, date, orario.
- **SAP**
  - lista WBS;
  - ricavi WBS per periodo;
  - costi WBS per periodo;
  - fatturato WBS per periodo.
- **CDG app**
  - raccordo account Jira - WBS SAP;
  - output trasformazione ore Jira in tracciato SAP;
  - export iniziative potenziali per forecast.
- **File ricavi / Forecast WCS**
  - pianificazione ricavi residui, backlog e iniziative potenziali.

## Tabelle Guida

La documentazione descrive un set ricco di tabelle guida, da trattare nella blueprint come reference data governati:

- ricodifica PM gestionale;
- assegnazione commesse a team;
- eccezioni WBS/team;
- scomposizione account category;
- team, area e profit center;
- gruppo cliente;
- linked issue Jira;
- distinzione costi primo margine / costi struttura;
- tipo commessa per priority;
- interna / cliente per priority;
- attivita' specifica;
- probabilita' alta/bassa;
- periodi.

## Processi P1-P6

### P1 - Actual Ore Mensile

Normalizza e arricchisce le rilevazioni ore mensili.

Produce `OUTPUT 1 - Tabella A Mensile Actual`, da storicizzare.

Elementi chiave:

- chiave period + issue + full name + account;
- linked issue;
- decodifica account category;
- team risorsa e team commessa;
- WBS di destinazione;
- attributi SAP;
- gruppo cliente;
- flag assenze/rilevazioni;
- flag periodo.

### P2 - Actual Ore Inframensile

Supporta controlli inframensili e viene sostituito a ogni estrazione.

Controlli citati:

- congruenza tra linked issue e issue key rispetto ad account key;
- status WBS vs presenza di ore rilevate;
- account Jira raccordati a WBS chiuse.

### P3 - Ore Secondarie / Linked Issue

Usa lo storico actual per calcolare ore secondarie su issue T&M Cheleo e linked issue.

Produce `OUTPUT 2 - Tabella Linked Issue Actual`.

### P4 - Actual Economics

Integra ricavi, costi e fatturato su chiave period-WBS.

Calcoli e arricchimenti:

- costi primo margine;
- costi struttura;
- allocazione costi interni e struttura;
- margine;
- EBITDA LOB;
- EBITDA;
- PM/team/area/profit center;
- gruppo cliente;
- tipo commessa;
- interna/cliente;
- attivita' specifica.

Produce `OUTPUT 3 - Tabella Economic plus Actual`.

### P5 - Ore SAP Per Integrazione Economics

Raggruppa le ore rendicontate da output CDG app su chiave period-WBS.

Produce `OUTPUT 4 - Tabella Ore per WBS per integrazione con Economics actual`.

### P6 - Forecast

Normalizza e storicizza forecast da estrazioni C3, R1 e F1.

Produce `OUTPUT 5 - Tabella Storico forecast completo`.

Campi chiave:

- data estrazione;
- cliente;
- WBS SAP;
- descrizione iniziativa/WBS;
- stato iniziativa;
- tipo elemento di offerta;
- linea di offerta;
- perimetro;
- PM/IM;
- periodo;
- ricavi netti/lordi;
- probabilita' alta/bassa.

## Sequenza File E Dipendenze Operative

`Analisi sequenza file.xlsx` descrive un processo pre e post `Output All`.

Esempi rilevanti:

- estrazione account Jira;
- report ore new;
- ticket light;
- ticket storico + Power Query;
- issue dati aggiuntivi;
- tabella di raccordo CDG app;
- PQ issue e account;
- Power Query Output All;
- PQ anagrafica risorse;
- controlli post Output All;
- analisi servizi;
- R&S dati gestionali.

La sequenza conferma che Internal CDG non e' solo una pipeline tecnica: e' un flusso operativo con dipendenze, aggiornamenti propedeutici, controlli e file intermedi.

## Indicazioni TO BE Gia' Presenti

Il materiale `CDG Process Reengineering` include gia' una direzione TO BE:

- ridurre manualita';
- ingegnerizzare fasi del processo;
- aumentare affidabilita' e ripetibilita';
- rafforzare sicurezza e tracciabilita';
- efficientare effort;
- costruire soluzione generalizzabile ed estendibile.

I blocchi TO BE ricorrenti sono:

- staging area e pipeline dati;
- caricamento input grezzi;
- normalizzazione;
- mapping automatico/manuale;
- gestione scarti;
- quadrature e audit trail;
- storicizzazione;
- dashboard CDG;
- dashboard tecnica;
- logging e monitoraggio;
- profili e matrice accessi;
- ambienti dev/test/prod.

## Implicazioni Per La Blueprint

Internal CDG deve diventare il caso di riferimento principale della presentazione, non un gap.

La blueprint deve includere almeno:

1. **Data contracts per fonte:** Jira/Tempo, SAP, CDG app, file forecast, organico.
2. **Reference data governati:** tabelle guida T1-T13, mapping e validita' temporale.
3. **Layer raw/stg/mart:** raw source-faithful, staging normalizzato, mart/output per P1-P6.
4. **Orchestrazione per processo:** P1-P6 come job o asset logici, con dipendenze e refresh differenziati.
5. **Controlli e quadrature:** linked issue, WBS chiuse, scarti, fonte vs output.
6. **Storicizzazione selettiva:** input e output marcati come `DA STORICIZZARE`.
7. **Data product finali:** Actual ore, Inframensile, Linked issue, Economics plus, Ore SAP x economics, Storico forecast.
8. **BI e governance:** dashboard CDG, dashboard tecnica, audit trail, logging, profili.

## Correzione Rispetto Alla Sintesi Precedente

Prima Internal CDG era indicato come materiale da recuperare o da confermare.

Questa analisi mostra invece che:

- Internal CDG e' ampiamente documentato in `cdg-data-pipeline-docs`;
- il materiale descrive AS IS, TO BE, input, processi, output e piano;
- CDG e Internal CDG possono essere trattati come lo stesso caso sorgente principale, salvo diversa precisazione dell'utente.

## Gap Residui

- Verificare quali parti del materiale sono ancora attuali rispetto al repository `cdg-data-pipeline`.
- Decidere se importare estratti testuali generati dai binari come materiale derivato in `source-materials/` o mantenerli solo nei draft.
- Chiarire se Kiron CDG deve essere trattato come variante di questa blueprint o come caso separato.
- Per ProSignal resta necessario materiale aggiornato e file/tracciati di esempio.

