---
title: Funktionen
parent: 3. Session
nav_order: 1
permalink: /3rd_session/funktionen
---


# Funktionen

## Grundlagen

In Python kann man selbst Funktionen definieren. Das geht so:

```python
def funktionsname(arg1, arg2 = 2):
    '''Doc-String: wird angezeigt, wenn die Hilfe
    help(funktionsname) aufgerufen wird.
    '''
    print('Die Funktion "funktionsname" wird ausgefuehrt')
    return arg1 * arg2
```

Mit `return ...` wird die Größe definiert, die anschließend als Wert der Funktion zurückgegeben wird. Wird kein Rückgabewert bei `return`definiert wird der Wert `None` zurückgegeben.

Argumente, die der Funktion übergeben werden, können einen Defaultwert haben, wie das bei `arg2` der Fall ist.

So wird die Funktion aufgerufen:
```python
funktionsname(2)
funktionsname(2, 4)
funktionsname(2, arg2 = 4)
```

## Argumente

Werte die einer Funktion übergeben werden stehen in den runden Klammern nach dem Funktionsnamen.

Wird den Argumenten kein Default-Wert zugewiesen, erfolgt die Übergabe durch die Position der Argumente (positional arguments)

```python
def pos_arg_fkt(arg1, arg2):
    return arg1 * arg2

pos_arg_fkt(1, 2) # hier wird arg1 = 1 und arg2 = 2
pos_arg_fkt(1, arg2=2) # ist auch erlaubt

pos_arg_fkt(arg1=1, 2) # syntax error!!
```
Man darf bei dieser Funktion auch Keywords benutzen, wichtig ist allerdings, dass niemals ein
Positions-Argument nach einem Keyword-Argument kommt!

Das gilt auch für Funktionen mit Keyword-Argumenten (also Default-Werten:

```python
def key_arg_fkt(arg1 = 1, arg2 = 2):
    return arg1 * arg2

key_arg_fkt() # hier wird arg1 = 1 und arg2 = 2
key_arg_fkt(arg2=4) # ist auch erlaubt

key_arg_fkt(arg1=2, 4) # syntax error!!
```

Man kann beide Arten auch mischen:

```python
def mixed_arg_fkt(arg1, arg2 = 2):
    return arg1 * arg2

mixed_arg_fkt(1) # hier wird arg1 = 1 und arg2 = 2
mixed_arg_fkt(1, 2) # ist auch erlaubt

mixed_arg_fkt(arg2=4) # error: missing 1 required positional argument
mixed_arg_fkt(arg1=2, 4) # syntax error!!
```

## Lokale und globale Variablen

Gewisse Funktionen in Python sollen immer verfügbar sein, z.B. `id()` oder `type()`. Diese Funktionen sind im *built-in namespace* zu finden. Variablen die innerhalb des "Hauptkörpers" des Programms definiert werden gehören zum *global namespace*. Alle Variablen, die in einer Funktion verändert oder zugewiesen werden, sind Teil des *local namespace*.

```python
konstante = 42  #Variable "konstante" im global namespace

def f(x):
    konstante = 1 #Variable "konstante" im local namespace
    y = konstante*x
    return y
```

Das Ergebnis von `f(1)` ist `1`, da die der Wert der lokalen `konstante` eins ist. Dabei wir die Variable `konstante` die vor der Funktionsdefinition steht nie verändert!


Im Folgenden Beispiel wird die Variable aus dem globalen Namenstraum innerhalb der Funktion benutzt.

```python
konstante = 42

def f(x):
    global konstante
    y = x*konstante
    konstante =1
    return y

f(1)
```

<img src="./namespaces.jpg" alt="Namespaces" style="width: 60%;">
<img src="./namespaces.jpg" width = "640em">

### Achtung: mutable und immutable

Wenn einer Funktion Argumente übergeben werden, so muss darauf geachtet werden, ob die Argumente mutable oder immutable sind.

`funktion1` verändert die ihr übergebene Liste, `funktion2` tut das ebenfalls und gibt ein ganz anderes Objekt zurück. `funktion3` verändert die übergebene Liste nicht und gibt eine neue, abgeänderte Liste zurück.

```python
from copy import copy

def funktion1(x):
    '''erwartet eine Liste'''
    x.append(4)
    print("f1 durchgefuehrt")

def funktion2(x):
    '''erwartet eine Liste'''
    x[1] = 'Huhn'
    x = 3.33  # ab hier verliert 'x' die Verbindung
    # zum übergebenen Objekt x
    print("f2 durchgefuehrt")
    return x

def funktion3(x):
    '''erwartet eine Liste'''
    y = copy(x)
    y.append('asdf')
    print("f3 durchgefuehrt")
```



## Noch mehr zur Übergabe von Argumenten...

### Obligatorische Schlüsselwortargumente ohne Default-Wert

Bei den oben skizzierten Varianten der Übergabe von Argumenteen wurden diese entweder *ohne Default-Wert* nach ihrer Position übergeben oder *mit Default-Werten* über Schlüsselwörter. Es könnte aber wünschenswert sein, Argumente ohne Default-Wert über Schlüsselwörter zu übergeben.

Argumente ohne Default-Wert müssen tatsächlich übergeben werden, man kann sie nicht weglassen. In Python 3 geht das so:

    def f(a,*,b,c=3):
       print("a: ",a)
       print("b: ",b)
       print("c: ",c)

**Alle Argumente nach dem \* müssen über ihr Schlüsselwort** übergeben werden. Dabei kann man die Argumente mit Default-Wert (hier c) weglassen, b aber kann man nicht weglassen. Also z. B.


```python
# Achtung! Nur Python 3

def integral(f, *, a, b, n=1000):
    '''Approximiert das Integral über f von a bis b nach der Trapezregel
    mit n Unterteilungen'''
    x = np.linspace(a, b, n+1)
    return (-0.5*f(a)-0.5*f(b)+np.sum(f(x)))*(b-a)/n
```


```python
integral(np.exp, a=1, b=2, n=1000)  # geht
```


```python
integral(np.exp, a=1, b=2) # geht auch
```


```python
integral(np.cos, 1, 2, 1000)  # Fehler
```


### Argumente ein- und auspacken (optional)

#### Durch  Position bestimmte Argumente: Listen und Tupel übergeben

Eine beliebige Zahl von durch ihre Position bestimmten Argumenten kann verpackt werden in ein Tupel (oder eine Liste), bzw. ausgepackt werden aus einem Tupel oder einer Liste.

Syntax bei der Funktionsdeklaration mit **Sternchen:**

```python
def f(*x):
    print("0. Arg: ", x[0])
    print("1. Arg: ", x[1])
    print("Rest: ", x[2:])
    print(type(x))
```


#### Durch Schlüsselwort bestimmte Argumente: Dictionaries übergeben

Eine beliebige Zahl von durch Schlüsselwort bestimmte Argumente kann in ein **Wörterbuch** verpackt, bzw. aus diesem ausgepackt werden.

Syntax bei der Funktionsdeklaration mit **zwei Sternchen:**

```python
def f(**x):
    print(x)

# Argumente werden in das Wörterbuch x verpackt
f(tag='Montag', anzahl=5, preis=3.8)
```


```python
def diskriminante(**x):
    '''berechnet die Diskriminante von a*x**2+b*x+c=0'''
    return x['b']**2-4*x['a']*x['c']

# Argumente werden in das Wörterbuch x verpackt
diskriminante(a=2, b=3.5, c=-4)
```

**Syntax beim Aufruf:**


```python
def g(a=1, b=2):
    print(a*b)


wb = {'a': 5, 'b': 17}
g(**wb)  # Wörterbuch wird beim Aufruf ausgepackt
```

### Kombination aller Arten von Argumenten (optional)

In Python-Lehrbüchern werden Positions-Argumente häufig mit `pargs`, die keyword-Argumente mit `kwargs` abgekürzt.

Man kann nun in einer **Funktionsdeklaration** einzelne Positionsargumente mit verpackten pargs und kwargs kombinieren:


```python
def f(a, b, *pargs, **kwargs):
    print(("a: ", a))
    print(("b: ", b))
    print(("pargs: ", pargs))
    print(type(pargs))
    print(("kwargs: ", kwargs))
    print(type(kwargs))

f(11, 2, 3, 4, x=3.14, y=0.0)
```

**Beachtedabei die Reihenfolge:** Einzelne Positionsargumente -- \*pargs -- \*\*kwargs.

Beim Aufruf sieht das so aus:

```python
def f(a, b, c, d, x=0.0, y=0.0):
    print(("a: ", a))
    print(("b: ", b))
    print(("c: ", c))
    print(("d: ", d))
    print(("x: ", x))
    print(("y: ", y))
    return a*b*c*d+x*y

liste = [2, 3]
woerterbuch = {'x': 10., 'y': 3.5}

f(1, 4, *liste, **woerterbuch)
```
