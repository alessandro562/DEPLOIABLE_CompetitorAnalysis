#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Catalogo d'offerta e profili di competenza.

Cambio di modello rispetto a competitor.json: l'unita' di analisi non e' piu'
l'operatore con dei punteggi, ma il SINGOLO SERVIZIO VENDUTO, con la sua fonte,
la sua data e la sua marcatura. Un operatore e' la somma dei suoi servizi.

Marcature: V verificato da terzi · D dichiarato dall'operatore · S stimato · N non trovato
"""
import json

# ------------------------------------------------------------------ vocabolari
TIPI = {
  "assessment":      "Diagnosi e mappatura",
  "formazione":      "Formazione e academy",
  "governance":      "Policy, compliance, AI Act",
  "progettazione":   "Strategia e roadmap",
  "sviluppo-agenti": "Sviluppo di agenti e automazioni",
  "sviluppo-prodotto":"Sviluppo di prodotto su misura",
  "piattaforma":     "Piattaforma proprietaria a licenza",
  "integrazione":    "Integrazione sui sistemi esistenti",
  "gestione":        "Esercizio e managed services",
  "scouting":        "Scouting e matching con startup",
  "venture-building":"Costruzione di imprese",
  "advisory":        "Advisory su capitale e M&A",
  "talent":          "Ricerca e inserimento di personale",
}
LINEE = {"ai":"AI Adoption","oi":"Open Innovation","vb":"Venture Building",
         "ma":"M&A buy-side","fuori":"Fuori dal nostro perimetro"}
CAPACITA = ["Non tocca codice","Integra strumenti di terzi",
            "Sviluppa su stack altrui","Sviluppa tecnologia propria"]
INCASA = ["Tutto in subappalto","Coordina, esegue poco",
          "Esegue il grosso in casa","Interamente in casa"]
PROFILI = {"ingegneri":"Ingegneri e sviluppatori","data":"Data scientist e ML",
  "economics":"Economics e finance","design":"Designer","consulenti":"Consulenti",
  "commerciali":"Commerciali e account","ricerca":"Ricercatori","formatori":"Formatori"}

S = []
def s(op, nome, tipo, linea, consegna, durata, prezzo, prova, fonte, mk, data="08/2026"):
    S.append(dict(op=op, nome=nome, tipo=tipo, linea=linea, consegna=consegna,
                  durata=durata, prezzo=prezzo, prova=prova, fonte=fonte, mk=mk, data=data))

C = {}
def comp(op, **k): C[op] = k

# ==================================================================== NOI
comp("deploiable", composizione=["economics","consulenti"], headcount=6, headcount_mk="D",
  capacita=1, in_casa=2, stack=["strumenti generalisti"], deploy=["non dichiarato"],
  proprietario=["metodologia lean startup applicata a qualunque verticale"],
  nota="Tutto il team ha background economics e finance. Le competenze AI sono in "
       "costruzione. L'MVP si costruisce in casa, poi un tech partner porta a TRL 8-9. "
       "E' il punto in cui il modello si interrompe e il cliente cambia interlocutore.")
s("deploiable","Open innovation su commessa","scouting","oi",
  "Scouting startup per corporate venture clienting o acquisizione diretta","non dichiarata",
  "non esposto","Comtel, Braga Moro, Cipierre, Marchiani, SFS","interno","D")
s("deploiable","Corporate venture building","venture-building","vb",
  "Supporto allo sviluppo di un asset interno all'azienda","non dichiarata",
  "non esposto","Stellantis (team innovation interno)","interno","D")
s("deploiable","AI adoption","assessment","ai",
  "Diagnosi del processo che conviene toccare, poi MVP","non dichiarata",
  "non esposto","nessun caso pubblicato","interno","N")
s("deploiable","M&A buy-side","advisory","ma",
  "Assistenza a chi compra","non dichiarata","non esposto","nessun mandato documentato",
  "interno","N")
s("deploiable","Posizionamento e lead generation di prodotto","progettazione","fuori",
  "Rebranding, sito, strategia di posizionamento, gestione lead. La chiusura la fanno i "
  "sales del cliente","12 mesi","recurring fee + success fee sui lead","Marchiani Automation",
  "interno","D")

# ==================================================================== YELLOW TECH
comp("yellow-tech", composizione=["ingegneri","formatori","data"], headcount=30, headcount_mk="D",
  capacita=3, in_casa=3,
  stack=["OpenAI","Anthropic","Google","Meta","Mistral","RAG","vector database","self-hosted"],
  deploy=["tenant del cliente su Azure/AWS/GCP","on-premise"],
  proprietario=["piattaforma di gestione del ciclo di adozione","AIFIA (associazione fondata da loro)"],
  nota="Multi-modello e vendor-agnostic dichiarato. Team dedicati di AI Engineer per "
       "ciascuna delle quattro practice. La piattaforma trasforma la consulenza in ricavo "
       "ricorrente: e' l'asset che gli altri della sua arena non hanno.")
s("yellow-tech","AI Adoption Assessment","assessment","ai",
  "Distribuzione dell'assessment su tutta la popolazione aziendale, report automatici con "
  "indicazioni operative, dati aggregati e benchmark di settore","non dichiarata",
  "non esposto","minimo 50 rispondenti cross-funzionali dichiarato","yellowtech.it/ai-adoption","D")
s("yellow-tech","AI Leadership","formazione","ai","Percorso per il management","non dichiarata",
  "non esposto","parte dei 20.000+ formati","yellowtech.it/ai-adoption","D")
s("yellow-tech","AI Upskilling","formazione","ai",
  "Percorsi digitali con video, esercizi, quiz e tracking del completamento, su tutti i livelli",
  "sei moduli combinabili","non esposto","20.000+ persone formate in 500+ organizzazioni",
  "yellowtech.it/ai-adoption","D")
s("yellow-tech","Redazione AI Policy","governance","ai",
  "Stesura della policy aziendale sull'uso dell'AI","non dichiarata","non esposto",
  "non nominata","yellowtech.it/ai-adoption","D")
s("yellow-tech","Programma AI Champion","formazione","ai",
  "Costruzione di referenti interni che guidano l'adozione","non dichiarata","non esposto",
  "non nominata","yellowtech.it/ai-adoption","D")
s("yellow-tech","Piattaforma di adozione","piattaforma","ai",
  "Gestione dell'intero ciclo di adozione: assessment, percorsi, dashboard per HR e "
  "management, benchmark","licenza","non esposto","dichiarata proprietaria",
  "yellowtech.it/ai-adoption","D")
s("yellow-tech","Agenti · Finance & Document Automation","sviluppo-agenti","ai",
  "Ciclo documentale e finanziario: fatture XML da SDI, DDT, contratti, ordini d'acquisto, "
  "note spese, PEC","4-8 settimane per processo","quotato su misura",
  "300+ agenti in produzione dichiarati sul totale delle practice","yellowtech.it/ai-agents","D")
s("yellow-tech","Agenti · Customer Operations","sviluppo-agenti","ai",
  "Automazione delle operazioni di servizio al cliente","4-8 settimane per processo",
  "quotato su misura","Bocconi, Atlante, Nital, Growens fra i casi documentati",
  "yellowtech.it/ai-agents","D")
s("yellow-tech","Agenti · Sales & Revenue","sviluppo-agenti","ai",
  "Automazione su vendite e ricavo","4-8 settimane per processo","quotato su misura",
  "non disaggregata","yellowtech.it/ai-agents","D")
s("yellow-tech","Agenti · Governance & Compliance","governance","ai",
  "AI Risk Assessment Agent, AI Registry Agent, Regulatory Change Monitor, GDPR-AI "
  "Compliance Agent. Valutazione dei sistemi rispetto all'AI Act, registro obbligatorio, DPIA",
  "4-8 settimane per processo","quotato su misura",
  "practice aperta con la guida AI Act pubblicata a giugno 2026","yellowtech.it/ai-agents","D")

# ==================================================================== DATAPIZZA
comp("datapizza", composizione=["ingegneri","data","commerciali"], headcount=90, headcount_mk="V",
  capacita=3, in_casa=3,
  stack=["OpenAI","Anthropic","Gemini","modelli open source","RAG","agenti"],
  deploy=["integrazione sui sistemi del cliente"],
  proprietario=["Datapizza AI (suite di prodotti)","community da 500.000 persone"],
  nota="Vendor-neutral dichiarato. Eta' media bassa per scelta: assumono chi ha appena "
       "finito la formazione su AI. La community e' insieme canale commerciale e bacino di "
       "reclutamento — e viene monetizzata due volte, con la formazione e con il placement.")
s("datapizza","Analisi e mappatura dei processi","assessment","ai",
  "Analisi dei processi e definizione della strategia di adozione","non dichiarata",
  "non esposto","100+ aziende in portafoglio: 20 corporation, 80 fra PMI e startup",
  "datapizza.tech · Il Sole 24 Ore","D")
s("datapizza","Percorsi di formazione e change management","formazione","ai",
  "Sessioni pratiche in cui i dipendenti usano gli strumenti, mappatura delle competenze "
  "interne, azioni di change management","non dichiarata","non esposto",
  "dichiarato come prima attivita' che fanno entrando","datapizza.tech","D")
s("datapizza","Sviluppo e messa in produzione di soluzioni AI","sviluppo-agenti","ai",
  "Progettazione e sviluppo di sistemi AI per contesti enterprise, integrati nei sistemi "
  "informativi esistenti","non dichiarata","non esposto","Allianz, Credem",
  "Forbes Italia 23/07/2026","V")
s("datapizza","Datapizza AI","piattaforma","ai",
  "Suite proprietaria per agenti e RAG: interfacce, comportamento prevedibile, visibilita' "
  "end-to-end, orchestrazione dal PoC alla scala","licenza","non esposto",
  "dichiarata integrabile e personalizzabile, con misura del ROI","datapizza.tech","D")
s("datapizza","Jobs · ricerca e inserimento di talenti tech","talent","fuori",
  "Match fra aziende e talenti tech dalla community. Pagano sia la formazione sia "
  "l'assunzione","non dichiarata","fee sull'assunzione, cresce col livello inserito",
  "120 programmatori assunti presso clienti","Il Sole 24 Ore","D")
s("datapizza","Verticale Manufacturing enterprise","progettazione","ai",
  "Value proposition di AI Transformation costruita su un settore specifico","in costruzione",
  "non esposto","assunzione aperta di un Sales Industry Leader Manufacturing",
  "datapizza.tech/jobs","V")

# ==================================================================== M-AI
comp("m-ai", composizione=["ingegneri"], headcount=0, headcount_mk="N",
  capacita=2, in_casa=3, stack=["OCR","computer vision","NLP"],
  deploy=["integrazione sul gestionale del cliente"], proprietario=[],
  nota="Organico e fatturato non esposti. La forza e' nei casi: sei processi industriali "
       "reali con clienti nominati, che e' esattamente cio' che manca a quasi tutti gli altri.")
s("m-ai","Prima call conoscitiva","assessment","ai",
  "Conoscenza dell'azienda, obiettivi, dove l'AI puo' incidere","una call","gratuito",
  "ingresso dichiarato","m-ai.it","D")
s("m-ai","Mappatura processi e prioritizzazione","assessment","ai",
  "Mezza giornata per business unit con i team operativi, raccolta dati reali, matrice "
  "impatto-fattibilita' per scegliere i quick win","mezza giornata per unit","non esposto",
  "sei casi documentati","m-ai.it","D")
s("m-ai","Automazioni documentali","sviluppo-agenti","ai",
  "OCR avanzato che legge bolle e ordini da PDF e scansioni, popola il gestionale e verifica "
  "i codici articolo a database","non dichiarata","non esposto",
  "Tomatis Lamiere, Gualini Lamiere","m-ai.it","D")
s("m-ai","Automazioni su contenuti tecnici e immagini","sviluppo-agenti","ai",
  "Generazione di manuali d'uso e manutenzione, catalogazione e tagging automatico di "
  "immagini","non dichiarata","non esposto","SGI, Circet Italia, Energy Italy, MEF",
  "m-ai.it","D")

# ==================================================================== GELLIFY
comp("gellify", composizione=["ingegneri","consulenti","data"], headcount=133, headcount_mk="V",
  capacita=3, in_casa=3, stack=["agentic factory","piattaforme digitali"],
  deploy=["sistemi del cliente"],
  proprietario=["Venture Box","Bianco Ventures (con Deloitte e Arad)"],
  nota="ATECO 62201 sull'entita' operativa: e' una societa' di consulenza informatica con "
       "CTO in organico, non uno studio di advisory. E' l'unico del panel che copra tutte e "
       "quattro le nostre linee con veicoli reali.")
s("gellify","Strategy & AI Transformation","progettazione","ai",
  "Strategia di trasformazione con l'AI come baricentro","non dichiarata","non esposto",
  "quattro delle sei linee di servizio sono esplicitamente AI","gellify.com","D")
s("gellify","Data & AI","integrazione","ai","Dati e intelligenza artificiale sui sistemi del cliente",
  "non dichiarata","non esposto","non disaggregata","gellify.com","D")
s("gellify","Digital Platforms · agentic factory","sviluppo-agenti","ai",
  "Costruzione di piattaforme e agenti","non dichiarata","non esposto","non disaggregata",
  "gellify.com","D")
s("gellify","Ecosystem & network","scouting","oi",
  "Rete proprietaria di open innovation che collega startup, corporate e innovation manager",
  "non dichiarata","non esposto","due acceleratori CDP; lotto accordo quadro Gruppo FS",
  "gellify.com · cdpventurecapital.it","V")
s("gellify","AI-native venture building","venture-building","vb",
  "Creazione di imprese AI-native su commessa e in proprio","non dichiarata","non esposto",
  "3 venture builder costruiti, 15+ venture create (dichiarato)","gellify.com","D")
s("gellify","Creative Experience","sviluppo-prodotto","fuori","Esperienza e design",
  "non dichiarata","non esposto","non disaggregata","gellify.com","D")

# ==================================================================== ROOTBOX
comp("rootbox", composizione=["ingegneri","design"], headcount=0, headcount_mk="N",
  capacita=3, in_casa=3, stack=["AI conforme UE","sovranita' del dato"],
  deploy=["infrastruttura del cliente"], proprietario=[],
  nota="Product factory: la competenza e' tecnica e di design, non di impresa. Costruisce "
       "cio' che gli viene chiesto. Per noi e' fornitore a valle dell'MVP prima che concorrente.")
s("rootbox","Product Strategy","progettazione","fuori",
  "Direzione di prodotto con orizzonte di lungo periodo","non dichiarata","non esposto",
  "nessun cliente nominato","werootbox.com","D")
s("rootbox","Experience & Design Systems","sviluppo-prodotto","fuori",
  "Design system inclusivi e accessibili","non dichiarata","non esposto","nessun cliente nominato",
  "werootbox.com","D")
s("rootbox","Engineering & Delivery","sviluppo-prodotto","fuori",
  "Costruzione con attenzione a qualita', resilienza e impronta digitale","non dichiarata",
  "non esposto","nessun cliente nominato","werootbox.com","D")
s("rootbox","Applied AI","integrazione","ai",
  "Intelligenza trasparente e conforme UE, con sovranita' del dato e controllo del cliente",
  "non dichiarata","non esposto","nessun cliente nominato","werootbox.com","D")

# ==================================================================== TEAMSYSTEM
comp("teamsystem", composizione=["ingegneri","commerciali"], headcount=0, headcount_mk="N",
  capacita=3, in_casa=3, stack=["AI dentro la suite gestionale"],
  deploy=["cloud proprietario"],
  proprietario=["TeamSystem AI Agent","Fatture in Cloud","TeamSystem Enterprise Cloud","Danea"],
  nota="Non vende AI: vende software che ha l'AI dentro. La competenza decisiva non e' "
       "tecnica ma distributiva — la rete di commercialisti e consulenti del lavoro, che "
       "e' il canale attraverso cui la PMI italiana compra qualunque cosa.")
s("teamsystem","AI dentro il gestionale di studio","integrazione","ai",
  "Modulo AI e automazione contabile per commercialisti e consulenti del lavoro: "
  "monitoraggio normativo, segnalazione di modifiche, azioni correttive","incluso nella licenza",
  "dentro l'abbonamento","oltre 2 milioni di clienti sul gruppo","teamsystem.com","D")
s("teamsystem","AI dentro l'ERP","integrazione","ai",
  "ERP potenziato dall'AI, controllo di gestione predittivo","incluso nella licenza",
  "dentro l'abbonamento","TeamSystem AI Agent: 60 milioni di predizioni in 12 mesi",
  "teamsystem.com · lucasammarco.com","D")
s("teamsystem","Fatture in Cloud","piattaforma","ai",
  "Gestionale per microimprese e forfettari con AI nella riconciliazione bancaria","abbonamento",
  "da 4 a 51 euro al mese","listino pubblico","lucasammarco.com","V")
s("teamsystem","Verticali con AI integrata","piattaforma","ai",
  "Studi legali, HR, hospitality, gestione PEC: ciascuno con la propria AI","abbonamento",
  "a listino per verticale","suite piu' estesa del mercato italiano per copertura verticale",
  "teamsystem.com","D")

# ==================================================================== SEEDBLE
comp("seedble", composizione=["consulenti"], headcount=0, headcount_mk="N",
  capacita=1, in_casa=2, stack=[], deploy=["non applicabile"],
  proprietario=["Rocket Lab","BLENDX (societa' separata)"],
  nota="Nessuna evidenza di capacita' di sviluppo interna. L'unica venture costruita e' la "
       "propria. Il valore e' nel formato commerciale — sono gli unici a esporre il prezzo.")
s("seedble","Inspiration Session","formazione","oi","Sessione introduttiva","una sessione",
  "800 euro + IVA","prezzo esposto sul sito","seedble.com","D")
s("seedble","Emerging Tech Program (ETP)","assessment","ai",
  "Analisi dei bisogni, tre workshop tecnologici, sessione col management, report","60 giorni",
  "3.000 euro + IVA","unico prezzo pubblico su un servizio d'innovazione in tutto il panel",
  "seedble.com","D")
s("seedble","Rocket Lab","scouting","oi",
  "Scouting, call for startup, hackathon, PoC, accelerazione","non dichiarata",
  "non esposto","22 loghi, zero casi con obiettivo e risultato","seedble.com","N")
s("seedble","BLENDX","piattaforma","fuori","Licenza software in abbonamento, societa' separata",
  "abbonamento","non esposto","venture propria","seedble.com","D")

# ==================================================================== CEFRIEL
comp("cefriel", composizione=["ricerca","ingegneri","data"], headcount=0, headcount_mk="N",
  capacita=3, in_casa=3, stack=["AI & Data"], deploy=["sistemi del cliente"],
  proprietario=["marchio e rete del Politecnico di Milano"],
  nota="Centro di ricerca: la garanzia e' istituzionale. Uno dei tre soli operatori su 46 a "
       "presidiare il territorio verbale del risultato misurabile.")
s("cefriel","AI & Data","sviluppo-prodotto","ai",
  "Progetti di intelligenza artificiale e dati su commessa","non dichiarata","non esposto",
  "sette clienti nominati","cefriel.com","D")
s("cefriel","Innovazione su commessa","progettazione","oi",
  "Progetti di innovazione per grandi imprese, PMI e PA","non dichiarata","non esposto",
  "partecipante in 5 procedure lombarde, zero aggiudicazioni","open data Regione Lombardia","V")
s("cefriel","Formazione tecnica","formazione","ai","Percorsi su tecnologie e dati",
  "non dichiarata","non esposto","non disaggregata","cefriel.com","D")

# ==================================================================== LASTING DYNAMICS
comp("lasting-dynamics", composizione=["ingegneri"], headcount=0, headcount_mk="N",
  capacita=3, in_casa=3, stack=["AI custom","GDPR-first","DPIA","NIS2"],
  deploy=["settori regolamentati"], proprietario=[],
  nota="Occupa gia' il territorio della conformita' applicata all'AI — quello che l'AI Act "
       "ha appena aperto — con competenza tecnica vera su finance, sanita' e PA.")
s("lasting-dynamics","AI custom per settori regolamentati","sviluppo-prodotto","ai",
  "Sistemi AI su misura con approccio GDPR-first, DPIA e conformita' NIS2 integrate dalle "
  "prime fasi","non dichiarata","non esposto","posizionamento su finance, sanita' e PA",
  "sectorpunk.com (ranking di settore)","S")
s("lasting-dynamics","Software su misura","sviluppo-prodotto","fuori",
  "Sviluppo custom con conoscenza del quadro normativo italiano: Codice dei Contratti "
  "Pubblici, linee guida AGID, SDI e FatturaPA","non dichiarata","non esposto",
  "non nominati","sectorpunk.com","S")

if __name__ == "__main__":
    d = json.load(open("competitor.json", encoding="utf-8"))
    per_op = {}
    for x in S:
        per_op.setdefault(x["op"], []).append(x)
    fatti = 0
    for o in d["operatori"]:
        o["competenze"] = C.get(o["slug"])
        o["catalogo"] = per_op.get(o["slug"], [])
        o["mappato"] = bool(o["catalogo"])
        if o["mappato"]: fatti += 1
    d["vocabolari"].update(tipi=TIPI, linee_srv=LINEE, capacita=CAPACITA,
                           incasa=INCASA, profili=PROFILI)
    json.dump(d, open("competitor.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"operatori con catalogo: {fatti} su {len(d['operatori'])}")
    print(f"servizi mappati: {len(S)}")
    print()
    from collections import Counter
    print("servizi per tipo:")
    for t, n in Counter(x["tipo"] for x in S).most_common():
        print(f"  {n:3d}  {TIPI[t]}")
    print()
    print("copertura per operatore:")
    for k, v in sorted(per_op.items(), key=lambda x: -len(x[1])):
        tipi = sorted({x['tipo'] for x in v})
        print(f"  {len(v):2d}  {k:20s} {', '.join(tipi)}")
    print()
    pub = [x for x in S if "euro" in x["prezzo"] or "$" in x["prezzo"] or "gratuito" in x["prezzo"]]
    print(f"servizi con un prezzo reale: {len(pub)} su {len(S)}")
    for x in pub: print(f"   {x['op']:16s} {x['nome'][:38]:40s} {x['prezzo']}")
