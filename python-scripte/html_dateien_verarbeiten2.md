# Beschreibung

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

