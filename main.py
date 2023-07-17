import turtle
from turtle import Turtle, Screen

tim = turtle.Turtle()
tim.speed('fast')
tim.shape('classic')
tim.penup()
tim.left(90)
tim.forward(100)
tim.left(30)
tim.pendown()
tim.pensize(2)
tim.color('red3')
for _ in range(4):
    tim.forward(100)
    tim.right(120)
tim.color('orangered')
for _ in range(4):
    tim.forward(100)
    tim.right(90)
tim.color('orange1')
for _ in range(5):
    tim.forward(100)
    tim.right(72)
tim.color('yellow')
for _ in range(6):
    tim.forward(100)
    tim.right(60)
tim.color('springgreen3')
for _ in range(7):
    tim.forward(100)
    tim.right(51.43)
tim.color('cornflowerblue')
for _ in range(8):
    tim.forward(100)
    tim.right(45)
tim.color('slateblue3')
for _ in range(9):
    tim.forward(100)
    tim.right(40)
tim.color('purple4')
for _ in range(10):
    tim.forward(100)
    tim.right(36)



screen = Screen()
screen.exitonclick()