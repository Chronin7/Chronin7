import turtle,math,random
buttons = []
amount=[0,0,0,0,0]
screen = turtle.Screen()

screen.setup(width=1000, height=1000)

screen.title("turtle betting game")
screen.tracer(0)
def start_race():
	global contestant_1
	global contestant_2
	global contestant_3
	global contestant_4
	global contestant_5
	global amount
	global balence
	contestant_1.pendown()
	contestant_2.pendown()
	contestant_3.pendown()
	contestant_4.pendown()
	contestant_5.pendown()
	while contestant_1.xcor()<50 or contestant_2.xcor()<50 or contestant_3.xcor()<50 or contestant_4.xcor()<50 or contestant_5.xcor()<50:
		contestant_1.forward(random.uniform(0,5))
		contestant_2.forward(random.uniform(0,5))
		contestant_3.forward(random.uniform(0,5))
		contestant_4.forward(random.uniform(0,5))
		contestant_5.forward(random.uniform(0,5))
	if contestant_1.xcor()>50:
		balence+=amount[0]
	if contestant_2.xcor()>50:
		balence+=amount[1]
	if contestant_3.xcor()>50:
		balence+=amount[2]
	if contestant_4.xcor()>50:
		balence+=amount[3]
	if contestant_5.xcor()>50:
		balence+=amount[4]
def reset():
	global contestant_1
	global contestant_2
	global contestant_3
	global contestant_4
	global contestant_5
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
def get_valid_type(type_return, prompt, invalid_prompt="Invalid input. Please try again.", valid=None):
	while True:
		try:
			to_return = type_return(input(prompt))

			if valid is None:
				return to_return
			if isinstance(valid, tuple):
				if valid[0] <= to_return <= valid[1]:
					return to_return
				else:
					print(f"Input must be between {valid[0]} and {valid[1]}.")
			elif isinstance(valid, list):
				if to_return in valid:
					return to_return
				else:
					print(f"Input must be one of: {valid}.")
			else:
				return to_return
		except ValueError:
			print(invalid_prompt)
def bet(turtle_num):
	global amount
	global balence
	amount[turtle_num]=get_valid_type(int,f"how much do you want to bet on {["jeff","bob","shelstey","clang","valery"][turtle_num]} \n curent bet: {amount} \n curent ballence: {balence}","ether invalid amount or invalid input",(0,balence))
	balence-=amount[turtle_num]

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
	def __init__(self, x1, y1, x2, y2, text,on_click_function,peramaters, pen_color="black", fill_color="black", text_color="white", font_size=12, font="Arial", font_type="normal"):
		self.button_turtle = turtle.Turtle()
		self.button_turtle.hideturtle()
		self.cords = [[x1, y1], [x2, y2]]
		self.on_click_function=on_click_function
		self.perams=peramaters
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
		self.on_click_function(*self.perams)
def output_balance():
	global balence
	ref_1.clear()  # Clear previous text
	ref_1.write(f"Current Value: {my_variable}", align="center", font=("Arial", 16, "normal"))
	my_variable += 1  # Increment the variable
	ref_1.update()  # Update the screen
	ref_1.ontimer(output_balance, 100)
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
balence=100
button1=button(-300,-300,-250,-250,"+",bet,[0],"black","red")
buttons.append(button1) 

button2=button(-225,-300,-175,-250,"+",bet,[1],"black","green")
buttons.append(button2) 

button3=button(-150,-300,-100,-250,"+",bet,[2],"black","blue")
buttons.append(button3) 

button4=button(-75,-300,-25,-250,"+",bet,[3],"black","yellow")
buttons.append(button4) 

button5=button(0,-300,50,-250,"+",bet,[4],"black","cyan")
buttons.append(button5) 
start=button(-50,-400,100,-350,"+",start_race,[4],"green","green")
buttons.append(start) 
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




screen.onscreenclick(global_click_handler)
screen.mainloop()
