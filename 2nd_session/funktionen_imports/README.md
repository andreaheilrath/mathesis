---
title: Funktionen & Imports 
parent: 2. Session
nav_order: 3
permalink: /2nd_session/funktionen_imports/
---

## Vorweg etwas über Funktionen

Wie eine  **Funktion** in Python deklariert wird, sei an zwei Beispielen gezeigt.

```python
def funktionsname( .... ):    # durch Komma getrennte Argumente, u.U. auch kein Argument
        ..........
        ..........          # Block der Funktion
        ..........
        return ...          # Werte, die die Funktion zurückgibt, kann entfallen
```

```python
def flaeche(a, b):
    return a*b                  # diese Funktion gibt einen Wert zurück
```


## Imports

### Variante 1 (besser nicht benutzen)

Alle Funktionen eines Moduls direkt importieren:
```python
from math import *  # Alle Funktionen und Variablen des Moduls math werden direkt importiert
sin(pi)
```

Einzelne Funktionen eines Moduls importieren:
```python
from math import sin, cos
sin(pi)
```

### Variante 2

Grundsätzlich **sicherer** ist die folgende Form des Imports, da für das Modul ein eigener Namensraum geschaffen wird.
Alle Funktionen und Variablen aus dem Modul sind jetzt unter dem Präfix `math` erreichbar.

```python
import math
math.sin(math.pi)
```

### Variante 3

Die dritte Variante erlaubt, einen alternativen ('aka') 'Vornamen' zu verwenden:

```python
import math as m
m.sin(m.pi)
```

## Weitere wichtige Bibliotheken

### numpy

Für numerische Berechnungen werden wir häufig das Modul `numpy` (Numerical Python)  benutzen.


```python
import numpy as np
np.sin(np.pi / 2.0)
```

Damit ist es möglich, Matrizen, Vektoren, Tensoren als so genannte Arrays zu definieren:


```python
A = np.zeros((2,3)) # numpy macht aus Listen und Tupeln Matrizen!
B = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([1.0, 3.0, 5.0]) #man kann auch einen leeren Vektor einer gewissen "shape" erstellen
```

`A` ist dann eine $2\times 3$-Matrix, die Nullen (als Fließkommazahlen) enthält, `B` ist eine solche Matrix, die in der ersten Zeile $1,2,3$, sowie in der zweiten $4,5,6$ enthält. `v` ist ein Vektor, dessen 3 Einträge 1.0, 3.0 und 5.0 sind.

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

### Fortgeschrittenes Beispiel: Funktion zum Plotten einer Funktion

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
import matplotlib.pyplot as plt
from schallwerkzeuge import *

y = recordsnd(None, 2)
plt.plot(y)
plt.show()

playsnd(y, RATE)
playsnd(y, 2*RATE)
```
