invertedP = ""
import time
import random
doagennP = True
iterationP = 1
def type_text(text):
	for x in text:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,1.0))
	print("")
just_started = 0
runnerP = "placeholder"
nameP = str(input("Hi I am Pally please input a word or sentence and i will tell you if it's a palindrome or not: ")).lower()
while doagennP == True:
	invertedP = ""
	iterationP = 1
	if just_started == 1:
		nameP = str(input("Ok input the desired word to be tested:"))
	if len(nameP) == 1:
		print(nameP,"is a palindrome")
		invertedP = ""
		runnerP = str(input("Do you want me to detect another palindrome for you? (y/n): "))
		just_started = 1
		if runnerP == "n":
			type_text("Ok sending you back to Hubby")
			time.sleep(1)
			doagennP = False
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
			runnerP = str(input("Do you want me to detect another palindrome for you? (y/n): ")).lower()
			just_started = 1
			if runnerP == "n":
				type_text("ok sending you back to Hubby")
				time.sleep(1)
				doagennP = False