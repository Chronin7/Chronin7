
import time
import random
def type_text(text):
	for x in text:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,1.0))
	print("")
type_text("Hi i am Arion. I am a area finder")
while True:
	e = 1
	type_text("1 for rectangle")
	type_text("2 for square")
	type_text("3 for triangle")
	type_text("4 for circle")
	type_text("5 for trapezoid")
	shape = int(input("what do you want or type stop to stop: "))
	if shape == "1":
		#square/rectangle
		type_text("ok input the numbers that you want")
		a = int(input("what is the hight (only numbers please): "))
		b = int(input("what is the length (only numbers please): "))
		type_text(f"when the hight is {a} and the length is {b} the area is {a*b}.")
		e = 0
	if shape == "4":
		#circle
		type_text("ok input the numbers that you want")
		e = 0
		a = int(input("what is the hight (only numbers please): "))
		type_text(f"when the radius is {a} the area is {3.141592653589793238462643383279*a^2}")
	if shape == "3":
		#triangle
		type_text("ok input the numbers that you want")
		e = 0
		a = int(input("what is the hight (only numbers please): "))
		b = int(input("what is the length (only numbers please): "))
		type_text(f"when the hight is {a} and the length is {b} the area is {(a*b)*(1/2)}.")
	if shape == "5":
		#trapezoid
		type_text("ok input the numbers that you want")
		e = 0
		a = int(input("what is the hight (only numbers please): "))
		b = int(input("what is the top (only numbers please): "))
		c = int(input("what is the bottom (only numbers please): "))
		type_text(f"when the hight is {a} and the bottom is {b} and the top is {c} the area is {((b+c)/2)*a}.")
	if shape == "2":
		type_text("ok input the numbers that you want")
		e = 0
		a = int(input("what is the length of one of the sides (only numbers please): "))
		type_text(f"when the hight is {a} and the length is {b} the area is {a*2}.")
		e = 0
	if shape == "6":
		type_text("sorry coming soon")
		e = 0
	if shape == "7":
		type_text("sorry coming soon")
		e = 0
	if shape == "8":
		type_text("sorry coming soon")
		e = 0
	if shape == "9":
		type_text("sorry coming soon")
		e = 0
	if shape == "10":
		type_text("sorry coming soon")
		e = 0
	if shape == "11":
		type_text("sorry coming soon")
		e = 0
	if shape == "12":
		type_text("sorry coming soon")
		e = 0
	if shape == "13":
		type_text("sorry coming soon")
		e = 0
	if shape == "14":
		type_text("sorry coming soon")
		e = 0
	if shape == "15":
		type_text("sorry coming soon")
		e = 0
	if shape == "16":
		type_text("sorry coming soon")
		e = 0
	if shape == "17":
		type_text("sorry coming soon")
		e = 0
	if shape == "18":
		type_text("sorry coming soon")
		e = 0
	if shape == "19":
		type_text("sorry coming soon")
		e = 0
	if shape == "20":
		type_text("sorry coming soon")
		e = 0
	if shape == "stop":
		type_text("ok sending you back to Hubby")
		break
	else:
		type_text("sorry coming soon")
		e = 0
	if e == 1:
		type_text("sorry i didn't understand")
		e = 1
