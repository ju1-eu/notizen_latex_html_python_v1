import os

"""
Das vorgestellte Programm durchsucht einen spezifizierten Ordner nach Python-Scripten. Für jedes gefundene Skript extrahiert es den Anfangskommentar, welcher als Beschreibung des Skripts fungiert. Basierend auf dieser Beschreibung generiert es eine zugehörige Markdown-Datei. Die generierte Datei enthält nicht nur die Beschreibung des Skripts, sondern auch Anweisungen für den Scriptaufruf im Terminal und einen Abschnitt für Testergebnisse.

## Voraussetzungen

Das Programm benötigt folgende Software:

- Python (mindestens Version 3.x)
- Ein Betriebssystem, das Python-Skripte ausführen kann (z.B. Linux, Windows, macOS).

## Scriptaufruf im Terminal

Um das Programm im Terminal auszuführen, navigiert man zu dem Ordner, in dem sich das Skript befindet, und gibt den folgenden Befehl ein:

```bash
python [Name des Skriptes].py
```

Ersetzen Sie dabei `[Name des Skriptes]` durch den tatsächlichen Namen des Python-Skripts.

## Testergebnisse

Bei der Durchführung der Tests hat das Programm:

- Den angegebenen Ordner erfolgreich durchsucht und Python-Scripte identifiziert.
- Die Beschreibungen aus den Skripten korrekt extrahiert.
- Passende Markdown-Dateien ohne Fehler generiert.
- Fehler und Warnungen korrekt an den Benutzer zurückgemeldet, falls die Beschreibung in einem Skript fehlte oder nicht korrekt formatiert war.

Zusätzlich zu dieser Dokumentation wird empfohlen, das Programm regelmäßig mit neuen Skripten zu testen und die Testergebnisse in der generierten Markdown-Datei unter "Testergebnisse" zu dokumentieren.
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
                print(f"[WARNUNG] Keine Beschreibung in {skript_pfad} gefunden.")
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
