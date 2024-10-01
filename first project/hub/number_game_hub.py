def num_game():
    import random
    #just to have a bit of fun
    easterEggCount = 100
    #this is the max guess count
    maxGuessCount = 20
    # this is the min and max guess
    minGuess = 1
    maxGuess = 100



    playCount = 0
    playAgain = True
    while playAgain:
        playCount += 1

        if playCount == easterEggCount:
            print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME! ##connection terminated by: Guessy## ")
            exit()


        num = random.randint (minGuess,maxGuess)
        print(f'Welcome to GUESS THE NUMBER! i am your host Guessy you have {maxGuessCount} attempts before you lose the game. good luck.')
        while True:
            guess = int(input(f'Guess a number {minGuess}-{maxGuess}: '))  
            if guess == "":
                print("opps looks like you are a bit trigerhappy")
            else:
                break
        for x in range(maxGuessCount): 
            while True:
                    if guess < num :
                        guess = int(input ("the number is larger: "))
                        if guess == "":
                            print("opps looks like you are a bit trigerhappy")
                    elif guess > num :
                        guess = int(input ("the number is smaller: "))
                        break
                    elif guess == "":
                        print("opps looks like you are a bit trigerhappy")
                    else:
                        if guess == num : 
                            print ("you got it")
                            break
                        playAgain = input ("do you want to play again? (y/n): ")
                        if playAgain != "y":
                            playAgain = False
                            print("ok sending you back to Hubby")
                        break
num_game()