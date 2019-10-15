from turtle import forward, left, right, exitonclick, penup, pendown
from random import randint

length = 50
x = randint(-100, 100)
y = randint(-100, 100)
d = randint(0,360)

i = int(input("Hom many n-gons do you want? "))

for i in range(i):
    penup()
    forward(x)
    forward(y)
    right(d)
    pendown()

    n = randint(3, 10)
    for side in range(n):
        forward(length)
        right(180-(180-360/n))

exitonclick()