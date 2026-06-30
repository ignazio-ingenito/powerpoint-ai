	Oggetto: Spunti dall’AWS Summit Milano 2026

Ciao a tutti,

dopo la partecipazione all’AWS Summit Milano 2026, condivido qualche spunto sulle sessioni seguite e su quello che, secondo me, può essere interessante per TXT Novigo.

Il messaggio generale dell’evento, già dalla keynote di AWS, è stato abbastanza chiaro: il cloud non viene più proposto solo come infrastruttura, ma come piattaforma per modernizzare applicazioni, gestire meglio i dati e portare l’AI dentro processi reali, non solo dentro demo o chatbot.

I temi emersi sono molto vicini ad alcune sfide che abbiamo già davanti: modernizzazione dello stack PHP 7.4, integrazione con AS400/RPG, progetti di data ingestion con grandi volumi, gestione web di file molto grandi, uso di OutSystems e costruzione di un orchestratore AI.

Il primo punto forte riguarda la modernizzazione del legacy. Nella sessione “Strangler Fig, Sagas & Circuit Breaker Patterns for transformation”, raccontata attraverso il caso Volksbank, è emerso un messaggio molto concreto: su sistemi critici non ha senso partire da una riscrittura completa. È più realistico procedere per passi, isolando il legacy, creando API di disaccoppiamento, mappando le dipendenze e sostituendo progressivamente le parti più critiche. Questo approccio mi sembra molto applicabile al nostro scenario PHP/AS400.

Lo stesso tema è tornato anche nella sessione AWS “Dal legacy al Cloud AWS: come reinventare i canali bancari”, dove il punto non era “buttare via tutto”, ma costruire un percorso controllato: rendere il legacy più osservabile, proteggerlo con pattern architetturali adeguati e modernizzare progressivamente le aree a maggior valore o maggior rischio.

Il secondo tema riguarda i dati. Nella sessione AWS “Tre passi verso il futuro: migrazione, data platform e AI” è emerso chiaramente che l’AI funziona bene solo se sotto ci sono dati governati, accessibili e tracciabili. Per i nostri progetti di ingestion e gestione di file di diversi GB (come Prosignal), questo significa evitare soluzioni troppo applicative e pensare invece a una piattaforma con storage scalabile, processing asincrono, audit, monitoraggio e qualità del dato. In pratica, OutSystems può gestire bene UI e workflow, ma non dovrebbe diventare il motore che si porta sulle spalle file enormi e lavorazioni pesanti.

Sul tema AI, la sessione “Sviluppo di modelli AI con Amazon SageMaker AI”, con il caso Multiverse, ha mostrato un approccio più strutturato alla gestione di modelli, dati e processi AI. Per noi il punto non è necessariamente addestrare modelli custom da subito, ma capire quando servono piattaforme più complete per MLOps, governance, controllo qualità e gestione del ciclo di vita dei modelli.

Un altro spunto utile è arrivato dalla sessione AWS “AWS DevOps Agent: investigare incidenti con l’AI autonoma”, dove l’AI viene usata come supporto operativo per analizzare log, metriche, alert e possibili cause di un incidente. È un caso d’uso interessante anche internamente: un assistente DevOps che aiuti nella diagnosi, proponga runbook o remediation, ma lasci al team il controllo sulle azioni critiche.

Il tema più vicino al nostro orchestratore AI è emerso nelle sessioni sull’AI agentica. TeamSystem, nella sessione “Dalle piattaforme agentiche alla Agentic UI”, ha raccontato l’evoluzione verso interfacce in cui l’utente non si limita a compilare form, ma viene supportato da agenti capaci di interpretare contesto, suggerire azioni e guidare processi. Questo si collega bene a OutSystems: possiamo immaginare OutSystems come layer di UI e workflow, e un orchestratore AI come motore intelligente integrato con dati, API e sistemi aziendali.

Anche OverIT e Prometeia, nella sessione “Agentic AI per modernizzazione e sviluppo software”, hanno mostrato come l’AI agentica possa avere valore non solo nei prodotti, ma anche nel delivery: analisi del codice, documentazione, refactoring assistito, generazione test, code review e supporto alla modernizzazione. Il punto è governarla bene: non uno sviluppatore automatico lasciato libero di fare danni con entusiasmo, ma un acceleratore controllato dentro un processo con review, test e tracciabilità.

Secondo me il punto da evitare è trattare AWS solo come hosting o l’AI come iniziativa separata dal resto. Il valore vero sta nel collegare modernizzazione, dati e AI dentro un modello più coerente e riusabile.

In sintesi, il Summit mi sembra confermi una direzione interessante per noi: modernizzare il legacy senza strappi, costruire basi dati più solide e portare l’AI dentro processi reali, governati e misurabili.

Come passo successivo, potrebbe avere senso individuare uno o due casi concreti su cui verificare questi pattern, ad esempio un progetto data-intensive come Prosignal, un primo scenario legato all’orchestratore AI oppure, in modo più mirato, un ambito PHP/AS400 su cui valutare un percorso di modernizzazione progressiva.

Ignazio