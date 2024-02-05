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
