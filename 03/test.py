from turtle import forward, left, right, exitonclick

strana = 50
for sestuholnik in range(6):
    left(120)
    for side in range(6):
        forward(strana)
        right(60)
    
    forward(strana)
    right(60)

exitonclick()