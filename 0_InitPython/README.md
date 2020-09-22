## 0. Session

Diese Session dient dazu, euren Rechner vorzubereiten und zum ersten mal Python zu starten. Die wichtigsten Schritte findet ihr hier - im Video gibt es etwas mehr Hintergrundinfos.

### Inhalte

* Basics: Algorithmen, Computer, Programmiersprachen
* Installation von Python via Anaconda
* Die Konsole - erster Kontakt mit Python
* Texteditoren und erste kleine Skripte
* Jupyter Notebooks - Struktur und Bedienung

### Schritt-für-Schritt Anleitung

1. **Python 3 / Anaconda.** Es gibt verschiedene Wege, Python zu installieren. Einer der einfachsten ist die Installation über [Anaconda](https://www.anaconda.com/products/individual), unter dem Link findet ihr die Installationsdateien für euer Betriebssystem.

2. **Die Konsole.** Alternativ zur gewohnten Interaktion mit dem Computer über die grafische Oberfläche (Fenster, Mauszeiger, Buttons, ...), kann man dem Rechner per Text kommunizieren. Das is möglich über die Konsole. Wenn ihr Windows benutzt, startet die **Anaconda Prompt**, unter Mac/Linux einfach **Terminal** suchen. Um einen Befehl abzusenden, müsst ihr die Eingabetaste drücken. 
Die Konsole befindet sich immer in einem bestimmten Verzeichnis auf eurem Rechner. Die Eingabe `dir` (Windows) bzw `ls` (Mac/Linux) listet den Inhalt des Verzeichnisses auf. Mit `cd <Verzeichnisname>` (cd = change directory) kommt ihr in ein Unterverzeichnis mit  `cd ..` kommt ihr zurück.

3. **Python in der Konsole starten.** Starte den interaktiven Python-Interpreter, indem du `python` in die Konsole eingibst und die Enter-Taste drückst. Jetzt sollten in der nächsten Zeile drei Häkchen auftauchen, so etwa: 
```     
>>> 
```

4. **Erste Schritte.** Jetzt kannst du direkt Berechnungen durchführen wie `2 + 2` oder `2 ** 8`. Ein anderer grundlegender Befehl ist der print-Befehl: `print("Hello World")`.
Im Allgemeinen lassen sich die Funktionalitäten erweitern, indem man Module importiert - beispielsweise die Turtle: `import turtle`. Hier passiert scheinbar garnichts - allerdings könnt ihr jetzt Befehle aus dem Turtle-Modul ausführen, z. B. `turtle.forward(50)`, `turtle.left(90)`, `turtle.backward(100)`. Mit `help(modul_name)` kann man die Dokumentation der Module aufrufen (also `help(turtle)`), durch drücken der Taste `q` kommt ihr wieder zurück. Mit `exit()` oder der Tastenkombination `CRTL + d` beendet ihr Python.

5. **Python Skripte & Text Editor.** Für längere Programme ist es ungünstig, alle Schritt immer wieder eingeben zu müssen. Daher wollen wir jetzt eine Textdatei verfassen, in der die Befehle zusammengefasst sind. Es gibt viele Editoren, wenn du noch keinen auf deinem System installiert hast, empfehlen wir **[Atom](https://atom.io)**. Erstellt eine neue Datei (Datei -> neue Datei) mit dem Namen *HelloWorld.py*. Diese Datei soll zwei Zeilen haben:
```
print("Hello World")
wert = 2 ** 6
```


### Text

* [Chaos Computer Buch](https://monoskop.org/images/b/ba/Wieckmann,_Jürgen_%28ed.%29_-_Das_Chaos_Computer_Buch._Hacking_made_in_Germany_%28German%29.pdf), Seite 125, Die Drei Hände des Zeichners, Peter Glaser


### Andere Einführungen in Python

* https://www.kaggle.com/learn/python
* https://cscircles.cemc.uwaterloo.ca

### Referenzen & Tools

* https://runestone.academy/runestone/books/published/thinkcspy/index.html
* https://runestone.academy/runestone/books/published/thinkcspy/index.html
* http://www.pythontutor.com
