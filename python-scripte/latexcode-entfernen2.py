import os
import glob
import argparse
import re

# Konstanten als Großbuchstaben (Python-Konvention)
VERZEICHNIS_PFAD = "./tex"
LATEX_BEFEHL = "\\passthrough"  # suchen und ersetzen von \passthrough

# Muster für die Suche und Ersetzung
# Such- und Ersatzmuster
SUCHMUSTER = r'\{\[\}@([^:]+:[^:]+:[^\]]+)\{\]\}'
ERSATZMUSTER = r'\\textcite{\1}'

def suche_und_ersetze(tex_pfad, suchmuster, ersetzen_durch):
    """
    Sucht nach einem Muster in einer .tex-Datei und ersetzt es durch den angegebenen Text.
    """
    try:
        with open(tex_pfad, 'r') as datei:
            inhalt = datei.read()

            # Suche nach dem Muster und ersetze es
            inhalt = re.sub(suchmuster, ersetzen_durch, inhalt)

        backup_pfad = tex_pfad + '.bak'
        with open(backup_pfad, 'w') as backup_datei:
            backup_datei.write(inhalt)
        with open(tex_pfad, 'w') as datei:
            datei.write(inhalt)
    except IOError as e:
        print(f"Fehler beim Bearbeiten der Datei {tex_pfad}: {e}")

def entferne_befehl(tex_pfad, befehl):
    """
    Entfernt einen bestimmten LaTeX-Befehl aus einer .tex-Datei und erstellt eine .bak-Backup-Datei.
    """
    try:
        with open(tex_pfad, 'r') as datei:
            inhalt = datei.read()
            # debug
            if befehl in inhalt:
                print(f"Befehl {befehl} gefunden in {tex_pfad}")
            else:
                print(f"Befehl {befehl} nicht gefunden in {tex_pfad}")

        backup_pfad = tex_pfad + '.bak'
        with open(backup_pfad, 'w') as backup_datei:
            backup_datei.write(inhalt)
        with open(tex_pfad, 'w') as datei:
            datei.write(inhalt.replace(befehl, ""))

    except IOError as e:
        print(f"Fehler beim Bearbeiten der Datei {tex_pfad}: {e}")

def loesche_backup_dateien():
    """
    Löscht alle .bak-Dateien im angegebenen Verzeichnis.
    """
    for backup_datei in glob.iglob(os.path.join(VERZEICHNIS_PFAD, "*.bak")):
        try:
            os.remove(backup_datei)
        except OSError as e:
            print(f"Fehler beim Löschen der Backup-Datei {backup_datei}: {e}")

def bearbeite_dateien(spezifische_datei=None):
    """
    Bearbeitet .tex-Dateien im angegebenen Verzeichnis oder eine spezifische Datei.
    """
    dateien = [os.path.join(VERZEICHNIS_PFAD, spezifische_datei + '.tex')] if spezifische_datei else list(glob.iglob(os.path.join(VERZEICHNIS_PFAD, "*.tex")))

    for tex_datei in dateien:
        if os.path.isfile(tex_datei):
            suche_und_ersetze(tex_datei, SUCHMUSTER, ERSATZMUSTER)
            print(f"Datei {tex_datei} bearbeitet.")

def main():
    """
    Hauptfunktion, die andere Funktionen in der richtigen Reihenfolge aufruft.
    """
    parser = argparse.ArgumentParser(description='Bearbeitet LaTeX-Dateien.')
    parser.add_argument('--datei', help='Name der spezifischen .tex-Datei, die bearbeitet werden soll. Ohne .tex-Endung.')
    args = parser.parse_args()

    # Sicherheitsüberprüfung: Stellen Sie sicher, dass der Dateiname keine unsicheren Zeichen oder Pfade enthält.
    if args.datei and (not args.datei.isalnum() or '..' in args.datei or '/' in args.datei):
        print("Ungültiger Dateiname. Bitte geben Sie einen sicheren Dateinamen ohne Pfadangaben an.")
        return

    bearbeite_dateien(args.datei)
    loesche_backup_dateien()

if __name__ == "__main__":
    main()
