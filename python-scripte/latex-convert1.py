import os
import subprocess
import glob

# Konstanten
QUELLPFAD = "./md"
ZIELPFAD = "./tex"
VORLAGEPFAD = "content/vorlage-main.tex"  # Latexvorlage


def ist_pandoc_installiert():
    """Prüft, ob Pandoc auf dem System installiert ist."""
    try:
        subprocess.run(["pandoc", "--version"],
                       capture_output=True, check=True)
        return True
    except Exception:
        return False


def extrahiere_thema_aus_dateiname(dateiname):
    """Extrahiert das Thema aus dem Dateinamen."""
    # Nehmen Sie an, dass der Dateiname keine Erweiterung hat (z.B. .md)
    return os.path.splitext(os.path.basename(dateiname))[0]


def konvertiere_md_zu_tex(md_pfad, tex_pfad):
    """Konvertiert eine einzelne .md-Datei in .tex mit Pandoc, einer benutzerdefinierten CSL-Datei und einer Bibliographie."""
    thema = extrahiere_thema_aus_dateiname(md_pfad)

    try:
        subprocess.run(
            [
                "pandoc",
                "--template=" + VORLAGEPFAD,
                "--listings",
                "--variable=title:" + thema,
                md_pfad,
                "-o",
                tex_pfad,
            ],
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Konvertierung der Datei {
              md_pfad}:\n{e.stderr.decode()}")


def konvertiere_dateien(dateiname=None):
    """Konvertiert ausgewählte oder alle Markdown-Dateien zu LaTeX."""
    if not os.path.exists(QUELLPFAD):
        print(f"Quellordner {QUELLPFAD} existiert nicht.")
        return

    if not os.path.exists(VORLAGEPFAD):
        print(f"Vorlage {VORLAGEPFAD} existiert nicht.")
        return

    if not os.path.isdir(ZIELPFAD):
        os.makedirs(ZIELPFAD)

    if dateiname:
        if not dateiname.endswith(".md"):
            print("Bitte eine gültige .md-Datei angeben.")
            return
        md_dateien = [os.path.join(QUELLPFAD, dateiname)]
    else:
        md_dateien = glob.glob(os.path.join(QUELLPFAD, "*.md"))

    for md_datei in md_dateien:
        if not os.path.exists(md_datei):
            print(f"Die Datei {md_datei} existiert nicht.")
            continue
        tex_datei = os.path.join(ZIELPFAD, os.path.splitext(
            os.path.basename(md_datei))[0] + ".tex")
        konvertiere_md_zu_tex(md_datei, tex_datei)

    print("Konvertierung abgeschlossen.")


def main():
    if not ist_pandoc_installiert():
        print(
            "Pandoc ist nicht installiert. Bitte installieren Sie Pandoc, um fortzufahren.")
        return
    konvertiere_dateien()


if __name__ == "__main__":
    main()
