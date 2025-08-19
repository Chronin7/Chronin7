import random
import time
intel = 0
hp = 0
dexterity = 0
stren = 0
classs = ""
race = ""
name = ""
def pc():
	global classs
	global race
	global name
	global hp
	global stren
	global dexterity
	global intel
	print(f"""
name: {name}	   

race: {race}

class: {classs}

health: {hp}

strength: {stren}

dexterity: {dexterity}

intelligence: {intel}

""")
def cname():
	global name
	name = input("what do you what your name to be:")
	print(f"ok your new name is {name}")
def racees():
	global race
	print("""1 for ranger
2 for barbarean
3 for bard
4 for 
	   
	   
	   
	   
	   
	   """)
	race = input("what is your race")
	print(f"ok your new race is {race}")
def clas():
	global classs
	classs = input("what is your class")
	print(f"ok your new class is {classs}")
while True:
	print("0 to quit")
	print("1 to change name")
	print("2 to change max HP")
	print("3 to change strength")
	print("4 to cnange intelligence")
	print("5 to change dexterity")
	print("6 to change race")
	print("7 to change class")
	print("8 to print chericter")
	print("9 to print save file /_\\ under construction /_\\")
	while True:
		try:
			goinputthing = int(input())
			break
		except:
			print("enter a number")
	if goinputthing == 0:
		quit
	elif goinputthing == 1:
		cname()
	elif goinputthing == 2:
		chp()
	elif goinputthing == 3:
		stress()
	elif goinputthing == 4:
		know()
	elif goinputthing == 5:
		dex()
	elif goinputthing == 6:
		racees()
	elif goinputthing == 7:
		clas()
	elif goinputthing == 8:
		pc()
	elif goinputthing == 9:
		print("not ready")
	elif goinputthing == 33:
		print("doofenshmirtz evil incorporated!!!")
		time.sleep(2)
	else:
		print("not a option")