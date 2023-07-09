from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.write(f"Score: {self.score}" , align = "center" , font = ("Arial" , 24 , "normal"))
        

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.color("White")
        self.penup() 
        self.goto(0,0)       
        self.write(f"Game Over! Your score is :{str(self.score)}" , align = "center" , font = ("Arial" , 24 , "normal"))
        self.hideturtle()


    