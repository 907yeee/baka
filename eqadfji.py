import turtle
def flatoval(r):
    turtle.right(45)
    turtle.fillcolor("yellow")   
    turtle.begin_fill()  
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/3,90)
        turtle.end_fill()  
flatoval(40)
