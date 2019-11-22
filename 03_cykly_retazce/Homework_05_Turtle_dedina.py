# 10 domcekov
from turtle import forward, shape, left, right, exitonclick, pendown, penup
from math import sqrt

strana = 40
shape('turtle')
#turtle.speed(6)
penup()
forward(-300)
pendown()

for house in range(10):    
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
    forward(strana*1.5)
    

exitonclick()