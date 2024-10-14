import random
board = [None] * 9
def piece_char(i, c):
	if c == "X":
		return "✗"
	elif c == "O":
		return "○"
	else:
		return "" + str(i+1)
def print_board(board):
	for i, place in enumerate(board):	
		c = piece_char(i, place)
		if (i + 1) % 3 == 0:
			print(f" {c} ")
			if i <=6:
				print("-----------")
		else:
			print(f" {c} |", end="")
	print()
def possible_boards(cBoard,turn):
	moves = []
	for i in range(9):
		if cBoard[i] == None:
			newBoard = cBoard.copy()
			newBoard[i] = turn
			moves.append(newBoard)
	return moves

def choose_move(cBoard, turn):
	possible = possible_boards(cBoard, turn)

	if len(possible) == 1:
		return possible[0]

	nextTurn = "X"
	if turn == "X":
		nextTurn = "O"

	bestBoard = possible[0]
	bestX, bestO, bestT = score_move(bestBoard, nextTurn)

	for b in possible[1:]:
		x, o, t = score_move(b, nextTurn)
		if turn == "X":
			if o > bestO:
				continue
			elif x > bestX:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
			elif t > bestT and o < bestO and x >= bestX:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
		else:
			if x > bestX:
				continue
			elif o > bestO:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
			elif t > bestT and x < bestX and o >= bestO:
				bestX = x
				bestO = o
				bestT = t
				bestBoard = b
	return bestBoard

def score_move(cBoard, turn):
	possible = possible_boards(cBoard, turn)
	x = 0.0
	o = 0.0
	t = 0.0
	for i, b in enumerate(possible):
		result = check_win(b)
		if result == "tie":
			return (0.0, 0.0, 1.0)
		elif result == "X":
			return (1.0, 0.0, 0.0)
		elif result == "O":
			return (0.0, 1.0, 0.0)
		elif turn == "X":
			bx, bo, bt = score_move(b, "O")
			x += bx
			o += bo
			t += bt
		else:
			bx, bo, bt = score_move(b, "X")
			x += bx
			o += bo
			t += bt
	# x /= len(possible)
	# o /= len(possible)
	# t /= len(possible)
	return(x,o,t)
		
def check_win(board):
	for c in ["X","O"]:
		if board[0] == c and board[1] == c and board[2] == c:
			return c
		elif board[3] == c and board[4] == c and board[5] == c:
			return c
		elif board[6] == c and board[7] == c and board[8] == c:
			return c
		elif board[0] == c and board[3] == c and board[6] == c:
			return c
		elif board[1] == c and board[4] == c and board[7] == c:
			return c
		elif board[2] == c and board[5] == c and board[8] == c:
			return c
		elif board[0] == c and board[4] == c and board[8] == c:
			return c
		elif board[2] == c and board[4] == c and board[6] == c:
			return c
	for x in board:
		if x == None:
			return None
	return "tie"

def check_move(board, playerMove):
	playerMove -= 1
	return board[playerMove] == None
while True:
	board = choose_move(board, "X")
	if check_win(board) != None:
		print_board(board)
		print(check_win(board))
		break
	while True:
		print_board(board)
		if check_win(board) != None:
			break
		print("1 for top left")
		print("2 for top middle")
		print("3 for top right")
		print("4 for middle left")
		print("5 for middle middle")
		print("6 for middle right")
		print("7 for bottom left")
		print("8 for bottom middle")
		print("9 for bottom right")
		play_go = int(input("where do you want to go: "))
		if play_go < 10 and play_go > 0:
			if play_go == 1 and board[0] != None:
				print("that is alredy taken")
			elif play_go == 2 and board[1] != None:
				print("that is alredy taken")
			elif play_go == 3 and board[2] != None:
				print("that is alredy taken")
			elif play_go == 4 and board[3] != None:
				print("that is alredy taken")
			elif play_go == 5 and board[4] != None:
				print("that is alredy taken")
			elif play_go == 6 and board[5] != None:
				print("that is alredy taken")
			elif play_go == 7 and board[6] != None:
				print("that is alredy taken")
			elif play_go == 8 and board[7] != None:
				print("that is alredy taken")
			elif play_go == 9 and board[8] != None:
				print("that is alredy taken")
			else:
				if play_go == 1:
					board[0] = "O"
				if play_go == 2:
					board[1] = "O"
				if play_go == 3:
					board[2] = "O"
				if play_go == 4:
					board[3] = "O"
				if play_go == 5:
					board[4] = "O"
				if play_go == 6:
					board[5] = "O"
				if play_go == 7:
					board[6] = "O"
				if play_go == 8:
					board[7] = "O"
				if play_go == 9:
					board[8] = "O"
				print_board(board)
				possible_boards(board, "X")
				break
		else:
			print("nope")
	if check_win(board) != None:
		print(check_win(board))
		print_board(board)
		break
def print_X():
	print("""
    ███          ███
	  ███      ███
	    ███  ███
          ████
        ███  ███
      ███      ███
    ███          ███
""",flush=False)
def print_O():
	print("""
       ███████████
    ███           ███
   ███             ███
   ███             ███
   ███             ███
   ███             ███
	███           ███
	   ███████████
""",sep=True)
print_X
print_O
def print_board(board):
	for i, place in enumerate(board):	
		c = piece_char(i, place)
		if (i + 1) % 3 == 0:
			print(f" {c} ")
			if i <=6:
				print("-----------")
		else:
			print(f" {c} |", end="")

def p_board(board):
	p
row1 ="	                     ██	                     ██                               "
row2 ="	                     ██	                     ██                               "
row3 ="	                     ██	                     ██                               "
row4 ="	                     ██	                     ██                               "
row5 ="	                     ██	                     ██                               "
row6 ="	                     ██	                     ██                               "
row7 ="	                     ██                      ██                               "
row8 ="	                     ██	                     ██                               "
row9 ="	                     ██	                     ██                               "
row10 ="███████████████████████████████████████████████████████████████████████████████"
row11 ="	                     ██	                     ██                               "
row12 ="	                     ██	                     ██                               "
row13 ="	                     ██	                     ██                               "
row14 ="	                     ██	                     ██                               "
row15 ="	                     ██	                     ██                               "
row16 ="	                     ██	                     ██                               "
row17 ="	                     ██                      ██                               "
row18 ="	                     ██	                     ██                               "
row19 ="	                     ██	                     ██                               "
row20 ="███████████████████████████████████████████████████████████████████████████████"
row21 ="	                     ██	                     ██                               "
row22 ="	                     ██	                     ██                               "
row23 ="	                     ██	                     ██                               "
row24 ="	                     ██	                     ██                               "
row25 ="	                     ██	                     ██                               "
row26 ="	                     ██	                     ██                               "
row27 ="	                     ██                      ██                               "
row28 ="	                     ██	                     ██                               "
row29 ="	                     ██	                     ██                               "
q1 = f"""
	                     ██
   {q1111111111111111}   ██
   {q2222222222222222}   ██
   {q3333333333333333}   ██
   {q4444444444444444}   ██
   {q5555555555555555}   ██
   {q6666666666666666}   ██
   {q7777777777777777}   ██
   {}    ██
						 ██
"""

       ███████████
    ███           ███
   ███             ███
   ███             ███
   ███             ███
   ███             ███
	███           ███
	   ███████████
