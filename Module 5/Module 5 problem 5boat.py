
# Name: Israel Navarro
# Date: October 25, 2026
# Description: This program uses Python Turtle to
# draw a colorful sailboat on the water with
# a sun and clouds in the sky.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Sailboat on the Ocean")
screen.bgcolor("skyblue")
screen.setup(800, 600)

# Create the turtle
pen = turtle.Turtle()
pen.speed(6)
pen.pensize(3)

# Function to draw filled shapes
def draw_shape(points, color):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(point)

    pen.goto(points[0])
    pen.end_fill()

# Draw the blue ocean
draw_shape([
    (-400, -100),
    (400, -100),
    (400, -300),
    (-400, -300)
], "dodgerblue")

# Draw the boat's brown hull
draw_shape([
    (-180, -100),
    (180, -100),
    (120, -170),
    (-120, -170)
], "saddlebrown")

# Draw the boat mast
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.pencolor("black")
pen.pensize(6)
pen.goto(0, 190)

# Draw the large white sail
pen.pensize(3)
draw_shape([
    (-10, 175),
    (-10, -80),
    (-150, -80)
], "white")

# Draw the smaller red sail
draw_shape([
    (10, 160),
    (10, -80),
    (130, -80)
], "red")

# Draw the yellow sun
pen.penup()
pen.goto(270, 170)
pen.pendown()
pen.pencolor("orange")
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(45)
pen.end_fill()

# Draw sun rays using a loop
for i in range(8):
    pen.penup()
    pen.goto(270, 215)
    pen.setheading(i * 45)
    pen.forward(55)
    pen.pendown()
    pen.forward(20)

# Draw clouds using circles
pen.pencolor("white")
pen.fillcolor("white")

for x in [-280, -245, -210]:
    pen.penup()
    pen.goto(x, 170)
    pen.pendown()
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()

# Draw ocean waves using a loop
pen.pencolor("white")
pen.pensize(2)

for x in range(-350, 351, 100):
    pen.penup()
    pen.goto(x, -220)
    pen.pendown()
    pen.forward(45)

# Hide the turtle
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
