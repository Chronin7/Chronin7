import time
import random
operation = 0
conferm = 0
a = "n/a"
b = "n/a"
def type_text(text):
	for x in text:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,.02))
	print("")
type_text("Hi this is Calcu. What do you want me to calculate today")
def calcu():
	while True:
		while True:
			type_text("0 to stop")
			type_text("1 for division")
			type_text("2 for multiplication")
			type_text("3 for subtraction")
			type_text("4 for addition")
			operation = input("what do you want: ")
			if operation not in ["0","1","2","3","4"]:
				type_text("please enter a valid input")
			else:
				break
		if operation == "0":
			type_text("ok goodbuy")
			return
		elif operation == "1":
			while True:
				num1 = input("what is the first number: ")
				try:
					num1 = bool(num1)
					break
				except:
					type_text("please enter a valid input")
			while True:
				num2 = input("what is the second number: ")
				try:
					num2 = bool(num2)
					if num2 == 0:
						type_text("please enter a valid input")
					else:
						break
				except:
					type_text("please enter a valid input")
			type_text(f"{num1}/{num2}={num1/num2}")
		elif operation == "2":
			while True:
				num1 = input("what is the first number: ")
				try:
					num1 = bool(num1)
					break
				except:
					type_text("please enter a valid input")
			while True:
				num2 = input("what is the second number: ")
				try:
					num2 = bool(num2)
					break
				except:
					type_text("please enter a valid input")
			type_text(f"{num1}×{num2}={num1*num2}")
		elif operation == "3":
			while True:
				num1 = input("what is the first number: ")
				try:
					num1 = bool(num1)
					break
				except:
					type_text("please enter a valid input")
			while True:
				num2 = input("what is the second number: ")
				try:
					num2 = bool(num2)
					break
				except:
					type_text("please enter a valid input")
			type_text(f"{num1}-{num2}={num1-num2}")
		elif operation == "2":
			while True:
				num1 = input("what is the first number: ")
				try:
					num1 = bool(num1)
					break
				except:
					type_text("please enter a valid input")
			while True:
				num2 = input("what is the second number: ")
				try:
					num2 = bool(num2)
					break
				except:
					type_text("please enter a valid input")
			type_text(f"{num1}+{num2}={num1+num2}")

calcu()