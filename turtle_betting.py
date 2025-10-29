import turtle, math, random

# --- Global Variables ---
buttons = []
bet_buttons = []
amount = [0, 0, 0, 0, 0]
balence = 100
turtle_names = ["jeff", "bob", "shelstey", "clang", "valery"]
screen = turtle.Screen()

# --- Screen Setup ---
screen.setup(width=1000, height=1000)
screen.title("turtle betting game")
screen.tracer(0)

# --- Race Functions ---
def update_bet_buttons():
    """Updates the text on all bet buttons."""
    global amount
    for i, b in enumerate(bet_buttons):
        b.update_text(f"bet:{amount[i]}")
    # Also display balance and other information
    ref_2.clear()
    ref_2.penup()
    ref_2.goto(-480, -480)
    ref_2.color("black")
    ref_2.write(f"Balance: {balence}", font=("Arial", 16, "bold"))
    screen.update()

def start_race():
    global contestant_1, contestant_2, contestant_3, contestant_4, contestant_5
    global amount, balence
    finish = 400
    
    # Lift pens to prevent drawing before the race
    contestant_1.penup()
    contestant_2.penup()
    contestant_3.penup()
    contestant_4.penup()
    contestant_5.penup()
    
    # Move turtles back to start
    reset()

    # Place pens down for the race
    contestant_1.pendown()
    contestant_2.pendown()
    contestant_3.pendown()
    contestant_4.pendown()
    contestant_5.pendown()
    
    while contestant_1.xcor() < finish and contestant_2.xcor() < finish and \
          contestant_3.xcor() < finish and contestant_4.xcor() < finish and \
          contestant_5.xcor() < finish:
        contestant_1.forward(random.uniform(5, 20))
        contestant_2.forward(random.uniform(5, 20))
        contestant_3.forward(random.uniform(5, 20))
        contestant_4.forward(random.uniform(5, 20))
        contestant_5.forward(random.uniform(5, 20))
        screen.update()

    if contestant_1.xcor() > finish:
        balence += amount[0] * 2
    if contestant_2.xcor() > finish:
        balence += amount[1] * 2
    if contestant_3.xcor() > finish:
        balence += amount[2] * 2
    if contestant_4.xcor() > finish:
        balence += amount[3] * 2
    if contestant_5.xcor() > finish:
        balence += amount[4] * 2
        
    amount = [0, 0, 0, 0, 0]
    update_bet_buttons()

def reset():
    global contestant_1, contestant_2, contestant_3, contestant_4, contestant_5
    contestant_1.clear()
    contestant_2.clear()
    contestant_3.clear()
    contestant_4.clear()
    contestant_5.clear()
    
    contestant_1.penup()
    contestant_1.goto(-400, 400)
    contestant_2.penup()
    contestant_2.goto(-400, 300)
    contestant_3.penup()
    contestant_3.goto(-400, 200)
    contestant_4.penup()
    contestant_4.goto(-400, 100)
    contestant_5.penup()
    contestant_5.goto(-400, 0)
    screen.update()

# --- Button Handlers ---
def global_click_handler(x, y):
    """Checks all buttons to see if they were clicked."""
    for b in buttons:
        if b.is_clicked(x, y):
            b.on_click()

def get_valid_type(type_return, prompt, invalid_prompt="Invalid input. Please try again.", valid=None):
    while True:
        try:
            to_return = type_return(screen.textinput(title="Place Bet", prompt=prompt))
            if valid is not None:
                return to_return
            if isinstance(valid, tuple):
                if valid[0] <= to_return <= valid[1]:
                    return to_return
                else:
                    screen.textinput("Invalid Amount", f"Input must be between {valid[0]} and {valid[1]}.")
            elif isinstance(valid, list):
                if to_return in valid:
                    return to_return
                else:
                    screen.textinput("Invalid Input", f"Input must be one of: {valid}.")
            else:
                return to_return
        except ValueError:
            screen.textinput("Invalid Input", invalid_prompt)

def bet(turtle_num):
    global amount, balence
    new_bet = get_valid_type(int, f"how much do you want to bet on {turtle_names[turtle_num]}? \n Current bet: {amount} \n Current balance: {balence} amount to bet: ","ether invalid amount or invalid input", (0, balence))
    balence -= new_bet - amount[turtle_num]
    amount[turtle_num] = new_bet
    update_bet_buttons()

# --- Drawing Utilities ---
def draw_rectangle(t, bl_cord, tr_cord, pen_color="black", fill_color=""):
    t.color(pen_color, fill_color)
    if fill_color:
        t.begin_fill()
    t.penup()
    t.goto(bl_cord[0], bl_cord[1])
    t.pendown()
    t.goto(bl_cord[0], tr_cord[1])
    t.goto(tr_cord[0], tr_cord[1])
    t.goto(tr_cord[0], bl_cord[1])
    t.goto(bl_cord[0], bl_cord[1])
    if fill_color:
        t.end_fill()

def ref_checkers(square_size, x, y, xo, yo):
    x_size = x
    y_size = y
    y_ofset = yo
    x_ofset = xo

    for i in range(y_ofset, y_size + y_ofset):
        for j in range(x_ofset, x_size + x_ofset):
            x1 = j * square_size
            y1 = i * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            if (i + j) % 2 == 0:
                fill = "black"
            else:
                fill = "white"
            draw_rectangle(ref_1, [x1, y1], [x2, y2], "black", fill)

# --- Button Class ---
class button:
    def __init__(self, x1, y1, x2, y2, text, on_click_function, peramaters, pen_color="black", fill_color="black", text_color="white", font_size=12, font="Arial", font_type="normal"):
        self.button_turtle = turtle.Turtle()
        self.button_turtle.hideturtle()
        self.text_turtle = turtle.Turtle()
        self.text_turtle.hideturtle()
        self.cords = [x1, y1, x2, y2]
        self.on_click_function = on_click_function
        self.perams = peramaters
        self.text_color = text_color
        self.font_size = font_size
        self.font = font
        self.font_type = font_type
        
        draw_rectangle(self.button_turtle, [x1, y1], [x2, y2], pen_color, fill_color)
        
        self.center_x = (x1 + x2) / 2
        self.center_y = (y1 + y2) / 2
        self.text_y_position = self.center_y - (font_size / 2) - 3
        
        self.update_text(text)

    def is_clicked(self, x, y):
        x1, y1, x2, y2 = self.cords
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        return min_x <= x <= max_x and min_y <= y <= max_y

    def on_click(self):
        self.on_click_function(*self.perams)

    def update_text(self, new_text):
        self.text_turtle.clear()
        self.text_turtle.penup()
        self.text_turtle.goto(self.center_x, self.text_y_position)
        self.text_turtle.color(self.text_color)
        self.text_turtle.write(new_text, align="center", font=(self.font, self.font_size, self.font_type))

# --- Game Setup ---
ref_1 = turtle.Turtle()
ref_1.hideturtle()
ref_2 = turtle.Turtle()
ref_2.hideturtle()
contestant_1 = turtle.Turtle()
contestant_2 = turtle.Turtle()
contestant_3 = turtle.Turtle()
contestant_4 = turtle.Turtle()
contestant_5 = turtle.Turtle()

# Draw racetrack
ref_1.shape('turtle')
ref_1.color(.5, .5, .5)
ref_1.speed(0)
ref_1.penup()
ref_1.goto(-500, -50)
ref_1.pendown()
ref_1.goto(500, -50)
ref_1.goto(500, 450)
ref_1.goto(-500, 450)
ref_1.goto(-500, -50)
ref_1.penup()

# Draw track lines
for y_pos in range(50, 451, 100):
    ref_1.penup()
    ref_1.goto(-500, y_pos)
    ref_1.pendown()
    ref_1.goto(500, y_pos)

# Create buttons
bet_buttons.append(button(-300,-300,-250,-250,f"bet:{amount[0]}",bet,[0],"black","red"))
bet_buttons.append(button(-225,-300,-175,-250,f"bet:{amount[1]}",bet,[1],"black","green"))
bet_buttons.append(button(-150,-300,-100,-250,f"bet:{amount[2]}",bet,[2],"black","blue"))
bet_buttons.append(button(-75,-300,-25,-250,f"bet:{amount[3]}",bet,[3],"black","yellow"))
bet_buttons.append(button(0,-300,50,-250,f"bet:{amount[4]}",bet,[4],"black","cyan"))

buttons.extend(bet_buttons)

start_button = button(-50,-400,100,-350,"start",start_race,[],"green","green")
buttons.append(start_button)

reset_button = button(-50,-450,100,-400,"reset",reset,[],"red","red")
buttons.append(reset_button)

# Finish line
ref_1.penup()
ref_1.color("red")
ref_1.goto(400, -50)
ref_1.pendown()
ref_1.goto(400, 450)

# Configure contestants
contestant_1.shape('turtle')
contestant_2.shape('turtle')
contestant_3.shape('turtle')
contestant_4.shape('turtle')
contestant_5.shape('turtle')
contestant_1.color(1, 0, 0)
contestant_2.color(0, 1, 0)
contestant_3.color(0, 0, 1)
contestant_4.color(1, 1, 0)
contestant_5.color(0, 1, 1)
contestant_1.penup()
contestant_2.penup()
contestant_3.penup()
contestant_4.penup()
contestant_5.penup()

contestant_1.goto(-400, 400)
contestant_2.goto(-400, 300)
contestant_3.goto(-400, 200)
contestant_4.goto(-400, 100)
contestant_5.goto(-400, 0)

# Show initial state
screen.tracer(1)
update_bet_buttons()

screen.onscreenclick(global_click_handler)
screen.mainloop()