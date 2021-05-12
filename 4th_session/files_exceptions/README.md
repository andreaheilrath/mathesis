---
title: Dateien, Exceptions, Module
nav_order: 4
parent: 4. Session
permalink: /4th_session/files_exceptions/
---


# Hinweis zu Dateien, Exceptions und andere Module ...

Hier ein paar Code-Schnipsel, die vielleicht hilfreich sein werden ...

### Write to file

Häufig möchte man Ergebnisse einer Berechnung in einer Datei speichern. Das kann man z.B. mit `.write` machen:


```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("Another line.")
```

### Exceptions

Wenn ein Code einen Fehler ausgibt, bricht es ab.
Da es aber vorhersehbare Fehler gibt, kann man solche Error-Messages mit `try` ... `except` abfangen.


```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```


```python
filename = 'test.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
```

### Python Objekte speichern und Abrufen: Pickle


```python
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.p", "wb" ) )
```

```python
favorite_color = pickle.load( open( "save.p", "rb" ) )
print(favorite_color)
```

### Daten / Tabellen: Pandas


```python
import pandas as pd

dataframe = pd.read_csv("algebuei.csv", delimiter = ";")
print(dataframe)
```

### Andere nützliche Module

Referenz auf python.org: https://wiki.python.org/moin/UsefulModules

### Scientific Computing

* SciPy https://docs.scipy.org/doc/scipy/reference/
* Pandas https://pandas.pydata.org/docs/
* Numpy


### Image Processing

* PIL https://pillow.readthedocs.io/en/stable/
* OpenCV https://docs.opencv.org/4.5.0/

### Audio Processing

* Pyaudio http://people.csail.mit.edu/hubert/pyaudio/docs/
* sounddevice www.python-sounddevice.readthedocs.io

### WWW / Webscraping

* Requests https://requests.readthedocs.io/de/latest/
* Beautifulsoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### Spiele / Visualisierung

* Pygame
* VisPy

### Machine Learning

* Keras
* Pytorch
* Tensorflow

... und viele mehr!


# Zum Schluss: Guter Stil

Programme sollen nicht nur funktionieren, sondern lesbar sein. Dafür gibt es mit **[PEP8](https://www.python.org/dev/peps/pep-0008/) eine Guidline für alle Python-Programmier\*innen!**


```python
import this
```


```python

```
