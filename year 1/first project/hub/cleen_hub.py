debuging = 1
hubo = 0
import time
import random
def type_text(te):
	for c in str(te):
		print(c, end = "", flush = True)
		time.sleep(random.uniform(.01,.1))
	print("")
def hub():
	while True:
		type_text("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		type_text("0 to stop")
		type_text("1 for calculator")
		type_text("2 for number game")
		type_text("3 for palindrome detector")
		type_text("4 for pig latin translator")
		type_text("5 for anagram maker")
		type_text("6 for averager")
		type_text("7 for temperature calculator")
		type_text("8 for area calculator")
		hubo = int(input("what do you want: "))
		if hubo == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			if hubo ==0:
				type_text("Goodby please come back soon! ##connection terminated by:Hubby##")
			time.sleep(1)
			quit()
		if hubo ==1:
			type_text("Ok sending you to Calcu.")
			time.sleep(1)
			import calculater
		elif hubo ==2:
			type_text("Ok sending you to Guessy.")
			time.sleep(1)
			import number_game
		elif hubo ==3:
			type_text("Ok sending you to Pally.")
			time.sleep(1)
			import paladrome
		elif hubo ==4:
			type_text("Ok sending you to Pig.")
			time.sleep(1)
			import pig
		elif hubo ==5:
			type_text("Ok sending you to Anny.")
			time.sleep(1)
			import anagram
		elif hubo ==6:
			type_text("Ok sending you to AV (she is a bit crazy).")
			import avrage
		elif hubo ==7:
			type_text("Ok sending you to Kelvin.")
			import temp_calculater_hub
		elif hubo ==8:
			type_text("Ok sending you to Arion.")
			import area_calculater
		elif hubo ==9:
			type_text("Sorry this option is not available yet.")
		elif hubo ==10:
			type_text("Sorry this option is not available yet.")
		elif hubo == 7232010:
			import code
		else:
			type_text("Sorry this option is not available yet.")
if debuging == 0:
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("connection successful")
	time.sleep(1)
	hub()
else:
	hub()