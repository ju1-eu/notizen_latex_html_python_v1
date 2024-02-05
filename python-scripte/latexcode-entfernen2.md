# Beschreibung

Das Programm bearbeitet LaTeX-Dateien, indem es spezifische Befehle entfernt und vorherige Versionen der Dateien in Backup-Dateien speichert. Es kann entweder alle Dateien in einem Verzeichnis oder eine bestimmte Datei bearbeiten. Am Ende werden alle Backup-Dateien gelöscht.
python3 ./latex-convert1.py # alle Dateien konvertieren (A) oder nur eine bestimmte (B)
python3 ./latexcode-entfernen2.py # alle Dateien
python3 ./latexcode-entfernen2.py -h # Hilfe
python3 ./latexcode-entfernen2.py --datei DATEI # nur eine Datei ohne .tex
make # pdflatex - alle Dateien
make compile_with_xelatex # xelatex - alle Dateien
make single_pdflatex FILE=datei # pdflatex - nur eine Datei ohne .tex
make single_xelatex FILE=datei # xelatex - nur eine Datei ohne .tex

