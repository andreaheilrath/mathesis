---
title: Funktionen & Imports 
parent: 2. Session
nav_order: 3
permalink: /2nd_session/funktionen_imports/
---
# Funktionen & Imports

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


Form des Imports | Abruf der Funktionen | guter Stil?
--- | --- | ---
`from math import * ` | `sin(pi)` | in speziellen Fällen
`from math import sin, cos` | `sin(pi)` | in speziellen Fällen
`import math` | `math.sin(math.pi)` | ja
`import math as m` | `m.sin(m.pi)` | ja



## Weitere wichtige Bibliotheken

### numpy

Für numerische Berechnungen werden wir häufig das Modul `numpy` (Numerical Python)  benutzen.


```python
import numpy as np
np.sin(np.pi / 2.0)
```

Damit ist es möglich, Matrizen, Vektoren, Tensoren als so genannte Arrays zu definieren:


```python
B = np.array([[1, 2, 3], [4, 5, 6]])
A = np.zeros((2,3))
v = np.array([1.0, 3.0, 5.0])
```

* `B` ist eine solche Matrix, die in der ersten Zeile $1,2,3$, sowie in der zweiten $4,5,6$ enthält.
* `A` ist eine $2\times 3$-Matrix, die Nullen (als Fließkommazahlen) enthält.
* `v` ist ein Vektor, dessen 3 Einträge 1.0, 3.0 und 5.0 sind.

### matplotlib

`matplotlib` ist eine mächtige Biblothek zur grafischen Darstellung von Daten.


```python
import matplotlib.pyplot as plt

# Zunächst erstelle ich einige Listen, die gleich geplottet werden sollen.
x_werte = [0, 1, 2, 3, 4, 5]
y_werte1 = [0, 0, 2, 2, 4, 4]
y_werte2 = [3, 3, 1, 1, 0, 0]

plt.scatter(x_werte,y_werte1) #erzeugt punkte
plt.plot(x_werte,y_werte1) #erzeugt verbindungslinien
plt.scatter(x_werte,y_werte2, marker = "x") #erzeugt kreuze
plt.plot(x_werte,y_werte2) #erzeugt verbindungslinien
plt.show()
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

<div class="iframe-container">
<iframe src="https://www.youtube.com/embed/WYTSQhVEpFw" allowfullscreen></iframe>
</div>
