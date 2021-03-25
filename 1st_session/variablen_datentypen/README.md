---
title: Variablen und Datentypen
parent: 1. Session
nav_order: 2
permalink: /1st_session/variablen_datentypen/
---

# Variablen, Datentypen und Operationen

In allen Programmiersprachen können nur bestimmte "Formen" von Information gespeichert werden. Diese Formen nennt man **Datentypen**.

## Variablen

Um einen Wert zu speichern und wieder abrufen zukönnen, werden **Variablen** benutzt.

Durch das Gleich-Zeichen `=` wird eine **Zuweisung** vorgenommen.  Auf der linken Seite steht der Name einer Variable auf der rechten Seite ein Ausdruck, der ein Objekt irgendeines Typs liefert, zum Beispiel eine Dezimalzahl. Eine Zuweisung ist *keine mathematische Gleichung*, denn Gleichungen kann man umstellen, Zuweisungen nicht.

```
x = 1 
```

**Variablennamen** können aus Buchstaben, \_ und Zahlen bestehen, am Anfang darf aber keine Zahl stehen. Großbuchstaben und Kleinbuchstaben werden unterschieden. `Wert` und `wert` wären also verschiedene Variablennamen. 

Wählt in Programmen die Variablennamen systematisch und lesbar; im Idealfall sagt die Variable, wozu sie dient.

Beachtet außerdem nach Möglichkeiten Benennungskonventionen für Variablen: Sie sollten mit einem Kleinbuchstaben beginnen, vermeidet deutsche Sonderbuchstaben (ä,ö,ü,ß). Konstanten,  also Variablen, die nicht verändert werden sollen, sollten Namen aus Großbuchstaben haben.


## Datentypen


**Zahlen**
* `int`, beschreibt beliebig große **ganze Zahlen** (integers), die Größe ist begrenzt durch den Arbeitsspeicher
* `float` beschreibt **Fließkommazahlen** (floating point number), 
    64 Bit, größter Betrag: 1.7976931348623157e+308, kleinster Betrag: 2.2250738585072014e-30
* `complex` beschreibt **komplexe Zahlen**, Real- und Imaginärteil sind floats

**Zeichenketten**
* `str` (String)

**Wahrheitswerte**
* `bool` lässt nur zwei Werte zu: `True` und  `False`  

Die Funktion `type()` gibt den Datentyp einer Variable zurück.

## (Rechen-) Operationen

Ihr könnt die üblichen Grundrechenarten, darüber hinaus `**` für die Potenz benutzen. 

Der Typ der Ergebnisse solcher Rechenoperationen hängt vom Typ der beteiligten Zahlen ab: Operationen aus float und int liefern float, aus complex und einem der anderen liefert complex.
    

### Prioritäten:

- Geklammerte Ausdrücke werden zuerst berechnet, innere Klammern vor äußeren.
- *Punkt vor Strich:*  /,\* kommt vor +,-

### Weitere Operationen

Wichtig ist noch die Division mit Rest `//`, bzw. der Rest bei dieser Division (modulo) `%`, der sowohl für ganze Zahlen (mit ganzzahligem Ergebnis) als auch für Fließkommazahlen (mit float als Ergebnis) definiert ist:

     7//3  --> 2    ganzzahlige Division

     7%3   --> 1    Modulo-Operator

### Operationen mit Strings

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
