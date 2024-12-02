def ascii_art(artify):
	run = str(artify).split("@")
	itera = 0
	out1=[]
	out2=[]
	out3=[]
	out4=[]
	out5=[]
	for i in run:
		for x in i:
			if x == "a":
				out1.append(" █████ ")
				out2.append("██   ██")
				out3.append("███████")
				out4.append("██   ██")
				out5.append("██   ██")
			elif x == "b":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██████ ")
				out4.append("██   ██")
				out5.append("██████ ")
			elif x == "c":
				out1.append(" ██████")
				out2.append("██     ")
				out3.append("██     ")
				out4.append("██     ")
				out5.append(" ██████")
			elif x == "d":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██   ██")
				out4.append("██   ██")
				out5.append("██████ ")
			elif x == "e":
				out1.append("███████")
				out2.append("██     ")
				out3.append("█████  ")
				out4.append("██     ")
				out5.append("███████")
			elif x == "f":
				out1.append("███████")
				out2.append("██     ")
				out3.append("█████  ")
				out4.append("██     ")
				out5.append("██     ")
			elif x == "g":
				out1.append(" ██████ ")
				out2.append("██      ")
				out3.append("██   ███")
				out4.append("██    ██")
				out5.append(" ██████ ")
			elif x == "h":
				out1.append("██   ██")
				out2.append("██   ██")
				out3.append("███████")
				out4.append("██   ██")
				out5.append("██   ██")
			elif x == "i":
				out1.append("██")
				out2.append("██")
				out3.append("██")
				out4.append("██")
				out5.append("██")
			elif x == "j":
				out1.append("     ██")
				out2.append("     ██")
				out3.append("     ██")
				out4.append("██   ██")
				out5.append(" █████ ")
			elif x == "k":
				out1.append("██   ██")
				out2.append("██  ██ ")
				out3.append("█████  ")
				out4.append("██  ██ ")
				out5.append("██   ██")
			elif x == "l":
				out1.append("██     ")
				out2.append("██     ")
				out3.append("██     ")
				out4.append("██     ")
				out5.append("███████")
			elif x == "m":
				out1.append("███    ███")
				out2.append("████  ████")
				out3.append("██ ████ ██")
				out4.append("██  ██  ██")
				out5.append("██      ██")
			elif x == "n":
				out1.append("███    ██")
				out2.append("████   ██")
				out3.append("██ ██  ██")
				out4.append("██  ██ ██")
				out5.append("██   ████")
			elif x == "o":
				out1.append(" ██████ ")
				out2.append("██    ██")
				out3.append("██    ██")
				out4.append("██    ██")
				out5.append(" ██████ ")
			elif x == "p":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██████ ")
				out4.append("██     ")
				out5.append("██     ")
			elif x == "q":
				out1.append(" ██████ ")
				out2.append("██    ██")
				out3.append("██ ▄▄ ██")
				out4.append(" ██████ ")
				out5.append("    ▀▀  ")
			elif x == "r":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██████ ")
				out4.append("██   ██")
				out5.append("██   ██")
			elif x == "s":
				out1.append("███████")
				out2.append("██     ")
				out3.append("███████")
				out4.append("     ██")
				out5.append("███████")
			elif x == "t":
				out1.append("████████")
				out2.append("   ██   ")
				out3.append("   ██   ")
				out4.append("   ██   ")
				out5.append("   ██   ")
			elif x == "u":
				out1.append("██    ██")
				out2.append("██    ██")
				out3.append("██    ██")
				out4.append("██    ██")
				out5.append(" ██████ ")
			elif x == "v":
				out1.append("██    ██")
				out2.append("██    ██")
				out3.append("██    ██")
				out4.append(" ██  ██ ")
				out5.append("  ████  ")
			elif x == "w":
				out1.append("██     ██")
				out2.append("██     ██")
				out3.append("██  █  ██")
				out4.append("██ ███ ██")
				out5.append(" ███ ███ ")
			elif x == "x":
				out1.append("██   ██")
				out2.append(" ██ ██ ")
				out3.append("  ███  ")
				out4.append(" ██ ██ ")
				out5.append("██   ██")
			elif x == "y":
				out1.append("██    ██")
				out2.append(" ██  ██ ")
				out3.append("  ████  ")
				out4.append("   ██   ")
				out5.append("   ██   ")
			elif x == "z":
				out1.append("███████")
				out2.append("   ███ ")
				out3.append("  ███  ")
				out4.append(" ███   ")
				out5.append("███████")
			elif x == "1":
				out1.append(" ██")
				out2.append("███")
				out3.append(" ██")
				out4.append(" ██")
				out5.append(" ██")
			elif x == "2":
				out1.append("██████ ")
				out2.append("     ██")
				out3.append(" █████ ")
				out4.append("██     ")
				out5.append("███████")
			elif x == "3":
				out1.append("██████ ")
				out2.append("     ██")
				out3.append(" █████ ")
				out4.append("     ██")
				out5.append("██████ ")
			elif x == "4":
				out1.append("██   ██")
				out2.append("██   ██")
				out3.append("███████")
				out4.append("     ██")
				out5.append("     ██")
			elif x == "5":
				out1.append("███████")
				out2.append("██     ")
				out3.append("███████")
				out4.append("     ██")
				out5.append("███████")
			elif x == "6":
				out1.append(" ██████ ")
				out2.append("██      ")
				out3.append("███████ ")
				out4.append("██    ██")
				out5.append(" ██████ ")
			elif x == "7":
				out1.append("███████")
				out2.append("     ██")
				out3.append("    ██ ")
				out4.append("   ██  ")
				out5.append("   ██  ")
			elif x == "8":
				out1.append(" █████ ")
				out2.append("██   ██")
				out3.append(" █████ ")
				out4.append("██   ██")
				out5.append(" █████ ")
			elif x == "9":
				out1.append(" █████ ")
				out2.append("██   ██")
				out3.append(" ██████")
				out4.append("     ██")
				out5.append(" █████ ")
			elif x == "0":
				out1.append(" ██████ ")
				out2.append("██  ████")
				out3.append("██ ██ ██")
				out4.append("████  ██")
				out5.append(" ██████ ")
			elif x == ".":
				out1.append("  ")
				out2.append("  ")
				out3.append("  ")
				out4.append("  ")
				out5.append("██")
			elif x == "!":
				out1.append("██")
				out2.append("██")
				out3.append("██")
				out4.append("  ")
				out5.append("██")
			elif x == "?":
				out1.append("██████ ")
				out2.append("     ██")
				out3.append("  ▄███ ")
				out4.append("  ▀▀   ")
				out5.append("  ██   ")
			elif x == ":":
				out1.append("  ")
				out2.append("██")
				out3.append("  ")
				out4.append("██")
				out5.append("  ")
			elif x == " ":
				out1.append("     ")
				out2.append("     ")
				out3.append("     ")
				out4.append("     ")
				out5.append("     ")
			out1.append("  ")
			out2.append("  ")
			out3.append("  ")
			out4.append("  ")
			out5.append("  ")
		for x in out1:
			print(x,end="",flush=True)
		print()
		for x in out2:
			print(x,end="",flush=True)
		print()
		for x in out3:
			print(x,end="",flush=True)
		print()
		for x in out4:
			print(x,end="",flush=True)
		print()
		for x in out5:
			print(x,end="",flush=True)
		print()
		print("\n\n")
		out1=[]
		out2=[]
		out3=[]
		out4=[]
		out5=[]