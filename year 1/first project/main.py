import random

easterEggCount = 100
maxGuessCount = 20

minGuess = 1
maxGuess = 100


playCount = 0
playAgain = True
while playAgain:
	playCount += 1

	if playCount == easterEggCount:
		print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME!")
		exit()


	num = random.randint (minGuess,maxGuess)
	print(f'Welcome the GUESS THE NUMBER! you have {maxGuessCount} attempts before you lose the game. good luck.')
	guess = int(input(f'Guess a number {minGuess}-{maxGuess}: '))  

	for x in range(maxGuessCount): 
		if guess < num :
			guess = int(input ("the number is larger: "))
		if guess > num :
			guess = int(input ("the number is smaller: "))
		if guess == num : 
			print ("you got it")
			playAgain = input ("play again? (y/n): ")
			if playAgain != "y":
				print("ok")
				playAgain = False
			break