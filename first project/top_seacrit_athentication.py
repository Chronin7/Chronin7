username = input("what is your username: ")
admin = ["liam","ms larose", "jonas","bob","tom","tim","mat","joe"]
user = ["addy","maddy","daddy","mom","peat","chad","shakespear","alex"]
if username not in admin:
	if username not in user:
		print("no acount found")
	else:
		print("you do not have high enugh clerace")
else:
	print("in")
