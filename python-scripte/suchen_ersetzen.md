# Beschreibung

Dieses Skript durchläuft alle .tex-Dateien in einem vorgegebenen Verzeichnis und führt eine Reihe
von spezifischen Ersetzungen und Bereinigungen durch. Die Hauptziele sind:

Vorgehensweise:
1. Das Skript wechselt in das vorgegebene Verzeichnis TEX_PANDOC.
2. Es durchläuft alle .tex-Dateien und liest ihren Inhalt.
3. Spezifische Ersetzungen und Bereinigungen werden auf den Inhalt jeder Datei angewendet.
4. Der modifizierte Inhalt wird zurück in die jeweilige Datei geschrieben.
5. Nach der Bearbeitung aller Dateien kehrt das Skript zum ursprünglichen Verzeichnis zurück.

ANPASSEN:
- TEX_PANDOC: Pfad zum Verzeichnis, das die .tex-Dateien enthält.
- TIMESTAMP: Aktuelles Datum und Uhrzeit, verwendet für den eingefügten Kommentar.
- LABEL_REPLACE: Wörterbuch mit deutschen Sonderzeichen und ihren Ersetzungen
Befehle.

