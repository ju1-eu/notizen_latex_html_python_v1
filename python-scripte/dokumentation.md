# Beschreibung

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

