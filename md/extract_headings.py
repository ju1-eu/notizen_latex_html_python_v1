"""
Dieses Skript extrahiert Überschriften aus Markdown-Dateien und speichert sie in einer Textdatei.

Das Skript nutzt reguläre Ausdrücke, um Markdown-Überschriften (von Level 1 bis 4) zu identifizieren
und extrahiert diese in eine separate Textdatei. Es ist nützlich, um schnell die Struktur eines
Markdown-Dokuments zu erfassen oder ein Inhaltsverzeichnis zu erstellen.

Funktionen:
    - extract_headings(md_file_path, txt_file_path): Hauptfunktion zum Extrahieren der Überschriften.

Verwendung:
    - Die Pfade für die Quell-Markdown-Datei und die Ziel-Textdatei müssen als Argumente
      an die Funktion `extract_headings` übergeben werden.
    - Das Skript gibt Feedback über den Erfolg der Operation oder mögliche Fehler aus.

Beispiel:
    md_file_path = 'Beispiel.md'
    txt_file_path = 'extrahierte_ueberschriften.txt'
    extract_headings(md_file_path, txt_file_path)

Anforderungen:
    - Python 3.x
    - Keine externen Bibliotheken erforderlich.

Autor: [Dein Name]
Version: 1.0
"""
import re
from pathlib import Path

def extract_headings(md_file_path, txt_file_path):
    """
    Extrahiert Überschriften aus einer Markdown-Datei und speichert sie in einer Textdatei.

    Args:
        md_file_path (str): Pfad zur Quell-Markdown-Datei.
        txt_file_path (str): Pfad zur Ziel-Textdatei, in die die Überschriften geschrieben werden.

    Returns:
        None. Die extrahierten Überschriften werden in der angegebenen Textdatei gespeichert.
    """
    # Verbesserter regulärer Ausdruck für Überschriften
    heading_pattern = re.compile(r'^#{1,4}\s.*$', re.MULTILINE)

    try:
        # Verwendung von Path für plattformübergreifende Kompatibilität
        md_file_path = Path(md_file_path)
        txt_file_path = Path(txt_file_path)

        with md_file_path.open('r', encoding='utf-8') as md_file:
            with txt_file_path.open('w', encoding='utf-8') as txt_file:
                for line in md_file:
                    if heading_pattern.match(line):
                        txt_file.write(line)
        print(f"Überschriften wurden erfolgreich nach {txt_file_path} extrahiert.")
    except FileNotFoundError:
        print(f"Die Datei {md_file_path} wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Dateipfade festlegen
md_file_path = 'ErsteHilfe-notiz.md'
txt_file_path = 'headings_extracted.txt'

# Funktion ausführen
extract_headings(md_file_path, txt_file_path)
