import turtle
import random
import time,math
from turtle import Screen, Turtle
screen= Screen()
screen.tracer(False)
ongoing=False
#print("hi")
screenWidth = 800
screenHeight = 800
screen.screensize(screenWidth,screenHeight,bg="black")
screen.setup(screenWidth, screenHeight)
ListOfObjects = []
ENEMYWID=2
class Bomber(Turtle):
  def __init__(self,xpos,ypos,xSTRECH=1,ySTRECH=1,list= ListOfObjects):
    super().__init__()
    list.append(self)
    self.penup()
    self.orgpos=xpos,ypos
    self.shape("square")
    self.color("white")
    self.goto(xpos,ypos)
    self.shape("circle")
    self.shapesize(stretch_wid=ENEMYWID,stretch_len=ENEMYWID)
    self.dir= random.randint(0,360)
    self.yMove = 5*math.cos(self.dir)
    if self.yMove==0:
      self.yMove+=1
    self.xMove = 5*math.sin(self.dir)
  def move(self):
    global screenWidth,screenHeight
    self.x = self.xcor()+self.xMove
    self.y = self.ycor()+self.yMove
    self.goto(self.x,self.y)
    if self.x > screenWidth/2 or (screenWidth/2)*-1>self.x:
      self.xMove = self.xMove*-1
    if self.y > screenHeight/2 or (screenHeight/2)*-1>self.y:
      self.yMove = self.yMove *-1
    try:
      self.dir= math.atan(self.y/self.x)
    except:
      self.dir=.45
    
    if self.xMove<0:
      self.dir=math.pi/2+(math.pi/2-self.dir)
    #print(self.dir)





class player(Turtle):
  def moveup(self):
   
    self.goto(self.x,self.y)
    self.ymove=3
  def movedown(self):
    self.ymove = -3
    self.goto(self.x, self.y)
  def moveright(self):
    self.xmove = 3
    self.goto(self.x, self.y)
  def moveleft(self):
    self.xmove = -3
    self.goto(self.x, self.y)
  def __init__(self,list = ListOfObjects):
    super().__init__(shape="square")
    self.orgpos=0,0
    self.penup()
    self.color("red")
    list.append(self)
    screen.onkeypress(fun = self.moveright, key = "Right")
    self.x = 0
    self.y = 0
    self.shapesize(stretch_wid=1.5,stretch_len=1.5)
    self.xmove=0
    self.ymove=0
  def releaseLeft(self):
    if self.xmove<0:
      self.xmove=0  
  def releaseRight(self):
    if self.xmove>0:
      self.xmove=0
  def releaseUP(self):
    if self.ymove>0:
      self.ymove=0
  def releaseDown(self):
    if self.ymove<0:
      self.ymove=0
  def move(self):
   
    if self.x > screenWidth/2-30 :
      self.xmove=0
      self.x=screenWidth/2-30
    if (screenWidth)/2*-1+30>self.x:
      self.xmove=0
      self.x= -screenWidth/2+30
    if self.y > screenWidth/2-30 :
      self.ymove=0
      self.y=screenHeight/2-30
    if (screenHeight)/2*-1+30>self.y:
      self.ymove=0
      self.y=-screenHeight/2+30
    self.x+=self.xmove
    self.y+=self.ymove
    self.goto(self.x, self.y)
  def reset(self):
    self.goto(0,0)
    self.x=0
    self.y=0


class Timer(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.goto(-40,280)
    self.color("white")
  def writeTime(self,time):
    time = str(time)[0:6]
    self.clear()
    self.write(time,font=("times new roman",18,"normal"))
  def reset(self):
    #super().__init__()
    self.hideturtle()
    self.goto(-40,280)
    self.color("white")
  def GAMEOVER(self):
    self.goto(-100,100)
    self.write("GAME OVER", font=("times new roman",52,"bold"))








Timer = Timer()

bomber1= Bomber(-300,300)
bomber2= Bomber(300,300)
bomber3= Bomber(-300,-300)
bomber4= Bomber(300,-300)
bomber4= Bomber(300,-350)
bomber5= Bomber(000,-300)
bomber6= Bomber(300,000)
bomber7= Bomber(350,-350)
#Player = player()


screen.listen()


def Game(*args):
  global ongoing
  if ongoing==False:
    print("hello")
    Timer.reset()
    for i in ListOfObjects:
      i.goto(i.orgpos[0],i.orgpos[1])
  
  #screen.onkeypress(fun=Player.moveright, key="Right")
  #screen.onkeypress(fun=Player.moveleft, key="Left")
  #screen.onkeypress(fun=Player.moveup, key="Up")
  #screen.onkeypress(fun=Player.movedown, key="Down")
  #screen.onkeyrelease(fun=Player.releaseLeft, key="Left")
  #screen.onkeyrelease(fun=Player.releaseRight, key="Right")
  #screen.onkeyrelease(fun=Player.releaseUP, key="Up")
  #screen.onkeyrelease(fun=Player.releaseDown, key="Down")
  


    ongoing=True
    startTime= time.time()
    while True:
      Timer.writeTime(time.time() - startTime)
      for obj in ListOfObjects:
        for obj1 in ListOfObjects:
          if obj.distance(obj1)<40 and obj1!=obj:
            obj.yMove=-obj.yMove
            obj.xMove=-obj.xMove
          
        obj.move()
    
      time.sleep(.008)
      screen.update()
while 1:
  screen.onclick(fun = Game)
  Timer.write("Click to begin", font=("times new roman",52,"bold"))
  screen.mainloop()




