from turtle import Turtle , Screen
import random
is_race = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make your bet" , prompt = "Which turtle will win the race . Enter the colour")
colors =  ["red" , "blue" , "purple" , "orange" , "yellow" , "green"]
turtle_position = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtle = []

for turtle_index in range(0,6):
    moj = Turtle(shape ="turtle")
    moj.color(colors[turtle_index])
    moj.penup()
    moj.goto(x= -230 , y = turtle_position[turtle_index])
    all_turtle.append(moj)

if user_bet:
    is_race = True


while is_race:
    for turtle in all_turtle: 
        if turtle.xcor()>230:
            winner = turtle.pencolor()
            if winner == user_bet:
               
                screen.title(f"You've won! The {winner} turtle is the winner")
            else:
                screen.title(f"You lose! The {winner} turtle is the winner")
                
        dist = random.randint(0,10)
        turtle.forward(dist)

screen.exitonclick()