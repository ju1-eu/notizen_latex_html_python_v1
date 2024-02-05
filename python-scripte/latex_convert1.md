# Beschreibung

Konvertiert Markdown-Dateien zu LaTeX-Dateien unter Verwendung von Pandoc und einer spezifizierten
LaTeX-Vorlage.

Dieses Skript dient dazu, alle .md-Dateien in einem vorgegebenen Quellverzeichnis (QUELLPFAD)
in .tex-Dateien im Zielverzeichnis (ZIELPFAD) zu konvertieren. Dabei wird für die Konvertierung
eine spezifische LaTeX-Vorlage (VORLAGEPFAD) verwendet. Das Skript prüft zunächst, ob Pandoc auf
dem System installiert ist, da Pandoc für die Konvertierung erforderlich ist.

Funktionalitäten:
- Überprüft die Installation von Pandoc auf dem System.
- Konvertiert eine spezifische Markdown-Datei oder alle Markdown-Dateien im Quellverzeichnis
    zu LaTeX.
- Verwendet eine benutzerdefinierte LaTeX-Vorlage für die Konvertierung.
- Unterstützt die Extraktion des Themas aus dem Dateinamen zur Verwendung in der konvertierten
    Datei.

Konstanten:
- QUELLPFAD: Der Pfad zum Verzeichnis, das die Markdown-Quelldateien enthält.
- ZIELPFAD: Der Pfad zum Verzeichnis, in das die konvertierten LaTeX-Dateien geschrieben werden.
- VORLAGEPFAD: Der Pfad zur LaTeX-Vorlagendatei, die für die Konvertierung verwendet wird.

Funktionen:
- ist_pandoc_installiert(): Prüft, ob Pandoc auf dem System installiert ist.
- extrahiere_thema_aus_dateiname(dateiname): Extrahiert das Thema aus dem Dateinamen einer
    Markdown-Datei.
- konvertiere_md_zu_tex(md_pfad, tex_pfad): Konvertiert eine einzelne Markdown-Datei in eine
    LaTeX-Datei unter Verwendung der spezifizierten Vorlage.
- konvertiere_dateien(dateiname=None): Steuert die Konvertierung basierend auf der Benutzereingabe
    oder konvertiert alle Dateien im Quellverzeichnis.
- main(): Hauptfunktion, die die Ausführung des Skripts steuert und die Konvertierung initiiert.

Verwendung:
- Das Skript ohne Argumente ausführen, um alle Markdown-Dateien im QUELLPFAD zu konvertieren.
- Ein spezifischer Dateiname als Argument übergeben, um nur eine bestimmte Markdown-Datei zu
    konvertieren.

Beispiel:
- Alle .md-Dateien konvertieren: python skriptname.py
- Eine spezifische .md-Datei konvertieren: python skriptname.py --dateiname meine_datei.md

Anforderungen:
- Pandoc muss auf dem System installiert sein.

