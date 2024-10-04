import time
import random
input_o_code = input("shhhh. this is a secret i am liam what is the code(only numbers please): ")
break_it = 1
binary = ""
check = 0
for i in input_o_code:
	binary = binary + str(bin(ord(i)))
if binary == "0b11011100b11001010b11101100b11001010b11100100b1000000b11001110b11101010b11011100b11011100b11000010b1000000b11001110b11010010b11101100b11001010b1000000b11110010b11011110b11101010b1000000b11101010b11100000b100001":
	while True:
		code_decode = int(input("would you like to code (1) or decode (2) or stop (3): "))
		list_o_coded = []
		output =""
		decoded = ""
		iteration = 1
		loops_o_codeing = 0
		list_o_decoding = []
		if code_decode == 1:
			code = input("what is the uncoded word: ")
			seed = int(input("what is the decoding seed (whole numbers please): "))
			for x in code:
				list_o_coded.append(((ord(x))))
			for y in list_o_coded:
				if loops_o_codeing == 0:
					output = str(int(y)+seed)
				else:
					output = output +","+ str(int(y)+seed)
				loops_o_codeing += 1
			print(output)
		if code_decode == 2:
			coded_decoder = str(input("what is the coded thing: "))
			seed_o_decodeing = int(input("what is the seed: "))
			list_o_decoding = (coded_decoder.split(","))
			for z in list_o_decoding:
				var = str(chr(int(z)-seed_o_decodeing))
				decoded = decoded + var
			print(decoded)
		if code_decode == 3:
			input_o_code = ""
			break_it = 0
			break
if break_it == 1:
	print('"File "/workspaces/codespaces-jupyter/test.py," line 9"')
	print(f"pickle.({input_o_code})")
	print("		^")
	print("SyntaxError: invalid syntax")
	quit()
else:
	print ("ok sending you back to hubby")