from turtle import *

shape("turtle")
color("green")
speed(-1)

size = 5

for i in range(200):
    forward(size)
    left(90)

    size+=2

mainloop()