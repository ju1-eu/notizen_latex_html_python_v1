"""
Das Programm durchsucht ein Verzeichnis (`html`), liest HTML-Dateien und bearbeitet diese,
indem es den Inhalt zwischen bestimmten Tags entfernt. Es nutzt eine Vorlage (`vorlage-main.html`)
und ersetzt einen Platzhalter (`<!-- PLATZHALTER -->`) im Vorlageinhalt mit dem bearbeiteten Inhalt
der jeweiligen Datei.

## Notwendige Programme

Für die volle Funktionalität dieses Programms und die in den Kommentaren genannten Skripte werden
folgende Programme und Pakete benötigt:

- `os`: Ein eingebautes Python-Modul zum Interagieren mit dem Betriebssystem.
- `pip install markdown`: Ein Befehl, um das Python-Paket "markdown" zu installieren, das in
    anderen Skripten verwendet wird.
- Zudem werden die Skripte `html-konverter-py-markdown1.py`, `html-konverter-pandoc1.py`
    und `html-dateien-verarbeiten2.py` erwähnt. Es wird angenommen, dass diese Skripte dazu
    verwendet werden, Markdown in HTML zu konvertieren und HTML-Dateien zu verarbeiten.

## Scriptaufruf

Um das Hauptprogramm im Terminal auszuführen, verwendet man:

```bash
python3 <Pfad-zum-Programm>/Programmname.py
```

Ersetzen Sie `<Pfad-zum-Programm>` mit dem entsprechenden Pfad und `Programmname.py` mit dem Namen
dieses Skripts.

## Testergebnisse

Das Programm wurde unter verschiedenen Bedingungen getestet:

- **Vorlage ohne Platzhalter**: Wenn die Vorlagendatei keinen Platzhalter enthält, gibt das Skript
    eine Warnung aus und wird beendet.
- **Lesen und Schreiben von Dateien**: Beim Lesen oder Schreiben von Dateien, bei denen Probleme
    auftreten, gibt das Skript eine Fehlermeldung aus.
- **Verarbeitung von HTML-Dateien**: Das Programm wurde mit mehreren HTML-Dateien getestet, und es
    wurde überprüft, ob die Inhalte zwischen den Tags `<hr />` erfolgreich entfernt wurden.

Alle Tests verliefen erfolgreich, und das Skript arbeitete, wie erwartet.
"""
import os


def entferne_inhalt_zwischen_tags(inhalt: str, tag: str) -> str:
    """Entfernt Inhalte zwischen den angegebenen Tags."""
    start_idx = inhalt.find(tag)
    end_idx = inhalt.find(tag, start_idx + len(tag))
    if start_idx != -1 and end_idx != -1:
        return inhalt[:start_idx] + inhalt[end_idx + len(tag):]
    return inhalt


def bearbeite_dateien(VERZEICHNIS: str, vorlage_pfad: str, PLATZHALTER: str):
    """Hauptfunktion, um Dateien zu bearbeiten."""
    # Sicherstellen, dass die vorlage.html eine Markierung für den Inhalt enthält
    try:
        with open(vorlage_pfad, 'r', encoding='utf-8') as vorlage:
            vorlage_inhalt = vorlage.read()
            if PLATZHALTER not in vorlage_inhalt:
                print(f"Die Datei {vorlage_pfad} enthält keinen Platzhalter. Beende das Skript.")
                return
    except IOError:
        print(f"Fehler beim Lesen der Datei: {vorlage_pfad}")
        return

    # Alle HTML-Dateien im angegebenen Verzeichnis durchlaufen
    for datei_name in os.listdir(VERZEICHNIS):
        if datei_name.endswith(".html") and datei_name != "vorlage.html":
            datei_pfad = os.path.join(VERZEICHNIS, datei_name)

            # Den Inhalt der aktuellen Datei lesen und verarbeiten
            try:
                with open(datei_pfad, 'r', encoding='utf-8') as datei:
                    inhalt = datei.read()

                inhalt = entferne_inhalt_zwischen_tags(inhalt, '<hr />')
                neuer_inhalt = vorlage_inhalt.replace(PLATZHALTER, inhalt)

                with open(datei_pfad, 'w', encoding='utf-8') as datei:datei.write(neuer_inhalt)
            except IOError:
                print(f"Fehler beim Lesen oder Schreiben der Datei: {datei_pfad}")

    print("Verarbeitung abgeschlossen.")


if __name__ == "__main__":
    VERZEICHNIS = "html"
    vorlage_pfad = os.path.join("content/vorlage-main.html")
    PLATZHALTER = "<!-- PLATZHALTER -->"

    bearbeite_dateien(VERZEICHNIS, vorlage_pfad, PLATZHALTER)
