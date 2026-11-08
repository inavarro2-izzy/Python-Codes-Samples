# Israel Navarro
# November 8, 2026
# Problem 5: Draw five nested blue squares using turtle.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.title("Problem 5 - Nested Squares")
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)
alex.speed(5)

# Move to each square's bottom-left corner so they share a center.
for size in [30, 60, 90, 120, 150]:
    alex.penup()
    alex.goto(-size / 2, -size / 2)
    alex.setheading(0)
    alex.pendown()
    drawSquare(alex, size)

alex.penup()
alex.goto(-95, -95)
wn.exitonclick()
