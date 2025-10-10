import random
def win(board):
	if board[0]==board[1]==board[2]!=None:
		return board[0]
	if board[3]==board[4]==board[5]!=None:
		return board[3]
	if board[6]==board[7]==board[8]!=None:
		return board[6]
	if board[0]==board[3]==board[6]!=None:
		return board[0]
	if board[1]==board[4]==board[7]!=None:
		return board[1]
	if board[2]==board[5]==board[8]!=None:
		return board[2]
	if board[0]==board[4]==board[8]!=None:
		return board[2]
	if board[2]==board[4]==board[6]!=None:
		return board[2]
	else:
		return False
def check_input(inp,valid):
    if inp not in valid:
        return True
    else:
        return False
iteration=0
def print_board(board):
    for i,x in enumerate(board):
        if i+1%3==0:
            print(x,end="""
""")
        else:
            print(f"{x}|",end="")
board=[None,None,None,None,None,None,None,None,None]
while input("do you want to play (y/n)?")=="y":
	board=[None,None,None,None,None,None,None,None,None]
	while not win(board):
		print_board(board)
		valid =[]
		for i,x in enumerate(board):
			if x==None:
				valid.append(i+1)
		move="-1"
		while check_input(move,valid):
			move=input("where do you want to go")
			valid =[]
			for i,x in enumerate(board):
				if x==None:
					valid.append(str(i+1))


