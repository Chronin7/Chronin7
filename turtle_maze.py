import turtle
import util_functions
import random
import copy
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
    board=[]
    board.append(["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"])
    for x in range(0,50):
        board1=["#"]
        for y in range(0,50):
            if random.randint(0,3)==3:
                board1.append("#")
            else:
                board1.append(" ")
        board1.append("#")
        board.append(board1)
    board.append(["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"])
    board.append(["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"])
    return board
unsmooth_maze=random_maze()
print(["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"].index(" "))
def print_board(the_grid):
    for x in the_grid:
        for y in x:
            print(y,end="")
        print()
def smooth(grid):
    temp_grid=copy.deepcopy(grid)
    branch=[]
    xpos=31
    ypos=50
    while True:
        temp_grid[xpos][ypos]="x"
        print_board(temp_grid)
        up=(temp_grid[xpos][ypos-1],xpos,ypos-1,True if temp_grid[xpos][ypos-1]==" " else False)
        down=(temp_grid[xpos][ypos+1],xpos,ypos+1,True if temp_grid[xpos][ypos+1]==" " else False)
        left=(temp_grid[xpos-1][ypos],xpos-1,ypos,True if temp_grid[xpos-1][ypos]==" " else False)
        right=(temp_grid[xpos+1][ypos],xpos+1,ypos,True if temp_grid[xpos+1][ypos]==" " else False)
        if up[3]:
            branch.append(up)
        if down[3]:
            branch.append(down)
        if left[3]:
            branch.append(left)
        if right[3]:
            branch.append(right)
        xpos=branch[0][1]
        ypos=branch[0][2]
        temp_grid[xpos][ypos]="x"
        print_board(temp_grid)
        branch.pop()
        print_board(temp_grid)
smooth(unsmooth_maze)