#!/usr/bin/env python3
"""Verifica il contratto dati di dati.json.

Le regole che controlla sono quelle vincolanti del contratto, non preferenze:

  1. ogni campo di confronto ha un enum chiuso: qui si controlla che nessun
     valore stia fuori dall'enum dichiarato nel dato stesso;
  2. i giudizi sono separati dai fatti e portano autore, data e motivazione:
     un giudizio senza autore e un dato falso;
  3. le scale 0-3 hanno la definizione dei gradini nel dato, non nel codice;
  4. nessun numero derivato e salvato: qui si controlla che non compaiano
     campi di conteggio o punteggio calcolabile dentro gli operatori;
  5. ogni affermazione porta fonte, data e marcatura.

Esce con codice 1 al primo insieme di violazioni.

    python3 verifica-dati.py
"""

import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
GUASTI = []
DATA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def guasto(regola, msg):
    GUASTI.append((regola, msg))


def main():
    with open(os.path.join(BASE, "dati.json"), encoding="utf-8") as fh:
        d = json.load(fh)

    E = d["enum"]
    slug = {o["slug"] for o in d["operatori"]}

    # ------------------------------------------------- 1. enum chiusi
    for o in d["operatori"]:
        for campo, gruppo in (("arena", "arena"), ("stato", "stato"),
                              ("chi_rischia", "chi_rischia")):
            if o[campo] not in E[gruppo]:
                guasto(1, "operatore %s: %s=%r fuori enum" % (o["slug"], campo, o[campo]))
        for s in o["segmenti"]:
            if s not in E["segmento"]:
                guasto(1, "operatore %s: segmento %r fuori enum" % (o["slug"], s))
        for m in o["modello_ricavo"]:
            if m not in E["modello_ricavo"]:
                guasto(1, "operatore %s: modello_ricavo %r fuori enum" % (o["slug"], m))
        if o["segmenti_marcatura"] not in E["marcatura"]:
            guasto(1, "operatore %s: marcatura segmenti fuori enum" % o["slug"])
        if o["stato"] == "archiviato" and not o["motivo_archivio"]:
            guasto(1, "operatore %s: archiviato senza motivo" % o["slug"])

    for s in d["servizi"]:
        if s["operatore"] not in slug:
            guasto(1, "servizio %s: operatore ignoto %r" % (s["id"], s["operatore"]))
        if s["tipo"] not in E["tipo"]:
            guasto(1, "servizio %s: tipo %r fuori enum" % (s["id"], s["tipo"]))
        if s["linea"] not in E["linea"]:
            guasto(1, "servizio %s: linea %r fuori enum" % (s["id"], s["linea"]))
        if s["prezzo_natura"] not in E["prezzo_natura"]:
            guasto(1, "servizio %s: prezzo_natura %r fuori enum" % (s["id"], s["prezzo_natura"]))
        # il prezzo e cio che il cliente paga; il meccanismo sta in condizioni
        if s["prezzo_natura"] == "non-pubblico" and s["prezzo"]:
            guasto(1, "servizio %s: dichiarato non pubblico ma il campo prezzo non e vuoto" % s["id"])
        if s["prezzo_natura"] in ("listino", "aggiudicazione", "dotazione") and not s["prezzo"]:
            guasto(1, "servizio %s: %s senza importo" % (s["id"], s["prezzo_natura"]))

    for f in d["firme"]:
        if f["territorio"] not in E["territorio"]:
            guasto(1, "firma %s: territorio %r fuori enum" % (f["operatore"], f["territorio"]))

    for g in d["giudizi"]:
        if g["campo"] not in E["campo_giudizio"]:
            guasto(1, "giudizio %s: campo %r fuori enum" % (g["id"], g["campo"]))
        if g["campo"].startswith("sovr_") and g["valore"] not in ("alta", "media", "bassa", "nulla"):
            guasto(1, "giudizio %s: sovrapposizione %r fuori enum" % (g["id"], g["valore"]))
        if g["campo"] == "radar" and g["valore"] not in E["radar"]:
            guasto(1, "giudizio %s: radar %r fuori enum" % (g["id"], g["valore"]))
        if g["campo"] == "punteggio" and g["valore"] not in list("12345"):
            guasto(1, "giudizio %s: punteggio %r fuori 1-5" % (g["id"], g["valore"]))

    for s in d["segnali"]:
        if s["tipo"] not in E["tipo_segnale"]:
            guasto(1, "segnale %s: tipo %r fuori enum" % (s["id"], s["tipo"]))
        if s["soggetto"] not in slug and s["soggetto"] not in ("mercato", "norma"):
            guasto(1, "segnale %s: soggetto ignoto %r" % (s["id"], s["soggetto"]))

    for i in d["incertezze"]:
        if i["costo_stimato"] not in E["costo"]:
            guasto(1, "incertezza %s: costo %r fuori enum" % (i["id"], i["costo_stimato"]))
        if i["stato"] not in ("aperta", "in-corso", "chiusa"):
            guasto(1, "incertezza %s: stato %r fuori enum" % (i["id"], i["stato"]))
        if i["operatore"] and i["operatore"] not in slug:
            guasto(1, "incertezza %s: operatore ignoto %r" % (i["id"], i["operatore"]))

    # -------------------------------- 2. i giudizi portano autore, data, motivazione
    for g in d["giudizi"]:
        for campo in ("autore", "data", "motivazione"):
            if not g.get(campo):
                guasto(2, "giudizio %s su %s: manca %s" % (g["id"], g["operatore"], campo))
        if not DATA.match(g["data"]):
            guasto(2, "giudizio %s: data non ISO" % g["id"])
    # e non stanno fra i fatti
    for o in d["operatori"]:
        for vietato in ("minaccia", "sovrapposizione", "somiglianza", "punteggio"):
            if vietato in o:
                guasto(2, "operatore %s: %r e un giudizio, non puo stare fra i fatti"
                       % (o["slug"], vietato))

    # ------------------------------------------ 3. le scale definiscono i gradini
    for nome, sc in d["scale"].items():
        if set(sc["gradini"]) != {"0", "1", "2", "3"}:
            guasto(3, "scala %s: i gradini 0-3 non sono tutti definiti" % nome)
        for k, v in sc["gradini"].items():
            if not v or len(v) < 10:
                guasto(3, "scala %s gradino %s: definizione assente o troppo corta" % (nome, k))
    for c in d["competenze"]:
        for k in ("capacita_tecnica", "esecuzione_interna"):
            v = c[k]
            if v is not None and v not in (0, 1, 2, 3):
                guasto(3, "competenza %s: %s=%r fuori scala" % (c["operatore"], k, v))
            if k not in d["scale"]:
                guasto(3, "competenza %s: la scala %s non e definita nel dato" % (c["operatore"], k))

    # ------------------------------------------- 4. nessun numero derivato salvato
    derivati = ("n_servizi", "copertura", "conteggio", "somiglianza", "totale", "score")
    for gruppo in ("operatori", "servizi", "competenze"):
        for riga in d[gruppo]:
            for k in riga:
                if any(k.startswith(x) or k == x for x in derivati):
                    guasto(4, "%s: campo derivato salvato %r" % (gruppo, k))

    # ---------------------------------- 5. fonte, data e marcatura su ogni affermazione
    for s in d["servizi"]:
        if s["marcatura"] not in E["marcatura"]:
            guasto(5, "servizio %s: marcatura assente o fuori enum" % s["id"])
        if not DATA.match(s.get("data", "")):
            guasto(5, "servizio %s: data assente o non ISO" % s["id"])
        if s["marcatura"] != "N" and not s["fonte_url"]:
            guasto(5, "servizio %s (%s): marcata %s senza fonte_url"
                   % (s["id"], s["operatore"], s["marcatura"]))
    for c in d["competenze"]:
        if c["marcatura"] not in E["marcatura"] or not DATA.match(c["data"]):
            guasto(5, "competenza %s: marcatura o data mancante" % c["operatore"])
    for f in d["firme"]:
        if f["marcatura"] not in E["marcatura"] or not DATA.match(f["data"]):
            guasto(5, "firma %s: marcatura o data mancante" % f["operatore"])
    for s in d["segnali"]:
        if s["marcatura"] not in E["marcatura"] or not DATA.match(s["data"]):
            guasto(5, "segnale %s: marcatura o data mancante" % s["id"])
    for o in d["operatori"]:
        if o["economia_marcatura"] not in E["marcatura"]:
            guasto(5, "operatore %s: marcatura economia mancante" % o["slug"])
        if o["ultima_verifica"] and not DATA.match(o["ultima_verifica"]):
            guasto(5, "operatore %s: ultima_verifica non ISO" % o["slug"])
        if o["ultima_verifica"] and not o["verificato_da"]:
            guasto(5, "operatore %s: verificato ma senza il nome di chi" % o["slug"])

    # ------------------------------------------------------------------ esito
    testate = {
        1: "Enum chiusi su ogni campo di confronto",
        2: "Giudizi separati dai fatti, con autore, data e motivazione",
        3: "Scale 0-3 con i gradini definiti nel dato",
        4: "Nessun numero derivato salvato",
        5: "Ogni affermazione porta fonte, data e marcatura",
    }
    print("Contratto dati — dati.json\n")
    for n, t in testate.items():
        miei = [m for r, m in GUASTI if r == n]
        print(("  OK    " if not miei else "  ROTTA ") + "%d. %s" % (n, t))
        for m in miei[:12]:
            print("          " + m)
        if len(miei) > 12:
            print("          … e altre %d" % (len(miei) - 12))
    print()
    # copertura: e una misura, non una regola
    con = len({s["operatore"] for s in d["servizi"]})
    tot = len(d["operatori"])
    att = sum(1 for o in d["operatori"] if o["stato"] == "attivo")
    print("Copertura del catalogo: %d operatori su %d hanno servizi (%.0f%%), "
          "%d attivi in totale" % (con, tot, 100.0 * con / tot, att))
    if GUASTI:
        print("\n%d violazioni. Il contratto dati non regge." % len(GUASTI))
        return 1
    print("Il contratto dati regge.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
