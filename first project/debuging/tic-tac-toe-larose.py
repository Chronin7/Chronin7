board = [None] * 9
def piece_char(i, c):
	if c == "X":
		return "✗"
	elif c == "O":
		return "○"
	else:
		return "" + str(i+1)
def go_for_win(board):
	for x in rate # make the ai go for the win
def print_board(board):
	b1 = []
	b2 = []
	b3 = []
	itera = -1
	for x in board:
		itera += 1
		if itera < 3:
			b1.append(x)
		elif itera < 6:
			b2.append(x)
		else:
			b3.append(x)
	intern = 0
	while True:
		iteration = 0
		intern += 1
		while True:
			if iteration ==2 or iteration ==5 or iteration == 8:
				if intern < 2:
					if b1[iteration] != None:
						print(f" {b1[iteration]} ")
					else:
						print("   ")
				elif intern < 3:
					if b2[iteration] != None:
						print(f" {b2[iteration]} ")
					else:
						print("   ")
				else:
					if b3[iteration] != None:
						print(f" {b3[iteration]} ")
					else:
						print("   ")
				break
			if intern < 2:
				if b1[iteration] != None:
					print(f" {b1[iteration]} |",end="")
				else:
					print("   |",end="")
			elif intern < 3:
				if b2[iteration] != None:
					print(f" {b2[iteration]} |",end="")
				else:
					print("   |",end="")
			else:
				if b3[iteration] != None:
					print(f" {b3[iteration]} |",end="")
				else:
					print("   |",end="")
			iteration +=1
		if intern == 3:
			break
		print("-----------")
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
			elif t > bestT or o < bestO and x >= bestX or o<bestO or :
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
		choose_move(board, "X")
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
				possible_boards(board, "X")
				break
		else:
			print("nope")
	if check_win(board) != None:
		print(check_win(board))
		print_board(board)
		break