from turtle import left, right, penup, pendown, forward, exitonclick, speed
import turtle
from random import randint
from math import tan, atan

n = randint(1, 10)
r = 20
A = 2*3.14*r/360
beta = (180-(atan(A/r)*180/3.14))/2
gamma = 90-beta



artist = input('Concert of which Czech artist do yo organize? ')
print('Great! People are surelly looking forward to it. \nThe gate is open now.')

turtle.speed(0)


for x in range(n):
    for i in range(360):    # Sorry for the speed
        forward(A)
        right(2*gamma)
    ### Person ###
    penup()
    right(90)
    forward(2*r)
    pendown()
    forward(40)
    right(30)
    forward(30)
    penup()
    right(180)
    forward(30)
    pendown()
    right(120)
    forward(30)
    penup()
    right(180)
    forward(30)
    right(30)
    forward(20)
    right(90)
    forward(15)
    right(180)
    pendown()
    forward(30)
    penup()
    forward(randint(-50, 50))
    left(90)
    forward(randint(-50, 50))
    left(90)
    pendown()

print(f"{n} people visited the gig of {artist}.".format(n, artist))
exitonclick()