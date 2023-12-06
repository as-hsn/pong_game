from turtle import Turtle

class Paddle(Turtle):
   def __init__(self, position):
      super().__init__()
      self.shape ("square")
      self.color ("white")
      self.penup ()
      self.shapesize (stretch_wid=5,
                        stretch_len=1)
      self.goto (position)

   def go_up(self) :
       pad_plus = self.ycor () + 30
       self.sety (pad_plus)

   def go_down(self) :
       pad_minus = self.ycor () - 30
       self.sety (pad_minus)

