# Name: Israel Navarro
# Date: October 24, 2026
# Description: Ask for polygon settings, then draw and fill a regular polygon.

import turtle

# Get the polygon settings from the user.
while True:
    try:
        sides = int(input("Number of sides (3 or more): "))
        length = float(input("Length of each side (positive number): "))
        if sides >= 3 and length > 0:
            break
        print("Please enter at least 3 sides and a positive length.")
    except ValueError:
        print("Please enter valid numbers.")

line_color = input("Line color (for example, black): ").strip() or "black"
fill_color = input("Fill color (for example, blue): ").strip() or "blue"

# Draw a closed regular polygon, turning by its exterior angle.
screen = turtle.Screen()
screen.title("Regular Polygon")
pen = turtle.Turtle()
try:
    pen.pencolor(line_color)
    pen.fillcolor(fill_color)
except turtle.TurtleGraphicsError:
    print("Invalid color entered. Using black and blue.")
    pen.pencolor("black")
    pen.fillcolor("blue")
pen.pensize(3)
pen.begin_fill()
for side in range(sides):
    pen.forward(length)
    pen.left(360 / sides)
pen.end_fill()
pen.hideturtle()
screen.exitonclick()
