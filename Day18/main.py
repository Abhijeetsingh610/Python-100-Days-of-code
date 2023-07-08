from turtle import Screen, Turtle
import random
mojo = Turtle()
mojo.shape("turtle")
#mojo.color("blue")

colours = ["chartreuse" , "firebrick" , "orchid" , "indigo" , "blue violet"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        mojo.forward(100)
        mojo.left(angle)


for shape_side in range(3 , 11):
    mojo.color(random.choice(colours))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()