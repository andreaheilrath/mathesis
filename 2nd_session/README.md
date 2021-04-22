---
title: 2. Session
nav_order: 3
has_children: true
permalink: /2nd_session/
---

# 2. Session


Du lernst in dieser Einheit etwas über 

* Datenstrukturen: Tupel, Listen, Wörterbücher und Mengen
* Bedingungen: if, elif, else & while, Boolesche Variablen und Vergleiche
* Funktionen und Imports (numpy, matplotlib, schallwerkzeuge)


## Dateien zum Download

Alle Dateien die ihr braucht (Jupyter Notebooks, ein paar Bilder und Textdateien) sind in einer ZIP-Datei zusammengefasst.
Diese müsst ihr entpacken. Falls ihr nicht wisst, wie das geht, hier ein kleiner Guide.

2st_Session.zip


## Mathematische Grundlagen

### [Lineare Algebra](https://de.wikipedia.org/wiki/Lineare_Algebra)

...  (auch **Vektoralgebra**) ist ein Teilgebiet der Mathematik, das sich mit Vektorräumen und linearen Abbildungen zwischen diesen beschäftigt. Dies schließt insbesondere auch die Betrachtung von linearen Gleichungssystemen und Matrizen mit ein.

Vektoren und Matrizen sind mehrere Zahlen, die in ein Format zusammengefasst werden: (x, y, z) kann z. B. Koordinaten der drei Raumachsen bezeichnen.
Matrizen haben mehr als eine Dimension. Es gibt auch Operationen zwischen Matrizen und Vektoren - etwa die Multiplikation:

$$ \left( \begin{matrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{matrix} \right) * \begin{pmatrix} x \\ y \\ z \end{pmatrix} =  \begin{pmatrix}  1 x + 2 y + 3 z \\  4 x + 5 y + 6 z \\ 7 x + 8 y + 8 z \end{pmatrix}  $$

Wie man hier schon erkennen kann, lassen sich damit besonders gut lineare Gleichungssysteme beschreiben. Es gibt aber auch verschiedene andere Anwendungen für Lineare Algebra, z. B. die Transformation (Drehung, Stauchung, ...) von Koordinaten in Räumen.

## Begriffe aus der Informatik

### **Was ist eigentlich ein [Algorithmus](https://de.wikipedia.org/wiki/Algorithmus)?**

Es gibt verschiedene Definitionen für Algorithmen. Hier soll zunächst eine weniger "saubere", dafür zugängliche Version dargestellt werden. Im Allgemeinen können Algorithmen nicht nur von Computern ausgeführt werden, es muss sich nur um eine eindeutige Handlungsforschirft handeln, die folgende Eigenschaften besitzt:

1. **Eindeutigkeit**: ein Algorithmus darf keine widersprüchliche Beschreibung haben. Diese muss eindeutig sein.
2. **Ausführbarkeit**: jeder Einzelschritt muss ausführbar sein.
3. **Finitheit** (= Endlichkeit): die Beschreibung des Algorithmus muss endlich sein.
4. **Terminierung**: nach endlich vielen Schritten muss der Algorithmus enden und ein Ergebnis liefern.
5. **Determiniertheit**: der Algorithmus muss bei gleichen Voraussetzungen stets das gleiche Ergebnis liefern.
6. **Determinismus**: zu jedem Zeitpunkt der Ausführung besteht höchstens eine Möglichkeit der Fortsetzung. Der Folgeschritt ist also eindeutig bestimmt.


Die mathematisch korrekte Definition basiert auf dem Konzept der [Berechenbarkeit](https://de.wikipedia.org/wiki/Berechenbarkeit) und dem Modell der [Turingmaschine](https://de.wikipedia.org/wiki/Turingmaschine). Dazu später mehr.


Der Begriff [Laufzeit](https://de.wikipedia.org/wiki/Laufzeit_(Informatik)) beschreibt in der Informatik die Zeitdauer, die ein Programm zur Bewältigung einer Aufgabe benötigt.

Die absolute Laufzeit eines Programms ist von verschiedenen Faktoren, wie z. B. der Rechenleistung des Computers abhängig. Um verschiedene Algorithmen unabhängig von der ausführenden Maschine bezüglich ihrer Effizienz vergleichen zu können, wird die sogenannte *Asymptotische Laufzeit* angegeben. Um diese zu beschreiben, wird die [Landau-Notation](https://de.wikipedia.org/wiki/Landau-Symbole) verwendet.

[<img src="https://jarednielsen.com/static/9c24f10d0295ead7526e32d62fa2eac5/4117f/big-o-cheatsheet.png" width="50%" align="right" >](https://jarednielsen.com/big-o-logarithmic-time-complexity/)

Ein klassischer Fall, in dem die Laufzeit eine große Rolle spielt sind [Sortieralgorithmen](https://de.wikipedia.org/wiki/Sortierverfahren). Sortierung ist für viele andere Algorithmen relevant, aber auch für menschenlesbare Ausgabe großer Datenbanken. Hier ist wichtig, wie sich die Laufzeit mit zunehmender Anzahl zu sortierender Elemente verhält.

Der Algorithmus [Bubble Sort](https://de.wikipedia.org/wiki/Bubblesort) schneidet hier mit O(n<sup>2</sup>) schlechter ab als [Quicksort](https://de.wikipedia.org/wiki/Quicksort) mit O(n log(n)). Bei Bubble Sort verhält sich die Lautfzeit quadratisch zu der Anzahl Elemente - sollen also doppelt so viele Elemente sortiert werden, braucht der Algorithmus (im Mittel) vier mal so lange, Quicksort ist für viele Elemente bedeutend zeiteffizienter (siehe Grafik).

Hier findet ihr Videos zur Visualisierung verschiedener Sortieralgorithmen: [Plot](https://youtu.be/ZZuD6iUe3Pc) und [ungarischer Volkstanz](https://youtu.be/ywWBy6J5gz8)

Tatsächlich lässt sich im Allgeinen nicht vorhersagen, ob ein Algorithmus überhaupt zu einem Ende gelangt. Diese Fragestellung ist in der Informatik als [Halteproblem](https://de.wikipedia.org/wiki/Halteproblem) bekannt.

[Alan Turing](https://de.wikipedia.org/wiki/Alan_Turing) gelang der Beweis, dass es keinen Algorithmus gibt, der diese Frage für alle möglichen Algorithmen und beliebige Eingaben beantwortet. Wie viele theoretische Betrachtungen, wurde der Beweis anhand einer *abstrakten Maschine* vollzogen - die bekannteste ist die von Turing selbst entworfene
[Turingmaschine](https://de.wikipedia.org/wiki/Turingmaschine).

## Praktisches

* [Teletype für Atom](https://teletype.atom.io)
* [Anaconda Prompt Here](https://gist.github.com/jiewpeng/8ba446acf329b1801bf91db767d179ea)
* [Python for Data Science Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PythonForDataScience.pdf)
