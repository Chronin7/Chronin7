import random
import time
exoshtion = 0
gameover = False
rations = 5
monkilled = False
pythonbridge = False
win = False
loot = ["hp+20"]
name = ""
playedmount = 0
health = 100
coller = ""
lootunseen = ["h20"]
monlist = ["skeleton","mummy","giant lizard","dragon","flying snake","killer bunny","wannabe coder"]
movopt = []
damagebuff = 1
rpg=0
len_loot = -1
luck = 0
gunseen = ["cg","","h50","","","l7","l2"]
nunseen = ["","","h10","cd","l1","l2"]
runseen = ["","","h20","","","l3","l4"]
looted = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
monster = [None,None,None,None,True,None,None,None,None,True,None,None,None,True,None,None,True,None,True,True,True,None,True,None]
good = ['holy hand gernade one use insta kill','rpg once per battle 20 damage at begining','heth + 50 potion','Sten MK II tends to misfire sometimes has buletts bounce off of tagert +20% damage','Apache Revolver you can use it like a gun (terible aim) a nife (way to flexible) or a iron fist (the only safe way to use it) +30% damage','pickled lepercon head +1 luck for 7 turns','luck potion +1 luck for 2 turns']
norm = ["nuke (you cant use it cuse it will kill evorything and evoryone including you)","stick + 3% damage",'helth + 10 porion','deodorant (shreck wants it)','luck charm +1 luck for a turn','luck potion +1 luck for 2 turns']
rearer = ['a peace of a lemon','sord + 10% damage','helth + 20 prtion','slingshot +5% damage','a 15 foot long pole','clover +1 luck for 3 turns','luck potion +1 luck for 4 turns']
def getloot(rear):
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	if luck == 0:
		chr(1234)
	else:
		rear+=1
	len_loot+=1
	if rear == 1:
		rand = random.randint(0,5)
		if rand == 1:
			damagebuff +=.3
		lootunseen.append(nunseen[rand])
		return norm[rand]
	elif rear == 2:
		rand = random.randint(0,6)
		if rand == 1:
			damagebuff +=.10
		if rand == 3:
			damagebuff+=.05
		lootunseen.append(runseen[rand])
		return rearer[rand]
	elif rear == 3:
		rand = random.randint(0,6)
		if rand == 1:
			rpg +=20
		if rand == 3:
			damagebuff+=.20
		if rand == 4:
			damagebuff+=.30
		lootunseen.append(gunseen[rand])
		return good[rand]
	else:
		damagebuff += 1
		health = health*2
		return "spoon +100% damage and heath"

def monbattle(monname):
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	hp = random.randint(50,500)-rpg
	if random.randint(1,20) > 14:
		damage =random.randint(5,20)
		print(f"you took {damage} damage from a {monname}")
		health -= damage
	while True:
		if health < 1:
			print(f"you died from a {monname} puny mortal")
			print("game over")
			return "die"
		while True:
			try:
				inp = int(input("""1 to atack the monster
2 to use a item"""))
				if inp in [1,2]:
					break
				else:
					print("bruh")
			except:
				print("bruh")
		if inp == 1:
			damage = random.randint(3,10)*damagebuff
			print(f"you did {damage} damage")
			hp-=damage
			if hp <1:
				print(f"you killed {monname}")
				loot.append(getloot(2))
				print(f"you got a {loot[len_loot]}")
				return "live"
			else:
				print(f"the {monname} is at {hp} HP")
			damage =random.randint(5,20)
			print(f"you took {damage} damage from the {monname}")
			health -= damage
		if inp == 2:
			itera = 0
			prinitera = 0
			use = []
			print("your items you can use")
			for x in len(lootunseen):
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					if inp in list(range(prinitera)):
						break
					else:
						print("nope")
				except:
					print("nope")
			if "h" in lootunseen[use[inp-1]]:
				health += int(lootunseen[use[inp-1]][-2])
				loot.pop(use[inp-1])
				lootunseen.pop(use[inp-1])
				use.pop(inp-1)
			if "cg" == lootunseen[use[inp-1]]:
				loot.pop(use[inp-1])
				lootunseen.pop(use[inp-1])
				use.pop(inp-1)
				print(f"you killed {monname}")
				loot.append(getloot(2))
				print(f"you got a {loot[len_loot]}")
				return "live"
			if "cd" == lootunseen[use[inp-1]] and monname == "shreck":
				loot.pop(use[inp-1])
				lootunseen.pop(use[inp-1])
				use.pop(inp-1)
				print("shreck thanks you")
				loot.append(getloot(1275043980432759837259743))
				print("you get a spoon")
				return "live"
			elif "cd" == lootunseen[use[inp-1]] and monname !="shreck":
				print("the monster eats it and is engraged even more")
				loot.pop(use[inp-1])
				lootunseen.pop(use[inp-1])
				use.pop(inp-1)


			
def feld1():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
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
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
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
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
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
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
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
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		if monster[5] == True:
			monbattle()
			monster[5] = False
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
def intro():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
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
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	name = input("whats your name adventurer (type your name then press enter to continue): ")
	coller = input(f"hello {name} whats your favorite color: ")
	print(f"""hello {name} who likes the color {coller}, your quest is "To seek the Holy Grail" good luck""")
