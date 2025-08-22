#liam p who are you
namelist=[]
agelist=[]
collorlist=[]
while True:
	input_name=input("whats your name: ")
	if input_name in namelist:
		pos=namelist.index(input_name)
		print(f"hello {input_name} your age is {agelist[pos]} and your favorit collor is {collorlist[pos]}.")
	else:
		age=input("what is your age: ")
		collor=input("whats your favrit coller: ")
		namelist.append(input_name)
		agelist.append(age)
		collorlist.append(collor)
		print(f"hello {input_name} your age is {age} and your favorit collor is {collor}.")