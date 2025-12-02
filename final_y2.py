#setup
#Define map
#Make team manager
#	Make init
#		Hp
#		Damage
#		Drops
#		Resistance
#		Teir
#		Name
#		Description
#		Level
#		Mana
#		Xp
#		
#	Make get description
#		Get description
#	Make heal
#		Add heal to hp max at max hp
#	Make damage
#		If tier is not 0
#			If damage type is resistant
#				Subtract half damage from hp min at 0
#				Output damage
#		Subtract damage from hp min at 0
#		Output damage
#	Make if dead
#		remove
#	Make remove
#		If tier is 0
#			Output person damaged is unconscious
#			Set person damaged to unconscious
#			Remove person damaged from targets
#		Else
#			Grant player drops
#			
#			Output you got x and killed monster
#			Remove enemy
#	Make level up
#		Add one to level
#		Add 10 to max hp
#		Hp is max hp
#		Add 10 to max mana
#		Mana is max mana
#		Monster spawn rate +5 max at 70
#		Add 10 to bace damage
#	Make add buff
#		Damage to bace damage
#	Make atack
#		If player team go
#			Iterate thru conchis players
#			Get chose from enemies remaining use item or run
#			If atack
#				Set damage to bace damage
#				Damage enemies by damage
#			If use item
#				Output inventory
#				Use what player inputs what to use
#			If run
#				If randomnumber 1-5 is 5
#					Output run failed
#		Else
#			Iterate thru enemies
#				num=Randomnumber 1-tier
#				If num is 1
#					Damage random player
#				If num is 2
#					Damage all players
#				If num is 3
#					Damage random player with damage type of resistant
#				If num is 4
#					Damage all players with damage type of resistant
#
#				
#
#Make inventory manager
#Make init
#	Inventory = startin invintory
#Make use
#	If item useable
#		Pass item into evect func
#	Else
#		Raise error you found a error
#Make grant
#	Inventory add item if useable
#	Else
#		
#Make get length
#	Return length of inventory
#Make get inventory
#	Return inventory
#Make effect function with parameters of effect and person
#	If heal is in list effect 
#		Team manager target heal
#	Or if bomb is in list efect
#		Team manager tartget take damage
#Make prosses position function with x,y,description,speshal is defalt to none, item is defalt to none
#	pos=location on map
#	If pos is watter
#		output(“not a valid location
#		Location is iligal
#		Monster spawn rate is 2
#	If pos is lava
#		output(“not a valid location
#		Location is iligal
#		Monster spawn rate is 2
#	If pos is item
#		Grant item
#	Ect
#func setup
#	Init inventory with 3 potions and 1 magic weppon
#	party=team manager starting stats
#If in file main
#	Input =Get do you want to play
#	If input is yes
#		setup
#		Set pos to 15,18
#		Set battal chance to 20
#		While length of continuous players is not 0
#			Chose from north,south,east,west (remove inposipble options)
#			If north subtract 1 from y pos
#			If south add 1 to y pos
#			If east add 1 to x
#			If west subtract 1 from x
#			Process position
#			Battal chance add monster spawn rate times 10
#			num=Radom number 1-100
#			If is num less than battal chance
#				Iterate thru range (1,min(round((random num-num)/33),3)
#					Random monster 1-min(level,4)add to monsters
#					Monster team=team manager(unpacked monsters)
#While length of monster team is not 0 and length of continuous players is not 0
#	Attack plater turn
#	Atack monster turn
#While xp>= 25
#	Level up
#	xp-25
#			Elif position is speshal
#				If speshal = something
#					Do something
#				ect
#			Elif position is item
#				Grant item
#			Elif position is town
#				While true
#					Options are shop gamble and leave
#					If shop
#						Options are x y and z for x y and z
#					If gamble 
#						How much to gamble max gold
#						Optins are heads tails
#						if random num=1 and heads
#							Gold =gamble+gamble
#						If random num=2 and tails
#							Gold =gamble+gamble
#						Else
#							Lost
#					If leave 
#						Add one to x
#				
#	Else
#	Output goodbye

import util_functions
import random
class LogicError(Exception):
	print(f"logic error at line {util_functions.get_linenumber()}")
map=[["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","l","i","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","h","h","h","l","h","h","speshal","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","h","h","h","h","ni","l","l","h","h","i","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","h","u","h","h","l","l","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","u","u","h","l","h","s","l","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","u","c","h","b","h","h","l","l","h","u","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","h","h","h","h","h","l","h","h","h","h","h","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","h","u","f","f","f","f","f","f","f","f","f","f","h","u","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","h","f","f","f","f","f","f","s","f","f","f","f","f","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","f","f","f","f","f","f","c","f","f","f","t","p","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","f","f","s","f","f","f","f","f","f","f","f","p","f","f","ni","f","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","f","i","f","f","f","f","f","f","f","i","p","p","p","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","f","f","f","f","f","f","f","f","f","f","p","p","p","f","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","r","f","f","f","f","f","f","f","f","f","p","p","p","f","f","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","t","p","r","f","r","f","f","p","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","p","t","w","w","i","w","w"],
["w","w","w","w","w","w","p","f","b","r","f","f","p","p","p","p","p","p","c","u","f","f","f","f","f","f","f","f","f","f","w","w","f","f","f","w"],
["w","w","w","w","w","f","p","f","f","t","r","f","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","b","w","f","p","f","f","w"],
["w","w","w","w","f","p","p","p","f","f","f","b","r","c","p","spawn","p","p","p","p","f","f","f","f","f","f","f","f","r","s","p","p","p","p","f","w"],
["w","w","w","w","f","p","p","p","p","p","p","p","p","r","t","t","p","p","p","p","r","f","f","f","f","f","f","f","r","p","t","p","p","p","f","w"],
["w","w","w","w","f","c","f","f","p","p","p","p","p","r","t","t","r","r","p","r","p","f","f","f","f","f","f","f","f","r","p","p","p","p","w","w"],
["w","w","w","w","f","f","f","f","p","p","p","p","p","p","r","r","p","c","r","p","t","f","f","s","f","f","f","c","f","f","f","f","f","w","w","w"],
["w","w","w","w","f","f","f","f","p","p","p","p","p","p","p","p","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","w","w","w"],
["w","w","w","w","f","f","f","f","f","f","f","f","f","f","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","f","f","w","w","w"],
["w","w","w","w","w","s","s","f","f","s","s","s","s","s","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","f","w","w","w","w"],
["w","w","w","w","w","w","s","s","s","s","s","w","w","s","s","s","f","f","f","f","f","f","f","f","f","f","f","w","aw","aw","aw","aw","w","w","w","w"],
["w","w","w","w","w","w","s","s","s","s","w","w","w","w","s","s","s","f","f","f","f","s","s","s","s","s","w","aw","aw","aw","aw","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","s","s","w","w","w","w","w","s","s","s","s","s","s","s","s","s","s","s","w","w","aw","aw","i","aw","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","s","s","w","w","w","s","s","s","s","s","s","s","s","s","i","s","s","s","w","w","aw","aw","aw","aw","aw","aw","w","w","w"],
["w","w","w","w","w","i","s","s","w","w","w","s","s","s","s","s","s","s","s","t","s","s","s","s","w","w","w","w","aw","aw","ni","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","s","s","s","s","s","s","s","s","s","s","s","s","w","w","w","w","w","w","aw","aw","aw","w","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","s","s","s","s","s","i","s","s","s","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","w","s","s","s","s","s","s","s","ni","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]

class TeamManager:
	def __init__(self,hp,dmg,drops,resistance,teir,name,description,level=1,mana=10,xp=0):
		self.hp_max=hp
		self.hp=hp
		self.dmg=dmg
		self.drops=drops
		self.resistance=resistance
		self.teir=teir
		self.name=name
		self.description=description
		if teir[0]<0:
			self.level=level
			self.mana_max=mana
			self.mana=mana
			self.xp=xp
			self.type={"team member 1":{"hp:":self.hp[0],"dmg":self.dmg[0],"name":self.name[0],"description":self.description[0],"level":self.level[0],"mana":self.mana[0],"xp":self.xp[0]},
"team member 2":{"hp:":self.hp[1],"dmg":self.dmg[1],"name":self.name[1],"description":self.description[1],"level":self.level[1],"mana":self.mana[1],"xp":self.xp[1]},
"team member 3":{"hp:":self.hp[2],"dmg":self.dmg[2],"name":self.name[2],"description":self.description[2],"level":self.level[2],"mana":self.mana[2],"xp":self.xp[2]}}
		else:
			if hp[0]!=None:
				self.type=None
			elif hp[1]!=None:
				self.type=None
			elif hp[2]!=None:
				self.type=None
	def getattribute(self, name):
		return self.description
	def heal(self,heal_amount,person):
		self.hp[person]=min(self.hp[person]+heal_amount,self.hp_max[person])
	def damage(self,damage_amount,damage_type,person):
		if self.teir[person]!=0:
			self.hp[person]=max(self.hp[person]-damage_amount,0)
			print(f"{self.name[person]} took {damage_amount} damage")
			return
		self.hp[person]=max(self.hp[person]-damage_amount,0)
		print(f"{self.name[person]} took {damage_amount} damage")
	def if_dead(self,person,targets):
		if self.hp[person]<=0:
			self.remove(person,targets)
	def remove(self,person,targets):
		if self.teir[person]==0:
			print(f"{self.name[person]} is unconscious")
			self.hp[person]=-1
			
		else:
			print(f"You got {self.drops[person]} and killed {self.name[person]}")
			targets.pop(person)
	def level_up(self,person):
		self.level[person]+=1
		self.hp_max[person]+=10
		self.hp[person]=self.hp_max[person]
		self.mana_max[person]+=10
		self.mana[person]=self.mana_max[person]
		if self.level[person]%7==0:
			util_functions.monster_spawn_rate=min(util_functions.monster_spawn_rate+5,70)
		self.dmg[person]+=10
	def add_buff(self,damage_buff,person):
		self.dmg[person]+=damage_buff
	def attack(self,players_go,continuous_players,enemies,inventory):
		if players_go:
			for i in range(len(continuous_players)):
				print("Choose from attack, use item, or run")
				choice=util_functions.get_valid_type(str,"Choose action","that is not a valid action",["attack","use item","run"])
				if choice=="attack":
					damage=self.dmg[i]
					target=random.randint(0,len(enemies)-1)
					enemies.damage(damage,"normal",target)
				elif choice=="use item":
					print(inventory.get_inventory())
					print("What do you want to use?")
					item_choice=util_functions.get_valid_type(str,"Choose item","that is not a valid item",list(inventory.get_inventory().keys()))
					inventory.use(item_choice,continuous_players,i)
				elif choice=="run":
					if random.randint(1,5)==5:
						print("Run failed")
		else:
			for i in range(len(enemies.hp)):
				num=random.randint(1,enemies.teir[i])
				if num==1:
					target=random.randint(0,len(continuous_players)-1)
					enemies.damage(enemies.dmg[i],"normal",target)
				elif num==2:
					for j in range(len(continuous_players)):
						enemies.damage(enemies.dmg[i],"normal",j)
				elif num==3:
					target=random.randint(0,len(continuous_players)-1)
					enemies.damage(enemies.dmg[i]//2,"resistant",target)
				elif num==4:
					for j in range(len(continuous_players)):
						enemies.damage(enemies.dmg[i]//2,"resistant",j)
	def get_continuous_players(self):
		continuous_players=[]
		for i in range(3):
			if self.hp[i]>0:
				continuous_players.append(i)
		return continuous_players
	def gain_mana(self,mana_amount,person):
		self.mana[person]=min(self.mana[person]+mana_amount,self.mana_max[person])
	def magic_attack_choise(self,person,inventory):
		gems=[]
		print("all mana atacks cost 10 mana")
		prompt="Choose a chaos gem to use:\n0 to cancel"
		for gem in inventory.get_inventory():
			if gem["type"]=="chaos gem":
				gems.append(gem)
		for iter,x in enumerate(gems):
			prompt+=f"\n{iter} for {x['name']}: {x['description']}"
		util_functions.get_valid_type(int,prompt,"that is not a gem that is available",list(range(0,len(gems)+1)))-1
		if choice==-1:
			return
		if self.mana[person]>=10:
			self.mana[person]-=10
		choice=gems[choice]
		if choice =="water":
			enemies.damage(choice["damage"],"water",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="fire":
			enemies.damage(choice["damage"],"fire",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="wind":
			enemies.damage(choice["damage"],"wind",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="darkness":
			enemies.damage(choice["damage"],"darkness",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="frost":
			enemies.damage(choice["damage"],"ice",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="lightning":
			enemies.damage(choice["damage"],"electric",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="resurrection":
			party.heal(choice["heal"],util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(party.get_continuous_players())))))
enemies=TeamManager([50,50,50],[10,15,20],[{"name":"bomb core","quantity":1,"useable":True,"effect":{"bomb core":30}},{"name":"lightning core","quantity":1,"useable":True,"effect":{"lightning core":30}},{"name":"blizzard core","quantity":1,"useable":True,"effect":{"blizzard core":30}}],[ "fire","electric","ice"],[1,2,3],["Goblin","Orc","Troll"],["A weak goblin","A strong orc","A huge troll"])
class InventoryManager:
	def __init__(self,starting_inventory):
		self.inventory=starting_inventory
	def use(self,item,continuous_players,person):
		if item in self.inventory and self.inventory[item]["useable"]:
			self.effect_function(self.inventory[item]["effect"],continuous_players,person)
			self.inventory[item]["quantity"]-=1
			if self.inventory[item]["quantity"]<=0:
				self.inventory.pop(item)
		else:
			raise LogicError
	def grant(self,item):
		if item["useable"]:
			if item["name"] in self.inventory:
				self.inventory[item["name"]]["quantity"]+=item["quantity"]
			else:
				self.inventory[item["name"]]=item
	def get_length(self):
		return len(self.inventory)
	def get_inventory(self):
		return self.inventory
	def effect_function(self,effect,continuous_players,person):
		if "heal" in effect:
			party.heal(effect["heal"],person)
		if "heal+" in effect:
			party.heal(effect["heal+"],person)
		if "heal++" in effect:
			party.heal(effect["heal++"],person)
		if "ether" in effect:
			party.gain_mana(effect["ether"],person)
		if "elixir" in effect:
			party.gain_mana(effect["elixir"],person)
			party.heal(effect["elixir"],person)
		if "hi-ether" in effect:
			party.gain_mana(effect["hi-ether"],person)
		if "hi-elixir" in effect:
			party.gain_mana(effect["hi-elixir"],person)
			party.heal(effect["hi-elixir"],person)
		if "ඞ" in effect:
			party.heal(party.hp_max[person],1)
			party.heal(party.hp_max[person],2)
			party.heal(party.hp_max[person],3)
			party.gain_mana(party.mana_max[person],1)
			party.gain_mana(party.mana_max[person],2)
			party.gain_mana(party.mana_max[person],3)
			enemies.damage(effect["debug item"],"normal",1)
			enemies.damage(effect["debug item"],"normal",2)
			enemies.damage(effect["debug item"],"normal",3)
		elif "bomb core" in effect:
			enemies.damage(effect["bomb core"],"fire",1)
			enemies.damage(effect["bomb core"],"fire",2)
			enemies.damage(effect["bomb core"],"fire",3)
		elif "lightning core" in effect:
			enemies.damage(effect["lightning core"],"electric",1)
			enemies.damage(effect["lightning core"],"electric",2)
			enemies.damage(effect["lightning core"],"electric",3)
		elif "blizzard core" in effect:
			enemies.damage(effect["blizzard core"],"ice",1)
			enemies.damage(effect["blizzard core"],"ice",2)
			enemies.damage(effect["blizzard core"],"ice",3)
		elif "fire core" in effect:
			enemies.damage(effect["fire core"],"fire",person)
		elif "electric core" in effect:
			enemies.damage(effect["electric core"],"electric",person)
		elif "ice core" in effect:
			enemies.damage(effect["ice core"],"ice",person)
		elif "chaos gem" in effect:
			party.magic_attack_choise(person,self,inventory)
monster_dict={
"dragon":{"tier":2,"hp":150,"dmg":30,"drops":{"name":"dragon scale","quantity":1,"useable":True,"effect":{"heal":50}},"resistance":"fire","description":"A large fire-breathing dragon.","speshal spwan location":None},
"blob":{"tier":1,"hp":80,"dmg":15,"drops":{"name":"slime gel","quantity":1,"useable":True,"effect":{"heal":20}},"resistance":"water","description":"A gooey blob that oozes around.","speshal spwan location":None},
"orc":{}
"troll"
"goblin"
"knight"
"construct"
"Animated statue" 
"Possessed cow"
"mermaid"
"Lava monster"
"Fish lord"
"Lava warden"
"blain"
"liam"
"yeti"
"ice"
"Nyx-spawn"
}
def get_random_monsters(party_level,locaion):
	monsters=[]
	num_monsters=random.randint(1,min(max((party_level-random.randint(0,party_level))//33,1),3))
	for i in range(num_monsters):
		groop_chalange_total=(party_level//2)+random.randint(0,party_level//2)
		possible_monsters=[]
		for j in monster_list):
		
	return monsters
def process_position(x,y,description,special=None,item=None):
	pos=map[y][x]
	if pos=="w":
		print("not a valid location")
		location="illegal"
		util_functions.monster_spawn_rate=2
	elif pos=="l":
		print("not a valid location")
		location="illegal"
		util_functions.monster_spawn_rate=2
	elif pos=="i":
		util_functions.inventory.grant(item)
	elif pos=="speshal":
		if special=="something":
			pass
	return {"position":pos,"description":description,"special":special,"item":item}
inventory=InventoryManager({"potion":{"name":"potion","quantity":3,"useable":True,"effect":{"heal":20}}})
party=TeamManager([100,100,100],[10,10,10],[None,None,None],[None,None,None],[-1,-1,-1],["Zack","Amilia","Clang"],["your friend","you","a compiler for the language c++ that is also a deity"],[1,1,1],[10,0,20],[0,0,0])#setup later
monster_spawn_rate=20
if __name__=="__main__":
	input_play=	util_functions.get_valid_type(str,"Do you want to play?","that is not a valid answer",["yes","no"])
	if input_play.lower()=="yes":
		x_pos=15
		y_pos=18
		battle_chance=20
		while len(party.get_continuous_players())>0:
			print("Choose from north, south, east, west")
			choice=util_functions.get_valid_type(str,"Choose direction","that is not a valid direction",["north","south","east","west"])
			if choice=="north":
				y_pos-=1
			elif choice=="south":
				y_pos+=1
			elif choice=="east":
				x_pos+=1
			elif choice=="west":
				x_pos-=1
			location=process_position(x_pos,y_pos,None)
			battle_chance+=monster_spawn_rate*10
			num=random.randint(1,100)
			if num<battle_chance:
				monster_team=TeamManager(get_random_monsters(party.level,location))
				while len(monster_team.hp)>0 and util_functions.get_continuous_players_length()>0:
					party.attack(True,util_functions.get_continuous_players(),monster_team,util_functions.inventory)
					party.attack(False,util_functions.get_continuous_players(),monster_team,util_functions.inventory)
				while party.xp>=25:
					party.level_up(1)
					party.level_up(2)
					party.level_up(3)
					party.xp-=25
	else:
		print("Goodbye")