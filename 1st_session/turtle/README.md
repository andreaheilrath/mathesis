# Turtle Grafik

In diesem Notebook soll es um die Befehle des Turtle-Moduls gehen.

Mit `turtle.delay(...)` wird eingestellt,
welche Zeit (in Millisekunden) 'turtle' zwischen den einzelnen Aktionen wartet.
Mit `turtle.speed(...)` wird eingestellt,
wie schnell sich die Schildkröte bei den einzelnen Schritten bewegt.

Das Modul stellt verschiedene Funktionen zur Verfügung,
mit denen man zeichnen kann:

    turtle.fd(x)  #'forward'  bewegt turtle um x Einheiten vorwärts
    turtle.lt(x)  #'left turn' dreht turtle um x Grad nach links
    turtle.rt(x)  #'right turn' dreht turtle um x Grad nach rechts
    turtle.pd()   #'pen down'   versetzt turtle in den Schreibmodus
    turtle.pu()   #'pen up' beendet den Schreibmodus


Eine vollständige Übersicht über die Befehle findet man unter
https://docs.python.org/2/library/turtle.html

Wenn nicht im interaktiven Modus gearbeitet wird, geht das Fenster
gleich nach dem Zeichnen wieder zu. Mit dem Befehl

    turtle.exitonclick()

schließt das Fenster erst, wenn darauf geklickt wird.

Mit

    turtle.bye()

lässt sich ein turtle-Fenster schließen.

In manchen Betriebssystemen gibt es einen Konflikt zwischen dem Jupyter-Notebook und
der Verwaltung der Turtle-Fenster. Wenn ein Problem ergibt, sollten
Programme besser nicht in einem Notebook, sondern mit einem Editor geschrieben und direkt mit dem
Interpreter ausgeführt werden.

'''
import turtle

turtle.fd(100)
turtle.lt(90)
turtle.forward(50)
turtle.lt(90)
turtle.fd(25)
turtle.lt(90)
turtle.bye()
turtle.exitonclick()
'''

Die Turtlegraphik war ursprünglich so gedacht, wie oben beschrieben. Sie zeichnet, indem sie sich relativ zu einer Position bewegt.

Es gibt aber dennoch ein zugrundeliegendes unsichtbares Koordinatensystem. In diesem hat die Turtle eine Position (x,y). Man kann sie mit

    turtle.goto(x_neu, y_neu)

zu einer neuen absoluten Position bewegen.

Welche Koordinaten überhaupt verfügbar sind, lässt sich mit turtle.screensize ermitteln.
Der Ursprung (0,0) liegt in der Mitte.

'''
turtle.fd(100)
turtle.lt(90)
print(turtle.xcor(), turtle.ycor())
turtle.exitonclick()
'''
