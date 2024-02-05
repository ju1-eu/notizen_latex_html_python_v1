# Beschreibung

Dieses Skript automatisiert Git-Operationen, um den Workflow mit lokalen und entfernten
Git-Repositories zu vereinfachen.
Es bietet Funktionen für gängige Git-Aufgaben wie das Erstellen und Initialisieren
lokaler Repositories, das Verknüpfen mit GitHub,
das Hinzufügen, Commiten, Pushen und Pullen von Änderungen, das Verwalten von Branches und
das Anzeigen von Repository-Informationen.

Funktionsübersicht:
- Erstellen und Initialisieren eines lokalen Git-Repositories.
- Verknüpfen eines lokalen Repositories mit einem entfernten GitHub-Repository.
- Hinzufügen von Änderungen zum Staging-Bereich und Commiten dieser Änderungen.
- Pushen von Änderungen zu einem entfernten Repository und Pullen von Änderungen.
- Erstellen, Wechseln und Zusammenführen von Branches.
- Anzeigen von Status, Logs und Konflikten.
- Stashen von Änderungen und Löschen eines GitHub-Repositories.

Verwendung:
Das Skript wird über die Kommandozeile mit dem Namen des Zielordners als Argument aufgerufen, z.B.:
    python3 git_hilfsprogramm.py MeinProjekt

Es startet ein interaktives Menü, das es dem Benutzer ermöglicht, verschiedene Git-Operationen
auszuführen, indem die entsprechende Menüoption ausgewählt wird.

Anforderungen:
- Git muss auf dem System installiert und konfiguriert sein.
- Für einige Funktionen ist das GitHub CLI-Tool 'gh' erforderlich.
- Eine Internetverbindung ist für Operationen mit entfernten Repositories erforderlich.

Dieses Skript zielt darauf ab, die Verwendung von Git zu vereinfachen und Routineaufgaben
zu automatisieren, um die Effizienz bei der Versionskontrolle und Zusammenarbeit zu steigern.

