import random
playagenn = 0
num = random.randint (1,100)
y = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60}
print("Welcome the GUESS THE NUMBER! you have 20 atempts before you lose the game. good luck.")
guess = int(input("Guess a number 1-100: "))  
x = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
for x in range(20): 
  if guess < num :
    guess = int(input ("the number is larger: "))
  if guess > num :
    guess = int(input ("the number is smaller: "))
  if guess == num : 
    print ("you got it")
    playagenn = int(input ("play agen 1=yes 2=no: "))
    break
if  playagenn == 2:
  quit
elif playagenn == 1:
  playagenn = 0
  num = random.randint (1,100)

  print("Welcome the GUESS THE NUMBER! you have 20 atempts before you lose the game. good luck.")
  guess = int(input("Guess a number 1-100: "))  
  x = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
  for x in range(20): 
    if guess < num :
      guess = int(input ("the number is larger: "))
    if guess > num :
      guess = int(input ("the number is smaller: "))
    if guess == num : 
      print ("you got it")
    if x == 20:
      print("Game Over")
      quit