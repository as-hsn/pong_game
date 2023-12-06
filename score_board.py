from turtle import Turtle

FONT = ('Georgia', 30, 'normal')

class Score(Turtle):
    def __init__(self):
       super().__init__()
       self.color ("white")
       self.l_score = 0
       self.r_score = 0
       self.update_score ()
    def update_score(self):
        self.clear()
        self.penup ()
        self.hideturtle()
        self.goto(-100, 260)
        self.write(self.l_score,font= FONT)
        self.goto(100, 260)
        self.write (self.r_score,font= FONT)

    def left_score(self):
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.r_score += 1
        self.update_score()