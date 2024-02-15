"""
Dieses Skript konvertiert Markdown-Dateien (.md) aus einem Quellverzeichnis in LaTeX (.tex) Dateien
in einem Zielverzeichnis, unter Verwendung von Pandoc und einer benutzerdefinierten LaTeX-Vorlage.

Funktionalitäten:
- Überprüft, ob Pandoc auf dem System installiert ist.
- Erlaubt die Konvertierung einer Markdown-Datei oder aller Markdown-Dateien
- Nutzt eine LaTeX-Vorlage für die Konvertierung.
- Erstellt das Zielverzeichnis, falls es nicht existiert.
- Extrahiert das Thema aus dem Dateinamen der Markdown-Datei und setzt es als Titelvariable
    für Pandoc.

Verwendung:
- Zum Konvertieren aller Markdown-Dateien im Quellverzeichnis einfach das Skript ohne Argumente
    ausführen.
- Zum Konvertieren einer spezifischen Markdown-Datei das Skript mit dem Dateinamen als Argument
    ausführen.

Konstanten:
- QUELLPFAD: Verzeichnis mit den Quell-Markdown-Dateien.
- ZIELPFAD: Verzeichnis, in das die konvertierten LaTeX-Dateien geschrieben werden.
- VORLAGEPFAD: LaTeX-Vorlagendatei, die von Pandoc für die Konvertierung verwendet wird.

Das Skript besteht aus mehreren Funktionen:
- `ist_pandoc_installiert()`: Überprüft die Verfügbarkeit von Pandoc auf dem System.
- `extrahiere_thema_aus_dateiname(dateiname)`: Extrahiert das Thema aus dem Dateinamen
- `konvertiere_md_zu_tex(md_pfad, tex_pfad)`: Führt die eigentliche Konvertierung für eine einzelne
    Datei durch.
- `konvertiere_dateien(dateiname=None)`: Steuert die Konvertierung basierend auf der
    Benutzereingabe oder konvertiert alle Dateien.
- `main()`: Hauptfunktion, steuert Ausführung des Skripts.
"""

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
        with open(tex_pfad, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()

            # Suche nach dem Muster und ersetze es
            inhalt = re.sub(suchmuster, ersetzen_durch, inhalt)

        backup_pfad = tex_pfad + '.bak'
        with open(backup_pfad, 'w', encoding='utf-8') as backup_datei:
            backup_datei.write(inhalt)
        with open(tex_pfad, 'w', encoding='utf-8') as datei:
            datei.write(inhalt)
    except IOError as e:
        print(f"Fehler beim Bearbeiten der Datei {tex_pfad}: {e}")


def entferne_befehl(tex_pfad, befehl):
    """
    Entfernt einen bestimmten LaTeX-Befehl aus einer .tex-Datei und erstellt eine .bak-Backup-Datei.
    """
    try:
        with open(tex_pfad, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            # debug
            if befehl in inhalt:
                print(f"Befehl {befehl} gefunden in {tex_pfad}")
            else:
                print(f"Befehl {befehl} nicht gefunden in {tex_pfad}")

        backup_pfad = tex_pfad + '.bak'
        with open(backup_pfad, 'w', encoding='utf-8') as backup_datei:
            backup_datei.write(inhalt)
        with open(tex_pfad, 'w', encoding='utf-8') as datei:
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
    dateien = [os.path.join(VERZEICHNIS_PFAD, spezifische_datei + '.tex')
               ] if spezifische_datei else list(glob.iglob(os.path.join(VERZEICHNIS_PFAD, "*.tex")))

    for tex_datei in dateien:
        if os.path.isfile(tex_datei):
            suche_und_ersetze(tex_datei, SUCHMUSTER, ERSATZMUSTER)
            print(f"Datei {tex_datei} bearbeitet.")


def main():
    """
    Hauptfunktion, die andere Funktionen in der richtigen Reihenfolge aufruft.
    """
    parser = argparse.ArgumentParser(description='Bearbeitet LaTeX-Dateien.')
    parser.add_argument(
        '--datei', help='Name der .tex-Datei, die bearbeitet werden soll.')
    args = parser.parse_args()

    # Sicherheitsüberprüfung: Dateiname keine unsicheren Zeichen oder Pfade
    if args.datei and (not args.datei.isalnum() or '..' in args.datei or '/' in args.datei):
        print("Ungültiger Dateiname. Bitte geben Sie einen Dateinamen ohne Pfadangaben an.")
        return

    bearbeite_dateien(args.datei)
    loesche_backup_dateien()


if __name__ == "__main__":
    main()
