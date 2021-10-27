import turtle as t
import random as rand
import os

t.fillcolor("lavender")
t.begin_fill()
t.shapesize(15)
t.shape("square")
t.end_fill()

t.addshape("C:\Users\BRHS-PLTW-ST20\Documents\pictures") #u can make images in a new folder

myImage = t.Turtle()
myImage.speed(0) #so it will draw the image instantly
myImage.shape("C:\Users\BRHS-PLTW-ST20\Documents\pictures") #give your object the image
myImage.penup() #if you dont do this, it will draw a line
myImage.goto(0,0) #give your image a location

while True:
  wn.update() #update your window

wn = t.Screen()
wn.mainloop()
