import threading
import time
import random
import os
import keyboard
#defining vars
playerx=2
playery=102
on_ground=True
move_left=True
move_right=True
savex=2
savey=102
vol=0
curant_pos =" "
#the board
board=[
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                                                                               ",
"                                    checkpoint                                                 ",
"        this is       ███                                                                      ",
" ╔╧╗    a spike                        ╔╧╗                                                    ",
" ║★║      ∆            █               ║◉║                                                    ",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"███████████████████████████████████████████████████████████████████████████████████████████████"]
BOARD_HEIGHT = len(board)
BOARD_WIDTH = len(board[0])
VIEW_HEIGHT=10
VIEW_WIDTH=95
# Variables
playerx = 2
playery = 102 # Initial player y-position (adjusted for the ground)
on_ground = True
move_left = True
move_right = True
savex = 2
savey = 102
vol = 0
curant_pos = " "

def board_eval(board):
	"""Evaluates the board and returns the location of specific blocks."""
	out2 = []
	for y in board:
		out1 = []
		for x in y:
			if x == "█":
				out1.append("g")
			elif x == "∆":
				out1.append("d")
			elif x == "◉":
				out1.append("s")
			else:
				out1.append(" ")
		out2.append(out1)
	return out2

board_val = board_eval(board)

def get_map(inboard):
	"""Converts a list of strings into a list of lists of characters."""
	x = []
	for line in inboard:
		row = list(line)
		x.append(row)
	return x

def get_map_shown(playery, playerx):
	"""Returns a slice of the board centered around the player's position."""
	upper_bound_y = max(0, playery - VIEW_HEIGHT // 2)
	lower_bound_y = upper_bound_y + VIEW_HEIGHT
	if lower_bound_y > BOARD_HEIGHT:
		lower_bound_y = BOARD_HEIGHT
		upper_bound_y = max(0, BOARD_HEIGHT - VIEW_HEIGHT)

	upper_bound_x = max(0, playerx - VIEW_WIDTH // 2)
	lower_bound_x = upper_bound_x + VIEW_WIDTH
	if lower_bound_x > BOARD_WIDTH:
		lower_bound_x = BOARD_WIDTH
		upper_bound_x = max(0, BOARD_WIDTH - VIEW_WIDTH)

	visible_map_str = []
	for y in range(upper_bound_y, lower_bound_y):
		line = board[y][upper_bound_x:lower_bound_x]
		visible_map_str.append(line)
	
	return visible_map_str, upper_bound_x, upper_bound_y


def print_buffer(buffer):
	"""Prints the buffer content to the console."""
	os.system('cls' if os.name == 'nt' else 'clear')
	for line in buffer:
		print("".join(line))

def board_game_loop(playerx, playery):
	"""Renders the game board with the player and handles boundary checks."""
	visible_map_str, view_x_start, view_y_start = get_map_shown(playery, playerx)
	buffer = get_map(visible_map_str)
	
	local_playery = playery - view_y_start
	local_playerx = playerx - view_x_start

	# Ensure player position is within the buffer boundaries
	if 0 <= local_playery < len(buffer) and 0 <= local_playerx < len(buffer[local_playery]):
		buffer[local_playery][local_playerx] = "࿄"
	print_buffer(buffer)


# Main game loop
while True:
	# Handle input using is_pressed for continuous action
	if keyboard.is_pressed(" ") or keyboard.is_pressed("w") and on_ground:
		vol = 3

	# Update vertical movement based on velocity
	if vol != 0 or not on_ground:
		
		# Check for a block above the player during an upward jump
		if vol > 0:
			next_y = playery - vol
			if next_y >= 0 and board_val[next_y][playerx] == "g":
				playery = next_y + 1 # Move player to just below the ceiling
				vol = 0 # Kill upward momentum
			else:
				playery = next_y
		
		# Check for a block below the player during a downward movement
		elif vol < 0:
			next_y = playery - vol
			# Look at the ground one step ahead
			if next_y + 1 < BOARD_HEIGHT and board_val[next_y + 1][playerx] == "g":
				playery = next_y # Position player on top of the block
				vol = 0 # Kill downward momentum
			else:
				playery = next_y
		
		# Apply gravity
		if vol > -3: # Terminal velocity
			vol -= 1

	# --- HORIZONTAL MOVEMENT ---
	next_x = playerx
	if keyboard.is_pressed("a") and move_left:
		next_x = max(0, playerx - 1)
	if keyboard.is_pressed("d") and move_right:
		next_x = min(BOARD_WIDTH - 1, playerx + 1)
	
	# Check for horizontal obstacles at the new position
	if board_val[playery][next_x] != "g":
		playerx = next_x

	# Update collision flags
	# Check if there is ground below player
	if playery + 1 < BOARD_HEIGHT and board_val[playery + 1][playerx] == "g":
		on_ground = True
	else:
		on_ground = False
	
	# Check for walls left of player
	if playerx > 0 and board_val[playery][playerx - 1] == "g":
		move_left = False
	else:
		move_left = True
	
	# Check for walls right of player
	if playerx < BOARD_WIDTH - 1 and board_val[playery][playerx + 1] == "g":
		move_right = False
	else:
		move_right = True

	# Check current position for game events (death, save)
	curant_pos = board_val[playery][playerx]
	if curant_pos == "d":
		# Death
		print("You died!")
		input()
		playerx = savex
		playery = savey
	if curant_pos == "s":
		# Save stations
		savex = playerx
		savey = playery

	# Render the game frame
	board_game_loop(playerx, playery)
	
	# Control frame rate
	time.sleep(.05)