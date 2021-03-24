---
title: 3. Session
nav_order: 4
has_children: true
permalink: /3rd_session/
---

## 3. Session

**[Youtube Tutorial zu Session](https://youtu.be/XQ4nDt_m0Jw)**

### Grundlagen

#### Rekursion

Bei der [rekursiven Programmierung](https://de.wikipedia.org/wiki/Rekursive_Programmierung) ruft sich eine Prozedur, Funktion oder Methode in einem Computerprogramm selbst wieder auf. Es gibt viele Probleme, deren rekursive Formulierung besonders verständlich ist. Allerdings lässt sich, wer rekursiv programmiert, darauf ein, den genauen Ablauf der Ausführung schwer zu durchschauen. 

Ein Beispiel hierfür sind die **[Fibonacci-Zahlen](https://de.wikipedia.org/wiki/Fibonacci-Folge)**. 

<img src="fib.jpg" width=50%>

Durch die "Rekursionsanker" f<sub>0</sub> = 0, f<sub>1</sub> = 1 kann die Fibonacci-Folge auch rekursiv in einer Funktion berechnet werden:

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

Ruft eine Funktion sehr oft sich selbst auf, kann viel Speicherplatz verbraucht werden. Außerdem ist in Python eine maximale Rekursionstiefe (d.h. wie oft sich eine Funktion selbst aufrufen darf) eingestellt, die sich aber ändern lässt. Sie lässt sich auslesen mit `sys.getrecursionlimit()` und verändern mit `sys.setrecursionlimit()`.

Ein weiteres Beispiel ist die **[Drachenkurve](https://de.wikipedia.org/wiki/Drachenkurve)**

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Dragon_Curve_adding_corners_trails_rectangular_numbered_R.gif/300px-Dragon_Curve_adding_corners_trails_rectangular_numbered_R.gif">

[Quelle](https://commons.wikimedia.org/wiki/File:Dragon_Curve_adding_corners_trails_rectangular_numbered_R.gif)

Eine anschauliche Methode, diese Kurve zu erzeugen, ist folgende: 

Man nehme einen Papierstreifen und falte ihn in der Mitte, sodass sich seine Länge halbiert. Dies wiederhole man beliebig oft, dabei ist darauf zu achten, dass jedes Mal in dieselbe Richtung gefaltet wird. Zum Schluss falte man das Papier auseinander und ordne es so an, dass die Innenwinkel der Falze immer 90° betragen.

Diese Anleitung lässt sich ebenfalls rekursiv auffassen. Siehe dazu auch die Aufgabe in der Übung.

### Crashkurs

* *[funktionen.ipynb](./crashkurs/funktionen.ipynb)*
  * Definition
  * Doc-Strings
  * Namespaces
  * Keywords, Argumente
  
* *[numpy_matplotlib_anderes.ipynb](./crashkurs/numpy_matplotlib_anderes.ipynb)*
  * Numpy Array
  * Plots mit Matplotlib
  * Slicing
  * Lineare Algebra & Gleichungssysteme
  * Daten aus Tabelle lesen
  * Bilder bearbeiten
  * Schallbeispiele

* *[formatierung.ipynb](./crashkurs/formatierung.ipynb)*


### Ressourcen

* [numpy Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)