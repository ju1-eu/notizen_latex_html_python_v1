"""
Bilder
input: Screenshots png und  Handy heic
output:
    - web (schnelle Ladezeiten, 1600x, Qualität: 80%, 72dpi) png => webp und heic => webp
    - Beamer (Präsentation, 16:10): webp => pdf
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


def convert_image_to_webp(input_path, output_path, resolution=DEFAULT_RESOLUTION, quality=DEFAULT_QUALITY_WEBP):
    subprocess.run(["magick", input_path, "-resize", resolution,
                   "-quality", str(quality), output_path], check=True)
    print(f"Konvertierung erfolgreich: {output_path}")


def convert_webp_to_pdf_with_optimization(input_path, output_path, dpi=DEFAULT_DPI_PDF, quality=DEFAULT_QUALITY_PDF):
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
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Fehler bei der PDF-Kompression: {e}")


def process_images(input_folder, output_folder_web, output_folder_pres, resolution, web_quality, pdf_dpi, pdf_quality, gs_quality):
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
                        help="Ghostscript Qualitätseinstellung für PDF-Kompression ('screen', 'ebook', 'printer', 'prepress'). Standard: 'ebook'.")
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
