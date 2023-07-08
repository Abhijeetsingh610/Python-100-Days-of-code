from turtle import Turtle , Screen
import random

mojo = Turtle()

colours = ["chartreuse" , "firebrick" , "orchid" , "indigo" , "blue violet"]
directions = [0 , 90 , 180 , 270]
mojo.pensize(15)
mojo.speed("fastest")

for _ in range(200):
    mojo.color(random.choice(colours))
    mojo.forward(30)
    mojo.setheading(random.choice(directions))


















screen = Screen()
screen.exitonclick()