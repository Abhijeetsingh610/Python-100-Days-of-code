from turtle import Turtle , Screen
import random


mojo = Turtle()

def move():
    mojo.forward(100)


def move_back():
    mojo.backward(100)

def move_left():
    mojo.left(10)

def move_right():
    mojo.right(10)


screen = Screen()
screen.listen()
screen.onkey(key = "Up" , fun = move)
screen.onkey(key = "Down" , fun = move_back)
screen.onkey(key = "Left" , fun = move_left)
screen.onkey(key = "Right" , fun = move_right)
screen.exitonclick()