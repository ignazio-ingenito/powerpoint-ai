# ChatGPT Source Inventory — 2026-06-30 Data Pipeline

> Origine: ricognizione ChatGPT su memoria conversazionale, Gmail disponibile nella sessione e riferimenti File Library emersi nelle chat precedenti.  
> Stato: materiale preparatorio, non ancora validato da business/analisti.  
> Nota: non sono stati copiati file originali, URL personali, SharePoint, Gmail display URL, dump dati o export operativi. Dove utile è stata salvata una sintesi da riverificare.

## Fonti trovate

| Fonte | Tipo fonte | Path locale se copiato | Cosa contiene | Autorità | Rischio confidenzialità | Note / riverifica |
|---|---|---:|---|---|---|---|
| Memoria ChatGPT su CDG / Kiron / ProSIGNAL | memoria | `drafts/chatgpt-findings.md` | Richiami a lavori precedenti: blueprint data pipeline, PoC Jira/Tempo, uso Dagster/dbt/dlt, stack Metabase/NocoDB/Power BI, beneficiari Kiron CDG/Internal CDG/ProSIGNAL. | Bassa/Media | Medio | Traccia utile, ma non fonte definitiva. Va riverificata contro documenti originali. |
| `CDG_Requirements_Gap_Assessment_v0.1.xlsx` | documento/spreadsheet citato da File Library | Non copiato | Assessment CDG con executive summary, registro fonti, processi P1-P6, requisiti, gap, domande, impatto stima, gate architetturali e piano workshop. Include raw/normalized/curated, Jira/Tempo, SAP, Excel, Metabase/Qlik, Talend/Dagster/dbt e riuso multi-cliente. | Alta per gap/raccolta requisiti, Media per decisioni non chiuse | Medio/Alto | Documento più strutturato trovato. Recuperare originale e verificare fonti citate. |
| `CDG_Questionario_Analisti_Blueprint_v0.3.xlsx` | documento/spreadsheet citato da File Library | Non copiato | Questionario di 18 domande per chiudere perimetro, fonti ufficiali, mapping, ribaltamenti, forecast, rettifiche, controlli bloccanti, riuso e volumi. Include matrice “Riuso per cliente”. | Alta come materiale di lavoro | Medio | Utile per slide gap/P0 decisions. |
| `PROSIGNAL_Appunti_meeting_1_23_06_26_revisioni_finale_Ignazio.docx` | documento citato da File Library | Non copiato | Appunti finali su ProSIGNAL: UltraEdit AS-IS, file posizionali, file fino a 17M righe / 7GB, ZIP ~159MB, file decadale con 7/8 input, controlli FT, 4-eyes, dashboard, MFA, retention e parallel run. | Alta per ProSIGNAL | Alto | Contiene contesto ING/Finance e dettagli operativi. Copiare solo dopo redazione. |
| Varianti appunti ProSIGNAL | documento citato da File Library | Non copiato | Versioni intermedie/finali degli stessi appunti ProSIGNAL. | Media | Alto | Preferire versione finale Ignazio. |
| `Ongoing.md` / `Ongoing-kanban-compatible.md` | appunto/file citato da File Library | Non copiato | Indice di email/task recenti: Review Processi CDG, Internal Forge roll-out, QLIK knowledge sharing, Creazione progetto Jira ProSignal, Kiron CDG Set up, ProSignal Avvio progetto, Cartella progetto ING. | Media come registro fonti; bassa sul contenuto | Medio | Contiene riferimenti, non contenuto completo. Recuperare da mailbox/workspace. |
| Gmail draft senza subject del 2026-06-23 | email/draft | Non copiato | Trascrizione grezza meeting ProSIGNAL: sostituzione UltraEdit, flessibilità tracciati, file 7GB/16-17M righe, flusso decadale, upload e analisi successive. | Media | Alto | Testo grezzo e confidenziale; sintetizzato nei findings. |
| Possibile email `Kiron CDG Set up` | riferimento redatto | `source-materials/chatgpt-collected/README.md` | Riferimento da Ongoing: attività/piano/struttura Jira Kiron CDG. | Bassa finché non recuperata | Medio | Non trovata direttamente in Gmail con le query disponibili. |
| Possibile fonte `Review Processi CDG` | riferimento redatto | `source-materials/chatgpt-collected/README.md` | Riferimento a cartella condivisa/workspace CDG. | Bassa finché non recuperata | Alto | Recuperare dal workspace/SharePoint/Drive; eventuali link vanno redatti. |
| Possibile fonte `Cartella progetto ING` | riferimento redatto | `source-materials/chatgpt-collected/README.md` | Riferimento a cartella ufficiale ProSIGNAL. | Bassa finché non recuperata | Alto | Non copiare link firmati o URL con token. |

## Fonti escluse o non copiate

- File originali File Library: non copiati perché non disponibili come byte locali e/o potenzialmente confidenziali.
- Gmail display URL / link interni: non copiati perché personali e non portabili.
- Eventuali SharePoint o link firmati: non acquisiti; conservare solo nome fonte e percorso logico redatto.
- Dump dati, esempi di file bancari, macro Excel/VB operative, export cliente: non disponibili e comunque da non committare senza selezione/redazione.
