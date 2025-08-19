clist = input("what is the name of your list: ")
thelist = []
while True:
	action = input("""what do you want to do
1 add item
2 remove item
3 to print and leave the list (note this also deletes it): """)
	if int(action) != 1 and int(action) != 2 and int(action) != 3:
		print("i am not impressed with your efforts to brake me")
	if int(action) == 1 and int(action) == 2 and int(action) == 3:	
		if action == 1:
			inpuy = input("what do you want to add: ")
			thelist.append(inpuy)
		elif action == 2:
			print()
			print(f"          {clist}          ")
			print("___________________________")
			iteration = 1
			for x in thelist:
				print(f"| ⦿ {iteration}: {x}")
				iteration += 1
			print("___________________________")
			while True:
				remove = int(input("what do you want to remove: "))
				if remove > len(thelist):
					print(f"you dont have a item at {remove}")
				elif remove < 1:
					print("i am not impressed with your efforts to brake me")
				else:
					del thelist[remove-1]
					break
		elif action == 3:
			print()
			print(f"          {clist}          ")
			print("___________________________")
			iteration = 1
			for x in thelist:
				print(f"| ⦿ {iteration}: {x}")
				iteration += 1
			print("___________________________")
			clist = input("what is the new name for the new list: ")
			thelist = []
			
