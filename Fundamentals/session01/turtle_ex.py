from turtle import *

shape("turtle")
color("red")

n = int(input("Nhập vào số cạnh của hình : "))

for i in range(n):
    forward(100)
    left(360/n)

mainloop()