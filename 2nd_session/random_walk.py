import turtle
import random

turtle.speed(0)

max_iterations = 200
iteration = 0

step = 20

turtle.lt(random.randint(0,3)*90)
turtle.forward(step)

while not(round(turtle.xcor()) == 0 and round(turtle.ycor()) == 0):
    turtle.lt(random.randint(0,3)*90)
    turtle.forward(step)
    iteration += 1

print("Anzahl Schritte:", iteration)
print("Finale Koordinaten:", turtle.xcor(), turtle.ycor())
turtle.exitonclick()
