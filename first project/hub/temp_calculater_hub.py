import time
import random
def type_text(text):
	for x in text:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,1.0))
	print("")
type_text("hi this is Kelvin")
def temp():
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
temp()