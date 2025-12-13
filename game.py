# import do not tuch
from enum import Enum
from html import entities
import random
from re import I
from typing import Union
import util_functions
from final_map_y2 import *

# hi


# dictonarys do not tuch
class Location:
    def __init__(
        self,
        name: str,
        description: Union[str, list[str]],
        special: Union[str, list[str], None] = None,
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
    "g": Location(name="ground", description=["floating ground", "cave floor"]),
    "aw": Location(
        name="acsesable water",
        description="some nice watter to swim in",
        special="passable with gem of water",
    ),
    "p": Location(name="feild", description="a wide open feild"),
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
    def __init__(self, name: str, useable: bool, count: int, effect: Effect):
        self.name = name
        self.usable = useable
        self.count = count
        self.effect = effect


ITEM_LIST: list[Item] = [
    Item(name="dragon tooth", useable=False, count=1, effect=Effect(buff=50, xp=50)),
    Item(name="slime gel", useable=True, count=1, effect=Effect(heal=20, xp=25)),
    Item(name="orc tusk", useable=True, count=1, effect=Effect(buff=10, xp=25)),
    Item(name="troll club", useable=False, count=1, effect=Effect(buff=10, xp=50)),
    Item(name="goblin ear", useable=False, count=1, effect=Effect(buff=5, xp=15)),
    Item(name="knight shield", useable=False, count=1, effect=Effect(buff=20, xp=75)),
    Item(name="mechanical gear", useable=False, count=1, effect=Effect(buff=15, xp=60)),
    Item(name="stone shard", useable=False, count=1, effect=Effect(buff=10, xp=40)),
    Item(name="haunted horn", useable=False, count=1, effect=Effect(buff=8, xp=30)),
    Item(name="song of the sea", useable=True, count=1, effect=Effect(heal=15, xp=35)),
    Item(
        name="lava core",
        useable=True,
        count=1,
        effect=Effect(dmg=12, damage_type="bomb_core", xp=45),
    ),
    Item(
        name="trident of the deep",
        useable=False,
        count=1,
        effect=Effect(buff=25, xp=80),
    ),
    Item(name="ember shield", useable=False, count=1, effect=Effect(buff=30, xp=90)),
    Item(name="debug item", useable=True, count=1, effect=Effect(ඞ=9999)),
    Item(name="yeti fur", useable=False, count=1, effect=Effect(buff=20, xp=50)),
    Item(name="frost shard", useable=True, count=1, effect=Effect(heal=15, xp=20)),
    Item(name="shadow essence", useable=False, count=1, effect=Effect(buff=30, xp=75)),
    Item(name="phoenix feather", useable=True, count=1, effect=Effect(heal=30, xp=60)),
    Item(name="dark fang", useable=False, count=1, effect=Effect(buff=15, xp=40)),
    Item(name="wisp", useable=True, count=1, effect=Effect(heal=10, xp=15)),
    Item(name="rotting flesh", useable=False, count=1, effect=Effect(buff=5, xp=10)),
    Item(name="king's crown", useable=False, count=1, effect=Effect(buff=100, xp=500)),
    Item(name="shadow scale", useable=False, count=1, effect=Effect(buff=120, xp=600)),
    Item(name="guard's emblem", useable=False, count=1, effect=Effect(buff=50, xp=250)),
    Item(name="power suit", useable=False, count=1, effect=Effect(buff=3000, xp=1500)),
    Item(
        name="the soul of a korock you monster",
        useable=False,
        count=1,
        effect=Effect(buff=9999, xp=9999),
    ),
    Item(
        name="no one can get this item",
        useable=False,
        count=1,
        effect=Effect(
            buff=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
            xp=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        ),
    ),
    Item(name="potion", useable=True, count=1, effect=Effect(heal=30)),
    Item(name="magic weapon", useable=False, count=1, effect=Effect(buff=30)),
    Item(name="water gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="fire gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="wind gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="power gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="resurrection gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="dark gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="frost gem", useable=False, count=1, effect=Effect(buff=50)),
    Item(name="mana pouch", useable=True, count=1, effect=Effect(mana=30, xp=15)),
    Item(
        name="lightning core",
        useable=True,
        count=1,
        effect=Effect(dmg=30, damage_type="lightning_core"),
    ),
    Item(
        name="blizzard core",
        useable=True,
        count=1,
        effect=Effect(dmg=30, damage_type="blizzard_core"),
    ),
    Item(
        name="fire core",
        useable=True,
        count=1,
        effect=Effect(dmg=30, damage_type="fire_core"),
    ),
    Item(
        name="electric core",
        useable=True,
        count=1,
        effect=Effect(dmg=30, damage_type="electric_core"),
    ),
    Item(
        name="ice core",
        useable=True,
        count=1,
        effect=Effect(dmg=30, damage_type="ice_core"),
    ),
    Item(
        name="ඞ",
        useable=True,
        count=1,
        effect=Effect(buff=1000000, mana=10000000, xp=100000),
    ),
]

ITEM_DICT = {item.name: item for item in ITEM_LIST}


# the gbu 57 bunker buster can punch thru 60 meters of solid concrete. (sing to the tune of wellerman)
class Character:
    def __init__(
        self,
        name: str,
        level: int,
        hp: int,
        dmg: int,
        description: str,
        xp: int = 0,
        resistance: str = "none",
        drops: list[Item] = [],
        spawn_locations: list[str] = [],
        npc: bool = True,
    ) -> None:
        self.name = name
        self.level = level
        self.hp = hp
        self.hp_max = hp
        self.mana = 0
        self.mana_max = 15
        self.dmg = dmg
        self.xp = xp
        self.resistance = resistance
        self.description = description
        self.drops = drops
        self.spawn_locations = spawn_locations
        self.npc = npc

    def defeated(self):
        return self.hp <= 0

    def details(self):
        return f"""{self.name}: {'!!!OUT!!!' if self.defeated() else ''}
  hp:{self.hp}
  max hp:{self.hp_max}
  damage:{self.dmg}
  max mana:{self.mana_max}
  mana:{self.mana}
  level:{self.level}
  xp:{self.xp}
  resistance{self.resistance[0]}
  description:{self.description[0]}"""

    def __str__(self):
        return str(f"{self.name}\n  hp:{self.hp}\ndescription:{self.description}")

    def heal(self, amount: int):
        self.hp = min(self.hp_max, self.hp + amount)
        print(f"{self.name} +{amount}hp (HP now {self.hp})")

    def damage(self, amount: int, type: str = "basic"):
        if self.resistance == type:
            amount //= 2
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} took {amount} damage (HP now {self.hp})")

    def gain_mana(self, amount: int):
        self.mana = min(self.mana_max, self.mana + amount)


monster_list: list[Character] = [
    Character(
        name="dragon",
        level=4,
        hp=150,
        dmg=30,
        drops=[ITEM_DICT["dragon tooth"]],
        resistance="fire",
        description="A large fire-breathing dragon.",
        spawn_locations=["~water", "~lava", "hot", "~river", "~snow"],
    ),
    Character(
        name="blob",
        level=1,
        hp=80,
        dmg=15,
        drops=[ITEM_DICT["slime gel"]],
        resistance="water",
        description="A gooey blob that oozes around.",
        spawn_locations=["~water", "~lava", "~river", "~snow"],
    ),
    Character(
        name="orc",
        level=5,
        hp=120,
        dmg=25,
        drops=[ITEM_DICT["orc tusk"]],
        resistance="wind",
        description="A brutish orc warrior.",
        spawn_locations=["~lava", "~water", "~river"],
    ),
    Character(
        name="troll",
        level=3,
        hp=130,
        dmg=28,
        drops=[ITEM_DICT["troll club"]],
        resistance="wind",
        description="A large and strong troll.",
        spawn_locations=["~lava", "~water", "bridge", "~river"],
    ),
    Character(
        name="goblin",
        level=1,
        hp=30,
        dmg=12,
        drops=[ITEM_DICT["goblin ear"]],
        resistance="darkness",
        description="A sneaky goblin.",
        spawn_locations=["~water", "~lava", "cave", "~river"],
    ),
    Character(
        name="knight",
        level=3,
        hp=200,
        dmg=40,
        drops=[ITEM_DICT["knight shield"]],
        resistance="light",
        description="A heavily armored knight.",
        spawn_locations=["~water", "~lava", "town", "bridge", "~river"],
    ),  # if spawn on b)ige have speshal dialog (none shall pass, its only a flesh wound, tis but a scratch, ive had worse)
    Character(
        name="construct",
        level=5,
        hp=180,
        dmg=35,
        drops=[ITEM_DICT["mechanical gear"]],
        resistance="electric",
        description="A mechanical construct brought to life.",
        spawn_locations=["~water", "~lava", "cave", "~river"],
    ),
    Character(
        name="Animated statue",
        level=3,
        hp=140,
        dmg=22,
        drops=[ITEM_DICT["stone shard"]],
        resistance="wind",
        description="A statue that has come to life.",
        spawn_locations=["~water", "~lava", "cave", "hot", "~river"],
    ),
    Character(
        name="Possessed cow",
        level=1,
        hp=90,
        dmg=18,
        drops=[ITEM_DICT["haunted horn"]],
        resistance="darkness",
        description="A cow possessed by a spirit.",
        spawn_locations=["~water", "~lava", "feild", "~river"],
    ),
    Character(
        name="mermaid",
        level=2,
        hp=110,
        dmg=20,
        drops=[ITEM_DICT["song of the sea"]],
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
    Character(
        name="Lava monster",
        level=3,
        hp=160,
        dmg=27,
        drops=[ITEM_DICT["lava core"]],
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
    Character(
        name="Fish lord",
        level=5,
        hp=190,
        dmg=33,
        drops=[ITEM_DICT["trident of the deep"]],
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
    Character(
        name="Lava warden",
        level=5,
        hp=210,
        dmg=38,
        drops=[ITEM_DICT["ember shield"]],
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
    Character(
        name="blain",
        level=100,
        hp=9999,
        dmg=500,
        drops=[ITEM_DICT["ඞ"]],
        resistance="darkness",
        description="one of the makers of the game",
        spawn_locations=["debug"],
    ),
    Character(
        name="liam",
        level=100,
        hp=9999,
        dmg=500,
        drops=[ITEM_DICT["ඞ"]],
        resistance="darkness",
        description="one of the makers of the game",
        spawn_locations=["debug"],
    ),
    Character(
        name="yeti",
        level=2,
        hp=150,
        dmg=30,
        drops=[ITEM_DICT["yeti fur"]],
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
    Character(
        name="ice cube",
        level=1,
        hp=70,
        dmg=12,
        drops=[ITEM_DICT["frost shard"]],
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
    Character(
        name="Nyx-spawn",
        level=4,
        hp=200,
        dmg=40,
        drops=[ITEM_DICT["shadow essence"]],
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
    Character(
        name="phoenix",
        level=3,
        hp=180,
        dmg=35,
        drops=[ITEM_DICT["phoenix feather"]],
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
    Character(
        name="shadow beast",
        level=2,
        hp=140,
        dmg=22,
        drops=[ITEM_DICT["dark fang"]],
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
    Character(
        name="ghost",
        level=1,
        hp=60,
        dmg=10,
        drops=[ITEM_DICT["wisp"]],
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
    Character(
        name="zombie",
        level=1,
        hp=50,
        dmg=8,
        drops=[ITEM_DICT["rotting flesh"]],
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
    Character(
        name="lord king",
        level=10,
        hp=1000,
        dmg=100,
        drops=[ITEM_DICT["king's crown"]],
        resistance="light",
        description="The ultimate ruler.",
        spawn_locations=["debug"],
    ),
    Character(
        name="lord king's guard",
        level=9,
        hp=500,
        dmg=50,
        drops=[ITEM_DICT["guard's emblem"]],
        resistance="light",
        description="The elite guard of the lord king.",
        spawn_locations=["debug"],
    ),
    Character(
        name="shadow dragon",
        level=10,
        hp=1200,
        dmg=120,
        drops=[ITEM_DICT["shadow scale"]],
        resistance="darkness",
        description="A dragon born from shadows.",
        spawn_locations=["debug"],
    ),
    Character(
        name="samus aran",
        level=50,
        hp=3000,
        dmg=300,
        drops=[ITEM_DICT["power suit"]],
        resistance="electric",
        description="A legendary bounty hunter.",
        spawn_locations=["debug"],
    ),  # nentendo please dont sue me
    Character(
        name="korock",
        level=0,
        hp=1,
        dmg=1,
        drops=[ITEM_DICT["the soul of a korock you monster"]],
        resistance="wind",
        description="A small plant-like creature from the land of hyrule.",
        spawn_locations=["debug"],
    ),
    Character(
        name="nintendo",
        level=100000000000000000000000000000000000000000000000,
        hp=999999999999999999999999999999999999999999999999,
        dmg=999999999999999999999999999999999999999999999999,
        drops=[ITEM_DICT["no one can get this item"]],
        resistance="light",
        description="the ultimate being",
        spawn_locations=["debug"],
    ),
]

monster_dict = {monster.name: monster for monster in monster_list}

group_attack_spells=[
    "lightning_core",
    "bomb_core",
    "blizzard_core",
]

mana_costs={"bomb core":15,"fire core":10,"lightning core":15,"electric core":10,"blizzard core":15,"ice core":10}
# team manager
class TeamManager:
    @staticmethod
    def get_start_team():
        return TeamManager(
            [
                Character(
                    name=f"character {i}",
                    level=1,
                    hp=50,
                    dmg=15,
                    description=f"character {i}",
                    xp=0,
                    npc=False,
                )
                for i in range(1, 4)
            ]
        )

    def __init__(self, characters: list[Character] = []):
        self.characters = characters

    def __repr__(self):
        return f'{"hp_max":self.hp_max,"hp":self.hp,"dmg":self.dmg,"drops":self.drops,"resistance":self.resistance,"teir":self.teir,"name":self.name,"description":self.description,"level":self.level,"max_mana":self.mana_max,"mana":self.mana,"xp":self.xp}'

    def __str__(self):
        return "\n".join([c.details() for c in self.characters])

    def remove_dead(self, person: int, targets: list[int] = []):
        if 0 <= person < len(self.hp) and self.hp[person] <= 0:
            self.remove(person, targets)

    def remove(self, person: Character):
        if person.hp > 0:
            return
        if not person.npc:
            print(f"{person.name} is unconscious")
            person.hp = -1
            if person in targets:
                try:
                    targets.remove(person)
                except ValueError:
                    pass
        else:
            for drop in person.drops:
                print(f"You got {drop.name} and killed {person.name}")
                inventory.grant(drop)
                
            if 0 <= person < len(targets):
                targets.pop(person)

    def level_up(self, person: Character):
        global monster_spawn_rate
        if not (0 <= person < len(self.level)):
            return
        person.level += 1
        person.hp_max += 10
        person.hp = person.hp_max
        person.mana_max += 10
        person.mana = person.mana_max
        if person.level % 7 == 0:
            monster_spawn_rate = min(monster_spawn_rate + 5, 70)
        person.dmg += 10

    def add_buff(self, damage_buff: int, person: Character):
        person.dmg += damage_buff

    def player_turn(
        self,
        enemies: "TeamManager",
    ):
        global inventory
        conscious_players = self.get_conscious_players()
        conscious_enemies = enemies.get_conscious_players()
        for player in conscious_players:
            print(f"{player.name} is at {player.hp}")
            while True:

                castable_spells = [spell for (spell, cost) in mana_costs.items() if cost <= player.mana]

                possible_actions = ["attack", "run"]
                if (inventory.has_usable_items()):
                    possible_actions.append('use item')
                if len(castable_spells) > 0:
                    possible_actions.append('magic')

                choice = util_functions.select_item(possible_actions, "What would you like to do?: ", force_selection=True)
                if choice == "run":
                    if util_functions.alternate_random((0, 5), int) == 1:
                        print("the monsters where too fast and caught you as you tried to run away")
                        break
                    else:
                        print("you successfully ran away!")
                        return "ran"
                elif choice=="use items":
                    if "returned" == inventory.choose_item_and_use(True, self, enemies):
                        continue 
                elif choice=="magic":
                    while True:
                        spell = util_functions.select_item(
                            castable_spells,
                            "what spell would you like to cast?: ",
                        )
                        if spell == None:
                            continue
                        if choice in group_attack_spells:
                            for enemy in conscious_enemies:
                                enemy.damage(player.dmg)
                        player.mana -= mana_costs[spell]
                        return "cast spell"
                elif choice=="attack":
                    target = util_functions.select_item(
                        conscious_enemies,
                        "what enemy do you want to attack: ")
                    target.damage(player.dmg, "normal", target)
                    target.remove_dead(target, list(range(len(enemies.hp))))

    def enemy_turn(self, enemies: "TeamManager"):
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
                self.remove_dead(target, continuous_players)
            elif num == 2:
                for j in continuous_players:
                    enemies.damage(enemies.dmg[i], "normal", j)
                    self.remove_dead(j, continuous_players)
            elif num == 3:
                if not continuous_players:
                    continue
                target = random.choice(continuous_players)
                enemies.damage(enemies.dmg[i] // 2, "resistant", target)
                self.remove_dead(target, continuous_players)
            elif num == 4:
                for j in continuous_players:
                    enemies.damage(enemies.dmg[i] // 2, "resistant", j)
                    self.remove_dead(j, continuous_players)

    def get_conscious_players(self):
        return [character for character in self.characters if character.hp > 0]


class InventoryItem:
    def __init__(self, item: Item, count: int = 0):
        self.item = item
        self.count = count


class InventoryManager:
    def __init__(
        self,
        starting_inventory: set[Item] = {ITEM_DICT["potion"], ITEM_DICT["mana pouch"]},
    ):
        self.inventory = {
            item.name: InventoryItem(item=item) for item in starting_inventory
        }

    def __repr__(self):
        return f"{self.get_inventory()}"

    def has_item(self, item_name: str):
        return item_name in self.inventory

    def grant(self, item: Item):
        if item.name in self.inventory:
            self.inventory[item.name].count += 1
        else:
            self.inventory[item.name] = InventoryItem(item)

    def get_length(self):
        return len(self.inventory)

    def get_inventory(self):
        return self.inventory

    def pick_enemy_target(self, enemies: TeamManager):
        return util_functions.select_item(
            enemies.get_conscious_players(),
            "who do you want to attack: ",
        )

    def pick_friendly_target(self, party: TeamManager):
        return util_functions.select_item(
            party.characters,
            "which character do ou want to have these effects applied to: ",
        )
    
    def has_usable_items(self):
        for i_item in self.inventory.values():
            if i_item.item.usable:
                return True
        return False
    
    def choose_item_and_use(
        self, usable: bool, party: TeamManager, enemy_party: TeamManager
    ):
        key: list[InventoryItem] = []
        if usable:
            while True:
                i_item = util_functions.select_item(
                    [
                        i_item
                        for i_item in self.inventory.values()
                        if i_item.item.usable
                    ],
                    "what do you want to use: ",
                )
                if i_item == None:
                    return "returned"
                effect = i_item.item.effect
                attack_item = effect.dmg > 0

                if effect.ඞ > 0:
                    for c in party.characters:
                        c.heal(c.hp_max)
                        c.gain_mana(c.mana_max)
                    dmg = util_functions.get_valid_type(int, "")
                    for character in party.characters:
                        character.damage(dmg, "normal")
                elif attack_item:
                    if effect.damage_type in [
                        "lightning_core",
                        "bomb_core",
                        "blizzard_core",
                    ]:
                        for character in enemy_party.get_conscious_players():
                            character.damage(effect.dmg, effect.damage_type)
                    else:
                        target = self.pick_enemy_target(enemy_party)
                        if target == None:
                            continue
                        target.damage(effect.dmg, effect.damage_type)
                else:
                    target = self.pick_friendly_target(party)
                    if target == None:
                        continue
                    if effect.heal > 0:
                        target.heal(effect.heal)
                    if effect.mana > 0:
                        target.gain_mana(effect.mana)
                i_item.count -= 1
                if i_item.count == 0:
                    self.inventory.pop(i_item.item.name)
        else:
            for i, i_item in enumerate(
                [x for x in self.inventory.values() if not x.item.usable]
            ):
                print(f"{i + 1} for {i_item.item.name}")

    ###### wth
    def __str__(self):
        return str(self.inventory)


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
    spawnable: list[Character] = []

    # Process override list
    if len(override) > 0:
        for name in override:
            if name in monster_dict:
                spawnable.append(monster_dict[name])
    else:
        # Process monsters based on location
        avg_level = max(1, sum(party_levels) // len(party_levels))
        possible: list[Character] = []
        not_location = f"~{location.name}"
        for monster in monster_dict.values():
            if (
                not_location not in monster.spawn_locations
                and "debug" not in monster.spawn_locations
                and monster.level <= avg_level
            ):
                possible.append(monster)
                random.choice(possible)
        for _ in range(random.randint(1, 3)):
            spawnable.append(random.choice(possible))
    for monster in spawnable:
        print(monster)
    return spawnable


if __name__ == "__main__":
    inventory = InventoryManager()
    inventory.grant("potion")
    print(inventory)
    spawn_monster([3, 3, 3], location_dict["h"])
