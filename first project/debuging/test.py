import random
#cruintly broken
import time
turn = ""
runhub = True
debuging = 1
invertedP = ""
iterationP = 1
runnerP = ""
var = 0
hubo = 0
operation = 0
easterEggCount = 2
maxGuessCount = 20
minGuess = 1
maxGuess = 100
playCount = 0
playAgain = True
debuging = True
typing = False
type_speed = .01
player_score = 0
com_score = 0
def display_intro():
	type_text("Welcome to the Mystic Forest Adventure! i am The DM")
	type_text("You find yourself at the edge of a dark, mysterious forest.")
	type_text("Your goal is to find the hidden treasure and escape safely.")
def make_choice(options):
	for i,option in enumerate(options,1):
		type_text(f"{i}. {option}")
	while True:
		try:
			choice=int(input("Enter your choice: "))
			if 1<=choice<=len(options):
				return choice
			else:
				type_text("Invalid choice. Try again.")
		except ValueError:
			type_text("Please enter a number.")
def explore_forest():
	type_text("You venture deeper into the forest...")
	events=["You encounter a friendly woodland creature.","You find a shimmering portal.","You discover an ancient ruins.","You come across a bubbling stream."]
	type_text(random.choice(events))
def find_treasure():
	type_text("Congratulations! You've found the hidden treasure!")
	type_text("It's a chest filled with gold coins and magical artifacts.")
def face_challenge():
	type_text("Oh no! You've encountered a challenge!")
	challenges=["A giant spider blocks your path.","A riddle-speaking owl demands an answer.","A magical barrier requires a spell to pass."]
	type_text(random.choice(challenges))
	if random.random()<0.5:
		type_text("You successfully overcome the challenge!")
		return True
	else:
		type_text("You fail to overcome the challenge.")
		return False
def play_gamre():
	display_intro()
	treasure_found=False
	while not treasure_found:
		type_text("\nWhat would you like to do?")
		choice=make_choice(["Explore the forest","Search for treasure","Face a challenge","Exit the forest"])
		if choice==1:
			explore_forest()
		elif choice==2:
			if random.random()<0.3:
				find_treasure()
				treasure_found=True
			else:
				type_text("No treasure here. Keep searching!")
		elif type_text==3:
			if face_challenge():
				if random.random()<0.4:
					find_treasure()
					treasure_found=True
		elif choice==4:
			type_text("You decide to leave the forest. Game over!")
			return
	if treasure_found:
		type_text("Congratulations! You've won the game!")
def dwane_the_rock():
	player_score = 0
	com_score = 0
	type_text("The Rock wlcomes you to play Rock Paper Scissors")
	while True:
		type_text("1 for rock")
		type_text("2 for scissors")
		type_text("3 for paper")
		type_text("4 to quit")
		com_move = str(random.randint(1,3))
		if com_move == "1":
			com_prin = "🪨"
		if com_move == "2":
			com_prin = "✂️"
		if com_move == "3":
			com_prin = "📄"
		while True:
			players_move = input("The Rock asks what do you want:")
			if check_input(players_move,["1","2","3","4"]) == True:
				break
			else:
				type_text("The Rock dos'nt think that that is a valid input")
		if players_move == "1":
			players_move = "🪨"
		elif players_move == "2":
			players_move = "✂️"
		elif players_move == "3":
			players_move = "📄"
		elif players_move == "4":
			type_text("The Rock will send you back to the hub.")
			return
		print(f"The Rock: {com_prin} Player: {players_move}")

		if players_move == com_prin:
			type_text("The Rock is disaponted")
		elif players_move == "🪨" and com_prin == "✂️" or players_move == "✂️" and com_prin == "📄" or players_move == "📄" and com_prin == "🪨":
			type_text("how did you beat The Rock? The Rock will crush you.")
			player_score +=1
		else:
			type_text("HAHAHAHA The Rock wins once again")
			com_score += 1
		print(f"The Rock: {com_score} player: {player_score}")
def check_input(input,valid_inputs):
	if input  in  valid_inputs:
		return input
	return ""
def check_int(input):
	try:
		return int(input)
	except ValueError:
		type_text("please enter a number")
	return ""
def check_float(input):
	try:
		return float(input)
	except ValueError:
		type_text("not a valid input")
		return""
def type_text(textt):
	if typing != False:
		for x in textt:
			print(x, end = "", flush = True)
			time.sleep(random.uniform(.01,type_speed))
		print("")
	else:
		print(textt, flush= True)
def anagram():
	type_text("Hi i am Anny")
	while True:
		anagramt = []
		outputt = ""
		doitt = "12345"
		wordt = input("what is the word that you want into anagram or type stop to stop: ")
		if wordt == "stop":
			type_text("sending you back to Hubby")
			break
		if wordt == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			randt = len(wordt)
			for y in doitt:
				outputt = ""
				anagramt = []
				for x in wordt:
					anagramt.insert(random.randint(1,randt),x)
				for i in anagramt:
					outputt = outputt + i
				print (outputt)
def calculator():
		operation = 0
		a = "n/a"
		b = "n/a"
		type_text("Hi this is Calcu. What do you want me to calculate today")
		operation = 0
		while True:
			type_text("0 to stop")
			type_text("1 for division")
			type_text("2 for multiplication")
			type_text("3 for subtraction")
			type_text("4 for addition")
			type_text("5 for modulo")
			type_text("6 for factoring")
			operation = input("what do you want: ")
			if operation == "1" :
				while True:
					a = check_float(input("what is the first number:"))
					if a != "":
							break
				while True:
					b = check_float(input("what is the second number:"))
					if b != "":
						break
				if b == 0 :
						type_text("division by 0 error")
				else:
						type_text(a,"/",b,"=",a/b)
			if operation == "2" :
				while True:
					a = check_float(input("what is the first number:"))
					if a != "":
							break
				while True:
					b = check_float(input("what is the second number:"))
					if b != "":
						break
					type_text(a,"X",b,"=",a*b)
			if operation == "3" :
				while True:
					a = check_float(input("what is the first number:"))
					if a != "":
							break
				while True:
					b = check_float(input("what is the second number:"))
					if b != "":
						break
					type_text(a,"-",b,"=",a-b)
			if operation == "4" :
				while True:
					a = check_float(input("what is the first number:"))
					if a != "":
							break
				while True:
					b = check_float(input("what is the second number:"))
					if b != "":
						break
				type_text(a,"+",b,"=",a+b)
			if operation == "5" :
				while True:
					a = check_float(input("what is the first number:"))
					if a != "":
							break
				while True:
					b = check_float(input("what is the second number:"))
					if b != "":
						break
					type_text(a,"%",b,"=",a%b)
			if operation == "6" :
				while True:
					a = check_float(input("what is the first number:"))
					if a != "":
							break
				while True:
					b = check_float(input("what is the second number:"))
					if b != "":
						break
					type_text(a,"^",b,"=",a**b)
			if operation == "0" :
					type_text("ok sending you back to the hub")
					return
			else:
				type_text("Sorry I didn't understand")
def game():
		easterEggCount = 250
		maxGuessCount = 20
		minGuess = 1
		maxGuess = 100
		playCount = 0
		playAgain = True
		while playAgain == True:
				if playCount == easterEggCount:
						type_text("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME! ##connection terminated by: Guessy##")
						quit()
				playCount += 1
				num = random.randint (minGuess,maxGuess)
				type_text(f'Welcome the GUESS THE NUMBER! I am your host Guessy. You have {maxGuessCount} attempts before you lose the game. good luck.')
				while True:
					guess = input(f'Guess a number {minGuess}-{maxGuess}: ')
					if check_int(guess):
						guess = int(guess)
						break
				for x in range(maxGuessCount): 
					if guess < num:
						while True:
							guess = check_int(input("the number is larger: "))
							if guess != "":
								break
					if guess > num:
						while True:
							guess = check_int(input("the number is smaller: "))
							if guess != "":
								break
					if guess == num: 
						print ("you got it")
						playgain = str(input("do you want to play again? (y/n): "))
						if playgain != "y":
							playAgain = False
							type_text("ok sending you back to the hub")
							time.sleep(1)
							return
						else:
							type_text("ok")
							break
### pal got bug
def palindrome():
	invertedP = ""
	doagennP = True
	iterationP = 1
	runnerP = "placeholder"
	while doagennP == True:
		invertedP = ""
		iterationP = 1
		nameP = str(input("hi i am pally please input a word or sentence and i will tell you if it's a palindrome or not: ")).lower()
		if len(nameP) == 1:
				type_text(nameP,"is a palindrome")
				invertedP = ""
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): "))
				if runnerP == "n":
						type_text("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False
						return
		else:
				loopP = (len(nameP))
				lopnarP =(len(nameP))
				for lopnarP in range(lopnarP):
						invertedP += nameP[loopP-iterationP]
						iterationP += 1
				if invertedP == nameP:
						type_text(nameP,"is a palindrome")
				else:
						type_text(nameP,"is not a palindrome")
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): ")).lower()
				if runnerP == "n":
						type_text("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False
						return
def area():
	while True:
		e = 1
		type_text("1 for rectangle")
		type_text("2 for square")
		type_text("3 for triangle")
		type_text("4 for circle")
		type_text("5 for trapezoid")
		shape = input("what do you want or type stop to stop: ")
		if shape == "1":
			#square/rectangle
			type_text("ok input the numbers that you want")
			while True:
				a = check_float(input("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(input("what is the length (only numbers please): "))
				if b != "":
					break
			type_text(f"when the hight is {a} and the length is {b} the area is {a*b}.")
			e = 0
		if shape == "4":
			#circle
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(input("what is the radius (only numbers please): "))
				if a != "":
					break
			type_text(f"when the radius is {a} the area is {3.141592653589793238462643383279*a^2}")
		if shape == "3":
			#triangle
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(input("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(input("what is the length (only numbers please): "))
				if b != "":
					break
			type_text(f"when the hight is {a} and the length is {b} the area is {(a*b)*(1/2)}.")
		if shape == "5":
			#trapezoid
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(input("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(input("what is the top length (only numbers please): "))
				if b != "":
					break
			while True:
				c = check_float(input("what is the bottom length (only numbers please): "))
				if c != "":
					break
			type_text(f"when the hight is {a} and the bottom is {b} and the top is {c} the area is {((b+c)/2)*a}.")
		if shape == "2":
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = input("what is the length of one of the sides (only numbers please): ")
				if a != "":
					break
			type_text(f"when the the length of one of the sides is {a} the area is {a*2}.")
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
def avrage():
	while True:
		runsq = 1
		list_o_numsq = []
		percentageq = 0
		
		classesq = input("I am AV the Avenger. How many things do you want to average or type stop to stop: ")
		if classesq == "stop":
			type_text("ok sending you back to Hubby")
			break
		if classesq != "":
			classesq = int(classesq)
			for x in range(classesq):
				one_at_a_timeq = check_int(input(f"what is the percentage of # {runsq} (only numbers please): "))
				percentageq += one_at_a_timeq
				list_o_numsq.append(one_at_a_timeq)
				runsq += 1
			type_text(f"you entered {list_o_numsq} #'s it is an average of {percentageq/classesq}")
		go_aginq = input("do you want to use again (y/n): ")
		if go_aginq == "n":
			type_text("ok sending you back to Hubby")
			break
def code():
	input_o_code = input("shhhh. this is a secret i am liam what is the code(only numbers please): ")
	break_it = 1
	binary = ""
	checkw = 0
	for i in input_o_code:
		binary = binary + str(bin(ord(i)))
	if binary == "0b11011100b11001010b11101100b11001010b11100100b1000000b11001110b11101010b11011100b11011100b11000010b1000000b11001110b11010010b11101100b11001010b1000000b11110010b11011110b11101010b1000000b11101010b11100000b100001":
		while True:
			code_decode = int(input("would you like to code (1) or decode (2) or stop (3): "))
			list_o_coded = []
			output =""
			decoded = ""
			iterationw = 1
			loops_o_codeing = 0
			list_o_decoding = []
			if code_decode == 1:
				code = input("what is the uncoded word: ")
				seed = int(input("what is the decoding seed (whole numbers please): "))
				for x in code:
					list_o_coded.append(((ord(x))))
				for y in list_o_coded:
					if loops_o_codeing == 0:
						output = str(int(y)+seed)
					else:
						output = output +","+ str(int(y)+seed)
					loops_o_codeing += 1
				type_text(output)
			if code_decode == 2:
				coded_decoder = str(input("what is the coded thing: "))
				seed_o_decodeing = int(input("what is the seed: "))
				list_o_decoding = (coded_decoder.split(","))
				for z in list_o_decoding:
					var = str(chr(int(z)-seed_o_decodeing))
					decoded = decoded + var
				type_text(decoded)
			if code_decode == 3:
				input_o_code = ""
				break_it = 0
				break
	if break_it == 1:
		print(""""File "/workspaces/codespaces-jupyter/test.py," line 482" """,flush=True)
		print(f"pickle.({input_o_code})",flush=True)
		print("		^",flush=True)
		print("SyntaxError: invalid syntax",flush=True)
		time.sleep(50)
		print("lol")
		quit()
	else:
		print ("ok sending you back to hubby")
def translate_word(input_word):
	split = {}
	deleted = ""
	not_a_string = ""
	output = ""
	decoded = ""
	j = 0
	i = 0
	x = 0
	iteration = 1
	consonants = []
	if len(input_word) < 3:
		return(input_word)
	else:
		for x in input_word:
			if x == "a":
				deleted = "a"
				split = second_half(iteration, input_word)
				break
			if x == "e":
				deleted = "e"
				split = second_half(iteration, input_word)
				break
			if x == "i":
				deleted = "i"
				split = second_half(iteration, input_word)
				break
			if x == "o":
				deleted = "o"
				split = second_half(iteration, input_word)
				break
			if x == "u":
				deleted = "u"
				split = second_half(iteration, input_word)
				break
			if x == "y" and iteration > 1:
				deleted = "y"
				split = second_half(iteration, input_word)
				break
			iteration += 1
			consonants.append(x)
	for i in split:
		not_a_string = not_a_string + i
	for j in consonants:
		decoded = decoded + j
	output =deleted + not_a_string + decoded + "ay"
	return(output)
def second_half(num,word):
	return (word[num:])
def last_bit():
	while True:
		iteration = 1
		out = ""
		imput_o_word = input("what do you want to translate or type stop to go back to Hubby: ")
		if imput_o_word == "stop":
			type_text("Ok sending you back to hubby. Oink")
			break
		output = []
		intt = imput_o_word.split(" ")
		for i in intt:
			output.append(translate_word(i))
		for x in output:
			if iteration ==1:
				out = out + x
			else:
				out = out +" "+ x
			iteration += 1
		type_text(out)
def pig():
	type_text("Hi i am Pig")
	last_bit()
def change_settings(typing,debuging):
	while True:
		type_text("ok")
		type_text("0 to go back to the terminal")
		type_text("1 to toggle typing")
		type_text("2 to toggle debugging")
		type_text("3 to change typing speed")
		while True:
			imper = check_int(input("what do you want: "))
			if imper != "":
				break
		if imper == 0:
			type_text("ok back to the terminal")
			break
		elif imper == 1:
			if typing == True:
				typing = False
			else:
				typing = True
		elif imper == 2:
			if debuging == True:
				debuging = False
			else:
				debuging = True
		elif imper == 3:
			while True:
				sett = check_float(input("what do you want to change the typing speed to: "))
				if sett != "":
					break
def farinhight451():
	type_text("hi this is Kelvin")
	while True:
		yes = input("would you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			while True:
				tempofcelsius = check_int(input("what is the temp in celsius: "))
				if tempofcelsius != "":
					break
			type_text("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = input("would you like celsius to fahrenheit (y/n): ")
			if no == "y":
				while True:
					tempforfahrenheit = check_int(input("what is the temp in fahrenheit: "))
					if tempforfahrenheit != "":
						break
				type_text("the temp for celsius when fahrenheit is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			elif no == "n":				
				type_text("Ok sending you back to Hubby.")
				break
			else:
				type_text("sorry i didn't understand")
def print_ui(board):
	iteration = -1
	for x in board:
		iteration += 1
		if iteration == 0:
			if x == "O":
				q11 = "      ███████████      "
				q12 = "    ███         ███    "
				q13 = "   ███           ███   "
				q14 = "   ███           ███   "
				q15 = "   ███           ███   "
				q16 = "   ███           ███   "
				q17 = "    ███         ███    "
				q18 = "      ███████████      "
			elif x == "X":
				q11 = "   ███         ███    "
				q12 = "     ███     ███      "
				q13 = "       ███ ███        "
				q14 = "        █████         "
				q15 = "        █████         "
				q16 = "       ███ ███        "
				q17 = "     ███     ███      "
				q18 = "   ███         ███    "
			else:
				q11 = "                      "
				q12 = "                      "
				q13 = "                      "
				q14 = "                      "
				q15 = "                      "
				q16 = "                      "
				q17 = "                      "
				q18 = "                      "
		elif iteration == 1:
			if x == "O":
				q22 = "      ███████████      "
				q22 = "    ███         ███    "
				q23 = "   ███           ███   "
				q24 = "   ███           ███   "
				q25 = "   ███           ███   "
				q26 = "   ███           ███   "
				q27 = "    ███         ███    "
				q28 = "      ███████████      "
			elif x == "X":
				q21 = "   ███         ███    "
				q22 = "     ███     ███      "
				q23 = "       ███ ███        "
				q24 = "        █████         "
				q25 = "        █████         "
				q26 = "       ███ ███        "
				q27 = "     ███     ███      "
				q28 = "   ███         ███    "
			else:
				q21 = "                      "
				q22 = "                      "
				q23 = "                      "
				q24 = "                      "
				q25 = "                      "
				q26 = "                      "
				q27 = "                      "
				q28 = "                      "
		elif iteration == 2:
			if x == "O":
				q31 = "      ███████████      "
				q32 = "    ███         ███    "
				q33 = "   ███           ███   "
				q34 = "   ███           ███   "
				q35 = "   ███           ███   "
				q36 = "   ███           ███   "
				q37 = "    ███         ███    "
				q38 = "      ███████████      "
			elif x == "X":
				q31 = "   ███         ███    "
				q32 = "     ███     ███      "
				q33 = "       ███ ███        "
				q34 = "        █████         "
				q35 = "        █████         "
				q36 = "       ███ ███        "
				q37 = "     ███     ███      "
				q38 = "   ███         ███    "
			else:
				q31 = "                      "
				q32 = "                      "
				q33 = "                      "
				q34 = "                      "
				q35 = "                      "
				q36 = "                      "
				q37 = "                      "
				q38 = "                      "
		elif iteration == 3:
			if x == "O":
				q41 = "      ███████████      "
				q42 = "    ███         ███    "
				q43 = "   ███           ███   "
				q44 = "   ███           ███   "
				q45 = "   ███           ███   "
				q46 = "   ███           ███   "
				q47 = "    ███         ███    "
				q48 = "      ███████████      "
			elif x == "X":
				q41 = "   ███         ███    "
				q42 = "     ███     ███      "
				q43 = "       ███ ███        "
				q44 = "        █████         "
				q45 = "        █████         "
				q46 = "       ███ ███        "
				q47 = "     ███     ███      "
				q48 = "   ███         ███    "
			else:
				q41 = "                      "
				q42 = "                      "
				q43 = "                      "
				q44 = "                      "
				q45 = "                      "
				q46 = "                      "
				q47 = "                      "
				q48 = "                      "
		elif iteration == 4:
			if x == "O":
				q51 = "      ███████████      "
				q52 = "    ███         ███    "
				q53 = "   ███           ███   "
				q54 = "   ███           ███   "
				q55 = "   ███           ███   "
				q56 = "   ███           ███   "
				q57 = "    ███         ███    "
				q58 = "      ███████████      "
			elif x == "X":
				q51 = "   ███         ███    "
				q52 = "     ███     ███      "
				q53 = "       ███ ███        "
				q54 = "        █████         "
				q55 = "        █████         "
				q56 = "       ███ ███        "
				q57 = "     ███     ███      "
				q58 = "   ███         ███    "
			else:
				q51 = "                      "
				q52 = "                      "
				q53 = "                      "
				q54 = "                      "
				q55 = "                      "
				q56 = "                      "
				q57 = "                      "
				q58 = "                      "
		elif iteration == 5:
			if x == "O":
				q61 = "      ███████████      "
				q62 = "    ███         ███    "
				q63 = "   ███           ███   "
				q64 = "   ███           ███   "
				q65 = "   ███           ███   "
				q66 = "   ███           ███   "
				q67 = "    ███         ███    "
				q68 = "      ███████████      "
			elif x == "X":
				q61 = "   ███         ███    "
				q62 = "     ███     ███      "
				q63 = "       ███ ███        "
				q64 = "        █████         "
				q65 = "        █████         "
				q66 = "       ███ ███        "
				q67 = "     ███     ███      "
				q68 = "   ███         ███    "
			else:
				q61 = "                      "
				q62 = "                      "
				q63 = "                      "
				q64 = "                      "
				q65 = "                      "
				q66 = "                      "
				q67 = "                      "
				q68 = "                      "
		elif iteration == 6:
			if x == "O":
				q71 = "      ███████████      "
				q72 = "    ███         ███    "
				q73 = "   ███           ███   "
				q74 = "   ███           ███   "
				q75 = "   ███           ███   "
				q76 = "   ███           ███   "
				q77 = "    ███         ███    "
				q78 = "      ███████████      "
			elif x == "X":
				q71 = "   ███         ███    "
				q72 = "     ███     ███      "
				q73 = "       ███ ███        "
				q74 = "        █████         "
				q75 = "        █████         "
				q76 = "       ███ ███        "
				q77 = "     ███     ███      "
				q78 = "   ███         ███    "
			else:
				q71 = "                      "
				q72 = "                      "
				q73 = "                      "
				q74 = "                      "
				q75 = "                      "
				q76 = "                      "
				q77 = "                      "
				q78 = "                      "
		elif iteration == 7:
			if x == "O":
				q81 = "      ███████████      "
				q82 = "    ███         ███    "
				q83 = "   ███           ███   "
				q84 = "   ███           ███   "
				q85 = "   ███           ███   "
				q86 = "   ███           ███   "
				q87 = "    ███         ███    "
				q88 = "      ███████████      "
			elif x == "X":
				q81 = "   ███         ███    "
				q82 = "     ███     ███      "
				q83 = "       ███ ███        "
				q84 = "        █████         "
				q85 = "        █████         "
				q86 = "       ███ ███        "
				q87 = "     ███     ███      "
				q88 = "   ███         ███    "
			else:
				q81 = "                      "
				q82 = "                      "
				q83 = "                      "
				q84 = "                      "
				q85 = "                      "
				q86 = "                      "
				q87 = "                      "
				q88 = "                      "
		elif iteration == 8:
			if x == "O":
				q91 = "      ███████████      "
				q92 = "    ███         ███    "
				q93 = "   ███           ███   "
				q94 = "   ███           ███   "
				q95 = "   ███           ███   "
				q96 = "   ███           ███   "
				q97 = "    ███         ███    "
				q98 = "      ███████████      "
			elif x == "X":
				q91 = "   ███         ███    "
				q92 = "     ███     ███      "
				q93 = "       ███ ███        "
				q94 = "        █████         "
				q95 = "        █████         "
				q96 = "       ███ ███        "
				q97 = "     ███     ███      "
				q98 = "   ███         ███    "
			else:
				q91 = "                      "
				q92 = "                      "
				q93 = "                      "
				q94 = "                      "
				q95 = "                      "
				q96 = "                      "
				q97 = "                      "
				q98 = "                      "
			q1 = f"""
				 ██                            ██
	{q11}   ██   {q21}   ██   {q31}
	{q12}   ██   {q22}   ██   {q32}
	{q13}   ██   {q23}   ██   {q33}
	{q14}   ██   {q24}   ██   {q34}
	{q15}   ██   {q25}   ██   {q35}
	{q16}   ██   {q26}   ██   {q36}
	{q17}   ██   {q27}   ██   {q37}
	{q18}   ██   {q28}   ██   {q38}
                                 ██			       ██
       ████████████████████████████████████████████████████████████████████████████████████████
				 ██                            ██
	{q41}   ██   {q51}   ██   {q61}
	{q42}   ██   {q52}   ██   {q62}
	{q43}   ██   {q53}   ██   {q63}
	{q44}   ██   {q54}   ██   {q64}
	{q45}   ██   {q55}   ██   {q65}
	{q46}   ██   {q56}   ██   {q66}
	{q47}   ██   {q57}   ██   {q67}
	{q48}   ██   {q58}   ██   {q68}
                                 ██		               ██
       ████████████████████████████████████████████████████████████████████████████████████████
				 ██                            ██
	{q71}   ██   {q81}   ██   {q91}
	{q72}   ██   {q82}   ██   {q92}
	{q73}   ██   {q83}   ██   {q93}
	{q74}   ██   {q84}   ██   {q94}
	{q75}   ██   {q85}   ██   {q95}
	{q76}   ██   {q86}   ██   {q96}
	{q77}   ██   {q87}   ██   {q97}
	{q78}   ██   {q88}   ██   {q98}
                                 ██		               ██
"""
	print(q1, flush=True)
def possible_boards(cBoard,turn):
	moves = []
	for i in range(9):
		if cBoard[i] == None:
			newBoard = cBoard.copy()
			newBoard[i] = turn
			moves.append(newBoard)
	return moves
def choose_move(cBoard, turn):
	possible = possible_boards(cBoard, turn)

	if len(possible) == 1:
		return possible[0]

	nextTurn = "X"
	if turn == "X":
		nextTurn = "O"

	bestBoard = possible[0]
	bestX, bestO, bestT = score_move(bestBoard, nextTurn)

	for b in possible[1:]:
		x, o, t = score_move(b, nextTurn)
		if turn == "X":
			if o > bestO:
				continue
			elif x > bestX:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
			elif t > bestT and o < bestO and x >= bestX:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
		else:
			if x > bestX:
				continue
			elif o > bestO:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
			elif t > bestT and x < bestX and o >= bestO:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
	return bestBoard
def score_move(cBoard, turn):
	possible = possible_boards(cBoard, turn)
	x = 0.0
	o = 0.0
	t = 0.0
	for i, b in enumerate(possible):
		result = check_win(b)
		if result == "tie":
			return (0.0, 0.0, 1.0)
		elif result == "X":
			return (1.0, 0.0, 0.0)
		elif result == "O":
			return (0.0, 1.0, 0.0)
		elif turn == "X":
			bx, bo, bt = score_move(b, "O")
			x += bx
			o += bo
			t += bt
		else:
			bx, bo, bt = score_move(b, "X")
			x += bx
			o += bo
			t += bt
	# x /= len(possible)
	# o /= len(possible)
	# t /= len(possible)
	return(x,o,t)
def check_win(board):
	for c in ["X","O"]:
		if board[0] == c and board[1] == c and board[2] == c:
			return c
		elif board[3] == c and board[4] == c and board[5] == c:
			return c
		elif board[6] == c and board[7] == c and board[8] == c:
			return c
		elif board[0] == c and board[3] == c and board[6] == c:
			return c
		elif board[1] == c and board[4] == c and board[7] == c:
			return c
		elif board[2] == c and board[5] == c and board[8] == c:
			return c
		elif board[0] == c and board[4] == c and board[8] == c:
			return c
		elif board[2] == c and board[4] == c and board[6] == c:
			return c
	for x in board:
		if x == None:
			return None
	return "tie"
def meet_o_code(unused):
	type_text("hi i am The Gamer this is Tic Tac Toe")
	while True:
		play = str(input("1 to play computer 2 to play other player and 3 to stop: "))
		if play == "2":
			p1 = input("who is player 1: ")
			p2 = input("who is player 2: ")
			while True:
				go = check_int(input(f"1 for {p1} to go first 2 for {p2} to go first: "))
				if go != "":
					if go == "1":
						turn = "p1"
						break
					elif go == "2":
						turn = "p2"
						break
					else:
						type_text("not a valid input")
			while True:
				win = check_win(board)
				if win == "tie":
					type_text("tie")
					break
				elif win == "X":
					type_text(f"{p1} wins")
					break
				elif win == "O":
					type_text(f"{p2} wins")
					break
				else:
					print_ui(board)
				if turn == "p1":
					while True:
						while True:
							peace = check_int(input(f"{p1} where do you want to go(use the number of place like top left is 1):"))
							if peace != "":
								break
						if board[peace-1] != None:
							type_text("already taken")
						else:
							board[peace-1] = "X"
							turn = "p2"
							break
				elif turn == "p2":
					while True:
						while True:
							peace = check_int(input(f"{p2} where do you want to go(use the number of place like top left is 1):"))
							if peace != "":
								peace = int(peace)
								break						
						if board[peace-1] != None:
							type_text("already taken")
						else:
							board[peace-1] = "O"
							turn = "p1"
							break
				print_ui(board)
		elif play == "1":
			while True:
				board = choose_move(board, "X")
				if check_win(board) != None:
					print_ui(board)
					type_text(check_win(board))
					break
				while True:
					print_ui(board)
					if check_win(board) != None:
						break
					type_text("1 for top left")
					type_text("2 for top middle")
					type_text("3 for top right")
					type_text("4 for middle left")
					type_text("5 for middle middle")
					type_text("6 for middle right")
					type_text("7 for bottom left")
					type_text("8 for bottom middle")
					type_text("9 for bottom right")
					while True:
						play_go = check_int(input("where do you want to go: "))
						if play_go != "":
							break
					if play_go < 10 and play_go > 0:
						if play_go == 1 and board[0] != None:
							type_text("that is alredy taken")
						elif play_go == 2 and board[1] != None:
							type_text("that is alredy taken")
						elif play_go == 3 and board[2] != None:
							type_text("that is alredy taken")
						elif play_go == 4 and board[3] != None:
							type_text("that is alredy taken")
						elif play_go == 5 and board[4] != None:
							type_text("that is alredy taken")
						elif play_go == 6 and board[5] != None:
							type_text("that is alredy taken")
						elif play_go == 7 and board[6] != None:
							type_text("that is alredy taken")
						elif play_go == 8 and board[7] != None:
							type_text("that is alredy taken")
						elif play_go == 9 and board[8] != None:
							type_text("that is alredy taken")
						else:
							if play_go == 1:
								board[0] = "O"
							if play_go == 2:
								board[1] = "O"
							if play_go == 3:
								board[2] = "O"
							if play_go == 4:
								board[3] = "O"
							if play_go == 5:
								board[4] = "O"
							if play_go == 6:
								board[5] = "O"
							if play_go == 7:
								board[6] = "O"
							if play_go == 8:
								board[7] = "O"
							if play_go == 9:
								board[8] = "O"
							print_ui(board)
							possible_boards(board, "X")
							choose_move(board,"X")
							break
					else:
						type_text("nope")
				if check_win(board) != None:
					type_text(check_win(board))
					print_ui(board)
					break
		else:
			type_text("ok sending you back to the hub.")
			return
def madlib():
	type_text("hi i am libby")
	runlib = True
	if runlib == True:
		one = str(input("this is a mad lib. Choose a adjictive: "))
		two = str(input("Choose a noun: "))
		tree = str(input("Choose a adjective: "))
		forr = str(input("Choose a noun; place: "))
		five = str(input("Choose a adjictive: "))
		six = str(input("Choose a adjictive: "))
		seven = str(input("Choose a pleral noun; vehical: "))
		ate = str(input("Choose a adjictive: "))
		nine = str(input("Choose a adjective: "))
		ten = str(input("Choose a plural noun: "))
		elevin = str(input("Choose a adjictive: "))
		twelve = str(input("Choose a plural noun: "))
		thrteen = str(input("Choose a plural noun: "))
		forteen = str(input("Choose a adjictive: "))
		fifteen = str(input("Choose a noun: "))
		sixteen = str(input("Choose a verb: "))
		seventeen = str(input("Choose a adjective: "))
		eating = str(input("Choose a verb: "))
		nineteen = str(input("Choose a pleral noun: "))
		twonty = str(input("Choose a pleral noun; type of job: "))
		twuntyone = str(input("Choose a ajictive: "))
		twuntytwo = str(input("Choose a verb: "))
		twontytree = str(input("Choose a adjective: "))
		type_text(f"Star Wars is a {one} {two} of {tree} versus evil in a {forr} far far away. There are {five} battles between {six} {seven} in {ate} space and {nine} duels with {ten} called {elevin} sabers. {twelve} called droids are helpers and {thrteen} tho the heroes. A {forteen} power caled The {fifteen} {sixteen}s people to do {seventeen} things, like {eating} {nineteen}. The Jedi {twonty} use The Force for the {twuntyone} side and the sith {twuntytwo} it for the {twontytree} side.")
		libbs = input("do you want to do another one? (y/n):")
		if libbs == "n":
			type_text("ok")
			runlib = False
			return
def lists():
	type_text("hi i am listy (but evoryone calls me lil'lister)")
	clist = input("what is the name of your list: ")
	thelist = []
	while True:
		action = input("""what do you want to do
1 add item
2 remove item
3 to print and leave the list (note this also deletes it): """)
		if action != "1" and action != "2" and action != "3":
			type_text("i am not impressed with your efforts to brake me")
		if action == "1" or action == "2" or action == "3":	
			if action == "1":
				inpuy = input("what do you want to add: ")
				thelist.append(inpuy)
			elif action == "2":
				print(flush=True)
				print(f"          {clist}          ",flush=True)
				print("___________________________",flush=True)
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________",flush=True)
				while True:
					remove = int(input("what do you want to remove: "))
					if remove > len(thelist):
						type_text(f"you dont have a item at {remove}")
					elif remove < 1:
						type_text("i am not impressed with your efforts to brake me")
					else:
						del thelist[remove-1]
						break
			elif action == "3":
				print(flush=True)
				print(f"          {clist}          ",flush=True)
				print("___________________________",flush=True)
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________",flush=True)
				clist = input("what is the new name for the new list: ")
				thelist = []	
def hub():
	while True:
		type_text("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		type_text("0 to stop")
		type_text("1 for settings")
		type_text("2 for calculator")
		type_text("3 for number game")
		type_text("4 for palindrome detector")
		type_text("5 for pig latin translator")
		type_text("6 for anagram maker")
		type_text("7 for averager")
		type_text("8 for temperature calculator")
		type_text("9 for area calculator")
		type_text("10 for list maker")
		type_text("11 for tic tac toe game")
		type_text("12 for rock paper scissors")
		type_text("13 for text adventure game (made by mis larose)")
		hubo = input("what do you want: ")
		if check_int(hubo) == "":
			type_text("invalid input")
		else:
			hubo = int(hubo)
			if hubo == 0:
				type_text("Goodby please come back soon! ##connection terminated by:Hubby##")
				time.sleep(1)
				quit()
			elif hubo ==1:
				change_settings(typing,debuging)
			elif hubo ==2:
				type_text("Ok sending you to Calcu.")
				time.sleep(1)
				calculator()
			elif hubo ==3:
				type_text("Ok sending you to Guessy.")
				time.sleep(1)
				game()
			elif hubo ==4:
				type_text("Ok sending you to Pally.")
				time.sleep(1)
				palindrome()
			elif hubo ==5:
				type_text("Ok sending you to Pig.")
				time.sleep(1)
				pig()
			elif hubo ==6:
				type_text("Ok sending you to Anny.")
				time.sleep(1)
				anagram()
			elif hubo ==7:
				type_text("Ok sending you to AV (she is a bit crazy).")
				avrage()
			elif hubo ==8:
				type_text("Ok sending you to Kelvin.")
				farinhight451()
			elif hubo ==9:
				type_text("Ok sending you to Arion.")
				area()
			elif hubo ==10:
				type_text("Ok sending you to lil'lister")
				lists()
			elif hubo ==11:
				type_text("Ok sending you to The Gamer")
				meet_o_code(1)
			elif hubo == 12:
				type_text("ok sending you to The Rock")
				dwane_the_rock()
			elif hubo == 13:
				type_text("ok sendig you to The DM")
				play_gamre()
			elif hubo == 7232010:
				code()
			else:
				type_text("Sorry this option is not available yet.")
if debuging == False:
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