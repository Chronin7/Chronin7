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
	Item("banana: instakill", damagebuff=100000000000, type="consumable"),
	Item("banana: instakill", damagebuff=100000000000, type="consumable"),
	Item("banana: instakill", damagebuff=100000000000, type="consumable"),
	Item("sniper rifle: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("sniper rifle: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("sniper rifle: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("usi: tends to misfire +20% damage", damagebuff=.20, type="weapon"),
	Item("club: BIG STICK +30% damage", damagebuff=.30, type="weapon"),
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
	"mountain1": Location(description="you are in a mountain", itemRarity=3,moves=Moves(south="foothills1")),
	"mountain2": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="mountain3", east="swamp2")),
	"mountain3": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="mountain4", east="mountain2"), monster=Monster(name="dragon", health=100, damage=50, lootLevel=3)),	
	"mountain4": Location(description="you are in a mountain", itemRarity=2,moves=Moves(west="mountain5", east="mountain3"), monster=Monster(name="robot", health=50, damage=10, lootLevel=3)),
	"mountain5": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="glitchedPlains1", east="mountain4"), monster=Monster(name="robot", health=200, damage=20, lootLevel=3)),
	"BOD": Location(description="BODY", hasLoot=False, moves=Moves(north="moun1tain5")),
	"glitchedPlains1": Location(description="You have entered the glitched plains", itemRarity=3, moves=Moves(north="glitchedPlains2", east="mountain5"), monster=Monster(name="robot", health=250, damage=50, lootLevel=3)),
	"glitchedPlains2": Location(description="You have entered the glitched plains", itemRarity=2, moves=Moves(west="glitchedCitadel", south="glitchedPlains1"), monster=Monster(name="robot", health=300, damage=50, lootLevel=3)),
	"glitchedCitadel": Location(description="You have entered the glitched citadel.", hasLoot=False, moves=Moves(west="keyboard", east="glitchedPlains2"), monster=Monster(name="The Programer", health=1000, damage=50)),
	"keyboard": Location(description="keyboard",hasLoot=False, moves=Moves())
}

world: Dict[str,Location]
location: Location
inventory: List[Item]
health: int
damage: int
color: str
name: str
quest = "To seek the keyboard"
playedAmount = 0
damagebuff=0
def initGame():
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
	print("search for loot to get loot")
	print("battle monsters")
	print("get the keyboard")
	print("win")
	playedAmount+=1
	
def move(loc: str):
	global location
	global inventory
	for item in [item for item in inventory if item.life != None]:
			item.life -= 1
			if item.life == 0:
				print(f"Your {item.name} has expired")
				inventory.remove(item)
	location = world[loc]
	#print(f'moved to: {location}')

def selectOption(options: List[Tuple[str,any]], cancelable = True, noOptionText = "You can't do that.") -> any:
	options = [x for x in options if x[1] != None]
	if len(options) == 0:
		print(noOptionText)
		return None
	while True:
		try:
			print("Select an option:")
			if cancelable:
				print("0. Cancel")
			for i, option in enumerate(options):
				print(f"{i+1}. {option[0]}")
			value = int(input("Choose wisely: "))
			print()
			if cancelable and value == 0:
				return None
			elif value < 1 or value > len(options):
				print("try again")
			else:
				return options[value-1][1]
		except ValueError:
			print("Invalid input")

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
		print(f"You used {item.name} and gained {item.health} health")
	else:
		print(f"You used {item.name} and lost {-item.health} health")
	print(f"You have {health} health left")
	inventory.remove(item)

def keyboard():
	print("You have found the keyboard!")
	if input("do you type(y/n):").lower=="y":
		print("""Traceback (most recent call last):
  File "/Users/this is a joke/personal/pythonPlay/game.py", line ∞, in <all>
    item = banana
           ^^^^^^
  File "/Users/also a joke/personal/pythonPlay/game.py", line ∞, in lemon
    raise Exception(f"Invalid rarity {good food}")
Exception: Invalid rarity 2037946809832759832""")
		time.sleep(.01)
		print("BACK FROM THE DEAD CODE")
		print("hahaha")
		print("P.S. you win")
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
	print(f"A {monster.name} appears!")
	for item in predamageItems:
		print(f"you used an {item.name} and did {item.predamage} damage")
		monster.health-=max(item.predamage, 0)

	while True:
		print(f"The {monster.name} has {monster.health} health left")
		option = selectOption([
			("Fight", "fight"),
			("Use Item", "useItem")
		], cancelable=False)
		if option == "fight":
			print(f"You fight the {monster.name}")
			attack = totalDamage()
			print(f"You deal {attack} damage")
			monster.health = max(0, location.monster.health - attack)
			if monster.health <= 0:
				print(f"You have defeated the {monster.name}")
				item = randomItem(monster.lootLevel)
				print(f"{monster.name} dropped a {item.name} and you picked it up")
				inventory.append(item)
				location.monster = None
				return True
		elif option == "useItem":
			if useItem() == False:
				continue
		print(f"{location.monster.name} attacks!")
		health -= location.monster.damage
		if health <= 0:
			print("You have died and a antelope ate your earlobes")
			return False
		print(f"You have {health} health left")

playedAmount =0
while True:
	ep = 0
	if input("do you want to play(y/n)").lower()!="y":
		break
	if input("are you drunk(y/n): ").lower() != "y":
		print("dont drink its bad for your health")
		time.sleep(1)
		print("ʸᵉᵗ ᵍʳᵒʷᵗʰ ᵐⁱⁿᵈ ˢᵉᵗ")
	initGame()
	while True:
		if location.description == "keyboard":
			keyboard()
		else:
			print(location.description)
			if location.monster:
				if battle() == False:
					break
			if health<0:
				print("you died")
				print("game over")
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
					print(f"You found a {item.name}")
				else:
					print("You found nothing")
			elif option == "move":
				place = location.moves.selectMove()
				if place:
					move(place)