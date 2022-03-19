import turtle
import random
import time
from turtle import Screen, Turtle
screen= Screen()
screen.tracer(False)

screenWidth = 600
screenHeight = 600

turtle.screensize(screenWidth, screenHeight,bg="black")
ListOfObjects = []
class Bomber(Turtle):
  def __init__(self,xpos,ypos,xSTRECH=1,ySTRECH=1,list= ListOfObjects):
    super().__init__()
    list.append(self)
    self.penup()
    self.shape("square")
    self.color("white")
    self.goto(xpos,ypos)
    self.yMove = random.randint(-2,2)
    if self.yMove==0:
      self.yMove+=1
    self.xMove = random.randint(1,8)
  def move(self):
    global screenWidth,screenHeight
    self.x = self.xcor()+self.xMove
    self.y = self.ycor()+self.yMove
    self.goto(self.x,self.y)
    if self.x > screenWidth/2 or (screenWidth/2)*-1>self.x:
      self.xMove = self.xMove*-1
    if self.y > screenHeight/2 or (screenHeight/2)*-1>self.y:
      self.yMove = self.yMove *-1
class Player(Turtle):
  def moveup(self):
    self.y+=9
    self.goto(self.x,self.y)

  def movedown(self):
    self.y -= 9
    self.goto(self.x, self.y)
  def moveright(self):
    self.x += 9
    self.goto(self.x, self.y)
  def moveleft(self):
    self.x -= 9
    self.goto(self.x, self.y)
  def __init__(self,list = ListOfObjects):
    super().__init__(shape="square")
    self.penup()
    self.color("red")
    list.append(self)
    screen.onkeypress(fun = self.moveright, key = "Right")
    self.x = 0
    self.y = 0
    self.shapesize(stretch_wid=1.5,stretch_len=1.5)
  def move(self):
    pass
bomber1= Bomber(-200,200)
bomber2= Bomber(200,200)
bomber3= Bomber(-200,-200)
bomber4= Bomber(200,-200)
Player = Player()


screen.listen()
def Game(*args):
  screen.onkey(fun=Player.moveright, key="Right")
  screen.onkey(fun=Player.moveleft, key="Left")
  screen.onkey(fun=Player.moveup, key="Up")
  screen.onkey(fun=Player.movedown, key="Down")
  while True:
    for obj in ListOfObjects:
      obj.move()
      if obj.distance(Player)<30:
        print("GAMEOVER")
        break
    time.sleep(.008)
    screen.update()
while True:
    screen.onclick(fun = Game)
    screen.mainloop()

screen.mainloop()