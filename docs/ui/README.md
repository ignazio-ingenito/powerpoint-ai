# UI References

Questa cartella contiene riferimenti visivi e di layout per creare nuove presentazioni.

Usare questi file per dedurre lo stile grafico, la struttura delle slide, la densità del contenuto e il trattamento visuale di sezioni ricorrenti. Non usare questa cartella come destinazione per output generati.

## Reference Disponibili

Questa cartella deve essere trattata come un archivio dinamico di reference visuali.

Prima di creare, modificare o revisionare un deck, verificare sempre tutti i file effettivamente presenti in `docs/ui/`, non solo quelli elencati in questo README. Nuove immagini, PDF, screenshot o altri export aggiunti in futuro devono essere considerati automaticamente come possibili reference visive, salvo diversa indicazione dell'utente.

Usare un comando equivalente a:

```bash
find docs/ui -maxdepth 1 -type f | sort
```

Poi ispezionare i file rilevanti in base al tipo di deck richiesto.

### `*.png`

Sequenza di slide esportate da deck commerciali Novigo/TXT.
Da usare per dedurre ulteriori pattern grafici e di layout, in particolare quando il deck richiesto è più vicino a quel linguaggio visuale o quando contiene elementi analoghi per contenuto, struttura o densità.

Caratteristiche tecniche:

- formato 16:9
- risoluzione immagini: 1920 x 1080
- stile corporate, pulito, commerciale
- palette prevalente: bianco, nero/grigio, azzurro, teal/verde acqua
- uso di gradienti teal/azzurro per enfasi, label e barre decorative

### Altri File Futuri

Ogni nuovo file aggiunto in `docs/ui/` deve essere considerato parte delle reference disponibili:

- immagini esportate da slide;
- screenshot;
- PDF di riferimento;
- anteprime o mockup;
- altri asset visuali forniti dall'utente.

Non assumere che l'elenco sopra sia esaustivo. Se il contenuto di un nuovo file non è chiaro dal nome, ispezionarlo prima di decidere se usarlo come riferimento.

## Come Usare Questa Reference

Usare i file presenti in `docs/ui/` come riferimento per:

- proporzioni e ingombri generali della slide
- posizione di logo, titolo sezione e numero pagina
- uso dello spazio bianco
- gerarchia tipografica
- stile di titoli, sottotitoli e paragrafi
- trattamento di parole chiave evidenziate in colore
- struttura di slide con contenuto testuale
- struttura di slide architetturali o scenario-based
- tabelle e card per economics
- slide di apertura e chiusura

Non copiare contenuti specifici del cliente, nomi, importi, date, scenari, tecnologie o claim presenti nelle reference, salvo richiesta esplicita dell'utente.

## Pattern Layout

### Copertina

Riferimento principale: `bernadelli-01-copertina-proposta-infrastruttura-server.png`.

Pattern:

- loghi in alto a sinistra/alto centro
- grande titolo nella parte bassa della slide
- sottotitolo o nome cliente sotto al titolo
- data in basso a sinistra
- ampio spazio bianco
- elemento grafico decorativo sul lato destro
- titolo con gradiente o colore teal/azzurro

Usare questo pattern per aperture commerciali sobrie e istituzionali.

### Slide di Contesto

Riferimento principale: `bernadelli-02-contesto-esigenza-obiettivi.png`.

Pattern:

- header con logo a sinistra, titolo sezione in alto, numero pagina a destra
- barra decorativa sottile sotto l'header
- immagine verticale a sinistra con overlay teal
- contenuto principale a destra
- blocchi numerati per organizzare contesto, esigenza e obiettivi
- parole chiave evidenziate in teal/azzurro

Usare questo pattern per introdurre il razionale business della proposta.

### Slide Scenario / Architettura

Riferimenti principali: `bernadelli-06-scenario-on-premise-alta-affidabilita.png`, `bernadelli-07-scenario-cloud-distribuito.png`, `bernadelli-08-confronto-soluzioni.png`, `bernadelli-09-scenario-consigliato-cloud.png`.

Pattern:

- titolo sezione in alto con struttura "Scenario X | Messaggio"
- messaggio sintetico sotto al titolo
- area visuale a sinistra con box, icone, loghi o livelli architetturali
- area testuale a destra con bullet organizzati per macro-temi
- uso di box con bordo teal/azzurro e sfondo leggero
- enfasi sui benefici business e operativi

Usare questo pattern per confrontare opzioni, AS IS / TO BE, architetture e scenari evolutivi.

### Slide Economics / Costi

Riferimento principale: `bernadelli-10-costi-simulazione-lungo-periodo.png`.

Pattern:

- titolo sezione breve in alto
- messaggio introduttivo centrato o in alto
- card orizzontali per scenari di costo
- intestazioni card con gradiente teal/azzurro
- tabelle semplici con righe separate da linee sottili
- box di sintesi o raccomandazione nella parte bassa
- evidenza del confronto economico di lungo periodo

Usare questo pattern per confrontare scenari, canoni, una tantum, TCO o simulazioni economiche.

### Chiusura

Riferimento principale: `bernadelli-11-chiusura-contatti.png`.

Pattern:

- logo centrale o leggermente sopra il centro
- contatti aziendali sotto al logo
- background chiaro con texture molto leggera
- disclaimer/confidentiality in basso

Usare questo pattern per slide finali istituzionali.

## Regole di Stile

- Preferire slide ariose, con molto spazio bianco.
- Usare titoli grandi ma non eccessivi nelle slide interne.
- Usare grigio per titoli di sezione secondari e nero per contenuto principale.
- Usare teal/azzurro per highlight, label, barre decorative e parole chiave.
- Evidenziare solo poche parole chiave per slide.
- Evitare paragrafi troppo lunghi.
- Quando si usano bullet, raggrupparli sotto macro-titoli chiari.
- Per contenuti C-level, collegare sempre elementi tecnici a benefici, rischi, tempi o economics.

## Cosa Non Fare

- Non salvare nuovi deliverable in `docs/ui/`.
- Non usare queste immagini come contenuto finale rasterizzato se è possibile creare elementi PowerPoint modificabili.
- Non copiare importi, date, nomi cliente o dettagli progettuali dalle reference.
- Non sovraccaricare le slide con testo piccolo.
- Non introdurre decorazioni non coerenti con il linguaggio visuale della reference.

## Aggiornamento Reference

Questa cartella può cambiare nel tempo.

Prima di creare una nuova presentazione, rileggere sempre il contenuto aggiornato di `docs/ui/`, elencare i file disponibili e considerare anche eventuali reference aggiunte dopo l'ultimo aggiornamento di questo README.
