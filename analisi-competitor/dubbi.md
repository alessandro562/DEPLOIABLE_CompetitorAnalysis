# Registro delle incertezze

**Deploiable · analisi competitor V2**
Aggiornato l'11/08/2026 · alimenta la sezione finale del documento della fase 8

Ogni voce dice **cosa non è stato verificato** e **quale fonte servirebbe**. Si aggiunge in coda a ogni scheda prodotta: non si riscrive.

---

## Seedble — scheda completa del 11/08/2026

Fonte: `schede/seedble.md`, campo 14.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| S-1 | Compagine sociale e quote; presenza di soci diversi dai fondatori | Visura camerale ordinaria (Telemaco) |
| S-2 | Bilanci 2022-2025: ricavi, marginalità, costo del personale. L'ultimo dato reperibile è il 2021 | Bilanci depositati al Registro imprese |
| S-3 | Capitale sociale effettivo — due aggregatori danno valori incompatibili (€182.449,80 contro fascia €250mila-1mln) | Visura camerale |
| S-4 | Organico reale — 31 nomi sul sito contro 5-50 addetti secondo gli aggregatori | Nota integrativa al bilancio, o LinkedIn verificato a mano |
| S-5 | I due contratti pubblici: stazione appaltante, oggetto, durata, procedura. **È il dato di prezzo più prezioso disponibile su questo operatore** | ANAC — BDNCP, ricerca per CIG 9230119727 e B12987CB7D |
| S-6 | Data di costituzione di BLENDX S.r.l. e assetto proprietario: quanta parte è di Seedble | Visura camerale su P. IVA 15299231009 |
| S-7 | Prezzi di blendX — i quattro piani non espongono importi | Richiesta demo, o capitolati pubblici che includano la licenza |
| S-8 | Provenienza professionale dei fondatori — la pagina team non ha biografie | LinkedIn (non consultabile da agente: robots.txt), o interviste |
| S-9 | Datazione delle notizie — partnership e programmi non sono collocabili nel tempo | Wayback Machine sulle pagine archivio, o richiesta diretta |
| S-10 | Modello di ingaggio su Rocket Lab — nessun prezzo, nessuna durata, nessun modello di remunerazione. **È la linea più sovrapposta alla nostra Open Innovation ed è quella su cui sappiamo meno** | Capitolati di gara, interviste ai fondatori, conversazione con chi ha lavorato con loro |
| S-11 | Rapporto con Sogei — unico cliente pubblico nominato, nessun dettaglio | Sezione trasparenza di Sogei, ANAC |
| S-12 | Corrispondenza CIG B12987CB7D ↔ esito di gara Ecocerved: la pagina emersa dalla ricerca restituisce 404 e l'elenco affidamenti di Ecocerved (479 procedure) non contiene Seedble. **Non usare la corrispondenza finché non è confermata** | ANAC per CIG, o sezione trasparenza Ecocerved |

---

## Fase 1 — scouting per angolo, 11/08/2026

Limiti dichiarati dai sette angoli. Sono incertezze di **copertura**: dicono quanto della realtà la lista non contiene.

| # | Incertezza | Cosa servirebbe |
|---|---|---|
| A-1 | ANAC-BDNCP respinta da WAF, TED bloccato da robots.txt, piattaforma ANAC di pubblicità legale illeggibile perché SPA JavaScript. **Nessun CIG sulle sei aggiudicazioni principali dell'angolo A** | Accesso diretto o via API alla BDNCP; download degli open data ANAC |
| A-2 | Portali delle agenzie regionali per l'innovazione in gran parte non raggiunti (Sardegna Ricerche, ART-ER, Sviluppumbria, Finpiemonte, InnovaPuglia, ARIA). Lazio Innova non pubblica esiti né CIG | Consultazione manuale delle sezioni «amministrazione trasparente» |
| A-3 | Sull'open data di Regione Lombardia le query su «intelligenza artificiale» e «scouting» restituiscono **zero record**, e la serie si ferma al 2024 | Verifica se l'assenza è reale o è un problema di classificazione merceologica |
| B-1 | **Copertura dell'Open Innovation Lookout intorno al 30%**: 6 archivi di categoria su 24, 31 schede player aperte. **Le categorie «acceleratore» e «incubatore» non sono state scorse** | Spoglio sistematico delle 24 categorie |
| B-2 | Il directory pubblico del Lookout non è allineato al proprio rapporto 2026: il rapporto dichiara 503 organizzazioni e 103 consulenti OI, le pagine di categoria ne mostrano 58. **Circa 84 operatori censiti non sono raggiungibili pubblicamente** | Richiesta del dataset all'osservatorio |
| B-3 | Elenchi soci non estratti: InnovUp (53 «Enabler» pertinenti, filtri per categoria non funzionanti via URL), Italian Tech Alliance («lista in fase di aggiornamento»), Assintel, Assinter, Confindustria Digitale, registri MIMIT di incubatori certificati e PMI innovative | Consultazione manuale, o richiesta alle associazioni |
| B-4 | Attività negli ultimi 18 mesi verificata solo su 9 righe su 44; per le altre 35 l'unica evidenza è il censimento `[S]`, con dati autodichiarati e riferiti al 2022 | Verifica puntuale sui siti e sui bilanci |
| C-1 | Il sito di CDP Venture Capital ha restituito errore: la mappatura gestore ↔ programma della rete nazionale poggia su **una singola fonte terza**. La rete è cresciuta dopo quella rilevazione: l'elenco è incompleto per difetto | Pagina ufficiale della rete acceleratori CDP |
| C-2 | Le pagine «innovazione» di Enel, Eni, Poste, TIM, Leonardo, Ferrovie, A2A, Lavazza, Chiesi, Angelini, Bracco, Campari, Autogrill **non nominano il gestore** del programma | Comunicati di lancio, o domanda diretta agli innovation manager |
| C-3 | Il canale hackathon aziendali è il meno documentato: raramente produce comunicati che citino il gestore | Fonti di settore, contatti diretti |
| C-4 | Compensi e natura del rapporto non verificabili: la colonna «committente» va letta come soggetto promotore, **non necessariamente come cliente pagante** | Capitolati, bilanci dei promotori |
| D-1 | I programmi di **WMF**, **AI Festival** e **Rome Future Week** — le tre liste sponsor potenzialmente più ricche — non sono stati spogliati (errori 400 e robots.txt) | Consultazione manuale dei programmi |
| D-2 | Budget di ricerca esaurito prima di coprire SMAU regionali, Web Marketing Festival, IT'S TECH ed eventi Assintel | Nuova sessione dedicata |
| E-1 | I bilanci di sostenibilità si sono rivelati un canale povero: nei due controllati integralmente (Saipem 2024, OTB 2024) non compare alcun fornitore di innovazione nominato | Campione più ampio, o ricerca full-text sui PDF |
| E-2 | **Per venture building su commissione, AI adoption e M&A non esiste una sola citazione cliente-side verificabile** — marcatura `[N]`. La copertura dell'angolo E è squilibrata sull'open innovation | Ricerca cliente-per-cliente, che richiede budget di ricerca |
| E-3 | Le referenze di Plug and Play ed ELIS sono anteriori ai 18 mesi | Verifica dello stato attuale dei rapporti |
| F-1 | **LinkedIn non consultabile** (robots.txt): è il canale dominante in Italia per i ruoli cercati, e alcuni operatori pubblicano solo lì. **È il buco più grave dell'angolo F** | Consultazione manuale |
| F-2 | Il registro imprese non è interrogabile in modo parametrico da fonti aperte: nessuna ricerca per ATECO più anno di costituzione. Per questo la parte «nuovi entranti» restituisce quattro nomi anziché una decina | Accesso Telemaco, o open data MIMIT |
| F-3 | Le date di pubblicazione degli annunci non sono affidabili: i portali espongono la data di rendering o l'anzianità relativa | — |
| G-1 | **Nessuna evidenza testuale aperta di formule di remunerazione inusuali** — quota sul margine, royalty sulla linea di ricavo, gain-share, compenso legato all'adozione. Pubblicamente si trova solo l'allineamento dichiarato, mai il meccanismo | Interviste, o condizioni contrattuali di gare pubbliche estere |
| G-2 | Danimarca, Norvegia e Paesi Bassi non completati | Nuova sessione dedicata |

---

## Fase 2 — consolidamento, 11/08/2026

| # | Incertezza | Cosa servirebbe |
|---|---|---|
| K-1 | **The Doers**: acquisita da Digital Magics e confluita in Zest, ma `thedoers.co` non fetchabile e autonomia commerciale non accertata. Escluso in via cautelativa — **verifica da rifare** | Visura, o sito raggiungibile |
| K-2 | 10 domini non verificabili per blocco tecnico: `k-digitale.com`, `e12.it` (SSL non valido), `arsenalia.it`, `soft-strategy.com`, `ciaotech.com`, `pnoconsultants.com/it`, `devoteam.com/it`, `thedoers.co`; più StrategyInnovation senza dominio dichiarato nel censimento e TeamDev con sede ND | Verifica manuale da rete non filtrata |
| K-3 | 5 domini non risolti o divergenti: `gfactor.it` (DNS assente), `aiventurebuilder.com` (parcheggiato GoDaddy), `djungle.io` (pagina Lovable generica), `atlantegroup.it`, `spici.it`, `openadvisory.it` (SSL non valido) | Verifica manuale |
| K-4 | 17 domini non re-interrogati in fase 2 perché già fetchati dagli agenti di angolo, e i 12 esteri non re-interrogati | — |

---

## Fase 3 — screening, 11/08/2026

| # | Incertezza | Cosa servirebbe |
|---|---|---|
| T-1 | **Il budget di ricerca web era esaurito prima che lo screening iniziasse.** Tutti e cinque i lotti hanno lavorato solo con letture dirette di pagina, senza incrocio di fonti. I punteggi si reggono su ciò che l'operatore dice di sé | Rifare lo screening dei punteggio 4 con budget di ricerca |
| T-2 | **Nessuno dei 93 operatori ha un fatturato verificato.** Il campo dimensione è il più debole dello screening | Bilanci depositati sui candidati alla scheda completa |
| T-3 | Punteggi limitati dalla verificabilità e non dalla rilevanza: BIP, CiaoTech/PNO, K-Digitale, Devoteam, Soft Strategy, G-Factor, H-FARM. **Potrebbero valere di più** | Siti raggiungibili |
| T-4 | **Growth Capital**: il buy-side è dichiarato ma non documentato con un mandato — i deal nominati sono tutti aumenti di capitale, cioè il mestiere opposto. Le banche non compaiono nella loro segmentazione | `growthcapital.vc/index.php/site/investors`; comunicati su operazioni buy-side |
| T-5 | **FoolFarm**: il censimento dichiara corporate venture building, il sito vende solo investimento in proprio. Contraddizione irrisolta | Sito o intervista |
| T-6 | **Opinno**: assetto societario dell'entità italiana da chiarire | Visura |
| T-7 | Nessuno dei quattro operatori che risultano fare venture building su commissione (20V, Venture Architect, Start Factor, Day One) espone un solo cliente committente nominato | Referenze cliente-side |
| T-8 | Le tre formule di ricavo estere selezionate (quota associativa d'alleanza, triplo committente, fondo a più committenti) sono **strutturali**, non contrattuali: non sappiamo come sono prezzate | Interviste, o bilanci degli operatori esteri |

---

## Incertezze di metodo — trasversali

| # | Incertezza | Nota |
|---|---|---|
| M-1 | **Nessun output di agente è stato aperto a campione da una persona.** La regola di sicurezza del file `02-prompt-agenti.md` non è ancora stata applicata a questa tornata | È il passaggio da fare prima di portare qualunque cosa in riunione |
| M-2 | Divergenza fra `01-metodo-e-schema.md` e `02-prompt-agenti.md` sui campi 13 e 14 della scheda: il metodo prevede *sovrapposizione* e *in gara*, il Prompt 2 prevede *forza/fragilità* e *domande aperte*. Il Prompt 2 rinvia esplicitamente al Prompt 5 | Risolta nella V2 dei prompt: sovrapposizione e in gara si compilano con il Prompt 5 |
| M-3 | Il registro `dati/registro.csv` contiene oggi **una sola riga**, Seedble. Le altre si generano una per scheda in `dati/righe/` e si fondono | — |

---

## Fase 5 — schede complete del 11/08/2026

Domande aperte raccolte dal campo 14 di ciascuna scheda. La numerazione interna è quella assegnata dall'agente che ha prodotto la scheda; il prefisso è il nome dell'operatore.


### Cariplo Factory / Factory Plus

Fonte: `schede/cariplo-factory.md`, campo 14.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | Quota esatta di partecipazione di Fondazione Cariplo nella società ed eventuale presenza di altri soci (la Fondazione la elenca fra gli enti strumentali ma non pubblica la percentuale) | Visura camerale con elenco soci; bilancio di missione o consolidato di Fondazione Cariplo |
| 2 | Ripartizione dei ricavi fra committenza del sistema Fondazione Cariplo e mercato aperto — punto decisivo per capire se sia operatore di mercato o braccio operativo | Nota integrativa al bilancio depositato; Relazione d'Impatto 2024 integrale in PDF |
| 3 | Avvenuta iscrizione al registro imprese della nuova denominazione «Factory Plus S.r.l. Società Benefit» (gli aggregatori riportano ancora «Cariplo Factory S.r.l. Società Benefit») | Visura camerale aggiornata post-luglio 2026 |
| 4 | Capitale sociale e struttura patrimoniale (reportaziende.it ha restituito HTTP 403 in sessione) | Banca dati camerale accessibile o visura ordinaria |
| 5 | Natura societaria e compagine di B-C Ventures: diritto italiano o tedesco, ripartizione fra Factory Plus e Bridgemaker, quota detenuta nelle venture create | Visura del veicolo B-C Ventures; comunicato costitutivo integrale o atto notarile |
| 6 | Prezzi e condizioni economiche dei servizi corporate e di gestione programma (nessun dato pubblico) | Capitolato di gara o contratto pubblicato in amministrazione trasparente da un committente pubblico (es. Regione Lombardia su InnovaCultura) |
| 7 | Referenze confermate direttamente da clienti corporate privati (Snam, ING, Eni): i nomi compaiono solo sulle pagine dell'operatore | Comunicato stampa o case history pubblicata sui siti di quelle aziende |
| 8 | Bilancio 2025 e dati economici post-rebranding, non disponibili sugli aggregatori all'11/08/2026 | Deposito al registro imprese dell'esercizio 2025 |
| 9 | Dimensione del team dichiarata su LinkedIn e provenienza professionale puntuale delle persone chiave (LinkedIn non consultabile: robots.txt disallow) | Accesso diretto alla pagina LinkedIn aziendale e ai profili individuali |
| 10 | Contenuto delle «importanti novità che saranno svelate nei prossimi mesi» annunciate nel comunicato di rebranding: nuove linee di offerta non ancora pubbliche | Comunicati successivi di factoryplus.eu; rassegna stampa da settembre 2026 |


### Officine Innovazione (Deloitte)

Fonte: `schede/officine-innovazione.md`, campo 14.

Compilato l'11/08/2026 · a valle del Prompt 2 · solo fonti aperte consultate in sessione

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | **Chi è formalmente il socio e con quale quota.** L'appartenenza al network Deloitte è dichiarata e provata di fatto dal CdA (presidente il CEO di Deloitte Italia), ma la compagine sociale nominativa non è pubblica. Dato aggravante: Officine Innovazione **non compare** nella pagina «Dati societari» di Deloitte Italia che pubblica socio unico e direzione e coordinamento per 14 altre entità del network | Visura camerale ordinaria del Registro imprese di Milano, P. IVA 10230520966, sezioni compagine sociale e art. 2497 c.c. |
| 2 | **Se esista direzione e coordinamento ex art. 2497 c.c. e da parte di quale entità Deloitte** | Stessa visura, sezione «soggetto che esercita direzione e coordinamento»; in subordine, la nota integrativa del bilancio depositato |
| 3 | **L'organico reale della società.** 95 dipendenti (2025) e 49 (2021) da aggregatori; «1001-5000» dall'Osservatorio, che però è il dato del network; l'operatore non dichiara mai il proprio organico | Nota integrativa del bilancio depositato, voce «numero medio dei dipendenti nell'esercizio» |
| 4 | **La serie dei ricavi 2022, 2023, 2024.** Ho solo i due estremi (5,70 mln 2021 → 12,59 mln 2025): non so se la crescita sia lineare o concentrata in un esercizio, e quindi non so datare l'accelerazione | Bilanci depositati 2022, 2023 e 2024 dal Registro imprese |
| 5 | **Quale sia la sede legale attuale.** Via Santa Sofia 28 (20122 Milano) secondo un aggregatore, Via Tortona 25 (20144 Milano) secondo un altro e secondo l'Osservatorio. La pagina office locator di Deloitte carica l'indirizzo via JavaScript e non è leggibile | Visura camerale, sezione sede legale con data di variazione |
| 6 | **Se Officine Innovazione abbia mai vinto un appalto pubblico, e con quale importo.** Nei dataset lombardi risulta partecipante in 20 procedure 2021-2024 e aggiudicataria in **zero**. Non so se vinca altrove | BDNCP ANAC, ricerca per codice fiscale dell'operatore economico (10230520966) su tutte le stazioni appaltanti nazionali, 2018-2026 |
| 7 | **Cosa sia successo sul canale appalti nel 2025 e 2026.** La serie open data di Regione Lombardia si ferma al dataset 2024 | Dataset «Elenco affidamenti beni e servizi 2025/2026» di Regione Lombardia quando pubblicati; in alternativa la sezione Amministrazione Trasparente ex art. 1 c. 32 L. 190/2012 della Giunta regionale |
| 8 | **Chi sia l'aggiudicatario delle 18 procedure lombarde di cui conosco solo l'importo.** Ho il vincitore solo per i due lotti FEC 1/2022 (Avv. Cancelli, Dott. Grabellano). Sapere chi vince quando OI perde direbbe chi è il concorrente reale su quel canale | Stessi dataset interrogati per CIG con filtro `aggiudicatario_si_no=SI`, oppure gli avvisi sui risultati pubblicati su bandi.regione.lombardia.it per ciascun CIG |
| 9 | **La quota di Deloitte in Bianco Ventures, l'importo conferito, e se il socio sia Deloitte Italia o Officine Innovazione.** Le fonti dicono «Deloitte» e citano un Partner (Marco Perrone), ma il veicolo giuridico non è chiarito | Visura di Bianco Ventures S.r.l.; in alternativa la documentazione obbligatoria della campagna di equity crowdfunding su Mamacrowd, che espone la compagine pre-money |
| 10 | **Se esista un piano per portare il metodo Venture Client di 27pilots in Italia.** Al 11/08/2026 le due unità coesistono nel network senza alcun collegamento documentato; l'Italia non compare fra le geografie dichiarate di 27pilots | Comunicato congiunto Deloitte Italia/27pilots; oppure una pagina capability 27pilots sul dominio italiano di Deloitte; oppure un'intervista a Gregor Gimmy o a Cristiano Camponeschi sul perimetro geografico |
| 11 | **Perché non esista una linea AI in un'unità di innovazione nel 2026**, con catalogo servizi invariato dal 2021 e un GenAI Center da 25 mln di euro nel network | Brochure servizi aggiornata post-2021; Relazione di Impatto FY26; annuncio di riorganizzazione delle linee di servizio |
| 12 | **Quanto pesino i ricavi da programmi a finanziamento pubblico** (PNRR/MUSA-MHEO, DIHCUBE) sul totale | Nota integrativa con ripartizione dei ricavi; in alternativa i piani finanziari dei progetti MUSA e DIHCUBE, che nominano partner e budget assegnati |
| 13 | **Quali siano i clienti corporate paganti**, distinti dai partner di programma. I nomi noti (Amadori, Peroni, Acea, Finiper, Cereal Docks) sono partner di acceleratori: non è dimostrato che siano committenti | Case study con nome del committente, perimetro e durata; oppure comunicati emessi dal cliente |
| 14 | **Se esista un solo caso di venture building su commessa**, dopo cinque anni di linea a catalogo | Case study nominato; oppure visura di eventuali società veicolo partecipate da Officine Innovazione |
| 15 | **Chi siano le persone sotto il livello del CdA e da dove vengano.** Nessuna pagina team, nessun organigramma; LinkedIn non è consultabile da questo ambiente (robots.txt) | Accesso a LinkedIn (pagina azienda e filtro dipendenti); oppure la sezione people del sito Deloitte filtrata su Officine Innovazione |
| 16 | **Se i due «prodotti» della brochure 2021 esistano ancora** — la piattaforma di renting B2C di arredamento per smart working e la soluzione di Food Traceability — e chi li abbia costruiti | Brochure o pagina servizi aggiornata; visura di eventuali società veicolo; interrogazione del Registro marchi |
| 17 | **Quale sia il prezzo di un programma tipo** (acceleratore verticale, call for startup, percorso di corporate entrepreneurship). Nessun listino pubblico e nessun appalto aggiudicato da cui dedurlo | Un capitolato con base d'asta di una gara vinta dall'operatore; oppure un preventivo ottenuto per via commerciale |
| 18 | **Perché il 2026 sia completamente muto.** Nessun contenuto datato 2026 riferibile all'operatore su nessuna fonte aperta. Non è dimostrato che non sia successo nulla: è dimostrato che non è visibile | Press room Deloitte Italia filtrata per data; profilo LinkedIn dell'operatore; Relazione di Impatto FY26 quando pubblicata |


### Ventive

Fonte: `schede/ventive.md`, campo 14.

Scheda: `schede/ventive.md` · consultato il 11/08/2026 · dominio verificato: **ventivegroup.com** · soggetto: **Ventive S.r.l.**, Roma, P.IVA 15435551005 (esclusa l'omonima statunitense Ventive LLC, ventive.com).

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | La compagine sociale aggiornata dopo il round 2025 e le percentuali di possesso: i comunicati nominano gli investitori entrati ma non le quote. | Visura camerale ordinaria della Camera di Commercio di Roma (REA RM 1590212) o l'atto notarile di aumento di capitale del 6/10/2025 (notaio Guglielmo Siniscalchi). |
| 2 | Come è remunerata l'advisory di fundraising: se esiste una success fee sul capitale raccolto e a quale aliquota. Le pagine dedicate non lo spiegano. | Lettera d'incarico o contratto tipo, oppure testimonianza diretta di una startup cliente o di un investitore del Club Deal. |
| 3 | La quota di equity acquisita dal programma di incubazione InVentive, dichiarato «senza alcun costo» ma remunerato in equity. | Regolamento della call InVentive, term sheet del programma o visura di una delle startup incubate. |
| 4 | Se la sede di Londra annunciata a settembre 2025 sia stata effettivamente costituita, con quale denominazione, quando e con quali director. | Ricerca su Companies House (UK) per denominazione e per director Roberto Sfoglietta. |
| 5 | Se esista un committente corporate reale della linea Open Innovation & Corporate Venture Capital: nessun nome è pubblicato. | Comunicato stampa del corporate stesso, case study pubblicato, o avviso/contratto reperibile in fonte pubblica. |
| 6 | Il fatturato 2025 e la composizione dei ricavi fra fee di servizio e proventi da partecipazioni; l'ultimo dato disponibile è il 2024. | Bilancio d'esercizio 2025 depositato al Registro Imprese (o banca dati con nota integrativa). |
| 7 | L'organico effettivo al 2026: le fonti oscillano fra 6-9 addetti, 13 nomi sul sito, 11-50 su Crunchbase e 25 persone dichiarate nel 2022. | Nota integrativa/dipendenti medi del bilancio depositato, oppure headcount ufficiale dichiarato dalla società. |
| 8 | La provenienza professionale precedente delle persone chiave (aziende e ruoli anteriori a Ventive). | Profili LinkedIn individuali, non recuperabili in questa sessione perché LinkedIn blocca il fetch via robots.txt; in alternativa interviste o profili biografici pubblicati. |
| 9 | La discrepanza sui co-fondatori: Crunchbase indica Marco Scioli come co-founder e Riccardo Angioli fra le key people, nomi assenti dalla pagina «About us» del 2026. | Visura storica con elenco soci fondatori, oppure statuto/atto costitutivo 2019. |
| 10 | Se il numero dichiarato di «35+ operazioni di successo» e «oltre 30 mln investiti» sia verificabile: solo una exit è nominata (Karma Digital ceduta a Intent SpA) e una sola operazione è confermata da terzi (Gyala, marzo 2026). | Elenco delle exit con controparti e date, oppure database transazioni a pagamento (Dealroom, PitchBook) con record per investitore. |
| 11 | Se esista un veicolo di investimento strutturato (fondo o SICAF) distinto dalla S.r.l. operativa: sono nominate le holding Moonstone e Insquared ma non è chiaro il rapporto con Ventive S.r.l. | Visure delle società Moonstone e Insquared, o albo/registri di vigilanza per eventuali veicoli regolamentati. |
| 12 | Se nel periodo febbraio-agosto 2026 vi siano stati fatti rilevanti oltre al co-investimento in Gyala: nessun altro comunicato è emerso dalla ricerca. | Rassegna stampa a pagamento sul periodo, o la sezione news/comunicati del sito (non individuata come archivio datato). |


### Startup Geeks

Fonte: `schede/startup-geeks.md`, campo 14.

**Analisi competitor V2 · Prompt 2 · compilato l'11/08/2026**
Ricerca su sole fonti aperte. Nessuna visura camerale acquistata, nessun bilancio depositato letto in originale, nessun contatto diretto con l'operatore.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | **Il prezzo dello Startup Builder e dello Startup Booster** — cioè il prezzo dei due prodotti che generano il grosso del ricavo. La pagina cita "il prezzo dei percorsi disponibili" ma lo rilascia solo dopo compilazione del modulo. Cercato su: pagina programma sul sito principale, `sp.startupgeeks.it/startup-builder`, `sp.startupgeeks.it/startupbooster`, `sp.startupgeeks.it/premium`, `sp.startupgeeks.it/bundle-lanciare-prima-azienda`, pagina recensioni dell'operatore, loro rassegna sugli incubatori italiani, articoli di stampa 2023-2026, recensioni Trustpilot | Compilazione del form di richiesta con un contatto reale; in alternativa testimonianza diretta di un ex partecipante, oppure un bando o voucher regionale che rimborsi il programma indicandone l'importo a preventivo |
| 2 | **La ripartizione del fatturato fra B2C (founder) e corporate.** Sappiamo che il gruppo fa €2,9M nel 2025, non sappiamo quanto ne venga dalle aziende. È il dato che determina se la linea che ci riguarda sia marginale o sostanziale | Nota integrativa al bilancio 2025 con ripartizione dei ricavi per linea di attività (bilancio depositato al Registro imprese di Mantova), o intervista diretta ai fondatori |
| 3 | **La compagine sociale e il rapporto fra le due entità.** Esistono Startup Geeks S.r.l. SB (02613410204) e Startup Geeks Holding Srl (02697050207), stessa sede, ma il controllo non è ricostruibile. Quote dei fondatori e degli angel entrati in crowdfunding ignote. L'unico aggregatore che dichiara di avere la compagine la mette dietro paywall (€8,90) | Visura camerale ordinaria di entrambe le società presso la Camera di commercio di Mantova |
| 4 | **Se i rapporti con Eni, NTT DATA, Sisal, Italdesign, Lactalis, Unipol, ING, Credem siano progetti strutturati o attività una tantum.** Sono 12 loghi citati dall'operatore, zero confermati dal cliente | Comunicato stampa o pagina del cliente che citi Startup Geeks; in mancanza, un caso studio congiunto con perimetro, durata e risultato |
| 5 | **Quante startup siano realmente passate dai programmi, e quali.** I numeri autodichiarati sono fra loro incoerenti: 848 e "+1.000" sulla stessa home, 788 nel 2023, 1.070 ad agosto 2026; il capitale raccolto oscilla fra 7,3M, 9M, 10M e 11M | Elenco nominativo delle startup incubate; oppure il **report di impatto della società benefit**, obbligatorio per legge e da allegare al bilancio, che dovrebbe contenere metriche verificabili |
| 6 | **La provenienza professionale di Giulia D'Amato e Alessio Boceda prima del 2019.** Il sito li descrive solo come "leader carismatica" e "marketer e stratega". Cercato su sito, Chi siamo, CrowdFundMe, Corriere Nazionale, Capitalist, Il Sole 24 Ore | Profili LinkedIn dei due fondatori, o un'intervista biografica |
| 7 | **Se l'Investment Club prenda success fee, commissione o equity sui round facilitati.** La pagina dice che le condizioni economiche sono "comunicate in fase di ammissione" | Documentazione contrattuale di ammissione, o testimonianza di una startup ammessa al club |
| 8 | **Se l'obiettivo annunciato nel 2024 di investire €5 milioni tramite l'Investment Club sia stato raggiunto.** Ad oggi risultano dichiarati €450.000 investiti, cioè il 9% | Consuntivo dell'Investment Club, o registro delle operazioni di investimento |
| 9 | **Se il target "oltre €3 milioni entro fine 2026" si riferisca a Lever PR o all'intero gruppo.** Se fosse della sola agenzia, supererebbe l'intero fatturato 2025 del gruppo: le fonti sono ambigue | Chiarimento dell'ufficio stampa, o bilancio 2026 di Lever PR come entità distinta (se costituita come società autonoma — cosa a sua volta da verificare) |
| 10 | **Quando e perché sia stato ritirato dalla home il claim "L'incubatore online più grande d'Italia".** Il cambio è accertato, la data no | Archivio Wayback Machine della home page fra il 2024 e il 2026, o dichiarazione dell'operatore |
| 11 | **Se esista una linea verso enti pubblici** (comuni, regioni, camere di commercio, PNRR). Nessuna evidenza trovata, ma l'assenza da fonti aperte non è prova di assenza | Interrogazione delle banche dati appalti (ANAC, CIG) sulle due partite IVA; portali di trasparenza degli enti |
| 12 | **Il codice ATECO reale.** Due aggregatori ne riportano due diversi: 6391 "portali di ricerca sul web" e 63.12 "servizi di informazione e consulenza informatica". Nessuno dei due descrive incubazione o formazione | Visura camerale, che riporta ATECO primario e secondari aggiornati |
| 13 | **L'anno di costituzione effettivo.** Registro imprese: 20/02/2020. Operatore e stampa: 2019. La campagna crowdfunding cita una valutazione già ad aprile 2020 | Visura camerale con data di costituzione dell'atto, distinta dalla data di iscrizione |
| 14 | **L'organico reale.** 40 collaboratori dichiarati contro 15 dipendenti da bilancio. La differenza è compatibile con collaboratori a partita IVA ma non è stata verificata | Bilancio depositato 2025 con costo del personale e numero medio dipendenti, più eventuale nota sui collaboratori |
| 15 | **Rating e numero di recensioni su Trustpilot.** L'operatore dichiara 4,7/5 su una pagina e 4,6/5 su un'altra. La verifica diretta è fallita: la pagina Trustpilot ha respinto il fetch con errore 403 | Consultazione diretta di `it.trustpilot.com/review/www.startupgeeks.it` da browser |
| 16 | **Il contenuto di `servizi.startupgeeks.it`**, sottodominio attivo e indicizzato ma tecnicamente inaccessibile in questa sessione: il fetch fallisce con errore di handshake TLS/SSL e robots.txt non recuperabile | Accesso da browser, o versione archiviata su Wayback Machine |
| 17 | **Se il riconoscimento "Leader della Crescita 2026" de Il Sole 24 Ore / Statista e la nomina Forbes Under 30 2020 di Giulia D'Amato siano confermati alla fonte.** Entrambi sono al momento solo autodichiarati | Elenco originale Il Sole 24 Ore-Statista "Leader della Crescita 2026"; lista Forbes Italia Under 30 2020, categoria Education |
| 18 | **Se il "Corporate Venture Building" a catalogo abbia mai prodotto una venture.** Il servizio è dichiarato, nessun caso è documentato | Caso studio dell'operatore, o visura di una società costituita da un cliente corporate con il loro coinvolgimento |
| 19 | **Cosa sia esattamente l'"Osservatorio dell'Intrapreneurship"** citato fra i servizi corporate: se sia una ricerca pubblicata, un report a pagamento o un'iniziativa annunciata. La URL diretta tentata restituisce 404 | Il report stesso, o la pagina corretta sul sito `innovation.startupgeeks.it` |
| 20 | **Se la "piattaforma formativa gratuita" annunciata per il 2026 sia stata lanciata**, e come si concili con un modello che vende formazione a pagamento | Verifica sul sito nei mesi successivi, o comunicato di lancio |


### Webidoo

Fonte: `schede/webidoo.md`, campo 14.

Consultato il 11/08/2026. Solo fonti aperte reperite in sessione.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | Numero totale di PMI paganti in abbonamento (dichiarati solo «oltre 100 clienti USA»): è la metrica decisiva per un modello a volume | Information memorandum del round IXC3, nota agli investitori di Azimut Libera Impresa, o dichiarazione pubblica del management con il dato |
| 2 | Churn e ARPU degli abbonamenti Jooice | Metriche SaaS in una presentazione investitori o in un prospetto pre-IPO |
| 3 | Ripartizione dei 18 mln $ di ricavi 2025 fra SaaS, digital factory, AI Lab, digital export e retail | Bilancio consolidato Webidoo S.p.A. 2025 con nota integrativa (Camera di Commercio / Registro Imprese); companyreports.it e reportaziende.it hanno risposto 403 in sessione |
| 4 | Rapporto societario e di controllo fra Webidoo S.p.A. (P.IVA 10076860963) e WEBIDOO STORE S.R.L. (P.IVA 11946990964) | Visura camerale con assetti partecipativi di entrambe le società |
| 5 | Compagine sociale nominativa e percentuali esatte di IXC3/Azimut, 8a+ Innovation e TIM Ventures | Visura camerale aggiornata o comunicato completo del fondo IXC3 |
| 6 | Valutazione pre e post money del round di maggio 2026 e quota ceduta | Deal note di BeBeez o Mergermarket in versione integrale (paywall in sessione) |
| 7 | Termini economici degli accordi di canale con TIM, Nexi ed Esprinet (revenue share? rivendita? white label?) e volumi generati | Contratti non pubblici: servirebbe una dichiarazione di una delle parti, una relazione annuale Nexi/TIM, o un prospetto informativo |
| 8 | Prezzi di Groow (lanciato 05/06/2025, beta da settembre 2025) e di Welpy | Listino pubblico mai pubblicato: servirebbe un preventivo commerciale o una scheda di canale TIM/Nexi |
| 9 | Prezzi e contenuto operativo dei programmi «AI Lab» per grandi imprese e delle «digital factory» | Un caso cliente pubblicato, un comunicato di una grande impresa committente, o un bando/contratto |
| 10 | Chi sono i clienti enterprise degli AI Lab: nessun nome mai citato | Comunicato stampa del committente o case study firmato dal cliente |
| 11 | Organico reale: 350 persone dichiarate a novembre 2022 contro 11-50 dipendenti su Crunchbase | Numero dipendenti a bilancio o dato INPS/visura |
| 12 | Modelli AI di base su cui gira Groow (OpenAI, Anthropic, Google, modelli proprietari?) | Documentazione tecnica, pagina developer o DPA del prodotto: nessuna reperita |
| 13 | Cloud, certificazioni di sicurezza, conformità (ISO, SOC2, trattamento dati AI Act) | Trust center o pagina compliance, inesistenti sui domini consultati |
| 14 | Quali acquisizioni sono state effettivamente chiuse nel 2026 (dichiarate «una o due negli USA entro fine anno», nessuna annunciata alla data di consultazione) | Comunicati stampa successivi all'11/08/2026 o registro imprese USA/italiano |
| 15 | Provenienza professionale dei tre fondatori prima del 2017 | LinkedIn (bloccato da robots.txt in sessione); giovannifarese.com/en/about-me ha risposto 404; servirebbe un profilo giornalistico esteso |
| 16 | Ruolo attuale di Daniel Rota (CEO nel 2022, oggi CEO è Farese) e di Egidio Murru | Visura con cariche sociali o pagina team, assente sul sito |
| 17 | Identità di CFO, CTO e composizione del consiglio di amministrazione, inclusi eventuali rappresentanti di Azimut | Visura camerale con cariche o pagina governance |
| 18 | Conteggio e verifica delle recensioni «4,8 su Google e 4,8 su G2» esposte da Jooice | Profilo G2 pubblico di Jooice, non consultato direttamente |
| 19 | Se il redirect 302 di webidoodigitalservices.com su webidoo.com corrisponda a una fusione societaria o solo a un consolidamento di brand | Visura camerale / storico Registro Imprese dell'eventuale società Webidoo Digital Services |
| 20 | Numero effettivo di brevetti depositati (contatore presente in homepage ma non leggibile nella versione consultata) | Ricerca su EPO/UIBM per titolare Webidoo S.p.A. |
| 21 | Quota di ricavi generata dall'Italia rispetto a USA, Spagna e Medio Oriente | Bilancio consolidato con informativa per area geografica |


### Vento (Exor)

Fonte: `schede/vento.md`, campo 14.

Ricerca dell'11/08/2026, sole fonti aperte. Il soggetto è stato **identificato con certezza** come il veicolo venture di Exor, dominio ufficiale `vento.ventures`. Restano aperte le seguenti questioni.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | Se il fondo acquisisca oggi equity nelle società nate dal programma di venture building. Alla nascita era dichiarato testualmente il contrario («nessuna acquisizione di equity né success fee di alcun tipo»), ma oggi diverse società uscite dal programma figurano nel portafoglio. È la differenza fra un builder a fondo perduto e uno studio con equity, e determina il campo 7 | Visura camerale con elenco soci di due o tre società nate da Reef (es. Lexroom S.r.l., Qura, Clev), oppure il regolamento ufficiale del programma nella versione 2026 |
| 2 | La percentuale esatta di Exor nel capitale di Vento Ventures S.p.A. e l'identità degli amministratori. Le schede camerali gratuite consultate espongono sede, P.IVA, REA, capitale e ATECO ma non la compagine | Visura camerale ordinaria a pagamento (Registro Imprese di Torino, P.IVA 13163070017) con compagine sociale e organo amministrativo, oppure statuto depositato |
| 3 | Il rapporto fra il portafoglio Exor Ventures da 640 milioni gestito da Noam Ohana come gestore indipendente dall'ottobre 2024 e il Fondo II da 75 milioni di Vento. Nessuna fonte dichiara il nesso, che pure è cronologicamente stretto | Comunicato Exor sulla riorganizzazione della linea venture, oppure la sezione investimenti non-core dell'Annual Report Exor 2025 su exor.com |
| 4 | Il perimetro esatto dei numeri del decennale (160+ startup, 700+ milioni raccolti, portafoglio oltre 3 miliardi): se si riferiscano al solo marchio Vento o all'intera attività venture di Exor dal 2016, assorbita retroattivamente sotto il marchio | Comunicato stampa integrale del 16/03/2026 su exor.com o vento.ventures, con nota metodologica sul perimetro di consolidamento |
| 5 | La dimensione e la composizione del team. Il dato camerale (2 dipendenti) non è la dimensione operativa; l'aggregatore ne elenca una sola persona | Pagina `/team` di vento.ventures consultata da browser reale, oppure l'elenco dipendenti della pagina LinkedIn aziendale — entrambi inaccessibili a fetch automatico in questa sessione |
| 6 | La riconciliazione fra i due indirizzi torinesi: Corso Castelfidardo 22 (sede legale camerale) e Via Ormea 48 (indirizzo su aggregatore). Non è chiaro se siano sede legale e sede operativa o un dato non aggiornato | Pagina contatti del sito ufficiale, oppure visura camerale con elenco unità locali |
| 7 | L'economia dell'evento Wave by Vento: se la biglietteria introdotta nel 2026 sia destinata a coprire i costi o a generare margine, e quale società ne incassi i ricavi | Bilancio della società organizzatrice dell'evento, o dichiarazione dell'operatore sui conti dell'edizione 2026 |
| 8 | La provenienza professionale di Diyala D'Aveni prima di Vento. È la figura operativa di riferimento e il dato è assente da tutte le fonti consultate | Profilo LinkedIn personale, biografia ufficiale sul sito, o intervista biografica su testata |
| 9 | Se Vento venda o abbia mai venduto servizi a corporate. Le «challenge» proposte dai partner al lancio 2021 (Telepass, Reply, UniCredit) implicano uno scambio economico mai chiarito in nessuna fonte | Comunicato di partnership con descrizione degli obblighi economici, o dichiarazione di uno dei partner corporate citati |
| 10 | L'ultimo fatturato e il risultato d'esercizio. La S.p.A. è iscritta dal 30/12/2024 e non ha bilanci pubblicati; il comunicato Exor FY2025 non menziona la linea venture | Bilancio d'esercizio depositato al Registro Imprese, appena disponibile |
| 11 | Il contenuto dell'intervista di agenzia del 28/02/2026 alla CEO sull'AI e sul talento italiano: il titolo è verificabile, il corpo dell'articolo non è risultato leggibile | Testo integrale dell'articolo Radiocor su borsaitaliana.it, o accesso a rassegna stampa |
| 12 | Il numero e la natura degli investimenti chiusi nel 2026 fino ad agosto. Sono stati verificati singoli round da fonte terza (Qura a marzo, Lexroom a maggio) ma non esiste un conteggio periodico verificabile | Elenco investimenti datato su vento.ventures, o report Dealroom/Italian Tech Alliance sul primo semestre 2026 |


### GELLIFY

Fonte: `schede/gellify.md`, campo 14.

Consultato il 11/08/2026. Dominio ufficiale attivo verificato: `gellify.com`.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | L'assetto proprietario di GELLIFY GROUP S.P.A.: chi controlla, con che percentuali, e in particolare quanto pesa Azimut dopo l'aumento di capitale da 15 mln del 2019. Nessun aggregatore espone la compagine (ReportAziende 403, FatturatoAzienda dietro paywall a €8,90, Visura.pro senza elenco soci). | Visura camerale ordinaria con elenco soci di GELLIFY GROUP S.P.A. (P.IVA 10377000962) dal Registro Imprese, oppure fascicolo di bilancio completo con nota integrativa. |
| 2 | Il **CIG** e il **valore del singolo lotto** della gara Gruppo FS aggiudicata a GELLIFY. Le testate riportano solo l'aggregato di 8,8 mln e FS parla di «oltre 5 milioni»: nessuna fonte espone la base d'asta per lotto né il codice identificativo gara. | Determina/avviso di aggiudicazione sul portale e-procurement del Gruppo FS o su TED (Tenders Electronic Daily), oppure estrazione dalla Banca Dati Nazionale dei Contratti Pubblici ANAC per stazione appaltante FS Italiane, anno 2024. |
| 3 | La riconciliazione fra i **8,8 mln** riportati dalla stampa (Arena Digitale, Telenord, Borsa Italiana/Radiocor, comunicato GELLIFY) e gli **«oltre 5 milioni»** dichiarati da FS sul proprio organo di informazione per lo stesso accordo quadro innovazione a 3 lotti. | Bando integrale / disciplinare di gara con importo a base d'asta per ciascun lotto, e documento di aggiudicazione definitiva. |
| 4 | Se **Forward Factory** sia tuttora operativo o concluso, e a che batch sia arrivato. La pagina acceleratore su cdpventurecapital.it restituisce «Errore Generico»; l'ultima call documentata è la seconda. | Pagina acceleratore attiva di CDP Venture Capital, o rendiconto annuale della Rete Nazionale Acceleratori CDP, o comunicato di chiusura/rinnovo del programma. |
| 5 | Quote societarie, capitale sociale, P.IVA e sede registrata di **Bianco Ventures S.r.l.**, e la ripartizione fra GELLIFY, Deloitte e Arad Digital. Costituzione (05/12/2024) e sede operativa (Casalecchio di Reno) sono note, il resto no. | Visura camerale di Bianco Ventures S.r.l., oppure il documento di offerta pubblicato su Mamacrowd, che per obbligo normativo contiene la compagine pre-offerta e il capitale. |
| 6 | Il **fatturato consolidato di gruppo** 2024 e 2025. Sono noti solo i bilanci civilistici separati 2024 (GELLIFY ITALIA €18,57 mln; holding €202.867 con perdita) e un dato *dichiarato* alla stampa nel 2024 («37 mln pro-forma 2023»). Il bilancio 2025 non risulta ancora esposto. | Bilancio consolidato depositato di GELLIFY GROUP S.P.A. presso il Registro Imprese, esercizi 2024 e 2025. |
| 7 | Esistenza, forma e consistenza delle **entità estere**, in particolare negli Emirati Arabi Uniti (l'hub di Dubai è dichiarato dal 2020, non risulta una ragione sociale locale verificata) e in Spagna (GELLIFY Iberia, NOBA Ventures 51%). | Visura del registro DED o DMCC/free zone di Dubai; Registro Mercantil spagnolo per le entità iberiche; oppure il perimetro di consolidamento nella nota integrativa del bilancio consolidato. |
| 8 | Quante persone e **quali competenze tecniche** siano effettivamente in casa (sviluppatori, data scientist, ML engineer) rispetto ai 133 dipendenti registrati e ai 300 dichiarati. Il sito non espone pagine team o organigramma. | Prospetto del personale in nota integrativa del bilancio, oppure estrazione strutturata dei dipendenti dal profilo LinkedIn aziendale (non accessibile via fetch in questa sessione per robots.txt). |
| 9 | **Quali corporate private siano clienti paganti.** Le referenze verificabili sono quasi tutte pubbliche o istituzionali (FS, CDP) o di sponsorizzazione (Ducati). Le aziende citate nel contenuto proprietario sul CIO Hub 2026 (Edison, Camst, Gambero Rosso, McKinsey, BFM) sono relatori a un evento, non clienti. | Case study firmato dal cliente sul sito GELLIFY, testimonianza pubblica del cliente, o citazione della fornitura nella relazione sulla gestione / bilancio di sostenibilità del cliente. |
| 10 | Se GELLIFY **venda M&A advisory a terzi** o sia solo acquirente in proprio. Cinque acquisizioni proprie sono documentate, ma nessuna linea di servizio M&A/due diligence tecnologica compare fra le sei pubblicate. | Pagina di servizio dedicata su gellify.com, mandato pubblico di advisory, o menzione in un comunicato di operazione in cui GELLIFY figuri come advisor e non come parte. |
| 11 | La **provenienza professionale** di Gianluigi Martina, Fabio Bucci, Massimo Cannizzo, Diego Fernandez e Vincenzo Mura: i ruoli provengono da un aggregatore commerciale [S], le biografie non sono pubblicate. | Pagina leadership/team su gellify.com (attualmente assente), profili LinkedIn individuali, o visure con elenco cariche delle società del gruppo. |
| 12 | La **ripartizione dei ricavi** fra consulenza a progetto, fee di gestione acceleratori, equity/capital gain e ricavi delle società acquisite. Il modello di ricavo è ricostruito per evidenze indirette, non per dichiarazione. | Nota integrativa al bilancio con ripartizione dei ricavi per categoria di attività, oppure information memorandum o intervista con breakdown esplicito. |
| 13 | **Attività societarie e commerciali nella finestra febbraio 2025 – agosto 2026** diverse da Bianco Ventures e dal ciclo Frontech: nessuna acquisizione, nessun round, nessun nuovo contratto rilevante trovato. La sezione news di gellify.com restituisce «No results found» ai filtri. | Archivio stampa completo (Factiva/Nexis) o rassegna BeBeez/Il Sole 24 ORE dietro paywall (402 in questa sessione), oppure visura storica delle modifiche societarie del gruppo. |
| 14 | Il **terzo venture builder** implicito nel claim «3 venture builders built»: sono identificati Venture Box e Bianco Ventures; il terzo non è nominato in fonti aperte. | Pagina di dettaglio della linea venture building su gellify.com, o comunicato stampa di lancio del terzo veicolo. |


### Growth Capital

Fonte: `schede/growth-capital.md`, campo 14.

Ricerca dell'11/08/2026, sole fonti aperte. Il soggetto è stato **identificato con certezza**: Growth Capital S.r.l., P.IVA 10993370963, Piazza Generale Armando Diaz 5, Milano, dominio ufficiale attivo **`growthcapital.vc`** (il dominio storico `growthcapital.it` risponde con redirect 302 verso il `.vc`). Esclusi gli omonimi `growthcapital.co.uk`, `growthcapitalventures.co.uk`, `gcadvisory.com` (boutique M&A anch'essa milanese, con business area «Buy Side M&A») e Growth Capital Partners S.r.l. (P.IVA 12421020962). Restano aperte le seguenti questioni.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | La **compagine sociale** di Growth Capital S.r.l. e le quote dei singoli soci. Le schede camerali gratuite consultate (ufficiocamerale.it, fatturatoitalia.it, reportaziende.it) espongono P.IVA, REA, sede, ATECO, capitale e dati economici ma non l'elenco soci né l'organo amministrativo | Visura camerale ordinaria a pagamento del Registro Imprese di Milano, P.IVA 10993370963, con compagine sociale e amministratori |
| 2 | Il **rapporto societario fra Growth Capital e Growth Engine**. Il fondatore è founding partner e «major shareholder» di entrambe; Growth Engine mette il capitale in A-Road mentre Growth Capital mette l'advisory. Se ci sia partecipazione incrociata, controllo comune o solo contiguità personale è indeterminato, e cambia la lettura del modello | Visure camerali di entrambe le società con elenco soci, oppure una dichiarazione pubblica sull'assetto del gruppo |
| 3 | **Il modello di remunerazione**: retainer, success fee sul closing, percentuale sul valore dell'operazione, o combinazione. Nessuna informazione pubblica su nessuna delle pagine di servizio, sul sito A-Road, su PitchBook o nei comunicati delle operazioni. Non stimato per analogia su istruzione esplicita | Lettera di incarico o mandato tipo, prospetto informativo di un'emittente assistita che dichiari i costi di advisory, o dichiarazione dell'operatore su un'intervista |
| 4 | Se **esistano clienti corporate e bancari**, e in particolare se la linea «disegno e lancio di CVC e acceleratori» abbia mai avuto un committente. La pagina corporate è la più articolata del sito ma è l'unica delle tre pagine di servizio senza un solo cliente nominato; nessuna banca compare fra i tipi di investitore dichiarati | Comunicato congiunto con un committente corporate, case study nominativo sul sito, o menzione in un bilancio o report di sostenibilità di un'impresa che citi l'advisor del proprio CVC |
| 5 | Il **ruolo di EDF Pulse Ventures** nella lista transazioni. È l'unico nome corporate nell'elenco e la pagina non ne specifica la parte; la ricerca su fonti terze non ha prodotto alcun comunicato che leghi l'operatore a un mandato per il CVC di EDF | Comunicato stampa dell'operazione con indicazione degli advisor, o scheda di dettaglio della transazione sul sito dell'operatore |
| 6 | Se il **buy-side sia diversificato oltre Cosmico**. Le tre operazioni etichettate «Buy-Side M&A» riguardano tutte lo stesso acquirente; PitchBook conta 5 buy-side services su 69 complessivi, ma non ne nomina gli altri due | Elenco completo e datato delle transazioni con indicazione del lato del mandato, o accesso alla scheda PitchBook con il dettaglio delle cinque operazioni buy-side |
| 7 | La **consistenza reale delle sedi di Madrid e Londra**. La homepage dichiara tre uffici, ma il sito pubblica un solo indirizzo (Milano) e non è stato reperito alcun riscontro registrale o giornalistico dell'apertura britannica | Registro Mercantil spagnolo, Companies House per il Regno Unito, o pagina Contact dell'operatore con gli indirizzi delle tre sedi |
| 8 | Le **condizioni economiche e di equity di A-Road** per le scaleup partecipanti, e il rapporto contrattuale fra Growth Capital, Growth Engine e le partecipanti. Il sito dichiara l'investimento in entrata (200-500 mila euro) ma non cosa cede la scaleup | Regolamento o term sheet tipo del programma, oppure visura di una partecipante del batch 6 o 7 con elenco soci successivo all'ingresso in programma |
| 9 | La **discrepanza sull'anno di fondazione**: registro camerale 03/10/2019, PitchBook 2018. Probabilmente differenza fra avvio dell'attività e costituzione del veicolo, ma nessuna fonte lo dichiara | Pagina About con la storia della società, o intervista biografica al fondatore che dati l'avvio |
| 10 | Le **biografie individuali dei 26 nominativi del team** oltre al fondatore. La provenienza è dichiarata solo in forma collettiva («IB, VC, strategic consulting, and international law firms»), e in particolare non è identificabile chi guidi la linea corporate e chi la presenza spagnola | Pagine di dettaglio dei singoli profili sul sito, o profili LinkedIn personali consultati da browser reale |
| 11 | **Natura, dimensione e tecnologia del database proprietario** citato nel blocco «Insights & Activation» e presupposto dall'osservatorio trimestrale. Se sia un asset strutturato o una raccolta interna di fogli di lavoro cambia la valutazione del perimetro tecnico | Descrizione tecnica sul sito, demo o accesso al prodotto, o nota metodologica dell'osservatorio con la fonte dei dati |
| 12 | Il **contenuto del report sul Corporate Venture Capital in Italia** nell'edizione più recente. La pagina è indicizzata dai motori ma restituisce errore 500 in lettura diretta l'11/08/2026; è disponibile solo il riscontro indiretto sull'edizione precedente («solo 69 milioni investiti dai CVC in Italia nel 2024») | PDF del report scaricato dalla sezione Insights/VC Reports del sito, o copertura stampa dell'edizione 2026 |
| 13 | Se **A-Road generi ricavi per Growth Capital**. L'assistenza al round è dichiarata come prestata «from Growth Capital team», ma non è dichiarato se sia fatturata alle partecipanti, remunerata da Growth Engine, o scambiata con una posizione economica sul round successivo | Bilancio con nota integrativa che dettagli la composizione dei ricavi, o regolamento del programma |
| 14 | Il **bilancio dell'ultimo esercizio in forma ufficiale**. I due aggregatori consultati riportano annualità diverse (2023 e un esercizio indicato come 2025) con dati non sovrapponibili, e nessuno espone il bilancio integrale | Bilancio d'esercizio depositato al Registro Imprese di Milano |
| 15 | Il **numero e la natura delle operazioni chiuse nel 2026 fino ad agosto**. Sono verificate singole operazioni (Dronus a marzo, Cosmico-Flatmates a maggio, GR3N a giugno) ma il sito non data le transazioni e non esiste un conteggio periodico verificabile | Pagina Transactions con date, o rendiconto annuale dell'operatore, o classifica advisor su venture italiano di una fonte terza (es. Dealroom, BeBeez Private Data) |


### Tinexta Innovation Hub

Fonte: `schede/tinexta-innovation-hub.md`, campo 14.

Scheda: `schede/tinexta-innovation-hub.md` · Consultato il 11/08/2026 · Solo fonti aperte.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | L'aliquota percentuale della success fee sulla finanza agevolata e il mix fra fee fissa e compenso a risultato. L'esistenza della componente a successo è provata (tassi di successo ponderati come determinante dei ricavi, riconoscimento del credito all'89,77%), la sua misura no. | Un contratto o una convenzione associativa con condizioni economiche esposte (le convenzioni Confindustria/ASSISTAL sono la via più probabile: la pagina assistal.it è andata in timeout in questa sessione), oppure la nota integrativa del bilancio civilistico di Tinexta Innovation Hub S.p.A. depositato al Registro Imprese, alla voce criteri di riconoscimento dei ricavi e corrispettivi variabili. |
| 2 | Il peso in valore assoluto delle aree non agevolative (digital & innovation, ESG, export, digital marketing, lean) sui 156,2 milioni di ricavi 2025 della BU. La reportistica dà solo variazioni percentuali per area. | Relazione sulla gestione del bilancio separato di Tinexta Innovation Hub S.p.A., oppure una presentazione agli analisti o un fascicolo di segment reporting con lo split per area di servizio. |
| 3 | La soglia dimensionale minima del cliente (fatturato, dipendenti, taglia minima di investimento agevolabile). Il sito dichiara solo "imprese di ogni dimensione e settore". | Una brochure commerciale, una scheda di servizio con criteri di ammissibilità del cliente, o un bando/convenzione che espliciti la fascia servita. |
| 4 | Se esista una linea AI con prodotto, ricavi e clienti propri, oltre alla voce di catalogo "Soluzioni AI". La pagina dedicata ha restituito 404 in questa sessione e il piano 2026-2028 della BU non nomina l'AI. | Una presentazione commerciale della linea, un case study cliente, un comunicato di prodotto o un annuncio di lavoro che descriva ruoli e stack della linea AI. |
| 5 | Il perimetro delle società confluite nel rebrand: è stata verificata l'unione di cinque realtà nell'area Digital & Innovation (Plannet, Enhancers, Trix, Warrant Innovation Lab, PrivacyLab) più Compass360 nel gruppo, ma il numero esatto di sette società integrate e le date di fusione per incorporazione non sono stati confermati. | Atti di fusione depositati al Registro Imprese, oppure la sezione "aggregazioni aziendali / variazioni di perimetro" della Relazione Finanziaria Annuale con l'elenco delle incorporate e le date di efficacia. |
| 6 | Clienti che confermino in proprio la collaborazione. I casi disponibili (Italpizza, Avicola Alimentare Monteverde, progetto Tentacle) sono la versione dell'operatore ripresa da stampa. | Comunicati stampa, relazioni sulla gestione o bilanci di imprese clienti che nominino Warrant Hub / Tinexta Innovation Hub come advisor, oppure elenchi pubblici di beneficiari di incentivi con indicazione del soggetto proponente. |
| 7 | Organi sociali e prima linea manageriale oltre all'amministratore delegato Fiorenzo Bellelli: presidente, consiglio di amministrazione, responsabili di area. | Visura camerale ordinaria di Tinexta Innovation Hub S.p.A. con gli organi sociali, o la sezione governance del bilancio della controllata. |
| 8 | L'organico della sola Tinexta Innovation Hub S.p.A. al 31/12/2025: i 952 FTE sono l'intera BU Business Innovation (che include ABF, Euroquality, Europroject, Evalue, Lenovys, Forvalue, Queryo, Studio Fieschi), i 560 dipendenti vengono da un aggregatore. | Nota integrativa del bilancio civilistico (numero medio dei dipendenti per categoria) o dichiarazione ufficiale dell'operatore. |
| 9 | Cosa succede al perimetro e alla disclosure della BU dopo il delisting sotto Advent International / Nextalia. Con l'uscita da Euronext Star Milan si perde la fonte primaria su cui poggia quasi tutta questa scheda. | Comunicazioni post-delisting dell'offerente, bilancio consolidato 2026 della controllante non quotata depositato al Registro Imprese, o eventuali prospetti legati al debito emesso. |
| 10 | Lo stato effettivo del sottodominio `wnews.warranthub.it`, che risulta ancora indicizzato con contenuti autonomi (agevolazioni, programmi, newsletter) mentre il dominio principale reindirizza: non è stato possibile aprirlo direttamente. | Accesso diretto al sottodominio o una verifica DNS/HTTP indipendente, per stabilire se il vecchio marchio sopravviva su una linea editoriale attiva o si tratti solo di residuo di indicizzazione. |


### Plug and Play Italy

Fonte: `schede/plug-and-play-italy.md`, campo 14.

Ricerca dell'11/08/2026, sole fonti aperte. Il soggetto è stato **identificato con certezza** come **Plug and Play Italy S.r.l.**, P.IVA 10792270968, Piazza Vetra 17 Milano, filiale italiana di Plug and Play Tech Center (Sunnyvale, California). Va tenuta distinta l'omonima **Plug And Play Informatica S.r.l.** di Milano, che non è l'operatore.

**Limite metodologico che condiziona tutta la scheda:** il dominio proprietario `plugandplaytechcenter.com` risolve ma **non restituisce testo** ad alcuna forma di lettura tentata in questa sessione (lettura diretta, richiesta HTTP grezza, servizio di resa intermedio), su sei percorsi diversi. Tutte le formulazioni proprietarie riportate provengono da comunicati stampa su piattaforme terze e da pagine dei clienti. Diversi dubbi qui sotto si risolverebbero con una singola lettura del sito da browser reale.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | **Come sia strutturata la sottoscrizione in Italia**: importo in euro, numero e nome dei livelli, durata contrattuale, preavviso di recesso, se la quota includa o meno l'accesso al fondo. Le uniche cifre reperite (200.000 USD/anno Gold, 100.000 USD/anno White) sono globali, in dollari, dichiarate in un'intervista **non databile con certezza**, e riguardano la piattaforma non l'entità italiana | Un contratto di partnership corporate, oppure la **delibera o determina di aggiudicazione di CDP Venture Capital** sui programmi Motor Valley Accelerator, Takeoff e CrossConnect, che espone il valore dell'affidamento; in alternativa il bilancio depositato di Plug and Play Italy S.r.l. con la nota integrativa sulla composizione dei ricavi |
| 2 | **La data dell'intervista** da cui provengono i due livelli Gold e White. È la fonte più informativa sul modello ma non è collocabile nel tempo, quindi non si sa se descriva il listino corrente o una struttura superata | Metadati di pubblicazione dell'articolo su The Asian Banker, o una seconda fonte indipendente che riporti gli stessi livelli con una data |
| 3 | **La compagine sociale e l'organo amministrativo della S.r.l. italiana**: la percentuale detenuta dalla casa madre statunitense, l'eventuale presenza di soci italiani, i nomi degli amministratori. Le schede camerali gratuite consultate espongono sede, P.IVA, REA, ATECO, capitale e data di iscrizione ma **non** l'elenco soci | Visura camerale ordinaria a pagamento presso il Registro Imprese di Milano (P.IVA 10792270968), con compagine sociale e organo amministrativo |
| 4 | **Chi sia oggi il vertice dell'entità italiana.** Borja Aznar-Bonilla è stato nominato Managing Director per l'Italia l'11/04/2023 ma **non compare in alcuna fonte 2025-2026** fra quelle consultate; la rappresentanza pubblica dal settembre 2024 è interamente di Tommaso Maschera, con il titolo di Director. Tre titoli coesistono senza gerarchia ricostruibile | Visura camerale con l'organo amministrativo, oppure la pagina team del sito proprietario letta da browser reale, oppure la pagina LinkedIn aziendale |
| 5 | **La provenienza professionale di Tommaso Maschera**, figura pubblica di riferimento dell'entità italiana dal 2024 al 2026. Nessuna delle fonti che lo cita riporta una biografia | Profilo LinkedIn personale, biografia ufficiale sul sito, o intervista biografica su testata |
| 6 | **Se la sede di Catanzaro sia mai stata aperta.** Annunciata nell'aprile 2023 come quarto quartier generale italiano con inaugurazione prevista nel 2024 e con l'obiettivo dichiarato di «replicare il modello Ogr a Torino»; tutte le fonti successive parlano invece di **Catania** (CrossConnect, novembre 2024). Le due città vanno tenute distinte finché la questione non è risolta | Elenco delle unità locali sulla visura camerale, oppure un comunicato di inaugurazione, oppure la pagina locations del sito proprietario |
| 7 | **Se le relazioni con Nexi, A2A, UniCredit ed Esselunga siano ancora attive nel 2026.** Le pagine dei clienti sono redatte al presente e tuttora online, ma le date di riferimento sono 2019-2023 e nessuna è aggiornata | Dichiarazione di rinnovo, oppure il bilancio di sostenibilità o la relazione integrata 2025 dei committenti, oppure la pagina partner del sito dell'operatore con data |
| 8 | **Perché nessun nuovo committente corporate italiano confermato dal cliente compaia fra febbraio 2025 e agosto 2026.** Può essere assenza di nuovi contratti, oppure semplice assenza di comunicazione da parte dei clienti: le due ipotesi non sono distinguibili con le fonti aperte disponibili | Elenco partner datato sul sito dell'operatore, oppure una rassegna dei comunicati Plug and Play Italy del periodo (la pagina press del dominio proprietario e il profilo iPressLIVE, che sarebbero le fonti naturali, sono rispettivamente non leggibile e in errore 404) |
| 9 | **Il contenuto dell'iniziativa con il Politecnico di Torino del 25/02/2025** e della call **FoundHer** per startup italiane a guida femminile. Sono i due soli segnali di attività italiana propria dentro la finestra dei 18 mesi, ma dell'una si conosce solo il titolo (fonte bloccata da robots.txt) e dell'altra solo l'esistenza (pagina in errore 404) | Testo integrale dell'articolo su arenadigitale.it; comunicato FoundHer ripubblicato su altra piattaforma, o la pagina di programma sul sito dell'operatore |
| 10 | **Se i programmi CDP siano ancora in corso e a quale edizione.** Motor Valley Accelerator (dal 2021), Takeoff con la declinazione DualTech nella rete NATO DIANA (dal 2022-2024) e CrossConnect (dal 2024) risultano avviati ma non se ne è potuta verificare l'edizione corrente: `motorvalleyaccelerator.com` è attivo ma non è stato letto per redirezione, `crossconnect.it` restituisce un errore di certificato TLS per mancata corrispondenza del nome host | Lettura dei due siti di programma da browser reale; oppure il portale della Rete Nazionale Acceleratori di CDP Venture Capital con lo stato aggiornato dei programmi |
| 11 | **La ripartizione dei ricavi italiani fra quote di partnership, gestione dei programmi su commessa pubblica e riaddebiti infragruppo.** Il fatturato 2024 di 3.852.542 euro è noto nel totale ma non nella composizione, e la differenza cambia la lettura del modello: una quota associativa ricorrente e una commessa pubblica pluriennale non hanno lo stesso profilo | Bilancio d'esercizio depositato con nota integrativa, dal Registro Imprese di Milano |
| 12 | **Perché il fatturato italiano sia fermo su tre esercizi** (3,86 mln nel 2022, 3,82 nel 2023, 3,85 nel 2024) mentre il perimetro dichiarato passa da tre a cinque località. Non è determinabile se sia saturazione del numero di partner, uscita di partner compensata da ingressi, o contabilizzazione altrove nel gruppo dei ricavi delle nuove sedi | Bilanci 2023-2025 con nota integrativa; bilancio 2025 non ancora disponibile sulle fonti consultate |
| 13 | **Quale sia il verticale «GOAL»** che compare nell'elenco dei verticali globali del comunicato del 26/03/2026 accanto a Enterprise & AI, Semiconductors e Aerospace & Defense. L'acronimo non è sciolto in nessuna fonte consultata | Pagina dei verticali sul sito proprietario, o un comunicato dedicato al lancio del verticale |
| 14 | **Se Lavazza sia ancora partner e in quale forma.** È indicata come «partner fondatore» dalla sola stampa di settore del 2019 e citata da Nexi nella descrizione del verticale food; esiste una pagina partner sul dominio dell'operatore, che è però fonte dichiarativa. **Nessun documento su dominio Lavazza è stato trovato** | Pagina o comunicato su lavazzagroup.com, oppure la relazione di sostenibilità del gruppo Lavazza che nomini il fornitore |
| 15 | **Il testo proprietario dell'operatore**: payoff breve di sito, descrizione pubblica dei livelli di membership, elenco ufficiale dei partner corporate italiani, organigramma. Tutto ciò è presumibilmente pubblicato sul dominio proprietario ma **non è stato leggibile** | Lettura di `plugandplaytechcenter.com` e dei percorsi `/italy`, `/locations/milan`, `/corporate-innovation`, `/press/italy-summit-2025` **da browser reale**, con resa JavaScript |


### Infinite Area

Fonte: `schede/infinite-area.md`, campo 14.

**Analisi competitor V2 · Deploiable · compilato il 11/08/2026**
Elenco di ciò che non è stato possibile determinare da fonti aperte in questa sessione, con la fonte che servirebbe per chiuderlo.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | **La ripartizione dei ricavi fra affitti/eventi e consulenza.** Il fatturato 2024 è noto (1.507.963 euro) ma non disaggregato. Il codice ATECO principale è immobiliare (68.20.02) e il margine netto del 10,3% con 7 dipendenti è coerente con la gestione di spazi, non con la consulenza: la componente consulenziale non è quantificabile. | Bilancio depositato con nota integrativa 2024 e 2025, via visura camerale a pagamento o Registro Imprese Telemaco. In alternativa, la scheda aggiornata dell'Osservatorio Open Innovation Lookout, che nel 2022 raccoglieva la ripartizione per dichiarazione dell'operatore. |
| 2 | **L'assetto proprietario: chi sono i soci e con quali quote.** È verificato che la società appartiene all'ecosistema Infinite Group presieduto da Patrizio Bof, ma nessun aggregatore consultato espone la compagine sociale né l'eventuale presenza di una holding o di soci terzi. | Visura camerale ordinaria con elenco soci (Registro Imprese). |
| 3 | **Lo scarto fra costituzione societaria (09/07/2013) e nascita dichiarata del brand (2015).** Non è chiaro se la società sia nata con altro oggetto sociale e altra denominazione e sia stata poi riconvertita al progetto Infinite Area. | Visura storica con gli atti di modifica di denominazione e oggetto sociale. |
| 4 | **Se esista anche un solo cliente pagante nominabile sulla linea AI o sulla linea open innovation.** Ricerca esaustiva a esito negativo: nessuna pagina casi studio, nessuna referenza, nessun logo, `/partner/` in 404. È il vuoto probatorio più rilevante della scheda. | Una dichiarazione del cliente stesso: comunicato aziendale, intervista o case study pubblicato dal committente. In alternativa il profilo LinkedIn aziendale con post di progetto, non consultabile in sessione (robots.txt). |
| 5 | **Oggetto, importo unitario, stazione appaltante e date dei 5 contratti pubblici da 346.174 euro complessivi (2021-2026).** Il totale aggregato è noto da aggregatore, il dettaglio no. È l'unica traccia certa di committenza pagante e va aperta. | ANAC / Portale Nazionale Contratti Pubblici, sezioni Amministrazione Trasparente degli enti veneti committenti, TED per le soglie comunitarie. |
| 6 | **Se Infinite Area riceva un contributo diretto per «Spazio al Non Spazio» o presti l'attività a titolo non oneroso.** Il ruolo di co-organizzatore con Regione del Veneto, ESA e Agenda Digitale del Veneto è verificato; il flusso economico sottostante no. Risultano 11.630 euro di aiuti di Stato 2021-2026, senza causale. | Delibere e decreti della Regione del Veneto su `bandi.regione.veneto.it`, Registro Nazionale Aiuti di Stato (RNA) per il dettaglio delle causali, convenzioni pubblicate da Agenda Digitale del Veneto. |
| 7 | **Se Infinite Area sia partner in progetti europei finanziati.** La scheda Copernicus prova solo l'appartenenza a un network di contatti, non un ruolo in un consorzio. Nessun record attribuibile con certezza è emerso in sessione. | Ricerca per partita IVA (04610440267) su CORDIS, Kohesio e Funding & Tenders Portal della Commissione. |
| 8 | **L'organigramma effettivo dopo il riposizionamento AI-first: se Marco Battistella sia ancora Open Innovation Director e chi guidi la funzione tecnica.** Il ruolo di Battistella viene da Crunchbase e dalla scheda Lookout, entrambe anteriori al pivot; nessuna menzione in materiali 2025-2026. Nessun CTO identificato. | LinkedIn (bloccato da robots.txt in sessione) o una pagina «team» sul sito, che oggi non esiste. |
| 9 | **La provenienza professionale delle tre persone chiave** (Patrizio Bof, Marco Battistella, Giovanni Fagherazzi). Nessuna biografia pubblicata su alcuna fonte consultata. | LinkedIn, oppure profili relatore di conferenze di settore, oppure interviste in cui il percorso venga ripercorso. |
| 10 | **Il perimetro tecnico reale: stack, cloud provider, partnership con vendor AI, certificazioni.** Le capacità dichiarate (agenti autonomi, LLM on-premise, integrazione industriale) non hanno alcun riscontro tecnico pubblico, e la società sta cercando ora il proprio AI Engineer. | Repository pubblici, pagine partner dei vendor (Microsoft, AWS, NVIDIA, Google Cloud partner directory), annunci di lavoro dettagliati con requisiti di stack. |
| 11 | **Se lo Startup Studio sia ancora attivo e se abbia prodotto venture dopo Da Mario e H4H.** Il modello è documentato dalla stampa 2025 ma è assente dal sito attuale, interamente riorganizzato sulle cinque linee IA. | Registro Imprese per società costituite con Infinite Area fra i soci; sezione startup innovative del Registro Imprese; comunicati dell'operatore successivi a giugno 2025. |
| 12 | **Il contenuto dell'articolo di Industria Italiana su AI e aerospace** (`industriaitaliana.it/ia-aerospace-infinite-area/`), che dal titolo è il pezzo più direttamente rilevante sulla strategia AI dell'operatore ma restituisce HTTP 402 (paywall). Analogamente inaccessibili l'articolo StartupItalia sullo Startup Studio di Milano (403) e Innovation Nation (robots.txt). | Abbonamento a Industria Italiana; oppure ripresa dello stesso contenuto su testata accessibile; oppure archivio web della pagina. |
| 13 | **Il numero reale di aziende e persone ospitate nel campus e la superficie in metri quadri.** L'operatore dichiara «circa 200 professionisti», la stampa non quantifica mq né numero di imprese insediate, e il portale community `hub-workspace` richiede autenticazione. | Portale community autenticato, presentazione istituzionale o media kit dell'operatore, schede di progetto degli studi di architettura che hanno realizzato il campus. |
| 14 | **Le tariffe: né listino consulenza, né quote di membership del coworking.** Nessun prezzo pubblico su alcun canale, incluse le directory di coworking. | Portale `hub-workspace.infinitearea.com` previa registrazione; richiesta commerciale diretta; directory di coworking con listini (nessuna di quelle consultate espone le tariffe). |


### Bridgemaker

Fonte: `schede/bridgemaker.md`, campo 14.

**Scheda:** `schede/bridgemaker.md` · **Riga:** `dati/righe/bridgemaker.csv` · **Data di consultazione:** 11/08/2026
**Limite di sessione da dichiarare:** il budget di WebSearch si è esaurito (200/200) durante la ricerca; le verifiche successive sono state fatte come letture dirette di pagina via fetch. LinkedIn non è risultato consultabile. `reportaziende.it` e `companyhouse.de` restituiscono 403; `bridgemaker.de` non risponde.

| # | Cosa non è stato determinato | Fonte che servirebbe |
|---|---|---|
| 1 | I nomi e le percentuali dei **due soci di BridgeMaker GmbH**. Il registro conferma che esistono due soci attivi ma li tiene dietro paywall; è noto solo che Henrike Luszick ha la maggioranza dal buy-out 2021 e che esiste un gruppo di equity partner, senza quote. | **Gesellschafterliste** depositata presso l'Amtsgericht Berlin-Charlottenburg, HRB 179174 B — estratto a pagamento da NorthData o dall'Unternehmensregister tedesco. |
| 2 | La **ripartizione delle quote di BC VENTURES S.R.L.** (P.IVA 13511430962, Via Pellegrini 22, Milano) fra Bridgemaker e Factory Plus, e chi la amministra. Entrambe le parti la chiamano «joint venture» senza mai pubblicare percentuali né organi. Non è nemmeno accertato se sia paritetica. | **Visura camerale con elenco soci** della Camera di Commercio di Milano Monza Brianza Lodi su P.IVA 13511430962. Gli aggregatori gratuiti consultati (xrayfinance.it) non espongono la compagine; reportaziende.it restituisce 403. |
| 3 | **Chi incassa che cosa sul mandato Maritime Ventures.** Il veicolo BC Ventures ha ricavi 0 e 0 dipendenti nel 2024: i corrispettivi non passano da lì. Non è determinabile se Bridgemaker sia pagata a fee direttamente dal committente, remunerata in equity nelle venture costruite, o entrambe, né in quale proporzione rispetto a Factory Plus. | **Bilancio 2025 di BC Ventures S.r.l. con nota integrativa**; oppure bilancio di **Maritime Ventures S.r.l.** (P.IVA 02955220997); oppure delibera/contratto di **CDP Venture Capital** sul Fondo Boost Innovation relativo al programma. |
| 4 | Il **fatturato di BridgeMaker GmbH** per qualunque esercizio. I bilanci 2017-2024 risultano depositati ma gli importi sono a pagamento; Dealroom espone i tassi di crescita 2018-2023 (+154% nel 2019, +40% nel 2021) con gli importi oscurati. Manca quindi anche il dato di come si sia mossa l'azienda durante il riposizionamento del 2024. | **Estratto del Bundesanzeiger** (Jahresabschluss) per gli esercizi 2023 e 2024, o accesso premium a NorthData / Dealroom. |
| 5 | La **percentuale della componente outcome-based** sulla remunerazione totale e il meccanismo di calcolo, in particolare per la quota agganciata all'**Unternehmenswert**. Il sito dichiara che «una parte» del compenso è legata a risultati misurabili e che decade se il risultato non arriva, ma non quantifica nulla. | **Lettera d'incarico o term sheet** di un progetto Commercial OS; in alternativa una testimonianza diretta e attribuibile di un cliente private equity. |
| 6 | Se Bridgemaker abbia **altri mandati o veicoli italiani** oltre a Maritime Ventures, in corso o in trattativa, con committenti diversi da CDP Venture Capital. La ricerca ha dato esito negativo, ma per sola assenza di menzione: è lo stesso limite che aveva nascosto l'operatività italiana nella prima mappatura. | **Verbali o delibere di CDP Venture Capital** e delle fondazioni bancarie; **annunci di lavoro con sede italiana** su portali tedeschi e italiani; **lista clienti aggiornata di Factory Plus** dopo il rebranding. |
| 7 | Che cosa succede a **B-C Ventures dopo maggio 2027**, alla scadenza dichiarata del programma Maritime Ventures: se la JV prosegue con altri mandati, resta come holding delle partecipazioni, o viene liquidata. | **Dichiarazione dei soci della JV** o **piano industriale di Factory Plus** successivo al rebranding di luglio 2026. |
| 8 | Se **Tautiom AI** sia licenziabile separatamente dal mandato di consulenza, e a quali condizioni. Sul sito compare solo come «Delivery-Plattform» interna; non esistono pagina prodotto, pricing né accesso self-service. Da questo dipende se la componente AI sia prodotto o solo consulenza. | **Pagina prodotto o contratto di licenza** di Tautiom AI; in alternativa una richiesta diretta all'operatore o un cliente che dichiari di averla in licenza. |
| 9 | La **provenienza professionale** di Henrike Luszick e dei quattro equity partner attuali (Hofmann, Bussian, Esser, Peter), oltre che di Henkensiefken e Sanders. La pagina Über uns sostituisce le biografie con una formula di postura. | **Profili LinkedIn** dei sette (non consultabili in questa sessione) o profili biografici sulla stampa di settore tedesca (consulting.de, marktforschung.de, Handelsblatt). |
| 10 | Il **numero reale di dipendenti nel 2026**. Gli aggregatori danno fasce discordanti (51-100 su Startbase, 51-200 su Dealroom) e l'unico numero puntuale reperito — «circa 100» — risale al 2021, cioè a prima del riposizionamento. | **Dato di organico dal bilancio depositato** (Bundesanzeiger) o dichiarazione dell'operatore. |
| 11 | Se le **referenze corporate diverse da Jungheinrich** (Landgard, RENK, Greiner Packaging, Bernard Krone, BLANC & FISCHER, TRUMPF, Henkel, BASF, Volkswagen) siano confermate dai clienti stessi. Al momento sono citate solo dall'operatore; solo Jungheinrich ha una testimonianza nominale, e comunque ospitata sul sito di Bridgemaker. | **Comunicati o pagine sui domini dei clienti** (jungheinrich.com, renk.com, landgard.de, ecc.), o riprese di stampa di settore tedesca. |
| 12 | Il **momento e la forma del riposizionamento 2024**. La timeline «2024 rebranding come consulenza AI-nativa» è dichiarata solo sulla pagina Über uns: non è stato trovato un comunicato stampa datato né una copertura giornalistica del cambio di categoria. | **Comunicato stampa dell'operatore** o **copertura su stampa di settore tedesca**; in alternativa snapshot storici del sito (Wayback Machine) per datare il cambio di homepage. |
| 13 | Gli **esiti economici realizzati** delle venture costruite in Italia: ricavi, exit, ritorno per gli investitori. Sono pubblici solo i conteggi (7 costruite, 3 scorporate, 4 MVP) e le valutazioni seed dichiarate (4-10 mln). | **Bilanci delle società scorporate** da Registro Imprese; comunicati di round su BeBeez / VCWire / CDP Venture Capital. |
| 14 | Il **perimetro delle 7 partecipazioni attive** intestate a BridgeMaker GmbH nel registro tedesco (fra cui ATOLL Living Spaces, Circulix, aboDeinauto): se siano venture di clienti, venture proprie, o partecipazioni residue. Da questo dipende se esista una linea equity propria oltre ai veicoli con partner. | **Estratto NorthData premium** sulle Beteiligungen, o visure delle singole partecipate. |
