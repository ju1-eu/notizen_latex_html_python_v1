# Beschreibung

Dieses Script (`scriptauswahl.py`) stellt ein interaktives Menüsystem bereit, das verschiedene
Automatisierungsbefehle für die Verarbeitung von LaTeX- und HTML-Dateien anbietet.

Hauptfunktionen:
- `kombinierte_html_verarbeitung()`: Führt eine Reihe von HTML-bezogenen Befehlen sequenziell aus.
- `sicherer_aufruf(befehl)`: Führt einen gegebenen Befehl sicher aus, fängt und behandelt Fehler.
- `zeige_menue_und_waehle()`: Zeigt das Befehlsmenü an und liest die Benutzerauswahl ein.
- `pause()`: Pausiert die Ausführung, bis der Benutzer eingreift.
- `verarbeite_alle_tex_dateien()`: Synchronisiert alle `.tex`-Dateien in einem
    bestimmten Verzeichnis.
- `kombinierte_latex_verarbeitung()`: Führt eine Sequenz von Schritten zur Verarbeitung
    von LaTeX-Dateien durch.
- `main()`: Initialisiert die Benutzerschnittstelle des Menüsystems und
    verarbeitet Benutzereingaben.

Parameter:
- Keine expliziten Parameter für die Hauptfunktionen; sie werden hauptsächlich
    durch Benutzerinteraktion gesteuert.

Rückgabewerte:
- Keine der Funktionen liefert explizite Werte zurück; sie führen Seiteneffekte aus
    (z.B. Dateiverarbeitung, Ausgabe auf die Konsole).

