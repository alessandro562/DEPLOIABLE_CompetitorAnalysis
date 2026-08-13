#!/usr/bin/env python3
"""Genera campo.html — l'artefatto di distribuzione.

Il dato sta in dati.json e la presentazione in index.html: sono due file, ed e
cosi che vanno modificati. Il file unico e ammesso solo come artefatto di
distribuzione, generato: si apre con un doppio clic, funziona senza rete e
senza server, si manda per email.

    python3 costruisci.py

Non ha dipendenze: solo Python 3.
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATI = os.path.join(BASE, "dati.json")
MODELLO = os.path.join(BASE, "index.html")
USCITA = os.path.join(BASE, "campo.html")

SEGNAPOSTO = "/*INNESTO-DATI*/"


def main():
    for p in (DATI, MODELLO):
        if not os.path.exists(p):
            print("manca", p)
            return 1

    with open(DATI, encoding="utf-8") as fh:
        dati = json.load(fh)
    with open(MODELLO, encoding="utf-8") as fh:
        html = fh.read()

    if SEGNAPOSTO not in html:
        print("index.html non contiene il punto di innesto dei dati: "
              "cerco la riga\n  " + SEGNAPOSTO)
        return 1

    # </script> dentro una stringa JSON chiuderebbe il tag: si spezza.
    grezzo = json.dumps(dati, ensure_ascii=False, separators=(",", ":"))
    grezzo = grezzo.replace("</", "<\\/")

    innesto = "window.DATI = " + grezzo + ";"
    fuori = html.replace(SEGNAPOSTO, innesto, 1)
    fuori = fuori.replace("<title>Il campo — Deploiable</title>",
                          "<title>Il campo — Deploiable</title>\n"
                          "<!-- artefatto di distribuzione generato da costruisci.py: "
                          "non modificarlo a mano, le modifiche si perdono al primo rigenera -->")

    with open(USCITA, "w", encoding="utf-8") as fh:
        fh.write(fuori)

    attivi = sum(1 for o in dati["operatori"] if o["stato"] == "attivo")
    con_cat = len({s["operatore"] for s in dati["servizi"]})
    print("scritto", USCITA)
    print("  %d operatori (%d attivi), %d servizi su %d operatori, %d giudizi"
          % (len(dati["operatori"]), attivi, len(dati["servizi"]), con_cat, len(dati["giudizi"])))
    print("  peso %.0f KB" % (os.path.getsize(USCITA) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
