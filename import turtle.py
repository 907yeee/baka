import turtle
import math
import time
turtle.speed(0)
turtle.shape("square")
turtle.goto(0,0)
turtle.lt(90)
turtle.fd(200)
turtle.goto(0,0)
turtle.bk(200)
turtle.goto(0,0)
turtle.rt(90)
turtle.fd(200)
turtle.goto(0,0)
turtle.lt(180)
turtle.fd(200)
turtle.goto(0,0)
turtle.write("0")
turtle.goto(0,30)
turtle.write("30")
turtle.goto(0,60)
turtle.write("60")
turtle.goto(0,90)
turtle.write("90")
turtle.goto(0,120)
turtle.write("120")
turtle.goto(0,150)
turtle.write("150")
turtle.goto(0,180)
turtle.write("180")
turtle.goto(0,0)
turtle.goto(30,0)
turtle.write("30")
turtle.goto(60,0)
turtle.write("60")
turtle.goto(90,0)
turtle.write("90")
turtle.goto(120,0)
turtle.write("120")
turtle.goto(150,0)
turtle.write("150")
turtle.goto(180,0)
turtle.write("180")
turtle.goto(0,0)
turtle.goto(-30,0)
turtle.write("-30")
turtle.goto(-60,0)
turtle.write("-60")
turtle.goto(-90,0)
turtle.write("-90")
turtle.goto(-120,0)
turtle.write("-120")
turtle.goto(-150,0)
turtle.write("-150")
turtle.goto(-180,0)
turtle.write("-180")
turtle.goto(0,0)
turtle.write("0")
turtle.goto(0,-30)
turtle.write("-30")
turtle.goto(0,-60)
turtle.write("-60")
turtle.goto(0,-90)
turtle.write("-90")
turtle.goto(0,-120)
turtle.write("-120")
turtle.goto(0,-150)
turtle.write("-150")
turtle.goto(0,-180)
turtle.write("-180")
turtle.home()
m=float(input("enter your slope"))
angle=math.atan(m)
b=float(input("enter your intercept"))
turtle.goto(0,b)
x=0
#while 1==1:
y=m*x+b
turtle.goto(x,y)
turtle.lt(angle)
turtle.fd(180)
turtle.rt(180)
turtle.fd(360)

time.sleep(100)