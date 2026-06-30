Tags: #area/lavoro #cliente/txt-novigo #progetto/cdg #tipo/analisi #stato/attivo

- Infra per tool e app

A - dati storicizzati
B - dati alla data

/input
	raccoglie tutti i file con dati di input

P.IVA

Ultimo giorno del mese entro pranzo - JIRA
Verifica 

# Estrazioni
## Jira

Utente con accesso a tutti i progetti
### Account
- Tempo 
	- Settings / Import Export / Export 1001 Accounts
	- Reports ->  (Mese precedete e mese corrente)
	- CDG APP (se il task è locckato il task non viene estratto)

Estrazione in Excel con plugin JIRA

```
((statusCategory != Done and created < startOfMonth()) or (updated >= startOfMonth(-1)))  ORDER BY updated ASC
```

| Campi estratti           |
| ------------------------ |
| Key                      |
| Status                   |
| Account                  |
| Organizations            |
| Created                  |
| Project                  |
| Assignee                 |
| Attività su DB           |
| Categoria                |
| Categoria SQL            |
| Comando SQL              |
| Data TK Axel             |
| Impatto incident         |
| Issue Type               |
| KPI Breached             |
| Labels                   |
| Linked Issues            |
| ODA - Ordine di Acquisto |
| Data presa in carico     |
| Processi                 |
| Prodotti                 |
| Resolved                 |
| Satisfaction             |
| Satisfaction date        |
| SLA AMCO                 |
| SLA ING                  |
| SLA SB                   |
| Sla_ticket               |
| Tempo di presa in carico |
| Service Desk time        |
| Tipo Attività            |
| BPO AMCO                 |
| BPO AMPRE                |
| BPO JJ TATOOINE          |
| SOW - Statement of Work  |
| Summary                  |
| Updated                  |
| Reporter                 |
| Priority                 |
| Presa in carico          |
| SLA ELAPSED              |

## Organico

File `organico.xlsx`

Tabella di raccordo gestita in CDG APP 	
`Racccordo JIRA-SAP`

Per le ore arrotondate per SAP
Prende da CDGAPP la tabella Dipendenti

Ore lavorate
da Nuova elaborazione estraggo per mese (fatta da Inder)

Check straordinari
File per la verificare gli straordinari autorizzati


WBS
Company NOV + Profit center NOV delle altre company (nessun filtro di stato)

## Dati Gestionali (SharePoint)
Output All DEF - Ore + Ticket (A+B+C+Linked Issue)
PQ Ricavi - Economics E + Storico forecast

# Sequenza operazioni
La sequenza delle estrazioni / elaborazioni è specificato in
`Analisi sequenza file.xlsx` su SharePoint TXT Novigo.

Nota: link SharePoint redatto nella copia locale del materiale.

## Collegamenti

- [[TODO]]
- [[TXT Novigo/CDG/Preparazione slide]]
- [[TXT Novigo/CDG/Task x Infra]]
- [[WBS]]
