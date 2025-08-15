inp=str(input())
data=[]
placeholder=""
for x in inp:
	if x == "-" and placeholder != "-":
		placeholder=x
	elif placeholder == "-":
		data.append("-"+str(x))
		placeholder=""
	else:
		data.append(x)
try:
	data[0]-1
except:
	print("error")
print(data)
operaters=["!","+","/","%","^","(",")","*"]
typeof=[]
for x in data:
	if x in operaters:#add the iteration count
		for y in operaters:
			if x==y:
				typeof.append(operaters[iteration])