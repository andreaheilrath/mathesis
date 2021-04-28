---
title: Datenstrukturen
parent: 2. Session
nav_order: 1
permalink: /2nd_session/datenstrukturen/
---


# Datenstrukturen

In Python gibt es Datenstrukturen, die verschiedene einfachere Datentypen enthalten die ihr schon kennt (`int`,` float`, `string`, ...). 

Kürzel | Datentyp | Zuweisung | Aufruf | elementweise Zuweisung
--- | --- | --- | --- | ---
`tuple`| Tupel | `x = (1, 2, 3)` | `x[0]` | -
`list`| Liste | `x = [1, 2, 3]` | `x[0]` | `x[0] = 4`
`dict`| Wörterbuch | `x = {"key1": 1, 42 : 2, "key3": 3}` | `x["key1"]` | `x["key1"] = 4`
`set`| Menge | `x = {'a', 'b', 'c', 'd'}` | - | -


## mutable vs. immutable

Sogenannte *immutable* (unveränderbare) Objekte können nicht mehr verändert werden, nachdem sie einmal in eine Variable gespeichert wurden.
*Mutables* dagegen, können im Verlauf verschiedene Werte beinhalten.

immutable | mutable 
--- | --- 
`int`, `float`, `str`, `bool`, `tuple` | `list`,  `dict`, `set`

Vergleiche das Verhalten von Listen und Tupeln

```python
var_tuple = (1, 2, 3)
var_list = [1, 2, 3]

var_tuple[0] = 2   # fuehrt zu einem TypeError - tuple sind immutable!
var_list[0] = 2    # kein Problem, die Liste ist jetzt [2, 2, 3]
```

Vergleich von String-Methoden und Listen-Methoden

```python
s = s.replace('a', 'i') # Neuzuweisung des Strings in s
l.append(4)             # append verändert die Liste l direkt
```

## Mehr zu Listen

[Python List Methods](https://www.w3schools.com/python/python_ref_list.asp)

Operation | Effekt
--- | --- 
`l.append(x)`| einzelnes Element `x` an `l` anhängen
`l.extend(l2)`| Elemente der Liste `l2` einzeln an `l` anhängen
`l.insert(i, x)`| einzelnes Element `x` an Stelle `i` von `l` hinzufügen
`del l[i]` | Element von `l` an Stelle `i` löschen
`l2 = l1` | `l2` __ist__ `l1`
`l2 = copy(l1)` | erstellt eine Kopie von `l1` in `l2` auf oberster Ebene
 `l2 = deepcopy(l1)` | erstellt auch Kopien von verschachtelten Listen
 `sum(l)` | summiert `l` falls möglich
`list(map(f,l))` | wendet die Funktion `f` auf alle Einträge von `l` an.


### Listen aus Tupeln

```python
liste_aus_tupel = list(tupel)
```

### Listen aus Strings und andersrum

```python
s = 'Hund,Katze,Maus'
wortliste = s.split(',') # hier wir die Liste ['Hund', 'Katze', 'Maus'] erzeugt
','.join(wortliste)      # stellt den ursprünglichen String wieder her
```

### Zugehörigkeit

Die Zugehörigkeit zu einer Liste prüft man mit `in`:

```python
l = [1, 2, 3]
print(1 in l) # True
print(8 in l) # False
```

### Slicing

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l[2:7])  # [3, .., 7]
print(l[8:])   # [9, 10]
print(l[:-3])  # [8, 9, 10]
print(l[1::2]) # [2, 4, 6, 8, 10]
```


## Wörterbücher

**Wörterbücher** oder **Dictionaries** sind ein praktischer Datentyp, um irgendwelchen Daten (*keys*) irgendwelche
anderen Daten zuzuordnen (*values*). 

```python
wb = {} 
wb["house"] = "Haus"
wb["black"] = "schwarz"
wb["cat"] ="Katze"
```

```python
list(wb.keys())    # damit bekommt man eine Liste aller keys aus dem dictionary
"cat" in wb        # True, da "cat" ein Key des Wörterbuchs ist
"Katze" in wb      # False, da "Katze" KEIN Key des Wörterbuchs ist - "Katze" taucht nur als Value auf
```

## Mengen (Zusatz)

Python kennt außer Listen auch Mengen. Eine Menge kann man entweder durch die Auflistung der Elemente in Mengenklammern angeben oder, indem man die den Typ umwandelnde Funktion `set` auf eine Menge anwendet. Mengen sind nicht geordnet, jedes Element kommt nur einmal vor. Die üblichem Mengenoperationen (Vereinigung, Schnitt, Differenz) sind verfügbar.   

```python
set1 = {'a', 'b', 'c', 'd'}  #Initialisierung mit geschweiften Klammern - ohne ':' für Verknüpfung wie bei dicts
set2 = set(['a', 'b', 'e', 'e'])

print("difference", set1.difference(set2))            # print(set1-set2)  # alternative Kurzschreibweise
print("union", set1.union(set2))                      # print(set1 | set2)  # alternative Kurzschreibweise
print("intersection", print(set1.intersection(set2))  # print(set1 & set2)  # alternative Kurzschreibweise
```


<div class="iframe-container">
<iframe src="https://www.youtube.com/embed/u4TnSnRwrm8" allowfullscreen></iframe>
</div>
