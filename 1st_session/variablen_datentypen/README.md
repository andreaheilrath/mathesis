---
title: Variablen und Datentypen
parent: 1. Session
nav_order: 2
permalink: /1st_session/variablen_datentypen/
---

# Variablen, Datentypen und Operationen

## Variablen

In vielen anderen Programmiersprachen muss der Datentyp einer Variable zuvor definiert werden. In Python ist die Typisierung dynamisch und erfolgt durch den Wert, der in die Variable gespeichert wird.

Variablennamen können aus Buchstaben, \_ und Zahlen bestehen, am Anfang darf aber keine Zahl stehen. Großbuchstaben und Kleinbuchstaben werden unterschieden.

```
x = 1
y_2 = "test"
```


## Datentypen

Grundsätzlich gibt es verschiedene Arten von Daten: Zahlen, Text und Wahrheitswerte.

Kürzel | Datentyp | Beispiel
--- | --- | ---
`int`| ganze Zahlen | `x = 1`
`float`| Fließkommazahlen | `x = 1.0`
`complex`| komplexe Zahlen | `x = 1.1 + 4j`
`str`| Zeichenketten | `x = "Test123" x = '1String'`
 `bool`| Wahrheitswert | `x = True`


Wichtige Funktionen im Kontext von Datentypen:

* `type(x)` gibt den Datentyp einer Variable `x` zurück
* `int()`, `float()`, `complex()` wandelt Zahlen-Datentypen ineinander um
* `str()` erzeugt Strings aus anderen Datentypen
* `bool()` erzeugt Wahrheitswerte

## Eingaben und Ausgaben

* `print(x)` gibt den Inhalt von `x` aus
* `input()` öffnet ein Textfeld zur Eingabe einer Zeichenkette

## Rechenoperationen

*  +,-,\*,/
* `**` Potenzrechung
* `//` ganzzahlige Division
* `%` Modulo-Operator (gibt den Rest der Division an)

## Operationen mit Strings

* `len()` gibt die Länge des Strings

Indizierung und Slicing:

* `s[0]` gibt das erste Zeichen des Strings `s`, `s[1]` das zweite usw.
* `s[anfang:ende]`  liefert den Teil des Strings, der zu den Indices i mit `anfang` $\leq i< $ `ende` gehört, der letzte Index ist also `ende-1`!
* `s[anfang:ende:sprung]` liefert den Teil des Strings, der zu den Indices $i \in \{ $ `anfang, anfang+sprung, anfang+2*sprung` $ ,\ldots \{$ mit $ i< $`ende` gehört.

Andere Funktionen für Strings:

* `s.replace(alt,neu)` liefert einen String, in dem alle Vorkommen des Strings `alt` im String `s` durch den String `neu` ersetzt wurden. 
* `s.upper` und `s.lower` liefern den String in Groß- bzw. Kleinbuchstaben umgewandelt 
* `s.find(...)` sucht, ab welchem Index der für ... eingesetzte String nin `s` vorkommt.
