# Beschreibung

Dieses Skript konvertiert Markdown-Dateien in HTML unter Verwendung von Pandoc und berücksichtigt
dabei Zitierungen
mit einem spezifischen Zitierstil sowie mehrere Bibliographiequellen. Es ermöglicht die Erstellung
von HTML-Dokumenten
mit akademischen Referenzen direkt aus Markdown-Quelldateien.

Funktionalitäten:
- Durchsucht einen spezifizierten Quellordner nach Markdown-Dateien und konvertiert diese in
    HTML-Dateien im Zielordner.
- Nutzt Pandoc für die Konvertierung und wendet dabei einen spezifischen CSL-Zitierstil an.
- Bezieht Informationen aus mehreren Bibliographiequellen (.bib-Dateien) für die Zitierungen.
- Prüft, ob Pandoc auf dem System installiert ist, bevor mit der Konvertierung begonnen wird.
- Verwendet sichere Pfadverknüpfungen, um Traversierungsversuche zu verhindern.

Konstanten:
- QUELL_ORDNER: Verzeichnis, das die zu konvertierenden Markdown-Quelldateien enthält.
- ZIEL_ORDNER: Verzeichnis für die resultierenden HTML-Dateien.
- ERWEITERUNG: Die Dateierweiterung der zu konvertierenden Dateien (Standard: ".md").
- csl_datei: Der Pfad zur CSL-Datei, die den Zitierstil definiert.
- bib_dateien: Eine Liste von Pfaden zu .bib-Dateien, die die Bibliographiequellen enthalten.

Funktionen:
- sicher_verknuepfen(ordner, dateiname): Verknüpft einen Ordner und einen Dateinamen sicher.
- markdown_nach_html_konvertieren(quell_datei, ziel_datei): Konvertiert eine einzelne
    Markdown-Datei in eine HTML-Datei unter Verwendung von Pandoc.
- pandoc_ist_installiert(): Überprüft, ob Pandoc auf dem System installiert ist.
- main(): Hauptfunktion, die die Konvertierung koordiniert und die anderen Funktionen aufruft.

Verwendung:
- Stellen Sie sicher, dass Pandoc installiert ist und die erforderlichen .bib- und .csl-Dateien
    verfügbar sind.
- Passen Sie bei Bedarf die Konstanten an Ihre Umgebung an.
- Führen Sie das Skript aus, um die Konvertierung zu starten.

Beispielaufruf:
    python3 mein_skript.py

Anforderungen:
- Pandoc muss auf dem System installiert sein.

Hinweis:
- Das Skript setzt voraus, dass die Quelldateien korrekt formatiertes Markdown enthalten und
    dass die Bibliographiequellen und der Zitierstil korrekt definiert sind.

