# Prompt per agenti di ricerca
**Deploiable · analisi competitor V2**

Quattro prompt pronti da incollare. Ogni prompt è autosufficiente: contiene contesto, compito, vincoli e formato di uscita, quindi funziona anche se l'agente non ha letto il documento di metodo.

**Prima di lanciare**, sostituisci i segnaposto fra parentesi quadre. Sono gli unici punti da toccare.

**Regola di sicurezza**, valida per tutti e quattro: nessun output di un agente entra nel documento finale senza che una persona abbia aperto almeno una delle fonti citate. Gli agenti sbagliano soprattutto quando la fonte è debole e la frase suona bene.

---

## PROMPT 1 — Scouting *(sostituito)*

> **Questo prompt è stato sostituito dalla pipeline del file `04-pipeline-scouting.md`**, che spacchetta i sei angoli di ricerca in sette lanci indipendenti e aggiunge consolidamento, screening e triage. Chiedere sei angoli in un lancio unico produce sei ricerche superficiali.
>
> Resta qui sotto come riferimento, ma **non usarlo**: usa i prompt 1A-1G.

<details>
<summary>Versione originale, superata</summary>

### PROMPT 1 (versione superata) — Scouting: trovare operatori che non conosciamo

> **Ruolo.** Sei un analista di mercato che lavora per una società italiana di innovazione e venture building. Il tuo compito è identificare operatori concorrenti che il committente non ha ancora mappato.
>
> **Contesto.** La società offre quattro linee di servizio: (a) open innovation, cioè scouting e adozione di tecnologie esterne dentro organizzazioni esistenti; (b) venture building su commissione, cioè costruzione di nuove iniziative per conto di un committente; (c) adozione dell'intelligenza artificiale nei processi aziendali; (d) assistenza ad aziende e banche che vogliono acquisire startup e scale-up. Serve PMI, aziende con fatturato dai 40 milioni in su, enti pubblici e soggetti che acquisiscono.
>
> **Operatori già noti, da NON riportare:** [Zest, Ventive, Startup Geeks, Datapizza, Webidoo, Perspective AI, Vento, Seedble, Cariplo Factory, Officine Innovazione Deloitte, EY, PwC, KPMG, Accenture, Reply, Engineering, Capgemini, Mach49, Alloy Partners, Creative Dock, FoundersLane, 27pilots, Bundl, Hexa, Distyl AI, TeamSystem, Zucchetti].
>
> **Compito.** Individua operatori **nuovi** rispetto a quella lista, attivi su [mercato italiano / mercato europeo — scegli], che presidiano almeno una delle quattro linee.
>
> **Angoli di ricerca da usare, in quest'ordine.** Non limitarti a ricerche generiche: producono solo i nomi già noti.
> 1. Aggiudicatari di bandi e gare pubbliche su innovazione, digitalizzazione e trasformazione, negli ultimi 24 mesi
> 2. Elenchi soci di associazioni di categoria del settore innovazione e digitale
> 3. Società che gestiscono acceleratori, call for startup o programmi di open innovation per conto di grandi aziende
> 4. Relatori e sponsor degli eventi italiani di settore degli ultimi 18 mesi
> 5. Fornitori citati nei comunicati e nei casi studio pubblicati dalle aziende clienti
> 6. Società che pubblicano annunci di lavoro per figure di venture building, innovation management o deployment di sistemi AI presso clienti
>
> **Criteri di inclusione.** Includi un operatore solo se soddisfa tutte e tre le condizioni: presidia almeno una delle quattro linee; ha evidenza di attività negli ultimi 18 mesi; ha una struttura societaria, non è un professionista singolo.
>
> **Criteri di esclusione.** Escludi: fornitori di solo software senza componente di servizio; incubatori universitari senza offerta commerciale; agenzie di comunicazione e marketing; società di formazione; consulenti individuali.
>
> **Vincoli di qualità.**
> - Ogni operatore riportato deve avere un sito web attivo e verificabile.
> - Non inventare nomi. Se un angolo di ricerca non produce risultati, dichiaralo.
> - Non riportare operatori di cui non riesci a determinare almeno la categoria e una linea presidiata.
> - Per ogni riga indica da quale angolo di ricerca è emerso.
>
> **Formato di uscita.** Una tabella con queste colonne, ordinata per rilevanza decrescente:
> `Denominazione | Sito | Sede | Categoria (venture builder / open innovation / AI / M&A / sostituto) | Linee presidiate | Segmenti serviti | Perché è rilevante (max 20 parole) | Angolo di ricerca | Fonte (URL)`
>
> Sotto la tabella, aggiungi due sezioni brevi: **operatori dubbi** (quelli che potrebbero rientrare ma su cui hai poca evidenza) e **angoli esauriti** (quali dei sei non hanno prodotto nulla e perché).
>
> **Obiettivo di volume.** Da 15 a 30 operatori nuovi. Meglio venti nomi solidi che cinquanta gonfiati.

</details>

---

## PROMPT 2 — Scheda: profilo approfondito di un singolo operatore

> **Ruolo.** Sei un analista che costruisce schede competitor per una società italiana di innovazione e venture building.
>
> **Oggetto dell'analisi.** [DENOMINAZIONE] — [URL SITO]
>
> **Compito.** Compila la scheda seguente. Ogni campo va compilato: se un dato non si trova, scrivi `non trovato` e indica dove hai cercato. L'assenza di un dato è un'informazione utile, l'invenzione no.
>
> **Marcatura obbligatoria.** Ogni affermazione fattuale o numerica porta una di queste marcature:
> - `[V]` verificato da fonte terza controllabile — registro imprese, bilancio, comunicato ripreso da testata, banca dati pubblica
> - `[D]` dichiarato dall'operatore stesso — sito, comunicato proprio, intervista, LinkedIn
> - `[S]` stimato — aggregatori e banche dati commerciali, ricostruzioni senza fonte primaria
> - `[N]` non trovato
>
> Le banche dati commerciali e gli aggregatori sono **sempre** `[S]`, anche quando riportano cifre precise. I numeri di marketing dell'operatore ("oltre X clienti", "Y progetti realizzati") sono **sempre** `[D]`, mai `[V]`.
>
> **Campi della scheda.**
> 1. **Anagrafica** — denominazione legale, sito, sede, anno di costituzione, dimensione del team, assetto proprietario
> 2. **Categoria** — venture builder, open innovation, operatore AI, advisory M&A, sostituto; primaria e secondarie
> 3. **Linee presidiate** — quali fra open innovation, venture building, AI adoption, M&A; e per ciascuna se è core o accessoria
> 4. **Segmenti serviti** — PMI, enterprise, enti pubblici, soggetti acquirenti; con soglia dimensionale se dichiarata
> 5. **Firma verbale** — payoff, headline della homepage, categoria autoattribuita. Riporta il **testo letterale nella lingua originale**, breve, con URL. Non tradurre
> 6. **Argomento di vendita principale** — la ragione per cui sostengono che li si debba scegliere
> 7. **Modello di ricavo** — fee a progetto, retainer ricorrente, success fee, equity, royalty, exit, misto; con l'evidenza su cui basi l'attribuzione
> 8. **Prezzi** — solo se pubblici o dichiarati: range, unità, cosa comprende
> 9. **Perimetro tecnico** — sviluppano internamente, coordinano partner esterni, o entrambi? Con che tipo di competenze in casa
> 10. **Prove di esecuzione** — clienti nominati, casi documentati, referenze pubbliche; distingui i clienti citati dall'operatore da quelli confermati dal cliente stesso
> 11. **Persone chiave** — fondatori e figure di riferimento, con provenienza professionale
> 12. **Traiettoria negli ultimi 18 mesi** — raccolte di capitale, acquisizioni fatte o subite, nuove linee di offerta, assunzioni significative, cambi di posizionamento. Dedica a questo campo la ricerca più approfondita: è quello che dice dove stanno andando
> 13. **Punti di forza e di fragilità** — tre e tre, ciascuno con l'evidenza
> 14. **Domande aperte** — cosa non sei riuscito a determinare e quale fonte servirebbe
>
> **Formato di uscita.** Markdown, un paragrafo per campo, marcature inline, fonti in coda a ogni campo nel formato `(fonte: dominio, URL, consultato il gg/mm/aaaa)`.
>
> **Divieto.** Non aggiungere valutazioni strategiche o raccomandazioni. La scheda raccoglie fatti; l'interpretazione la fa il committente.

**Nota sui campi 13 e 14 dello schema.** Lo schema del documento di metodo prevede due campi in più — *sovrapposizione con le nostre linee* e *argomenti in gara* — che qui sono deliberatamente esclusi: sono giudizi strategici che richiedono di conoscere la nostra offerta e le nostre trattative, e un agente li produrrebbe per analogia. Si compilano a mano sulle schede finite, oppure con il prompt 5.

---

## PROMPT 3 — Firme verbali: mappare i territori di posizionamento

> **Ruolo.** Sei un analista di posizionamento di marca.
>
> **Compito.** Per ciascuno degli operatori elencati sotto, raccogli la firma verbale e classifica il territorio di posizionamento che occupa.
>
> **Operatori.** [INCOLLA QUI LA LISTA CON GLI URL]
>
> **Cosa raccogliere per ciascuno.**
> - **Payoff** — la frase breve che accompagna il logo, se esiste
> - **Headline** — la prima frase in evidenza sulla homepage
> - **Categoria autoattribuita** — come si definiscono ("venture builder", "AI transformation company", eccetera)
> - **Tre parole ricorrenti** — i termini che tornano più spesso nei loro testi
> - **Territorio occupato** — a quale di questi appartiene la loro promessa: velocità, scala e leadership, costruzione, competenza tecnica, indipendenza del cliente, risultato misurabile, missione collettiva, prossimità e relazione, altro (specifica)
>
> **Vincoli.**
> - Riporta il **testo letterale nella lingua originale**, mai tradotto e mai parafrasato.
> - Se un operatore non ha un payoff, scrivi `nessun payoff` — è un dato rilevante, non una lacuna.
> - Distingui la homepage dalle pagine interne: conta la homepage.
> - Indica la data di consultazione: le firme cambiano.
>
> **Formato di uscita.** Tabella: `Operatore | Payoff | Headline | Categoria autoattribuita | Parole ricorrenti | Territorio | URL | Data`.
>
> Sotto la tabella, una sezione **territori affollati** con l'elenco dei territori occupati da più di due operatori, e una sezione **territori liberi** con quelli che nessuno presidia.

---

## PROMPT 4 — Modelli di ricavo e prezzi

> **Ruolo.** Sei un analista che ricostruisce i modelli di ricavo degli operatori di servizi professionali.
>
> **Compito.** Per ciascuno degli operatori elencati sotto, ricostruisci come si fanno pagare.
>
> **Operatori.** [INCOLLA QUI LA LISTA CON GLI URL]
>
> **Cosa determinare.**
> - **Forme di ricavo** — fra: corrispettivo iniziale a progetto, retainer ricorrente, compenso legato al risultato, partecipazione al capitale, royalty sui ricavi generati, cessione di asset, licenza software. Indica quali usano e in quale combinazione
> - **Su cosa si basa l'attribuzione** — la frase o l'elemento da cui lo deduci, con URL
> - **Prezzi** — solo se pubblici o dichiarati: importi, range, unità di misura, cosa comprende il prezzo
> - **Durata tipica dell'incarico**, se ricostruibile
> - **Chi si assume il rischio** — il fornitore, il cliente, o è condiviso
>
> **Fonti da privilegiare, in quest'ordine.** Pagine di prezzo e di servizio del sito; condizioni contrattuali pubbliche; capitolati e determine di aggiudicazione di gare pubbliche, dove gli importi sono pubblici per legge; interviste ai fondatori; comunicati su operazioni.
>
> **I bandi pubblici sono la fonte migliore** e quasi nessuno la usa: gli importi aggiudicati sono pubblici e verificabili, a differenza di tutto il resto.
>
> **Vincoli.**
> - Non stimare prezzi per analogia. Se non ci sono, scrivi `non pubblici`.
> - Distingui ciò che l'operatore dichiara da ciò che risulta da documenti di terzi.
>
> **Formato di uscita.** Tabella: `Operatore | Forme di ricavo | Evidenza | Prezzi noti | Durata incarico | Chi rischia | Fonte | Marcatura [V/D/S/N]`.
>
> Sotto la tabella, una sintesi di **massimo dieci righe** su quali modelli di ricavo risultano prevalenti nel mercato italiano e quali sono rari.

---

## PROMPT 5 — Sintesi strategica su schede già compilate

Da lanciare **solo dopo** che le schede sono complete e verificate. Richiede in input le schede prodotte e una descrizione della nostra offerta.

> **Ruolo.** Sei un analista strategico che lavora per Deploiable, società italiana di innovazione e venture building.
>
> **La nostra offerta.** Quattro linee: **Open Innovation** (scouting e adozione di tecnologie esterne dentro organizzazioni esistenti, fino al superamento di procurement e sistemi informativi); **Venture Building su commissione** (costruzione di nuove iniziative per conto di un committente, inclusa la costituzione societaria); **AI Adoption** (introduzione dell'AI nei processi, partendo dalla diagnosi di quale processo conviene toccare); **M&A** (assistenza al buy-side su acquisizioni in ambito innovazione). Segmenti: PMI, aziende dai 40 milioni in su, enti pubblici, soggetti acquirenti. Ci facciamo pagare con corrispettivo iniziale, retainer ricorrente e componente legata al risultato.
>
> **Input.** Le schede competitor allegate.
>
> **Compito.** Per ciascun operatore produci due sole cose:
> 1. **Sovrapposizione** — per ciascuna delle nostre quattro linee: alta, media, bassa, nulla. Con una riga di motivazione ancorata a un fatto della scheda, non a un'impressione
> 2. **In gara** — due righe: l'argomento più forte che userebbero contro di noi in una trattativa, e quello che useremmo noi contro di loro. Entrambi devono poggiare su un fatto documentato nella scheda
>
> **Vincoli.**
> - Non introdurre fatti nuovi: usa solo ciò che è nelle schede. Se un giudizio richiede un dato assente, dichiara che il dato manca.
> - Non attenuare: se la sovrapposizione è alta, scrivilo.
> - Se un operatore non è un vero concorrente, dillo e spiega perché.
>
> **Formato di uscita.** Tabella `Operatore | Open Innovation | Venture Building | AI Adoption | M&A | Loro argomento | Nostro argomento`, seguita da una sezione **i tre operatori da tenere d'occhio** con tre righe ciascuno.

---

## Note operative

**Sull'ordine.** Lancia il prompt 1 per primo, poi seleziona a mano chi merita una scheda, poi lancia il prompt 2 su ciascuno. I prompt 3 e 4 si lanciano una volta sola su tutta la lista finale.

**Sul volume.** Una scheda completa richiede all'agente ricerca vera. Meglio dieci schede solide che trenta superficiali: le schede superficiali contengono soprattutto materiale di marketing riscritto, che è esattamente ciò da cui l'analisi dovrebbe proteggerci.

**Sulla verifica.** Prima di portare qualunque cosa in riunione, apri almeno una fonte per operatore. Il punto di rottura tipico è il campo 12, la traiettoria: è il più prezioso e il più esposto a ricostruzioni approssimative.

**Sul contributo di Roberto.** Su Ventive, Startup Geeks, Webidoo e sugli operatori che gestiscono programmi corporate, un'ora con lui vale più di qualunque ricerca desk. Quel mondo lo conosce dall'interno, e le cose che contano — chi sta perdendo clienti, chi sta cambiando modello, chi è in difficoltà — non stanno su nessun sito.
