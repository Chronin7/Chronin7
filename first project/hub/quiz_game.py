corect = 0
import random
anserd = 0
qed = []
def q1():
	global corect
	global qed
	global anserd
	qed.append("q1")
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
		return 1
	else:
		print("incorect")
		anserd += 1
		return -1
def q2():
	global corect
	global qed
	global anserd
	qed.append("q2")
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
		return 1
	else:
		print("incorect")
		anserd += 1
		return -1
def q4():
	global corect
	global qed
	global anserd
	qed.append("q4")
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
		return 1
	else:
		print("incorect")
		anserd += 1
		return -1
def q3():
	global corect
	global anserd
	global qed
	qed.append("q3")
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
	if ans in ["a","A"]:
		print("corect")
		corect += 1
		anserd += 1
		return 1
	else:
		print("incorect")
		anserd += 1
		return -1
def q5():
	global corect
	global qed
	global anserd
	qed.append("q5")
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
		return 1
	else:
		print("incorect")
		anserd += 1
		return -1
print("welcom to the quiz game")
ques = random.randint(1,5)
if ques == 1:
	d = q1()
	r = 1
elif ques == 2:
	d = q2()
	r = 2
elif ques == 3:
	d = q3()
	r = 3
elif ques == 4:
	d = q4()
	r = 4
elif ques == 5:
	d = q5()
	r = 5
while True:
	nq = r + d
	if nq == 5:
		if "q5" not in qed:
			d = q5()
			r = 5
		elif "q4" not in qed:
			d = q4()
			r = 4
		elif "q3" not in qed:
			d = q3()
			r = 3
		elif "q2" not in qed:
			d = q2()
			r = 2
		elif "q1" not in qed:
			d = q1()
			r = 1
		else:
			break
	elif nq == 4:
		if "q4" not in qed:
			d = q4()
			r = 4
		elif "q3" not in qed:
			d = q3()
			r = 3
		elif "q2" not in qed:
			d = q2()
			r = 2
		elif "q1" not in qed:
			d = q1()
			r = 1
		else:
			nq = 5
	elif nq == 3:
		if "q3" not in qed:
			d = q3()
			r = 3
		elif "q2" not in qed:
			d = q2()
			r = 2
		elif "q1" not in qed:
			d = q1()
			r = 1
		else:
			nq = 4
	elif nq == 2:
		if "q2" not in qed:
			d = q2()
			r = 2
		elif "q1" not in qed:
			d = q1()
			r = 1
		else:
			nq = 3
	elif nq == 1:
		if "q1" not in qed:
			d = q1()
			r = 1
		else:
			nq = 2
	else:
		if "q1" not in qed:
			d = q1()
			r = 1
		elif "q2" not in qed:
			d = q2()
			r = 2
		elif "q3" not in qed:
			d = q3()
			r = 3
		elif "q4" not in qed:
			d = q4()
			r = 4
		elif "q5" not in qed:
			d = q5()
			r = 5
		else:
			break
print(f"your score was {corect}/5")