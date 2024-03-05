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


def clean_up_table_content(content):
    # Entfernen der spezifischen Sequenzen
    patterns_to_remove = [
        r'\\toprule\\noalign{}\n',
        r'\\noalign{}\n\\endhead\n',
        r'\\bottomrule\\noalign{}\n\\endlastfoot\n',
    ]
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content)

    return content


def replace_longtable_with_table(match):
    column_definitions = match.group(1)
    content = match.group(2)
    cleaned_content = clean_up_table_content(content)
    # Verwenden von [h] für die Platzierung und Hinzufügen von \bottomrule am Ende der Tabelle
    return f"\\begin{{table}}[ht]\n  %\\caption{{}}\n  %\\label{{tab:my-table}}\n  \\begin{{tabular}}{{@{{}}{column_definitions}@{{}}}}\n  \\toprule\n" + cleaned_content + "  \\bottomrule\n  \\end{tabular}%\n\\end{table}"

def convert_longtable_to_table(latex_content):
    pattern = r'\\begin{longtable}\[\]{@{}(.*?)@{}}(.*?)\\end{longtable}'
    replaced_content = re.sub(pattern, replace_longtable_with_table, latex_content, flags=re.DOTALL)
    return replaced_content


def adjust_table_format(latex_content):
    def extract_and_clean_table_content(table_content):
        # Extrahieren des Hauptinhalts der Tabelle
        main_content_match = re.search(r'\\toprule(.*?)\\bottomrule', table_content, flags=re.DOTALL)
        if main_content_match:
            main_content = main_content_match.group(1)
        else:
            main_content = "Inhalt konnte nicht extrahiert werden."

        # Entfernen von 'minipage' und anderen spezifischen Formatierungen
        clean_content = re.sub(r'\\begin{minipage}\[.*?\]{.*?}\\raggedright', '', main_content)
        clean_content = re.sub(r'\\end{minipage}', '', clean_content)

        return clean_content.strip()

    def replacement_function(match):
        original_table_structure = match.group(0)
        table_content = extract_and_clean_table_content(original_table_structure)

        # Berechnung der Spaltenanzahl
        columns_count = table_content.count('&') // table_content.count('\\\\') + 1

        # Erstellen der neuen Tabellenstruktur
        new_table_structure = f'\\begin{{tabular}}{{@{{}}{"l" * columns_count}@{{}}}}\n\\toprule\n{table_content}\n\\bottomrule\n\\end{{tabular}}'
        
        return new_table_structure

    # Ersetzen spezifisch formatierter Tabellen
    adjusted_content = re.sub(
        r'\\begin{tabular}{@{}\s*>\s*{\\raggedright.*?\\end{tabular}',
        replacement_function,
        latex_content,
        flags=re.DOTALL
    )

    return adjusted_content


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
        floatnotes = '%\\floatnotes{}\n'
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

        print(f"Verarbeite {filename}...")  # Bestätigung, dass die Datei gelesen wird

        content = add_or_replace_comment(content, filename)
        # Anwenden der Funktion zur Aktualisierung der figure Umgebung
        content = update_figure_environment(content)

        content = content.replace(',height=\\textheight', '')
        content = content.replace('``', '>>')
        content = content.replace("''", '<<')
        content = content.replace('\\tightlist', '')
        content = re.sub(r'\\label{([^}]*?)}',
                         replace_german_chars_in_label, content)
        content = re.sub(
            r'\\passthrough{\\lstinline!(.*?)!}', r'\\verb|\1|', content)
        
        # Ersetzen Sie alle longtable-Umgebungen und deren Inhalt durch table
        content = convert_longtable_to_table(content)
        # Ersetze
        content = content.replace('\\midrule', '\\midrule[\\heavyrulewidth]\n')
        content = adjust_table_format(content)

        content = re.sub(r'\\\(', '$', content)
        content = re.sub(r'\\\)', '$', content)

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

os.chdir('..')

print("...fertig")
