import random
import copy
import util_functions
try:
	from game import mid, upper, underground, TeamManager, InventoryManager, party, enemies, inventory, monster_spawn_rate
except Exception:
	# If import fails, inform the user and stop.
	print("Could not import game definitions from game.py. Make sure your game code (maps, TeamManager, InventoryManager, party, enemies, inventory) is in game.py.")
	raise

def setup_new_game():
	"""
	Initialize a fresh party, inventory, and starting position.
	Returns a dict with game state.
	"""
	# copy party/enemies/inventory so we don't mutate original templates
	game_state = {}
	game_state['party'] = party  # party is already a TeamManager instance in game.py
	game_state['enemies_template'] = enemies  # template for enemy types
	game_state['inventory'] = inventory  # InventoryManager instance
	# Starting position (as in your design)
	game_state['pos'] = [15, 18]  # x, y
	game_state['area'] = 'mid'  # which map we're on: 'mid', 'upper', 'underground'
	game_state['battle_chance'] = 20  # base battle chance
	game_state['monster_spawn_rate'] = monster_spawn_rate if 'monster_spawn_rate' in globals() else 20
	return game_state

def get_tile_at(pos, area):
	x, y = pos
	if area == 'mid':
		return mid[y][x]
	if area == 'upper':
		return upper[y][x]
	if area == 'underground':
		return underground[y][x]
	return None

def process_position(game_state):
	"""
	Process the tile the party is standing on.
	Effects: items, special tiles, towns, spawn modifiers, etc.
	This function keeps the original idea: item grants, special events, towns with shops/gamble.
	"""
	x, y = game_state['pos']
	area = game_state['area']
	tile = get_tile_at((x, y), area)
	inv = game_state['inventory']

	# Basic tile handling (extend as needed)
	if tile is None:
		print("You are out of bounds.")
		return

	if tile.startswith('i'):  # item tile like i1, i2...
		# Example: grant a simple potion for any item tile
		item = {"name": "potion", "quantity": 1, "useable": True, "effect": {"heal": 30}}
		inv.grant(item)
		print(f"You found an item: {item['name']}")
		# Optionally mark tile as visited by replacing with 'h' (here we won't modify maps)
		return

	if tile == 'spawn':
		# Increase local spawn chance
		game_state['battle_chance'] += game_state['monster_spawn_rate'] * 10
		print("This area feels dangerous... monsters may appear more often.")
		return

	if tile == 'town' or tile == 't':
		# Town interaction: shop, gamble, leave
		while True:
			print("\nYou are in a town. Options: shop, gamble, leave")
			choice = util_functions.get_valid_type(str, "Choose: ", "Not a valid option", ["shop", "gamble", "leave"])
			if choice == "shop":
				# Simple shop: sell a potion for 10 gold (we don't track gold in this simple main)
				print("Shop is not fully implemented in this demo.")
			elif choice == "gamble":
				print("Gambling not implemented in this demo.")
			elif choice == "leave":
				print("You leave the town.")
				break
		return

	if tile == 'speshal' or tile == 'spehsal':
		print("You found a special tile. Something interesting might happen here.")
		# Placeholder for special events
		return

	# Water/lava handling (as in your design)
	if tile == 'w':
		print("You are at a wall or water tile; movement may be restricted.")
		return
	if tile == 'l':
		print("This tile is lava or illegal to stand on; be careful.")
		return

	# Default: nothing special
	return

def spawn_monsters(game_state):
	"""
	Decide whether to spawn monsters based on battle chance and monster_spawn_rate.
	Returns a TeamManager instance for the spawned monsters or None.
	"""
	chance = game_state['battle_chance']
	roll = random.randint(1, 100)
	if roll <= chance:
		# Determine number of monsters: 1 to min(round((random-num)/33),3) in original pseudo
		# We'll approximate: spawn_count = random between 1 and min( max(1, party average level), 3)
		party_levels = game_state['party'].level
		avg_level = max(1, sum(party_levels) // len(party_levels))
		spawn_count = random.randint(1, min(avg_level, 3))
		# Build a list of random monsters based on enemies_template
		template = game_state['enemies_template']
		spawned_hp = []
		spawned_dmg = []
		spawned_drops = []
		spawned_res = []
		spawned_teir = []
		spawned_name = []
		spawned_desc = []
		for _ in range(spawn_count):
			idx = random.randint(0, len(template.hp)-1)
			spawned_hp.append(template.hp_max[idx])
			spawned_dmg.append(template.dmg[idx])
			spawned_drops.append(template.drops[idx])
			spawned_res.append(template.resistance[idx])
			spawned_teir.append(template.teir[idx])
			spawned_name.append(template.name[idx])
			spawned_desc.append(template.description[idx])
		spawned = TeamManager(spawned_hp, spawned_dmg, spawned_drops, spawned_res, spawned_teir, spawned_name, spawned_desc)
		print(f"Monsters appeared: {', '.join(spawned_name)}")
		return spawned
	return None

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
		spawned = spawn_monsters(game_state)
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
