from logging import PlaceHolder 
import random
import copy
from tkinter import N
from game import MAP_HEIGHT, MAP_WIDTH, GameState, Location
import util_functions

try:
    from game import (
        mid,
        upper,
        underground,
        TeamManager,
        InventoryManager,
        location_dict,
        inventory,
        spawn_monster,
        monster_spawn_rate,
        ITEM_DICT,
        get_tile_at,
    )
except Exception:
    # If import fails, inform the user and stop.
    print(
        "Could not import game definitions from game.py. Make sure your game code (maps, TeamManager, InventoryManager, party, enemies, inventory) is in game.py."
    )
    raise
level_of_map = "mid"


def get_tile_at(pos: tuple[int, int], area: str):
    x, y = pos
    if area == "mid":
        return mid[y][x]
    if area == "upper":
        return upper[y][x]
    if area == "underground":
        return underground[y][x]
    return None


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# 1f9d
loot = [
    "potion",
    "magic weapon",
    "stone shard",
    "mana pouch",
    "lightning core",
    "lightning core",
    "electric core",
    "fire core",
    "lightning core",
    "blizzard core",
    "ice core",
    "lightning core",
    "electric core",
    "blizzard core",
    "blizzard core",
    "fire core",
    "fire core",
    "ice core",
]
nloot = ["fire gem", "dark gem", "resurrection gem", "frost gem", "wind gem", "power gem", "water gem"]

def only_get_one(num: int,game_state: GameState,nesasary:bool):
    global nloot
    global loot
    inv = game_state.inventory
    if loot[num]==None:
        return "alrady got, nothing here"
    if nesasary:
        inv.grant(nloot[num-1])
        nloot[num-1]=None
        return f"got {nloot[num-1]}"
    inv.grant(loot[num-1])
    loot[num-1]=None
    return f"got {loot[num-1]}"
def process_position(game_state: GameState):
    """
    Process the tile the party is standing on.
    Effects: items, special tiles, towns, spawn modifiers, etc.
    This function keeps the original idea: item grants, special events, towns with shops/gamble.
    """
    global loot
    global nloot
    global location_dict
    global level_of_map
    x, y = game_state.pos
    area = game_state.area
    tile = get_tile_at((x, y), area)
    inv = game_state.inventory

    if tile is None:
        print("You are out of bounds.")
        return
    # TODO: FIX THIS
    if "i" in tile:
        print(only_get_one(int(tile[1:]),game_state,False))
        return location_dict["i"]
    if "ni" in tile:
        print(only_get_one(int(tile[2:]),game_state,True))
        return location_dict["ni"]
    if "h" in tile:
        return location_dict["h"]
    if "l" in tile:
        return location_dict["l"]
    if "w" == tile:
        return location_dict["w"]
    if "c" in tile:
        if level_of_map == "underground":  # V to godhood
            choise = util_functions.get_valid_type(
                str,
                "do you want to ascend: ",
                "that is not an option, press enter to continue",
                ["yes", "no"],
            )
            if choise == "yes":
                print("you climb up to middle earth")
                level_of_map = "mid"
            if choise == "no":
                print("you stay underground")
        else:
            choise = util_functions.get_valid_type(
                str,
                "do you want to descend: ",
                "that is not an option, press enter to continue",
                ["yes", "no"],
            )
            if choise == "yes":
                print("you climb underground")
                level_of_map = "underground"
            if choise == "no":
                print("you stay in middle earth")
        return location_dict["c"]
    if "sk" in tile:
        if level_of_map == "mid":
            choise = util_functions.get_valid_type(
                str,
                "do you want to ascend: ",
                "that is not an option, press enter to continue",
                ["yes", "no"],
            )
            if choise == "yes":
                print("you climb up to middle earth")
                level_of_map = "mid"
            if choise == "no":
                print("you stay underground")
        else:
            choise = util_functions.get_valid_type(
                str,
                "do you want to descend: ",
                "that is not an option, press enter to continue",
                ["yes", "no"],
            )
            if choise == "yes":
                print("you get lifted skyward")
                level_of_map = "underground"
            if choise == "no":
                print("you stay in middle earth")
        return location_dict["sk"]
    if "b" in tile:
        return location_dict["b"]
    if "t" in tile:
        return location_dict["t"]
    if "f" in tile:
        return location_dict["f"]
    if "r" in tile:
        if inventory.has_item("water gem"):
            return Location(
                name= "river",
                description= "a flowing river",
                special="passable with gem of water",
            )
        else:
            raise Error("logic error at line 176")
    if "spawn" in tile:
        return location_dict["spawn"]
    if "s" == tile:
        return location_dict["s"]
    if "u" in tile:
        return location_dict["u"]
    if "g" in tile:
        if level_of_map == "underground":
            return Location(name="ground", description= "cave floor")
        return Location(name="ground", description="floating ground")
    if "aw" == tile:
        if inventory.has_item("water gem"):
            return location_dict["aw"]
    if "p" == tile:
        return location_dict["p"]
    if "f" in tile:
        return location_dict["f"]
    raise Error("logic error at line 190")


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def battle_loop(game_state: GameState, enemies_team: TeamManager):
    party_tm = game_state.party
    inv = game_state.inventory
    players_go = True
    while any(hp > 0 for hp in party_tm.hp) and any(hp > 0 for hp in enemies_team.hp):
        continuous_players = party_tm.get_conscious_players()
        if not continuous_players:
            print("All players are down.")
            break
        # Player turn
        result = party_tm.attack(True, continuous_players, enemies_team, party_tm)
        if result == "ran":
            print("You fled the battle.")
            return "ran"
╗
        # Remove dead enemies
        for i in range(len(enemies_team.hp) - 1, -1, -1):
            if enemies_team.hp[i] <= 0:
                inventory.grant(enemies_team[])
                enemies_team.remove(i, list(range(len(enemies_team.hp))))
        # Enemy turn
        continuous_players = party_tm.get_conscious_players()
        if not continuous_players:
            print("All players are down.")
            break
        party_tm.attack(False, continuous_players, enemies_team, party_tm)
        # Remove dead players for now need to make a way to revive them
        for i in range(len(party_tm.hp)):
            if party_tm.hp[i] <= 0:
                party_tm.remove_dead(i)
    # Award XP for surviving players
    if any(hp > 0 for hp in party_tm.hp) and not any(hp > 0 for hp in enemies_team.hp):
        xp_gain = 10 * len(enemies_team.hp)
        for i in range(len(party_tm.xp)):
            party_tm.xp[i] += xp_gain
            # level up while xp >= 25
            while party_tm.xp[i] >= 25:
                party_tm.xp[i] -= 25
                party_tm.level_up(i)
                print(f"{party_tm.name[i]} leveled up to {party_tm.level[i]}!")
    return "ended"

def can_go_to(pos:tuple[int,int], area: str, game_state: GameState):
    global location_dict
    x, y = pos
    if y < 0:
        return False
    if y >= MAP_HEIGHT:
        return False
    if x < 0:
        return False
    if x >= MAP_WIDTH:
        return False
    
    target = get_tile_at(pos, area)
    if not target:
        raise Error(f"There isn't a tile for ({x},{y}):{area}")
    if "ni" in target:
        location = location_dict["ni"]
    elif "i" in target:
        location = location_dict["i"]
    else:
        location = location_dict[target]
    if not location:
        raise Error(f"Location for '{target}' not found.")
    
    if game_state.inventory.has_item('ඞ'):
        return True
    
    if target in ['r','aw'] and not game_state.inventory.has_item('water gem'):
        return False
    
    return True


def main_loop():
    print("Welcome to the game.")
    play = util_functions.get_valid_type(
        str, "Do you want to play? (yes/no): ", "Please answer yes or no", ["yes", "no"]
    )
    if play != "yes":
        print("Goodbye.")
        return

    game_state = GameState()
    print(f"Starting position: {game_state.pos} on {game_state.area} map.")

    # Main exploration loop
    while any(hp > 0 for hp in game_state.party.hp):
        # Show possible directions
        x, y = game_state.pos
        area = game_state.area
        max_y = (
            len(mid) - 1
            if area == "mid"
            else (len(upper) - 1 if area == "upper" else len(underground) - 1)
        )
        max_x = (
            len(mid[0]) - 1
            if area == "mid"
            else (len(upper[0]) - 1 if area == "upper" else len(underground[0]) - 1)
        )
        options: list[str] = []
        
        if can_go_to((x,y-1),area,game_state):
            options.append("north")
        if can_go_to((x,y+1),area,game_state):
            options.append("south")
        if can_go_to((x+1,y),area,game_state):
            options.append("east")
        if can_go_to((x-1,y),area,game_state):
            options.append("west")
        options.append("status")
        options.append("inventory")
        options.append("quit")
        print(f"\nPosition: {game_state.pos} on {game_state.area}. Options: {options}")
        choice: str = util_functions.get_valid_type(
            str, "Choose direction or action: ", "Not valid", options
        )
        party = game_state.party
        if choice == "north":
            game_state.pos[1] -= 1
        elif choice == "south":
            game_state.pos[1] += 1
        elif choice == "east":
            game_state.pos[0] += 1
        elif choice == "west":
            game_state.pos[0] -= 1
        elif choice == "status":
            party = game_state.party
            for i in range(len(party.hp)):
                print(
                    f"{party.name[i]} - HP: {party.hp[i]}/{party.hp_max[i]}\nMana: {party.mana[i]}/{party.mana_max[i]}\nLevel: {party.level[i]}\nXP: {party.xp[i]}"
                )
            continue
        elif choice == "inventory":
            print("Inventory:",game_state.inventory)
            continue
        elif choice == "quit":
            print("Goodbye.")
            break
        # Process the tile player moved onto
        position = process_position(game_state)
        # Increase battle chance by spawn rate * 10
        print(f"location:{position.name}:{position.description}")
        game_state.battle_chance = min(
            100,
            game_state.battle_chance,
            + game_state.monster_spawn_rate * 2,
        )
        # Roll for monster spawn
        spawned = spawn_monster(party.level, position)
        if spawned:
            result = battle_loop(game_state, spawned)
            if result == "ran":
                continue

        # small passive mana regen or other per-step effects
        for i in range(len(game_state.party.hp)):
            if game_state.party.hp[i] > 0:
                game_state.party.gain_mana(1, i)

    print("Game over.")


if __name__ == "__main__":
    main_loop()
