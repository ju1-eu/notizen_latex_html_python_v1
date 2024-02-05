# Beschreibung

Dieses Skript durchsucht HTML-Dateien in einem vorgegebenen Verzeichnis nach Referenzen auf .eps-
und .pdf-Dateien
innerhalb von Bildquellen (src-Attribut) und ersetzt diese durch Referenzen auf .svg- bzw.
.webp-Dateien.

Die Ersetzung erfolgt auf der Basis von regulären Ausdrücken, die definierte Muster für .eps- und
.pdf-Dateien erkennen
und diese durch neue Pfade für .svg- und .webp-Dateien ersetzen. Die Pfade zu den Original- und
Zielbildern werden
innerhalb des Skripts über Konstanten definiert.

Das Skript kann entweder auf alle HTML-Dateien im spezifizierten Verzeichnis angewendet werden oder
auf eine einzelne,
spezifisch benannte HTML-Datei. Es nimmt einen optionalen Argumentparameter entgegen, der den Namen
der spezifischen
HTML-Datei (ohne .html-Endung) angibt, die bearbeitet werden soll. Bei Abwesenheit dieses Parameters
werden alle
HTML-Dateien im Verzeichnis bearbeitet.

Verwendung:
    python skriptname.py [--datei DATEINAME_OHNE_ENDUNG]

Beispiel:
    python skriptname.py --datei index

Sicherheitshinweise:
    Das Skript führt eine einfache Validierung des Dateinamens durch, um die Verwendung unsicherer
    Dateipfade zu verhindern.
    Es ist darauf zu achten, dass die Dateinamen und Pfade, mit denen das Skript arbeitet,
    vertrauenswürdig sind, da die
    Verwendung von 'open' mit schreibendem Zugriff potenziell manipulative Operationen auf dem
    Dateisystem ermöglicht.

Konstanten:
    VERZEICHNIS_PFAD: Der Pfad zum Verzeichnis, das die zu bearbeitenden HTML-Dateien enthält.
    SUCH_MUSTER_EPS/PDF: Reguläre Ausdrücke zum Finden der .eps/.pdf-Dateireferenzen in den
    HTML-Dateien.
    ERSETZ_MUSTER_EPS/PDF: Die Muster, durch die die gefundenen Referenzen ersetzt werden sollen.

Funktionen:
    ersetze_in_datei(html_pfad): Liest den Inhalt einer spezifischen HTML-Datei, ersetzt gefundene
    Muster und schreibt die Änderungen zurück.
    bearbeite_dateien(spezifische_datei): Wendet 'ersetze_in_datei' auf alle oder eine spezifische
    HTML-Datei an.
    main(): Einstiegspunkt des Skripts; verarbeitet Befehlszeilenargumente und ruft die
    Bearbeitungsfunktion auf.

