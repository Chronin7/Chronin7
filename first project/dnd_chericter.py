import random
intel = 0
hp = 0
dex = 0
stren = 0
name = ""
def pc():
	print(f"""
name: {name}	   

health: {hp}

strength: {stren}

dexterity: {dex}

intelligence: {intel}

""")
print("make your chericter")
while True:
	print("1 to change name")
	print("2 to change max hp")
	print("3 to change strength")
	print("4 to cnange intelligence")
	print("5 to print chericter")
	print("6 to print save file /_\\ under construction /_\\")
	print("7 to quit")
	goinputthing = input()