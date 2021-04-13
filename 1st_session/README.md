---
title: 1. Session
nav_order: 2
has_children: true
permalink: /1st_session/
---

# 1. Session

Heute starten wir durch und lernen mehr über Python!

Du lernst heute etwas über 
* Variablen und Datentypen, User Input, Rechenoperationen, Operationen mit Strings
* Bedingungen: if, elif, else & while, Boolesche Variablen und Vergleiche
* Turtle Grafik


## Dateien zum Download

....

## Check yourself!

Diesen Code solltest du nach der Session vollständig verstehen können.

```
import turtle

user_input = input("Gib eine ganze Zahl ein:")
number = int(user_input)
step = 20
angle = 360

while number > 0:
    print("Die Variable number hat den Wert", number)
    if number % 2 == 0:
        turtle.forward(step)
        turtle.left(angle / number)
    else:
        turtle.forward(step * 2)
        turtle.left(angle / number / 2)
    number = number - 1

turtle.exitonclick()

```
