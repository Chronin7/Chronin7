
bord =[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
xcord=5
ycord=5

import msvcrt
while True:
	if msvcrt.kbhit():
		key = msvcrt.getch().decode("utf-8").lower() 
		if key == "w"and ycord !=0: 
			ycord-=1
		elif key == "a":
			xcord-=1
		elif key == "s":
			ycord+=1
		elif key == "d":
			xcord+=1
		elif key == "p":
			quit()
		print(" ")
		for x in range(50):
			print("_",end="")
		for x in range(ycord-1):
			print("|                                                  |")
		print("|",end="")
		for x in range(xcord):
			print(" ",end="")
		print("x",end="")
		for x in range(49-(xcord)):
			print(" ",end="")
		print("|")
		for x in range(20-ycord):
			print("|                                                  |")
		print("|__________________________________________________|") 