# Name: Samantha Lin
# Email: samantha.lin108@myhunter.cuny.edu
# 1 November 2023
# Program: pumpkin using turtle library

import turtle       # import turtle package/library
import time

window = turtle.Screen()    # opens screen for turtle drawing
window.bgcolor("black")     # background color

# drawing whole pumpkin - creates big orange dot
pumpkin = turtle.Turtle()   # instantiate turtle
pumpkin.hideturtle()        # hides drawing pen
pumpkin.color("orange")     # set color
pumpkin.dot(200)            # set dot size

# turtle will "carve" the pumpkin (the big orange dot)
carver = turtle.Turtle()

# "flatten" the lower part of the pumpkin
carver.penup()                  # move turtle without drawing lines
carver.setposition(-200, -110)  # place turtle at a particular set of coordinates
carver.pensize(50)              # set pen size
carver.pendown()                # move turtle with drawing lines
carver.forward(600)             # turtle move forward
carver.pensize(2)               # change pen size

# top part of pumpkin
carver.penup()
carver.setposition(-200, 107)
carver.pensize(50)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# stem of pumpkin
stem = turtle.Turtle()
stem.hideturtle()
stem.penup()
stem.setposition(-15,82)
stem.setheading(80)
stem.pensize(1)
stem.pendown()
stem.color("#7B3F00")
stem.fillcolor("#7B3F00")
stem.begin_fill()

stem.forward(40)
stem.right(95)
stem.forward(40)
stem.right(95)
stem.forward(31)
stem.right(70)
stem.forward(35)
stem.right(180)
stem.forward(35)
stem.end_fill()

# small leaf on stem
stem.color("#00B300")
stem.pensize(2)
stem.circle(40,70)

# initiate function
def carve_pumpkin(color):   # this function takes an argument
    carver.color(color)     # allows to choose what color the holes would be

    # make eyes
    # since making two eyes, it's easier to create a function to create an eye
    def make_eye(start, orientation):   # set input parameters
    # allows to fine tune where the drawing of the eye should start
    # and whether to start with the right eye or left eye
        carver.setheading(0)        # needs angle and turns turtle to head towards the angle
        carver.pensize(1)
        carver.penup()
        carver.setposition(*start)  # opens up the tuplet or list and puts its contents instead
        carver.pendown()
        carver.begin_fill()         # start filling up section
        carver.forward(orientation * 40)    # orientation either 1 or -1 to create symmetrical images
        carver.setheading(orientation * 135)
        carver.forward(orientation * 70)
        carver.end_fill()           # end filling up section

    make_eye((-50, 20), 1)  # left eye (start, orientation)
    make_eye((50, 20), -1)  # right eye (start, orientation)

    # make mouth
    carver.penup()
    carver.setposition(-50, -30)
    carver.setheading(45)
    carver.pendown()
    carver.pensize(1)
    carver.begin_fill()     # 'sandwich' code that draws a shape
                            # this shape is then filled in using the current color of the turtle
    for i in range(5):
        carver.forward(15)
        carver.right(90)    # turtle turn right
        carver.forward(15)
        carver.left(90)     # turtle turn left
    carver.setheading(260)
    carver.forward(20)
    carver.setheading(180)
    carver.forward(99)
    carver.end_fill()

    # make nose
    carver.penup()
    carver.setposition(0, 0)
    carver.setheading(90)
    carver.shape("triangle")    # changes shape of the drawing pen on the screen
    carver.stamp()              # creates permanent copy (or stamp) of the turtle

carve_pumpkin("#000000")    # color set to BLACK

# write text on animation
text = turtle.Turtle()
text.color('orange')
text.penup()
text.sety(155)              # this method only sets the y-coordinate
# this method takes a font parameter which allows you to customize how the text looks
style = ('Times New Roman', 55, 'bold')
text.write('Happy Halloween!', font=style, align='center')
text.hideturtle()

window.tracer(0)        # use on Screen object
                        # allows to draw shapes instantly and not have to wait for the turtle to make its way across the screen

# use time module
start = time.time() # start timer which resets every one second
count = 0
colors = "yellow", "black"      # tuple (alternate colors and use colors to call carve_pumpkin(color))
while True:
    if time.time() - start > 1:
        carve_pumpkin(colors[count % 2])        # returns the remainder
                                                # checks whether count is even or odd
                                                # allows to swap between yellow and black and again
        window.update() # use on Screen object
        count += 1
        start = time.time()     # reset timer

turtle.done()
