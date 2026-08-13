#!/usr/bin/env python3
"""Estrae il contenuto della cartella analisi-competitor in un unico JSON,
usato poi da costruisci.py per generare la dashboard HTML autoconsistente.

Non inventa nulla: converte i markdown esistenti in HTML e struttura le
tabelle già presenti. Se un file cambia, si rilancia questo script.
"""

import csv
import io
import json
import os
import re

import mistune

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "dashboard", "dati.json")

SCHEDE = [
    ("gellify", "GELLIFY"),
    ("tinexta-innovation-hub", "Tinexta Innovation Hub"),
    ("growth-capital", "Growth Capital"),
    ("plug-and-play-italy", "Plug and Play Italy"),
    ("seedble", "Seedble"),
    ("cariplo-factory", "Cariplo Factory / Factory Plus"),
    ("officine-innovazione", "Officine Innovazione (Deloitte)"),
    ("bridgemaker", "Bridgemaker"),
    ("infinite-area", "Infinite Area"),
    ("ventive", "Ventive"),
    ("startup-geeks", "Startup Geeks"),
    ("webidoo", "Webidoo"),
    ("vento", "Vento (Exor)"),
]

md = mistune.create_markdown(plugins=["table", "strikethrough"], escape=False)

TOKEN = re.compile(r"(?<![\w>])\[([VDSN])\](?![\w<])")


def marca(html):
    """Avvolge i marcatori di affidabilità in span, così la dashboard può
    filtrarli. Non tocca il testo dentro i tag."""
    fuori = []
    pezzi = re.split(r"(<[^>]+>)", html)
    for p in pezzi:
        if p.startswith("<"):
            fuori.append(p)
        else:
            fuori.append(TOKEN.sub(
                lambda m: f'<span class="mk mk-{m.group(1)}" data-mk="{m.group(1)}" '
                          f'title="{ETICHETTA[m.group(1)]}">{m.group(1)}</span>', p))
    return "".join(fuori)


ETICHETTA = {
    "V": "verificato da fonte terza controllabile",
    "D": "dichiarato dall'operatore",
    "S": "stimato — aggregatore o banca dati commerciale",
    "N": "cercato e non trovato",
}


def slugifica(testo):
    s = re.sub(r"<[^>]+>", "", testo)
    s = s.lower().strip()
    s = re.sub(r"[àáâ]", "a", s)
    s = re.sub(r"[èéê]", "e", s)
    s = re.sub(r"[ìí]", "i", s)
    s = re.sub(r"[òó]", "o", s)
    s = re.sub(r"[ùú]", "u", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]


def ancora(html):
    """Aggiunge un id a ogni h2/h3 per la navigazione interna."""
    def rep(m):
        tag, attrs, testo = m.group(1), m.group(2), m.group(3)
        return f'<{tag}{attrs} id="h-{slugifica(testo)}">{testo}</{tag}>'
    return re.sub(r"<(h[23])([^>]*)>(.*?)</\1>", rep, html, flags=re.S)


def leggi(rel):
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def a_html(rel, togli_h1=True):
    testo = leggi(rel)
    if testo is None:
        return None
    if togli_h1:
        testo = re.sub(r"\A#\s[^\n]*\n", "", testo)
    return ancora(marca(md(testo)))


# ---------------------------------------------------------------- operatori

def pulisci_cella(c):
    c = c.strip()
    c = re.sub(r"^\*\*|\*\*$", "", c.strip())
    return c.strip()


def nome_e_nota(cella):
    """'**GELLIFY** (Opinno Italy)' -> ('GELLIFY', '(Opinno Italy)')"""
    grassetto = re.match(r"\s*\*\*(.+?)\*\*\s*(.*)$", cella)
    if grassetto:
        return grassetto.group(1).strip(), grassetto.group(2).strip()
    return cella.strip(), ""


def estrai_operatori():
    """Legge le tabelle per punteggio di screening.md e l'elenco in prosa dei
    punteggio 1. Restituisce un record per operatore."""
    testo = leggi("scouting/screening.md")
    ops = []
    sezione = None
    for riga in testo.split("\n"):
        h = re.match(r"^## Punteggio (\d)", riga)
        if h:
            sezione = int(h.group(1))
            continue
        if riga.startswith("## ") and not h:
            if sezione is not None and not riga.startswith("## Punteggio"):
                sezione = None
        if sezione and riga.startswith("|") and "---" not in riga:
            # il pipe sfuggito (a\|cube) non è un separatore di colonna
            protetta = riga.replace("\\|", "")
            celle = [c.replace("", "|") for c in protetta.split("|")[1:-1]]
            if len(celle) < 3:
                continue
            if pulisci_cella(celle[0]).lower() == "operatore":
                continue
            nome, nota = nome_e_nota(celle[0])
            lotto = pulisci_cella(celle[1])
            motivo = celle[2].strip()
            if not nome or nome.lower().startswith("perché"):
                continue
            ops.append({
                "nome": re.sub(r"\\", "", nome),
                "nota": re.sub(r"\*\*", "", nota),
                "punteggio": sezione,
                "lotto": lotto,
                "motivo": marca(md(motivo)).replace("<p>", "").replace("</p>", "").strip(),
            })

    # punteggio 1: elenco in prosa
    blocco = re.search(r"## Punteggio 1 —.*?(?=\n## )", testo, re.S)
    if blocco:
        b = blocco.group(0)
        gruppi = [
            (r"\*\*Costruiscono in proprio, non su commessa\*\* \(lotto 3\):(.+?)\.\n", 3,
             "costruisce imprese proprie, non su commessa"),
            (r"\*\*Fuori perimetro\*\* \(lotto 2\): ([^—]+) —", 2,
             "fuori dai criteri: riposizionata su HR e sviluppo organizzativo"),
            (r"\*\*Esteri, riferimenti di modello\*\* \(lotto 5\):(.+?)\.\n", 5,
             "estero: riferimento di modello, non concorrente"),
        ]
        for pattern, lotto, motivo in gruppi:
            m = re.search(pattern, b, re.S)
            if not m:
                continue
            for nome in m.group(1).split("·"):
                nome = re.sub(r"\*\*|\.", "", nome).strip()
                nome = re.sub(r"\s*\(([A-Z]{2})\)$", r" (\1)", nome)
                if not nome:
                    continue
                ops.append({"nome": nome, "nota": "", "punteggio": 1,
                            "lotto": str(lotto), "motivo": motivo})

    # ZNExt ha una nota di segno opposto nello stesso paragrafo
    for o in ops:
        if o["nome"].startswith("ZNExt"):
            o["motivo"] = ("venture builder interno di Zanichelli e acquirente in proprio: "
                           "<strong>potenziale committente, non concorrente</strong>")

    slug_per_nome = {}
    for slug, etichetta in SCHEDE:
        slug_per_nome[etichetta.lower()] = slug
    alias = {
        "gellify": "gellify", "opinno": None,
        "tinexta innovation hub": "tinexta-innovation-hub",
        "growth capital": "growth-capital",
        "plug and play italy": "plug-and-play-italy",
        "seedble": "seedble", "infinite area": "infinite-area",
        "bridgemaker": "bridgemaker",
    }
    for o in ops:
        chiave = o["nome"].lower()
        o["scheda"] = alias.get(chiave) or slug_per_nome.get(chiave)
        o["origine"] = "scouting"

    # I sette operatori della base non passano dallo scouting — erano nella
    # lista di esclusione perché già noti — ma hanno una scheda completa e
    # devono essere cercabili qui. Punteggio assente per costruzione: non
    # sono mai stati screenati, e inventarne uno sarebbe un dato falso.
    base = [
        ("Seedble", "seedble", "B — open innovation",
         "Scheda della base, rifatta l'11/08/2026. Unico operatore del campione con un listino pubblico su un servizio di innovazione."),
        ("Cariplo Factory / Factory Plus", "cariplo-factory", "B — open innovation",
         "Scheda della base, mai fatta prima. Ha cambiato nome in Factory Plus il 24/07/2026; socia di B-C Ventures con Bridgemaker."),
        ("Officine Innovazione (Deloitte)", "officine-innovazione", "B — open innovation",
         "Scheda della base, mai fatta prima. Presente in 20 procedure di Regione Lombardia, aggiudicataria in nessuna."),
        ("Ventive", "ventive", "D — advisory sul capitale",
         "Scheda della base, rifatta. Riclassificata: non fa venture building ma advisory sul capitale e investimento in proprio."),
        ("Startup Geeks", "startup-geeks", "A — incubazione",
         "Scheda della base, rifatta. Cliente pagante è il founder, non la corporate: la linea corporate esiste ma è senza prove da 18 mesi."),
        ("Webidoo", "webidoo", "E — sostituto",
         "Scheda della base, rifatta. Riclassificata da operatore AI a sostituto: vende abbonamento alla micro-impresa via TIM, Nexi, Esprinet."),
        ("Vento (Exor)", "vento", "F — non concorrente",
         "Scheda della base, rifatta. Riclassificata: è un fondo che investe capitale proprio di Exor, non un fornitore di servizi."),
    ]
    for nome, slug, categoria, motivo in base:
        ops.append({"nome": nome, "nota": "", "punteggio": None, "lotto": "base",
                    "motivo": motivo, "scheda": slug, "origine": "base",
                    "categoria": categoria})
    return ops


# ---------------------------------------------------------------- registro

def estrai_registro():
    p = os.path.join(BASE, "dati", "registro.csv")
    with open(p, "rb") as fh:
        testo = fh.read().decode("utf-8-sig")
    righe = list(csv.reader(io.StringIO(testo)))
    return {"colonne": righe[0], "righe": righe[1:]}


# ---------------------------------------------------------------- contratti

def estrai_contratti():
    """Tabella riassuntiva dei contratti pubblici, dal messaggio di sintesi
    già consolidato in modelli-di-ricavo-e-prezzi.md."""
    return [
        {"operatore": "Tinexta Innovation Hub", "n": 33, "totale": 958726, "max": 30000},
        {"operatore": "CRIT", "n": 14, "totale": 826697, "max": 138200},
        {"operatore": "Plug and Play Italy", "n": 3, "totale": 678941, "max": 425186},
        {"operatore": "Almacube", "n": 6, "totale": 497237, "max": 139500},
        {"operatore": "GELLIFY Italia", "n": 6, "totale": 424705, "max": 137705},
        {"operatore": "Infinite Area", "n": 5, "totale": 346174, "max": None},
        {"operatore": "Nana Bianca", "n": 5, "totale": 262268, "max": 220000},
        {"operatore": "Seedble", "n": 2, "totale": 235000, "max": 130000},
        {"operatore": "Webidoo", "n": 2, "totale": 162773, "max": 138773},
        {"operatore": "Growth Capital", "n": 1, "totale": 5280, "max": 5280},
    ]


def main():
    dati = {
        "generato": "11/08/2026",
        "operatori": estrai_operatori(),
        "registro": estrai_registro(),
        "contratti": estrai_contratti(),
        "schede": [],
        "documenti": {},
    }

    for slug, etichetta in SCHEDE:
        html = a_html(f"schede/{slug}.md")
        if html is None:
            continue
        dati["schede"].append({"slug": slug, "titolo": etichetta, "html": html})

    documenti = {
        "finale": "ANALISI-COMPETITOR-V2.md",
        "sintesi": "sintesi-strategica.md",
        "prezzi": "modelli-di-ricavo-e-prezzi.md",
        "firme": "firme-verbali.md",
        "dubbi": "dubbi.md",
        "verifica": "verifica.md",
        "screening": "scouting/screening.md",
        "consolidato": "scouting/consolidato.md",
        "selezione": "scouting/selezione.md",
        "metodo": "01-metodo-e-schema.md",
        "pipeline": "04-pipeline-scouting.md",
        "base": "03-base-e-buchi.md",
        "prompt": "02-prompt-agenti.md",
    }
    for chiave, rel in documenti.items():
        h = a_html(rel)
        if h:
            dati["documenti"][chiave] = h

    for lettera in "abcdefg":
        nome = {
            "a": "a-appalti", "b": "b-osservatori", "c": "c-programmi-corporate",
            "d": "d-eventi", "e": "e-casi-cliente", "f": "f-annunci-lavoro",
            "g": "g-estero",
        }[lettera]
        h = a_html(f"scouting/{nome}.md")
        if h:
            dati["documenti"]["scouting_" + lettera] = h

    for n in range(1, 5):
        h = a_html(f"scouting/screening-lotto{n}.md")
        if h:
            dati["documenti"][f"lotto{n}"] = h
    h = a_html("scouting/screening-lotto5-estero.md")
    if h:
        dati["documenti"]["lotto5"] = h

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(dati, fh, ensure_ascii=False)

    print(f"scritto {OUT}")
    print(f"  operatori: {len(dati['operatori'])}")
    da_punteggio = {}
    for o in dati["operatori"]:
        k = o["punteggio"] if o["punteggio"] is not None else 0
        da_punteggio[k] = da_punteggio.get(k, 0) + 1
    print(f"  per punteggio (0 = base, mai screenato): "
          f"{dict(sorted(da_punteggio.items(), reverse=True))}")
    print(f"  schede: {len(dati['schede'])}")
    print(f"  documenti: {len(dati['documenti'])}")
    print(f"  peso json: {os.path.getsize(OUT)/1024:.0f} KB")


if __name__ == "__main__":
    main()
