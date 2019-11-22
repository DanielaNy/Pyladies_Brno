from turtle import forward, left, right, getcanvas

forward(50)
left(50)
forward(50)
right(50)
forward(50)

getcanvas().postscript(file='obrazek.ps')

