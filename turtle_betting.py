import turtle
buttons = []
screen = turtle.Screen()

screen.setup(width=1000, height=1000)

screen.title("turtle betting game")
screen.tracer(0)
def draw_rectangle(t,bl_cord,tr_cord,pen_color="black", fill_color=""):
	t.color(pen_color, fill_color)
	if fill_color:
		t.begin_fill()
	t.teleport(bl_cord[0],bl_cord[1])
	t.goto(bl_cord[0],tr_cord[1])
	t.goto(tr_cord[0],tr_cord[1])
	t.goto(tr_cord[0],bl_cord[1])
	t.goto(bl_cord[0],bl_cord[1])
	if fill_color:
		t.end_fill()
def ref_checkers(square_size,x,y,xo,yo):
	x_sixe=x
	y_size=y
	y_ofset=yo
	x_ofset=xo

	for i in range(y_ofset,y_size+y_ofset):
		for j in range(x_ofset,x_sixe+x_ofset):
			x1 = j * square_size
			y1 = i * square_size
			x2 = x1 + square_size
			y2 = y1 + square_size
			if (i + j) % 2 == 0:
				fill = "black"
			else:
				fill = "white"
			draw_rectangle(ref_1,[x1, y1],[x2, y2],"black",fill)
class button:
	def __init__(self, x1, y1, x2, y2, text, pen_color="black", fill_color="black", text_color="white", font_size=12, font="Arial", font_type="normal"):
		self.button_turtle = turtle.Turtle()
		self.button_turtle.hideturtle()
		self.cords = [[x1, y1], [x2, y2]]
		draw_rectangle(self.button_turtle, self.cords[0], self.cords[1], pen_color, fill_color)
		self.button_turtle.color(text_color)
		center_x = (x1 + x2) / 2
		center_y = (y1 + y2) / 2
		text_y_position = center_y - (font_size / 2) - 3
		self.button_turtle.penup()
		self.button_turtle.goto(center_x, text_y_position)
		self.button_turtle.write(text, align="center", font=(font, font_size, font_type))
	def is_clicked(self, x, y):
		x1, y1 = self.cords[0]
		x2, y2 = self.cords[1]
		min_x = min(x1, x2)
		max_x = max(x1, x2)
		min_y = min(y1, y2)
		max_y = max(y1, y2)
		return min_x <= x <= max_x and min_y <= y <= max_y
	def on_click(self):
		print("test")
button1=button(1,1,101,101,"hi")
buttons.append(button1) 
ref_1=turtle.Turtle()
ref_1.hideturtle()
contestant_1 = turtle.Turtle()
contestant_2 = turtle.Turtle()
contestant_3 = turtle.Turtle()
contestant_4 = turtle.Turtle()
contestant_5 = turtle.Turtle()
ref_1.shape('turtle')
ref_1.color(.5,.5,.5)
ref_1.speed(0)
ref_1.teleport(-500,-50)
ref_1.goto(500,-50)
ref_1.goto(500,50)
ref_1.goto(-500,50)
ref_1.goto(-500,150)
ref_1.goto(500,150)
ref_1.goto(-500,150)
ref_1.goto(-500,150)
ref_1.goto(-500,250)
ref_1.goto(500,250)
ref_1.goto(-500,250)
ref_1.goto(-500,250)
ref_1.goto(-500,350)
ref_1.goto(500,350)
ref_1.goto(-500,350)
ref_1.goto(-500,350)
ref_1.goto(-500,450)
ref_1.goto(500,450)
ref_1.goto(-500,450)
ref_1.goto(-500,450)
ref_1.end_poly()
ref_checkers(10,4,3,40,-10)
tempx=400
tempy=-150
ref_1.teleport(tempx,tempy)
ref_1.goto(tempx,tempy+50)
ref_checkers(10,2,50,42,-5)
screen.tracer(1)
contestant_1.shape('turtle')
contestant_2.shape('turtle')
contestant_3.shape('turtle')
contestant_4.shape('turtle')
contestant_5.shape('turtle')
contestant_1.color(1,0,0)
contestant_2.color(0,1,0)
contestant_3.color(0,0,1)
contestant_4.color(1,1,0)
contestant_5.color(0,1,1)
contestant_1.penup()
contestant_1.goto(-400,400)
contestant_2.penup()
contestant_2.goto(-400,300)
contestant_3.penup()
contestant_3.goto(-400,200)
contestant_4.penup()
contestant_4.goto(-400,100)
contestant_5.penup()
contestant_5.goto(-400,0)


def global_click_handler(x, y):
	"""Checks all buttons to see if they were clicked."""
	for b in buttons:
		if b.is_clicked(x, y):
			b.on_click()
screen.onscreenclick(global_click_handler)
screen.mainloop()
