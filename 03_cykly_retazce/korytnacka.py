from turtle import forward, shape, left, right, exitonclick

shape('turtle')
for turn in range(3):    
    for move in range(4):
        forward(50)
        left(90)
    left(20)


exitonclick()