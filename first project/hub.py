import random
import time

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
def hub():
	time.sleep(1)
	while runhub == True:
		print("welcome to the hub. I am hubby I will direct you to wherever you want.")

		hubo = 0

		hubo = int(input("1 for calculator 2 for guessing game 3 for palindrome detector 4 for madlibs and 0 to quit: "))
    
		if hubo ==0:
			print("goodby please come back soon! ##connection terminated by:Hubby##")
			time.sleep(1)

			quit()

		if hubo ==1:
			print("ok sending you to Calcu.")
			time.sleep(1)

			calculator()
			time.sleep(1)

		if hubo ==2:
			print("ok sending you to Guessy.")
			time.sleep(1)

			game()
			time.sleep(1)
		if hubo ==3:
			print("ok sending you to Pally.")
			time.sleep(1)

			palindrome()
			time.sleep(1)
		if hubo ==4:
			print("ok sending you to liby.")
			time.sleep(1)
			madlib()
			time.sleep(1)
		if hubo ==5:
			print("sorry this option is not available yet.")
		if hubo ==6:
			print("sorry this option is not available yet.")
		if hubo ==7:
			print("sorry this option is not available yet.")
		if hubo ==8:
			print("sorry this option is not available yet.")
		if hubo ==9:
			print("sorry this option is not available yet.")
		if hubo ==10:
			print("sorry this option is not available yet.")
		if hubo ==31415926:
			print("you broke it.")
			
		else:
			print("sorry this option is not available yet.")


def calculator():
		operation = 0
		a = "n/a"
		b = "n/a"
		print("Hi this is Calcu. What do you want me to calculate today")
		operation = 0
		if operation == 0 :
			operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ").lower()
			if operation == "division" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				if b == 0 :
						print("division by 0 error")



				else:
						print(a,"/",b,"=",a/b)



			if operation == "multiplication" :
					a = int(input("what is the first number:"))
					b = int(input("what is the second number:"))
					print(a,"X",b,"=",a*b)



			if operation == "subtraction" :
					a = int(input("what is the first number:"))
					b = int(input("what is the second number:"))
					print(a,"-",b,"=",a-b)



			if operation == "addition" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				print(a,"+",b,"=",a+b)



			if operation == "modulo" :
					a = int(input("what is the first number:"))
					b = int(input("what is the second number:"))
					print(a,"%",b,"=",a%b)



			if operation == "factoring" :
					a = int(input("what is the first number:"))
					b = int(input("what is the second number:"))
					print(a,"^",b,"=",a**b)



			if operation == "stop" :
					print("ok sending you back to the hub")
					return
			if operation == 0 :

					print("")

			else:
				print("Sorry I didn't understand")


		operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ").lower()
		if operation == "division" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
		else:
				if b == 0 :
						print("division by 0 error")



						print(a,"/",b,"=",a/b)



		if operation == "multiplication" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				print(a,"X",b,"=",a*b)



		if operation == "subtraction" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				print(a,"-",b,"=",a-b)



		if operation == "addition" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				print(a,"+",b,"=",a+b)



		if operation == "modulo" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				print(a,"%",b,"=",a%b)



		if operation == "factoring" :
				a = int(input("what is the first number:"))
				b = int(input("what is the second number:"))
				print(a,"^",b,"=",a**b)



		if operation == "stop" :
				print("ok sending you back to the hub")

				return

		if operation == 0 :

				print("")

		else:
				print("Sorry I didn't understand")



def game():
		easterEggCount = 250
		maxGuessCount = 20
		minGuess = 1
		maxGuess = 100
		playCount = 0
		playAgain = True
		while playAgain == True:
				if playCount == easterEggCount:
						print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME! ##connection terminated by: Guessy##")
						quit()
				playCount += 1
				num = random.randint (minGuess,maxGuess)
				print(f'Welcome the GUESS THE NUMBER! I am your host Guessy. You have {maxGuessCount} attempts before you lose the game. good luck.')
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
							print("ok sending you back to the hub")
							time.sleep(1)
							return
						else:
							print("ok")

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
				print(nameP,"is a palindrome")
				invertedP = ""
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): "))
				if runnerP == "n":
						print("ok sending you back to the hub")
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
						print(nameP,"is a palindrome")
				else:
						print(nameP,"is not a palindrome")
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): ")).lower()
				if runnerP == "n":
						print("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False

						return


# madlib profishensy test
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
		print(f"Star Wars is a {one} {two} of {tree} versus evil in a {forr} far far away. There are {five} battles between {six} {seven} in {ate} space and {nine} duels with {ten} called {elevin} sabers. {twelve} called droids are helpers and {thrteen} tho the heroes. A {forteen} power caled The {fifteen} {sixteen}s people to do {seventeen} things, like {eating} {nineteen}. The Jedi {twonty} use The Force for the {twuntyone} side and the sith {twuntytwo} it for the {twontytree} side.")
		libbs = input("do you want to do another one? (y/n):")
		if libbs == "n":
			print("ok")
			runlib = False
			return

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
