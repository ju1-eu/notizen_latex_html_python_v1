"""
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
"""

import subprocess


def sicherer_aufruf(befehl):
    """Führt einen Befehl sicher aus."""
    try:
        subprocess.run(befehl, check=True)
    except subprocess.CalledProcessError:
        print("Es gab einen Fehler beim Ausführen des Befehls.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


def synchronisiere_tex_dateien(spezifische_datei=None):
    """Synchronisiert .tex-Dateien basierend auf der Benutzerauswahl."""
    befehl = ["rsync", "-avh", "--progress"]
    if spezifische_datei:
        # Korrigiere hier den Pfad zur spezifischen Datei
        vollstaendiger_pfad = "tex/" + spezifische_datei
        befehl.append(vollstaendiger_pfad)
    else:
        befehl.append("tex/")
    befehl.append(".")  # Zielverzeichnis
    sicherer_aufruf(befehl)


def auswahl_und_synchronisierung():
    """Ermöglicht die Benutzerauswahl und führt die Synchronisation durch."""
    auswahl = input(
        "Möchten Sie alle Dateien kopieren (A) oder nur eine bestimmte (B)? [A/B]: ").strip().upper()
    if auswahl == "A":
        synchronisiere_tex_dateien()  # Alle Dateien synchronisieren
    elif auswahl == "B":
        dateiname = input(
            "Geben Sie den Namen der Datei ein (z.B. beispiel.tex): ")
        # Spezifische Datei synchronisieren
        synchronisiere_tex_dateien(dateiname)
    else:
        print("Ungültige Auswahl.")


def main():
    auswahl_und_synchronisierung()


if __name__ == "__main__":
    main()
