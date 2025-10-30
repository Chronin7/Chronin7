import turtle
import time
import itertools

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("turtle pit")
turtle_slave = turtle.Turtle()
screen.colormode(255)
screen.bgcolor(0,0,0)
# Speed up the drawing animation
turtle_slave.speed(0)
screen.tracer(0, 0) # The second argument controls update delay, 0 means no delay

size = 100

def generate_fade_colors(start_rgb, end_rgb, steps):
    """
    Generates a list of RGB colors for a smooth transition.
    
    Args:
        start_rgb (tuple): The starting color (e.g., (255, 0, 0)).
        end_rgb (tuple): The ending color (e.g., (0, 255, 0)).
        steps (int): The number of steps in the transition.
        
    Returns:
        list: A list of RGB color tuples.
    """
    fade_colors = []
    
    # Unpack the start and end RGB tuples
    r1, g1, b1 = start_rgb
    r2, g2, b2 = end_rgb
    
    # Calculate the change per step for each component
    r_step = (r2 - r1) / steps
    g_step = (g2 - g1) / steps
    b_step = (b2 - b1) / steps
    
    for i in range(steps):
        r = int(r1 + r_step * i)
        g = int(g1 + g_step * i)
        b = int(b1 + b_step * i)
        fade_colors.append((r, g, b))
    
    # Add the final color to ensure the transition is complete
    fade_colors.append(end_rgb)
    return fade_colors

# The sequence of pure colors to fade between
color_stops = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_cycle = itertools.cycle(color_stops)

# Start with the first color
current_color = next(color_cycle)
next_color = next(color_cycle)

# Main drawing loop
step = 0
while True:
    # Generate the list of colors for the fade effect
    fade_steps = 255
    colors = generate_fade_colors(current_color, next_color, fade_steps)

    for color in colors:
        step += 1
        turtle_slave.left(181)
        turtle_slave.forward(step)
        turtle_slave.color(color)
        screen.update()

    # Move to the next transition
    current_color = next_color
    next_color = next(color_cycle)