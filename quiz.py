print("this is a quiz")
score = 0
anser_one = 12
anser_two = 3
anser_three = 18
anser_for = 90
anser_five = 6
anser_six = 48
anser_seven = 1000
uno = 0
duo = 0
treo = 0
quodro = 0
sinko = 0
sixo = 0
sept = 0
uno = int(input("what is 6 X 2: "))
duo = int(input("what is 1 X 3: "))
treo = int(input("what is 3 X 6: "))
quodro = int(input("what is 9 X 10: "))
sinko = int(input("what is 3 X 2: "))
sixo = int(input("what is 6 X 8: "))
sept = int(input("what is 20 X 50: "))

if uno == anser_one:
	print(f"questen 1 you anserd {uno} it was corect")
	score = score+1
else:
	print(f"questen 1 you anserd {uno} is was incorect the anser was {anser_one}")
if duo == anser_two:
	print(f"questen 2 you anserd {duo} it was corect")
	score = score+1
else:
	print(f"questen 2 you anserd {duo} is was incorect the anser was {anser_two}")
if treo == anser_three:
	print(f"questen 3 you anserd {treo} it was corect")
	score = score+1
else:
	print(f"questen 3 you anserd {treo} is was incorect the anser was {anser_three}")
if quodro == anser_for:
	print(f"questen 4 you anserd {quodro} it was corect")
	score = score+1
else:
	print(f"questen 4 you anserd {quodro} is was incorect the anser was {anser_for}")
if sinko == anser_five:
	print(f"questen 5 you anserd {sinko} it was corect")
	score = score+1
else:
	print(f"questen 5 you anserd {sinko} is was incorect the anser was {anser_five}")
if sixo == anser_six:
	print(f"questen 6 you anserd {sixo} it was corect")
	score = score+1
else:
	print(f"questen 6 you anserd {sixo} is was incorect the anser was {anser_six}")
if sept == anser_seven:
	print(f"questen 7 you anserd {sept} it was corect")
	score = score+1
else:
	print(f"questen 7 you anserd {sept} is was incorect the anser was {anser_seven}")

print(f"your score is {score} out of 7")