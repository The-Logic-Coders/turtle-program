import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the screen background
screen.bgpic("maze3.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-50, 205)
my_turtle.pendown()
my_turtle.pencolor("red")

# INSERT CODE HERE

turtle.done()