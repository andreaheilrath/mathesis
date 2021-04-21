---
title: Funktionen & Imports 
parent: 2. Session
nav_order: 3
permalink: /2nd_session/funktionen_imports/
---

## Vorweg etwas über Funktionen

Da wir nun langsam in etwas komplexere Gefilde eintreten und gleich viele "fremde" Funktionen benutzen, hier vorab schon ein paar Hinweise zur Struktur von Funktionen.

Funktionen ermöglichen, Code, der mehrfach ausgeführt werden soll, auch an verschiedenen Stellen des Programms, übersichtlich zu verpacken.

Wie eine  **Funktion** in Python deklariert wird, sei an zwei Beispielen gezeigt.

    def funktionsname( .... ):    # durch Komma getrennte Argumente, u.U. auch kein Argument
        ..........
        ..........          # Block der Funktion
        ..........
        return ...          # Werte, die die Funktion zurückgibt, kann entfallen


```python
def flaeche(a, b):
    return a*b                  # diese Funktione gibt einen Wert zurücl

def ruehme(s):
    print(s + " sei gelobt!")    # diese Funktion "tut nur etwas"

def fluche():                 # diese Funktion hat kein Argument
    print("*x!####!")
```


```python
flaeche(2, 3)
```


```python
ruehme("Die Maus")
```


```python
fluche()
```

## Imports

Wir haben schon ein paar Module kennen gelernt, z.B. `turtle`, `math` und `random`. 

Bevor wir diese Module benutzen können, müssen wie sie **importieren**, bisher haben wir das so gemacht:

    import math
    import random

Python kommt mit einer großen Standardbibliothek, in der bereits viele nützliche Module enthalten sind. Darüber hinaus gibt es eine Community, die für die verschiedensten Gebiete weitere externe Module entwickelt und pflegt (Linguistik, Numerik, Astronomie, Spiele,...).

Für Imports gibt es **verschiedene Möglichkeiten**. Einige seien hier vorgestellt.

### Variante 1


```python
from math import *  # Alle Funktionen und Variablen des Moduls math werden direkt importiert
```

Dies ist die einfachste, aber manchmal gefährliche Methode.  Sie bedeutet, dass alle in dem Modul `math` definierten Namen von Variablen, Konstanten, Funktionen, Klassen nun direkt benutzt werden können (z.B. `sin, cos, exp, log, tan,...`). Sie sind jetzt im **Namensraum (name space)** des Programms.  Das heißt aber auch, dass eine vor dem Import definierte Variable durch den Import überschrieben werden kann.


```python
pi, e
```


```python
sin(pi)
```


```python
# Achtung, man kann die importierten Variablen und Funktionen überschreiben
pi = 3
```


```python
pi
```

Übersichtlicher wird diese Form des Imports, wenn nur bestimmte Objekte importiert werden:


```python
from math import sin, cos
```

importiert **nur die Funktionen `sin` und `cos`**.

### Variante 2

Grundsätzlich **sicherer** ist die folgende Form des Imports:


```python
import math
```

Danach sind alle Namen nur sozusagen über ihren 'Vornamen' `math` benutzbar, also etwa `math.sin, math.cos. math.exp, math.log,...`.


```python
math.pi
```


```python
math.cos(math.pi)
```

### Variante 3

Die dritte Variante erlaubt, einen alternativen ('aka') 'Vornamen' zu verwenden:


```python
import math as m
```

Danach sind alle Funktionen mit dem alternativen Vornamen erreichbar, also `m.sin, m.cos, m.exp`.

Korrekter als von Namen mit einem 'Vornamen' wäre  von Namen in einem  **Namensraum - oder name space** zu sprechen.


```python
m.cos(23)
```


```python
m.e
```

**Aufgabe:** Verwenden Sie die Funktionen des Moduls `math`, um herauszubekommen, wieviele Dezimalstellen 2\*\*10000 hat. (Zählen taugt nicht so gut, wie Sie sehen werden.)

## Weitere wichtige Bibliotheken

### numpy

Für numerische Berechnungen werden wir häufig das Modul `numpy` (Numerical Python)  benutzen.


```python
import numpy as np
np.__version__
```


```python
np.sin(np.pi / 2.0)
```

Damit ist es möglich, Matrizen, Vektoren, Tensoren als so genannte Arrays zu definieren:


```python
A = np.zeros((2,3)) # numpy macht aus Listen und Tupeln Matrizen!
B = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([1.0, 3.0, 5.0]) #man kann auch einen leeren Vektor einer gewissen "shape" erstellen
```

`A` ist dann eine $2\times 3$-Matrix, die Nullen (als Fließkommazahlen) enthält, `B` ist eine solche Matrix, die in der ersten Zeile $1,2,3$, sowie in der zweiten $4,5,6$ enthält. `v` ist ein Vektor, dessen 3 Einträge 1.0, 3.0 und 5.0 sind.


```python
A
```


```python
B
```


```python
v
```


```python
A.shape
```


```python
B.shape
```


```python
v.shape
```


```python
B.dot(v) # bezeichnet das Produkt aus B mit v
```

### matplotlib

`matplotlib` ist eine mächtige Biblothek zur grafischen Darstellung von Daten.


```python
import matplotlib.pyplot as plt

# Zunächst erstelle ich einige Listen, die gleich geplottet werden sollen.
x_werte = [0, 1, 2, 3, 4, 5]
y_werte1 = [0, 0, 2, 2, 4, 4]
y_werte2 = [3, 3, 1, 1, 0, 0]

plt.clf()
plt.scatter(x_werte,y_werte1) #erzeugt punkte
plt.plot(x_werte,y_werte1) #erzeugt verbindungslinien
plt.scatter(x_werte,y_werte2, marker = "x") #erzeugt kreuze
plt.plot(x_werte,y_werte2) #erzeugt verbindungslinien
plt.show()
```


```python
import math
import matplotlib.pyplot as plt

# %matplotlib inline #gibt ins Notebook integrierte Pixelgraphik
# %matplotlib notebook gibt ins Notebook integrierte Graphik mit Zoom-Möglichkeit
# %matplotlib qt gibt eigenes Fenster mit Zoom-Möglichkeit

listx = list(range(100))
listy = list(map(math.sin, listx))
plt.clf()
plt.plot(listx, listy)
plt.show()
```

### Fortgeschrittenes Beispiel: Funktion zum Plotten einer Funktion

Versuche den unten dargestellten Code zu verstehen und zu manipulieren.


```python
from matplotlib import pyplot as plt
import numpy as np


def plotfunction(f, x0, x1):
    x = np.linspace(x0, x1, 1000)
    y = f(x)
    plt.figure()
    plt.plot(x, y)
    plt.show()


plotfunction(np.sin, -10, 10)
plotfunction(np.cos, -10, 10)
plotfunction(np.arctan, -100, 100)
```

## Schall

Wer mit Daten von Tonaufnahmen umgehen will, könnte das interessant finden.

**Hinweis:** um das Modul `schallwerkzeuge` zu benutzen, muss das Modul `pyaudio` mit dem Befehl `conda install pyaudio` in der Konsole installiert werden!


```python
from schallwerkzeuge import *
```


```python
help(recordsnd)
```


```python
y = recordsnd(None, 2)
```


```python
y.shape
```


```python

```


```python
%matplotlib notebook
import matplotlib.pyplot as plt
```


```python
plt.plot(y)
plt.show()
```


```python
help(playsnd)
```


```python
playsnd(y, RATE)
```


```python
playsnd(y, 2*RATE)
```
