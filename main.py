import turtle
import random
import time,math

from turtle import Screen, Turtle
screen= Screen()
screen.tracer(False)
ongoing=False


screenWidth = 650
screenHeight = 650
screen.screensize(800,800,bg="black")
screen.setup(screenWidth, screenHeight)
ListOfObjects = []
ENEMYWID=1
avgdir=0
class Bomber(Turtle):
  def __init__(self,xpos,ypos,xSTRECH=1,ySTRECH=1,list= ListOfObjects):
    super().__init__()
    list.append(self)
    self.penup()
    self.orgpos=xpos,ypos
    self.shape("square")
    self.color("white")
    self.goto(xpos,ypos)
    self.shape("classic")
    self.shapesize(stretch_wid=ENEMYWID,stretch_len=ENEMYWID)
    self.dir= random.randint(0,360)
    self.yMove = 5*math.cos(self.dir)
    if self.yMove==0:
      self.yMove+=1
    self.xMove = 5*math.sin(self.dir)
    self.x=xpos
    self.y=ypos
    self.setheading(self.dir)
  def move(self):
    Alpha=False
    global screenWidth,screenHeight,avgdir
    print(screenWidth,screenHeight)
    self.xMove=math.cos(self.heading()*math.pi/360)*4
    self.ymove=math.sin(self.heading()*math.pi/360)*4
    if 270>self.heading()>90:
      self.xMove=-self.xMove
    if (self.xcor() > screenWidth/2  ) or ((screenWidth/2)*-1>self.xcor() ):
      Alpha=True
      self.dir=-2*self.heading()+180
      #self.xMove = self.xMove*-1
      if self.xcor()>screenWidth/2:
        self.setx(screenWidth/2)
      if self.xcor()<-screenWidth/2:
        self.setx(-screenWidth/2)

    if (self.ycor() > screenHeight/2 or (screenHeight/2)*-1>self.ycor()) :
      if self.ycor()>screenHeight/2:
        self.sety(screenHeight/2)
      if self.ycor()<-screenHeight:
        self.sety(-screenHeight/2)
      self.dir=-2*self.heading()+180
    #try:
     # self.dir= math.atan(self.yMove/self.xMove)
    #except:
    
    
    #if self.xMove<0:
     # self.dir=self.dir+math.pi
    self.setheading(self.dir)
    self.forward(8)
    #self.dir=self.dir+avgdir/50
    #self.x = self.xcor()+self.xMove
    #self.y = self.ycor()+self.yMove
    #self.goto(self.x,self.y)
    #print(self.dir)













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
list=[]
for i in range(6):
  list.append(Bomber(0,50*i))

screen.listen()


avgHeading=[0,0]
avgxMove=0
avgyMove=0
def Game(*args):
  global ongoing,avgyMove,avgxMove,avgdir
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
          if obj.distance(obj1)<25 and obj1!=obj:
            #obj.dir=-obj.dir
            pass



        avgxMove+=obj.xMove
        avgyMove+=obj.yMove  
        obj.move()
      avgyMove/=len(ListOfObjects)
      avgxMove/=len(ListOfObjects)
      avgdir= math.atan(avgyMove/avgxMove)
      #if avgxMove<0:
       # avgdir+=math.pi
      time.sleep(.005)
      
      screen.update()
while 1:
  screen.onclick(fun = Game)
  Timer.write("Click to begin", font=("times new roman",52,"bold"))
  screen.mainloop()




