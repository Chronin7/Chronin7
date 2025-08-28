#lp avrage grade
import time
import random
def type_text(text):
	for x in text:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,1.0))
	print("")
while True:
	inp = input("1 to stop 2 to avrage stuff 3 to find your grade letter: ")
	if inp == "1":
		break
	if inp == "2":
		while True:
			runs = 1
			list_o_nums = []
			percentage = 0
			classes = input(" How many things do you want to average: ")
			classes = int(classes)
			for x in range(classes):
				one_at_a_time = int(input(f"what is the percentage of # {runs} (only numbers please): "))
				percentage += one_at_a_time
				list_o_nums.append(one_at_a_time)
				runs += 1
			type_text(f"you entered {list_o_nums} #'s it is an average of {percentage/classes}")
			go_agin = input("do you want to use again (y/n): ")
			if go_agin == "n":
				type_text("ok")
				break
	if inp == "3":
		while True:
			av = bool(input("what is you grade in persentage (no persentage sign pleese): "))
			if av < 65:
				type_text("you have a F and have a GPA of 0")
			elif av < 66:
				type_text("you have a D- and have a GPA of ~.67")
			elif av < 66:
				type_text("you have a D and have a GPA of ~1")
			elif av < 66:
				type_text("you have a D+ and have a GPA of ~1.33")
			elif av < 66:
				type_text("you have a C- and have a GPA of ~1.66")
			elif av < 66:
				type_text("you have a C and have a GPA of ~2")
			elif av < 66:
				type_text("you have a C+ and have a GPA of ~2.33")
			elif av < 66:
				type_text("you have a B- and have a GPA of ~2.66")
			elif av < 66:
				type_text("you have a B and have a GPA of ~3")
			elif av < 66:
				type_text("you have a B+ and have a GPA of ~3.33")
			elif av < 66:
				type_text("you have a A- and have a GPA of ~3.66")
			elif av < 66:
				type_text("you have a A and have a GPA of ~4")
			elif av == 100:
				type_text("you have a A+ and have a GPA of ~5")
			elif av < 100:
				type_text("how")
				time.sleep(3)
				type_text("just how")
			else:
				continue
			go = input("do you want to use again (y/n): ")
			if go  == "n":
				type_text("ok")
				break