---
title: Numpy & Matplotlib
parent: 3. Session
nav_order: 2
permalink: /3rd_session/numpy_matplotlib/
---


# Numpy & Matplotlib

**Numpy** ist eine Bibliothek, die eine einfache Handhabung von Vektoren, Matrizen oder generell großen mehrdimensionalen Arrays ermöglicht. Neben den Datenstrukturen bietet NumPy auch effizient implementierte Funktionen für numerische Berechnungen an.

**Matplotlib** erlaubt es mathematische Darstellungen aller Art anzufertigen.

## Numpy

### Zentrale Datenstruktur: array

Ein **Array** ist eine Speicherstruktur, in der Zahlen (oder andere Objekte) in Abhängigkeit von einer gewissen Zahl von Indices gespeichert sind. Eine Matrix als rechteckige Anordnung von Zahlen ist der Spezialfall eines Arrays mit zwei Indices.

[<img src = "./array.png" width= 50%>](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)

In der [Dokumentation](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) findet ihr alle Attribute und Methoden, die ein Numpy Array hat.

```python
import numpy as np
v = np.array([1,2,3,4,5,6]) # Vektor mit 6 Einträgen
A = np.array([[1,2],[3,4]]) # 2x2 Matrix aus verschachtelten Listen
print(A)
```

```python
A.shape
A.ndim
A[0] #wir nur ein Index angegeben, wird eine komplette Zeile ausgewählt
A[0][1] # Um ein einzelnes Element zu erhalten müssen so viele Indizes wie Dimensionen angegeben werden - in diesem Fall 2
A[0,1] #ist äquivalent zur oberen Abfrage
```

### Erzeugen von Arrays

Es gibt verschiedene Möglichkeiten ein Array zu erzeugen. Die Funktion `np.array` macht aus einer oder mehreren Listen ein Array.

Weitere praktische Möglichkeiten sind die folgenden:


```python
shape = (3,3)  # der Tupel shape wird im Folgenden benutzt um Numpy-Arrays zu erzeugen, die 3x3 Matrizen entsprechen
np.zeros(shape) # erzeugt ein Array aus Nullen, dessen Shape durch das Tupel `shape` gegeben ist
np.ones(shape)  # erzeugt ein Array aus Einsen, dessen Shape durch das Tupel `shape` gegeben ist
np.zeros_like(A) # erzeugt ein Array aus Nullen mit der selben Shape wie A
np.ones_like(A)  # erzeugt ein Array aus Einsen mit der selben Shape wie A
```

Neben den Varianten zur Erzeugung von Arrays, die nur aus Nullen oder Einsen bestehen, gibt es folgende Funktionen, die ein "vorgefülltes" Array erstellen:


```python
np.arange(10)  #erzeugt das Array mit Elementen 0...9
np.linspace(0, 100, 11) # erzeugt ein Array mit 11 Elementen und gleichen Abständen, 0 ist anfang, 100 ist ende.
np.random.rand(*shape)  # erzeugt eine Matrix der gegeben Shape,
                        # die mit gleichverteilten Zufallszahlen zwischen [0,1] gefüllt ist
np.random.randn(*shape) # erzeugt eine Matrix der gegeben Shape,
                        # die mit Zufallszahlen aus der Gauß'schen Normalverteilung gefüllt ist
```

## Matplotlib (pyplot)


### klassische 2D Plots

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)   # in diesem Schritt wird die Sinusfunktion auf jedes einzelne Element des Arrays angewandt. 
                # Das geht zunächst nur mit 'universal functions' - eigene erstellt man mit numpy.vectorize
plt.figure()
plt.plot(x, y)
plt.show()
```

Bei den meisten graphischen "Backends" erscheint die Graphik erst beim Aufruf von `plt.show()` Vorher existiert sie nur als Datenstruktur.

In Jupyter-Notebooks entfällt `show()` meistens, da es automatisch aufgerufen wird.
Für eine interaktive Umgebung zur Datenanalyse (und zum Ausprobieren) ist das sinnvoll.


```python
x = np.linspace(0, 10, 100)
y = np.random.rand(100)  # das geht schief - die Arrays müssen immer gleich lang sein!
                        # Sonst ValueError("x and y must be the same size")
plt.figure()
plt.scatter(x, y, marker ="x", color = "black", label = "zufällige Datenpunkte")
plt.legend()
plt.show()
```

### Matrizen als Bilder darstellen

Eine 2D Matrix kann als Bild interpretiert werden. Die farbliche Darstellung kann über
[Colormaps](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html) definiert werden.

Hier wird eine Matrix aus Zufallszahlen erstellt und mit `plt.imshow()` visualisiert:


```python
M = np.random.rand(24,24)

plt.figure()
plt.imshow(M, cmap=plt.get_cmap('viridis'))
plt.show()
```

### Zugriff auf Teile des Arrays: slicing

Wie bei Listen und Strings ist Slicing eine wichtige Operation, die hier noch flexibler ist, denn man kann auch mit einem Tupel `(t1,t2,...,tk)` für die entsprechende Dimension gerade die Einträge mit den Indices t1,...,tk auswählen.

```python
M = np.zeros((24,24))
M[0] = 1
M[0,0] = 0.5
M[4] = 1

M[:,1] = 1
M[2,0::2] = 1
M[10:15, 10:15] = 0.5

plt.figure()
plt.imshow(M, cmap=plt.get_cmap('viridis'))
plt.show()
```

### Aus Arrays neue Arrays machen     

Zwei Funktionen, mit denen aus bereits bestehenden Arrays neue gemacht werden können, sind `concatenate` und `reshape`.

`concatenate` fügt zwei Arrays hintereinander an

`reshape` transferiert die Einträge eines Arrays in eine neues Array mit anderer Shape


```python
v = np.arange(20)
v2 = np.concatenate((v, v))  # Aneinanderhängen zweier Vektoren
print(v2)
print(v2.shape)
```


```python
w = v.reshape((2, 10))  # beachtet: die neue Matrix wird zeilenweise befüllt
w
```

## Lineare Algebra

[Matrizenmultiplikation](https://de.wikipedia.org/wiki/Matrizenmultiplikation) ist die zentrale algebraische Operation für Matrizen.

Hier zwei Beispiele für die Multiplikation einer Matrix mit einem Vektor, die wiederum einen Vektor liefert und der Multiplikation zweier Vektoren, welche ein Skalar ergibt.

<img src="Matrixmult.jpg" width=80%>

In `numpy` wird diese Operation mit `np.dot(M,x)` bzw. `M.dot(x)` durchgeführt.


```python
M = np.array([[1, 2], [3, 4]])
x = np.array([2,3])
np.dot(M, x) # Matrix-Vektor-Produkt
M.dot(x)  # alternative Schreibweise
M@x # alternative Schreibweise
x.dot(x) # Skalarprodukt mit sich selbst
x@x   # alternative Schreibweise
```

**Transponieren** (Vertauschen von Zeilen und Spalten) geht nicht über eine Funktion, sondern über ein Attribut.

**Achtung!** Dieses legt kein neues Objekt im Speicher an, sondern nur eine anderen 'View' auf dasselbe Objekt. Wenn man also das Transponierte verändert, verändert sich das ursprüngliche Objekt auch. Alternativ mussen explizit mit `np.copy` eine Kopie angelegt werden.


```python
M.T  # transponieren
# M und M.T beziehen sich auf dasselbe Objekt im Speicher:
N = M.T
N[0,0] = 5  # verändert M und N
print(N)
print(M)
```

```python
# Diesmal wird M.T kopiert: N bezieht sich auf ein anderes Objekt im Speicher.
N = np.copy(M.T)
N[0, 0] = 6   # verändert nur N
print(N)
print(M)
```

Für weitergehende Operationen der linearen Algebra gibt es ein Unterpaket: `numpy.linalg`.
Eine Funktion, die sehr wichtig ist, ist  `numpy.linalg.solve`. Sie löst ein lineares Gleichungssystem mit einer schnellen, in C programmierten Variante des Gauß'schen Algorithmus.

**An dieser Stelle noch ein paar Hinweise zu Linearen Gleichungssystemen**
<img src="LinearesGleichungssystem.jpg" width=85%>


```python
M = np.array([[3, 2, 1], [4, -5, 18], [-7, 8, -2]])
y = np.array([7, 12, 42])

print(M, y)
```


```python
x = np.linalg.solve(M, y)
print(x)
```


```python
# Probieren wir mal, wie lange ein 10000x10000-Gleichungssystem dauert
v = np.random.rand(10000)
```


```python
v[:100]
```


```python
A = np.random.rand(10000, 10000)
```


```python
A.shape
```


```python
v.shape
```


```python
%time np.linalg.solve(A, v)  #das dauert eine Weile ...
```

###  Kumulierende Funktionen

     numpy.sum(..., [axis=...])     summiert die Einträge, gegebenenfalls längs axis
     numpy.mean(..., [axis=...])    Mittelwert über die Einträge, ggf. längs axis
     numpy.std(..., [axis=...])     Standardabweichung ü.d. Einträge, ggf. längs axis

Dabei ist axis entweder eine Zahl oder ein Tupel, wenn über mehre Dimension summiert werden soll. Es gibt noch viel mehr solcher Funktionen, aber hier wird keine Vollständigkeit angestrebt.



```python
np.sum(A, axis=1)
```


```python
np.sum(A, axis=0)
```


```python
np.mean(A)
```


```python
np.mean(A, axis=1)
```

### Daten aus Tabelle lesen und darstellen

Da numpy unter anderem zur Datenverarbeitung gut ist, gibt es auch Funktionen, die beim Lesen von Daten helfen, etwa aus einer 'komma-separierten Liste' csv.

     np.genfromtxt(dateiname, [delimiter=...,[skip_header=...])


```python
%ls *.csv
```


```python
daten = np.genfromtxt("algebuei.csv", delimiter=";", skip_header=True)
```


```python
daten
```


```python
np.mean(daten, axis=0)
```


```python
plt.figure()
plt.hist(daten[:, 3], bins=50)
```


```python
plt.show() #das braucht ihr in einem "normalen" Python-Skript um den Plot anzuzeigen
```


```python
daten.shape
```

### 3D Plots

Man kann mit Matplotlib auch 3D Plots erstellen ...


```python
%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx*xx+yy*yy)
ax.plot_surface(xx, yy, z)
plt.show()
```

### Bilder einlesen


```python
import imageio
```


```python
bild = imageio.imread('images/IMGP2821.JPG', pilmode='F')
# tragen Sie doch hier den Namen eines Bildes ein, das sich im
# Verzeichnis befindet.
```


```python
bild.shape
```


```python
plt.figure()
plt.imshow(bild)
```


```python
plt.figure()
plt.imshow(bild, cmap=plt.get_cmap('gray'))
```


```python
a = np.abs(bild[10:, :]-bild[:-10])
# Was koennte diese Rechnung bewirken?
```


```python
plt.figure()
plt.imshow(a, cmap=plt.get_cmap('gray'))
```
