# Verifica avversariale di `ANALISI-COMPETITOR-V2.md`

**Data:** 11/08/2026 · **Nessuna ricerca web condotta.** La verifica è fatta solo confrontando il documento finale con i file interni da cui dichiara di derivare.

## Metodo

Il presupposto di lavoro è stato che il documento contenga errori. Ho cercato, in quest'ordine: fatti non rintracciabili in nessuna fonte; marcature di affidabilità cadute o innalzate; incoerenze numeriche fra documento e fonti o interne al documento; giudizi presentati come fatti; attenuazioni o rafforzamenti rispetto alla cautela della fonte; citazioni alterate.

**Cosa ho letto per intero:** `ANALISI-COMPETITOR-V2.md`; `scouting/screening.md`; `firme-verbali.md`; `modelli-di-ricavo-e-prezzi.md`; `sintesi-strategica.md`; `dati/registro.csv` (letto strutturalmente, 14 righe × 34 colonne); l'intestazione di `scouting/selezione.md`, `scouting/consolidato.md`, `dubbi.md`, `01-metodo-e-schema.md`, `03-base-e-buchi.md`.
**Cosa ho letto in modo mirato:** tutte e tredici le schede in `schede/`, interrogate per ciascun numero citato nel documento; `scouting/screening-lotto3.md` e `screening-lotto4.md`; `scouting/b-osservatori.md`; `dubbi.md` per le voci citate in §7.3.

**Campionamento.** Ho controllato **oltre 60 affermazioni numeriche o fattuali distinte**, distribuite su tutte e sette le sezioni, con questo criterio:
- **censimento completo** (non campione) dei numeri di struttura: 93 / 46 / 36+12 / 77 / 4.397.801 € / 13 schede / 24 e 19 a punteggio 4-5 / 28 e 41 / 120 righe grezze / 13×34 colonne;
- **censimento completo** della tabella §4.4 (dieci operatori: numero contratti e importi ricontrollati e risommati contro `modelli-di-ricavo-e-prezzi.md` §C.1);
- **censimento completo** dei gradi di sovrapposizione: 52 celle della tabella 3.1 e 76 celle della tabella 3.2, confrontate una a una con `sintesi-strategica.md` Tabelle A e B;
- **censimento completo** dei dati di bilancio e organico delle tredici righe della §2 (13 su 13 verificati sulla scheda corrispondente, marcatura inclusa);
- **campione mirato** sulle citazioni testuali di §1.3, §4, §5 (dieci payoff e clausole a confronto letterale con `firme-verbali.md` e con il campo 5 delle schede);
- **campione mirato** sulle cinque conclusioni operative: per ciascuna ho risalito ogni fatto citato alla fonte e alla sua marcatura;
- **campione mirato** su §7: le sei incertezze U-1…U-6 e le tredici voci di §7.3 confrontate con `dubbi.md`.

---

## Tabella dei rilievi

| # | Gravità | Sezione | Che cosa dice il documento | Che cosa dice la fonte | Fonte | Correzione proposta |
|---|---|---|---|---|---|---|
| **1** | **alta** | §3.1, «Lettura in una riga» (riga 158) | «Su tredici schede: **sei hanno Open Innovation alta o media**» | La tabella 3.1 **dello stesso documento** assegna Open Innovation **alta a cinque** operatori (GELLIFY, Seedble, Cariplo Factory, Officine Innovazione, Plug and Play) e **media a tre** (Growth Capital, Infinite Area, Startup Geeks): **otto, non sei**. Il conteggio coincide cella per cella con `sintesi-strategica.md` Tabella A, che quindi non è la causa dell'errore | Interna al documento; `sintesi-strategica.md` righe 31-43 | Correggere in «**otto hanno Open Innovation alta o media**». È l'unica riga di sintesi della tabella più importante del documento, e sottostima del 25% l'affollamento sulla nostra prima linea. Gli altri tre conteggi della stessa riga (quattro su VB, cinque su AI, uno su M&A) sono **corretti** |
| **2** | **media** | §7.1 U-1 e §7.4 punto 1 | «**i cinque contratti sopra i 100.000 €** (Plug and Play 425.186; Nana Bianca 220.000; Almacube 139.500 **e 136.400**; GELLIFY 137.705; CRIT 138.200)» | Gli importi elencati sono **sei**, non cinque. E nella fonte i contratti sopra i 100.000 € sono almeno **dodici**: Plug and Play 425.186 / 139.000 / 114.755; Almacube 139.500 / 136.400 / 118.500; GELLIFY 137.705 / 122.500 / 100.000; Nana Bianca 220.000; CRIT 138.200 / 111.940. L'errore è ereditato da `modelli-di-ricavo-e-prezzi.md` (riga 209), ma qui diventa un **ordine di priorità operativo** | `modelli-di-ricavo-e-prezzi.md` §C.1 e §Limiti | Riscrivere come «i **sei** contratti sopra i 130.000 €» oppure «i **dodici** contratti sopra i 100.000 €», scegliendo la soglia. Così com'è, la prima azione della lista §7.4 è dimensionata su un numero sbagliato |
| **3** | **media** | §6, conclusione 1, «Che cosa la falsificherebbe» | «Trovare **almeno tre operatori italiani con prezzo pubblico su servizi di innovazione a corporate** (**oggi zero**)» | Il documento stesso, §4.3 e §1.3, dice che **Seedble** espone il prezzo di un servizio di innovazione (ETP 3.000 € + IVA) e `dati/registro.csv` gli attribuisce fra i segmenti «Corporate/enterprise, PMI, PA». La fonte dice «4 su 36 espongono un listino, di questi **solo Seedble** espone il prezzo di un servizio di innovazione vero»: uno, non zero | `modelli-di-ricavo-e-prezzi.md` §Sintesi punto 8; `dati/registro.csv` riga Seedble | Sostituire «oggi zero» con «**oggi uno, Seedble**», oppure qualificare esplicitamente «prezzo pubblico su servizi venduti a corporate da 40 mln in su», che è la lettura che rende vera la frase — ma va scritta, non lasciata implicita |
| **4** | **media** | §2, riga 6 (Webidoo) | «**25 mln $ raccolti nel 2026** e **18 mln di ricavi 2025** `[D]`» | La scheda e `sintesi-strategica.md` dicono **«ricavi 18 milioni di dollari»**. Nel documento la valuta cade solo sul secondo numero, accanto a uno che porta il «$»: la lettura naturale è 18 milioni di **euro**, cioè circa il 15% in più | `schede/webidoo.md` §12 e §13; `sintesi-strategica.md` riga 36 | Scrivere «**18 mln $ di ricavi 2025**». La stessa correzione va fatta ovunque il numero ricompaia |
| **5** | **media** | §6, conclusione 5, «Il fatto» | «Stessa lettura per **Ayming** e **Leyton** (**3.000 imprese italiane servite** `[D]`)» | Il dato dei **3.000** è di **Leyton Italia** soltanto («3.000+ aziende servite in Italia, oltre 1.000 consulenti»). **Ayming Italia** dichiara numeri diversi e non italiani: «1.600 colleghi nel mondo, **15.000+ clienti**, 14 paesi». La parentesi, posta dopo entrambi i nomi, attribuisce a due operatori un numero che ne riguarda uno | `scouting/screening-lotto4.md` righe 21-22; `scouting/consolidato.md` riga 138 | Scrivere «Ayming e **Leyton** (quest'ultima con 3.000+ imprese italiane servite `[D]`)» |
| **6** | **media** | §1.2, riga categoria **B**, colonna «Quanti — **numero documentato**» | «**36 screenati** (18 gestori di programmi e acceleratori + 18 consulenze OI censite dagli osservatori)» | Il 36 è la somma dei lotti 1 e 2, cioè esattamente ciò che §1.1 del documento definisce «**corrispondenza di lotto**, che è **un giudizio di questo documento** e non un dato delle fonti». Nessun file conta gli operatori per categoria A-F — cosa che il documento dichiara correttamente in §1.1 e poi contraddice in tabella. (Il 22 della categoria A regge invece: `screening.md` conta esplicitamente «22 venture builder e startup studio») | Interna al documento, §1.1 contro §1.2; `scouting/screening.md` righe 10-14 | Spostare «36» dalla colonna «numero documentato» alla colonna «corrispondenza di lotto *(giudizio)*», o marcarlo *(giudizio)* in cella. È l'unico punto in cui il documento viola la propria regola di separazione fatti/giudizi |
| **7** | **bassa** | §7.2, riga B-1/B-2 | «il rapporto dichiara **503 organizzazioni e 103 consulenti OI**, le pagine ne mostrano **58** → **~84 operatori censiti non raggiungibili**» | L'84 non discende da 103−58 (=45). Nella fonte è la somma di **due** scarti: consulenze OI da 58 a 103 (+45) **e startup studio/venture builder da 36 a 75** (+39). La compressione ha eliminato la seconda metà, lasciando un'aritmetica che non torna | `scouting/b-osservatori.md` riga 109; `scouting/consolidato.md` riga 335 | Aggiungere «e startup studio/venture builder da 36 a 75», oppure togliere la freccia e il calcolo implicito |
| **8** | **bassa** | §2, riga 6 (Webidoo) | Il round da 25 mln $ è marcato **`[D]`** | La scheda marca il closing di maggio 2026 **`[V]`** (evento al Nasdaq, ripresa di stampa) e la classificazione CB Insights **`[V/S]`**. La marcatura del documento è **più prudente** del dovuto, non meno: non crea rischio, ma è comunque una marcatura sbagliata | `schede/webidoo.md` §12 | Portare a `[V]` il round e lasciare `[D]` ai soli ricavi |
| **9** | **bassa** | §6, conclusione 2, «La mossa» (b) | «Il taglio d'ingresso è alla nostra portata: **10.000-140.000 €** il tipico» — **senza marcatura** | Il dato è `[S]` (aggregatore ANAC ripubblicato) e il documento stesso, in §4.4 e in U-1, dice che su tutti i 77 contratti **mancano stazione appaltante e oggetto** e che è «il buco più serio». Nella conclusione la cautela cade e il numero diventa una base d'azione nuda | `modelli-di-ricavo-e-prezzi.md` §Sintesi punto 7 e §Limiti punto 5; `ANALISI-COMPETITOR-V2.md` §4.4 | Aggiungere `[S]` e il richiamo «(oggetto dei contratti ignoto — U-1)» |
| **10** | **bassa** | «Come si legge questo documento», legenda | «`[S]` aggregatore o banca dati ripubblicata» | Il metodo definisce «`[S]` **stimato** — aggregatori di dati, banche dati commerciali, **ricostruzioni giornalistiche senza fonte primaria**». La legenda del documento perde la parola «stimato» e l'intera terza fattispecie, indebolendo il significato della marcatura più usata nel documento | `01-metodo-e-schema.md` §4.1 | Riportare la definizione integrale del metodo |
| **11** | **bassa** | §5.2, riga «Indipendenza del cliente» | Bridgemaker «ci arriva vicino (**«a business that runs without us»**)» | La citazione integrale è «**From the first Wargame to a business that runs without us**». Il troncamento non altera il senso, ma è un taglio senza segno di omissione in una sezione che dichiara «payoff e headline **letterali, mai tradotti**» | `firme-verbali.md` riga 112 | Usare i puntini di sospensione o la frase intera |

---

## Verifiche superate

Elenco di ciò che ho controllato e che **non** ha prodotto rilievi. Serve a sapere cosa è stato guardato.

**Numeri di struttura — tutti corretti.** 93 operatori su 5 lotti (18+18+22+23+12 = 93); distribuzione per punteggio 4/20/28/21/20 e quote 4%/22%/30%/23%/22%; 81 in Italia + 12 esteri; 46 firme verbali = 27 Tabella A + 19 Tabella B; 36 italiani + 12 esteri sui modelli di ricavo; 13 schede; 28 a punteggio 3 e 41 a punteggio 1-2; 120 righe grezze di scouting; `dati/registro.csv` esattamente 13 righe × 34 colonne; «190+ voci» in `dubbi.md` è conservativo per difetto (le voci sono oltre 200).

**La nota aritmetica di §3.2 è corretta e non banale.** «Gli operatori a punteggio 4-5 sono 24; cinque hanno già la scheda; restano 19» — verificato contro `screening.md` (4+20) e contro l'elenco dei tredici; la tabella 3.2 contiene esattamente 19 righe.

**§4.4 — la tabella dei contratti pubblici regge alla risomma.** I dieci operatori sommano **esattamente 77 contratti** (33+14+3+6+6+5+5+2+2+1) e **esattamente 4.397.801 €**. Ogni importo, ogni «contratto più alto» e ogni data coincidono con `modelli-di-ricavo-e-prezzi.md` §C.1. La marcatura collettiva `[S]` è corretta e la distinzione fra `[S]` (aggregatore) e `[V]` (dato negativo Regione Lombardia, gare con importo pubblicato) è tenuta con precisione.

**L'avvertenza sui 178 operatori con `aggiudicatario = NO`** è riportata fedelmente, compresa la lettura corretta («elenco di invitati, non una gara persa da tutti»): è il punto in cui il documento avrebbe potuto rafforzare un dato negativo, e non lo fa.

**Le 52 celle della tabella 3.1 coincidono una a una con `sintesi-strategica.md` Tabella A**, marcature `[N]` incluse. Lo stesso vale per le **76 celle della tabella 3.2** contro la Tabella B, e la dichiarazione «ogni cella è marcata `da screening`… non vanno lette come righe dello stesso valore probatorio» è più esplicita della fonte, non meno.

**I tredici profili di §2 — dati economici e organici, marcatura inclusa.** Verificati sulla scheda corrispondente e tutti corretti: Seedble 781.551 € (2021) `[S]`; Cariplo Factory 5.607.206 € / 18.065 € / −64,01% `[S]` e 38 imprese `[D]`; Officine Innovazione 12,59 mln / 983mila / 95 dipendenti `[S]` e 20 procedure con zero aggiudicazioni `[V]`; Ventive 610.679 € / −436.499 € `[S]`; Startup Geeks 2.900.349 € / 292.771 € `[S]`; Vento fondo 75 mln `[V]`; GELLIFY 133 dipendenti / 18.565.249 € / 1.006.572 € `[V]` e holding 202.867 € / −216.899 € `[V]`; Growth Capital ~2 mln / 17.245 € / 12 dipendenti camerali contro 26 nominativi `[S]`; Tinexta 156,2 mln / 952 FTE / 29,1→24,0→8,4% / 29→14% / 6,3→2,75 mld, tutti `[V]`; Plug and Play 3.862.817 → 3.821.446 → 3.852.542 `[S]`; Infinite Area 1.507.963 € / −3,6% / 7 dipendenti / ATECO 68.20.02 `[S]`; Bridgemaker BC Ventures ricavi 0 / −13mila / 0 dipendenti `[S]` e fondo PwC-Segenia 30 mln `[V]`. **Nessun `[S]` o `[D]` è stato innalzato a `[V]`** — che era l'errore più grave possibile e non c'è.

**Le referenze di Plug and Play sono corrette, contro l'apparenza.** Il documento cita «Marelli, UniCredit, Nexi, A2A, Amplifon»; `screening.md` (fase 3) dice «Marelli, Nexi, A2A, **Esselunga**». Sembra un errore e non lo è: la scheda completa, prodotta dopo, spiega che le referenze **confermate sul dominio del cliente** sono cinque e che Esselunga sta «in una classe intermedia» perché la dichiarazione del CMO è ospitata su un canale terzo. Il documento segue la fonte più forte e più recente. Corretto anche «16 progetti pilota in 2 anni» `[V]` e il bacino «68-90.000 startup» qualificato come *dichiarato*.

**Citazioni testuali — nessuna traduzione, nessuna alterazione.** Confrontate a campione con `firme-verbali.md` e col campo 5 delle schede: «Ein Teil unserer Vergütung ist an vorab definierte, messbare Ergebnisse gekoppelt» / «Tritt das Ergebnis nicht ein, entfällt dieser Teil» (Bridgemaker); «Wholly funded by Exor…» e «nessuna acquisizione di equity delle startup create, né success fee di alcun tipo» (Vento); «Libérateur d'ambitions» (WILCO); «Future. Faster.» (Zest); «Un equipo de constructores» (Byld); «We try to build the future» (Nana Bianca); «invest alongside our partners … also our own capital into the fund» (whataventure); «Die Digitalberatung für KI-Transformation» (Bridgemaker); «Small businesses now have AI agents» (Webidoo). Tutte letterali. La marcatura `[2M]` sui dati di seconda mano è mantenuta dove serve (Datapizza, 27pilots, Zest, Creative Dock).

**§5 — i conteggi sulle firme tornano tutti.** 9 costruzione / 7 missione collettiva / 4 scala e leadership / 3 risultato misurabile / 3 competenza tecnica; «cinque italiani su ventisette»; 9 senza payoff più Plug and Play `non rilevato`; 7 firme su 46 con primato dichiarato; 8 operatori italiani che firmano in inglese; «innovazione» fra le tre parole ricorrenti di 22 su 46; «0 su 46» sul prezzo nel payoff. Tutti coincidono con `firme-verbali.md`.

**§4 — i dieci modelli di ricavo.** 30 su 36 sul corrispettivo a progetto; 5 su 36 sul ricavo ricorrente; 1 caso italiano `[V]` e 1 estero `[D]` sul compenso a risultato; 1 su 36 sull'equity al posto del corrispettivo; ~8 sull'equity di portafoglio; 2 sulla licenza; **zero** su royalty e cessione di asset; 26 su 36 che incassano a prescindere; «unica clausola di rinuncia trovata su 25 operatori esaminati»; 4 su 36 con listino pubblico. Tutti verificati. I prezzi di §4.3 (Seedble 800/3.000 €; Startup Geeks 24,90/249/44,95 €; Webidoo 86/65 $; Vento 500/230/700/900 €; Plug and Play 200.000/100.000 $) coincidono con le fonti, marcature comprese, e la cautela sul prezzo di Plug and Play («cifre globali in dollari, da intervista non databile, nessun prezzo italiano in euro» `[N]`) è **riportata integralmente**, non attenuata.

**§1.3 — i tre risultati negativi.** N1 (22 venture builder, 4 su commissione, 12 in proprio, nessun cliente committente nominato) coincide con `screening.md` e con `screening-lotto3.md` punto 79. N2 (uno su 93, dodici schede su tredici con M&A nulla o bassa) coincide con `screening.md` e `sintesi-strategica.md`. N3 coincide con `firme-verbali.md`. **In tutti e tre i casi l'avvertenza della fonte è riportata, ed è correttamente etichettata come *giudizio* in N1 e come *fatto* in N2** — è il punto in cui il documento poteva rafforzare e non lo fa.

**§6 — le cinque conclusioni, fatto per fatto.** Ogni fatto citato esiste nelle fonti e, salvo i rilievi 3, 5 e 9, porta la marcatura corretta. Le sezioni «che cosa la falsificherebbe» sono ancorate a limiti realmente dichiarati nelle fonti (l'avvertenza «che nessuno lo faccia può significare che non funziona» è testuale in `modelli-di-ricavo-e-prezzi.md`; il contro-esempio Officine Innovazione/Deloitte è corretto; `gcadvisory.com` esiste davvero nella scheda Growth Capital, trovata nell'esclusione degli omonimi). La conclusione 3 **non** dichiara libero il campo M&A e riporta il limite dello strumento: è il punto in cui il documento resiste alla tentazione più forte.

**§7 — il registro delle incertezze.** U-1…U-6 e le tredici voci di §7.3 corrispondono a voci reali di `dubbi.md` (verificate: Seedble S-10 e S-2, Cariplo #2 e #5, Ventive #5, Startup Geeks #2, Webidoo #1, Vento #1, GELLIFY #9, Growth Capital #6, Tinexta #1, Plug and Play #1, Infinite Area #4 e #1, Bridgemaker #5 e #2). Nessuna è stata addolcita. Le cautele «identità societaria da confermare (omonimia)» su CRIT, «attribuzione provvisoria», «discrepanza 8,8 mln vs oltre 5 mln non risolta» su GELLIFY/FS sono **tutte trasportate** nel documento finale.

**Perimetro — le cinque cose «non fatte» sono tutte documentate**: copertura Lookout ~30%, budget WebSearch esaurito 200/200 prima dello screening, «nessuno dei 93 ha un fatturato verificato», categoria E non lavorata, selezione fase 4 non validata da una persona (`selezione.md` porta davvero l'avvertenza in testa), nessun output letto a campione. Nessuna è omessa o ammorbidita.

---

## Quello che non ho potuto verificare

1. **Le fonti esterne.** Non ho fatto ricerca web: ho verificato la **coerenza fra documento e file interni**, non la verità dei file interni. Se una scheda ha letto male un bilancio o attribuito un CIG all'azienda sbagliata, questa verifica non lo intercetta. Vale in particolare per i 77 contratti ANAC, tutti di seconda mano, e per l'omonimia CRIT che le fonti stesse dichiarano irrisolta.
2. **La correttezza dei giudizi.** Ho verificato che i giudizi siano etichettati come tali e ancorati a un fatto esistente; non che siano giusti. Un grado «media» invece di «alta» in tabella 3.1 è una valutazione di `sintesi-strategica.md`, non un fatto falsificabile con i file a disposizione.
3. **I cinque file di lotto dello screening** li ho letti solo per i punti contestati (lotti 3 e 4). Le 76 celle della tabella 3.2 sono state verificate contro `sintesi-strategica.md`, che è la fonte immediata del documento, **non** risalendo a ciascuna riga di screening: un errore introdotto già in `sintesi-strategica.md` sarebbe passato.
4. **Il conteggio esatto delle voci di `dubbi.md`.** Ho verificato che «190+» sia conservativo, non il numero preciso.
5. **`scouting/consolidato.md`** l'ho letto in testa e nei punti citati, non integralmente: non posso escludere che un operatore del documento non compaia lì.
6. **Le quattro voci di offerta di Deploiable e i segmenti** («PMI, aziende dai 40 milioni in su, enti pubblici, soggetti acquirenti») non sono verificabili contro nessuna delle fonti elencate: provengono dal committente, non dall'analisi. Non è un errore, ma non è materiale che questa verifica possa confermare.

---

## Giudizio finale

Il documento è **utilizzabile per una decisione con le correzioni indicate**, e le correzioni sono poche e circoscritte: nessun rilievo tocca la sostanza delle cinque conclusioni operative.
L'errore che conta davvero è **uno solo** — la riga di sintesi della tabella 3.1 dice «sei» dove la tabella stessa dice otto — e va corretto prima della riunione perché sottostima l'affollamento sulla nostra prima linea.
**Non ho trovato nessuna marcatura innalzata**: nessun dato `[S]` o `[D]` delle schede compare nel documento come `[V]` o nudo, che era l'errore più grave cercato e il più probabile in una compressione di questa scala.
Il documento è anzi **sistematicamente più cauto delle proprie fonti** — trasporta le avvertenze su omonimie, discrepanze non risolte, dati di seconda mano e limiti di copertura, e in due casi (rilievo 8, e la marcatura del round Webidoo) sbaglia per difetto anziché per eccesso.
Restano da correggere: la riga di sintesi §3.1, il «cinque contratti» che sono sei, lo «zero» che è uno in conclusione 1, i «18 mln» che sono dollari e i «3.000» che sono di Leyton — mezz'ora di lavoro, dopo la quale il documento regge.

---

## Stato delle correzioni — 11/08/2026

**Tutti e undici i rilievi sono stati applicati** a `ANALISI-COMPETITOR-V2.md` subito dopo questa verifica. Il rilievo 2 è stato corretto **anche alla fonte**, in `modelli-di-ricavo-e-prezzi.md` §Limiti, dove l'errore era nato.

| # | Gravità | Applicato | Come |
|---|---|---|---|
| 1 | alta | sì | «sei» → «**otto** hanno Open Innovation alta o media» |
| 2 | media | sì, in due file | «cinque contratti sopra i 100.000 €» → «**dodici**», con i dodici importi elencati e la soglia alternativa dei sei sopra i 130.000 € |
| 3 | media | sì | «oggi zero» → «oggi **uno**: il percorso ETP di Seedble a 3.000 € + IVA `[D]`», con la qualificazione esplicita del segmento |
| 4 | media | sì | «18 mln di ricavi» → «**18 mln $** di ricavi» |
| 5 | media | sì | i 3.000 clienti attribuiti alla sola **Leyton** |
| 6 | media | sì | il «36» della categoria B marcato *(giudizio)* in cella, con la spiegazione |
| 7 | bassa | sì | ricostruita l'aritmetica dell'84: +45 consulenti OI **e** +39 startup studio/venture builder |
| 8 | bassa | sì | round Webidoo portato a `[V]`, ricavi lasciati `[D]` |
| 9 | bassa | sì | aggiunta la marcatura `[S]` e il rimando a U-1 sul taglio 10.000-140.000 € |
| 10 | bassa | sì | ripristinata la definizione integrale di `[S]` dal metodo |
| 11 | bassa | sì | citazione Bridgemaker riportata per intero |

**Quello che questa verifica non ha coperto resta valido come limite** ed è riportato nella sezione precedente: la coerenza fra documento e file interni è stata controllata, la **verità dei file interni no**. Il controllo umano previsto dal metodo — aprire almeno una fonte per operatore — **non è ancora stato fatto**.
