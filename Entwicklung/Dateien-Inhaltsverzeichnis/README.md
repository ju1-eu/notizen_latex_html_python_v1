# Dokumentation für das Skript dateien_inhaltsverzeichnis.py

## Projektbeschreibung

Dieses Skript dient der Automatisierung der Konvertierung verschiedenartiger Dateien (darunter Markdown, C++, Python und PDF) in HTML-Format. Es wurde entwickelt, um eine breite Palette von Dokumenten — von Lehrmaterialien über technische Dokumentation bis hin zu Übungsdateien — effizient und benutzerfreundlich für die Webdarstellung aufzubereiten. Zusätzlich zur Konvertierung erstellt das Skript eine strukturierte Inhaltsübersicht, die eine einfache Navigation durch die konvertierten Materialien ermöglicht. Diese Funktionalität ist besonders nützlich Inhalte digital zugänglich zu machen.

## Installation

Voraussetzungen:
- Python 3.x
- Pandoc
- Pygments

Installiere die Python-Abhängigkeiten mit:

```sh
pip install -r requirements.txt
```

Stelle sicher, dass Pandoc und Pygments auf deinem System installiert sind. Die Installationsanleitungen findest du auf den offiziellen Webseiten der Tools.

## Verwendung

1. Platziere das Skript im Wurzelverzeichnis deiner Kursmaterialien.
2. Stelle sicher, dass `VERZEICHNIS` und `ZIELVERZEICHNIS` in `dateien_inhaltsverzeichnis.py` korrekt gesetzt sind.
3. Führe das Skript mit Python aus:

```sh
python dateien_inhaltsverzeichnis.py
```

Das Skript durchsucht das angegebene Verzeichnis (`VERZEICHNIS`), konvertiert unterstützte Dateitypen und speichert die Ergebnisse sowie eine Inhaltsübersicht im `ZIELVERZEICHNIS`.

## Lizenz

Dieses Projekt ist unter der MIT Lizenz veröffentlicht. Details findest du in der `LICENSE`-Datei.

## Mitwirkende

- Jan Unger - Hauptentwickler

Für weitere Informationen zu Abhängigkeiten und spezifischen Versionen siehe `requirements.txt` und die Abschnitte über Pandoc und Pygments in dieser Dokumentation.
