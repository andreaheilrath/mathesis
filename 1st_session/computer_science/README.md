---
title: Computer Science
parent: 1. Session
nav_order: 2
permalink: /1st_session/computer_science/
---

## Operationen mit Bedingungen / Boolschen Variablen

Für Wahrheitswerte sind die *Rechenoperationen* die logischen Operationen: `and`, `or`, `not`. 

Man spricht in diesem Zusammenhang von einer Bool'schen Algebra.  Es gibt für `and` und `or` zwei Distributivgesetze, und für den Zusammenhang zwischen `not` und `und`, bzw. `or` die de Morgan'schen Regeln.

Das logische `und` muss nicht erklärt werden, das logische `oder` kann aber zu Missverständnissen führen: Es schließt den Fall, dass beide Seiten wahr sind, mit ein, ist also kein 'entweder ... oder'.



### Machinensprache?

Rechner basieren auf physikalischen Zuständen, meist elektrische Spannungen und Magnetfelder. Dabei erfolgt die Kodierung von Informationen in einer [binären Darstellung](https://de.wikipedia.org/wiki/Dualsystem)  - das heißt, es gibt nur zwei Zustände: an/aus - wahr/falsch - 1/0.

Das Binärsystem wurde schon  im 3. Jahrhundert v. Chr. in Indien benutzt, in Europa wurde es Ende des 17. Jahrhunderts von [Gottfried Wilhelm Leibniz](https://de.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) "entdeckt" und mit dem christlichen Glauben begründet. 
1847 veröffentlichte der britische Mathematiker [George Boole](https://de.wikipedia.org/wiki/George_Boole) das Buch  *The Mathematical Analysis of Logic*, welches die Verbindung von Binären Zahlen mit Logischen Operationen herstellt - diese Darstellung ist bis heute als [Boolsche Algebra](https://de.wikipedia.org/wiki/Boolesche_Algebra) bekannt. Erst durch diese Grundlage war es möglich, Computer zu bauen, die Logische Operationen durchführen. Hier ein paar Beispiele für die Konversion von Dezimalzahlen in Binärdarstellung:

|Dezimalzahl|Binärdarstellung|
|---|---|
|1|1|
|2|10|
|3|11|
|7|111|
|31|11111|
|32|100000|


## **Was ist eigentlich ein [Algorithmus](https://de.wikipedia.org/wiki/Algorithmus)?**

Es gibt verschiedene Definitionen für Algorithmen. Hier soll zunächst eine weniger "saubere", dafür zugängliche Version dargestellt werden. Im Allgemeinen können Algorithmen nicht nur von Computern ausgeführt werden, es muss sich nur um eine eindeutige Handlungsforschirft handeln, die folgende Eigenschaften besitzt:

1. **Eindeutigkeit**: ein Algorithmus darf keine widersprüchliche Beschreibung haben. Diese muss eindeutig sein.
2. **Ausführbarkeit**: jeder Einzelschritt muss ausführbar sein.
3. **Finitheit** (= Endlichkeit): die Beschreibung des Algorithmus muss endlich sein.
4. **Terminierung**: nach endlich vielen Schritten muss der Algorithmus enden und ein Ergebnis liefern.
5. **Determiniertheit**: der Algorithmus muss bei gleichen Voraussetzungen stets das gleiche Ergebnis liefern.
6. **Determinismus**: zu jedem Zeitpunkt der Ausführung besteht höchstens eine Möglichkeit der Fortsetzung. Der Folgeschritt ist also eindeutig bestimmt.


Die mathematisch korrekte Definition basiert auf dem Konzept der [Berechenbarkeit](https://de.wikipedia.org/wiki/Berechenbarkeit) und dem Modell der [Turingmaschine](https://de.wikipedia.org/wiki/Turingmaschine). Dazu später mehr.
