import random
import time
#this function is from geeks for geeks
def check():
	print(space)
	print(input_word)
	print(iteration)
	print(not_a_string)
	print(not_a)
	print(oouutt)
def check_space(stringer):
    count = 0
    for i in range(0, len(stringer)):
        if stringer[i] == " ":
            count += 1
    return count
#this function is from me
def type_text(text):
	for x in text:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,1.0))
	print("")
out = []
outer_iteration = 1
oouutt = ""
while True:
	inp = str(input("I am Pig what do you want to translate:"))
	if inp == "":
		print("oops looks like you are a bit trigerhappy")
	else:
		space = check_space(inp)
		imp = inp.split(" ")
		for i in imp:
			input_word = i
			checks = 0
			splitt = []
			deleted = ""
			not_a_string = ""
			output = ""
			not_a = ""
			while True:
				iteration = 1
				if len(input_word) < 3:
					if outer_iteration == 1:
						out.append(input_word)
					else:
						out.append(" ")
						out.append(input_word)
				else:
					for x in input_word:
						if x == "a":
							splitt = input_word.split("a",1)
							deleted = "a"
							break
						if x == "e":
							splitt = input_word.split("e",1)
							deleted = "e"
							break
						if x == "i":
							splitt = input_word.split("i",1)
							deleted = "i"
							break
						if x == "o":
							splitt = input_word.split("o",1)
							deleted = "o"
							break
						if x == "u":
							splitt = input_word.split("u",1)
							deleted = "u"
							break
						if x == "y" and iteration > 1:
							splitt = input_word.split("y",1)
							deleted = "y"
							break
						iteration += 1
				not_a_string = splitt[:iteration]
				for i in not_a_string:
					not_a = not_a +''+i
				output = not_a + deleted +"ay"
				if outer_iteration == 1:
					out.append(input_word)
				else:
					out.append(" ")
					out.append(input_word)
				if len(out) == len(imp) + space:
					break
				else:
					outer_iteration += 1
			for z in out:
				oouutt = oouutt + z
			print(oouutt)
			go = input("Do you want to translate again? (y/n): ")
			if input_word == "":
				print ("oops looks like you are a bit trigerhappy")
			else:
				if go != "y":
					type_text("Ok sending you back to Hubby")
					break
				else:
					input_word = ""
					input_word = input("What do you want to translate (one word at a time):")
					if input_word == "":
						print ("oops looks like you are a bit trigerhappy")