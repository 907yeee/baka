# Import turtle package
import turtle
import time
# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text

def flatoval(r):
    turtle.right(45)
    turtle.fillcolor("yellow")   
    turtle.begin_fill()  
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/3,90)
    turtle.end_fill()  

# Draw a heart

heart()

# Write text

flatoval(40)
# To hide turtle

time.sleep(100)
pen.ht() 
