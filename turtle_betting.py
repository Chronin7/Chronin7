import turtle,math
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
def get_valid_type(type_return,prompt,invalid_prompt="invalid input try again",valid=None):
	to_return=None
	if valid is isinstance(valid,tuple):
		while valid[0]<to_return<valid[1]:
			try:
				to_return=int(input(prompt))
				if valid[0]<to_return<valid[1]:
					return to_return
				else:
					chr("3")
			except:
				print(invalid_prompt)
	if valid==None:
		while True:
			try:
				to_return=type_return(input(prompt))
				return to_return
			except:
				print(invalid_prompt)
	while to_return not in valid:
		try:
			to_return=type_return(input(prompt))
			break
		except:
			print(invalid_prompt)
	return to_return
amount=[0,0,0,0,0]
def bet(turtle_num):
	global amount
	global balence
	amount[turtle_num]=get_valid_type(int,f"how much do you want to bet on {["jeff","bob","shelstey","clang","valery"][turtle_num]} \n curent bet: {amount} \n curent ballence: {balence}","ether invalid amount or invalid input",(0,66125646655438184824034357503490176636099264991633465762201498014519123891859268733983653039388726432642995143358504569007771585986934024968669434028350416345702241180663304045682364832214940764929170988448662499142908799298664245623314794704849295304798107198075017717708753814435626352262734959756725609267280962722018526857388403754623314994104842572188601739700249377103859789493522946388742872159309483907924798646897590296799087138432035293041592297258616156208443607672462374144231313952523825412147224367895213575069108067843852391312126679152860656972235771923495366310698192918524201617510712807620967003175264646329092876562122951842146119916941895931718937037709622303904807519784876983985859485514354675809345820163038895549147316490316119029733685356457419092050823362333977133993758927393621966880365414110809808625711116204972494708604941468381375412202718800307572761434643952896448769099158664932122062500535504003852936733767015374683609607646579137867083807813238348719611910693255294339716425075))

balence=100
button1=button(1,1,101,101,"+",bet,[0])
buttons.append(button1) 

button1=button(1,1,101,101,"+",bet,[0])
buttons.append(button2) 

button1=button(1,1,101,101,"+",bet,[0])
buttons.append(button3) 

button1=button(1,1,101,101,"+",bet,[0])
buttons.append(button4) 

button1=button(1,1,101,101,"+",bet,[0])
buttons.append(button5) 
screen.onscreenclick(global_click_handler)
screen.mainloop()
