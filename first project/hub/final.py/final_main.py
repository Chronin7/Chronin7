from asccii_art import *
from final_mon import *
import random
import time
exost = 0
goal = 15
rations = 3
ascii_art("welcome travler")
ascii_art("what is your@name:")
name = input()
ascii_art("what is your@favorite coller:")
collor = input()
ascii_art(f"hello {name}@your quest is@to find the@holly grail@good luck")
while True:
	ascii_art(f"rations left: {rations}")
	ascii_art(f"exostion level: {exost}")
	ascii_art("1 to travel@along path")
	ascii_art("2 to rest")
	ascii_art("3 to hunt for@food")
	ascii_art("4 to check stats")
	inp = input()
	if inp == "1":
		exost+=1
		rations-=1
		goal -=1
		event = random.randint(1,3)
		if event>1:
			if goal<1:
				sumon(1000,"miss la")
                break

