#!/usr/bin/env python3
"""Verifica del contrasto — si lancia PRIMA di toccare il CSS, non dopo.

La versione precedente dello strumento aveva la parola «libero» a 2,29:1:
aveva reso invisibile il proprio segnale piu importante. Questo script esiste
perche quella cosa non possa succedere di nuovo senza che qualcuno se ne accorga.

Uso:
    python3 contrasto.py            verifica la tavolozza e le coppie dichiarate
    python3 contrasto.py --css      estrae anche le variabili da index.html e
                                    controlla che coincidano con la tavolozza

Esce con codice 1 se anche una sola coppia sta sotto 4,5:1.
"""

import os
import re
import sys

SOGLIA = 4.5

# --------------------------------------------------------------- tavolozza
# Un solo accento forte, riservato a una cosa sola: il buco.
# Tutto il resto e inchiostro su carta.
TAVOLOZZA = {
    "carta":        "#FFFFFF",  # fondo pagina
    "carta-2":      "#F1EFEA",  # fondo di intestazioni, barre, celle pari
    "carta-3":      "#E4E1D9",  # fondo di riposo, righe selezionate
    "inchiostro":   "#141310",  # testo primario
    "inchiostro-2": "#4C483F",  # testo secondario, etichette
    "bordo":        "#B9B5A9",  # linee della griglia
    "bordo-forte":  "#7A756A",  # linee di sezione
    "buco":         "#A81C06",  # L'ACCENTO. Solo assenza di copertura.
    "buco-carta":   "#FBE7E2",  # fondo delle celle vuote
}

# Ogni coppia testo-fondo che l'interfaccia produce davvero.
COPPIE = [
    ("inchiostro",   "carta",       "testo primario su pagina"),
    ("inchiostro",   "carta-2",     "testo su intestazione di tabella"),
    ("inchiostro",   "carta-3",     "testo su riga selezionata"),
    ("inchiostro-2", "carta",       "etichetta secondaria su pagina"),
    ("inchiostro-2", "carta-2",     "etichetta secondaria su intestazione"),
    ("inchiostro-2", "carta-3",     "etichetta secondaria su riga selezionata"),
    ("buco",         "carta",       "segnale di buco su pagina"),
    ("buco",         "carta-2",     "segnale di buco su intestazione"),
    ("buco",         "buco-carta",  "segnale di buco su cella vuota"),
    ("bordo-forte",  "carta",       "linea di sezione su pagina"),
    ("carta",        "inchiostro",  "testo invertito su barra scura"),
    ("carta",        "buco",        "testo invertito su accento"),
]


def canale(v):
    v = v / 255
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def luminanza(esa):
    esa = esa.lstrip("#")
    r, g, b = (int(esa[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * canale(r) + 0.7152 * canale(g) + 0.0722 * canale(b)


def contrasto(a, b):
    la, lb = luminanza(a), luminanza(b)
    chiaro, scuro = max(la, lb), min(la, lb)
    return (chiaro + 0.05) / (scuro + 0.05)


def verifica_tavolozza():
    print("Tavolozza — un accento solo, riservato al buco\n")
    for nome, esa in TAVOLOZZA.items():
        print(f"  --{nome:<13} {esa}")
    print()

    print(f"Coppie testo-fondo — soglia {SOGLIA}:1\n")
    esito = True
    for davanti, dietro, uso in COPPIE:
        r = contrasto(TAVOLOZZA[davanti], TAVOLOZZA[dietro])
        ok = r >= SOGLIA
        esito = esito and ok
        print(f"  {'OK  ' if ok else 'SOTTO'} {r:5.2f}:1  "
              f"{davanti} su {dietro:<12} — {uso}")
    print()
    return esito


def verifica_css(percorso):
    """Le variabili scritte nel CSS devono essere quelle verificate qui.
    Un CSS che diverge dalla tavolozza rende questo script una decorazione."""
    if not os.path.exists(percorso):
        print(f"  {percorso} non trovato: salto il confronto col CSS")
        return True
    testo = open(percorso, encoding="utf-8").read()
    dichiarate = dict(re.findall(r"--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})", testo))
    esito = True
    print("Confronto con il CSS di index.html\n")
    for nome, esa in TAVOLOZZA.items():
        trovato = dichiarate.get(nome)
        if trovato is None:
            print(f"  ASSENTE  --{nome} non e dichiarata nel CSS")
            esito = False
        elif trovato.upper() != esa.upper():
            print(f"  DIVERGE  --{nome}: CSS {trovato} != tavolozza {esa}")
            esito = False
        else:
            print(f"  OK       --{nome}")
    # colori scritti a mano fuori dalla tavolozza
    fuori = set(re.findall(r"(#[0-9A-Fa-f]{3,8})\b", testo))
    ammessi = {v.upper() for v in TAVOLOZZA.values()}
    intrusi = sorted(c for c in fuori if c.upper() not in ammessi)
    if intrusi:
        print(f"\n  COLORI FUORI TAVOLOZZA: {', '.join(intrusi)}")
        print("  Ogni colore deve passare da qui, altrimenti non e verificato.")
        esito = False
    print()
    return esito


def main():
    ok = verifica_tavolozza()
    if "--css" in sys.argv:
        base = os.path.dirname(os.path.abspath(__file__))
        ok = verifica_css(os.path.join(base, "index.html")) and ok
    if ok:
        print("Tutte le coppie superano 4,5:1.")
        return 0
    print("ALMENO UNA COPPIA E SOTTO SOGLIA. Non scrivere il CSS cosi.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
