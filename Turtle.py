# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 02:35:11 2023

@author: abduqodir
"""
from turtle import Turtle, Screen
oyna=Screen()
oyna.title("mening oynam")

chiziq=Turtle()
chiziq.color("red")
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()

chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

ramka=Turtle()
ramka.color('blue')
ramka.pensize(5)
ramka.speed(0)
ramka.hideturtle()


ramka.up()
# ramka.goto(0, 0)
ramka.goto(0, -300)
ramka.down()
ramka.goto(-200, -300)
ramka.goto(-200, -250)
ramka.goto(0, -250)
ramka.goto(0, -300)

koptok=Turtle()
koptok.shape('circle')
koptok.color('black')
koptok.shapesize(0.7)

koptok.up()
koptok.goto(0, 0)
step_x=3
step_y=2
while True:
    x, y=koptok.position()
    if x+step_x>=300 or x+step_x<=-300:
        step_x=-step_x
    if y+step_y>=300 or y+step_y<=-300:
        step_y=-step_y
        
    koptok.goto(x+step_x, y+step_y)
    
    x1=x+step_x
    y1=y+step_y
    if x1<=-250 and y1<=-250:
        continue
    if x1<=0 and y1<-250:
        break
    
    


oyna.mainloop()




