import random
x = 1
hubo = 0
operation = 0
easterEggCount = 2
maxGuessCount = 20
minGuess = 1
maxGuess = 100
playCount = 0
playAgain = True
def hub():
    print("welcome to the hub.")
    hubo = input("1 for calculater 2 for guessing game 3 for paladrome detector and 4 to quit: ")
def calculater():
    operation = 0
    conferm = 0
    a = "n/a"
    b = "n/a"
    print("Hi this is Calcu. What do you want me to calculate today")
    def calcu():
        operation = 0
        if operation == 0 :
            operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ")
        if operation == "division" :
            a = int(input("what is the first number:"))
            b = int(input("what is the second number:"))
            if b == 0 :
                print("division by 0 error")
                calcu()
            else:
                print(a,"/",b,"=",a/b)
                calcu()
        if operation == "multiplication" :
            a = int(input("what is the first number:"))
            b = int(input("what is the second number:"))
            print(a,"X",b,"=",a*b)
            calcu()
        if operation == "subtraction" :
            a = int(input("what is the first number:"))
            b = int(input("what is the second number:"))
            print(a,"-",b,"=",a-b)
            calcu()
        if operation == "addition" :
            a = int(input("what is the first number:"))
            b = int(input("what is the second number:"))
            print(a,"+",b,"=",a+b)
            calcu()
        if operation == "modulo" :
            a = int(input("what is the first number:"))
            b = int(input("what is the second number:"))
            print(a,"%",b,"=",a%b)
            calcu()
        if operation == "factoring" :
            a = int(input("what is the first number:"))
            b = int(input("what is the second number:"))
            print(a,"^",b,"=",a**b)
            calcu()
        if operation == "stop" :
            print("ok")
            quit()
        if operation == 0 :
            calcu()
        else:
            print("Sorry I didn't understand")
        calcu()
    operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ")
    if operation == "division" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
    else:
        if b == 0 :
            print("division by 0 error")
            calcu()
            print(a,"/",b,"=",a/b)
            calcu()
    if operation == "multiplication" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"X",b,"=",a*b)
        calcu()
    if operation == "subtraction" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"-",b,"=",a-b)
        calcu()
    if operation == "addition" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"+",b,"=",a+b)
        calcu()
    if operation == "modulo" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"%",b,"=",a%b)
        calcu()
    if operation == "factoring" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"^",b,"=",a**b)
        calcu()
    if operation == "stop" :
        print("ok")
        hub()
    if operation == 0 :
        calcu()
    else:
        print("Sorry I didn't understand")
    calcu()

def game():
    x = 1
    easterEggCount = 2
    maxGuessCount = 20
    minGuess = 1
    maxGuess = 100
    playCount = 0
    playAgain = True
    while playAgain:
        if playCount == easterEggCount:
		    print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETIER WITH YOUR TIME!")
		    hub()
        playCount += 1
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
		    		playAgain = False
	        break
    hub()