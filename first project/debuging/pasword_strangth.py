while True:
	password = input("what your pasword: ")
	listt = []
	iteration = 0
	chri = False
	num = False
	leng = False
	for x in password:
		listt.append(x)
	for x in listt:
		iteration += 1
		if x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "0":
			num = True
		if iteration > 8:
			leng = True
		if x in ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '<', ',', '>', '.', '?', '/']:
			chri = True
	if chri==True and leng==True and num==True:
		print("good password")
		break
	else:
		print("bad")
		if num == False:
			print("you need a number")
		if leng == False:
			print("you need at least 8 long password")
		if chri == False:
			print("you need a speshal cericter")