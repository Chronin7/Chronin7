import turtle

# Create a screen object
screen = turtle.Screen()

# Set up the screen size (width, height)
screen.setup(width=600, height=400)

# Set the window title
screen.title("My Turtle Drawing")

# Create a turtle object
my_turtle = turtle.Turtle()

# You can now start drawing with my_turtle
# For example:
# my_turtle.forward(100)

# Keep the window open until it's clicked
screen.exitonclick()