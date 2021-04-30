def fib(n):
    if n == 1 or n == 0:
        turtle.left(90)
        turtle.forward(4)
        return 1
    else:
        value = fib(n-2) + fib(n-1)
        turtle.left(90)
        turtle.forward(value*4)
        return value

import turtle
turtle.penup()
turtle.goto(-120,-120)
turtle.pendown()
turtle.speed(0)
print(fib(11))
turtle.exitonclick()
