---
title: "Git-Info"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 5-2-24 Git-Info.md
pandoc Git-Info.md -o Git-Info.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Git-Info

## Konfliktauflösung und das Verständnis von Merge-Konflikten

### Erkennen von Merge-Konflikten

Ein Merge-Konflikt tritt auf, wenn Git nicht automatisch Änderungen aus verschiedenen Branches in derselben Datei zusammenführen kann. Dies geschieht häufig, wenn zwei Entwickler gleichzeitig Änderungen an denselben Zeilen einer Datei vornehmen oder wenn ein Entwickler eine Datei löscht, während ein anderer sie bearbeitet hat.

### Verstehen von Merge-Konflikten

Wenn ein Konflikt auftritt, kennzeichnet Git die betroffenen Bereiche in der Datei und unterbricht den Merge-Prozess. Der Konflikt muss manuell gelöst werden, bevor der Merge abgeschlossen werden kann.

In der Datei sehen Konflikte typischerweise so aus:

```plaintext
<<<<<<< HEAD
[Inhalt im aktuellen Branch]
=======
[Inhalt aus dem zu mergenden Branch]
>>>>>>> [Branch-Name]
```

- `<<<<<<< HEAD` markiert den Beginn des konfliktbehafteten Bereichs in Ihrem aktuellen Branch.
- `=======` trennt die unterschiedlichen Inhalte.
- `>>>>>>> [Branch-Name]` markiert das Ende des konfliktbehafteten Bereichs und zeigt den Namen des anderen Branches an.

### Auflösen von Merge-Konflikten

1. **Identifizieren Sie alle Konfliktbereiche** in der Datei. Suchen Sie nach den Markierungen `<<<<<<<`, `=======`, und `>>>>>>>`.

2. **Entscheiden Sie für jeden Konfliktbereich**, welchen Inhalt Sie behalten möchten:
    - Wählen Sie den Inhalt von einem der Branches.
    - Kombinieren Sie Inhalte aus beiden Branches.
    - Schreiben Sie einen neuen Inhalt, der beide Änderungen berücksichtigt.

3. **Bearbeiten Sie die Datei** und entfernen Sie die Markierungen (`<<<<<<<`, `=======`, `>>>>>>>`), sodass nur der gewünschte Inhalt übrig bleibt.

4. **Fügen Sie die gelösten Dateien zum Staging-Bereich hinzu**:
   ```bash
   git add [Dateiname]
   ```

5. **Schließen Sie den Merge-Vorgang ab**. Wenn alle Konflikte gelöst sind, führen Sie den Merge mit einem Commit ab:
   ```bash
   git commit
   ```
   Git öffnet einen Editor für den Commit-Message. Die vorgefertigte Nachricht enthält Informationen über den Merge und die gelösten Konflikte. Speichern Sie die Nachricht und schließen Sie den Editor.

6. **Testen Sie die Änderungen**. Stellen Sie sicher, dass Ihr Code nach der Konfliktlösung wie erwartet funktioniert.




## Unterschied push und fetch

### Git push

- **Zweck**: Der Befehl `git push` wird verwendet, um lokale Änderungen an einem Remote-Repository zu übermitteln. Wenn Sie Commits in Ihrem lokalen Repository gemacht haben, die noch nicht im Remote-Repository vorhanden sind, können Sie `git push` verwenden, um diese Änderungen hochzuladen und das Remote-Repository zu aktualisieren.
- **Richtung**: `push` sendet Daten vom lokalen Repository zum Remote-Repository.
- **Zugriffsrechte**: Um `push` ausführen zu können, benötigen Sie Schreibzugriff auf das Remote-Repository. Ohne die entsprechenden Berechtigungen wird der `push`-Versuch mit einer Fehlermeldung abgelehnt.
- **Anwendung**: `push` wird typischerweise verwendet, nachdem Sie lokale Commits gemacht haben und bereit sind, diese Änderungen mit anderen zu teilen oder ein zentrales Repository auf dem neuesten Stand zu halten.

### Git fetch

- **Zweck**: Der Befehl `git fetch` wird verwendet, um Informationen vom Remote-Repository zu holen, ohne diese automatisch mit Ihrem lokalen Arbeitsverzeichnis oder Ihren lokalen Branches zu mergen. `fetch` holt alle neuen Arbeit von dem angegebenen Remote-Repository, einschließlich neuer Branches und Tags sowie Änderungen in bestehenden Branches.
- **Richtung**: `fetch` holt Daten vom Remote-Repository zum lokalen Repository.
- **Zugriffsrechte**: Für `fetch` benötigen Sie lediglich Lesezugriff auf das Remote-Repository. Da es keine Änderungen am Remote-Repository vornimmt, sind die Zugriffsanforderungen weniger streng.
- **Anwendung**: `fetch` wird verwendet, um auf dem Laufenden zu bleiben mit dem, was im Remote-Repository passiert, ohne die eigenen lokalen Änderungen zu beeinflussen. Nach einem `fetch` können Sie entscheiden, ob und wie Sie die geholten Änderungen in Ihre Arbeit integrieren möchten, z.B. durch einen `merge` oder `rebase`.

**Zusammenfassung**

- `push` **sendet** Änderungen vom lokalen zum Remote-Repository, erfordert Schreibzugriff und wird verwendet, um Ihre Arbeit mit anderen zu teilen.
- `fetch` **holt** Änderungen vom Remote-Repository, erfordert nur Lesezugriff und beeinflusst Ihre lokale Arbeit nicht direkt. Es erlaubt Ihnen, die Änderungen zu sehen und zu entscheiden, wie Sie diese in Ihre Arbeit integrieren möchten.


## Unterschied Merge und rebase

### Git merge

- **Was es tut**: `merge` nimmt die Inhalte von zwei Branches und vereinigt sie in einem neuen "Merge-Commit". Wenn Sie einen `merge` durchführen, bleibt die gesamte Historie der Branches erhalten, und es wird ein neuer Commit erstellt, der zwei Eltern hat: einen für jeden Branch, der zusammengeführt wird.
- **Commit-Historie**: Die resultierende Commit-Historie ist eine nicht-lineare Historie, die die parallele Entwicklung der Branches zeigt. Das macht es leichter, die historischen Kontexte der Entwicklungspfade zu verstehen.
- **Verwendung**: `merge` wird oft in Teams verwendet, um Änderungen aus einem Feature-Branch in den Hauptbranch (z.B. `main` oder `master`) zu integrieren, da es die vollständige Historie und die Entscheidungen hinter den Änderungen bewahrt.

### Git rebase

- **Was es tut**: `rebase` nimmt die Commits von einem Branch und "reappliziert" sie auf einen anderen Branch. Dabei wird die Basis des Feature-Branches auf den aktuellen Endpunkt des Zielbranches verschoben. Dies kann dazu führen, dass die Commit-Historie geändert wird, da die Commit-IDs der rebasierten Commits neu erstellt werden.
- **Commit-Historie**: Die resultierende Commit-Historie ist linear, was eine saubere, gerade Entwicklungslinie ohne die Merge-Commits erzeugt, die man bei der Verwendung von `merge` sieht. Dies kann die Historie übersichtlicher und einfacher zu verstehen machen, insbesondere bei der Untersuchung von Projektverläufen.
- **Verwendung**: `rebase` wird häufig verwendet, um einen lokalen Branch auf den neuesten Stand zu bringen, indem man ihn auf die Spitze des Hauptbranches setzt, bevor man Änderungen zu einem Remote-Repository pushen oder einen Pull-Request erstellen will. Es wird auch verwendet, um eine saubere, lineare Historie zu erstellen, die leichter zu navigieren ist.

**Unterschiede zusammengefasst**

- **Historie**: `merge` bewahrt die tatsächliche Entwicklungsgeschichte und die Struktur der Branches, während `rebase` eine lineare Historie erstellt, indem es die Commits neu anordnet, als wären sie auf dem neuesten Stand des Zielbranches gemacht worden.
- **Konflikte**: Sowohl `merge` als auch `rebase` können Konflikte erzeugen, die manuell gelöst werden müssen. Bei einem `rebase` müssen diese Konflikte jedoch für jeden Commit einzeln gelöst werden, durch den der `rebase` durchgeführt wird, was in manchen Situationen mühsamer sein kann.
- **Sicherheit und Transparenz**: `merge` gilt als sicherer für die öffentliche oder geteilte Historie, da es die tatsächliche Entwicklungsgeschichte nicht verändert. `Rebase` ändert die Commit-Historie, was in geteilten Branches zu Problemen führen kann, wenn nicht sorgfältig gehandhabt.

**Empfehlungen**

- Verwenden Sie `merge`, wenn Sie die vollständige Historie und die Kontexte der Branch-Entwicklung bewahren möchten, insbesondere in geteilten Repositories.
- Verwenden Sie `rebase`, um eine saubere, lineare Historie für lokale Änderungen zu schaffen, bevor Sie diese teilen, oder wenn Sie die Übersichtlichkeit und Einfachheit einer linearen Commit-Historie bevorzugen.

