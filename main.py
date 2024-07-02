import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle named "spiral"
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest drawing speed

# Function to generate random colors
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# Draw a spiral pattern
for i in range(360):
    color = random_color()
    spiral.pencolor(color)
    spiral.width(i / 100 + 1)
    spiral.forward(i)
    spiral.right(59)

# Hide the turtle and display the window
spiral.hideturtle()
turtle.done()
