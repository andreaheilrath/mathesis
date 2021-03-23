---
title: 2. Session
nav_order: 3
has_children: true
permalink: 2nd_Session
---

## 2. Session

**[Youtube Tutorial zu Session](https://youtu.be/DikSQol1gFE)**

### Grundlagen

#### [Lineare Algebra](https://de.wikipedia.org/wiki/Lineare_Algebra)

...  (auch **Vektoralgebra**) ist ein Teilgebiet der Mathematik, das sich mit Vektorräumen und linearen Abbildungen zwischen diesen beschäftigt. Dies schließt insbesondere auch die Betrachtung von linearen Gleichungssystemen und Matrizen mit ein.

Vektoren und Matrizen sind mehrere Zahlen, die in ein Format zusammengefasst werden: (x, y, z) kann z. B. Koordinaten der drei Raumachsen bezeichnen.
Matrizen haben mehr als eine Dimension. Es gibt auch Operationen zwischen Matrizen und Vektoren - etwa die Multiplikation:

    1 2 3       x       1*x + 2*y + 3*z
    4 5 6   *   y   =   4*x + 5*y + 6*z
    7 8 9       z       7*x + 8*y + 8*z
    
Wie man hier schon erkennen kann, lassen sich damit besonders gut lineare Gleichungssysteme beschreiben. Es gibt aber auch verschiedene andere Anwendungen für Lineare Algebra, z. B. die Transformation (Drehung, Stauchung, ...) von Koordinaten in Räumen.

#### Begriffe aus der Informatik

Der Begriff [Laufzeit](https://de.wikipedia.org/wiki/Laufzeit_(Informatik)) beschreibt in der Informatik die Zeitdauer, die ein Programm zur Bewältigung einer Aufgabe benötigt.

Die absolute Laufzeit eines Programms ist von verschiedenen Faktoren, wie z. B. der Rechenleistung des Computers abhängig. Um verschiedene Algorithmen unabhängig von der ausführenden Maschine bezüglich ihrer Effizienz vergleichen zu können, wird die sogenannte *Asymptotische Laufzeit* angegeben. Um diese zu beschreiben, wird die [Landau-Notation](https://de.wikipedia.org/wiki/Landau-Symbole) verwendet.

[<img src="https://jarednielsen.com/static/9c24f10d0295ead7526e32d62fa2eac5/4117f/big-o-cheatsheet.png" width="50%" align="right" >](https://jarednielsen.com/big-o-logarithmic-time-complexity/)

Ein klassischer Fall, in dem die Laufzeit eine große Rolle spielt sind [Sortieralgorithmen](https://de.wikipedia.org/wiki/Sortierverfahren). Sortierung ist für viele andere Algorithmen relevant, aber auch für menschenlesbare Ausgabe großer Datenbanken. Hier ist wichtig, wie sich die Laufzeit mit zunehmender Anzahl zu sortierender Elemente verhält.

Der Algorithmus [Bubble Sort](https://de.wikipedia.org/wiki/Bubblesort) schneidet hier mit O(n<sup>2</sup>) schlechter ab als [Quicksort](https://de.wikipedia.org/wiki/Quicksort) mit O(n log(n)). Bei Bubble Sort verhält sich die Lautfzeit quadratisch zu der Anzahl Elemente - sollen also doppelt so viele Elemente sortiert werden, braucht der Algorithmus (im Mittel) vier mal so lange, Quicksort ist für viele Elemente bedeutend zeiteffizienter (siehe Grafik).

Hier findet ihr Videos zur Visualisierung verschiedener Sortieralgorithmen: [Plot](https://youtu.be/ZZuD6iUe3Pc) und [ungarischer Volkstanz](https://youtu.be/ywWBy6J5gz8)

Tatsächlich lässt sich im Allgeinen nicht vorhersagen, ob ein Algorithmus überhaupt zu einem Ende gelangt. Diese Fragestellung ist in der Informatik als [Halteproblem](https://de.wikipedia.org/wiki/Halteproblem) bekannt.

[Alan Turing](https://de.wikipedia.org/wiki/Alan_Turing) gelang der Beweis, dass es keinen Algorithmus gibt, der diese Frage für alle möglichen Algorithmen und beliebige Eingaben beantwortet. Wie viele theoretische Betrachtungen, wurde der Beweis anhand einer *abstrakten Maschine* vollzogen - die bekannteste ist die von Turing selbst entworfene 
[Turingmaschine](https://de.wikipedia.org/wiki/Turingmaschine).


### Crashkurs

* [*datenstrukturen.ipynb*](./crashkurs/datenstrukturen.ipynb)

  * Tupel
  * Listen
  * Dictionaries
  * (Mengen)
  
* [*for_schleifen_iteratoren.ipynb*](./crashkurs/for_schleifen_iteratoren.ipynb)

  * for-Schleifen
  * range
  * Generatoren
  * List Comprehensions
  
* [*funktionen_imports_module.ipynb*](./crashkurs/funktionen_imports_module.ipynb)

  * Funktionen (intro)
  * Verschiedene Formen des Imports
  * numpy & matplotlib
  * schallwerkzeuge

### Praktisches

* [Teletype für Atom](https://teletype.atom.io)
* [Anaconda Prompt Here](https://gist.github.com/jiewpeng/8ba446acf329b1801bf91db767d179ea)
* [Python for Data Science Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PythonForDataScience.pdf)
