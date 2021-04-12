---
title: Control Flow
parent: 1. Session
nav_order: 3
permalink: /1st_session/control_flow/
---

# Control Flow (Part 1)

Beim Programmieren tritt häufig der Fall auf, dass Teile des Codes nur unter einer gewissen Bedingung ausgeführt werden sollen.

Bedingungen werden über Boolsche Variablen abgefragt, also `True` und `False`.

In vielen anderen Programmiersprachen wird Code mit Klammern strukturiert - in Python allerdings funktioniert die Struktur über **Einrückungen von Blöcken**.

## Coder unter Bedingungen ausführen

### if .. elif .. else

```
zahl = 42

if zahl > 42:
    print("Das ist nicht die Antwort auf die Frage.")
elif zahl == 42:
    print("Aha!")
else:
    print("Die Zahl ist kleiner als 42.")
```

Der Programmfluss sieht so aus:

<img src='if_elif_else.png'></img>

### while-Schleifen

Man kann einen Programmblock so lange durchführen, wie eine gewisse Bedingung erfüllt ist, dann
mit dem weiteren Programm fortfahren.

```
n=int(input("Geben Sie eine nat. Zahl groesser als 0 ein: "))

while n%2 == 0:
    n = n//2
    print("n halbiert")
    print("Ergebnis: ", n)
```

Das Flussdiagramm sieht so aus:

<img src="while.png"></img>

Da in diesem Diagramm ein eine Schleife (loop) vorkommt, nennt man dieses Konstrukt 'while-Schleife'.


## Operationen mit Bedingungen / Boolschen Variablen

Für Wahrheitswerte sind die *Rechenoperationen* die logischen Operationen: `and`, `or`, `not`.

Man spricht in diesem Zusammenhang von einer Bool'schen Algebra.  Es gibt für `and` und `or` zwei Distributivgesetze, und für den Zusammenhang zwischen `not` und `und`, bzw. `or` die de Morgan'schen Regeln.

Das logische `und` muss nicht erklärt werden, das logische `oder` kann aber zu Missverständnissen führen: Es schließt den Fall, dass beide Seiten wahr sind, mit ein, ist also kein 'entweder ... oder'.

'''
True and False
'''


### Machinensprache?

Rechner basieren auf physikalischen Zuständen, meist elektrische Spannungen und Magnetfelder. Dabei erfolgt die Kodierung von Informationen in einer [binären Darstellung](https://de.wikipedia.org/wiki/Dualsystem)  - das heißt, es gibt nur zwei Zustände: an/aus - wahr/falsch - 1/0.

Das Binärsystem wurde schon  im 3. Jahrhundert v. Chr. in Indien benutzt, in Europa wurde es Ende des 17. Jahrhunderts von [Gottfried Wilhelm Leibniz](https://de.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) "entdeckt" und mit dem christlichen Glauben begründet. 1847 veröffentlichte der britische Mathematiker [George Boole](https://de.wikipedia.org/wiki/George_Boole) das Buch  *The Mathematical Analysis of Logic*, welches die Verbindung von Binären Zahlen mit Logischen Operationen herstellt - diese Darstellung ist bis heute als [Boolsche Algebra](https://de.wikipedia.org/wiki/Boolesche_Algebra) bekannt. Erst durch diese Grundlage war es möglich, Computer zu bauen, die Logische Operationen durchführen. Hier ein paar Beispiele für die Konversion von Dezimalzahlen in Binärdarstellung:

|Dezimalzahl|Binärdarstellung|
|---|---|
|1|1|
|2|10|
|3|11|
|7|111|
|31|11111|
|32|100000|


### Vergleiche

Durch `==` kann man prüfen, ob zwei Werte gleich sind, das Ergebnis ist `True`, wenn sie es sind, sonst `False`.


**Achtung**: Hier stehen **zwei Gleichheitszeichen!** Ein Gleichheitszeichen wird nur Zuweisungen von Variablen verwendet.

''' 1 == 1 '''
