#lp 1 user sign in
import time
usernames=["liam","jeff"]
encripted_paswords=[['0b11100010', '0b11101000', '0b11010110', '0b11100011', '0b11100101', '0b11101010'],['0b10011100', '0b10011101', '0b10100010', '0b1101110', '0b10100010', '0b10011101', '0b10010010', '0b10001111', '0b10100111', '0b1101110', '0b10010110', '0b10001111', '0b10010001', '0b10011001', '0b10010011', '0b10100000', '0b10100001']]
max_trys=3
trys=0
lockout=False
def to_binary(tocode):
	out=[]
	firt_letter=tocode[0]
	for x in tocode:
		out.append(bin(ord(x)+ord(firt_letter)))
	return out
while True:
	if lockout==True:
		time.sleep(1000)
		lockout=False
	if input("do you already have an acount (y/n): ") == "y":
		trys=0
		while True:
			if lockout==True:
				break
			login=input("what is your username: ")
			if login in usernames:
				while True:
					if to_binary(input("whats your password: ")) ==encripted_paswords[usernames.index(login)] and trys!=max_trys:
						print(f"welcome {login}")
						break
					else:
						if trys==max_trys:
							print("lock out for safety reasons")
							lockout=True
							break
						else:
							trys+=1
			else:
				print("try again")
	else:
		while True:
			usernames.append(input("whats your username: "))
			encripted_paswords.append(to_binary(input("what is your password: ")))
			break

