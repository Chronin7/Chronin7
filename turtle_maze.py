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
def print_board(the_grid,t):
    for xpos,x in enumerate(the_grid):
        for ypos,y in enumerate(x):
            if y=="#":
                t.color("black")
                t.fillcolor("black")
                draw_rectangle(t,[-250+10*ypos,250-10*xpos],[-240+10*ypos,260-10*xpos],"black","black")    
def smooth(grid,t):
    temp_grid=copy.deepcopy(grid)
    branch=[]
    xpos=31
    ypos=50
    width=len(temp_grid[0])
    height=len(temp_grid)
    branch.append((xpos, ypos))
    while branch:
        xpos, ypos = branch[-1] 
        if temp_grid[xpos][ypos] != 'x':
            temp_grid[xpos][ypos] = "x"
        if ypos == 50:
            print_board(temp_grid,t)
            return True
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        found_path = False

        for dx, dy in moves:
            next_x, next_y = xpos + dx, ypos + dy

            # Check boundaries and if the next cell is a valid space ' '
            if 0 <= next_x < height and 0 <= next_y < height:
                if temp_grid[next_x][next_y] == " ":
                    branch.append((next_x, next_y))
                    found_path = True
                    break
        if not found_path:
            branch.pop() 
tur=turtle.Turtle()
while not smooth(unsmooth_maze,tur):
    unsmooth_maze=random_maze()
def up():
    global posy
    global unsmooth_maze
    if unsmooth_maze[posx][posy-1]==" ":
        posy-=1
def down():
    global posy
    global unsmooth_maze
    if unsmooth_maze[posx][posy+1]==" ":
        posy+=1
def left():
    global posx
    global unsmooth_maze
    if unsmooth_maze[posx-1][posy]==" ":
        posx-=1
def right():
    global posx
    global unsmooth_maze
    if unsmooth_maze[posx+1][posy]==" ":
        posx+=1
screen.update()
posx=31
posy=50
button(-350,-350,-300,-300,"up",up,[],"black","red","black")
button(-350,-400,-300,-350,"down",down,[],"black","yellow","black")
button(-400,-400,-350,-350,"left",left,[],"black","green","black")
button(-250,-400,-300,-350,"right",right,[],"black","blue","black")
turtle.done()
while posx!=1 and posy!=50:
    screen.update()
    tur.goto(-250+10*posy,-250+10*(50-posx))
    