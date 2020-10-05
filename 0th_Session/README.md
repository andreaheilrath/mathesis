## 0. Session

Diese Session dient dazu, euren Rechner vorzubereiten und zum ersten mal Python zu starten. Die wichtigsten Schritte findet ihr hier - im Video gibt es etwas mehr Hintergrundinfos.

### Inhalte

* Allgemeine Grundlagen: Algorithmen, Rechner, Programmiersprachen -> findet ihr [hier](grundlagen)

* Get started with Python
  * Installation von Python via Anaconda
  * Die Konsole - das Command Line Interface
  * Python interaktiv in der Konsole
  * Texteditoren und erste kleine Skripte
  * Jupyter Notebooks - Struktur und Bedienung
  * Error Messages

### Get started with Python

1. **Installation von Python via Anaconda** 

    Es gibt verschiedene Wege, Python zu installieren. Für den Crashkurs nutzt bitte [**Anaconda**](https://www.anaconda.com/products/individual). Unter dem Link findet ihr die    Installationsdateien für alle Betriebssysteme (üblich sind 64bit Systeme). Klickt euch einfach durch die Installation, es sind keine besonderen Einstellungen nötig.


2. **Die Konsole - das Command Line Interface**

    Alternativ zur gewohnten Interaktion mit dem Computer über die grafische Oberfläche (Fenster, Mauszeiger, Buttons, ...), kann man dem Rechner per Texteingabe kommunizieren.
    Das is möglich über die **Konsole**. Wenn ihr Windows benutzt, startet die **Anaconda Prompt**, unter Mac/Linux das **Terminal**. Am einfachsten ist es, wenn ihr nach diesen Programmen sucht.
    
    Wenn das Terminal läuft, wird euch ein Dateipfad angezeigt - das aktuelle Arbeitsverzeichnis. Normalerweise ist das zunächst euer Home-Folder (unter Mac/Linux auch mit `~` abgekürzt).
    ```
    C:\Users\username
    ```
    Wichtige Befehle in der Konsole:
    * `dir` (Windows) bzw `ls` (Mac/Linux) listet den **Inhalt des aktuellen Verzeichnisses** auf
    * `cd <Verzeichnisname>` (cd = change directory) **navigiert** in das genannte **Unterverzeichnis**
    * `cd ..` navigiert eine Ebene **nach oben**
    * Prozess beenden: `CTRL + C`
    
    Mehr Befehle und Infos über die Konsole findet ihr z. B. [hier](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955).

3. **Python interaktiv in der Konsole** 

    StartePython, indem du `python` in die Konsole eingibst und die Enter-Taste drückst. Jetzt sollten in der nächsten Zeile drei Häkchen auftauchen, so etwa: 
    ```     
    >>> 
    ```
    Jetzt läuft der **interaktive Python-Interpreter**. Werden nun Befehle eingegeben und mit `ENTER` abgeschickt, wird der Befehl von Python "interpretiert" und ausgeführt.
    Hier ein paar Beispiele:
    * `2 + 2`
    * `2 ** 8`
    * `print("Hello World")`
    * `x = 5`
    * `print(x)`
    
    Der Befehl `x = 5` erstellt eine neue Variable `x` die den Wert 5 hat. Von da an existiert `x` und der Wert kann abgerufen werden.
    
    Vorab ein Beispiel für den **Import eines Moduls: Turtle!**
    * `import turtle` Scheinbar passiert nichts, aber im Hintergrund werden Funktionen geladen.
    * `turtle.forward(50)` hier öffnet sich ein Fenster - lass es offen und beobachte den Effekt der nächsten Befehle.
    * `turtle.left(90)`
    * `turtle.backward(100)`
    
    **Hilfe:** `help(modul_name)` zeigt die Dokumentation des Moduls an. Für die Turtle wäre das `help(turtle)`.
    Die Taste `q` schließt die Dokumentation.
    
    **Beende Python** mit dem Befehl `exit()` oder der Tastenkombination `CRTL + d`.

5. **Texteditoren und erste kleine Skripte** 

    Anstatt einzelne Befehle in den Interpreter einzugeben, kann man eine Textdatei erstellen, in der Befehle zusammengefasst sind.
    Python Skripte haben üblicherweise die Dateiendung *.py*. Mit einem Texeditor lässt sich eine Python-Datei bearbeiten.
    
    Wenn du noch keinen Texteditor hast, empfehlen wir **[Atom](https://atom.io)**.
    
    Erstellt eine neue Datei (Datei -> neue Datei) mit dem Namen *hello.py*. Diese Datei soll zwei Zeilen haben:
    ```
    print("Hello World")
    wert = 2 ** 6
    ```
    Nachdem du die Datei bearbeitet und gespeichert hast, kannst du sie in der Konsole ausführen mit ```python hello.py```. **Achtung:** Das funktioniert nur, wenn du mit der Konsole in dem Verzeichnis bist, in dem sich *hello.py* befindet! Beim Ausführen von `dir`, bzw. `ls` sollte euch die Datei angezeigt werden. Führe die Datei auch im interaktiven Modus aus: `python -i hello.py`. Anschließent kannst du mit der Eingabe `wert` den Wert der Variable *wert* abrufen.

    Hier zwei simple Beispiele, was ein Skript so tun kann. Probier es mal aus!
    ```
    for zaehler in range(0,10):
      print(zaehler, "Hello World")
    ```
    ```
    import turtle
    for zaehler in range(0,38):
      turtle.forward(10)
      turtle.left(10)

    turtle.mainloop()
    ```

9. **Jupyter Notebook**

10. **Skripte in Atom ausführen.** Unter Datei -> Einstellungen -> Install kannst du das Paket *script* installieren. Mit der Tastenkombination `CRTL + SHIFT + B` wird der Code ausgeführt und es öffnet sich eine Konsole. Unter Linux und Mac sollte das einfach laufen. Unter Windows funktioniert es, wenn man Atom mit dem Befehl `atom` aus der Anaconda-Prompt startet, dann weiß Atom wo es Python "finden" kann. Alternativ kann man auch Pfadvariablen in der Registry hinzufügen, siehe **missing link**.

7. **Error Messages.** Wenn ihr anfangt, selbst Code zu verändern und zu produzieren, werdet ihr schnell auf Fehlermeldungen stoßen. Die Konsole gibt nicht das Ergebnis aus, sondern verschiedene Arten von Error Messages. Ihr bekommt auch die 

[16 Common Python Runtime Errors](https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find)

### Text

* [Chaos Computer Buch](https://monoskop.org/images/b/ba/Wieckmann,_Jürgen_%28ed.%29_-_Das_Chaos_Computer_Buch._Hacking_made_in_Germany_%28German%29.pdf), Seite 125, Die Drei Hände des Zeichners, Peter Glaser


### Andere Einführungen in Python

* https://www.kaggle.com/learn/python
* https://cscircles.cemc.uwaterloo.ca

### Referenzen & Tools

* https://runestone.academy/runestone/books/published/thinkcspy/index.html
* https://runestone.academy/runestone/books/published/thinkcspy/index.html
* http://www.pythontutor.com
