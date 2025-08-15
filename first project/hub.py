import random
import time
import os
import smtplib
import ssl
from email.message import Emai
turn = ""
runhub = True
debuging = 1
invertedP = ""
iterationP = 1
runnerP = ""
var = 0
hubo = 0
operation = 0
easterEggCount = 5
maxGuessCount = 10
minGuess = 1
maxGuess = 100
playCount = 0
playAgain = True
debuging = False
typing = True
type_speed = .01
player_score = 0
com_score = 0
board = [None] * 9
from dataclasses import dataclass
from copy import copy, deepcopy
import time, random
from typing import List, Dict, Tuple
@dataclass
class Monster:
	name:str
	health:str
	damage:str
	lootLevel:int = 1

@dataclass
class Item:
	name:str
	health:int = 0
	damagebuff:float = 0
	predamage:int = 0
	luck:int = 0
	life:int = None
	type:str = "consumable"

@dataclass
class Moves:
	north:str = None
	south:str = None
	east:str = None
	west:str = None
	def selectMove(self):
		return selectOption([
			("North", self.north),
			("South", self.south),
			("East", self.east),
			("West", self.west)
		])

@dataclass
class Location:
	description:str
	moves:Moves
	itemRarity:int = 1
	hasLoot:bool = True
	monster:Monster = None

#best
goodLoot = [
	Item("Holy Hand Grenade: instakill", damagebuff=100000000000, type="consumable"),
	Item("Holy Hand Grenade: instakill", damagebuff=100000000000, type="consumable"),
	Item("Holy Hand Grenade: instakill", damagebuff=100000000000, type="consumable"),
	Item("RPG: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("RPG: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("RPG: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Sten MK II: tends to misfire sometimes has bullets bounce off of target +20% damage", damagebuff=.20, type="weapon"),
	Item("Apache Revolver: you can use it like a gun (terrible aim) a knife (way too flexible) or an iron fist (the only safe way to use it) +30% damage", damagebuff=.30, type="weapon"),
	Item("Pickled Leprechaun Head: +1 luck for 7 turns", life=7, type="timed"),
	Item("Luck Potion: +1 luck for 10 turns", life=10, type="timed")
]
#worst
norm = [
	Item("Nuke Kill All", health=-100000000,damagebuff=0, type="consumable"),
	Item("Stick +5% damage", damagebuff=.5, type="weapon"),
	Item("Health +10 potion", health=10, type="consumable"),
	Item('Deodorant', type='consumable'),
	Item(name='luck charm +1 luck for a turn', life=1, type="timed"),
	Item(name='luck potion +1 luck for 2 turns', life=2, type="timed")
]
#meh
rearer = [
	Item('A Peace of a Lemon', health=20,  type='consumable'),
	Item('Sword + 10% damage', damagebuff=.1, type='weapon'),#damageBuff ?
	Item('Health + 20 potion', health=20, type='consumable'),
	Item('Slingshot +5% damage', damagebuff=.05, type='weapon'),
	Item('A 15 foot long pole', health=2, type='consumable'),
	Item('clover +1 luck for 3 turns', luck=1, type='timed'),
	Item('luck potion +1 luck for 4 turns', luck=1, type='timed')]


worldTemplate = {
	"start": Location(description="French castle (how did you get in here anyway hon hon hon)", itemRarity=3, moves=Moves(east="field4")),
	"field1": Location(description="You are in a field of grass",itemRarity=1,moves=Moves(north="foothills1")),
	"field2": Location(description="You are in a field of goat heads", itemRarity=1,moves=Moves(west="field3",east="foothills1")),
	"field3": Location(description="You are in a field of mud",itemRarity=2,moves=Moves(north="forest",east="field2")),
	"field4": Location(description="You are in a field of molten rice",itemRarity=1, moves=Moves(south="forest")),
	"field5": Location(description="You are in a field of grass",itemRarity=2,moves=Moves(west="foothills1",east="field6"), monster=Monster(name="flying snake", health=50, damage=10, lootLevel=3)),
	"field6": Location(description="You are in a field of coconuts",itemRarity=2,moves=Moves(north="foothills2", west="field5")),
	"foothills1": Location(description="you are in a foothills biome",itemRarity=3,moves=Moves(north="mountain1",south="field1",west="field2",east="field5")),
	"foothills2": Location(description="you are in a foothills biome", itemRarity=2,moves=Moves(east="foothills3", south="field6")),
	"foothills3": Location(description="you are in a foothills biome", itemRarity=2,moves=Moves(east="swamp1",west="foothills2")),
	"forest": Location(description="you in big fat forest", itemRarity=3,moves=Moves(north="field4",south="field3"), monster=Monster(name="killer bunny", health=15, damage=10, lootLevel=3)),
	"swamp1": Location(description="yucky swamp you in hmmmm?", itemRarity=3,moves=Moves(north="swamp3",west="foothills3")),
	"swamp2": Location(description="in yucky swamp am i hmmmm?", itemRarity=2,moves=Moves(west="mountain2", south="swamp3")),
	"swamp3": Location(description="swamp yucky in both are we hmmmm?", itemRarity=3,moves=Moves(north="swamp2",south="swamp1"), monster=Monster(name="shreck", health=300, damage=2, lootLevel=3)),
	"mountain1": Location(description="you are in a mountain", itemRarity=3,moves=Moves(north="BOD", south="foothills1")),
	"mountain2": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="mountain3", east="swamp2")),
	"mountain3": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="mountain4", east="mountain2"), monster=Monster(name="dragon", health=100, damage=50, lootLevel=3)),	
	"mountain4": Location(description="you are in a mountain", itemRarity=2,moves=Moves(west="mountain5", east="mountain3"), monster=Monster(name="robot", health=50, damage=10, lootLevel=3)),
	"mountain5": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="glitchedPlains1", east="mountain4"), monster=Monster(name="robot", health=200, damage=20, lootLevel=3)),
	"BOD": Location(description="BODY", hasLoot=False, moves=Moves(north="moun1tain5")),
	"glitchedPlains1": Location(description="You have entered the glitched plains", itemRarity=3, moves=Moves(north="glitchedPlains2", east="mountain5"), monster=Monster(name="robot", health=250, damage=50, lootLevel=3)),
	"glitchedPlains2": Location(description="You have entered the glitched plains", itemRarity=2, moves=Moves(west="glitchedCitadel", south="glitchedPlains1"), monster=Monster(name="robot", health=300, damage=50, lootLevel=3)),
	"glitchedCitadel": Location(description="You have entered the glitched citadel. This is where the boss is good luck from the game itsleff", hasLoot=False, moves=Moves(west="holyGrail", east="glitchedPlains2"), monster=Monster(name="The Programer", health=1000, damage=50)),
	"holyGrail": Location(description="grail",hasLoot=False, moves=Moves())
}

world: Dict[str,Location]
location: Location
inventory: List[Item]
health: int
damage: int
color: str
name: str
quest = "To seek the Holy Grail"
playedAmount = 0
damagebuff=0
def initGame():
	global ep
	time.sleep(1)
	gointor = 1
	if ep == 0:
		while gointor != 2000:
			for x in range(random.randint(1,gointor)):
				print("  ",end="")
			for x in range(round(gointor/10)+1):
				print(random.randint(0,1),end="")
			print()
			time.sleep(random.uniform(0,3/gointor))
			if gointor %50 ==0:
				print(""" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                                                                              """)
			gointor+=1
		print(""" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                                                                              """)
		time.sleep(.7)
		for x in range(10000):
			print()
	global world
	global location
	global inventory
	global health
	global damage
	global color
	global name
	global playedAmount
	world = deepcopy(worldTemplate)
	location = world["field4"]
	inventory = []
	health = 100
	damage = 5
	name = input("whats your name adventurer (type your name then press enter to continue): ")
	color = input(f"hello {name} whats your favorite color: ")
	type_text(f"""hello {name} who likes the color {color}, your quest is "{quest}" good luck""")
	type_text("search for loot to get loot")
	type_text("battle monsters")
	type_text("get the holy grail")
	type_text("win")
	playedAmount+=1
	
def move(loc: str):
	global location
	global inventory
	for item in [item for item in inventory if item.life != None]:
			item.life -= 1
			if item.life == 0:
				type_text(f"Your {item.name} has expired")
				inventory.remove(item)
	location = world[loc]
	#print(f'moved to: {location}')

def selectOption(options: List[Tuple[str,any]], cancelable = True, noOptionText = "You can't do that.") -> any:
	options = [x for x in options if x[1] != None]
	if len(options) == 0:
		type_text(noOptionText)
		return None
	while True:
		try:
			type_text("Select an option:")
			if cancelable:
				type_text("0. Cancel")
			for i, option in enumerate(options):
				type_text(f"{i+1}. {option[0]}")
			value = int(input("Choose wisely: "))
			type_text()
			if cancelable and value == 0:
				return None
			elif value < 1 or value > len(options):
				type_text("try again")
			else:
				return options[value-1][1]
		except ValueError:
			type_text("Invalid input")

def randomItem(rarity = 0):
	if sum([item.luck for item in inventory]) > 0:
		rarity += 1
	if rarity == 1:
		return copy(random.choice(norm))
	elif rarity ==2:
		return copy(random.choice(rearer))
	elif rarity ==3:
		return copy(random.choice(goodLoot))
	elif rarity ==4:
		return Item("ball of thorns", health=50 ,type="consumable")
	raise Exception(f"Invalid rarity {rarity}")

def useItem():
	global health
	global inventory
	item:Item = selectOption([(item.name, item) for item in inventory if item.type == "consumable"], noOptionText="You have no items to use")
	if item == None:
		return False
	health += item.health
	if item.health > 0:
		type_text(f"You used {item.name} and gained {item.health} health")
	else:
		type_text(f"You used {item.name} and lost {-item.health} health")
	type_text(f"You have {health} health left")
	inventory.remove(item)

def BOD():
	global name
	global playedAmount
	global color
	nam = input("""you come to a rope bridge spanning a casum and a man stops you and says "Stop. Who would cross the Bridge of Death must answer me these questions three, ere the other side he see. What... is your name: """)
	if nam.lower() != name.lower():
		type_text("wrong *as you are thrown into the casum")
		type_text("you die and aliens take your body and are diapointed that you cant play poker")

		type_text("game over")
		return "dead"
	else:
		nam = str(input("What... is your quest: "))
		if nam.lower().strip() != quest.lower().strip():
			type_text("wrong *as you are thrown into the casum*")
			type_text("you die and are turned into a lemon")
			type_text("game over")
			return "dead"
		if playedAmount >1:
			nam = input("What... is the air-speed velocity of an unladen swallow: ").lower()
			if nam == "What do you mean? An African or a European swallow?".lower():

				type_text(" Huh? I... I don't know that. AUUUUUUUGGGGGGGGGGGHHH!! *as he is thrown into the casum*")
				type_text("you successfully make it across the bridge")
				return "mountain5"
			else:
				type_text("wrong *as you are thrown into the casum")
				type_text("you die and joe takes your apendix")
				type_text("game over")
				return "dead"
		else:
			nam = input("What... is your favorite colour: ").lower()
			if nam != color.lower():
				type_text("wrong *as you are thrown into the casum*")
				type_text("you die and billy the bird makes you into a nest")
				type_text("game over")
				return "dead"
			else:
				type_text("you may pass")
				type_text("you make it across the bridge")
				return "mountain5"
				
def holyGrail():
	type_text("You have found the Holy Grail!")
	if input("do you drink(y/n):").lower=="y":
		print("""Traceback (most recent call last):
  File "/Users/this is a joke/personal/pythonPlay/game.py", line ∞, in <all>
    item = banana
           ^^^^^^
  File "/Users/also a joke/personal/pythonPlay/game.py", line ∞, in lemon
    raise Exception(f"Invalid rarity {good food}")
Exception: Invalid rarity 2037946809832759832""")
		time.sleep(.01)
		type_text("BACK FROM THE DEAD CODE")
		type_text("hahaha")
		type_text("P.S. you win")
		return "dead"
	else:
		return "dead"


def totalDamage():
	"""returns total damage"""
	return (sum([item.damagebuff for item in inventory ])+1)*damage

def battle():
	global health
	global inventory
	global location
	predamageItems = [item for item in inventory if item.predamage > 0]
	monster = location.monster
	type_text(f"A {monster.name} appears!")
	for item in predamageItems:
		type_text(f"you used an {item.name} and did {item.predamage} damage")
		monster.health-=max(item.predamage, 0)

	while True:
		type_text(f"The {monster.name} has {monster.health} health left")
		option = selectOption([
			("Fight", "fight"),
			("Use Item", "useItem")
		], cancelable=False)
		if option == "fight":
			type_text(f"You fight the {monster.name}")
			attack = totalDamage()
			type_text(f"You deal {attack} damage")
			monster.health = max(0, location.monster.health - attack)
			if monster.health <= 0:
				type_text(f"You have defeated the {monster.name}")
				item = randomItem(monster.lootLevel)
				type_text(f"{monster.name} dropped a {item.name} and you picked it up")
				inventory.append(item)
				location.monster = None
				return True
		elif option == "useItem":
			if useItem() == False:
				continue
		type_text(f"{location.monster.name} attacks!")
		health -= location.monster.damage
		if health <= 0:
			type_text("You have died and a antelope ate your earlobes")
			return False
		type_text(f"You have {health} health left")
playedAmount = 0
def the_game():
	type_text("welcome i am the GAME MASTER")
	while True:
		ep = 0
		if input("do you want to play(y/n)").lower()!="y":
			break
		if input("do you have epalepsy(y/n): ").lower() != "y":
			ep = 1
		initGame()

		while True:
			if location.description == "BODY":
				if BOD()=="dead":
					break
				else:
					move("mountain5")
			elif location.description == "grail":
				holyGrail()
			else:
				type_text(location.description)
				if location.monster:
					if battle() == False:
						break
				if health<0:
					type_text("you died")
					type_text("game over")
					break
				option = selectOption([
					("Move", "move"),
					("Search for loot", "search"),
					("Use Item", "useItem")
				], False)
				if option == "useItem":
					useItem()
				elif option == "search":
					if location.hasLoot:
						item = randomItem(location.itemRarity)
						location.hasLoot = False
						inventory.append(item)
						type_text(f"You found a {item.name}")
					else:
						type_text("You found nothing")
				elif option == "move":
					place = location.moves.selectMove()
					if place:
						move(place)
	type_text("ok sending you back to the hub")
def dwane_the_rock():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	player_score = 0
	com_score = 0
	type_text("The Rock wlcomes you to play Rock Paper Scissors")
	while True:
		type_text("1 for rock")
		type_text("2 for scissors")
		type_text("3 for paper")
		type_text("4 to quit")
		com_move = str(random.randint(1,3))
		if com_move == "1":
			com_prin = "🪨"
		if com_move == "2":
			com_prin = "✂️"
		if com_move == "3":
			com_prin = "📄"
		while True:
			players_move = input("The Rock asks what do you want:")
			players_move = check_int(players_move)
			if check_int(players_move) != "":
				break
			else:
				type_text("The Rock dosn't think that that is a valid input")
		if players_move == 1:
			players_move = "🪨"
		elif players_move == 2:
			players_move = "✂️"
		elif players_move == 3:
			players_move = "📄"
		elif players_move ==4:
			type_text("The Rock will send you back to the hub.")
			return
		print(f"The Rock: {com_prin} Player: {players_move}")

		if players_move == com_prin:
			type_text("The Rock is disaponted")
		elif players_move == "🪨" and com_prin == "✂️" or players_move == "✂️" and com_prin == "📄" or players_move == "📄" and com_prin == "🪨":
			type_text("how did you beat The Rock? The Rock will crush you.")
			player_score +=1
		else:
			type_text("HAHAHAHA The Rock wins once again")
			com_score += 1
		print(f"The Rock: {com_score} player: {player_score}")
def check_input(input,valid_inputs):
	if input  in  valid_inputs:
		return input
	return ""
def check_int(input):
	try:
		return int(input)
	except ValueError:
		type_text("please enter a number")
	return ""
def check_float(input):
	try:
		return float(input)
	except ValueError:
		type_text("not a valid input")
		return""
def type_text(textt):
	if typing == True:
		for x in textt:
			print(x, end = "", flush = True)
			time.sleep(random.uniform(.01,type_speed))
		print("")
	else:
		print(textt,flush=True)
def anagram():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	type_text("Hi i am Anny")
	while True:
		anagramt = []
		outputt = ""
		doitt = "12345"
		wordt = input("what is the word that you want into anagram or type stop to stop: ")
		if wordt == "stop":
			type_text("sending you back to Hubby")
			break
		if wordt == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			randt = len(wordt)
			for y in doitt:
				outputt = ""
				anagramt = []
				for x in wordt:
					anagramt.insert(random.randint(1,randt),x)
				for i in anagramt:
					outputt = outputt + i
				print (outputt)
def calculator():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	operation = 0
	a = "n/a"
	b = "n/a"
	type_text("Hi this is Calcu. What do you want me to calculate today")
	operation = 0
	while True:
		type_text("0 to stop")
		type_text("1 for devision")
		type_text("2 for multiplication")
		type_text("3 for subtraction")
		type_text("4 for addition")
		type_text("5 for modulo")
		type_text("6 for factoring")
		operation = input("what do you want: ")
		if operation == "1" :
			while True:
				a = check_float(input("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(input("what is the second number:"))
				if b != "" and b != 0:
					break
			if b == 0 :
				type_text("division by 0 error")
			else:
				print(a,"/",b,"=",a/b)
		elif operation == "2" :
			while True:
				a = check_float(input("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(input("what is the second number:"))
				if b != "":
					break
			print(a,"X",b,"=",a*b)
		elif operation == "3" :
			while True:
				a = check_float(input("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(input("what is the second number:"))
				if b != "":
					break
			print(a,"-",b,"=",a-b)
		elif operation == "4" :
			while True:
				a = check_float(input("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(input("what is the second number:"))
				if b != "":
					break
			print(a,"+",b,"=",a+b)
		elif operation == "5" :
			while True:
				a = check_float(input("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(input("what is the second number:"))
				if b != "":
					break
			print(a,"%",b,"=",a%b)
		elif operation == "6" :
			while True:
				a = check_float(input("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(input("what is the second number:"))
				if b != "":
					break
			print(a,"^",b,"=",a**b)
		elif operation == "0" :
				type_text("ok sending you back to the hub")
				return
		else:
			type_text("Sorry I didn't understand")
def game():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	easterEggCount = 250
	maxGuessCount = 20
	minGuess = 1
	maxGuess = 100
	playCount = 0
	playAgain = True
	while playAgain == True:
			if playCount == easterEggCount:
					type_text("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME! ##connection terminated by: Guessy##")
					quit()
			playCount += 1
			num = random.randint (minGuess,maxGuess)
			type_text(f'Welcome the GUESS THE NUMBER! I am your host Guessy. You have {maxGuessCount} attempts before you lose the game. good luck.')
			while True:
				guess = input(f'Guess a number {minGuess}-{maxGuess}: ')
				if check_int(guess):
					guess = int(guess)
					break
			for x in range(maxGuessCount): 
				if guess < num:
					while True:
						guess = check_int(input("the number is larger: "))
						if guess != "":
							break
				if guess > num:
					while True:
						guess = check_int(input("the number is smaller: "))
						if guess != "":
							break
				if guess == num: 
					print ("you got it")
					playgain = str(input("do you want to play again? (y/n): "))
					if playgain != "y":
						playAgain = False
						type_text("ok sending you back to the hub")
						time.sleep(1)
						return
					else:
						type_text("ok")
def palindrome():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	invertedP = ""
	doagennP = True
	iterationP = 1
	runnerP = "placeholder"
	while doagennP == True:
		invertedP = ""
		iterationP = 1
		nameP = str(input("hi i am pally please input a word or sentence and i will tell you if it's a palindrome or not: ")).lower()
		if len(nameP) == 1:
				type_text(nameP,"is a palindrome")
				invertedP = ""
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): "))
				if runnerP == "n":
						type_text("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False
						return
		else:
				loopP = (len(nameP))
				lopnarP =(len(nameP))
				for lopnarP in range(lopnarP):
						invertedP += nameP[loopP-iterationP]
						iterationP += 1
				if invertedP == nameP:
						print(nameP,"is a palindrome")
				else:
						print(nameP,"is not a palindrome")
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): ")).lower()
				if runnerP == "n":
						type_text("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False
						return
def area():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		e = 1
		type_text("1 for rectangle")
		type_text("2 for square")
		type_text("3 for triangle")
		type_text("4 for circle")
		type_text("5 for trapezoid")
		shape = input("what do you want or type stop to stop: ")
		if shape == "1":
			#square/rectangle
			type_text("ok input the numbers that you want")
			while True:
				a = check_float(input("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(input("what is the length (only numbers please): "))
				if b != "":
					break
			type_text(f"when the hight is {a} and the length is {b} the area is {a*b}.")
			e = 0
		if shape == "4":
			#circle
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(input("what is the radius (only numbers please): "))
				if a != "":
					break
			type_text(f"when the radius is {a} the area is {3.141592653589793238462643383279*a^2}")
		if shape == "3":
			#triangle
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(input("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(input("what is the length (only numbers please): "))
				if b != "":
					break
			type_text(f"when the hight is {a} and the length is {b} the area is {(a*b)*(1/2)}.")
		if shape == "5":
			#trapezoid
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(input("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(input("what is the top length (only numbers please): "))
				if b != "":
					break
			while True:
				c = check_float(input("what is the bottom length (only numbers please): "))
				if c != "":
					break
			type_text(f"when the hight is {a} and the bottom is {b} and the top is {c} the area is {((b+c)/2)*a}.")
		if shape == "2":
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = input("what is the length of one of the sides (only numbers please): ")
				if a != "":
					break
			type_text(f"when the the length of one of the sides is {a} the area is {a*2}.")
			e = 0
		if shape == "6":
			type_text("sorry coming soon")
			e = 0
		if shape == "7":
			type_text("sorry coming soon")
			e = 0
		if shape == "8":
			type_text("sorry coming soon")
			e = 0
		if shape == "9":
			type_text("sorry coming soon")
			e = 0
		if shape == "10":
			type_text("sorry coming soon")
			e = 0
		if shape == "11":
			type_text("sorry coming soon")
			e = 0
		if shape == "12":
			type_text("sorry coming soon")
			e = 0
		if shape == "13":
			type_text("sorry coming soon")
			e = 0
		if shape == "14":
			type_text("sorry coming soon")
			e = 0
		if shape == "15":
			type_text("sorry coming soon")
			e = 0
		if shape == "16":
			type_text("sorry coming soon")
			e = 0
		if shape == "17":
			type_text("sorry coming soon")
			e = 0
		if shape == "18":
			type_text("sorry coming soon")
			e = 0
		if shape == "19":
			type_text("sorry coming soon")
			e = 0
		if shape == "20":
			type_text("sorry coming soon")
			e = 0
		if shape == "stop":
			type_text("ok sending you back to Hubby")
			break
		else:
			type_text("sorry coming soon")
			e = 0
		if e == 1:
			type_text("sorry i didn't understand")
			e = 1
def avrage():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		runsq = 1
		list_o_numsq = []
		percentageq = 0
		while True:
			classesq = input("I am AV the Avenger. How many things do you want to average or type stop to stop: ")
			if classesq == "stop":
				type_text("ok sending you back to Hubby")
				return
			if classesq != "":
				classesq = check_int(classesq)
				if classesq != "":
					break
		for x in range(classesq):
			while True:
				one_at_a_timeq = check_int(input(f"what is the percentage of # {runsq} (only numbers please): "))
				if one_at_a_timeq != "":
					break
			percentageq += one_at_a_timeq
			list_o_numsq.append(one_at_a_timeq)
			runsq += 1
		type_text(f"you entered {list_o_numsq} they have an average of {percentageq/classesq}")
def code():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	input_o_code = input("shhhh. this is a secret i am liam what is the code(only numbers please): ")
	break_it = 1
	binary = ""
	checkw = 0
	for i in input_o_code:
		binary = binary + str(bin(ord(i)))
	if binary == "0b11011100b11001010b11101100b11001010b11100100b1000000b11001110b11101010b11011100b11011100b11000010b1000000b11001110b11010010b11101100b11001010b1000000b11110010b11011110b11101010b1000000b11101010b11100000b100001":
		while True:
			code_decode = int(input("would you like to code (1) or decode (2) or stop (3): "))
			list_o_coded = []
			output =""
			decoded = ""
			iterationw = 1
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
				type_text(output)
			if code_decode == 2:
				coded_decoder = str(input("what is the coded thing: "))
				seed_o_decodeing = int(input("what is the seed: "))
				list_o_decoding = (coded_decoder.split(","))
				for z in list_o_decoding:
					var = str(chr(int(z)-seed_o_decodeing))
					decoded = decoded + var
				type_text(decoded)
			if code_decode == 3:
				input_o_code = ""
				break_it = 0
				break
	if break_it == 1:
		print(f"""Traceback (most recent call last):
  File "c:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7{chr(92)}first project{chr(92)}hub.py", line 1315, in <module>
    hub()
  File "c:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7{chr(92)}first project{chr(92)}hub.py", line 1299, in hub
    code()
  File "c:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7{chr(92)}first project{chr(92)}hub.py", line 506, in code
    isinstance(input_o_code)
TypeError: isinstance expected 2 arguments, got 1""")
		print(f"PS C:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7>",end="")
		time.sleep(10)
		print()
		print("gotem")
		quit()
	else:
		print ("ok sending you back to hubby")
def translate_word(input_word):
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	split = {}
	deleted = ""
	not_a_string = ""
	output = ""
	decoded = ""
	j = 0
	i = 0
	x = 0
	iteration = 1
	consonants = []
	if len(input_word) < 3:
		return(input_word)
	else:
		for x in input_word:
			if x == "a":
				deleted = "a"
				split = second_half(iteration, input_word)
				break
			if x == "e":
				deleted = "e"
				split = second_half(iteration, input_word)
				break
			if x == "i":
				deleted = "i"
				split = second_half(iteration, input_word)
				break
			if x == "o":
				deleted = "o"
				split = second_half(iteration, input_word)
				break
			if x == "u":
				deleted = "u"
				split = second_half(iteration, input_word)
				break
			if x == "y" and iteration > 1:
				deleted = "y"
				split = second_half(iteration, input_word)
				break
			iteration += 1
			consonants.append(x)
	for i in split:
		not_a_string = not_a_string + i
	for j in consonants:
		decoded = decoded + j
	output =deleted + not_a_string + decoded + "ay"
	return(output)
def second_half(num,word):
	return (word[num:])
def last_bit():
	while True:
		iteration = 1
		out = ""
		imput_o_word = input("what do you want to translate or type stop to go back to Hubby: ")
		if imput_o_word == "stop":
			type_text("Ok sending you back to hubby. Oink")
			time.sleep(1)
			break
		output = []
		intt = imput_o_word.split(" ")
		for i in intt:
			output.append(translate_word(i))
		for x in output:
			if iteration ==1:
				out = out + x
			else:
				out = out +" "+ x
			iteration += 1
		type_text(out)
def pig():
	type_text("Hi i am Pig")
	last_bit()
def change_settings():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		type_text("ok")
		type_text("0 to go back to the terminal")
		type_text("1 to toggle typing")
		type_text("2 to toggle debugging")
		type_text("3 to change typing speed")
		while True:
			imper = check_int(input("what do you want"))
			if imper != "":
				
				break
		if imper == 0:
			type_text("ok back to the terminal")
			break
		elif imper == 1:
			if typing == True:
				typing = False
			else:
				typing = True
		elif imper == 2:
			if debuging == True:
				debuging = False
			else:
				debuging = True
		elif imper == 3:
			while True:
				sett = check_float(input("what do you want to change the typing speed to: "))
				if sett != "":
					break
def farinhight451():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	type_text("hi this is Kelvin")
	while True:
		yes = input("would you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			while True:
				tempofcelsius = check_int(input("what is the temp in celsius: "))
				if tempofcelsius != "":
					break
			type_text("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = input("would you like celsius to fahrenheit (y/n): ")
			if no == "y":
				while True:
					tempforfahrenheit = check_int(input("what is the temp in fahrenheit: "))
					if tempforfahrenheit != "":
						break
				type_text("the temp for celsius when fahrenheit is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			elif no == "n":				
				type_text("Ok sending you back to Hubby.")
				break
			else:
				type_text("sorry i didn't understand")
def print_board(board):
	iteration = -1
	for x in board:
		iteration += 1
		if iteration == 0:
			if x == "O":
				q11 = "      ███████████     "
				q12 = "    ███         ███   "
				q13 = "   ███           ███  "
				q14 = "   ███           ███  "
				q15 = "   ███           ███  "
				q16 = "   ███           ███  "
				q17 = "    ███         ███   "
				q18 = "      ███████████     "
			elif x == "X":
				q11 = "   ███         ███    "
				q12 = "     ███     ███      "
				q13 = "       ███ ███        "
				q14 = "        █████         "
				q15 = "        █████         "
				q16 = "       ███ ███        "
				q17 = "     ███     ███      "
				q18 = "   ███         ███    "
			else:
				q11 = "                      "
				q12 = "                      "
				q13 = "                      "
				q14 = "                      "
				q15 = "                      "
				q16 = "                      "
				q17 = "                      "
				q18 = "                      "
		elif iteration == 1:
			if x == "O":
				q21 = "      ███████████     "
				q22 = "    ███         ███   "
				q23 = "   ███           ███  "
				q24 = "   ███           ███  "
				q25 = "   ███           ███  "
				q26 = "   ███           ███  "
				q27 = "    ███         ███   "
				q28 = "      ███████████     "
			elif x == "X":
				q21 = "   ███         ███    "
				q22 = "     ███     ███      "
				q23 = "       ███ ███        "
				q24 = "        █████         "
				q25 = "        █████         "
				q26 = "       ███ ███        "
				q27 = "     ███     ███      "
				q28 = "   ███         ███    "
			else:
				q21 = "                      "
				q22 = "                      "
				q23 = "                      "
				q24 = "                      "
				q25 = "                      "
				q26 = "                      "
				q27 = "                      "
				q28 = "                      "
		elif iteration == 2:
			if x == "O":
				q31 = "      ███████████     "
				q32 = "    ███         ███   "
				q33 = "   ███           ███  "
				q34 = "   ███           ███  "
				q35 = "   ███           ███  "
				q36 = "   ███           ███  "
				q37 = "    ███         ███   "
				q38 = "      ███████████     "
			elif x == "X":
				q31 = "   ███         ███    "
				q32 = "     ███     ███      "
				q33 = "       ███ ███        "
				q34 = "        █████         "
				q35 = "        █████         "
				q36 = "       ███ ███        "
				q37 = "     ███     ███      "
				q38 = "   ███         ███    "
			else:
				q31 = "                      "
				q32 = "                      "
				q33 = "                      "
				q34 = "                      "
				q35 = "                      "
				q36 = "                      "
				q37 = "                      "
				q38 = "                      "
		elif iteration == 3:
			if x == "O":
				q41 = "      ███████████     "
				q42 = "    ███         ███   "
				q43 = "   ███           ███  "
				q44 = "   ███           ███  "
				q45 = "   ███           ███  "
				q46 = "   ███           ███  "
				q47 = "    ███         ███   "
				q48 = "      ███████████     "
			elif x == "X":
				q41 = "   ███         ███    "
				q42 = "     ███     ███      "
				q43 = "       ███ ███        "
				q44 = "        █████         "
				q45 = "        █████         "
				q46 = "       ███ ███        "
				q47 = "     ███     ███      "
				q48 = "   ███         ███    "
			else:
				q41 = "                      "
				q42 = "                      "
				q43 = "                      "
				q44 = "                      "
				q45 = "                      "
				q46 = "                      "
				q47 = "                      "
				q48 = "                      "
		elif iteration == 4:
			if x == "O":
				q51 = "      ███████████     "
				q52 = "    ███         ███   "
				q53 = "   ███           ███  "
				q54 = "   ███           ███  "
				q55 = "   ███           ███  "
				q56 = "   ███           ███  "
				q57 = "    ███         ███   "
				q58 = "      ███████████     "
			elif x == "X":
				q51 = "   ███         ███    "
				q52 = "     ███     ███      "
				q53 = "       ███ ███        "
				q54 = "        █████         "
				q55 = "        █████         "
				q56 = "       ███ ███        "
				q57 = "     ███     ███      "
				q58 = "   ███         ███    "
			else:
				q51 = "                      "
				q52 = "                      "
				q53 = "                      "
				q54 = "                      "
				q55 = "                      "
				q56 = "                      "
				q57 = "                      "
				q58 = "                      "
		elif iteration == 5:
			if x == "O":
				q61 = "      ███████████     "
				q62 = "    ███         ███   "
				q63 = "   ███           ███  "
				q64 = "   ███           ███  "
				q65 = "   ███           ███  "
				q66 = "   ███           ███  "
				q67 = "    ███         ███   "
				q68 = "      ███████████     "
			elif x == "X":
				q61 = "   ███         ███    "
				q62 = "     ███     ███      "
				q63 = "       ███ ███        "
				q64 = "        █████         "
				q65 = "        █████         "
				q66 = "       ███ ███        "
				q67 = "     ███     ███      "
				q68 = "   ███         ███    "
			else:
				q61 = "                      "
				q62 = "                      "
				q63 = "                      "
				q64 = "                      "
				q65 = "                      "
				q66 = "                      "
				q67 = "                      "
				q68 = "                      "
		elif iteration == 6:
			if x == "O":
				q71 = "      ███████████     "
				q72 = "    ███         ███   "
				q73 = "   ███           ███  "
				q74 = "   ███           ███  "
				q75 = "   ███           ███  "
				q76 = "   ███           ███  "
				q77 = "    ███         ███   "
				q78 = "      ███████████     "
			elif x == "X":
				q71 = "   ███         ███    "
				q72 = "     ███     ███      "
				q73 = "       ███ ███        "
				q74 = "        █████         "
				q75 = "        █████         "
				q76 = "       ███ ███        "
				q77 = "     ███     ███      "
				q78 = "   ███         ███    "
			else:
				q71 = "                      "
				q72 = "                      "
				q73 = "                      "
				q74 = "                      "
				q75 = "                      "
				q76 = "                      "
				q77 = "                      "
				q78 = "                      "
		elif iteration == 7:
			if x == "O":
				q81 = "      ███████████     "
				q82 = "    ███         ███   "
				q83 = "   ███           ███  "
				q84 = "   ███           ███  "
				q85 = "   ███           ███  "
				q86 = "   ███           ███  "
				q87 = "    ███         ███   "
				q88 = "      ███████████     "
			elif x == "X":
				q81 = "   ███         ███    "
				q82 = "     ███     ███      "
				q83 = "       ███ ███        "
				q84 = "        █████         "
				q85 = "        █████         "
				q86 = "       ███ ███        "
				q87 = "     ███     ███      "
				q88 = "   ███         ███    "
			else:
				q81 = "                      "
				q82 = "                      "
				q83 = "                      "
				q84 = "                      "
				q85 = "                      "
				q86 = "                      "
				q87 = "                      "
				q88 = "                      "
		elif iteration == 8:
			if x == "O":
				q91 = "      ███████████     "
				q92 = "    ███         ███   "
				q93 = "   ███           ███  "
				q94 = "   ███           ███  "
				q95 = "   ███           ███  "
				q96 = "   ███           ███  "
				q97 = "    ███         ███   "
				q98 = "      ███████████     "
			elif x == "X":
				q91 = "   ███         ███    "
				q92 = "     ███     ███      "
				q93 = "       ███ ███        "
				q94 = "        █████         "
				q95 = "        █████         "
				q96 = "       ███ ███        "
				q97 = "     ███     ███      "
				q98 = "   ███         ███    "
			else:
				q91 = "                      "
				q92 = "                      "
				q93 = "                      "
				q94 = "                      "
				q95 = "                      "
				q96 = "                      "
				q97 = "                      "
				q98 = "                      "
			q1 = f"""
				 ██                            ██
	{q11}   ██   {q21}   ██   {q31}
	{q12}   ██   {q22}   ██   {q32}
	{q13}   ██   {q23}   ██   {q33}
	{q14}   ██   {q24}   ██   {q34}
	{q15}   ██   {q25}   ██   {q35}
	{q16}   ██   {q26}   ██   {q36}
	{q17}   ██   {q27}   ██   {q37}
	{q18}   ██   {q28}   ██   {q38}
                                 ██			       ██
       ████████████████████████████████████████████████████████████████████████████████████████
				 ██                            ██
	{q41}   ██   {q51}   ██   {q61}
	{q42}   ██   {q52}   ██   {q62}
	{q43}   ██   {q53}   ██   {q63}
	{q44}   ██   {q54}   ██   {q64}
	{q45}   ██   {q55}   ██   {q65}
	{q46}   ██   {q56}   ██   {q66}
	{q47}   ██   {q57}   ██   {q67}
	{q48}   ██   {q58}   ██   {q68}
                                 ██		               ██
       ████████████████████████████████████████████████████████████████████████████████████████
				 ██                            ██
	{q71}   ██   {q81}   ██   {q91}
	{q72}   ██   {q82}   ██   {q92}
	{q73}   ██   {q83}   ██   {q93}
	{q74}   ██   {q84}   ██   {q94}
	{q75}   ██   {q85}   ██   {q95}
	{q76}   ██   {q86}   ██   {q96}
	{q77}   ██   {q87}   ██   {q97}
	{q78}   ██   {q88}   ██   {q98}
                                 ██		               ██
"""
	print(q1)
def piece_char(i, c):
	if c == "X":
		return "✗"
	elif c == "O":
		return "○"
	else:
		return "" + str(i+1)
def prit_board(board):
	for i, place in enumerate(board):	
		c = piece_char(i, place)
		if (i + 1) % 3 == 0:
			print(f" {c} ")
			if i <=6:
				print("-----------")
		else:
			print(f" {c} |", end="")
	print()
def possible_boards(cBoard,turn):
	moves = []
	for i in range(9):
		if cBoard[i] == None:
			newBoard = cBoard.copy()
			newBoard[i] = turn
			moves.append(newBoard)
	return moves
def choose_move(cBoard, turn):
	possible = possible_boards(cBoard, turn)

	if len(possible) == 1:
		return possible[0]

	nextTurn = "X"
	if turn == "X":
		nextTurn = "O"

	bestBoard = possible[0]
	bestX, bestO, bestT = score_move(bestBoard, nextTurn)

	for b in possible[1:]:
		x, o, t = score_move(b, nextTurn)
		if turn == "X":
			if o > bestO:
				continue
			elif x > bestX:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
			elif t > bestT and o < bestO and x >= bestX:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
		else:
			if x > bestX:
				continue
			elif o > bestO:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
			elif t > bestT and x < bestX and o >= bestO:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
	return bestBoard
def score_move(cBoard, turn):
	possible = possible_boards(cBoard, turn)
	x = 0.0
	o = 0.0
	t = 0.0
	for i, b in enumerate(possible):
		result = check_win(b)
		if result == "tie":
			return (0.0, 0.0, 1.0)
		elif result == "X":
			return (1.0, 0.0, 0.0)
		elif result == "O":
			return (0.0, 1.0, 0.0)
		elif turn == "X":
			bx, bo, bt = score_move(b, "O")
			x += bx
			o += bo
			t += bt
		else:
			bx, bo, bt = score_move(b, "X")
			x += bx
			o += bo
			t += bt
	# x /= len(possible)
	# o /= len(possible)
	# t /= len(possible)
	return(x,o,t)
def check_win(board):
	for c in ["X","O"]:
		if board[0] == c and board[1] == c and board[2] == c:
			return c
		elif board[3] == c and board[4] == c and board[5] == c:
			return c
		elif board[6] == c and board[7] == c and board[8] == c:
			return c
		elif board[0] == c and board[3] == c and board[6] == c:
			return c
		elif board[1] == c and board[4] == c and board[7] == c:
			return c
		elif board[2] == c and board[5] == c and board[8] == c:
			return c
		elif board[0] == c and board[4] == c and board[8] == c:
			return c
		elif board[2] == c and board[4] == c and board[6] == c:
			return c
	for x in board:
		if x == None:
			return None
	return "tie"
def check_move(board, playerMove):
	playerMove -= 1
	return board[playerMove] == None
def meet_o_code():
	global board
	for x in range(9):
		board[x]=None
	while True:
		board = choose_move(board, "X")
		if check_win(board) != None:
			print_board(board)
			if check_win(board) == "X":
				print("""
███         ███        ███                        ███   ██████████████████   ███            ███      █████████
  ███     ███          ███                        ███           ███          ██████         ███    ███
    ███ ███             ███                      ███            ███          ███   ███      ███    ███
     █████               ███                    ███             ███          ███      ███   ███      █████████
     █████                ███      ██████      ███              ███          ███         ██████              ███
    ███ ███                ███    ███  ███    ███               ███          ███            ███              ███
  ███     ███               ███  ███    ███  ███                ███          ███            ███              ███
███         ███              ██████      ██████         ██████████████████   ███            ███      █████████
	""")
			elif check_win(board) == "O":
				print("""
   █████████           ███                        ███   ██████████████████   ███            ███      █████████
 ███       ███         ███                        ███           ███          ██████         ███    ███
███         ███         ███                      ███            ███          ███   ███      ███    ███
███         ███          ███                    ███             ███          ███      ███   ███      █████████
███         ███           ███      ██████      ███              ███          ███         ██████              ███
███         ███            ███    ███  ███    ███               ███          ███            ███              ███
 ███       ███              ███  ███    ███  ███                ███          ███            ███              ███
   █████████                 ██████      ██████         ██████████████████   ███            ███      █████████
			""")
			break
		while True:
			print_board(board)
			if check_win(board) != None:
				if check_win(board) == "X":
					print("""
███         ███        ███                        ███   ██████████████████   ███            ███      █████████
  ███     ███          ███                        ███           ███          ██████         ███    ███
    ███ ███             ███                      ███            ███          ███   ███      ███    ███
     █████               ███                    ███             ███          ███      ███   ███      █████████
     █████                ███      ██████      ███              ███          ███         ██████              ███
    ███ ███                ███    ███  ███    ███               ███          ███            ███              ███
  ███     ███               ███  ███    ███  ███                ███          ███            ███              ███
███         ███              ██████      ██████         ██████████████████   ███            ███      █████████
	""")
				elif check_win(board) == "O":
					print("""
   █████████           ███                        ███   ██████████████████   ███            ███      █████████
 ███       ███         ███                        ███           ███          ██████         ███    ███
███         ███         ███                      ███            ███          ███   ███      ███    ███
███         ███          ███                    ███             ███          ███      ███   ███      █████████
███         ███           ███      ██████      ███              ███          ███         ██████              ███
███         ███            ███    ███  ███    ███               ███          ███            ███              ███
 ███       ███              ███  ███    ███  ███                ███          ███            ███              ███
   █████████                 ██████      ██████         ██████████████████   ███            ███      █████████
				""")
				break
			print("1 for top left")
			print("2 for top middle")
			print("3 for top right")
			print("4 for middle left")
			print("5 for middle middle")
			print("6 for middle right")
			print("7 for bottom left")
			print("8 for bottom middle")
			print("9 for bottom right")
			while True:
				try:
					play_go = int(input("where do you want to go: "))
					break
				except:
					print("nope")
			if play_go < 10 and play_go > 0:
				if play_go == 1 and board[0] != None:
					print("that is alredy taken")
				elif play_go == 2 and board[1] != None:
					print("that is alredy taken")
				elif play_go == 3 and board[2] != None:
					print("that is alredy taken")
				elif play_go == 4 and board[3] != None:
					print("that is alredy taken")
				elif play_go == 5 and board[4] != None:
					print("that is alredy taken")
				elif play_go == 6 and board[5] != None:
					print("that is alredy taken")
				elif play_go == 7 and board[6] != None:
					print("that is alredy taken")
				elif play_go == 8 and board[7] != None:
					print("that is alredy taken")
				elif play_go == 9 and board[8] != None:
					print("that is alredy taken")
				else:
					if play_go == 1:
						board[0] = "O"
					if play_go == 2:
						board[1] = "O"
					if play_go == 3:
						board[2] = "O"
					if play_go == 4:
						board[3] = "O"
					if play_go == 5:
						board[4] = "O"
					if play_go == 6:
						board[5] = "O"
					if play_go == 7:
						board[6] = "O"
					if play_go == 8:
						board[7] = "O"
					if play_go == 9:
						board[8] = "O"
					print_board(board)
					possible_boards(board, "X")
					break
			else:
				print("nope")
		if check_win(board) == None:
			print_board(board)
		else:
			if check_win(board) == "X":
				print("""
███         ███        ███                        ███   ██████████████████   ███            ███      █████████
  ███     ███          ███                        ███           ███          ██████         ███    ███
    ███ ███             ███                      ███            ███          ███   ███      ███    ███
     █████               ███                    ███             ███          ███      ███   ███      █████████
     █████                ███      ██████      ███              ███          ███         ██████              ███
    ███ ███                ███    ███  ███    ███               ███          ███            ███              ███
  ███     ███               ███  ███    ███  ███                ███          ███            ███              ███
███         ███              ██████      ██████         ██████████████████   ███            ███      █████████
	""")
			elif check_win(board) == "O":
				print("""
   █████████           ███                        ███   ██████████████████   ███            ███      █████████
 ███       ███         ███                        ███           ███          ██████         ███    ███
███         ███         ███                      ███            ███          ███   ███      ███    ███
███         ███          ███                    ███             ███          ███      ███   ███      █████████
███         ███           ███      ██████      ███              ███          ███         ██████              ███
███         ███            ███    ███  ███    ███               ███          ███            ███              ███
 ███       ███              ███  ███    ███  ███                ███          ███            ███              ███
   █████████                 ██████      ██████         ██████████████████   ███            ███      █████████
	""")
			break
def madlib():
	type_text("hi i am libby")
	runlib = True
	if runlib == True:
		one = str(input("this is a mad lib. Choose a adjictive: "))
		two = str(input("Choose a noun: "))
		tree = str(input("Choose a adjective: "))
		forr = str(input("Choose a noun; place: "))
		five = str(input("Choose a adjictive: "))
		six = str(input("Choose a adjictive: "))
		seven = str(input("Choose a pleral noun; vehical: "))
		ate = str(input("Choose a adjictive: "))
		nine = str(input("Choose a adjective: "))
		ten = str(input("Choose a plural noun: "))
		elevin = str(input("Choose a adjictive: "))
		twelve = str(input("Choose a plural noun: "))
		thrteen = str(input("Choose a plural noun: "))
		forteen = str(input("Choose a adjictive: "))
		fifteen = str(input("Choose a noun: "))
		sixteen = str(input("Choose a verb: "))
		seventeen = str(input("Choose a adjective: "))
		eating = str(input("Choose a verb: "))
		nineteen = str(input("Choose a pleral noun: "))
		twonty = str(input("Choose a pleral noun; type of job: "))
		twuntyone = str(input("Choose a ajictive: "))
		twuntytwo = str(input("Choose a verb: "))
		twontytree = str(input("Choose a adjective: "))
		type_text(f"Star Wars is a {one} {two} of {tree} versus evil in a {forr} far far away. There are {five} battles between {six} {seven} in {ate} space and {nine} duels with {ten} called {elevin} sabers. {twelve} called droids are helpers and {thrteen} tho the heroes. A {forteen} power caled The {fifteen} {sixteen}s people to do {seventeen} things, like {eating} {nineteen}. The Jedi {twonty} use The Force for the {twuntyone} side and the sith {twuntytwo} it for the {twontytree} side.")
		libbs = input("do you want to do another one? (y/n):")
		if libbs == "n":
			type_text("ok")
			runlib = False
			return
def lists():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	type_text("hi i am listy (but evoryone calls me lil'lister)")
	clist = input("what is the name of your list: ")
	thelist = []
	while True:
		action = input("""what do you want to do
0 to stop
1 add item
2 remove item
3 to print and leave the list (note this also deletes it): """)
		if action != "1" and action != "2" and action != "3":
			type_text("i am not impressed with your efforts to brake me")
		if action == "1" or action == "2" or action == "3":	
			if action == "1":
				inpuy = input("what do you want to add: ")
				thelist.append(inpuy)
			elif action == "2":
				print(flush=True)
				print(f"          {clist}          ",flush=True)
				print("___________________________",flush=True)
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________",flush=True)
				while True:
					remove = int(input("what do you want to remove: "))
					if remove > len(thelist):
						type_text(f"you dont have a item at {remove}")
					elif remove < 1:
						type_text("i am not impressed with your efforts to brake me")
					else:
						del thelist[remove-1]
						break
			elif action == "3":
				print(flush=True)
				print(f"          {clist}          ",flush=True)
				print("___________________________",flush=True)
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________",flush=True)
				clist = input("what is the new name for the new list: ")
				thelist = []	
			elif action == "0":
				return
def hub():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		type_text("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		type_text("0 to stop")
		type_text("1 for settings")
		type_text("2 for calculator")
		type_text("3 for number game")
		type_text("4 for palindrome detector")
		type_text("5 for pig latin translator")
		type_text("6 for anagram maker")
		type_text("7 for averager")
		type_text("8 for temperature calculator")
		type_text("9 for area calculator")
		type_text("10 for list maker")
		type_text("11 for tic tac toe game")
		type_text("12 for rock paper scissors")
		type_text("13 for text adventure game (made by mis larose)")
		hubo = input("what do you want: ")
		if check_int(hubo) == "":
			type_text("invalid input")
		else:
			hubo = int(hubo)
			if hubo == 0:
				type_text("Goodby please come back soon! ##connection terminated by:Hubby##, end sequance initiated:")
				time.sleep(4)
				print("""
		  		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		  		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-.......     ......:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-......:::--==++++===--:::....  .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@#...-=-::-+++*++++++++++++++++++++-.. :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@..-+=...=-...=++++++++++++++++++++++++-. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%.-++.+@@@@@@+.=++++++++++++++=+++++++++=. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.+*+.@@@@@@@@=-+++++++++++++++++=++=+====..@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.*++.@@@@@@@@--++++++++++++++++++++++++++:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.+++:.@@@@@@..=++++++++=++++++=++++++====:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.**++:... ..:=+++++++++++++++++++++=+++++:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-:*+++++++++++++++++++++++++++++=+===+====:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@      .              ..==++++++++++++++==+:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-*=+=========+==++=:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@%*#########%###################@=:=++++++++++=++++==:.@@@%%@@@@@@%@@@@@@@@@@@@@@@@
				@@@@@@@@@@@+.....:..............................-=+=++=+=+==========:.@@@*##########*#@@@@@@@@@@@@
				@@@@@@@@@...-+***++++++++++++++++++++=+++++++++++++++++++++++++++===:.@@@#@@@@@@@%%@%%##%@@@@@@@@@
				@@@@@@@..-+*+++++++++++++++++++++++++++++++++++=++==+==+====+=======:.@@@#%@@@%@@@@@@@@%##@@@@@@@@
				@@@@@@..=+++*++++++*++++++++++++++++++++++++++++++++++=+=++++=======:.@@@#%@@@%@@@@@@@@@@#%@@@@@@@
				@@@@@.:+**+++++++++++++++++++++++++++++++++=+++++====+==+===========:.@@@#%%%@%@@@@%%%%%%%#@@@@@@@
				@@@@@.+*+++++++++++++++++++++++++++++++++++++++=+++++++++=+=======++..@@@#%@@@%@@%%@@%%%@%##@@@@@@
				@@@@.:++++++++++++++++++++++++++++++++++++=========================- *@@%%@@@@%%%%%%%%%%%%%#@@@@@@
				@@@@.+++++++++++++++++++++++++++++++++++++++++++++=++++===========: .@@@%%%@@@@@%%%%@%%%@%%##@@@@@
				@@@*.*++++++++++++++++++++=++++++++++++++======+=++=+=========+=:. -@@@##%%%%%%%%%%%%%%%%%%%#@@@@@
				@@@.-++++*+*+*+*+++++++++++++++++-=-:........................    :@@@@#%%@%%@%%%%%%%@%%%%%%%#%@@@@
				@@@.=+++++++++++++++++++=++++-:.    ........................-*#@@@@@###%%%%%%%%@@%%%%%@@@%%%#%@@@@
				@@@+++++++++++++++++++++++:. .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###%%%@@@%%%%%%%%%%%%%%%%%%##@@@@@
				@@@.=+*++++++++++++++++++-. +@@@@@@%#%%%%%%%%%%##############*####%%%%%%%%%%%%%%%%%@@%%%%%%%##@@@@
				@@@.:+++++++++++++=+++++:.-@@@@####%%%%%%%%%%%%%%%%%%%%%%%%%%%@%@%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@@
				@@@#.*++++++++++++++++=:.@@@@##%%@@@@@@@@@@@@@@@%%@@@@@@@%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%##@@@@@
				@@@@ =*+++++++++++++++=.%@@@%%@@@@@@@@@@@@@@%%%@@@@@@@@%%@@%%@%%@@%%%%%%%%%%%@%%%%%%%%%%%%%#*@@@@@
				@@@@.:++++++++++++++++::@@@%%%@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%@@@%%@@%%%%%%%%%%%%%%%%%*@@@@@@
				@@@@@.=+++++++++++++++.:@@##@@@@@@@@@@@@%%%@%@@@@@@@@@@%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*@@@@@@
				@@@@@..=++++++++++=+++.:@@%%@@@@@@@@@%%%%%@@%%%%%%%%%@%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%#*@@@@@@@
				@@@@@@ .=++=++++++++++.:@@%%%@@@%%%%@@@@@@@%%@@%%%@%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*@@@@@@@@
				@@@@@@@..-++++++=+++++.:@@%%@@@@@@@@@@@@@%%%%%%%%%%%%@@%%%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%#*%@@@@@@@@
				@@@@@@@@-..:-*++++++++.:@@%%@%%%@@@@%@@@%%@@%@@@%%@%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%###**@@@@@@@@@@
				@@@@@@@@@@*   ........ .@@%%@%@@@%%%%%%%%%%%%%%%###########***######****#****####*****%@@@@@@@@@@@
				@@@@@@@@@@@@@@@%*@####=*@@%#%@@@@@@@@%@@%%%%%%%#@@%@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@%%%%%%%%%%%%@%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%@%%%%@%%%%%%%%%%%##*******++++++++++++++@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%@@%@@@%%@%%%@%%%%%%%%%%%%%%%%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%##***+**#%%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@##@%%%%%%%%%%%%%%@%%%%%%%%%%%%*@@@@@@%*#%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%*@@@@@@@@@#%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%%%%@@%%%%%%%%%%%%%%%%%%%#@@@@@@@@@#%%*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@#*%%%%%%%%%%%%%%%%%%%%%%%%%%##@@@@@@@*##**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*#%%%%%%%%%%%%%%%%%%%%%%%%###*###*###*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**#%%%%%%%%%%%%%%%%%%%%%%%%###****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#****####%%%%%%%%%%%%%###*+***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**++++**++*++***#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				""")
				type_text("made in python")
				time.sleep(3)
				type_text("mostly by Liam")
				time.sleep(3)
				type_text("tested by Jonas")
				time.sleep(3)
				type_text("help from my dad")
				time.sleep(3)
				type_text("great ideas made by my bothers and teacher thanks ;)")
				time.sleep(3)
				type_text("goodby comeback soon")
				time.sleep(1)
				quit()
			elif hubo ==1:
				change_settings()
			elif hubo ==2:
				type_text("Ok sending you to Calcu.")
				time.sleep(1)
				calculator()
			elif hubo ==3:
				type_text("Ok sending you to Guessy.")
				time.sleep(1)
				t()
			elif hubo ==4:
				type_text("Ok sending you to Pally.")
				time.sleep(1)
				palindrome()
			elif hubo ==5:
				type_text("Ok sending you to Pig.")
				time.sleep(1)
				pig()
			elif hubo ==6:
				type_text("Ok sending you to Anny.")
				time.sleep(1)
				anagram()
			elif hubo ==7:
				type_text("Ok sending you to AV (she is a bit crazy).")
				avrage()
			elif hubo ==8:
				type_text("Ok sending you to Kelvin.")
				farinhight451()
			elif hubo ==9:
				type_text("Ok sending you to Arion.")
				area()
			elif hubo ==10:
				type_text("Ok sending you to lil'lister")
				lists()
			elif hubo ==11:
				type_text("Ok sending you to The Gamer")
				meet_o_code()
			elif hubo == 12:
				type_text("ok sending you to The Rock")
				dwane_the_rock()
			elif hubo == 13:
				type_text("ok sendig you to The DM")
				the_game()
			elif hubo == 7232010:
				code()
			else:
				type_text("Sorry this option is not available yet.")
if debuging == False:
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("connection successful")
	time.sleep(1)
	hub()
else:
	hub()