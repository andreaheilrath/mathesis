# for - Schleifen

Häufig ist es nötig, mit allen Einträgen einer Liste oder eines Vektors eine Operation vorzunehmen. Dafür sind so genannte `for`-Schleifen geeignet. 

Ist `liste` eine Liste, so führt

    for x in liste:
        ....
        ....
        ....

eine Schleife über alle Elemente `x` der Liste `liste` aus.

Ein Beispiel mit der Liste `kohl` vom letzten Notebook, zusammen mit der Ausgabe, die es hervorbringt:


```python
kohl = ['Weißkohl', 'Rotkohl', 'Wirsing']

for sorte in kohl:
    print(sorte + " ist wohlschmeckend und gesund")
```


```python
sorte
```


```python
del(sorte) #damit lässt sich die variable sorte löschen
```


```python
sorte
```

### Worüber kann man eine  for-Schleife durchführen ?

Über Listen, Tupel, Strings (als Ketten von Zeichen) und noch einige andere. Der Idee nach taugt alles, was man durchzählen kann. 

In Python ist das dadurch gegeben, dass das Objekt einen Zufgriff auf Elemente durch ihren Index (`[...]`) erlaubt oder einen **Iterator** zur Verfügung stellt. Dabei handelt es sich um ein Objekt, das jeweils das nächste Element in der Aufzählung liefert und weiß, wann es fertig ist.


```python
for a in (1, 2, 4, 8):  #hier wird "in place" ein Tupel definiert durch den dann iteriert wird
    print(2**a)
```


```python
#mit der for-Schleife lässt sich auch über die Zeichen in einem String iterieren.
l = []
for buchstabe in 'Maus':
    print(buchstabe)
    l.append(10*buchstabe) #hier wird 10*buchstabe an die Liste l angefügt
```


```python
l
```

### range( ) und typische for-Schleifen

Eine typische Form der for-Schleife zählt durch. Das lässt sich besonders einfach mit `range` bewerkstelligen.


```python
for index in range(4):
    print(index, "ter Durchlauf")
```

`range` ist ein Objekt in Python, das "auf Anfrage" Elemente zurückgibt.


```python
print(range(0,3))
print(list(range(0,3))) #erst durch die Umwandlung in eine Liste werden die expliziten Einträge erzeugt
```


```python
type(range(0,3)) #das range-Objekt hat einen eigenen Datentyp
```

Durch `list(range(a,b))`wird die Liste aller ganzen Zahlen $i$ mit $a\leq i <b$ erzeugt, also wird etwa durch `list(range(0,10))` die Liste `[0,1,2,3,4,5,6,7,8,9]` erzeugt. 

Für eine `for`-Schleife ist es jedoch nicht nötig `range` in eine Liste umzuwandeln. Hier noch einige Beispiele.


```python
for i in range(0, 3):
    print(i, i*i)
```


```python
for i in range(3):
    print('__________________')
    print("Wert von i", i)
    for j in range(3):
        print("Wert von j", j)
```


```python
for i in range(8,12):
    print (i)
```


```python
for i in range(17,12,-1):
    print(i)
```

Der große Vorteil von `range` im vergleich zu einer Liste, ist dass es weniger Speicher und insbesondere auch weniger Zeit benötigt!


```python
%timeit for i in range(0,100): pass
```


```python
%timeit for i in list(range(0,100)): pass
```

### Praktische Beispiele

Hier wird die for-Schleife mit einer if-Abfrage kombiniert.


```python
for x in [1, 2.323, 1+1j, 'Katze']:
    if isinstance(x, complex):
        print(x, "gehört zum Datentyp 'complex'")
    elif isinstance(x, int):
        print(x, "gehört zum Datentyp 'int'")
    else: print(x, "ist weder 'complex' noch 'int'")
```

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

Besonders nützlich sind eine Reihe von Generatoren, die aus anderen iterierbaren Objekten (Listen, Tupeln, Strings, Generatoren) neue machen.

####  1. enumerate

Der pythonische Stil von for-Schleifen hat viel für sich. Die for-Schleife iteriert etwa über den Elementen einer Liste, ohne dass man mit deren Indices herumrechnen müsste. Das ist lesbarer und weniger fehlerträchtig.

Was aber tun, wenn man zu dem Eintrag in einer Liste auch den Index braucht? Die einfachste Idee wäre, doch über den Indices `range(0,len(l))` zu iterieren und mit dem Index auf die Listenelemente zuzugreifen. Dann aber wird der Code wieder schwerer lesbar und weniger pythonisch. Dafür gibt es `enumerate`. 

`enumerate(l)` liefert beispielsweise für eine Liste `l` (oder ein anderes iterables Objekt) in jedem Durchlauf ein Tupel `(index, element)`, also etwas `(0,l[0])`, dann `(1,l[1])` etc.


```python
alle_kuchen = ['Apfelkuchen','Streuselkuchen', 'Pflaumenkuchen']

for kuchen in alle_kuchen:
    print(kuchen)
```


```python
for i, kuchen in enumerate(alle_kuchen):
    print('%i. %s'%(i+1,kuchen))
```

#### 2. zip

Eine andere häufige Situation besteht darin, mehrere Listen gleicher Länge zu haben. Ich möchte nun eine
Operation mit den ersten Elementen aller Listen, anschließend mit den zweiten, etc. Auch hier wäre eine einfache, aber eher unschöne Lösung, über die Indices zu iterieren und damit auf alle Listen zuzugreifen.

`zip(l1,l2,...)` liefert nun für zwei oder mehr Listen einen Generator, der beim ersten Mal das Tupel aller ersten Elemente, beim zweite Mal das Tupel aller zweiten Elemente etc. liefert. 


```python
alle_getraenke = ['Tee', 'Kaffee', 'Wasser']

for kuchen, getraenk in zip(alle_kuchen, alle_getraenke):
    print(kuchen, ' mit ', getraenk)
```

#### 3. Noch mehr davon: itertools

In dem Paket der Standardbibliothek `itertools` gibt es noch mehr nützliche Generatoren. 
Für Python 2 finden Sie die offizielle Dokumentation hier:

https://docs.python.org/2/library/itertools.html

Viele davon sind nützlich, nur eine soll an dieser Stelle vorgeführt werden: `product`. 

Er produziert einen Generator für das kartesische  Produkt zweier Mengen, also die Menge der Tupel, wobei das erste Element des Tupels aus der ersten Menge und das zweite aus der zweiten stammt.


```python
from itertools import product
```


```python
for kuchen, getraenk in product(alle_kuchen,alle_getraenke):
    print(kuchen,'mit', getraenk)
```

### List comprehensions (optional)

Um aus Listen neue Listen zu definieren gibt es so genannte **list
comprehensions**:
 
Abstrakt sieht die Syntax so aus:

    neue_liste=[funktion(element) for element in alte_liste if bedingung(element)]
    
Der Ausdruck ist strukturiert durch `for ... in  ... if`, dabei kann `if` entfallen. 


```python
l1 = [2, 3, 4, 5, 9, 100]

l2 = [a*a for a in l1 if a < 10]

print(l2)
```

Die neue Liste besteht also aus den Quadraten $a*a$ aller Listenelemente
$a$ von $l1$, die die Bedingung $a<10$ erfüllen.

... das könnte man auch so schreiben:


```python
l2 = []
for x in l1:
    if x < 10:
        l2.append(x**2)
print(l2)
```
