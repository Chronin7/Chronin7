import threading
import time
import random
import os
import curses
#defining vars ugg
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
"                                                                                               ",
"                                    checkpoint                                                 ",
"        this is       ███                                                                      ",
" ╔╧╗    a spike                         ╔╧╗                                                    ",
" ║▶║      ∆            █                ║◉║                                                    ",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
""
]
#constants
VIEW_HEIGHT = 50
VIEW_WIDTH = 95
BOARD_HEIGHT=len(board)
BOARD_WIDTH=len(board[0])
def board_eval(board):
	"""
	evaluates the board and returns the board and where the location of spisific blocks are
	"""
	out1=[]
	out2=[]
	for y in board:
		for x in y:
			if x =="█":
				out1.append("g")
			if x =="∆":
				out1.append("d")
			if x=="◉":
				out1.append("s")
			else:
				out1.append(" ")
		out2.append(out1)
		out1=[]
	return(out2)

board_val=board_eval(board)
def get_map(inboard):
	x=[]
	for line in inboard:
		row=[]
		for ch in line:
			row.append(ch)
		x.append(row)
	return x

def get_map_shown(playery, playerx):
	"""
	Returns a slice of the board centered around the player's y-coordinate.wdaw
	"""
	upper_bound = max(0, playery - VIEW_HEIGHT // 2)
	lower_bound = upper_bound + VIEW_HEIGHT
	# Ensure bounds don't exceed the board dimensions
	if lower_bound > BOARD_HEIGHT:
		lower_bound = BOARD_HEIGHT
		upper_bound = max(0, BOARD_HEIGHT - VIEW_HEIGHT)
	return board[upper_bound:lower_bound]

def print_buffer(buffer):
	"""Prints the buffer content to the console."""
	#os.system('cls' if os.name == 'nt' else 'clear')
	for line in buffer:
		for ch in line:
			print(ch, end="")
		print()

def get_key():
	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	char = screen.getch()

	key = screen.getch()
	new_key = key
	while new_key == key:
		new_key = screen.getch() # This will block until a new key is pressed or nodelay is active
	key = new_key
	return chr(char)

def board_game_loop(playerx, playery):
	"""
	Renders the game board with the player and handles boundary checks.
	"""
	# Get the visible part of the map
	visible_map_str = get_map_shown(playery, playerx)
	buffer = get_map(visible_map_str)
	# Calculate the player's *local* coordinates within the visible buffer
	local_playery = playery - (max(0, playery - VIEW_HEIGHT // 2))
	# Ensure player position is within the buffer boundaries
	if 0 <= local_playery < len(buffer) and 0 <= playerx < len(buffer[local_playery]):
		buffer[local_playery][playerx] = "࿄"
	print_buffer(buffer)
move=""
def moveer():
	global move
	move=get_key()
	board_game_loop(playerx,playery)
	return
movethred=threading.Thread(target=moveer)


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
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                                                                                              █",
"                             █                                                                █",
"                                                                                              █",
"                                                                                              █",
"                                  █                                                           █",
"                                                                                              █",
"                           █                                                                  █",
"                                █                                                             █",
"                                      █                                                       █",
"                                                                                              █",
"                                █                                                             █",
"                                                                                              █",
"                         █          checkpoint                                                █",
"        this is                                                                               █",
" ╔╧╗    a spike                        ╔╧╗                                                    █",
" ║★║      ▲            █               ║◉║                                                    █",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"███████████████████████████████████████████████████████████████████████████████████████████████",
"███████████████████████████████████████████████████████████████████████████████████████████████"]
BOARD_HEIGHT = len(board)
BOARD_WIDTH = len(board[0])
VIEW_HEIGHT=30
VIEW_WIDTH=95
win=False
# Variables
playerx = 2
playery = 305# Initial player y-position (adjusted for the ground)
on_ground = True
move_left = True
move_right = True
savex = 2
savey = playery
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
			elif x == "◀" or x== "▼" or x=="▶" or x=="▲":
				out1.append("d")
			elif x == "◉":
				out1.append("s")
			elif x== "⚐":
				out1.append("w")
			elif x in ["➊","➋","➌","➍","➎","➏","➐","➑","➒","➓","⓫","⓬","⓭","⓮","⓯","⓰","⓱","⓲","⓳","⓴"]:
				for count,y in enumerate(["➊","➋","➌","➍","➎","➏","➐","➑","➒","➓","⓫","⓬","⓭","⓮","⓯","⓰","⓱","⓲","⓳","⓴"]):
					if x==y:
						out1.append(count)
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

move=""
# Main game loop
while True:
		try:
			print("Program started. Press WASD. Press Ctrl+C to exit.")
			while True:
				try:
					movethred.start()
				except:
					pass
				move = get_key()
				
				# --- Handle Jump and Vertical Movement ---
				if move == " " or (move == "w" and on_ground):
					vol = 1
				
				# Apply gravity
				if vol > -1.5:  # Terminal velocity
					vol -= .125

				# Check for a collision on the next Y position
				if vol != 0:
					# Check incrementally for collision to avoid "tunneling"
					step_direction = -1 if vol > 0 else 1 # Move up or down
					# Loop through each step of the vertical movement
					for _ in range(abs(round(vol))):
						next_y = playery + step_direction
						
						# Check if the next position is a solid block
						if next_y < 0 or next_y >= BOARD_HEIGHT or board_val[next_y][playerx] == "g":
							if step_direction > 0: # Landing only happens when falling
								on_ground = True
							vol = 0 # Reset velocity and stop movement
							break # Stop all vertical movement
						else:
							playery = next_y # Move the player one step
				
				# --- Handle Horizontal Movement ---
				next_x = playerx
				if move =="k":
					print("you died")
					playerx = savex
					playery = savey
				if move == "a" and move_left:
					next_x = max(0, playerx - 1)
				if move == "d" and move_right:
					next_x = min(BOARD_WIDTH - 1, playerx + 1)
				# Check for horizontal obstacles at the new position
				if board_val[playery][next_x] != "g":
					playerx = next_x

				# --- Update Collision Flags ---
				on_ground = playery + 1 < BOARD_HEIGHT and board_val[playery + 1][playerx] == "g"

				# Corrected logic for horizontal movement flags to prevent index errors
				if playerx > 0:
					move_left = board_val[playery][playerx - 1] != "g"
				else:
					move_left = False

				if playerx < BOARD_WIDTH - 1:
					move_right = board_val[playery][playerx + 1] != "g"
				else:
					move_right = False
				
				# --- Render the Game Frame ---
				board_game_loop(playerx, playery)
				
				# --- Check for Game Events ---
				curant_pos = board_val[playery][playerx]
				if curant_pos == "d":
					print("You died!")
					time.sleep(0.5)
					playerx = savex
					playery = savey
				if curant_pos == "s":
					savex = playerx
					savey = playery
				if curant_pos == "w":
					win=True
					break
				# --- Control Frame Rate ---
				time.sleep(0.075)
					
		except KeyboardInterrupt:
			print("Ctrl+C detected. Shutting down...")
			quit()
		if win == True:
			break
print("you win")
