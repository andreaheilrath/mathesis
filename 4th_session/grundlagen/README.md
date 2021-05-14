---
title: OOP Basics
nav_order: 1
parent: 4. Session
permalink: /4th_session/grundlagen/
---

# Objektorientierte Programmierung (OOP)

[Alan Kay](https://de.wikipedia.org/wiki/Alan_Kay), der Erfinder der Programmiersprache Smalltalk und des Begriffs „object oriented“, definierte das [objektorientierte Programmieren](https://de.wikipedia.org/wiki/Objektorientierte_Programmierung) folgendermaßen:

1. Everything is an object
2. Objects communicate by sending and receiving messages (in terms of objects)
3. Objects have their own memory (in terms of objects)
4. Every object is an instance of a class (which must be an object)
5. The class holds the shared behavior for its instances (in the form of objects in a program list)
6. To eval a program list, control is passed to the first object and the remainder is treated as its message


## Worum geht es hier?

Beim Objektorientierten Programmieren wird Code anders strukturiert als bei der Prozeduralen Programmierung, die wir bisher genutzt haben. Mit beiden Varianten lassen sich gleiche Ergebnisse erzielen, aber auf anderem Weg.

Jedes Objekt gehört dabei zu einer Klasse. Die Klasse ist eine Art "Blaupause" für alle Objekte die zu dieser Klasse gehören. Die einzelnen Objekte einer Klasse werden auch **Instanzen** genannt.

Instanzen einer Klasse unterscheiden sich in ihrem Zustand, nicht aber in ihrem Verhalten. Zustandsvariablen eines Objekts werden **Attribute** genannt. Funktionen (also das Verhalten) die zu einem Objekt gehören sind dessen **Methoden**.

Ein Beispiel für ein Objekt in Python sind die Numpy-Arrays.
```python
import numpy as np

a = np.array([0, 1, 2, 3])  # erstellt eine Instanz der Klasse Numpy
print(a.shape)              # Printet das Attribut shape
b = a.reshape(2,2)          # Aufruf der Methode reshape
print(b.shape)              # Printet das Attribut shape von b
```

Wir werden uns ein Beispiel ansehen, bei dem eine Klasse für Katzen erstellt wird. Jede Katze hat ähnliche Eigenschaften, die unabhängig von der indivituellen Katze sind. 

Unsere Klasse `Cat` hat die Methoden `play` und `meow` und die Attribute `mood`, `enegery`, `hunger`, `sounds`.

<img src="cat_class.png" style="width:100em">


## Grundkonzepte der OOP

* Verkapselung: Strukturen werden einen Container verpackt
* Abstraktion: Komplexe Vorgänge werden einfach dargestellt
* Vererbung: Klassen können auf anderen Klassen aufbauen
* Polymorphismus: Verschiedene Klassen können ähnliches Verhalten zeigen

Einige Beispiele und Konzepte sind aus diesem [FreeCodeCamp Post](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/) entnommen.

<div class="iframe-container">
<iframe src="https://www.youtube.com/embed/AyPDykrCFI8" allowfullscreen></iframe>
</div>
