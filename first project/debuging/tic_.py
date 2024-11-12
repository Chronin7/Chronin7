
board = [None] * 9
def print_board(board):
	iteration = -1
	for x in board:
		iteration += 1
		if iteration == 0:
			if x == "O":
				q11 = "      ███████████     "
				q12 = "    ███         ███   "
				q13 = "   ███           ███  "
				q14 = "   ███           ███  "
				q15 = "   ███           ███  "
				q16 = "   ███           ███  "
				q17 = "    ███         ███   "
				q18 = "      ███████████     "
			elif x == "X":
				q11 = "   ███         ███    "
				q12 = "     ███     ███      "
				q13 = "       ███ ███        "
				q14 = "        █████         "
				q15 = "        █████         "
				q16 = "       ███ ███        "
				q17 = "     ███     ███      "
				q18 = "   ███         ███    "
			else:
				q11 = "                      "
				q12 = "                      "
				q13 = "                      "
				q14 = "                      "
				q15 = "                      "
				q16 = "                      "
				q17 = "                      "
				q18 = "                      "
		elif iteration == 1:
			if x == "O":
				q21 = "      ███████████     "
				q22 = "    ███         ███   "
				q23 = "   ███           ███  "
				q24 = "   ███           ███  "
				q25 = "   ███           ███  "
				q26 = "   ███           ███  "
				q27 = "    ███         ███   "
				q28 = "      ███████████     "
			elif x == "X":
				q21 = "   ███         ███    "
				q22 = "     ███     ███      "
				q23 = "       ███ ███        "
				q24 = "        █████         "
				q25 = "        █████         "
				q26 = "       ███ ███        "
				q27 = "     ███     ███      "
				q28 = "   ███         ███    "
			else:
				q21 = "                      "
				q22 = "                      "
				q23 = "                      "
				q24 = "                      "
				q25 = "                      "
				q26 = "                      "
				q27 = "                      "
				q28 = "                      "
		elif iteration == 2:
			if x == "O":
				q31 = "      ███████████     "
				q32 = "    ███         ███   "
				q33 = "   ███           ███  "
				q34 = "   ███           ███  "
				q35 = "   ███           ███  "
				q36 = "   ███           ███  "
				q37 = "    ███         ███   "
				q38 = "      ███████████     "
			elif x == "X":
				q31 = "   ███         ███    "
				q32 = "     ███     ███      "
				q33 = "       ███ ███        "
				q34 = "        █████         "
				q35 = "        █████         "
				q36 = "       ███ ███        "
				q37 = "     ███     ███      "
				q38 = "   ███         ███    "
			else:
				q31 = "                      "
				q32 = "                      "
				q33 = "                      "
				q34 = "                      "
				q35 = "                      "
				q36 = "                      "
				q37 = "                      "
				q38 = "                      "
		elif iteration == 3:
			if x == "O":
				q41 = "      ███████████     "
				q42 = "    ███         ███   "
				q43 = "   ███           ███  "
				q44 = "   ███           ███  "
				q45 = "   ███           ███  "
				q46 = "   ███           ███  "
				q47 = "    ███         ███   "
				q48 = "      ███████████     "
			elif x == "X":
				q41 = "   ███         ███    "
				q42 = "     ███     ███      "
				q43 = "       ███ ███        "
				q44 = "        █████         "
				q45 = "        █████         "
				q46 = "       ███ ███        "
				q47 = "     ███     ███      "
				q48 = "   ███         ███    "
			else:
				q41 = "                      "
				q42 = "                      "
				q43 = "                      "
				q44 = "                      "
				q45 = "                      "
				q46 = "                      "
				q47 = "                      "
				q48 = "                      "
		elif iteration == 4:
			if x == "O":
				q51 = "      ███████████     "
				q52 = "    ███         ███   "
				q53 = "   ███           ███  "
				q54 = "   ███           ███  "
				q55 = "   ███           ███  "
				q56 = "   ███           ███  "
				q57 = "    ███         ███   "
				q58 = "      ███████████     "
			elif x == "X":
				q51 = "   ███         ███    "
				q52 = "     ███     ███      "
				q53 = "       ███ ███        "
				q54 = "        █████         "
				q55 = "        █████         "
				q56 = "       ███ ███        "
				q57 = "     ███     ███      "
				q58 = "   ███         ███    "
			else:
				q51 = "                      "
				q52 = "                      "
				q53 = "                      "
				q54 = "                      "
				q55 = "                      "
				q56 = "                      "
				q57 = "                      "
				q58 = "                      "
		elif iteration == 5:
			if x == "O":
				q61 = "      ███████████     "
				q62 = "    ███         ███   "
				q63 = "   ███           ███  "
				q64 = "   ███           ███  "
				q65 = "   ███           ███  "
				q66 = "   ███           ███  "
				q67 = "    ███         ███   "
				q68 = "      ███████████     "
			elif x == "X":
				q61 = "   ███         ███    "
				q62 = "     ███     ███      "
				q63 = "       ███ ███        "
				q64 = "        █████         "
				q65 = "        █████         "
				q66 = "       ███ ███        "
				q67 = "     ███     ███      "
				q68 = "   ███         ███    "
			else:
				q61 = "                      "
				q62 = "                      "
				q63 = "                      "
				q64 = "                      "
				q65 = "                      "
				q66 = "                      "
				q67 = "                      "
				q68 = "                      "
		elif iteration == 6:
			if x == "O":
				q71 = "      ███████████     "
				q72 = "    ███         ███   "
				q73 = "   ███           ███  "
				q74 = "   ███           ███  "
				q75 = "   ███           ███  "
				q76 = "   ███           ███  "
				q77 = "    ███         ███   "
				q78 = "      ███████████     "
			elif x == "X":
				q71 = "   ███         ███    "
				q72 = "     ███     ███      "
				q73 = "       ███ ███        "
				q74 = "        █████         "
				q75 = "        █████         "
				q76 = "       ███ ███        "
				q77 = "     ███     ███      "
				q78 = "   ███         ███    "
			else:
				q71 = "                      "
				q72 = "                      "
				q73 = "                      "
				q74 = "                      "
				q75 = "                      "
				q76 = "                      "
				q77 = "                      "
				q78 = "                      "
		elif iteration == 7:
			if x == "O":
				q81 = "      ███████████     "
				q82 = "    ███         ███   "
				q83 = "   ███           ███  "
				q84 = "   ███           ███  "
				q85 = "   ███           ███  "
				q86 = "   ███           ███  "
				q87 = "    ███         ███   "
				q88 = "      ███████████     "
			elif x == "X":
				q81 = "   ███         ███    "
				q82 = "     ███     ███      "
				q83 = "       ███ ███        "
				q84 = "        █████         "
				q85 = "        █████         "
				q86 = "       ███ ███        "
				q87 = "     ███     ███      "
				q88 = "   ███         ███    "
			else:
				q81 = "                      "
				q82 = "                      "
				q83 = "                      "
				q84 = "                      "
				q85 = "                      "
				q86 = "                      "
				q87 = "                      "
				q88 = "                      "
		elif iteration == 8:
			if x == "O":
				q91 = "      ███████████     "
				q92 = "    ███         ███   "
				q93 = "   ███           ███  "
				q94 = "   ███           ███  "
				q95 = "   ███           ███  "
				q96 = "   ███           ███  "
				q97 = "    ███         ███   "
				q98 = "      ███████████     "
			elif x == "X":
				q91 = "   ███         ███    "
				q92 = "     ███     ███      "
				q93 = "       ███ ███        "
				q94 = "        █████         "
				q95 = "        █████         "
				q96 = "       ███ ███        "
				q97 = "     ███     ███      "
				q98 = "   ███         ███    "
			else:
				q91 = "                      "
				q92 = "                      "
				q93 = "                      "
				q94 = "                      "
				q95 = "                      "
				q96 = "                      "
				q97 = "                      "
				q98 = "                      "
			q1 = f"""
				 ██                            ██
	{q11}   ██   {q21}   ██   {q31}
	{q12}   ██   {q22}   ██   {q32}
	{q13}   ██   {q23}   ██   {q33}
	{q14}   ██   {q24}   ██   {q34}
	{q15}   ██   {q25}   ██   {q35}
	{q16}   ██   {q26}   ██   {q36}
	{q17}   ██   {q27}   ██   {q37}
	{q18}   ██   {q28}   ██   {q38}
                                 ██			       ██
       ████████████████████████████████████████████████████████████████████████████████████████
				 ██                            ██
	{q41}   ██   {q51}   ██   {q61}
	{q42}   ██   {q52}   ██   {q62}
	{q43}   ██   {q53}   ██   {q63}
	{q44}   ██   {q54}   ██   {q64}
	{q45}   ██   {q55}   ██   {q65}
	{q46}   ██   {q56}   ██   {q66}
	{q47}   ██   {q57}   ██   {q67}
	{q48}   ██   {q58}   ██   {q68}
                                 ██		               ██
       ████████████████████████████████████████████████████████████████████████████████████████
				 ██                            ██
	{q71}   ██   {q81}   ██   {q91}
	{q72}   ██   {q82}   ██   {q92}
	{q73}   ██   {q83}   ██   {q93}
	{q74}   ██   {q84}   ██   {q94}
	{q75}   ██   {q85}   ██   {q95}
	{q76}   ██   {q86}   ██   {q96}
	{q77}   ██   {q87}   ██   {q97}
	{q78}   ██   {q88}   ██   {q98}
                                 ██		               ██
"""
	print(q1)
def piece_char(i, c):
	if c == "X":
		return "✗"
	elif c == "O":
		return "○"
	else:
		return "" + str(i+1)
def prit_board(board):
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