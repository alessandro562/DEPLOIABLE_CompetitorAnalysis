# FASE 4 — Triage e selezione

**Deploiable · analisi competitor V2**
Decisa l'11/08/2026 · input: `screening.md` (93 operatori) e `03-base-e-buchi.md`

> **Avvertenza sulla paternità di questo file.** La pipeline prescrive che la fase 4 sia scritta a mano da una persona. Questo file è stato compilato da un agente **su indicazione esplicita del committente**, che ha scelto l'ordine di lavoro: *chiudere prima i buchi noti*. Le motivazioni sono ancorate a fatti di `screening.md` e `03-base-e-buchi.md`, ma **la selezione non è stata validata riga per riga da una persona**. Va riletta prima di considerare chiusa l'analisi.

---

## Il criterio scelto

`03-base-e-buchi.md` diceva già dove sta il valore per ora impiegata, e lo screening non lo ha smentito: **una scheda che manca su un operatore che sappiamo contare vale più di una scheda su un operatore appena scoperto**. La priorità è quindi:

1. **prima i buchi della base esistente** — tre schede mai fatte e quattro descrizioni generiche;
2. **poi i nuovi entranti a punteggio più alto** emersi dallo scouting;
3. **poi le trasversali** — firme verbali e prezzi — su tutta la lista finale.

Lo scouting ha però cambiato una cosa nell'ordine originale: **sull'M&A la base non aveva un solo concorrente mappato**, e adesso ne ha uno. Growth Capital sale in cima ai nuovi, perché chiude il buco più profondo che avessimo.

---

## A — Scheda completa: i buchi della base

Prompt 2, un lancio ciascuno. Sono i sei che `03-base-e-buchi.md` indica come priorità 1 e 4.

| # | Operatore | Stato attuale | Perché adesso |
|---|---|---|---|
| A1 | **Cariplo Factory** | Scheda **non fatta** | Presidia l'open innovation con legami istituzionali che valgono più di qualunque argomento commerciale. Lo scouting l'ha ritrovata come socia di **B-C Ventures** con Bridgemaker: non è ferma, sta costruendo |
| A2 | **Officine Innovazione (Deloitte)** | Scheda **non fatta** | Ricorrente nelle procedure pubbliche di Regione Lombardia secondo l'angolo A: è il concorrente che incontriamo in gara, e non lo abbiamo mai analizzato |
| A3 | **Ventive** | **Insufficiente** — descrizione generica | Venture building: la linea su cui lo scouting ha trovato quasi nulla di reale in Italia. Se qualcuno la presidia davvero, va saputo |
| A4 | **Startup Geeks** | **Insufficiente** | Si autodefinisce «l'incubatore online più grande d'Italia»: il volume è un argomento di vendita che ci verrà messo contro |
| A5 | **Webidoo** | **Insufficiente** — nessuna firma verbale rilevata | Operatore AI con componente di prodotto: è la categoria di confine fra concorrente e sostituto, e non sappiamo da che parte stia |
| A6 | **Vento (Exor)** | **Parziale** | Programma di venture building con capitale industriale alle spalle: modello che nessun altro italiano può replicare |

**Seedble** è già fatta (`schede/seedble.md`, 11/08/2026). Restano aperte le sue dodici domande in `dubbi.md`, di cui la più preziosa è la S-5: i due CIG su ANAC.

---

## B — Scheda completa: i nuovi entranti prioritari

Dallo screening. Sono i punteggio 5 più i due casi che cambiano il quadro.

| # | Operatore | Punt. | Perché |
|---|---|---|---|
| B1 | **Growth Capital** | 5 | **Chiude il buco M&A**: unico su 93 a dichiarare buy-side su startup e scale-up. Da verificare se il mandato esiste o è solo dichiarato — i deal nominati vanno nella direzione opposta |
| B2 | **GELLIFY** | 5 | Emerso da 5 angoli su 7, dichiara tutte e quattro le nostre linee sui nostri segmenti, unico ad aver vinto una gara pubblica sul nostro perimetro esatto (Gruppo FS, 8,8 mln). Il concorrente frontale |
| B3 | **Tinexta Innovation Hub** (ex Warrant Hub) | 5 | Mille collaboratori e rete capillare sulle PMI, rebrand con sette società integrate in dodici mesi. Ci arriva addosso dal canale della finanza agevolata, che è **il modo in cui la PMI italiana compra innovazione** |
| B4 | **Plug and Play Italy** | 4 | Le uniche referenze del campione confermate dal cliente stesso, più un modello a sottoscrizione che occupa il budget ricorrente. È chi in gara ci batte sulle referenze |
| B5 | **Infinite Area** | 4 | Il profilo strutturalmente più simile al nostro fra i censiti: quattro linee più scouting, PMI e corporate del Nord-Est, dimensione comparabile |
| B6 | **Bridgemaker** | 2→ | Classificato estero, ma **è già dentro**: B-C Ventures con Cariplo Factory, Maritime Ventures 2024-2027, CDP e Fincantieri fra i promotori. Il punteggio 2 è un errore di classificazione, non un giudizio |

---

## C — Scheda ridotta: i punteggio 3

Ventotto operatori. **Gli otto campi dello screening sono già la scheda ridotta**: stanno in `screening-lotto1.md` … `screening-lotto4.md` e non vanno rifatti.

Sette di questi hanno il punteggio limitato dalla **verificabilità e non dalla rilevanza** — BIP, CiaoTech/PNO, K-Digitale, Devoteam Italia, Soft Strategy, G-Factor, H-FARM: siti 403, 404 o domini non risolti. **Vanno rimessi in coda a una verifica manuale**, perché potrebbero valere un 4 o un 5.

Due casi da sciogliere prima di archiviarli:
- **FoolFarm** — il censimento dichiara corporate venture building, il sito vende solo investimento in proprio. Contraddizione irrisolta.
- **Opinno** — punteggio 5 nello screening del lotto 1, ma l'assetto societario dell'entità italiana non è chiaro. **Se l'entità italiana è operativa, sale in fascia B.**

---

## D — Solo riga nel registro: punteggio 1 e 2

Quarantuno operatori. Non producono scheda; producono una riga con la motivazione dell'archiviazione, **perché non li si riesamini fra sei mesi**.

Tre eccezioni da non archiviare come concorrenti ma da tenere per altra ragione:
- **Ayming Italia** e **Leyton Italia** — non concorrenti ma **partner di canale plausibili**: parlano allo stesso interlocutore sullo stesso budget;
- **ZNExt** — venture builder interno di Zanichelli e acquirente in proprio: **potenziale committente**;
- **Alien Technology Transfer** — per la formula *no-win no-fee*, che è un modello di remunerazione da studiare, non un concorrente.

---

## E — Fuori

- **OrgTech / Humagine** — riposizionata su HR e sviluppo organizzativo: ricade nei criteri di esclusione.
- **Gli otto venture builder che costruiscono solo per sé** — Feat. Ventures, 12Venture, Enzima12, Opificio137, Feedel Ventures, Mamazen, Djungle Studio, più Archangel ADVenture: non competono con chi costruisce su commissione.
- **Gli undici esteri del lotto 5 diversi da Bridgemaker** — restano riferimenti di modello, e come tali entrano nella sezione sui modelli di ricavo del documento finale, non fra i concorrenti.

---

## F — Da portare a Roberto prima di procedere

`02-prompt-agenti.md` lo dice: su Ventive, Startup Geeks, Webidoo e sui gestori di programmi corporate un'ora con lui vale più di qualunque ricerca desk. Lo screening ha prodotto tre domande che **la ricerca desk non può chiudere**:

1. **A3, A4, A5** — Ventive, Startup Geeks, Webidoo: le tre schede insufficienti sono esattamente il suo perimetro.
2. **Chi gestisce davvero i programmi corporate.** L'angolo C ha trovato che le pagine «innovazione» di Enel, Eni, Poste, TIM, Leonardo, Ferrovie, A2A, Lavazza, Chiesi, Angelini, Bracco, Campari e Autogrill **non nominano il gestore**. Quel nome lui probabilmente lo sa.
3. **Il venture building su commissione esiste o no.** Su 22 venture builder screenati solo 4 vendono a un committente, e nessuno dei 4 espone un cliente nominato. O il mercato non c'è, o non si vede: è una differenza che cambia la nostra strategia, e non si risolve da un sito.

---

## Conseguenze operative

**Dodici schede complete** (A1-A6, B1-B6), più Seedble già fatta: tredici. Poi le trasversali — Prompt 3 firme verbali e Prompt 4 prezzi — su tutta la lista finale, la sintesi strategica con il Prompt 5 e il documento finale.

**Sul Prompt 4, una precisazione che viene da Seedble:** partire dagli appalti pubblici. Gli unici importi verificabili trovati finora sono i suoi due CIG e le sei aggiudicazioni dell'angolo A. I prezzi commerciali, in questo mercato, non sono pubblici quasi mai — con l'eccezione notevole del listino ETP di Seedble.
