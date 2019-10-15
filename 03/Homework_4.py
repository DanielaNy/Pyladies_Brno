from turtle import forward, shape, left, right, exitonclick, pendown, penup
from math import sqrt

strana = 50
shape('turtle')

pendown()
left(90)
forward(strana)
right(45)
forward(strana/(sqrt(2)))
right(90)
forward(strana/(sqrt(2)))
right(45)
forward(strana)
right(135)
forward(2*strana/(sqrt(2)))
right(135)
forward(strana)
right(135)
forward(2*strana/(sqrt(2)))
left(135)
forward(strana)

penup()

exitonclick()