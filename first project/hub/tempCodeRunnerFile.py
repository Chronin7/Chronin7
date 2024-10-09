	print("hi i am lister")
	in_list = make_list(input("make a list name: "))
	action = int(input("""What would you like to do?
		1 to add item
		2 to remove item
		3 to go to a deferent list
		4 to make a new list
		5 to print a list
		6 to stop: """))

	if action == 1:
		add_to_list(f"what do you want to add to {in_list}: ")
	elif action == 2:
		remove_itom()
	elif action == 3:
		go_dif_list()
	elif action == 4:
		make_list(input("what is the name of the new list"))
	elif action == 5:
		print(print_lists())
	elif action == 6:
		quit
	else:
		print("sorry dident understand")