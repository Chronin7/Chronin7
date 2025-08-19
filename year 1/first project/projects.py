import random
import time
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
def type_text(textt):
	for x in textt:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,type_speed))
	print("")
def calculator():
		operation = 0
		a = "n/a"
		b = "n/a"
		type_text("Hi this is Calcu. What do you want me to calculate today")
		while True:
			operation = 0
			if operation == 0 :
				operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ").lower()
				if operation != "devision" and operation != "multiplication" and operation != "subtraction" and operation != "addition" and operation != "modulo" and operation != "factoring" and operation != "stop":
					type_text("you probably spelt it wrong.")
					if operation == "division" :
						a = int(input("what is the first number:"))
						b = int(input("what is the second number:"))
						if b == 0 :
								type_text("division by 0 error")



						else:
								type_text(a,"/",b,"=",a/b)



					if operation == "multiplication" :
							a = int(input("what is the first number:"))
							b = int(input("what is the second number:"))
							type_text(a,"X",b,"=",a*b)



					if operation == "subtraction" :
							a = int(input("what is the first number:"))
							b = int(input("what is the second number:"))
							type_text(a,"-",b,"=",a-b)



					if operation == "addition" :
						a = int(input("what is the first number:"))
						b = int(input("what is the second number:"))
						type_text(a,"+",b,"=",a+b)



					if operation == "modulo" :
							a = int(input("what is the first number:"))
							b = int(input("what is the second number:"))
							type_text(a,"%",b,"=",a%b)



					if operation == "factoring" :
							a = int(input("what is the first number:"))
							b = int(input("what is the second number:"))
							type_text(a,"^",b,"=",a**b)



					if operation == "stop" :
							type_text("ok sending you back to the hub")
							return
					if operation == 0 :

							print("")

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
				guess = int(input(f'Guess a number {minGuess}-{maxGuess}: '))  
				for x in range(maxGuessCount): 
					if guess < num:
						guess = int(input("the number is larger: "))
					if guess > num:
						guess = int(input("the number is smaller: "))
					if guess == num : 
						print ("you got it")
						playgain = str(input("do you want to play again? (y/n): "))
						if playgain != "y":
							playAgain = False
							type_text("ok sending you back to the hub")
							time.sleep(1)
							return
						else:
							type_text("ok")
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
	type_text("hi i am Arion")
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
def avrage():
	while True:
		runsq = 1
		list_o_numsq = []
		percentageq = 0
		classesq = input("I am AV the Avenger. How many things do you want to average or type stop to stop: ")
		if classesq == "stop":
			type_text("ok sending you back to Hubby")
			break
		classesq = int(classesq)
		for x in range(classesq):
			one_at_a_timeq = int(input(f"what is the percentage of # {runsq} (only numbers please): "))
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
		print('"File "/workspaces/codespaces-jupyter/test.py," line 9"')
		print(f"pickle.({input_o_code})")
		print("		^")
		print("SyntaxError: invalid syntax")
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
def change_settings():
	type_text("ok")
	while True:
		type_text("0 to go back to the terminal")
		type_text(f"1 to toggle typing: {typing}")
		type_text(f"2 to toggle debugging: {debugging}")
		type_text(f"3 to change typing speed: {type_speed}")
		imper = input("what do you want")
		if imper == 0:
			type_text("ok back to the terminal")
			break
		elif imper == 1:
			typing = not typing
		elif imper == 2:
			debugging = not debugging
		elif imper == 3:
			sett = float(input("what do you want to change the typing speed to: "))
			if sett < .1:
				continue
			else:
				type_speed = sett
def farinhight451():
	type_text("hi this is Kelvin")
	while True:
		yes = input("would you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			tempofcelsius = int(input("what is the temp in celsius: "))
			print ("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = input("would you like celsius to fahrenheit (y/n): ")
			if no == "y":
				tempforfahrenheit = int(input("what is the temp in fahrenheit: "))  
				type_text("the temp for celsius when fahrenheit is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			elif no == "n":				
				type_text("Ok sending you back to Hubby.")
				break
			else:
				type_text("sorry i didn't understand")
def madlib():
	runlib = True
	if runlib == True:
		madlim = int(input("This is liby chose one for starwars madlib and more are coming soon!: "))
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
				print()
				print(f"          {clist}          ")
				print("___________________________")
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________")
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
				print()
				print(f"          {clist}          ")
				print("___________________________")
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________")
				clist = input("what is the new name for the new list: ")
				thelist = []		