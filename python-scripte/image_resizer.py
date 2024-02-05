"""
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
"""

import argparse
import os
import subprocess

# Globale Standardwerte als Konstanten definieren
DEFAULT_QUALITY_WEBP = 80
DEFAULT_DPI_PDF = 72
DEFAULT_QUALITY_PDF = 80
# Einstellungsstufen in Ghostscript ('screen', 'ebook', 'printer', 'prepress')
DEFAULT_GS_QUALITY = "ebook"
DEFAULT_RESOLUTION = "1600x1600>"
INPUT_FOLDER = "images/input"
OUTPUT_FOLDER_WEB = "images/output/web"
OUTPUT_FOLDER_PRES = "images/output/presentation"


def convert_image_to_webp(input_path, output_path, resolution=DEFAULT_RESOLUTION,
                          quality=DEFAULT_QUALITY_WEBP):
    """
    Konvertiert ein Bild in das WebP-Format mit spezifizierter Auflösung und Qualität.

    Diese Funktion nimmt den Pfad zu einer Bilddatei entgegen, konvertiert das Bild ins WebP-Format
    und speichert es an einem neuen Ort. Sie verwendet das 'magick' Kommandozeilenwerkzeug
    (Teil von ImageMagick) für die Konvertierung, erlaubt die Anpassung der Bildauflösung und
    der Qualitätsstufe.

    Args:
        input_path (str): Der Pfad zur Eingabedatei. Das Bild, das konvertiert werden soll.
        output_path (str): Der Pfad, unter dem das konvertierte Bild gespeichert wird.
        resolution (str, optional): Die Zielauflösung für das Bild als Zeichenkette,
                                     z.B. '1600x1600>'. Standardwert ist DEFAULT_RESOLUTION.
        quality (int, optional): Die Qualitätsstufe für das konvertierte Bild. Muss ein
                                 Wert zwischen 0 und 100 sein, wobei 100 die höchste Qualität ist.
                                 Standardwert ist DEFAULT_QUALITY_WEBP.

    Diese Funktion gibt keine Werte zurück, sondern druckt eine Bestätigung aus, dass
    die Konvertierung erfolgreich war, und zeigt den Pfad der Ausgabedatei an.
    """
    subprocess.run(["magick", input_path, "-resize", resolution,
                   "-quality", str(quality), output_path], check=True)
    print(f"Konvertierung erfolgreich: {output_path}")


def convert_webp_to_pdf_with_optimization(input_path, output_path, dpi=DEFAULT_DPI_PDF, quality=DEFAULT_QUALITY_PDF):
    """
    Konvertiert ein WebP-Bild in eine PDF-Datei mit spezifizierter DPI und Qualität,
    und wendet JPEG-Kompression an, um die Dateigröße für optimale Darstellung zu reduzieren.

    Diese Funktion verwendet das 'magick' Kommandozeilenwerkzeug (Teil von ImageMagick), um
    ein WebP-Bild in ein PDF zu konvertieren. Dabei lässt sich die Auflösung (DPI) und die
    Qualität der Bildkompression anpassen. Die Kompression erfolgt über das JPEG-Format,
    was zu einer signifikanten Reduzierung der Dateigröße führen kann, ideal für Präsentationen
    oder Web-Uploads, bei denen die Dateigröße eine Rolle spielt.

    Args:
        input_path (str): Der Pfad zur WebP-Eingabedatei, die konvertiert werden soll.
        output_path (str): Der Pfad, unter dem das PDF gespeichert wird.
        dpi (int, optional): Die Auflösung (DPI) des erzeugten PDFs. Ein höherer DPI-Wert
                             führt zu einer höheren Bildqualität, aber auch zu einer
                             größeren Dateigröße. Standardwert ist DEFAULT_DPI_PDF.
        quality (int, optional): Die Qualitätsstufe für die JPEG-Kompression im PDF. Muss
                                 ein Wert zwischen 0 und 100 sein, wobei 100 die
                                 höchste Qualität ist. Standardwert ist DEFAULT_QUALITY_PDF.

    Diese Funktion gibt keine Werte zurück, sondern druckt eine Bestätigung aus, dass die
    Konvertierung erfolgreich war, und zeigt den Pfad der Ausgabedatei an.
    """
    subprocess.run([
        "magick", input_path,
        "-density", str(dpi),
        "-quality", str(quality),
        "-compress", "jpeg",
        output_path
    ], check=True)
    print(f"Optimierte Konvertierung zu PDF erfolgreich: {output_path}")


def compress_pdf_with_ghostscript(input_path, output_path, quality="ebook"):
    """
    Verwendet Ghostscript, um die Größe einer PDF-Datei zu reduzieren.
    Die Qualitätsoption kann sein: 'screen', 'ebook', 'printer', 'prepress'
    """
    try:
        subprocess.run([
            "gs", "-sDEVICE=pdfwrite", f"-dPDFSETTINGS=/{quality}",
            "-dCompatibilityLevel=1.4", "-dNOPAUSE", "-dBATCH",
            f"-sOutputFile={output_path}", input_path
        ], check=True)
        print(f"PDF-Kompression erfolgreich: {output_path}")
    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Fehler bei der PDF-Kompression: {error}")


def process_images(input_folder, output_folder_web, output_folder_pres, resolution, web_quality,
                   pdf_dpi, pdf_quality, gs_quality):
    """
    Verarbeitet eine Sammlung von Bildern für Web- und Präsentationszwecke durch Konvertierung
    und Optimierung. Bilder im PNG- und HEIC-Format werden zu WebP konvertiert für Web-Zwecke
    und anschließend zu optimierten PDFs für Präsentationen.

    Args:
        input_folder (str): Pfad zum Ordner, der die Eingabebilder enthält.
        output_folder_web (str): Zielordner für die konvertierten WebP-Bilder.
        output_folder_pres (str): Zielordner für die daraus erzeugten und optimierten PDF-Dateien.
        resolution (str): Die Zielauflösung für WebP-Bilder, z.B. '1600x1600>'.
        web_quality (int): Qualitätseinstellung für die WebP-Bilder (0-100).
        pdf_dpi (int): DPI-Einstellung für die PDF-Erzeugung.
        pdf_quality (int): Qualitätseinstellung für die PDF-Kompression (0-100).
        gs_quality (str): Qualitätseinstellung für Ghostscript beim Komprimieren der PDFs,
                          unterstützt Werte wie 'screen', 'ebook', 'printer', 'prepress'.

    Dieses Skript erstellt zunächst die Zielordner (falls nicht vorhanden), durchläuft dann alle
    Bilder im Eingabeordner und konvertiert unterstützte Formate (PNG, HEIC) zu WebP für die
    Webnutzung. Anschließend werden diese WebP-Bilder zu temporären PDFs konvertiert, die
    durch Ghostscript weiter optimiert werden, bevor die temporären Dateien gelöscht werden.

    Die Funktion gibt keine Werte zurück, sondern druckt Statusmeldungen während der Verarbeitung.
    """
    os.makedirs(output_folder_web, exist_ok=True)
    os.makedirs(output_folder_pres, exist_ok=True)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]

        # Ziel-Pfade
        output_path_webp = os.path.join(output_folder_web, base_name + '.webp')
        output_path_pdf = os.path.join(output_folder_pres, base_name + '.pdf')

        # Konvertiert PNG und HEIC Bilder zu WebP für das Web
        if filename.lower().endswith((".png", ".heic")):
            convert_image_to_webp(
                file_path, output_path_webp, resolution=resolution, quality=web_quality)
            temp_pdf_path = output_path_pdf.replace('.pdf', '_temp.pdf')
            convert_webp_to_pdf_with_optimization(
                output_path_webp, temp_pdf_path, dpi=pdf_dpi, quality=pdf_quality)
            compress_pdf_with_ghostscript(
                temp_pdf_path, output_path_pdf, quality=gs_quality)
            os.remove(temp_pdf_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Bildverarbeitung für Web und Präsentationen.")
    parser.add_argument("--input_folder", default=INPUT_FOLDER,
                        help="Pfad zum Eingabeordner mit den Bildern.")
    parser.add_argument("--output_folder_web", default=OUTPUT_FOLDER_WEB,
                        help="Pfad zum Ausgabeordner für Web-Bilder.")
    parser.add_argument("--output_folder_pres", default=OUTPUT_FOLDER_PRES,
                        help="Pfad zum Ausgabeordner für Präsentations-PDFs.")
    parser.add_argument("--web_quality", type=int, default=DEFAULT_QUALITY_WEBP,
                        help="Qualität der WebP-Bilder (Standard: 80).")
    parser.add_argument("--pdf_dpi", type=int, default=DEFAULT_DPI_PDF,
                        help="DPI für PDF-Bilder (Standard: 72).")
    parser.add_argument("--pdf_quality", type=int, default=DEFAULT_QUALITY_PDF,
                        help="Qualität der PDF-Bilder (Standard: 80).")
    parser.add_argument("--gs_quality", default=DEFAULT_GS_QUALITY,
                        help="Ghostscript Qualitätseinstellung für PDF-Kompression")
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION,
                        help="Auflösung für die Bildkonvertierung zu WebP (Standard: 1200x1200>).")

    args = parser.parse_args()

    process_images(
        input_folder=args.input_folder,
        output_folder_web=args.output_folder_web,
        output_folder_pres=args.output_folder_pres,
        resolution=args.resolution,
        web_quality=args.web_quality,
        pdf_dpi=args.pdf_dpi,
        pdf_quality=args.pdf_quality,
        gs_quality=args.gs_quality
    )
