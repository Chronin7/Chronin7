
import time
import random
def type_text(text):
	for x in text:
		print(x, end = "")
		time.sleep(random.uniform(.01,1.0))
	print("")
while True:
	runs = 1
	list_o_nums = []
	percentage = 0
	classes = input("I am AV the Avenger. How many things do you want to average or type stop to stop: ")
	if classes == "stop":
		type_text("ok sending you back to Hubby")
		break
	classes = int(classes)
	for x in range(classes):
		one_at_a_time = int(input(f"what is the percentage of # {runs} (only numbers please): "))
		percentage += one_at_a_time
		list_o_nums.append(one_at_a_time)
		runs += 1
	type_text(f"you entered {list_o_nums} #'s it is an average of {percentage/classes}")
	go_agin = input("do you want to use again (y/n): ")
	if go_agin == "n":
		type_text("ok sending you back to Hubby")
		break
