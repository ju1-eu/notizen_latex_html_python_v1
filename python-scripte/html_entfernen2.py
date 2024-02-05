"""
Dieses Skript durchsucht HTML-Dateien in einem vorgegebenen Verzeichnis nach Referenzen auf .eps-
und .pdf-Dateien
innerhalb von Bildquellen (src-Attribut) und ersetzt diese durch Referenzen auf .svg- bzw.
.webp-Dateien.

Die Ersetzung erfolgt auf der Basis von regulären Ausdrücken, die definierte Muster für .eps- und
.pdf-Dateien erkennen
und diese durch neue Pfade für .svg- und .webp-Dateien ersetzen. Die Pfade zu den Original- und
Zielbildern werden
innerhalb des Skripts über Konstanten definiert.

Das Skript kann entweder auf alle HTML-Dateien im spezifizierten Verzeichnis angewendet werden oder
auf eine einzelne,
spezifisch benannte HTML-Datei. Es nimmt einen optionalen Argumentparameter entgegen, der den Namen
der spezifischen
HTML-Datei (ohne .html-Endung) angibt, die bearbeitet werden soll. Bei Abwesenheit dieses Parameters
werden alle
HTML-Dateien im Verzeichnis bearbeitet.

Verwendung:
    python skriptname.py [--datei DATEINAME_OHNE_ENDUNG]

Beispiel:
    python skriptname.py --datei index

Sicherheitshinweise:
    Das Skript führt eine einfache Validierung des Dateinamens durch, um die Verwendung unsicherer
    Dateipfade zu verhindern.
    Es ist darauf zu achten, dass die Dateinamen und Pfade, mit denen das Skript arbeitet,
    vertrauenswürdig sind, da die
    Verwendung von 'open' mit schreibendem Zugriff potenziell manipulative Operationen auf dem
    Dateisystem ermöglicht.

Konstanten:
    VERZEICHNIS_PFAD: Der Pfad zum Verzeichnis, das die zu bearbeitenden HTML-Dateien enthält.
    SUCH_MUSTER_EPS/PDF: Reguläre Ausdrücke zum Finden der .eps/.pdf-Dateireferenzen in den
    HTML-Dateien.
    ERSETZ_MUSTER_EPS/PDF: Die Muster, durch die die gefundenen Referenzen ersetzt werden sollen.

Funktionen:
    ersetze_in_datei(html_pfad): Liest den Inhalt einer spezifischen HTML-Datei, ersetzt gefundene
    Muster und schreibt die Änderungen zurück.
    bearbeite_dateien(spezifische_datei): Wendet 'ersetze_in_datei' auf alle oder eine spezifische
    HTML-Datei an.
    main(): Einstiegspunkt des Skripts; verarbeitet Befehlszeilenargumente und ruft die
    Bearbeitungsfunktion auf.
"""


import os
import glob
import argparse
import re

# Konstanten als Großbuchstaben (Python-Konvention)
VERZEICHNIS_PFAD = "./html"
SUCH_MUSTER_EPS = r'src="images/(.*?)\.eps"'   # zu suchender String für .eps
SUCH_MUSTER_PDF = r'src="images/(.*?)\.pdf"'   # zu suchender String für .pdf
ERSETZ_MUSTER_EPS = r'src="./images/\1.svg"'  # Ersatzstring für .eps
ERSETZ_MUSTER_PDF = r'src="./images/\1.webp"' # Ersatzstring für .pdf

def ersetze_in_datei(html_pfad):
    """
    Ersetzt alle Vorkommen des Suchmusters durch das Ersetzungsmuster in einer .html-Datei.
    """
    try:
        with open(html_pfad, 'r') as datei:
            inhalt = datei.read()

            # Ersetzen von .eps und .pdf Referenzen
            inhalt = re.sub(SUCH_MUSTER_EPS, ERSETZ_MUSTER_EPS, inhalt)
            inhalt = re.sub(SUCH_MUSTER_PDF, ERSETZ_MUSTER_PDF, inhalt)

        with open(html_pfad, 'w') as datei:
            datei.write(inhalt)
    except IOError as e:
        print(f"Fehler beim Bearbeiten der Datei {html_pfad}: {e}")


def bearbeite_dateien(spezifische_datei=None):
    """
    Bearbeitet .html-Dateien im angegebenen Verzeichnis oder eine spezifische Datei.
    """
    dateien = [os.path.join(VERZEICHNIS_PFAD, spezifische_datei + '.html')] if spezifische_datei else list(glob.iglob(os.path.join(VERZEICHNIS_PFAD, "*.html")))

    for html_datei in dateien:
        if os.path.isfile(html_datei):
            ersetze_in_datei(html_datei)
            print(f"Datei {html_datei} bearbeitet.")

def main():
    """
    Hauptfunktion, die andere Funktionen in der richtigen Reihenfolge aufruft.
    """
    parser = argparse.ArgumentParser(description='Bearbeitet HTML-Dateien.')
    parser.add_argument('--datei', help='Name der spezifischen .html-Datei, die bearbeitet werden soll. Ohne .html-Endung.')
    args = parser.parse_args()

    # Sicherheitsüberprüfung
    if args.datei and (not args.datei.isalnum() or '..' in args.datei or '/' in args.datei):
        print("Ungültiger Dateiname. Bitte geben Sie einen sicheren Dateinamen ohne Pfadangaben an.")
        return

    bearbeite_dateien(args.datei)

if __name__ == "__main__":
    main()
