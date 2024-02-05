# Beschreibung

Dieses Skript ermöglicht die Synchronisation von LaTeX (.tex) Dateien zwischen dem aktuellen
Verzeichnis und einem spezifizierten Quellverzeichnis.
Der Benutzer hat die Möglichkeit, entweder alle `.tex`-Dateien oder eine spezifische Datei zu
synchronisieren.

Verwendung:
- Das Skript fragt den Benutzer interaktiv, ob alle Dateien oder nur eine bestimmte Datei
    synchronisiert werden sollen.
- Bei Auswahl einer spezifischen Datei wird der Benutzer aufgefordert, den Dateinamen einzugeben.

Funktionen:
- `sicherer_aufruf(befehl)`: Führt einen gegebenen Shell-Befehl aus und fängt mögliche Fehler ab.
    Dies umfasst die Behandlung von `subprocess.CalledProcessError` für fehlgeschlagene Befehle
    und allgemeine Ausnahmen.
- `synchronisiere_tex_dateien(spezifische_datei=None)`: Führt die Synchronisation durch. Wenn ein
    Dateiname angegeben wird, synchronisiert es nur diese spezifische Datei. Ohne Angabe werden
    alle `.tex`-Dateien im Quellverzeichnis synchronisiert.
- `auswahl_und_synchronisierung()`: Interaktive Funktion, die die Benutzerauswahl
    abfragt und die entsprechende Synchronisation initiiert.
- `main()`: Einstiegspunkt des Skripts, der die Auswahl und Synchronisation startet.

