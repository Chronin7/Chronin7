corect = 0
import random
anserd = 0
def q1():
	global corect
	global anserd
	print("what is the main wepon that Link uses")
	print("A: the Master Torch")
	print("B: the Master Sword")
	print("C: the Master Glock")
	print("D: the Master Stick")
	while True:
		ans = input()
		if ans not in ["a","b","c","d","A","B","C","D"]:
			print("please input a valid input")
		else:
			break
	if ans in ["b","B"]:
		print("corect")
		corect += 1
		anserd += 1
		return
	else:
		print("incorect")
		anserd += 1
		return
def q2():
	global corect
	global anserd
	print("what is the final boss")
	print("A: Flower Blight Ganon")
	print("B: Master Kohga")
	print("C: Dark Beast Ganon")
	print("D: Ganondorf")
	while True:
		ans = input()
		if ans not in ["a","b","c","d","A","B","C","D"]:
			print("please input a valid input")
		else:
			break
	if ans in ["c","C"]:
		print("corect")
		corect += 1
		anserd += 1
		return
	else:
		print("incorect")
		anserd += 1
		return
def q4():
	global corect
	global anserd
	print("how much is a hard boiled egg bought for")
	print("A: 100 rupys")
	print("B: 16 rupys")
	print("C: 17 rupys")
	print("D: 10 rupys")
	while True:
		ans = input()
		if ans not in ["a","b","c","d","A","B","C","D"]:
			print("please input a valid input")
		else:
			break
	if ans in ["d","D"]:
		print("corect")
		corect += 1
		anserd += 1
		return
	else:
		print("incorect")
		anserd += 1
		return
def q3():
	global corect
	global anserd
	print("how much damage duse a royal clamore do")
	print("A: 52 damage")
	print("B: 16 damage")
	print("C: 17 damage")
	print("D: 10 damage")
	while True:
		ans = input()
		if ans not in ["a","b","c","d","A","B","C","D"]:
			print("please input a valid input")
		else:
			break
	if ans in ["d","D"]:
		print("corect")
		corect += 1
		anserd += 1
		return
	else:
		print("incorect")
		anserd += 1
		return
def q5():
	global corect
	global anserd
	print("how many gardeins are around hyrule castle")
	print("A: 135")
	print("B: 30")
	print("C: 17")
	print("D: 10")
	while True:
		ans = input()
		if ans not in ["a","b","c","d","A","B","C","D"]:
			print("please input a valid input")
		else:
			break
	if ans in ["b","B"]:
		print("corect")
		corect += 1
		anserd += 1
		return
	else:
		print("incorect")
		anserd += 1
		return
	