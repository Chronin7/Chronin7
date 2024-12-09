import time
import math
import random
import threading
bord =[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
xcord=5
ycord=5
inp = input()
if input() == inp:
	print("bob")
import msvcrt
def main():
		global xcord
		global ycord
		key = ""
		if msvcrt.kbhit():
			key =  msvcrt.getch()
		for x in range(500):
			print()
		if key == "w"and ycord !=0: 
			ycord-=1
		elif key == inp:
			xcord-=1
		elif key == "s":
			ycord+=1
		elif key == "d":
			xcord+=1
		elif key == "p":
			quit()
		print(" ")
		for x in range(ycord-1):
			print("                                                  ")
		for x in range(xcord):
			print(" ",end="")
		print("x",end="")
while True:
	main()