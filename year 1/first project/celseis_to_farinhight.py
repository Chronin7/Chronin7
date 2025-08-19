#liam celsius to fahrenheit calculater/profishency test
while True:
	yes = input("woud you like celsius to fahrenheit (y/n): ")
	if yes == "y":
		tempofcelsius = int(input("what is the temp in celsius: ")) 
		print ("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
	if yes == "n":
		no = input("woud you like celsius to fahrenheit (y/n): ")
		if no == "y":
			tempforfahrenheit = int(input("what is the temp in fahrenheit: ")) 
			print("the temp for celsius when fahrenheight is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
		elif no == "n":
			print("Ok sending you back to Hubby.")
			break
		else:
			print("sorry i dident understand")
