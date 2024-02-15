# Beschreibung

Dieses Skript konvertiert Markdown-Dateien (.md) aus einem Quellverzeichnis in LaTeX (.tex) Dateien
in einem Zielverzeichnis, unter Verwendung von Pandoc und einer benutzerdefinierten LaTeX-Vorlage.

Funktionalitäten:
- Überprüft, ob Pandoc auf dem System installiert ist.
- Erlaubt die Konvertierung einer Markdown-Datei oder aller Markdown-Dateien
- Nutzt eine LaTeX-Vorlage für die Konvertierung.
- Erstellt das Zielverzeichnis, falls es nicht existiert.
- Extrahiert das Thema aus dem Dateinamen der Markdown-Datei und setzt es als Titelvariable
    für Pandoc.

Verwendung:
- Zum Konvertieren aller Markdown-Dateien im Quellverzeichnis einfach das Skript ohne Argumente
    ausführen.
- Zum Konvertieren einer spezifischen Markdown-Datei das Skript mit dem Dateinamen als Argument
    ausführen.

Konstanten:
- QUELLPFAD: Verzeichnis mit den Quell-Markdown-Dateien.
- ZIELPFAD: Verzeichnis, in das die konvertierten LaTeX-Dateien geschrieben werden.
- VORLAGEPFAD: LaTeX-Vorlagendatei, die von Pandoc für die Konvertierung verwendet wird.

Das Skript besteht aus mehreren Funktionen:
- `ist_pandoc_installiert()`: Überprüft die Verfügbarkeit von Pandoc auf dem System.
- `extrahiere_thema_aus_dateiname(dateiname)`: Extrahiert das Thema aus dem Dateinamen
- `konvertiere_md_zu_tex(md_pfad, tex_pfad)`: Führt die eigentliche Konvertierung für eine einzelne
    Datei durch.
- `konvertiere_dateien(dateiname=None)`: Steuert die Konvertierung basierend auf der
    Benutzereingabe oder konvertiert alle Dateien.
- `main()`: Hauptfunktion, steuert Ausführung des Skripts.

