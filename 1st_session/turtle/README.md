---
title: Turtle Grafik
parent: 1. Session
nav_order: 4
permalink: /1st_session/turtle/
---

# Turtle Grafik

In dieser Einheit soll es um die Befehle des Turtle Grafik-Moduls gehen.

## Grundlegende Befehle

Das Modul stellt verschiedene Funktionen zur Verfügung, mit denen man zeichnen kann:

```
turtle.fd(x)    #'forward'  bewegt turtle um x Einheiten vorwärts
turtle.lt(x)    #'left turn' dreht turtle um x Grad nach links
turtle.rt(x)    #'right turn' dreht turtle um x Grad nach rechts
turtle.pd()     #'pen down'   versetzt turtle in den Schreibmodus
turtle.pu()     #'pen up' beendet den Schreibmodus
```

Weitere Befehle des Turtle-Moduls:

* `turtle.bye()` schließt das Turtle-Fenster
* `turtle.exitonclick()` hält das Turtle-Fenster offen, bis darauf geklickt wird
* `turtle.delay(...)` stellt ein wie viele Millisekunden 'turtle' zwischen den einzelnen Aktionen wartet
* `turtle.speed(...)` bestimmt, wie schnell sich die Schildkröte bei den einzelnen Schritten bewegt

Eine vollständige Übersicht über die Befehle findet man unter [https://docs.python.org/2/library/turtle.html](https://docs.python.org/2/library/turtle.html)


In manchen Betriebssystemen gibt es einen Konflikt zwischen dem Jupyter-Notebook und der Verwaltung der Turtle-Fenster. Wenn ein Problem ergibt, sollten
Programme besser nicht in einem Notebook, sondern mit einem Editor geschrieben und direkt mit dem Interpreter ausgeführt werden.


## Beispiele



```
import turtle

turtle.fd(100)
turtle.lt(90)
turtle.forward(50)
turtle.lt(90)
turtle.fd(25)
turtle.lt(90)
turtle.exitonclick()

```

... hier noch ein paar neue Funktionen.
Was passiert hier?

```
import turtle

turtle.fd(100)
turtle.lt(90)
print(turtle.xcor(), turtle.ycor())
turtle.goto(200, 100)
print(turtle.xcor(), turtle.ycor())
turtle.exitonclick()

```
