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
def getloot(rear):# 1 for norm 2 for rear 3 for good
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
				print(f"you are at {health} HP")
				inp = int(input("""1 to atack the monster
2 to use a item: """))
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
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
			if inp == 0:
				continue
			if "h" in use[inp-1]:
				health += int(use[inp-1][len(use[inp-1]) - 2:])
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print(f"you are now at {health} HP")
			if "cg" == use[inp-1]:
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print(f"you killed {monname}")
				loot.append(getloot(2))
				print(f"you got a {loot[len_loot]}")
				return "live"
			if "cd" == use[inp-1] and monname == "shreck":
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print("shreck thanks you")
				loot.append(getloot(1275043980432759837259743))
				print("you get a spoon")
				return "live"
			elif "cd" == use[inp-1] and monname !="shreck":
				print("the monster eats it and is engraged even more")
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
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
1 to move north
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

		return "fo1"
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
			return "f2"
		elif desition == 1:
			return "fo1"
		elif desition == 2:
			return "fe3"
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
			return "fe3"
		elif desition == 1:
			return "fe2"
		elif desition == 2:
			return "f"
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
			return "fe4"
		elif desition == 1:
			print("they hate you so they dont let you in")
			return "fe4"
		elif desition == 2:
			return "f"
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
	if monster[4] == True:
		if monbattle("flying snake") != "live":
			return "dead"
		monster[4] = False
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
2 to move west
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "fe5"
		elif desition == 1:
			return "fe6"
		elif desition == 2:
			return "fo1"
def feld6():
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
		if looted[5]==False:
			looted[5]=True
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
1 to move west
2 to move north
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "fe6"
		elif desition == 1:
			return "fe5"
		elif desition == 2:
			return "fo2"
def foothills1():
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
		if looted[6]==False:
			looted[6]=True
			temp = getloot(3)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move north
2 to move south
3 to move east
4 to move west
""")
				if desition in [0,1,2,3,4]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "fo1"
		elif desition == 1:
			return "m1"
		elif desition == 2:
			return "fe1"
		elif desition == 3:
			return "fe5"
		elif desition == 4:
			return "fe2"
def foothills2():
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
		if looted[7]==False:
			looted[7]=True
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
1 to move south
2 to move east
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "fo2"
		elif desition == 1:
			return "fe6"
		elif desition == 2:
			return "fo3"
def foothills3():
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
		if looted[8]==False:
			looted[8]=True
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
2 to move west
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "fo3"
		elif desition == 1:
			return "s1"
		elif desition == 2:
			return "fo2"
def forest():
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
	if monster[9] == True:
		if monbattle("killer bunny") != "live":
			return "dead"
		monster[9] = False
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
		if looted[9]==False:
			looted[9]=True
			temp = getloot(3)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move north
2 to move south
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "f"
		elif desition == 1:
			return "fe4"
		elif desition == 2:
			return "fe3"
def swamp1():
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
		if looted[10]==False:
			looted[10]=True
			temp = getloot(3)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move north
2 to move west
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "s1"
		elif desition == 1:
			return "s3"
		elif desition == 2:
			return "fo3"
def swamp2():
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
		if looted[11]==False:
			looted[11]=True
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
1 to move south
2 to move west
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "s2"
		elif desition == 1:
			return "s3"
		elif desition == 2:
			return "m2"
def swamp3():
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
	if monster[13]==True:
		monster[13]==False
		if monbattle("shreck") != "live":
			return "dead"
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
		print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move north
2 to move south
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "s3"
		elif desition == 1:
			return "s1"
		elif desition == 2:
			return "s2"
def mountan1():
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
		if looted[14]==False:
			looted[14]=True
			temp = getloot(3)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move north
2 to move south

""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "m1"
		elif desition == 1:
			return "bod"
		elif desition == 2:
			return "fo1"
def mountan2():
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
		if looted[15]==False:
			looted[15]=True
			temp = getloot(3)
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
			return "m21"
		elif desition == 1:
			return "s2"
		elif desition == 2:
			return "m3"
def mountan3():
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
	if monster[16] == True:
		if monbattle("dragon") != "live":
			return "dead"
		monster[16] = False
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
		if looted[16]==False:
			looted[16]=True
			temp = getloot(3)
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
			return "m3"
		elif desition == 1:
			return "m2"
		elif desition == 2:
			return "m4"
def mountan4():
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
		if looted[17]==False:
			looted[17]=True
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
2 to move west
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "m4"
		elif desition == 1:
			return "m3"
		elif desition == 2:
			return "m5"
def mountan5():
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
	if monster[18] == True:
		if monbattle("robot") != "live":
			return "dead"
		monster[18] = False
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
		if looted[18]==False:
			looted[18]=True
			temp = getloot(3)
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
			return "m5"
		elif desition == 1:
			return "m4"
		elif desition == 2:
			return "g1"
def glich1():
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
	print("you take 10 damage from the enviorment")
	health-=10
	if monster[19] == True:
		if monbattle("dragon") != "live":
			return "dead"
		monster[19] = False
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
		if looted[19]==False:
			looted[19]=True
			temp = getloot(3)
			loot.append(temp)
			print(f"you got a {temp}")
		else:
			print("you dont find anything")
	if desition == 1:
		while True:
			try:
				desition=input("""
0 to return
1 to move north
2 to move east
""")
				if desition in [0,1,2]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition	== 0:
			return "g1"
		elif desition == 1:
			return "g2"
		elif desition == 2:
			return "m5"
def glich2():
def bod():
def glichcidicel():
def grail():
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
