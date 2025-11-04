import turtle
import util_functions
import random
import copy
screen = turtle.Screen()
screen.tracer(0)
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
def random_maze():
    t=turtle.Turtle()
    ofset=20
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.goto(0,ofset*20)
    t.goto(ofset*19,ofset*20)
    t.penup()
    t.goto(ofset*20,ofset*20)
    t.pendown()
    t.goto(ofset*20,0)
    t.goto(ofset,0)
    t.penup()
    maze=[
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
    for x in range(1,21):
        for y in range(1,21):
            if random.randint(1,2)==1:
                t.goto(x*ofset,y*ofset)
                t.pendown()
                t.goto(x*ofset,y*ofset-ofset)
                t.penup()
    for x in range(1,21):
        for y in range(1,21):
            if random.randint(1,2)==1:
                t.goto(x*ofset,y*ofset)
                t.pendown()
                t.goto(x*ofset-ofset,y*ofset)
                t.penup()

random_maze()
turtle.done()