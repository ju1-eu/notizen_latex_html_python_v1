# TODO

pylint

- dokumentation.py 9,03/10
- latex_convert1.py **fehler**
- git_hilfsprogramm.py 7.75/10
- latexcode_entfernen2.py 7.72/10
- html_dateien_verarbeiten2.py **fehler**
- navigationsseite_html.py **fehler**
- html_entfernen2.py 8.29/10
- scriptauswahl.py 9.85/10
- html_konverter_pandoc1.py 9.57/10
- suchen_ersetzen.py **fehler**
- html_konverter_py_markdown1.py 8.65/10
- sync_tex.py 8.57/10
- image_resizer.py 9.39/10

```
# pylint image_resizer.py
# 9.39/10
image_resizer.py:77:0: C0301: Line too long (117/100) (line-too-long)
image_resizer.py:124:8: W0707: Consider explicitly re-raising using 'raise RuntimeError(f'Fehler bei der PDF-Kompression: {error}') from error' (raise-missing-from)
image_resizer.py:127:0: R0913: Too many arguments (8/5) (too-many-arguments)

# pylint sync_tex.py
# 8.57/10
sync_tex.py:53:0: C0301: Line too long (101/100) (line-too-long)
sync_tex.py:33:11: W0718: Catching too general exception Exception (broad-exception-caught)
sync_tex.py:33:4: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)
sync_tex.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)

# pylint suchen_ersetzen.py
#
suchen_ersetzen.py:99:23: E0001: Parsing failed: 'unterminated string literal (detected at line 99) (<unknown>, line 99)' (syntax-error)

# pylint html_konverter_py_markdown1.py
# 8.65/10
html_konverter_py_markdown1.py:60:53: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
html_konverter_py_markdown1.py:67:46: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
html_konverter_py_markdown1.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)
html_konverter_py_markdown1.py:93:15: W0718: Catching too general exception Exception (broad-exception-caught)
html_konverter_py_markdown1.py:93:8: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)

# pylint html_konverter_pandoc1.py
# 9.57/10
html_konverter_pandoc1.py:88:11: W0718: Catching too general exception Exception (broad-exception-caught)
html_konverter_pandoc1.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)

# pylint scriptauswahl.py
# 9.85/10
scriptauswahl.py:66:11: W0718: Catching too general exception Exception (broad-exception-caught)

# pylint html_entfernen2.py
# 8.29/10
html_entfernen2.py:85:0: C0301: Line too long (160/100) (line-too-long)
html_entfernen2.py:97:0: C0301: Line too long (124/100) (line-too-long)
html_entfernen2.py:102:0: C0301: Line too long (101/100) (line-too-long)
html_entfernen2.py:68:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
html_entfernen2.py:75:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
html_entfernen2.py:77:4: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)

# pylint navigationsseite_html.py
#
navigationsseite_html.py:74:11: E0001: Parsing failed: 'unterminated string literal (detected at line 74) (<unknown>, line 74)' (syntax-error)

# pylint html_dateien_verarbeiten2.py
#
html_dateien_verarbeiten2.py:62:23: E0001: Parsing failed: 'unterminated string literal (detected at line 62) (<unknown>, line 62)' (syntax-error)

# pylint latexcode_entfernen2.py
# 7.72/10
latexcode_entfernen2.py:116:0: C0301: Line too long (158/100) (line-too-long)
latexcode_entfernen2.py:128:0: C0301: Line too long (122/100) (line-too-long)
latexcode_entfernen2.py:131:0: C0301: Line too long (113/100) (line-too-long)
latexcode_entfernen2.py:133:0: C0301: Line too long (101/100) (line-too-long)
latexcode_entfernen2.py:66:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
latexcode_entfernen2.py:73:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
latexcode_entfernen2.py:75:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
latexcode_entfernen2.py:77:4: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)
latexcode_entfernen2.py:85:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
latexcode_entfernen2.py:94:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
latexcode_entfernen2.py:96:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
latexcode_entfernen2.py:99:4: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)
latexcode_entfernen2.py:109:8: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)

# pylint latex_convert1.py
#
latex_convert1.py:92:15: E0001: Parsing failed: 'unterminated string literal (detected at line 92) (<unknown>, line 92)' (syntax-error)
```

