# ideut proof lp 1
auth=False
while auth==False:
	name=input("what is your name (first name and last name): ")
	if " " not in name:
		print("bruh i am too smart for you try again")
	try:
		thing1=""
		thing2=""
		thing1,thing2=name.split(" ")
		if len(thing1)>0 and len(thing2)>0:
			auth=True
		else:
			chr("d")
	except:
		print("your not fooling me bucko try again")
while auth == True:
	try:
		number=int(input("what is your phone number: "))
		if len(str(number))==10:
			auth=False
		else:
			print("wow you are really determined")
	except:
		print("wow you are really determined")
while auth == False:
	try:
		gpa=float(input("whats your gpa: "))
		gpa=round(gpa,2)
		if gpa<=4 and gpa >=0:
			auth=True
	except:
		print("you will always fail at breaking me")
print(f"your name is {name} your phone number is {number} your gpa is {gpa}")
if gpa>3:
	print("thats a good gpa")
else:
	print("lol get a better gpa")