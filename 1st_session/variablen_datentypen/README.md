---
title: Variablen und Datentypen
parent: 1. Session
nav_order: 2
permalink: /1st_session/variablen_datentypen/
---

# Variablen, Datentypen und Operationen

## Variablen

Die Zuweisung einer Variablen in Python funktioniert so:

```
x = 1
```

**Variablennamen** können aus Buchstaben, \_ und Zahlen bestehen, am Anfang darf aber keine Zahl stehen. Großbuchstaben und Kleinbuchstaben werden unterschieden.


## Datentypen

Grundsätzlich gibt es verschiedene Arten von Daten: Zahlen, Text und Wahrheitswerte.

* `int`: ganze Zahlen
* `float`: Fließkommazahlen
* `complex`: komplexe Zahlen
* `str`: Zeichenketten (Strings)
* `bool`: Wahrheitswert - `True` oder `False`  

Wichtige Funktionen im Kontext von Datentypen:

* `type()` gibt den Datentyp einer Variable zurück
* `int()`, `float()`, `complex()` wandelt Zahlen-Datentypen ineinander um
* `str()` erzeugt Strings aus anderen Datentypen
* `bool()` erzeugt Wahrheitswerte

## Rechenoperationen

*  +,-,\*,/
* `**` Potenzrechung
* `//` ganzzahlige Division
* `%` Modulo-Operator (gibt den Rest der Division an)

## Operationen mit Strings

Eine Zeichenkette kann durch Einfache Anführungszeichen '...' oder doppelte Anführungszeichen "..." eingeschlossen werden. Passt eine solche Zeichenkette nicht in eine Zeile, so lässt sich - wie stets in Python - durch einen Backslash `\` die Zeile in die folgende Zeile verlängern. Die über mehrere Zeilen verteilten Langzeilen werden vom Interpreter anschließend wieder aneinander gehängt, dabei werden die \ wieder entfernt.

Für wirklich mehrzeiligen Text gibt es noch eine praktischere Variante, dreifache Anführungszeichen am Anfang und am Ende. Die Zeilenumbrüche werden in dieser Variante Teil der Zeichenkette. Ein Zeilenumbruch kann auch mit `\n` codiert werden.


Die **einzelnen Zeichen eines Strings** kann man über einen Index in eckigen Klammern erreichen.

**Indizierung** ist ein wichtiges Konzept bei größeren Datenstruktueren wie Listen oder Arrays, die wir nächste Woche kennen lernen.

Durch `s[0]` greift man auf den ersten Buchstaben einens Strings zu, `s[1]` auf den zweiten, etc.  Das letzte Zeichen eines Strings hat den Index `len(s)-1`.

Es ist auch möglich, mit negativen Indizes von hinten zu zählen: `s[-1]` liefert das letzte Zeichen, `s[-2]` das vorletze.

**Bemerkung**: So gut wie alle num(m)erierten Objekte in Python Zählen von Null an. Das entspricht natürlich nicht der Umgangssprache: In einer Reihe von zehn Bäumen wird man vom ersten, zweiten, ... , zehnten Baum sprechen.  Hier müssen Sie sich daran gewöhnen, vom nullten, ersten,  ... , neunten Baum zu reden.  Das ist eine mögliche Fehlerquelle, also Vorsicht!

Man kann auch einen Ausschnitt (ein `slice`) eines Strings bekommen, indem man in eckigen Klammern zwei oder drei durch Doppelpunkte getrennte Zahlen eingiebt.

- `s[anfang:ende]`  liefert den Teil des Strings, der zu den Indices i mit `anfang`$\leq i< $`ende` gehört, der letzte Index ist also `ende-1`!

- `s[anfang:ende:sprung]` liefert den Teil des Strings, der zu den Indices
i$\in\{$ `anfang, anfang+sprung, anfang+2*sprung` $,\ldots\}$ mit $ i< $`ende` gehört.

Für negative Indices ist wieder zu beachten, dass -1 dem Index `len(s)-1`, -k dem Index `len(s)-k` entspricht. In diesem Fall liefert `s[anfang:ende:sprung]`  für `anfang>ende` den Teilstring, der zu den Indices i$\in\{$ `anfang, anfang+sprung, anfang+2*sprung` $,\ldots\}$ mit $ i> $`ende` gehört.


Lässt man die erste Zahl weg, also etwa s[:3], so wäre alles ab dem Anfang (Index 0) gemeint. Lässt man die zweite
Zahl weg, so ist alles bis zum Ende gemeint.

Diese Art, bestimmte Teile eines indizierten Objekts zu bekommen, nennt man **slicing**.  Es ist sehr wichtig und nützlich und wird uns noch öfter begegnen.

Es gibt natürlich viel mehr Stringoperationen, die man nachschlagen kann, sobald man sie braucht. Es sollen noch einige erwähnt werden, weil wir sie bald gebrauchen können. **Beachtet im Folgenden, dass der Variablennamen durch einen Punkt vom Namen einer Funktion getrennt wird.** Wir werden das später noch näher kennenlernen; es handelt sich um so genannte Methoden von Objekten.

Ist `s` ein String, der am Ende Leerzeichen enthält oder `\n` (’newline’), bzw. `\r`(’carriage return’), so liefert die Funktion `s.rstrip()` einen String zurück, aus dem diese unsichtbaren Zeichen entfernt wurden. (Die Zeichen `\r` und `\n` trennen in gewöhnlichen Textdateien die Zeilen voneinander. Deswegen treten diese Zeichen beim Lesen solcher Dateien für gewöhnlich auf.)

Die Funktion `s.replace(alt,neu)` liefert einen String, in dem alle Vorkommen des Strings `alt` im String `s` durch den String `neu` ersetzt wurden. Die Funktionen `s.upper` und `s.lower` liefern den String in Groß- bzw. Kleinbuchstaben umgewandelt zurück. **Der ursprüngliche String bleibt dabei unverändert, wenn Sie die Variable nicht neu zuweisen.**

Eine weitere nützliche Funktion ist `s.find(...)`.  Diese sucht, ab welchem Index der für ... eingesetzte String
in `s` vorkommt. Kommt er nicht vor, wird -1 zurückgegeben.
