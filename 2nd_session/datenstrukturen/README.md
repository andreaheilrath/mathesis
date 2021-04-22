---
title: Datenstrukturen
parent: 2. Session
nav_order: 1
permalink: /2nd_session/datenstrukturen/
---


# Datenstrukturen

In Python gibt es Datenstrukturen, die verschiedene einfachere Datentypen enthalten die ihr schon kennt (`int`,` float`, `string`, ...). 

Kürzel | Datentyp | Beispiel
--- | --- | ---
`tuple`| Tupel | `x = (1, 2, 3)`
`list`| Liste | `x = [1, 2, 3]`
`dict`| Wörterbuch | `x['key'] = 1`
`set`| Menge | `x = {'a', 'b', 'c', 'd'}`

Bei **Tupel und Listen** kann man auf die einzelnen Einträge mit **Indizes** zugreifen und sie erlauben **Slicing**.
Der Abruf von Elementen bei **Dictionaries und Mengen** erfolgt über **Keys**.

## mutable vs. immutable

Sogenannte *immutable* (unveränderbare) Objekte können nicht mehr verändert werden, nachdem sie einmal in eine Variable gespeichert wurden.
*Mutables* dagegen, können im Verlauf verschiedene Werte beinhalten.

immutable | mutable 
--- | --- 
`int`, `float`, `str`, `bool`, `tuple`, | `list`,  `dict`, `set`


```python
var_tuple = (1, 2, 3)
var_list = [1, 2, 3]

print(var_tuple[0], var_list[0]) #ergibt beides die Ausgabe 1

var_tuple[0] = 2   # fuehrt zu einem TypeError - tuple sind immutable!
var_list[0] = 2    # kein Problem, die Liste ist jetzt [2, 2, 3]
```


## Funktionen von Listen

Listen lassen sich im Gegensatz zu Tupeln erweitern ... z.B. mit den Funktionen `.append` und `.extend`
```python
kohl.append('Romanesco')  #damit wir der Liste kohl das Element 'Romanesco' angehängt.
kohl
```

Die hinzugefügte Liste `l` ist jetzt **ein Element** der Liste `kohl`. 

Wollen wir nun auf ein Element der Liste `l` zugreifen, brauchen wir einen zweiten Index - einmal den Index der Stelle an der die Liste `l` steht und dann noch den Index der Liste `l` an dem z.B. der Integer 2 steht.


```python
kohl[4][1]
```

Wenn wir die einzelnen Elemente der Liste `l` an die Liste `kohl` anhängen möchten, benutzen wir die Funktion `.extend`


```python
kohl.extend(l)
kohl
```


```python
kohl[6] # der int 2 steht jetzt auch direkt in der Liste kohl
```


```python
#man kann auch Tupel in Listen umwandeln ...
liste_aus_tupel = list(tupel)
print(liste_aus_tupel)
```


```python
l = [] # man kann auch leere Listen erstellen. Das ist manchmal praktisch!
print(l)
```

### Hinweis 1: mutable vs immutable objects
Die Listen-Methoden wie `extend` und
`append` verändern eine gegebene Liste, sie liefern keinen Wert zurück.
Im Gegensatz dazu liefern die entsprechenden String-Methoden einen neuen
String.

Ein Listenobjekt ist veränderbar, **mutable**, während Tupel, Strings, Zahlen unveränderlich, **immutable** sind.
Der Wert einer Variablen, die auf ein  **immutable** Objekt weist, kann nur dadurch verändert werden, dass man sie **neu zuweist**.

Schaut euch die unten stehenden Beispiele gut an - dieser Unterschied ist eine häufige Fehlerquelle.


```python
s = 'Maus'
s.replace('a', 'i')
print(s)
```


```python
s = s.replace('a', 'i') #hier erfolgt eine Zuweisung!!
print(s)
```


```python
l = [1,2,3]
```


```python
l.append(4)  #hier erfolgt keine Zuweisung!!
print(l)
l = l.append(5)  # ACHTUNG! DAS TUT NICHT, WAS ES SOLL
#jede Funktion muss etwas zurückgeben - und wenn es keinen Inhalt haben soll - ist es None!
print(l)
```

### Hinweis 2: Listen "kopieren" ? 

Weisen wir eine Liste einer neuen Variable zu, so wird die Liste nicht kopiert, sondern die **neue Variable verweist auf die selbe Liste.** Die Liste hat jetzt sozusagen mehrere Namen.

Wir können also nun die Original-Liste auch unter dem neuen Namen ansprechen und verändern. Das kann gefährliche Nebenwirkungen haben, wenn man es nicht bedenkt.


```python
liste1 = [2, 3, 4]
liste2 = liste1
print(liste1)
print(liste2)
```


```python
liste2[1] = 7  #mit dieser Operation wird das Objekt verändert, das sowohl in Variable liste1 und liste2 steht
print(liste2)
print(liste1)
```

Wird eine **Kopie einer Liste** benötigt, die nichts mehr mit der ursprünglichen Liste zu tun hat, hilft das Modul `copy`. 

Dabei erzeugt die Funktion `copy.deepcopy`  ein volle Kopie, bei der auch in Listen verschachtelte Listen kopiert werden, während `copy.copy` nur die äußere Liste kopiert, aber eventuelle innere Listen dieselben bleiben.


```python
from copy import deepcopy
liste1 = [2, 3, 4]
liste2 = deepcopy(liste1)
liste2[1] = 7
print(liste2)
print(liste1)
```


```python
liste3 = deepcopy(liste1)
print(liste1 == liste3)
print(liste1 is liste3)
```

### Zugehörigkeit

Die Zugehörigkeit zu einer Liste prüft man mit `in`:


```python
print(kohl)
print("Wirsing" in kohl)
print("Kartoffel" in kohl)
print([1, 2] in kohl)
print([1, 2, 3] in kohl)
```

### Slicing

Wichtig sind noch Ausdrücke, die einen Teil einer Liste liefern. Ist `l` eine Liste, so liefert `l[a:e]` die Liste aller Einträge von `l` mit Index $i$, wobei $a\leq i<e$. Beachte die Zeichen $\leq$ und $<$! 

Lässt man $a$ oder $e$ weg, so fällt die enstprechende Bedingung weg, also liefert `l[:e]` alle Einträge von `l` mit Index kleiner e, sowie `l[a:]` alle Einträge von $l$ mit Index $\geq a$. 

Wollen Sie in einem solchen Indexbereich nur jedes $s.$ Zeichen, so schreiben Sie `l[a:e:s]`.


```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


```python
print(l[2:7])
print(l[8:])
print(l[:-3])
print(l[-5::-1])
print(l[::])
```


```python
l[1::2] = [0, 0, 0, 0, 0]  #hier findet eine Neuzuweisung statt!
```


```python
l
```

Da Listen der wohl wichtigste Datentyp in Python sind, hier eine Übersicht der Listen-Methoden (dabei sei `l` eine Liste). 

Darin bezeichnen die eckigen Klammern in den Argumenten der Funktionen ”optionale” Argumente, die man weglassen kann.

    l[i] = x                               Element i von l durch x ersetzen      
    l[i:j] = t                             "slice" von l von i bis j wird durch  t ersetzt     
    del l[i:j]                             dasselbe wie l[i:j] = []    
    l[i:j:k] = t                           die Elemente von l[i:j:k] werden durch die von t ersetzt     
    del l[i:j:k]                           entfernt die Elemente l[i:j:k] aus der Liste      
    l.append(x)                            dasselbe wie l[len(l):len(l)] = [x] 
    l.extend(x)                            dasselbe wie l[len(l):len(l)] = x 
    l.count(x)                             gibt die Anzahl der i‘s mit l[i] == x zurück    
    l.index(x[, i[, j]])                   gibt das kleinste k zurück mit l[k] == x und i <= k < j
    l.insert(i, x)                         dasselbe wie l[i:i] = [x]  
    l.pop(i)                               dasselbe wie x = l[i]; del l[i]; return x 
    l.pop()                                dasselbe wie pop(len(l)-1)
    l.remove(x )                           dasselbe wie del l[l.index(x)]   
    l.reverse()                            kehrt die Reihenfolge der Elemente von l um 
    l.sort([cmp[, key[, reverse]]])        sortiert die Elemente von l

Durch `sum(l)` erhält man die Summe der Elemente der Liste, wenn diese
definiert ist. Bei lauter Zahlen wäre das die gewöhnliche Summe, bei
Strings die Aneinanderkettung aller Strings.

Sehr nützlich ist es, zu wissen, wie man eine Funktion auf jedes Element
einer Liste anwenden kann: Wenn `f` eine Funktion ist und
`l=[a_0,a_1,..., a_n]` eine Liste von Objekten, für die diese
Funktion definiert ist, so liefert `list(map(f,l))` die Liste
`[f(a_0),f(a_1),...,f(a_n)]`.'

### Listen aus Strings

Eine Operation, die einen String in eine Liste von Strings umwandelt, soll noch erwähnt werden. Mit ihrer Hilfe bricht man
einen String an gewissen Trennzeichen in eine Liste von Strings auf.

Das ist ungemein nützlich zum Einlesen von Tabellen oder zum Zerlegen von Nutzereingaben.


```python
s = 'Hund,Katze,Maus'
s.split(',')
```


```python
s = 'Hund        Katze  Maus'
s.split()
```

Eine Umkehrung dieser Operation liefert `join`:


```python
l = ['Hund', 'Katze', 'Maus']
' und '.join(l)
```

## 3. Wörterbücher


**Wörterbücher** oder **Dictionaries** sind ein praktischer Datentyp, um irgendwelchen Daten (*keys*) irgendwelche
anderen Daten zuzuordnen (*values*). 

Ein Wörterbuch wird durch geschwungene Klammern gekennzeichnet und kann folgendermaßen angelegt:

    wb = {key1:value1, key2:value2, key3:value3} 
    wb = {}

Nun kann man durch `wb[key1]=value1` ein Paar `key1:value1` dem Wörterbuch hinzufügen, durch `wb[key2]=value2`
ein weiteres Paar `key2:value2`, etc. Durch `w[key1]` erhält man anschließend den Wert `value1`, etc. Ein Beispiel:


```python
wb = {} 
wb["house"] = "Haus"
wb["black"] = "schwarz"
wb["cat"] ="Katze"
```


```python
wb["cat"]
```


```python
list(wb.keys()) #damit bekommt man eine Liste aller keys aus dem dictionary
```


```python
wb["pi"] = 3.1415
wb[3] = ["drei","vier"]
wb[1.23] = [42]
print(wb)
```


```python
wb[3].append('Ratte')
print(wb)
```

Als **Keys** kommen Strings, ganze Zahlen, Bruchzahlen, Tupel von solchen und Objekte anderer grundlegender Datentypen in Frage (aber beispielsweise keine Listen.)

Ob ein gewisser **Key** im Wörterbuch vorkommt, lässt sich so abfragen:


```python
"cat" in wb # True, da "cat" ein Key des Wörterbuchs ist
```


```python
"Katze" in wb # False, da "Katze" KEIN Key des Wörterbuchs ist - "Katze" taucht nur als Value auf
```

## 4. Mengen (Zusatz)

Python kennt außer Listen auch Mengen. Eine Menge kann man entweder durch die Auflistung der Elemente in Mengenklammern angeben oder, indem man die den Typ umwandelnde Funktion `set` auf eine Menge anwendet.

Mengen sind nicht geordnet, jedes Element kommt nur einmal vor. Die üblichem Mengenoperationen (Vereinigung, Schnitt, Differenz) sind verfügbar.   

Wie bei Listen prüft man mit `in`, ob ein Objekt Element einer Menge ist. Mit $<=$, $>=$ prüft man, ob eine Menge Teilmenge, bzw. Obermenge ist, mit $<$, $>$, ob es sich um eine echte Teilmenge / Obermenge handelt.

Im Folgenden einige Beispiele zu den Operationen mit Mengen.


```python
set1 = {'a', 'b', 'c', 'd'}  #Initialisierung mit geschweiften Klammern - ohne ':' für Verknüpfung wie bei dicts
set2 = set(['a', 'b', 'e', 'e'])
print(set1)
print(set2)
```


```python
print("Difference ")
print(set1.difference(set2))
#print(set1-set2)  # alternative Kurzschreibweise
```


```python
print("Union")
print(set1.union(set2))
#print(set1 | set2)  # alternative Kurzschreibweise
```


```python
print("Intersection")
print(set1.intersection(set2))
#print(set1 & set2)  # alternative Kurzschreibweise
```


```python
print('a' in set1)
print(set1 < set2)
```


```python
print({'a', 'b'} < set1)
print((set1 > set1))
```


```python

```