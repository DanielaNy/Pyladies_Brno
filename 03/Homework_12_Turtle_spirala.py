from turtle import forward, pendown, penup, left, right, exitonclick
from math import tan, atan

r = int(input('Enter r: '))
A = 2*3.14*r/360

beta = (180-(atan(A/r)*180/3.14))/2
gamma = 90-beta
for i in range(10*360):
    forward(A+0.001*i)
    right(2*gamma)

exitonclick()