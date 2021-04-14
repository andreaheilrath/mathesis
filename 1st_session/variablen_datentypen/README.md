---
title: Variablen und Operationen
parent: 1. Session
nav_order: 2
permalink: /1st_session/variablen_datentypen/
---

# Variablen, Datentypen und Operationen

## Variablen

So sieht eine Variablendeklaration aus: 

```
x = 1
y_2 = "test"
```

In diesen beiden Zeilen werden die Variablen `x` und `y_2` erstellt und mit den Werten `1` bzw. `"test"` gefüllt. 

Variablennamen können aus Buchstaben, \_ und Zahlen bestehen, am Anfang darf aber keine Zahl stehen. Großbuchstaben und Kleinbuchstaben werden unterschieden.

In vielen anderen Programmiersprachen muss der Datentyp einer Variable zuvor definiert werden. In Python ist die Typisierung dynamisch und erfolgt durch den Wert, der in die Variable gespeichert wird.

## Datentypen

Grundsätzlich gibt es verschiedene Arten von Daten: Zahlen, Text und Wahrheitswerte.

Kürzel | Datentyp | Beispiel
--- | --- | ---
`int`| ganze Zahlen | `x = 1`
`float`| Fließkommazahlen | `x = 1.0`
`complex`| komplexe Zahlen | `x = 1.1 + 4j`
`str`| Zeichenketten | `x = "Test123" x = '1String'`
 `bool`| Wahrheitswert | `x = True`


### Typabfrage und Typumwandlung

* `type(x)` gibt den Datentyp einer Variable `x` zurück
* `int(x)`, `float(x)`, `complex(x)` wandelt `x` in den entsprechenden Datentyp um
* `str(x)` erzeugt String `x`
* `bool(x)` erzeugt einen Wahrheitswert aus `x`. 0 und `""` (ein leerer String) wird `False` alles andere `True`


## Eingaben und Ausgaben

* `print(x)` gibt den Inhalt von `x` aus
* `x = input('Texteingabe hier:')` öffnet ein Textfeld zur Eingabe einer Zeichenkette und speichert diese in `x`


## Rechenoperationen

*  `+`, `-`, `*`, `/` Grunderechenarten
* `**` Potenzrechung
* `//` ganzzahlige Division
* `%` Modulo-Operator (gibt den Rest der Division an)

## Operationen mit Strings

Im Folgenden soll in der Variable `s` ein Wert vom Datentyp String, also eine Zeicenkette gespeichert sein.

* `+`und `*` funktionieren auch für Strings
* `len(s)` gibt die Länge des Strings zurück (also die Anzahl an Zeichen)

Indizierung und Slicing:

* `s[0]` gibt das erste Zeichen des Strings `s`, `s[1]` das zweite usw.
* `s[anfang:ende]`  liefert den Teil des Strings, der zu den Indices i mit `anfang` $\leq i< $ `ende` gehört, der letzte Index ist also `ende-1`!
* `s[anfang:ende:sprung]` liefert den Teil des Strings, der zu den Indices $i$ aus `anfang, anfang+sprung, anfang+2*sprung` mit $i<$ `ende` gehört.

Andere Funktionen für Strings:

* `s.replace(alt,neu)` liefert einen String, in dem alle Vorkommen des Strings `alt` im String `s` durch den String `neu` ersetzt wurden. 
* `s.upper` und `s.lower` liefern den String in Groß- bzw. Kleinbuchstaben umgewandelt 
* `s.find(...)` sucht, ab welchem Index der für ... eingesetzte String nin `s` vorkommt.

## Ein Beispiel

```
eingabe = input("Bitte geben Sie eine ganze Zahl ein:")
zahl = int(eingabe)

print(zahl*2, eingabe*2)
```

Was wird wohl die Ausgabe dieses Codes sein?
