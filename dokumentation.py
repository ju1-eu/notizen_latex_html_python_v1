"""
Das Skript `dokumentation.py` automatisiert die Erstellung von Dokumentationen für Python-Skripte.
Es durchsucht einen spezifizierten Ordner nach Python-Skripten und extrahiert aus jedem Skript den
Anfangskommentar, der als Beschreibung dient. Anschließend generiert es für jedes Skript eine
Markdown-Datei (.md), die die Skriptbeschreibung, Anweisungen für den Aufruf des Skripts im Terminal
und einen Abschnitt für Testergebnisse enthält.

Der Prozess umfasst folgende Schritte:
1. Durchsuchen eines vorgegebenen Ordners nach Python-Dateien (.py).
2. Extrahieren der Beschreibung aus den Anfangskommentaren der Skripte.
3. Generieren einer Markdown-Datei für jedes Skript, das eine Beschreibung enthält.
4. Speichern der Markdown-Dateien im gleichen Verzeichnis wie die Skripte, mit dem gleichen
   Basisnamen wie das Skript und der Dateiendung .md.

Dieses Skript ist besonders nützlich für Entwickler, die eine schnelle und einheitliche
Dokumentation ihrer Skripte erstellen möchten, um die Übersichtlichkeit und Wartbarkeit
des Codes zu verbessern.
"""
import os


def extrahiere_beschreibung(skript_pfad):
    """
    Liest eine Python-Datei und extrahiert die Beschreibung aus den Anfangskommentaren.
    Generiert eine zugehörige Markdown-Datei.
    """
    try:
        with open(skript_pfad, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            start_index = inhalt.find('"""') + 3
            end_index = inhalt.find('"""', start_index)

            if start_index == 2 or end_index == -1:
                print(f"[WARNUNG] Keine Beschreibung in {skript_pfad} gefunden.")
                return ""

            return inhalt[start_index:end_index].strip()
    except Exception as error:
        print(f"Fehler beim Lesen von {skript_pfad}: {error}")
        return ""


def generiere_markdown(skript_pfad, beschreibung):
    """
    Generiert eine Markdown-Datei aus der übergebenen Skriptbeschreibung.

    Diese Funktion nimmt den Pfad zu einem Python-Skript und dessen Beschreibung als Eingabe.
    Sie erstellt eine neue Markdown-Datei im gleichen Verzeichnis wie das Skript mit einem
    ähnlichen Namen (ersetzt die '.py'-Endung durch '.md'). Die Markdown-Datei beginnt mit
    einem Titel 'Beschreibung' und enthält die übergebene Beschreibungstext des Skripts.

    Args:
        skript_pfad (str): Der Pfad zur Python-Datei, für die die Dokumentation generiert wird.
        beschreibung (str): Der Text, der als Beschreibung des Skripts in die
        Markdown-Datei eingefügt wird.

    Die Funktion versucht, die Markdown-Datei zu erstellen und den Beschreibungstext
    hineinzuschreiben.
    Im Falle eines Fehlers beim Dateizugriff oder Schreiben wird eine Fehlermeldung ausgegeben.

    Beispiel:
        generiere_markdown('pfad/zum/skript.py', 'Dies ist eine detaillierte Beschreibung
        des Skripts.')

    Erzeugt eine Markdown-Datei 'skript.md' im gleichen Verzeichnis mit der angegebenen
    Beschreibung.
    """
    md_pfad = os.path.splitext(skript_pfad)[0] + '.md'
    md_inhalt = f"# Beschreibung\n\n{beschreibung}\n\n"
    try:
        with open(md_pfad, 'w', encoding='utf-8') as md_datei:
            md_datei.write(md_inhalt)
    except Exception as error:
        print(f"Fehler beim Schreiben von {md_pfad}: {error}")


def main():
    ordner_pfad = 'python-scripte'

    for eintrag in os.scandir(ordner_pfad):
        if eintrag.is_file() and eintrag.name.endswith('.py'):
            beschreibung = extrahiere_beschreibung(eintrag.path)
            if beschreibung:
                generiere_markdown(eintrag.path, beschreibung)


if __name__ == '__main__':
    main()
