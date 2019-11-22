from turtle import forward, shape, left, right, exitonclick, pendown, penup

shape('turtle')

for move in range(40):
    penup()
    forward(3)
    pendown()
    forward(3+move)


exitonclick()