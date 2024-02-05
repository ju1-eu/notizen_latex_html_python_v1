# sync_tex.py
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
