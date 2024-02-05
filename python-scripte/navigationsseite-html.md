## Dokumentation

### Beschreibung des Programms

Das erstellte Programm durchsucht einen spezifischen Ordner, standardmäßig benannt als "html", nach allen Dateien, die die Erweiterung `.html` haben. Es erstellt dann eine Navigationsseite, `navigation.html`, die Links zu allen gefundenen HTML-Dateien enthält. Die Struktur der Navigationsseite wird durch eine Vorlagendatei, standardmäßig benannt als `vorlage-nav.html`, bestimmt. Die Vorlage und das erstellte Navigationsdokument befinden sich im gleichen Verzeichnis wie das Skript.

### Testergebnisse

Das Programm wurde auf einem Ordner getestet, der mehrere HTML-Dateien enthält. Es hat erfolgreich eine Navigationsseite erstellt, die Links zu allen gefundenen HTML-Dateien enthält. Die Links waren korrekt und jede Verlinkung führte zur entsprechenden HTML-Datei.

Ein zweiter Test wurde durchgeführt, um zu überprüfen, ob das Programm die `navigation.html`-Datei korrekt ausschließt, wenn sie bereits im Ordner vorhanden ist. Es wurde festgestellt, dass das Programm wie erwartet funktioniert und `navigation.html` nicht als Link in der erstellten Navigationsseite erscheint.

Zusammengefasst: Das Programm hat alle Tests erfolgreich bestanden. Es hat gezeigt, dass es in der Lage ist, eine Navigationsseite korrekt zu erstellen, die auf alle HTML-Dateien in einem spezifizierten Ordner verweist, und dabei die Navigationsseite selbst ausschließt.