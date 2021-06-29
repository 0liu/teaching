# Project I. Drawing turtle
# Problem 3. Draw a 5 x 8 dot grid with a nested loop.

import turtle

# create a turtle 
bob = turtle.Turtle()

# define the shape of the grid
dot_distance = 20
width = 5
height = 8

# pen up so we don't draw when moving between dots
bob.penup()

for row in range(8):
    row_width = 0
    for col in range(5):
        bob.dot()
        bob.forward(dot_distance)
        row_width += dot_distance

    # go to the starting position of the current row
    bob.backward(row_width)

    # move to the beginning of the next row
    bob.right(90)
    bob.forward(dot_distance)
    bob.left(90)

# We're done!
turtle.done()
