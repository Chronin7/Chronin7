import random
import time
def type_text(text):
	for x in text:
		print(x, end = "")
		time.sleep(random.uniform(.01,.1))
	print("")
while True:
	anagram = []
	output = ""
	doit = "12345"
	word = input("hi i am Anny what is the word that you want into anagram or type stop to stop: ")
	if word == "stop":
		type_text("sending you back to Hubby")
		break
	if word == "":
		type_text("oops looks like you are a bit trigerhappy")
	else:
		rand = len(word)
		for y in doit:
			output = ""
			anagram = []
			for x in word:
				anagram.insert(random.randint(1,rand),x)
			for i in anagram:
				output = output + i
			print (output)