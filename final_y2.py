import random
import copy
import util_functions
try:
	from game import mid, upper, underground, TeamManager, InventoryManager,location_dict, party, inventory,spawn_monster, monster_spawn_rate, item_dict,setup_new_game,get_tile_at
except Exception:
	# If import fails, inform the user and stop.
	print("Could not import game definitions from game.py. Make sure your game code (maps, TeamManager, InventoryManager, party, enemies, inventory) is in game.py.")
	raise
level_of_map="mid"

def get_tile_at(pos, area):
	x, y = pos
	if area == 'mid':
		return mid[y][x]
	if area == 'upper':
		return upper[y][x]
	if area == 'underground':
		return underground[y][x]
	return None
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#1f9d
loot=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
nloot=[False,False,False,False,False,False,False]
def process_position(game_state):
	"""
	Process the tile the party is standing on.
	Effects: items, special tiles, towns, spawn modifiers, etc.
	This function keeps the original idea: item grants, special events, towns with shops/gamble.
	"""
	global loot
	global nloot
	global location_dict
	global level_of_map
	x, y = game_state['pos']
	area = game_state['area']
	tile = get_tile_at((x, y), area)
	inv = game_state['inventory']
	out={}
	if tile is None:
		print("You are out of bounds.")
		return
	if "i" in tile and loot[tile[-1]]==False:
		inv.grant(item_dict[tile[-1]])
	if "ni" in tile and nloot[tile[-1]]==False:
		inv.grant(item_dict[tile[-1]])
	if "h" in tile:
		return location_dict["h"]
	if "l" in tile:
		return location_dict["l"]
	if "w" in tile:
		return location_dict["w"]
	if "c" in tile:
		if level_of_map =="underground":                                  #V to godhood
			choise=util_functions.get_valid_type(str,"do you want to ascend: ","that is not an option, press enter to continue",["yes","no"])
			if choise == "yes":
				print("you climb up to middle earth")
				level_of_map="mid"
			if choise == "no":
					print("you stay underground")
		else:
			choise=util_functions.get_valid_type(str,"do you want to descend: ","that is not an option, press enter to continue",["yes","no"])
			if choise == "yes":
				print("you climb underground")
				level_of_map="underground"
			if choise == "no":
					print("you stay in middle earth")
	if "sk" in tile:
		if level_of_map =="mid":
			choise=util_functions.get_valid_type(str,"do you want to ascend: ","that is not an option, press enter to continue",["yes","no"])
			if choise == "yes":
				print("you climb up to middle earth")
				level_of_map="mid"
			if choise == "no":
					print("you stay underground")
		else:
			choise=util_functions.get_valid_type(str,"do you want to descend: ","that is not an option, press enter to continue",["yes","no"])
			if choise == "yes":
				print("you get lifted skyward")
				level_of_map="underground"
			if choise == "no":
					print("you stay in middle earth")
	if "b" in tile:
		return location_dict["b"]
	if "t" in tile:
		return location_dict["t"]
	if "f" in tile:
		return location_dict["f"]
	if "r" in tile:
		if inventory["water gem"]
			return {"name":"river","description":"a flowing river","special":"passable with gem of water"}
		return "go back"
	if "spawn" in tile:
		return location_dict["spawn"]
	if "s" in tile:
		return location_dict["s"]
	if "u" in tile:
		return location_dict["u"]
	if "g" in tile:
		if level_of_map=="underground":
			return {"name":"ground","description":"cave floor","speashal":None}
		return {"name":"ground","description":"floating ground","speashal":None}
	if "aw" in tile:
		if inventory["water gem"]
			return location_dict["aw"]
		return "go back"
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def battle_loop(game_state, enemies_team):
	party_tm = game_state['party']
	inv = game_state['inventory']
	players_go = True
	while any(hp > 0 for hp in party_tm.hp) and any(hp > 0 for hp in enemies_team.hp):
		continuous_players = party_tm.get_continuous_players()
		if not continuous_players:
			print("All players are down.")
			break
		# Player turn
		result = party_tm.attack(True, continuous_players, enemies_team,party_tm)
		if result == "ran":
			print("You fled the battle.")
			return "ran"
		
		# Remove dead enemies
		for i in range(len(enemies_team.hp)-1, -1, -1):
			if enemies_team.hp[i] <= 0:
				enemies_team.remove(i, list(range(len(enemies_team.hp))))
		# Enemy turn
		continuous_players = party_tm.get_continuous_players()
		if not continuous_players:
			print("All players are down.")
			break
		party_tm.attack(False, continuous_players, enemies_team,party_tm)
		# Remove dead players for now need to make a way to revive them
		for i in range(len(party_tm.hp)):
			if party_tm.hp[i] <= 0:
				party_tm.if_dead(i, None)
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

def main_loop():
	print("Welcome to the game.")
	play = util_functions.get_valid_type(str, "Do you want to play? (yes/no): ", "Please answer yes or no", ["yes", "no"])
	if play != "yes":
		print("Goodbye.")
		return

	game_state = setup_new_game()
	print(f"Starting position: {game_state['pos']} on {game_state['area']} map.")

	# Main exploration loop
	while any(hp > 0 for hp in game_state['party'].hp):
		# Show possible directions
		x, y = game_state['pos']
		area = game_state['area']
		max_y = len(mid) - 1 if area == 'mid' else (len(upper)-1 if area == 'upper' else len(underground)-1)
		max_x = len(mid[0]) - 1 if area == 'mid' else (len(upper[0])-1 if area == 'upper' else len(underground[0])-1)

		options = []
		if y > 0:
			options.append("north")
		if y < max_y:
			options.append("south")
		if x < max_x:
			options.append("east")
		if x > 0:
			options.append("west")
		options.append("status")
		options.append("inventory")
		options.append("quit")

		print(f"\nPosition: {game_state['pos']} on {game_state['area']}. Options: {options}")
		choice = util_functions.get_valid_type(str, "Choose direction or action: ", "Not valid", options)

		if choice == "north":
			game_state['pos'][1] -= 1
		elif choice == "south":
			game_state['pos'][1] += 1
		elif choice == "east":
			game_state['pos'][0] += 1
		elif choice == "west":
			game_state['pos'][0] -= 1
		elif choice == "status":
			for i in range(len(game_state['party'].hp)):
				print(f"{game_state['party'].name[i]} - HP: {game_state['party'].hp[i]}/{game_state['party'].hp_max[i]}  Mana: {game_state['party'].mana[i]}/{game_state['party'].mana_max[i]}  Level: {game_state['party'].level[i]}  XP: {game_state['party'].xp[i]}")
			continue
		elif choice == "inventory":
			print("Inventory:", game_state['inventory'].get_inventory())
			continue
		elif choice == "quit":
			print("Goodbye.")
			break
		# Process the tile player moved onto
		process_position(game_state)
		# Increase battle chance by spawn rate * 10
		game_state['battle_chance'] = min(100, game_state.get('battle_chance', 20) + game_state.get('monster_spawn_rate', 20) * 10)

		# Roll for monster spawn
		spawned = spawn_monster(party.level,)
		if spawned:
			result = battle_loop(game_state, spawned)
			if result == "ran":
				continue

		#small passive mana regen or other per-step effects
		for i in range(len(game_state['party'].hp)):
			if game_state['party'].hp[i] > 0:
				game_state['party'].gain_mana(1, i)

	print("Game over.")

if __name__ == "__main__":
	main_loop()
