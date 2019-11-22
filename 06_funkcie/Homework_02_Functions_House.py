from turtle import forward, left, right, exitonclick
from math import sqrt
size = int(input('Enter the size of the house in pixels: '))

def print_house(size):
    'printing house function'
    left(90)
    forward(size)
    right(45)
    forward(size/(sqrt(2)))
    right(90)
    forward(size/(sqrt(2)))
    right(45)
    forward(size)
    right(135)
    forward(2*size/(sqrt(2)))
    right(135)
    forward(size)
    right(135)
    forward(2*size/(sqrt(2)))
    left(135)
    forward(size)
    exitonclick

print_house(size)