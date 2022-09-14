import turtle

from turtle import *

c=0
d=0
e=0
f=0
while(c<400):
    forward(500)
    left(90)
    c+=100
penup()
goto(0,100)
pendown()
while(d<4):
    forward(500)
    left(180)
    forward(500)
    right(90)
    forward(100)
    right(90)
    d+=1
penup()
goto(100,0)
pendown()
left(90)
while(e<2):
    forward(500)
    right(90)
    forward(100)
    right(90)
    e+=1
penup()
goto(300,0)
pendown()
while(f<2):
    forward(500)
    right(90)
    forward(100)
    right(90)
    f+=1
    
