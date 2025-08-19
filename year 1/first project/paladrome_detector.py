inverted = ""
doagenn ={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
iteration = 1
runner = ""
while doagenn == True:
	inverted = ""
	iteration = 1
	name = input("paladrome detector: ").lower()
	if len(name) == 1:
		print(name,"is a paladrome")
		inverted = ""
	else:
		loop = (len(name))
		lopnar =(len(name))
		for lopnar in range(lopnar):
			inverted += name[loop-iteration]
			iteration += 1
		if inverted == name:
			print(name,"is a paladrome")
		else:
			print(name,"is not a paladrome")
		runer = input("do you want to detect another paladrome? (y/n): ")
		if runner == "n":
			break