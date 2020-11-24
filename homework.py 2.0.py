from turtle import *
from random import *

screen = Screen()
screen.bgcolor("pink")
screen.setup(600,600)

speed(10)
penup()
goto(-140,140)

color("#cf7072")
for track in range(16):
    write(track, align="center")
    right(90)
    forward(10)
    pendown()
    forward(290)
    penup()
    backward(300)
    left(90)
    forward(20)



valentina = Turtle()
valentina.color("#cf70c9")
valentina.shape("turtle")

valentina.penup()
valentina.goto(-160,100)
valentina.down()
 
tuba= Turtle()
tuba.color("#7076cf")
tuba.shape("turtle")

tuba.penup()
tuba.goto(-160,50)
tuba.down()

tango = Turtle()
tango.color("#70cfbf")
tango.shape("turtle")

tango.penup()
tango.goto(-160,0)
tango.down()
    
tushca = Turtle()
tushca.color("#b1cf70")
tushca.shape("turtle")

tushca.penup()
tushca.goto(-160,-50)
tushca.down()

lego = Turtle()
lego.color("blue")
lego.shape("turtle")

lego.penup()
lego.goto(-160,-100)
lego.down()

    
speed(1)

for running in range(53):
   valentina.forward(randint(0,25))
   tuba.forward(randint(0,25))
   tango.forward(randint(0,25))
   tushca.forward(randint(0,25))
   lego.forward(randint(0,25))
