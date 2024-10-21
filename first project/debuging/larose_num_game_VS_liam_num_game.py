#laroses game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guess = 50
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
start_game()
#liams game
import random
import time
def type_text(textt):
	for x in textt:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,.05))
	print("")
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
							type_text("ok goodby")
							return
						else:
							type_text("ok")
game()