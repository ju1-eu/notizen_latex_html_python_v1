# Verwendung von virtuellen Umgebungen

Für Python-Projekte wird die Verwendung von virtuellen Umgebungen empfohlen, um Abhängigkeiten projekt-spezifisch und isoliert vom globalen Python-Interpreter zu verwalten. Dies verhindert Konflikte zwischen Projektanforderungen und erleichtert die Reproduzierbarkeit des Projekts auf anderen Systemen. Das Python-Modul `venv` ist Teil der Python-Standardbibliothek (ab Python 3.3) und ermöglicht die Erstellung virtueller Umgebungen. Hier ist, wie du eine virtuelle Umgebung für dieses Projekt einrichten und verwenden kannst:

1. **Erstelle eine virtuelle Umgebung**:
   Öffne ein Terminal oder eine Kommandozeile und navigiere zum Wurzelverzeichnis dieses Projekts. Führe dann den folgenden Befehl aus:

   ```bash
   python3 -m venv mein_projekt_env
   ```

   Dieser Befehl erstellt einen neuen Ordner `mein_projekt_env` im aktuellen Verzeichnis, der die virtuelle Umgebung beherbergt.

2. **Aktiviere die virtuelle Umgebung**:
   Um die virtuelle Umgebung zu aktivieren, führe den entsprechenden Befehl für dein Betriebssystem aus:

   - **Linux oder macOS**:

     ```bash
     source mein_projekt_env/bin/activate
     ```

3. **Installiere die erforderlichen Abhängigkeiten**:
   Nachdem die virtuelle Umgebung aktiviert ist, kannst du die erforderlichen Abhängigkeiten installieren. Wenn eine `requirements.txt`-Datei vorhanden ist, führe folgenden Befehl aus:

   ```bash
   pip install -r requirements.txt
   ```

   Um eine neue `requirements.txt`-Datei basierend auf den aktuellen Abhängigkeiten der virtuellen Umgebung zu erstellen, verwende:

   ```bash
   pip freeze > requirements.txt
   ```

   Dieser Schritt ist besonders nützlich, wenn du neue Pakete installiert hast und sicherstellen möchtest, dass andere Entwickler oder Benutzer dieselben Versionen verwenden können.

4. **Version**

   ```bash
   cat requirements.txt
      # certifi==2024.2.2
      # charset-normalizer==3.3.2
      # idna==3.6
      # Jinja2==3.1.3
      # MarkupSafe==2.1.5
      # Pygments==2.17.2
      # python-dotenv==1.0.1
      # requests==2.31.0
      # setuptools==69.2.0
      # urllib3==2.2.1
      # wheel==0.43.0

   # Version
   python3 --version
   pip --version
      # Python 3.12.2
      # pip 24.0
   ```
