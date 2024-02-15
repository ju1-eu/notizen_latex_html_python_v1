"""
Dieses Skript automatisiert die Einrichtung einer Entwicklungsumgebung in VS Code durch:
1. Installation einer Reihe spezifischer Erweiterungen.
2. Erstellung/Anpassung der settings.json mit vorgegebenen Einstellungen.
3. Erstellung einer .clang-format-Datei basierend auf dem Google C++ Style Guide.

Voraussetzungen:
- VS Code muss auf dem System installiert und der `code`-Befehl im PATH verfügbar sein.
- `clang-format` muss installiert sein für die Erstellung der .clang-format-Datei.
"""
import subprocess
import json
import os
import sys

# Liste der Erweiterungs-IDs mit Beschreibungen
extensions = {
   "ban.spellright": "Spell Right ist eine Rechtschreibprüfungserweiterung.",
   "ritwickdey.LiveServer": "Ermöglicht Live-Vorschau von Webseiten direkt im Browser.",
   "dbaeumer.vscode-eslint": "Integriert ESLint für JavaScript Linting.",
   "esbenp.prettier-vscode": "Code-Formatter für verschiedene Sprachen.",
   "ms-python.python": "Umfassende Unterstützung für Python-Entwicklung.",
   "ms-toolsai.jupyter": "Erstellung und Bearbeitung von Jupyter Notebooks.",
   "ms-python.vscode-pylance": "Erweiterte Python-Sprachunterstützung.",
   "ms-vscode.cpptools": "Unterstützung für C/C++ Entwicklung.",
   "ms-vscode.cmake-tools": "Unterstützung für CMake in VS Code.",
   "xaver.clang-format": "Automatische Formatierung von C/C++ Code.",
   "vsciot-vscode.vscode-arduino": "Unterstützung für Arduino-Entwicklung.",
   "ecmel.vscode-html-css": "Autovervollständigung für CSS-Klassen in HTML.",
   "bmewburn.vscode-intelephense-client": "PHP IntelliSense.",
   "James-Yu.latex-workshop": "Unterstützung für das Schreiben von LaTeX-Dokumenten.",
   "eamodio.gitlens": "Erweiterte Git-Integration und -Funktionalität.",
   "GitHub.vscode-pull-request-github": "Verwaltung von GitHub Pull Requests und Issues.",
   "yzhang.markdown-all-in-one": "Alles-in-einem Markdown-Unterstützung.",
   "shd101wyy.markdown-preview-enhanced": "Erweiterte Markdown-Vorschau.",
   "felixfbecker.php-debug": "PHP Debugging mit XDebug; ermöglicht das Debuggen von PHP-Code.",
   "xabikos.JavaScriptSnippets": "Sammlung von JavaScript (ES6)-Snippets für beschleunigte Entwicklung.",
   "ajshort.include-autocomplete": "Automatische Vervollständigung für #include-Anweisungen in C/C++.",
   "njpwerner.autodocstring": "Generiert automatisch detaillierte Docstrings für Python-Funktionen.",
   "DavidAnson.vscode-markdownlint": "Linting für Markdown-Dateien zur Sicherstellung von Konsistenz und Sauberkeit.",
   "yzane.markdown-pdf": "Konvertiert Markdown-Dateien in PDF, was die Verteilung und Präsentation vereinfacht.",
   "bierner.markdown-checkbox": "Unterstützung für interaktive Checkboxes in Markdown-Dokumenten.",
   "mhutchie.git-graph": "Visualisiert den Git-Verlauf als Graph, um die Repository-Historie zu veranschaulichen.",
   "DonJayamanne.githistory": "Ermöglicht die Anzeige der Git-Commit-Historie, einschließlich der Änderungen an Dateien.",
   "shaharkazaz.git-merger": "Vereinfacht den Git-Merge- und Rebase-Prozess innerhalb von VS Code.",
   "waderyan.gitblame": "Zeigt in der Statusleiste an, wer bestimmte Zeilen eines Files geändert hat."
}

# Konfigurationen für settings.json
settings = {
   "spellright.spellCheck": True,
   "spellright.documentTypes": ["markdown", "plaintext", "latex"],
   "spellright.language": ["de"],
   "spellright.ignoreWords": ["someCustomWord", "anotherWord"],
   "spellright.ignoreFiles": ["**/.git/**"],
   "editor.tabSize": 4,
   "editor.formatOnSave": True,
   "eslint.alwaysShowStatus": True,
   "python.analysis.typeCheckingMode": "basic",
   "python.linting.enabled": True,
   "python.linting.pylintEnabled": True,
   "python.linting.flake8Enabled": True,
   "python.formatting.provider": "black",
   "C_Cpp.updateChannel": "Default",
   "cmake.configureOnOpen": True,
   "clang-format.style": "file",
   "liveServer.settings.donotShowInfoMsg": True,
   "html-css-class-completion.enableEmmetSupport": True,
   "latex-workshop.latex.autoBuild.run": "onSave",
   "gitlens.views.repositories.files.layout": "tree",
   "markdown-all-in-one.italic.indicator": "_",
   "markdown-preview-enhanced.previewTheme": "github-dark.css",
   "latex-workshop.view.pdf.viewer": "tab",
   "markdown.preview.fontSize": 14,
   "markdown.preview.lineHeight": 1.6,
   "python.linting.flake8Args": ["--max-line-length=120"],
   "editor.codeActionsOnSave": {
   "source.fixAll.eslint": True
   },
   "python.testing.pytestArgs": [],
   "python.testing.unittestEnabled": False,
   "python.testing.nosetestsEnabled": False,
   "python.testing.pytestEnabled": True,
   "C_Cpp.clang_format_fallbackStyle": "Google",
   "files.autoSave": "onFocusChange",
   "editor.fontSize": 14,
   "platformio-ide.projectsDir": "/Ihr/Neuer/Pfad/PlatformIO/Projects"
}


def check_dependencies():
    """Überprüft, ob die notwendigen Abhängigkeiten (`code` und `clang-format`) verfügbar sind."""
    dependencies = ["code", "clang-format"]
    missing_dependencies = []
    for dependency in dependencies:
        if subprocess.call(["which", dependency], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            missing_dependencies.append(dependency)
    if missing_dependencies:
        print(f"Fehlende Abhängigkeiten: {', '.join(missing_dependencies)}. Bitte installieren Sie diese, bevor Sie fortfahren.")
        sys.exit(1)

def install_extensions(extensions_dict):
    """Installiert die definierten VS Code Erweiterungen."""
    for extension, description in extensions_dict.items():
        try:
            print(f"Installing {extension}: {description}")
            subprocess.run(["code", "--install-extension", extension], check=True)
        except subprocess.CalledProcessError:
            print(f"Fehler bei der Installation der Erweiterung {extension}. Bitte manuell überprüfen.")

def create_settings_file(settings_dict, project_root):
    """Erstellt oder aktualisiert die settings.json Datei."""
    settings_path = os.path.join(project_root, ".vscode", "settings.json")
    os.makedirs(os.path.dirname(settings_path), exist_ok=True)
    with open(settings_path, "w", encoding="utf-8") as file:
        json.dump(settings_dict, file, indent=4)
    print("settings.json erstellt/aktualisiert.")

def create_clang_format_file(project_root):
    """Erstellt eine .clang-format Datei mit Google-Stilrichtlinien."""
    clang_format_path = os.path.join(project_root, ".clang-format")
    try:
        with open(clang_format_path, "w") as file:
            subprocess.run(["clang-format", "-style=google", "-dump-config"], check=True, stdout=file)
        print(".clang-format Datei erstellt.")
    except subprocess.CalledProcessError:
        print("Fehler bei der Erstellung der .clang-format Datei. Bitte manuell überprüfen.")

if __name__ == "__main__":
    project_root = os.getcwd()  # Dynamische Ermittlung des Projektverzeichnisses
    check_dependencies()
    # Erweiterungen und Einstellungen hier definieren
    install_extensions(extensions)
    create_settings_file(settings, project_root)
    create_clang_format_file(project_root)
