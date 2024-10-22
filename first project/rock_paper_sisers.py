
import random
import time
type_speed = .02
def type_text(textt):
	for x in textt:
		print(x, end = "", flush = True)
		time.sleep(random.uniform(.01,type_speed))
	print("")
type_text("hi i am rocky")
while True:
	type_text("1 for rock")
	type_text("2 for scissors")
	type_text("3 for paper")
	com_move = str(random.randint(1,3))
	if com_move == "1":
		com_prin = "🪨"
	if com_move == "2":
		com_prin = "✂️"
	if com_move == "3":
		com_prin = "📄"
	players_move = input("what do you want:")
	print("☁️    3   ☁️")
	time.sleep(1)
	print("☁️    2   ☁️")
	time.sleep(1)
	print("☁️    1   ☁️")
	time.sleep(1)
	if players_move == "1":
		players_move = "🪨"
	elif players_move == "2":
		players_move = "✂️"
	elif players_move == "3":
		players_move = "📄"
	print(f"{com_prin}       {players_move}")
	if players_move == com_prin:
		type_text("tie")
	elif players_move == "🪨" and com_prin == "✂️" or players_move == "✂️" and com_prin == "📄" or players_move == "📄" and com_prin == "🪨":
		type_text("player win")
	else:
		type_text("com win")
	pap = input("play again(y/n): ")
	if pap == "n":
		type_text("ok")
		break
