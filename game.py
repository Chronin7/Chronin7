# import do not tuch
from enum import Enum
import random
from re import I
from typing import Union
import util_functions
from final_map_y2 import *


# dictonarys do not tuch
class Location:
	def __init__(
		self, name: str, description: Union[str,list[str]], special: Union[str, list[str], None] = None
	):
		self.name = name
		self.description = description
		self.special = special


location_dict: dict[str, Location] = {
	"h": Location(name="hot", description="a land of heat"),
	"l": Location(
		name="lava", description="tell the maker", special="not valid location"
	),
	"w": Location(
		name="water", description="tell the maker", special="Not valid location"
	),
	"i": Location(
		name="item",
		description="You found an item!",
		special="item",
	),
	"ni": Location(
		name="nessasary item",
		description="You found a nessasary item!",
		special="item",
	),
	"c": Location(name="cave", description="a dark cave", special=["desend", "ascend"]),
	"sk": Location(
		name="sky lift",
		description="a sacred place with powerfull lifting runes",
		special=["ascend", "desend"],
	),
	"b": Location(name="bridge", description="a rickety bridge"),
	"t": Location(name="town", description="a small town", special="town"),
	"f": Location(name="forest", description="a dense forest"),
	"r": Location(
		name="river",
		description="a flowing river",
		special="passable with gem of water",
	),
	"spawn": Location(
		name="spawn point", description="the place where your adventure begins"
	),
	"s": Location(name="snow", description="a cold snowy area"),
	"u": Location(
		name="unreachable", description="tell the maker", special="not valid location"
	),
	"g": Location(name="ground", description=["floating ground","cave floor"]),
	"aw": Location(
		name="acsesable water",
		description="some nice watter to swim in",
		special="passable with gem of water",
	),
	"p": Location(name="feild",description="a wide open feild")
}


class Effect:
	def __init__(
		self,
		buff: int = 0,
		heal: int = 0,
		xp: int = 0,
		dmg: int = 0,
		damage_type: str = "basic",
		ඞ: int = 0,
		mana: int = 0,
	):
		self.buff = buff
		self.heal = heal
		self.xp = xp
		self.dmg = dmg
		self.damage_type = damage_type
		self.mana = mana
		self.ඞ = ඞ


class Item:
	def __init__(self, useable: bool, effect: Effect):
		self.usable = useable
		self.effect = effect


ITEM_DICT: dict[str, Item] = {
	"dragon tooth": Item(useable=False, effect=Effect(buff=50, xp=50)),
	"slime gel": Item(useable=True, effect=Effect(heal=20, xp=25)),
	"orc tusk": Item(useable=True, effect=Effect(buff=10, xp=25)),
	"troll club": Item(useable=False, effect=Effect(buff=10, xp=50)),
	"goblin ear": Item(useable=False, effect=Effect(buff=5, xp=15)),
	"knight shield": Item(useable=False, effect=Effect(buff=20, xp=75)),
	"mechanical gear": Item(useable=False, effect=Effect(buff=15, xp=60)),
	"stone shard": Item(useable=False, effect=Effect(buff=10, xp=40)),
	"haunted horn": Item(useable=False, effect=Effect(buff=8, xp=30)),
	"song of the sea": Item(useable=True, effect=Effect(heal=15, xp=35)),
	"lava core": Item(
		useable=True, effect=Effect(dmg=12, damage_type="bomb_core", xp=45)
	),
	"trident of the deep": Item(useable=False, effect=Effect(buff=25, xp=80)),
	"ember shield": Item(useable=False, effect=Effect(buff=30, xp=90)),
	"debug item": Item(useable=True, effect=Effect(ඞ=9999)),
	"yeti fur": Item(useable=False, effect=Effect(buff=20, xp=50)),
	"frost shard": Item(useable=True, effect=Effect(heal=15, xp=20)),
	"shadow essence": Item(useable=False, effect=Effect(buff=30, xp=75)),
	"phoenix feather": Item(useable=True, effect=Effect(heal=30, xp=60)),
	"dark fang": Item(useable=False, effect=Effect(buff=15, xp=40)),
	"wisp": Item(useable=True, effect=Effect(heal=10, xp=15)),
	"rotting flesh": Item(useable=False, effect=Effect(buff=5, xp=10)),
	"king's crown": Item(useable=False, effect=Effect(buff=100, xp=500)),
	"shadow scale": Item(useable=False, effect=Effect(buff=120, xp=600)),
	"guard's emblem": Item(useable=False, effect=Effect(buff=50, xp=250)),
	"power suit": Item(useable=False, effect=Effect(buff=3000, xp=1500)),
	"the soul of a korock you monster": Item(
		useable=False, effect=Effect(buff=9999, xp=9999)
	),
	"no one can get this item": Item(
		useable=False,
		effect=Effect(
			buff=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
			xp=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
		),
	),
	"potion": Item(useable=True, effect=Effect(heal=30)),
	"magic weapon": Item(useable=False, effect=Effect(buff=30)),
	"water gem": Item(useable=False, effect=Effect(buff=50)),
	"fire gem": Item(useable=False, effect=Effect(buff=50)),
	"wind gem": Item(useable=False, effect=Effect(buff=50)),
	"power gem": Item(useable=False, effect=Effect(buff=50)),
	"resurrection gem": Item(useable=False, effect=Effect(buff=50)),
	"dark gem": Item(useable=False, effect=Effect(buff=50)),
	"frost gem": Item(useable=False, effect=Effect(buff=50)),
	"mana pouch": Item(useable=True, effect=Effect(mana=30, xp=15)),
	"lightning core": Item(
		useable=True, effect=Effect(dmg=30, damage_type="lightning_core")
	),
	"blizzard core": Item(
		useable=True, effect=Effect(dmg=30, damage_type="blizzard_core")
	),
	"fire core": Item(useable=True, effect=Effect(dmg=30, damage_type="fire_core")),
	"electric core": Item(
		useable=True, effect=Effect(dmg=30, damage_type="electric_core")
	),
	"ice core": Item(useable=True, effect=Effect(dmg=30, damage_type="ice_core")),
	"ඞ": Item(useable=True, effect=Effect(buff=1000000, mana=10000000, xp=100000)),
}


# the gbu 57 bunker buster can punch thru 60 meters of solid concrete. (sing to the tune of wellerman)
class Monster:
	def __init__(
		self,
		tier: int,
		hp: int,
		dmg: int,
		drops: Item,
		resistance: str,
		description: str,
		spawn_locations: list[str],
	) -> None:
		self.tier = tier
		self.hp = hp
		self.dmg = dmg
		self.resistance = resistance
		self.description = description
		self.spawn_locations = spawn_locations


monster_dict: dict[str, Monster] = {
	"dragon": Monster(
		tier=2,
		hp=150,
		dmg=30,
		drops=ITEM_DICT["dragon tooth"],
		resistance="fire",
		description="A large fire-breathing dragon.",
		spawn_locations=["~water", "~lava", "hot", "~river", "~snow"],
	),
	"blob": Monster(
		tier=1,
		hp=80,
		dmg=15,
		drops=ITEM_DICT["slime gel"],
		resistance="water",
		description="A gooey blob that oozes around.",
		spawn_locations=["~water", "~lava", "~river", "~snow"],
	),
	"orc": Monster(
		tier=2,
		hp=120,
		dmg=25,
		drops=ITEM_DICT["orc tusk"],
		resistance="wind",
		description="A brutish orc warrior.",
		spawn_locations=["~lava", "~water", "~river"],
	),
	"troll": Monster(
		tier=2,
		hp=130,
		dmg=28,
		drops=ITEM_DICT["troll club"],
		resistance="wind",
		description="A large and strong troll.",
		spawn_locations=["~lava", "~water", "bridge", "~river"],
	),
	"goblin": Monster(
		tier=1,
		hp=30,
		dmg=12,
		drops=ITEM_DICT["goblin ear"],
		resistance="darkness",
		description="A sneaky goblin.",
		spawn_locations=["~water", "~lava", "cave", "~river"],
	),
	"knight": Monster(
		tier=3,
		hp=200,
		dmg=40,
		drops=ITEM_DICT["knight shield"],
		resistance="light",
		description="A heavily armored knight.",
		spawn_locations=["~water", "~lava", "town", "bridge", "~river"],
	),  # if spawn on b)ige have speshal dialog (none shall pass, its only a flesh wound, tis but a scratch, ive had worse)
	"construct": Monster(
		tier=3,
		hp=180,
		dmg=35,
		drops=ITEM_DICT["mechanical gear"],
		resistance="electric",
		description="A mechanical construct brought to life.",
		spawn_locations=["~water", "~lava", "cave", "~river"],
	),
	"Animated statue": Monster(
		tier=2,
		hp=140,
		dmg=22,
		drops=ITEM_DICT["stone shard"],
		resistance="wind",
		description="A statue that has come to life.",
		spawn_locations=["~water", "~lava", "cave", "hot", "~river"],
	),
	"Possessed cow": Monster(
		tier=1,
		hp=90,
		dmg=18,
		drops=ITEM_DICT["haunted horn"],
		resistance="darkness",
		description="A cow possessed by a spirit.",
		spawn_locations=["~water", "~lava", "feild", "~river"],
	),
	"mermaid": Monster(
		tier=2,
		hp=110,
		dmg=20,
		drops=ITEM_DICT["song of the sea"],
		resistance="water",
		description="A mystical mermaid.",
		spawn_locations=[
			"water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"river",
			"~town",
			"~snow",
		],
	),
	"Lava monster": Monster(
		tier=2,
		hp=160,
		dmg=27,
		drops=ITEM_DICT["lava core"],
		resistance="fire",
		description="A creature made of molten lava.",
		spawn_locations=[
			"~water",
			"lava",
			"hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"~snow",
		],
	),
	"Fish lord": Monster(
		tier=3,
		hp=190,
		dmg=33,
		drops=ITEM_DICT["trident of the deep"],
		resistance="water",
		description="The ruler of all fish.",
		spawn_locations=[
			"water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"~snow",
		],
	),
	"Lava warden": Monster(
		tier=3,
		hp=210,
		dmg=38,
		drops=ITEM_DICT["ember shield"],
		resistance="fire",
		description="A guardian of the lava realms.",
		spawn_locations=[
			"~water",
			"lava",
			"hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"~snow",
		],
	),
	"blain": Monster(
		tier=100,
		hp=9999,
		dmg=500,
		drops=ITEM_DICT["ඞ"],
		resistance="darkness",
		description="one of the makers of the game",
		spawn_locations=["debug"],
	),
	"liam": Monster(
		tier=100,
		hp=9999,
		dmg=500,
		drops=ITEM_DICT["ඞ"],
		resistance="darkness",
		description="one of the makers of the game",
		spawn_locations=["debug"],
	),
	"yeti": Monster(
		tier=2,
		hp=150,
		dmg=30,
		drops=ITEM_DICT["yeti fur"],
		resistance="ice",
		description="A large ape-like creature covered in fur.",
		spawn_locations=[
			"~water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"snow",
		],
	),
	"ice cube": Monster(
		tier=1,
		hp=70,
		dmg=12,
		drops=ITEM_DICT["frost shard"],
		resistance="ice",
		description="A small cube of ice that has come to life.",
		spawn_locations=[
			"~water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"snow",
		],
	),
	"Nyx-spawn": Monster(
		tier=3,
		hp=200,
		dmg=40,
		drops=ITEM_DICT["shadow essence"],
		resistance="darkness",
		description="A creature born from the shadows.",
		spawn_locations=[
			"~water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"snow",
		],
	),
	"phoenix": Monster(
		tier=3,
		hp=180,
		dmg=35,
		drops=ITEM_DICT["phoenix feather"],
		resistance="fire",
		description="A mythical bird that rises from its ashes.",
		spawn_locations=[
			"~water",
			"lava",
			"hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"~snow",
		],
	),
	"shadow beast": Monster(
		tier=2,
		hp=140,
		dmg=22,
		drops=ITEM_DICT["dark fang"],
		resistance="darkness",
		description="A beast that lurks in the shadows.",
		spawn_locations=[
			"~water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"snow",
		],
	),
	"ghost": Monster(
		tier=1,
		hp=60,
		dmg=10,
		drops=ITEM_DICT["wisp"],
		resistance="darkness",
		description="A wandering spirit.",
		spawn_locations=[
			"~water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"snow",
		],
	),
	"zombie": Monster(
		tier=1,
		hp=50,
		dmg=8,
		drops=ITEM_DICT["rotting flesh"],
		resistance="darkness",
		description="A reanimated corpse.",
		spawn_locations=[
			"~water",
			"~lava",
			"~hot",
			"~feild",
			"~cave",
			"~bridge",
			"~town",
			"~river",
			"snow",
		],
	),
	"lord king": Monster(
		tier=10,
		hp=1000,
		dmg=100,
		drops=ITEM_DICT["king's crown"],
		resistance="light",
		description="The ultimate ruler.",
		spawn_locations=["debug"],
	),
	"lord king's guard": Monster(
		tier=5,
		hp=500,
		dmg=50,
		drops=ITEM_DICT["guard's emblem"],
		resistance="light",
		description="The elite guard of the lord king.",
		spawn_locations=["debug"],
	),
	"shadow dragon": Monster(
		tier=10,
		hp=1200,
		dmg=120,
		drops=ITEM_DICT["shadow scale"],
		resistance="darkness",
		description="A dragon born from shadows.",
		spawn_locations=["debug"],
	),
	"samus aran": Monster(
		tier=50,
		hp=3000,
		dmg=300,
		drops=ITEM_DICT["power suit"],
		resistance="electric",
		description="A legendary bounty hunter.",
		spawn_locations=["debug"],
	),  # nentendo please dont sue me
	"korock": Monster(
		tier=0,
		hp=1,
		dmg=1,
		drops=ITEM_DICT["the soul of a korock you monster"],
		resistance="wind",
		description="A small plant-like creature from the land of hyrule.",
		spawn_locations=["debug"],
	),
	"nintendo": Monster(
		tier=100000000000000000000000000000000000000000000000,
		hp=999999999999999999999999999999999999999999999999,
		dmg=999999999999999999999999999999999999999999999999,
		drops=ITEM_DICT["no one can get this item"],
		resistance="light",
		description="the ultimate being",
		spawn_locations=["debug"],
	),
}


# team manager
class TeamManager:
	def __init__(
		self,
		hp: list[int],
		dmg: list[int],
		drops: Union[list[Item], None],
		resistance: list[str],
		teir: list[int],
		name: list[str],
		description: list[str],
		level: Union[list[int], None ]= None,
		mana: Union[list[int], None] = None,
		xp: Union[list[int], None] = None,
	):
		# Expect lists for multi-entity teams
		self.hp_max = hp
		self.hp = hp
		self.dmg = dmg
		self.drops = drops
		self.resistance = resistance
		self.teir = teir
		self.name = name
		self.description = description
		# n is number of people in the team
		n = len(self.hp)
		if level is None:
			self.level = [1] * n
		else:
			self.level = list(level)
		if mana is None:
			self.mana_max = [10] * n
			self.mana = [10] * n
		else:
			self.mana_max = list(mana)
			self.mana = list(mana)
		if xp is None:
			self.xp = [0] * n
		else:
			self.xp = list(xp)

	def __repr__(self):
		return f'{"hp_max":self.hp_max,"hp":self.hp,"dmg":self.dmg,"drops":self.drops,"resistance":self.resistance,"teir":self.teir,"name":self.name,"description":self.description,"level":self.level,"max_mana":self.mana_max,"mana":self.mana,"xp":self.xp}'

	def __str__(self):
		return f"""
{self.name[0]}: {"!!!OUT!!!"if self.defeated(0) else ""}
max hp:{self.hp_max[0]}
hp:{self.hp[0]}
damage:{self.dmg[0]}
max mana:{self.mana_max[0]}
mana:{self.mana[0]}
level:{self.level[0]}
XP:{self.xp[0]}
resistance{self.resistance[0]}
description:{self.description[0]}
{self.name[1]}: {"!!!OUT!!!"if self.defeated(1) else ""}
max hp:{self.hp_max[1]}
hp:{self.hp[1]}
damage:{self.dmg[1]}
max mana:{self.mana_max[1]}
mana:{self.mana[1]}
level:{self.level[1]}
XP:{self.xp[1]}
resistance{self.resistance[1]}
description:{self.description[1]}
{self.name[2]}: {"!!!OUT!!!"if self.defeated(2) else ""}
max hp:{self.hp_max[2]}
hp:{self.hp[2]}
damage:{self.dmg[2]}
max mana:{self.mana_max[2]}
mana:{self.mana[2]}
level:{self.level[2]}
XP:{self.xp[2]}
resistance{self.resistance[2]}
description:{self.description[2]}
"""

	def getattribute(self, attr_name: str, person: int = 0):
		if hasattr(self, attr_name):
			val = getattr(self, attr_name)
			try:
				return val[person]
			except Exception:
				return val
		return None

	def heal(self, heal_amount: int, person: int):
		if 0 <= person < len(self.hp):
			self.hp[person] = min(self.hp[person] + heal_amount, self.hp_max[person])

	def damage(self, damage_amount: int, damage_type: str, person: int):
		if not (0 <= person < len(self.hp)):
			return
		actual = damage_amount
		if self.resistance and person < len(self.resistance):
			if self.resistance[person] == damage_type:
				actual = damage_amount // 2
		self.hp[person] = max(self.hp[person] - actual, 0)
		print(f"{self.name[person]} took {actual} damage (HP now {self.hp[person]})")

	def if_dead(self, person: int, targets: list[int] = []):
		if 0 <= person < len(self.hp) and self.hp[person] <= 0:
			self.remove(person, targets)

	def defeated(self, person: Union[int , None] = None):
		if person:
			return self.get_continuous_players()[person]
		if len(self.get_continuous_players()) < 1:
			return True
		else:
			return False

	def remove(self, person: int, targets: list[int] = []):
		if not (0 <= person < len(self.hp)):
			return
		if self.teir[person] == 0:
			print(f"{self.name[person]} is unconscious")
			self.hp[person] = -1
			if person in targets:
				try:
					targets.remove(person)
				except ValueError:
					pass
		else:
			if self.drops:
				print(f"You got {self.drops[person]} and killed {self.name[person]}")
			if 0 <= person < len(targets):
				targets.pop(person)

	def level_up(self, person: int):
		global monster_spawn_rate
		if not (0 <= person < len(self.level)):
			return
		self.level[person] += 1
		self.hp_max[person] += 10
		self.hp[person] = self.hp_max[person]
		self.mana_max[person] += 10
		self.mana[person] = self.mana_max[person]
		if self.level[person] % 7 == 0:
			monster_spawn_rate = min(monster_spawn_rate + 5, 70)
		self.dmg[person] += 10

	def add_buff(self, damage_buff: int, person: int):
		if 0 <= person < len(self.dmg):
			self.dmg[person] += damage_buff

	def attack(
		self,
		players_go: int,
		continuous_players: list[int],
		enemies: "TeamManager",
		players: "TeamManager",
	):
		global inventory
		if players_go:

			for player_index in continuous_players:
				print(
					f'{players.getattribute("name",0)} is at {players.getattribute("hp",0)} hp\n{players.getattribute("name",1)} is at {players.getattribute("hp",1)} hp\n{players.getattribute("name",2)} is at {players.getattribute("hp",2)} hp\n'
				)
				if enemies.defeated():
					break
				choise = util_functions.get_valid_type(
					int,
					"0 to run away, 1 to attack, 2 to use item: ",
					"that is not a number 0,1 or 2",
					[0, 1, 2],
				)
				if choise == 0:
					if util_functions.alternate_random((0, 5), int) == 1:
						print(
							"the monsters where too fast and caught you as you tried to run away"
						)
						continue
					else:
						print("you successfully ran away!")
						return "ran"
				elif choise == 2 and len(inventory.get_inventory()) > 0:
					inventory.choose_item_and_use(True, players, enemies)
				damage = self.dmg[player_index]
				if len(enemies.hp) == 0:
					continue
				target = random.randint(0, len(enemies.hp) - 1)
				enemies.damage(damage, "normal", target)
				enemies.if_dead(target, list(range(len(enemies.hp))))
		else:
			for i in range(len(enemies.hp)):
				if enemies.hp[i] <= 0:
					continue
				tier_val = (
					enemies.teir[i]
					if i < len(enemies.teir) and enemies.teir[i] > 0
					else 1
				)
				num = random.randint(1, max(1, tier_val))
				if num == 1:
					if not continuous_players:
						continue
					target = random.choice(continuous_players)
					enemies.damage(enemies.dmg[i], "normal", target)
					self.if_dead(target, continuous_players)
				elif num == 2:
					for j in continuous_players:
						enemies.damage(enemies.dmg[i], "normal", j)
						self.if_dead(j, continuous_players)
				elif num == 3:
					if not continuous_players:
						continue
					target = random.choice(continuous_players)
					enemies.damage(enemies.dmg[i] // 2, "resistant", target)
					self.if_dead(target, continuous_players)
				elif num == 4:
					for j in continuous_players:
						enemies.damage(enemies.dmg[i] // 2, "resistant", j)
						self.if_dead(j, continuous_players)

	def get_continuous_players(self):
		continuous_players: list[int] = []
		for i in range(len(self.hp)):
			if self.hp[i] > 0:
				continuous_players.append(i)
		return continuous_players

	def get_continuous_player_names(self):
		continuous_players: list[str] = []
		for i in range(len(self.hp)):
			if self.hp[i] > 0:
				continuous_players.append(self.name[i])
		return continuous_players

	def gain_mana(self, mana_amount: int, person: int):
		if 0 <= person < len(self.mana):
			self.mana[person] = min(
				self.mana[person] + mana_amount, self.mana_max[person]
			)

	# def


class InventoryManager:
	def __init__(self, starting_inventory: dict[str, int] = {}):
		self.inventory = starting_inventory.copy()

	def __repr__(self):
		return f"{self.get_inventory()}"

	def has_item(self, item_name: str):
		return item_name in self.inventory

	def use(
		self, item_name: str, party: TeamManager, person: int, enemies: "TeamManager"
	):
		item = ITEM_DICT[item_name]
		if item and item_name in self.inventory and item.usable:
			self.effect_function(item.effect, party, person, enemies)
			self.inventory[item_name] -= 1
			if self.inventory[item_name] <= 0:
				self.inventory.pop(item_name)
		else:
			raise Exception(f"Item '{item_name}' not usable or not found")

	def grant(self, item_name: str):
		if item_name in self.inventory:
			self.inventory["count"] += 1
		else:
			self.inventory["count"] = 1

	def get_length(self):
		return len(self.inventory)

	def get_inventory(self):
		return self.inventory

	def effect_function(
		self, effect: Effect, party: TeamManager, person: int, enemies: TeamManager
	):
		if not isinstance(effect, dict):
			return
		# healing and mana effects
		if effect.heal > 0:
			party.heal(effect.heal, person)
		if effect.mana > 0:
			party.gain_mana(effect.mana, person)
		# debug item
		if effect.ඞ > 0:
			for i in range(len(party.hp)):
				party.heal(party.hp_max[i], i)
				party.gain_mana(party.mana_max[i], i)
			dmg = util_functions.get_valid_type(int, "")
			for i in range(len(enemies.hp)):
				enemies.damage(dmg, "normal", i)

		if effect.dmg > 0:
			# items/efects
			if effect.damage_type == "bomb_core":
				for i in range(len(enemies.hp)):
					enemies.damage(effect.dmg, "fire", i)
			if effect.damage_type == "lightning_core":
				for i in range(len(enemies.hp)):
					enemies.damage(effect.dmg, "electric", i)
			if effect.damage_type == "blizzard_core":
				for i in range(len(enemies.hp)):
					enemies.damage(effect.dmg, "ice", i)
			if effect.damage_type == "fire_core":
				enemies.damage(effect.dmg, "fire", person)
			if effect.damage_type == "electric_core":
				enemies.damage(effect.dmg, "electric", person)
			if effect.damage_type == "ice_core":
				enemies.damage(effect.dmg, "ice", person)

	def choose_item_and_use(
		self, usable: bool, party: TeamManager, enemy_party: TeamManager
	):
		key: list[str] = []
		if usable:
			iteration = 0
			print("0 to return")
			for item_name in self.inventory:
				item = ITEM_DICT[item_name]
				if item.usable:
					iteration += 1
					print(f"{iteration} for {item_name}")
					key.append(item_name)
			while True:
				choise: int = util_functions.get_valid_type(
					int,
					"what do you want to use: ",
					"that is not a valid input, press enter to continue",
					(0, iteration),
				)
				if choise == 0:
					return "returned"
				item_name = key[choise - 1]
				item = ITEM_DICT[item_name]
				enemy_key: list[int] = []
				if item.effect.dmg > 0:
					while True:
						print("0 to return")
						for num, name in enumerate(
							enemy_party.get_continuous_player_names()
						):
							enemy_key.append(num)
							print(f"{num+1} to atack {name}")
							choise = util_functions.get_valid_type(
								int,
								"who do you want to atack; ",
								"that is not a valid input, press enter to continue",
								(0, num + 1),
							)
							if choise == 0:
								break
							else:
								choise = enemy_key[choise]
								self.use(item_name, party, choise, enemy_party)
		else:
			iteration = 0
			for num, item_name in enumerate(inventory.get_inventory()):
				item = ITEM_DICT[item_name]
				if not item.usable:
					iteration += 1
					print(f"{iteration} for {item_name}")
	###### wth
	def __str__(self):
		out = ""
		for count, name in enumerate(self.inventory):
			item = ITEM_DICT[name]
			out += f"{count} {name[1]}:{item.effect}/n"
		return out


monster_spawn_rate = 20  #


inventory = InventoryManager()


class GameState:
	def __init__(self):
		self.party = TeamManager(
			hp=[100, 80, 60],
			dmg=[12, 8, 15],
			drops=None,
			resistance=["none", "none", "none"],
			teir=[0, 0, 0],
			name=["Hero", "Mage", "Rogue"],
			description=["Brave hero", "Wise mage", "Sneaky rogue"],
		)
		self.inventory = InventoryManager()
		self.pos = [15, 18]
		self.area = "mid"
		self.battle_chance = 5
		self.monster_spawn_rate = 5


def get_tile_at(
	pos: tuple[int, int], area: str
) -> Union[str, None]:  # pyright: ignore[reportGeneralTypeIssues]
	"""
	Docstring for get_tile_at
	retruns string
	:param pos: the position
	:param area: the area
	"""
	x, y = pos
	if area == "mid":
		return mid[y][x]
	if area == "upper":
		return upper[y][x]
	if area == "underground":
		return underground[y][x]
	return None


def spawn_monster(
	party_levels: list[int], location: Location, override: list[str] = []
):
	global monster_dict
	# avg_level = max(1, sum(party_levels) // len(party_levels))
	spawnable: list[Monster] = []
	for name in override:
		spawnable.append(monster_dict[name])
	for monster in monster_dict.values():
		if f"~{location.name}" not in monster.spawn_locations:
			spawnable.append(monster)
	


if __name__ == "__main__":
	print(spawn_monster([3, 3, 3], location_dict["h"], ["yeti", "dragon", "NULL"]))
