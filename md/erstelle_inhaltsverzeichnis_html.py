import os
import glob
import subprocess
from urllib.parse import quote
from datetime import datetime

# Pfad zum aktuellen Verzeichnis
aktueller_ordner = os.getcwd()

# Konvertiere alle Markdown-Dateien in HTML
md_dateien = glob.glob(os.path.join(aktueller_ordner, '*.md'))
for md_datei in md_dateien:
    html_datei = md_datei.rsplit('.', 1)[0] + '.html'
    subprocess.run(["pandoc", md_datei, "-o", html_datei,
                    "-c", "inhalt.css", "--mathjax"])

# Pattern für das Finden von HTML-Dateien
html_dateien = glob.glob(os.path.join(aktueller_ordner, '*.html'))

# HTML5-Grundgerüst mit MathJax
html_boilerplate = '''
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inhalt</title>
    <link rel="stylesheet" href="inhalt.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
</head>
<body>
    <div class="container">
        <header>
            <h1>Inhaltsverzeichnis</h1>
        </header>
        <nav id="TOC" class="flex">
            <ul>
'''

# Aktuelles Datum
aktuelles_datum = datetime.now().strftime("%d.%m.%Y")

# Erstellen des Inhaltsverzeichnisses und Einbetten der HTML-Inhalte
with open('INHALT.html', 'w', encoding='utf-8') as ausgabe:
    ausgabe.write(html_boilerplate)
    for datei in html_dateien:
        dateiname = os.path.basename(datei)
        ausgabe.write(
            f'<li><a href="#{quote(dateiname)}">{dateiname}</a></li>\n')
    ausgabe.write('</ul>\n</nav>\n<inhalt>')

    for datei in html_dateien:
        dateiname = os.path.basename(datei)
        ausgabe.write(f'<hr><h2 id="{quote(dateiname)}">{dateiname}</h2>\n')
        with open(datei, 'r', encoding='utf-8') as f:
            inhalt = f.read()
            ausgabe.write('<section>\n' + inhalt + '\n</section>\n')

    ausgabe.write('</inhalt>\n')

    # Footer hinzufügen
    ausgabe.write(
        f'<footer>\n<p>Erstellt am: {aktuelles_datum} von Jan Unger</p>\n</footer>\n')

    ausgabe.write(
        "</div>\n<script>hljs.highlightAll();</script>\n</body>\n</html>")


print("Inhaltsverzeichnis in HTML aus .md wurde erstellt.")
