# Beschreibung

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

