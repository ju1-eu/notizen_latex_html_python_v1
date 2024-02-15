"""
Dieses Skript durchläuft alle .tex-Dateien in einem vorgegebenen Verzeichnis und führt eine Reihe
von spezifischen Ersetzungen und Bereinigungen durch. Die Hauptziele sind:

Vorgehensweise:
1. Das Skript wechselt in das vorgegebene Verzeichnis TEX_PANDOC.
2. Es durchläuft alle .tex-Dateien und liest ihren Inhalt.
3. Spezifische Ersetzungen und Bereinigungen werden auf den Inhalt jeder Datei angewendet.
4. Der modifizierte Inhalt wird zurück in die jeweilige Datei geschrieben.
5. Nach der Bearbeitung aller Dateien kehrt das Skript zum ursprünglichen Verzeichnis zurück.

ANPASSEN:
- TEX_PANDOC: Pfad zum Verzeichnis, das die .tex-Dateien enthält.
- TIMESTAMP: Aktuelles Datum und Uhrzeit, verwendet für den eingefügten Kommentar.
- LABEL_REPLACE: Wörterbuch mit deutschen Sonderzeichen und ihren Ersetzungen
Befehle.
"""

import re
import os
import datetime

# ANPASSEN
TEX_PANDOC = "./tex"
TIMESTAMP = datetime.datetime.now().strftime('%d-%b-%y')
LABEL_REPLACE = {
    'uxfc': 'ue',
    'uxf6': 'oe',
    'uxe4': 'ae',
    'uxdf': 'ss'
}


def add_or_replace_comment(content, filename):
    new_comment = f"% ju {TIMESTAMP} {filename}"
    content_lines = [line for line in content.splitlines(
    ) if not line.strip().startswith("% ju")]
    content_lines = [new_comment] + content_lines
    return "\n".join(content_lines)


def replace_german_chars_in_label(match):
    label_content = match.group(1)
    for char, replacement in LABEL_REPLACE.items():
        label_content = label_content.replace(char, replacement)
    return f"\\label{{{label_content}}}"

# nicht verwenden sonst keine Linie -------------------- möglich


def ersetze_match(match):
    label_text = match.group(1)
    return f"\\label{{{label_text.replace('---', '-')}}}"


def remove_hypertargets(text):
    return re.sub(r'\\hypertarget{[^}]*?}{[^}]*?}', '', text)


def replace_tables(match):
    column_spec = match.group(1)
    table_content = match.group(2)

    # Entferne doppelte \\toprule
    table_content = re.sub(r"\\\\toprule\s+\\\\toprule",
                           r"\\\\toprule", table_content)

    # Entferne \\endhead
    table_content = table_content.replace("\\endhead", "")

    # Erstelle die neue table-Umgebung
    return f"""\\begin{{table}}[!ht]
\\caption{{}}% \\label{{tab:}}%% anpassen
\\begin{{tabular}}{{@{{}}{column_spec}@{{}}}}
{table_content}
\\end{{tabular}}
\\floatnotes{{}}
\\end{{table}}"""


def update_figure_environment(content):
    # RegEx, um die figure Umgebung zu finden und zu aktualisieren
    pattern = re.compile(
        r'(\\begin{figure}\s*\\centering\s*)(\\includegraphics)(\{.*?\})',
        re.DOTALL
    )

    # Ersetzungsfunktion
    def repl(match):
        before = match.group(1)  # Der Teil vor \includegraphics
        # \includegraphics mit zusätzlicher Breitenangabe
        includegraphics = match.group(2) + '[width=0.8\\textwidth]'
        # Der Pfad und alles danach, bis zum Ende der figure Umgebung
        path_and_rest = match.group(3)
        # Der einzufügende \floatnotes Befehl
        floatnotes = '\\floatnotes{}\n'
        label = '%\\label{fig:}'  # Der \label Befehl
        # Zusammenfügen des neuen Inhalts
        new_content = f"{before}{includegraphics}{path_and_rest}\n{floatnotes}{label}"
        return new_content

    # Anwenden der Ersetzung
    updated_content = pattern.sub(repl, content)
    return updated_content


print("+ Suchen und Ersetzen => Latex")

os.chdir(TEX_PANDOC)

for filename in os.listdir('.'):
    if filename.endswith('.tex'):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        content = add_or_replace_comment(content, filename)
        # Anwenden der Funktion zur Aktualisierung der figure Umgebung
        content = update_figure_environment(content)
        # FEHLER
        # content = remove_hypertargets(content)
        # content = re.sub(r'\\label{([^}]*?)}', ersetze_match, content)
        # Ersetze \midrule durch \midrule[\heavyrulewidth]
        content = content.replace('\\midrule', '\\midrule[\\heavyrulewidth]')
        content = content.replace(',height=\\textheight', '')
        content = content.replace('``', '>>')
        content = content.replace("''", '<<')
        content = content.replace('\\tightlist', '')
        content = re.sub(r'\\label{([^}]*?)}',
                         replace_german_chars_in_label, content)
        content = re.sub(
            r'\\passthrough{\\lstinline!(.*?)!}', r'\\verb|\1|', content)
        # Ersetzen Sie alle longtable-Umgebungen und deren Inhalt durch table
        content = re.sub(
            r'\\begin{longtable}\[\]{@{}(.*?)@{}}(.+?)\\end{longtable}', replace_tables, content, flags=re.DOTALL)

        content = re.sub(r'\\\(', '$', content)
        content = re.sub(r'\\\)', '$', content)

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

os.chdir('..')

print("...fertig")
