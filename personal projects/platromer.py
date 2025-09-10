import threading
import time
import random
import os
#the board
board=[
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
["███████████████████████████████████████████████████████████████████████████████████████████████"]
]
#prints the board
def board_game_loop(playerx,playery):
	disprint=""
	vertprint=""
	for x in range(0,playerx):
		if board[playery][x] =="█":
			disprint=disprint+"█"
		else:
			disprint= disprint+" "
	for y in range(0,playery):
		vertprint=vertprint+"""
"""
	print(f"{disprint}x")
	print(vertprint,end="")
	print("")
