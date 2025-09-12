import threading
import time
import random
import os
import curses
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

def get_single_char():
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
#main game loop
move=""
def moveer():
	global move
	move=get_single_char()
	board_game_loop(playerx,playery)
	return
movethred=threading.Thread(target=moveer)

while True: 
	try:
		movethred.start()
	except:
		pass
	#print(board_val[playery][playerx])
	#print(playerx)
	#print(playery)
	#print(board_val)
	#print(len(board))
	print(move)
	if move in [" ","w"] and on_ground==True:
		vol=3
	if move=="a" and move_right==True:
		playerx = max(0, playerx - 1)
	if move=="d" and move_left==True:
		playerx = min(BOARD_WIDTH - 1, playerx + 1)
	if vol != 0 or on_ground==False:
		playery = max(0, playery-vol)
		if not vol <= -1:
			vol-=1
	curses.flushinp()
	move=""
	curant_pos =board_val[playery][playerx]
	if curant_pos=="d":
		#death
		print("you died")
		input()
		playerx=savex
		playery=savey
	if curant_pos=="s":
		#save stations
		savex=playerx
		savey=playery
	#checking if there is ground below player
	if board_val[playery+1][playerx]=="g":
		on_ground=True
	else:
		on_ground=False
	try:
		#checking if ground is left of player
		if board_val[playery][playerx-1]=="g":
			move_left=False
		else:
			move_left=True
	except:
		#this is so if player is next to out of bounds they cant go out
		move_left=False
	try:
		#checking if ground is left of player
		if board_val[playery][playerx-1]=="g":
			move_right=False
		else:
			move_right=True
	except:
		#this is so if player is next to out of bounds they cant go out
		move_right=False


