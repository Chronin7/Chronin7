
equating = True
while equating == True:
	inp=str(input())
	data=[]
	try:
		placeholder=""
		for x in inp:
			if x == "-" and placeholder != "-":
				placeholder=x
			elif placeholder == "-":
				data.append(int("-"+str(x)))
				placeholder=""
			else:
				data.append(int(x))
			print(data)
		operaters=["+","/","%","^","(",")","*"]
		typeof=[]
		for x in data:
			if x in operaters:
				iteration=-1
				for y in operaters:
					iteration+=1
					if x==y:
						typeof.append(operaters[iteration])
			elif "-" in x:
				typeof.append("negitive")
			else:
				typeof.append("number")
		print(data)
		print(typeof)
		a=0
		b=0
		iteration = -1
		for i in typeof:#figure out how to add the operations
			if i == "+":
				


	except:
		print("please input an equason (no ='s or ()'s (keep in mind i am not smart enugh to do order of operations so make shure that it is in the corect order (sorry)) ")
