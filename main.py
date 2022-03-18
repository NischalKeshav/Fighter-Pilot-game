import turtle
from turtle import Screen, Turtle
screen= Screen()
turtle.screensize(canvwidth=500, canvheight=300,bg="black")
class Bomber(Turtle):
  def __init__(self,xpos,ypos,xSTRECH=1,ySTRECH=1):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("white")
    self.goto(xpos,ypos)
bomber1= Bomber(-200,80)
bomber2= Bomber(200,80)
bomber3= Bomber(-200,-80)
bomber4= Bomber(200,-80)
screen.mainloop()