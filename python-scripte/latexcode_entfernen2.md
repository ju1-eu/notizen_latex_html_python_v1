# Beschreibung

Dieses Skript konvertiert Markdown-Dateien (.md) aus einem Quellverzeichnis in LaTeX (.tex) Dateien
in einem Zielverzeichnis, unter Verwendung von Pandoc und einer benutzerdefinierten LaTeX-Vorlage.

Funktionalitäten:
- Überprüft, ob Pandoc auf dem System installiert ist.
- Erlaubt die Konvertierung einer spezifischen Markdown-Datei oder aller Markdown-Dateien im

Quellverzeichnis.
- Nutzt eine spezifizierte LaTeX-Vorlage für die Konvertierung.
- Erstellt das Zielverzeichnis, falls es nicht existiert.
- Extrahiert das Thema aus dem Dateinamen der Markdown-Datei und setzt es als Titelvariable
    für Pandoc.

Voraussetzungen:
- Pandoc muss auf dem System installiert sein.
- Eine LaTeX-Vorlage muss im angegebenen VORLAGEPFAD vorhanden sein.

Verwendung:
- Zum Konvertieren aller Markdown-Dateien im Quellverzeichnis einfach das Skript ohne Argumente
    ausführen.
- Zum Konvertieren einer spezifischen Markdown-Datei das Skript mit dem Dateinamen als Argument
    ausführen.

Konstanten:
- QUELLPFAD: Pfad zum Verzeichnis mit den Quell-Markdown-Dateien.
- ZIELPFAD: Pfad zum Verzeichnis, in das die konvertierten LaTeX-Dateien geschrieben werden.
- VORLAGEPFAD: Pfad zur LaTeX-Vorlagendatei, die von Pandoc für die Konvertierung verwendet wird.

Das Skript besteht aus mehreren Funktionen:
- `ist_pandoc_installiert()`: Überprüft die Verfügbarkeit von Pandoc auf dem System.
- `extrahiere_thema_aus_dateiname(dateiname)`: Extrahiert das Thema aus dem Dateinamen der
    Markdown-Datei.
- `konvertiere_md_zu_tex(md_pfad, tex_pfad)`: Führt die eigentliche Konvertierung für eine einzelne
    Datei durch.
- `konvertiere_dateien(dateiname=None)`: Steuert die Konvertierung basierend auf der
    Benutzereingabe oder konvertiert alle Dateien.
- `main()`: Hauptfunktion, die die Ausführung des Skripts steuert.

Anmerkungen:
- Das Skript setzt voraus, dass die Markdown-Dateien keine Erweiterung im Namen haben (außer .md)
    und dass sie im QUELLPFAD liegen.
- Fehlermeldungen werden ausgegeben, wenn erforderliche Komponenten fehlen oder Probleme bei der
    Konvertierung auftreten.

