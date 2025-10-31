import turtle
import time
import itertools
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("turtle pit fractal animation with loop")
screen.colormode(255)
screen.bgcolor(100, 100, 100)
screen.tracer(0, 0)

# Global list to keep track of ALL turtles
all_turtles = []

# Global variables for fade steps and colors
FADE_STEPS = 255

def generate_fade_colors(start_rgb, end_rgb, steps):
    """Generates a list of RGB colors for a smooth transition."""
    fade_colors = []
    r1, g1, b1 = start_rgb
    r2, g2, b2 = end_rgb
    r_step = (r2 - r1) / steps
    g_step = (g2 - g1) / steps
    b_step = (b2 - b1) / steps
    for i in range(steps):
        r = int(r1 + r_step * i) # Ensure these are integers
        g = int(g1 + g_step * i) # Ensure these are integers
        b = int(b1 + b_step * i) # Ensure these are integers
        fade_colors.append((r, g, b))
    fade_colors.append(end_rgb)
    return fade_colors

SCOLORS = generate_fade_colors((0, 0, 0), (255, 255, 255), FADE_STEPS)
DCOLORS = generate_fade_colors((255, 255, 255), (0, 0, 0), FADE_STEPS)
current_step = 0
movement_speed = 0.5

def create_turtle_pair(color_s, color_d, pos, heading):
    """Helper function to create and configure a pair of turtles."""
    t_slave = turtle.Turtle()
    t_demon = turtle.Turtle()
    for t in [t_slave, t_demon]:
        t.speed(0)
        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()
    # Ensure colors passed here are also integers if they come from other functions
    t_slave.color(int(color_s[0]), int(color_s[1]), int(color_s[2]))
    t_demon.color(int(color_d[0]), int(color_d[1]), int(color_d[2]))
    all_turtles.append((t_slave, t_demon))
    return t_slave, t_demon

def generate_fractal(t_slave_base, t_demon_base, depth):
    if depth == 0:
        return
    
    angle_adjust1 = random.randint(-15, 15)
    angle_adjust2 = random.randint(-15, 15)
    
    # Ensure current color and pos are used when creating new turtles
    s_color = t_slave_base.color()
    d_color = t_demon_base.color()
    pos = t_slave_base.pos()
    heading = t_slave_base.heading()

    t_slave1, t_demon1 = create_turtle_pair(s_color[0], d_color[0], pos, heading + 30 + angle_adjust1) # Error was here
    t_slave2, t_demon2 = create_turtle_pair(s_color[0], d_color[0], pos, heading - 30 + angle_adjust2) # Error was here

    generate_fractal(t_slave1, t_demon1, depth - 1)
    generate_fractal(t_slave2, t_demon2, depth - 1)

def main_animation_loop():
    global current_step, movement_speed

    # Loop through ALL turtle pairs in the list
    for slave_t, demon_t in all_turtles:
        # Apply the same movement logic to every turtle
        slave_t.left(181)
        slave_t.forward(movement_speed)
        demon_t.right(181)
        demon_t.forward(movement_speed)

        # Update their colors based on the global fade cycle
        # The SCOLORS and DCOLORS lists already contain integers
        slave_t.color(SCOLORS[current_step])
        demon_t.color(DCOLORS[current_step])

    # Update global step variables
    current_step = (current_step + 1) % FADE_STEPS
    # movement_speed += 0.001

    # Update the screen once after all turtles have moved
    screen.update()

    # Periodically generate a new fractal from the first (original) turtle's location
    if random.randint(0, 200) == 1:
         # Use the first pair in the list to trigger the new branch
         generate_fractal(all_turtles[0][0], all_turtles[0][1], depth=255)

    # Schedule the next frame
    screen.ontimer(main_animation_loop, 10)

def batal():
    # Create the initial turtle pair at the start
    create_turtle_pair((255, 255, 255), (0, 0, 0), (0, 0), 0)
    
    # Start the continuous animation loop
    main_animation_loop()
    screen.exitonclick()

batal()