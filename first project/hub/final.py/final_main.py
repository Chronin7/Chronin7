
import random
import time
movopt = []
damagebuff = 0
rpg=0
good = ['holy hand gernade one use insta kill','rpg once per battle 20 damage at begining','heth + 50 potion','Sten MK II tends to misfire sometimes has buletts bounce off of tagert +20% damage','Apache Revolver you can use it like a gun (terible aim) a nife (way to flexible) or a iron fist (the only safe way to use it) +30% damage','pickled lepercon head +1 luck for 7 turns','luck potion +1 luck for 2 turns']
norm = ["nuke (you cant use it cuse it will kill evorything and evoryone including you)","stick + 3% damage",'helth + 10 porion','deodorant (shreck wants it)','luck charm +1 luck for a turn','luck potion +1 luck for 2 turns']
rearer = ['a peace of a lemon','sord + 10% damage','helth + 20 prtion','slingshot +5% damage','a 15 foot long pole','clover +1 luck for 3 turns','luck potion +1 luck for 4 turns']
def getloot(rear):
	global damagebuff
	global rpg
	if rear == 1:
		rand = random.randint(0,5)
		if rand == 1:
			damagebuff +=3
		return norm[rand]
	elif rear == 2:
		rand = random.randint(0,6)
		if rand == 1:
			damagebuff +=10
		if rand == 3:
			damagebuff+=5
		return rearer[rand]
	elif rear == 3:
		rand = random.randint(0,6)
		if rand == 1:
			rpg +=20
		if rand == 3:
			damagebuff+=20
		if rand == 4:
			damagebuff+=30
		return good[rand]
	else:
		damagebuff += 100
		health = health*2
		return "spoon +100% damage and heath"
looted = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
monster = [None,None,None,None,True,None,None,None,None,True,None,None,None,True,None,None,True,None,True,True,True,None,True,None]
def feld1():
	while True:
		try:
			desition = int(input(f"""would you like to 
1 to move
2 to serach for loot: """))
			if desition in [1,2]:
				break
			else:
				inputcorect()
		except:
			inputcorect()
	if desition == 2:
		if looted[0]==False:
			looted[0]=True
			temp = getloot(1)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		return "foothills1"
def feld2():
	while True:
		try:
			desition = int(input(f"""would you like to 
1 to move
2 to serach for loot: """))
			if desition in [1,2]:
				break
			else:
				inputcorect()
		except:
			inputcorect()
	if desition == 2:
		if looted[1]==False:
			looted[1]=True
			temp = getloot(1)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move east
2 to move west
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "feld2"
		elif desition == 1:
			return "foot hills1"
		elif desition == 2:
			return "feld3"
def feld3():
	while True:
		try:
			desition = int(input(f"""would you like to 
1 to move
2 to serach for loot: """))
			if desition in [1,2]:
				break
			else:
				inputcorect()
		except:
			inputcorect()
	if desition == 2:
		if looted[2]==False:
			looted[2]=True
			temp = getloot(2)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move east
2 to move north
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "feld3"
		elif desition == 1:
			return "feld2"
		elif desition == 2:
			return "forest"
def feld4():
	while True:
		try:
			desition = int(input(f"""would you like to 
1 to move
2 to serach for loot: """))
			if desition in [1,2]:
				break
			else:
				inputcorect()
		except:
			inputcorect()
	if desition == 2:
		if looted[3]==False:
			looted[3]=True
			temp = getloot(1)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move west
2 to move south
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "feld4"
		elif desition == 1:
			print("they hate you so they dont let you in")
			return "feld4"
		elif desition == 2:
			return "forest"
def feld5():
	while True:
		try:
			desition = int(input(f"""would you like to 
1 to move
2 to serach for loot: """))
			if desition in [1,2]:
				break
			else:
				inputcorect()
		except:
			inputcorect()
	if desition == 2:
		if looted[4]==False:
			looted[4]=True
			temp = getloot(2)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move east
2 to move north
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "feld3"
		elif desition == 1:
			return "feld2"
		elif desition == 2:
			return "forest"
def feld6():
def inputcorect():
	print("thats not a valid input ",end="")
	if random.randint(1,10):
		print("so a troll throws you into lava...")
		time.sleep(1)
		print("just kidding just please input a valid input")
	else:
		print()
def print_mon(hp,nm):
	print(f"""
          {nm}
 ________________________
| health left: {hp}
|________________________
""")
	return random.randint(1,20) < 14,random.randint(1,20)
exoshtion = 0
gameover = False
rations = 5
monkilled = False
pythonbridge = False
win = False
loot = [f"hp{20}"]
name = ""
playedmount = 0
health = 100
coller = ""
lootunseen = []
monlist = ["skeleton","mummy","giant lizard","dragon","flying snake","killer bunny","wannabe coder"]
def intro():
	global name
	global exoshtion
	global monkilled
	global rations
	global pythonbridge
	global win
	global loot
	global playedmount
	global coller
	global health
	global lootunseen
	global gameover
	exoshtion = 0
	rations = 5
	monkilled = False
	pythonbridge = False
	win = False
	loot = [f"hp{20}"]
	gameover = False
	name = ""
	playedmount = 0
	health = 100
	coller = ""
	gointor = 1
	lootunseen = []
	while gointor != 1000:
		for x in range(random.randint(1,gointor)):
			print("  ",end="")
		print("x")
		time.sleep(random.uniform(0,3/gointor))
		gointor+=1
		questens()
def questens():
	global name
	global lootunseen
	global exoshtion
	global monkilled
	global rations
	global pythonbridge
	global win
	global loot
	global playedmount
	global coller
	global health
	name = input("whats your name adventurer (type your name then press enter to continue): ")
	coller = input(f"hello {name} whats your favorite color: ")
	print(f"""hello {name} who likes the color {coller}, your quest is "To seek the Holy Grail" without reaching exhaustion level 5 good luck""")
def main():
	global name
	global exoshtion
	global monkilled
	global monhelth
	global rations
	global pythonbridge
	global win
	global loot
	global playedmount
	global coller
	global lootunseen
	global health
	global gameover
	while True:
		if gameover == True:
			break
		while True:
			if gameover == True:
				break
			if rations <0:
				print("you starved to death and killer guinea pigs ate you")
				print("game over")
				gameover = True
				break
			if exoshtion > 5:
				print("you died of exhaustion and carnivorous antelopes ate your earlobes.")
				print("game over")
				gameover = True
				break
			if health < 1:
				print("you died of... well... nevermind you just die.")
				print("game over")
				gameover = True
				break
			try:
				action = int(input(f"""rations left: {rations}
exhaustion level: {exoshtion}
health: {health}
what would you like to do
1 to continue along path
2 to rest
3 to hunt for food
4 to check inventory: """))
				if action not in [1,2,3,4]:
					inputcorect()
				else:
					break
			except:
				inputcorect()
		if action == 1:
			rations-=1
			event = random.randint(1,3)
			if event == 3:
				eventtype = random.randint(1,5)
				if eventtype == 1:
					lose = random.randint(0,2)
					print(f"a blizzard comes thru and you gain {lose} exhaustion",end=" ")
					exoshtion -= lose
					lose = random.randint(0,rations-1)
					print(f"and blew {lose} rations away.")
					rations-=lose
				if eventtype == 2:
					print("a robber came and stole a ration")
					rations -=1
				if eventtype == 3:
					nam = input("""you come to a rope bridge spanning a casum and a man stops you and says "Stop. Who would cross the Bridge of Death must answer me these questions three, ere the other side he see. What... is your name: """)
					if nam.lower != name.lower:
						print("wrong *as you are thrown into the casum*")
						print("you die and aliens take your body and are disappointed that you cant play poker")
						print("game over")
						gameover = True
						break
					else:
						nam = str(input("What... is your quest: ")).lower
						if nam != "To seek the Holy Grail":
							print("wrong *as you are thrown into the casum*")
							print("you die and are turned into a lemon")
							print("game over")
							gameover = True
							break
						if playedmount >1:
							nam = input("What... is the air-speed velocity of an unladen swallow: ").lower
							if nam == "What do you mean? An African or a European swallow?".lower:
								print(" Huh? I... I don't know that. AUUUUUUUGGGGGGGGGGGHHH!! *as he is thrown into the casum*")
								print("you successfully make it across the bridge")
							else:
								print("wrong *as you are thrown into the casum*")
								print("you die and a goat gives you a wet willy")
								print("game over")
								gameover = True
								break
						else:
							nam = input("What... is your favorite colour: ").lower
							if nam != coller:
								print("wrong *as you are thrown into the casum*")
								print("you die and billy the bird makes you into a nest")
								print("game over")
								gameover = True
								break
							else:
								print("you may pass")
								print("you make it across the bridge")
				if eventtype == 4:
					bob = random.randint(1,5)
					print(f"a flash flood comes in and you take {bob} damage.")
					health -= bob
				if eventtype == 5:
					monhelth = random.randint(50,100)
					monname = monlist[random.randint(0,6)]
					print(f"a {monname} appears")
					unused,unused = print_mon(monhelth,monname)
					while True:
						if gameover == True:
							break
						print("1 to heal")
						print("2 to attack")
						while True:
							tur = int(input())
							if tur not in [1,2]:
								inputcorect()
							else:
								break
						if tur == 2:
							damage = random.randint(25,51)
							if damage == 51:
								damage = random.randint(60,100)
							print(f"you deal {damage} damage")
							monhelth -= damage
							if monhelth < 1:
								print("you killed the monster")
								loot,lootunseen.append(get(raeraty=random.randint(3,5)))
								print(f"you get a {loot}")
								break
						elif tur == 1:
							iteration = 1
							print("0 to return")
							for x in loot:
								print(f"{iteration}: ",end = "")
								print(x)
								iteration += 1
							while True:
								try:
									inp = int(input("what do you want to use"))
									if inp == 0:
										break
									try:
										print(f"you used your {loot[inp-1]}")
										loot.pop(inp-1)
										health = lootunseen[inp-1] + health 
										lootunseen.pop(inp-1)
										break
									except:
										inputcorect()
								except:
									inputcorect()
						unused,damage = print_mon(monhelth,monname)
						health -=damage
						print(f"you take {damage} damage")
						if health < 1:
							print("the grim reper comes and uses your head as a bolling ball.")
							print("game over")
							gameover = True
							break
						if gameover == True:
							break
main()