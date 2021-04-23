---
title: for-Schleifen
parent: 2. Session
nav_order: 2
permalink: /2nd_session/for_loop/
---


# for - Schleifen

Häufig ist es nötig, mit allen Einträgen einer Liste oder eines Vektors eine Operation vorzunehmen. Dafür sind so genannte `for`-Schleifen geeignet. 

```python
l = [1, 2, 3, 4, 5]

for x in l:
    print(x**2)
```

Eine for-Schleife lässt sich über Listen, Tupel, Strings (als Ketten von Zeichen) und noch einige andere Datentypen durchführen. Der Idee nach taugt alles, was man durchzählen kann. 

### range( ) und typische for-Schleifen

Eine typische Form der for-Schleife zählt durch. Das lässt sich besonders einfach mit `range` bewerkstelligen.

```python
for index in range(4):
    print(index, "ter Durchlauf")
```

Verschachtelte for-Schleifen

```python
for i in range(3):
    print('__________________')
    print("Wert von i", i)
    for j in range(3):
        print("Wert von j", j)
```

### Praktische Beispiele

Im Folgenden wird mithilfe einer for-Schleife unter einer gewissen Bedingung ein Dictionary erstellt. Effektiv wird nun im Dicitonary angegeben, wie oft ein Wort in der Wortliste vorkommt. 


```python
alle_woerter = ["Katze", "Katze", "Hund",  "Katze",  "Katze",  "Maus",   "Hund",]

wb = {}
for wort in alle_woerter:
    if wort in wb:
        wb[wort] += 1
    else:
        wb[wort] = 1
        
print(wb)
```

### break, continue

Wie bei while-Schleifen  gibt es die Möglichkeit, mit `continue` direkt zum nächsten Schleifendurchlauf zu springen und mit `break` die Schleife zu beenden.


```python
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)
    if i % 17 == 0:
        break
```

### Nützliche Funktionen (= Generatoren ) für for-Schleifen (optional)

**enumerate**
```python
alle_kuchen = ['Apfelkuchen','Streuselkuchen', 'Pflaumenkuchen']

for i, kuchen in enumerate(alle_kuchen):
    print('%i. %s'%(i+1,kuchen))
```

**zip**
```python
alle_getraenke = ['Tee', 'Kaffee', 'Wasser']

for kuchen, getraenk in zip(alle_kuchen, alle_getraenke):
    print(kuchen, ' mit ', getraenk)
```

**Noch mehr davon: itertools**

In dem Paket der Standardbibliothek `itertools` gibt es noch mehr nützliche Generatoren.
[https://docs.python.org/3/library/itertools.html](https://docs.python.org/3/library/itertools.html)

```python
from itertools import product
for kuchen, getraenk in product(alle_kuchen,alle_getraenke):
    print(kuchen,'mit', getraenk)
```

### List comprehensions (optional)

Um aus Listen neue Listen zu definieren gibt es so genannte **list comprehensions**:
 
Abstrakt sieht die Syntax so aus:

    neue_liste=[funktion(element) for element in alte_liste if bedingung(element)]
    
Der Ausdruck ist strukturiert durch `for ... in  ... if`, dabei kann `if` entfallen. 

```python
l1 = [2, 3, 4, 5, 9, 100]
l2 = [a*a for a in l1 if a < 10]

print(l2)
```
