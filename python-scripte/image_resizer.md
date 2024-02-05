# Beschreibung

Dieses Skript (`image_resizer.py`) ist für die Verarbeitung von Bildern für Web und
Präsentationen optimiert. Es konvertiert Bilder in verschiedene Formate, optimiert sie
für spezifische Anwendungsfälle und erzeugt daraus PDFs für Präsentationen.

Eingabe:
- Bilder im PNG- und HEIC-Format, typischerweise Screenshots oder Fotos von Handys.

Ausgabe:
- Für Web optimierte Bilder: Konvertiert PNG und HEIC Bilder zu WebP mit einer
    Zielauflösung von 1600x, einer Qualität von 80% und 72dpi, um schnelle Ladezeiten
    zu gewährleisten.
- Für Präsentationen optimierte Bilder: Konvertiert WebP Bilder zu PDF, angepasst für das
    Seitenverhältnis 16:10, ideal für Beamer-Präsentationen.

Verarbeitungsschritte:
1. Konvertierung von PNG und HEIC zu WebP für das Web mit angepassten Einstellungen für Größe,
    Qualität und Auflösung.
2. Konvertierung von WebP zu PDF für Präsentationen mit Optimierung für die Darstellung auf Beamern.
3. Anwendung von Ghostscript zur weiteren Kompression der PDF-Dateien, mit anpassbaren
    Qualitätsstufen ('screen', 'ebook', 'printer', 'prepress').

Die Konfiguration der Bildverarbeitungseinstellungen wie Auflösung, Qualität und DPI kann
über Befehlszeilenargumente angepasst werden.

Beispielverwendung:
$ python image_resizer.py --input_folder images/input --output_folder_web images/output/web
    --output_folder_pres images/output/presentation

Dabei werden globale Standardwerte für die Konvertierungseinstellungen verwendet, die jedoch
über die Befehlszeilenargumente überschrieben werden können.

