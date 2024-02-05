import os

"""
# dokumentation.py
Das vorgestellte Programm durchsucht einen spezifizierten Ordner nach Python-Scripten. Für jedes gefundene Skript extrahiert es den Anfangskommentar, welcher als Beschreibung des Skripts fungiert. Basierend auf dieser Beschreibung generiert es eine zugehörige Markdown-Datei. Die generierte Datei enthält nicht nur die Beschreibung des Skripts, sondern auch Anweisungen für den Scriptaufruf im Terminal und einen Abschnitt für Testergebnisse.
"""


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
                print(f"[WARNUNG] Keine Beschreibung in {
                      skript_pfad} gefunden.")
                return ""

            return inhalt[start_index:end_index].strip()
    except Exception as e:
        print(f"Fehler beim Lesen von {skript_pfad}: {e}")
        return ""


def generiere_markdown(skript_pfad, beschreibung):
    md_pfad = os.path.splitext(skript_pfad)[0] + '.md'
    md_inhalt = f"# Beschreibung\n\n{beschreibung}\n\n"
    try:
        with open(md_pfad, 'w', encoding='utf-8') as md_datei:
            md_datei.write(md_inhalt)
    except Exception as e:
        print(f"Fehler beim Schreiben von {md_pfad}: {e}")


def main():
    ordner_pfad = 'python-scripte'

    for eintrag in os.scandir(ordner_pfad):
        if eintrag.is_file() and eintrag.name.endswith('.py'):
            beschreibung = extrahiere_beschreibung(eintrag.path)
            if beschreibung:
                generiere_markdown(eintrag.path, beschreibung)


if __name__ == '__main__':
    main()
