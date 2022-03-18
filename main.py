import turtle
import random
from turtle import Screen, Turtle
screen= Screen()
screen.tracer(False)

screenWidth = 400
screenHeight = 400

turtle.screensize(canvwidth=screenWidth, canvheight=screenHeight,bg="black")
ListOfObjects = []
class Bomber(Turtle):
  def __init__(self,xpos,ypos,xSTRECH=1,ySTRECH=1,list= ListOfObjects):
    super().__init__()
    list.append(self)
    self.penup()
    self.shape("square")
    self.color("white")
    self.goto(xpos,ypos)
    self.yMove = random.randint(-5,5)
    self.xMove = random.randint(0,10)-self.yMove
  def move(self):
    global screenWidth,screenHeight
    x = self.xcor()+self.xMove
    y = self.ycor()+self.yMove
    self.goto(x,y)
    if x > screenWidth/2 or screenWidth*-1<x:
      self.xMove = self.xMove*-1
    if
bomber1= Bomber(-200,200)
bomber2= Bomber(200,200)
bomber3= Bomber(-200,-200)
bomber4= Bomber(200,-200)
while True:  
  for  obj in ListOfObjects:
    obj.move()
  screen.update()
screen.mainloop()