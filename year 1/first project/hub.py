from dataclasses import dataclass
from copy import copy, deepcopy
import time, random, winsound
from typing import List, Dict, Tuple
confetty_animation=["""
 




     :  """
,"""




     :
     :  """
,"""



     :
     :
     : """
,"""

        
    .:.   
    ':' 
     :
       '"""
,"""
     :  
   '.:.' 
   .':'.   
     :   
       '"""
,"""

   . : .
 '.  :  .'
.  '.:.'  .
.  .':'.  .
 .'  :  '.
   ' : '"""
,"""
   . : .
 '.  :  .'
.  '   '  .
.  .   .  .
 .'  :  '.
   ' : '"""
,"""
   . : .
 '.  :  .'
.         .
.         .
 .'  :  '.
   ' : '"""
,"""
   . : .
 '       '
.         .
.         .
 .       .
   ' : '"""
,"""






"""]
age=0
dndname=""
player_name=""
race=""
backround=""
alingment=""
classs="" 
xp=0
level=0
strengthmod=0
strength=0
insperation=0
profishansy=0
ac=0
initative=0
hp=0
chp=0
speed=0
dexmod=0
dex=0
con=0
conmod=0
wis=0
wismod=0
cha=0
chamod=0
intelegance=0
intelegancemod=0
acrobaticsprof=""
eyes=""
temphp=0
hitdice=""
acrobatics=0
animalprof=""
animal=0
arcanaprof=""
arcana=0
athleticsprof=""
athletics=0
weponl1=""
weponl2=""
weponl3=""
weponl4=""
weponl5=""
weponl6=""
weponl7=""
weponl8=""
weponl9=""
weponl10=""
weponl11=""
weponl12=""
weponl13=""
weponl14=""
deseptionprof=""
deseption=0
historyprof=""
history=0
insightprof=""
insight=0
intimidationprof=""
intimidation=0
investigationprof=""
investigation=0
medesenprof=""
medicine=0
nature=0
natureprof=""
preseptionprof=""
preseption=0
preformance=0
preformanceprof=""
perswasonprof=""
perswason=0
relegionprof=""
relegion=0
slightofhandprof=""
slightofhand=0
stelthprof=""
stelth=0
servivalprof=""
servival=0
paswis=0
profl1=""
profl2=""
profl3=""
profl4=""
profl5=""
profl6=""
gender=""
hight=""
weight=""
skin=""
hair=""
belt_pouch=""
clohting=""
wepons_aromor=""
backpack=""
straped_to_sayd_backpack=""
camtris=""
lv1=""
lv2=""
lv3=""
lv4=""
lv5=""
lv6=""
lv7=""
lv8=""
lv9=""
lv1spells=""
lv2spells=""
lv3spells=""
lv4spells=""
lv5spells=""
lv6spells=""
lv7spells=""
lv8spells=""
lv9spells=""
racetrate=""
subrace=""
subracetrate=""
backroundtrate=""
classtrate=""
lv1trate=""
lv2trate=""
lv3trate=""
lv4trate=""
lv5trate=""
lv6trate=""
lv7trate=""
lv8trate=""
lv9trate=""
personalitytrate=""
ideals=""
bonds=""
flaws=""
backstory=""
playedAmount =0
turn = ""
runhub = True
debuging = 1
invertedP = ""
iterationP = 1
runnerP = ""
var = 0
hubo = 0
operation = 0
easterEggCount = 5
maxGuessCount = 10
minGuess = 1
maxGuess = 100
playCount = 0
playAgain = True
debuging = False
typing = True
type_speed = .01
player_score = 0
com_score = 0
board = [None] * 9

@dataclass
class Monster:
	name:str
	health:str
	damage:str
	lootLevel:int = 1

@dataclass
class Item:
	name:str
	health:int = 0
	damagebuff:float = 0
	predamage:int = 0
	luck:int = 0
	life:int = None
	type:str = "consumable"

@dataclass
class Moves:
	north:str = None
	south:str = None
	east:str = None
	west:str = None
	def selectMove(self):
		return selectOption([
			("North", self.north),
			("South", self.south),
			("East", self.east),
			("West", self.west)
		])

@dataclass
class Location:
	description:str
	moves:Moves
	itemRarity:int = 1
	hasLoot:bool = True
	monster:Monster = None

#best
goodLoot = [
	Item("Holy Hand Grenade: instakill", damagebuff=100, type="consumable"),
	Item("Holy Hand Grenade: instakill", damagebuff=100, type="consumable"),
	Item("Holy Hand Grenade: instakill", damagebuff=100, type="consumable"),
	Item("RPG: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("RPG: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("RPG: once per battle 20 damage at beginning", predamage=20, type="weapon"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Health + 50 Potion", health=50, type="consumable"),
	Item("Sten MK II: tends to misfire sometimes has bullets bounce off of target +20% damage", damagebuff=.20, type="weapon"),
	Item("Apache Revolver: you can use it like a gun (terrible aim) a knife (way too flexible) or an iron fist (the only safe way to use it) +30% damage", damagebuff=.30, type="weapon"),
	Item("Pickled Leprechaun Head: +1 luck for 7 turns", life=7, type="timed"),
	Item("Luck Potion: +1 luck for 10 turns", life=10, type="timed")
]
#worst
norm = [
	Item("Nuke Kill All", health=-100000000, type="consumable"),
	Item("Stick +5% damage", damagebuff=.5, type="weapon"),
	Item("Health +10 potion", health=10, type="consumable"),
	Item('Deodorant', type='consumable'),
	Item(name='luck charm +1 luck for a turn', life=1, type="timed"),
	Item(name='luck potion +1 luck for 2 turns', life=2, type="timed")
]
#meh
rearer = [
	Item('A Peace of a Lemon', health=20,  type='consumable'),
	Item('Sword + 10% damage', damagebuff=.1, type='weapon'),#damageBuff ?
	Item('Health + 20 potion', health=20, type='consumable'),
	Item('Slingshot +5% damage', damagebuff=.05, type='weapon'),
	Item('A 15 foot long pole', health=2, type='consumable'),
	Item('clover +1 luck for 3 turns', luck=1, type='timed'),
	Item('luck potion +1 luck for 4 turns', luck=1, type='timed')]


worldTemplate = {
	"start": Location(description="French castle (how did you get in here anyway hon hon hon)", itemRarity=3, moves=Moves(east="field4")),
	"field1": Location(description="You are in a field of grass",itemRarity=1,moves=Moves(north="foothills1")),
	"field2": Location(description="You are in a field of goat heads", itemRarity=1,moves=Moves(west="field3",east="foothills1")),
	"field3": Location(description="You are in a field of mud",itemRarity=2,moves=Moves(north="forest",east="field2")),
	"field4": Location(description="You are in a field of molten rice",itemRarity=1, moves=Moves(south="forest")),
	"field5": Location(description="You are in a field of grass",itemRarity=2,moves=Moves(west="foothills1",east="field6"), monster=Monster(name="flying snake", health=50, damage=10, lootLevel=3)),
	"field6": Location(description="You are in a field of coconuts",itemRarity=2,moves=Moves(north="foothills2", west="field5")),
	"foothills1": Location(description="you are in a foothills biome",itemRarity=3,moves=Moves(north="mountain1",south="field1",west="field2",east="field5")),
	"foothills2": Location(description="you are in a foothills biome", itemRarity=2,moves=Moves(east="foothills3", south="field6")),
	"foothills3": Location(description="you are in a foothills biome", itemRarity=2,moves=Moves(east="swamp1",west="foothills2")),
	"forest": Location(description="you in big fat forest", itemRarity=3,moves=Moves(north="field4",south="field3"), monster=Monster(name="killer bunny", health=15, damage=10, lootLevel=3)),
	"swamp1": Location(description="yucky swamp you in hmmmm?", itemRarity=3,moves=Moves(north="swamp3",west="foothills3")),
	"swamp2": Location(description="in yucky swamp am i hmmmm?", itemRarity=2,moves=Moves(west="mountain2", south="swamp3")),
	"swamp3": Location(description="swamp yucky in both are we hmmmm?", itemRarity=3,moves=Moves(north="swamp2",south="swamp1"), monster=Monster(name="shreck", health=300, damage=2, lootLevel=3)),
	"mountain1": Location(description="you are in a mountain", itemRarity=3,moves=Moves(north="BOD", south="foothills1")),
	"mountain2": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="mountain3", east="swamp2")),
	"mountain3": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="mountain4", east="mountain2"), monster=Monster(name="dragon", health=100, damage=50, lootLevel=3)),	
	"mountain4": Location(description="you are in a mountain", itemRarity=2,moves=Moves(west="mountain5", east="mountain3"), monster=Monster(name="robot", health=50, damage=10, lootLevel=3)),
	"mountain5": Location(description="you are in a mountain", itemRarity=3,moves=Moves(west="glitchedPlains1", east="mountain4"), monster=Monster(name="robot", health=200, damage=20, lootLevel=3)),
	"BOD": Location(description="BODY", hasLoot=False, moves=Moves(north="moun1tain5")),
	"glitchedPlains1": Location(description="You have entered the glitched plains", itemRarity=3, moves=Moves(north="glitchedPlains2", east="mountain5"), monster=Monster(name="robot", health=250, damage=50, lootLevel=3)),
	"glitchedPlains2": Location(description="You have entered the glitched plains", itemRarity=2, moves=Moves(west="glitchedCitadel", south="glitchedPlains1"), monster=Monster(name="robot", health=300, damage=50, lootLevel=3)),
	"glitchedCitadel": Location(description="You have entered the glitched citadel. This is where the boss is good luck from the game itsleff", hasLoot=False, moves=Moves(west="holyGrail", east="glitchedPlains2"), monster=Monster(name="The Programer", health=1000, damage=50)),
	"holyGrail": Location(description="grail",hasLoot=False, moves=Moves())
}

world: Dict[str,Location]
location: Location
inventory: List[Item]
health: int
damage: int
color: str
name: str
quest = "To seek the Holy Grail"
playedAmount = 0
damagebuff=0
def betinput(questen):
	type_text(questen)
	the_input_to_end_all_inputs=input()
	winsound.MessageBeep()
	return the_input_to_end_all_inputs
def display_intro():
	type_text("Welcome to the Mystic Forest Adventure! I am The DM")
	type_text("You find yourself at the edge of a dark, mysterious forest.")
	type_text("Your goal is to find the hidden treasure and escape safely.")
def make_choice(options):
	for i,option in enumerate(options,1):
		type_text(f"{i}. {option}")
	while True:
		try:
			choice=int(betinput("Enter your choice: "))
			if 1<=choice<=len(options):
				return choice
			else:
				type_text("Invalid choice. Try again.")
		except ValueError:
			type_text("Please enter a number.")
def explore_forest():
	type_text("You venture deeper into the forest...")
	events=["You encounter a friendly woodland creature.","You find a shimmering portal.","You discover an ancient ruins.","You come across a bubbling stream."]
	type_text(random.choice(events))
def find_treasure():
	type_text("Congratulations! You've found the hidden treasure!")
	type_text("It's a chest filled with gold coins and magical artifacts.")
def face_challenge():
	type_text("Oh no! You've encountered a challenge!")
	challenges=["A giant spider blocks your path.","A riddle-speaking owl demands an answer.","A magical barrier requires a spell to pass."]
	type_text(random.choice(challenges))
	if random.random()<0.5:
		type_text("You successfully overcome the challenge!")
		return True
	else:
		type_text("You fail to overcome the challenge.")
		return False
def play_gamre():
	display_intro()
	treasure_found=False
	while not treasure_found:
		type_text("\nWhat would you like to do?")
		choice=make_choice(["Explore the forest","Search for treasure","Face a challenge","Exit the forest"])
		if choice==1:
			explore_forest()
		elif choice==2:
			if random.random()<0.3:
				find_treasure()
				treasure_found=True
			else:
				type_text("No treasure here. Keep searching!")
		elif type_text==3:
			if face_challenge():
				if random.random()<0.4:
					find_treasure()
					treasure_found=True
		elif choice==4:
			type_text("You decide to leave the forest. Game over!")
			return
	if treasure_found:
		type_text("Congratulations! You've won the game!")
def dwane_the_rock():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	player_score = 0
	com_score = 0
	type_text("The Rock wlcomes you to play Rock Paper Scissors")
	while True:
		type_text("1 for rock")
		type_text("2 for scissors")
		type_text("3 for paper")
		type_text("4 to quit")
		com_move = str(random.randint(1,3))
		if com_move == "1":
			com_prin = "🪨"
		if com_move == "2":
			com_prin = "✂️"
		if com_move == "3":
			com_prin = "📄"
		while True:
			players_move = betinput("The Rock asks what do you want:")
			players_move = check_int(players_move)
			if check_int(players_move) != "":
				break
			else:
				type_text("The Rock dosn't think that that is a valid input")
		if players_move == 1:
			players_move = "🪨"
		elif players_move == 2:
			players_move = "✂️"
		elif players_move == 3:
			players_move = "📄"
		elif players_move ==4:
			type_text("The Rock will send you back to the hub.")
			return
		print(f"The Rock: {com_prin} Player: {players_move}")

		if players_move == com_prin:
			type_text("The Rock is disaponted")
		elif players_move == "🪨" and com_prin == "✂️" or players_move == "✂️" and com_prin == "📄" or players_move == "📄" and com_prin == "🪨":
			type_text("how did you beat The Rock? The Rock will crush you.")
			player_score +=1
		else:
			type_text("HAHAHAHA The Rock wins once again")
			com_score += 1
		print(f"The Rock: {com_score} player: {player_score}")
def check_input(input,valid_inputs):
	if input  in  valid_inputs:
		return input
	return ""
def check_int(input):
	try:
		return int(input)
	except ValueError:
		type_text("please enter a number")
	return ""
def check_float(input):
	try:
		return float(input)
	except ValueError:
		type_text("not a valid input")
		return""
def type_text(textt):
	if typing == True:
		for x in textt:
			print(x, end = "", flush = True)
			time.sleep(random.uniform(.01,type_speed))
		print("")
	else:
		print(textt,flush=True)
def anagram():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	type_text("Hi i am Anny")
	while True:
		anagramt = []
		outputt = ""
		doitt = "12345"
		wordt = betinput("what is the word that you want into anagram or type stop to stop: ")
		if wordt == "stop":
			type_text("sending you back to Hubby")
			break
		if wordt == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			randt = len(wordt)
			for y in doitt:
				outputt = ""
				anagramt = []
				for x in wordt:
					anagramt.insert(random.randint(1,randt),x)
				for i in anagramt:
					outputt = outputt + i
				print (outputt)
def calculator():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	operation = 0
	a = "n/a"
	b = "n/a"
	type_text("Hi this is Calcu. What do you want me to calculate today")
	operation = 0
	while True:
		type_text("0 to stop")
		type_text("1 for devision")
		type_text("2 for multiplication")
		type_text("3 for subtraction")
		type_text("4 for addition")
		type_text("5 for modulo")
		type_text("6 for factoring")
		operation = betinput("what do you want: ")
		if operation == "1" :
			while True:
				a = check_float(betinput("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the second number:"))
				if b != "" and b != 0:
					break
			if b == 0 :
				type_text("division by 0 error")
			else:
				print(a,"/",b,"=",a/b)
		elif operation == "2" :
			while True:
				a = check_float(betinput("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the second number:"))
				if b != "":
					break
			print(a,"X",b,"=",a*b)
		elif operation == "3" :
			while True:
				a = check_float(betinput("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the second number:"))
				if b != "":
					break
			print(a,"-",b,"=",a-b)
		elif operation == "4" :
			while True:
				a = check_float(betinput("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the second number:"))
				if b != "":
					break
			print(a,"+",b,"=",a+b)
		elif operation == "5" :
			while True:
				a = check_float(betinput("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the second number:"))
				if b != "":
					break
			print(a,"%",b,"=",a%b)
		elif operation == "6" :
			while True:
				a = check_float(betinput("what is the first number:"))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the second number:"))
				if b != "":
					break
			print(a,"^",b,"=",a**b)
		elif operation == "0" :
				type_text("ok sending you back to the hub")
				return
		else:
			type_text("Sorry I didn't understand")
def game():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	easterEggCount = 250
	maxGuessCount = 20
	minGuess = 1
	maxGuess = 100
	playCount = 0
	playAgain = True
	while playAgain == True:
			if playCount == easterEggCount:
					type_text("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME! ##connection terminated by: Guessy##")
					quit()
			playCount += 1
			num = random.randint (minGuess,maxGuess)
			type_text(f'Welcome the GUESS THE NUMBER! I am your host Guessy. You have {maxGuessCount} attempts before you lose the game. good luck.')
			while True:
				guess = betinput(f'Guess a number {minGuess}-{maxGuess}: ')
				if check_int(guess):
					guess = int(guess)
					break
			for x in range(maxGuessCount): 
				if guess < num:
					while True:
						guess = check_int(betinput("the number is larger: "))
						if guess != "":
							break
				if guess > num:
					while True:
						guess = check_int(betinput("the number is smaller: "))
						if guess != "":
							break
				if guess == num: 
					type_text ("you got it")
					playgain = str(betinput("do you want to play again? (y/n): "))
					if playgain != "y":
						playAgain = False
						type_text("ok sending you back to the hub")
						time.sleep(1)
						return
					else:
						type_text("ok")
def palindrome():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	invertedP = ""
	doagennP = True
	iterationP = 1
	runnerP = "placeholder"
	while doagennP == True:
		invertedP = ""
		iterationP = 1
		nameP = str(betinput("hi i am pally please input a word or sentence and i will tell you if it's a palindrome or not: ")).lower()
		if len(nameP) == 1:
				type_text(nameP,"is a palindrome")
				invertedP = ""
				runnerP = str(betinput("do you want me to detect another palindrome for you? (y/n): "))
				if runnerP == "n":
						type_text("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False
						return
		else:
				loopP = (len(nameP))
				lopnarP =(len(nameP))
				for lopnarP in range(lopnarP):
						invertedP += nameP[loopP-iterationP]
						iterationP += 1
				if invertedP == nameP:
						print(nameP,"is a palindrome")
				else:
						print(nameP,"is not a palindrome")
				runnerP = str(betinput("do you want me to detect another palindrome for you? (y/n): ")).lower()
				if runnerP == "n":
						type_text("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False
						return
def area():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		e = 1
		type_text("1 for rectangle")
		type_text("2 for square")
		type_text("3 for triangle")
		type_text("4 for circle")
		type_text("5 for trapezoid")
		shape = betinput("what do you want or type stop to stop: ")
		if shape == "1":
			#square/rectangle
			type_text("ok input the numbers that you want")
			while True:
				a = check_float(betinput("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the length (only numbers please): "))
				if b != "":
					break
			type_text(f"when the hight is {a} and the length is {b} the area is {a*b}.")
			e = 0
		if shape == "4":
			#circle
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(betinput("what is the radius (only numbers please): "))
				if a != "":
					break
			type_text(f"when the radius is {a} the area is {3.141592653589793238462643383279*a^2}")
		if shape == "3":
			#triangle
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(betinput("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the length (only numbers please): "))
				if b != "":
					break
			type_text(f"when the hight is {a} and the length is {b} the area is {(a*b)*(1/2)}.")
		if shape == "5":
			#trapezoid
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = check_float(betinput("what is the hight (only numbers please): "))
				if a != "":
					break
			while True:
				b = check_float(betinput("what is the top length (only numbers please): "))
				if b != "":
					break
			while True:
				c = check_float(betinput("what is the bottom length (only numbers please): "))
				if c != "":
					break
			type_text(f"when the hight is {a} and the bottom is {b} and the top is {c} the area is {((b+c)/2)*a}.")
		if shape == "2":
			type_text("ok input the numbers that you want")
			e = 0
			while True:
				a = betinput("what is the length of one of the sides (only numbers please): ")
				if a != "":
					break
			type_text(f"when the the length of one of the sides is {a} the area is {a*2}.")
			e = 0
		if shape == "6":
			type_text("sorry coming soon")
			e = 0
		if shape == "7":
			type_text("sorry coming soon")
			e = 0
		if shape == "8":
			type_text("sorry coming soon")
			e = 0
		if shape == "9":
			type_text("sorry coming soon")
			e = 0
		if shape == "10":
			type_text("sorry coming soon")
			e = 0
		if shape == "11":
			type_text("sorry coming soon")
			e = 0
		if shape == "12":
			type_text("sorry coming soon")
			e = 0
		if shape == "13":
			type_text("sorry coming soon")
			e = 0
		if shape == "14":
			type_text("sorry coming soon")
			e = 0
		if shape == "15":
			type_text("sorry coming soon")
			e = 0
		if shape == "16":
			type_text("sorry coming soon")
			e = 0
		if shape == "17":
			type_text("sorry coming soon")
			e = 0
		if shape == "18":
			type_text("sorry coming soon")
			e = 0
		if shape == "19":
			type_text("sorry coming soon")
			e = 0
		if shape == "20":
			type_text("sorry coming soon")
			e = 0
		if shape == "stop":
			type_text("ok sending you back to Hubby")
			break
		else:
			type_text("sorry coming soon")
			e = 0
		if e == 1:
			type_text("sorry i didn't understand")
			e = 1
def avrage():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		runsq = 1
		list_o_numsq = []
		percentageq = 0
		while True:
			classesq = betinput("I am AV the Avenger. How many things do you want to average or type stop to stop: ")
			if classesq == "stop":
				type_text("ok sending you back to Hubby")
				return
			if classesq != "":
				classesq = check_int(classesq)
				if classesq != "":
					break
		for x in range(classesq):
			while True:
				one_at_a_timeq = check_int(betinput(f"what is the percentage of # {runsq} (only numbers please): "))
				if one_at_a_timeq != "":
					break
			percentageq += one_at_a_timeq
			list_o_numsq.append(one_at_a_timeq)
			runsq += 1
		type_text(f"you entered {list_o_numsq} they have an average of {percentageq/classesq}")
def code():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	betinput_o_code = betinput("shhhh. this is a secret i am liam what is the code(only numbers please): ")
	break_it = 1
	binary = ""
	checkw = 0
	for i in betinput_o_code:
		binary = binary + str(bin(ord(i)))
	if binary == "0b11011100b11001010b11101100b11001010b11100100b1000000b11001110b11101010b11011100b11011100b11000010b1000000b11001110b11010010b11101100b11001010b1000000b11110010b11011110b11101010b1000000b11101010b11100000b100001":
		while True:
			code_decode = int(betinput("would you like to code (1) or decode (2) or stop (3): "))
			list_o_coded = []
			output =""
			decoded = ""
			iterationw = 1
			loops_o_codeing = 0
			list_o_decoding = []
			if code_decode == 1:
				code = betinput("what is the uncoded word: ")
				seed = int(betinput("what is the decoding seed (whole numbers please): "))
				for x in code:
					list_o_coded.append(((ord(x))))
				for y in list_o_coded:
					if loops_o_codeing == 0:
						output = str(int(y)+seed)
					else:
						output = output +","+ str(int(y)+seed)
					loops_o_codeing += 1
				type_text(output)
			if code_decode == 2:
				coded_decoder = str(betinput("what is the coded thing: "))
				seed_o_decodeing = int(betinput("what is the seed: "))
				list_o_decoding = (coded_decoder.split(","))
				for z in list_o_decoding:
					var = str(chr(int(z)-seed_o_decodeing))
					decoded = decoded + var
				type_text(decoded)
			if code_decode == 3:
				input_o_code = ""
				break_it = 0
				break
	if break_it == 1:
		print(f"""Traceback (most recent call last):
  File "c:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7{chr(92)}first project{chr(92)}hub.py", line 1315, in <module>
    hub()
  File "c:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7{chr(92)}first project{chr(92)}hub.py", line 1299, in hub
    code()
  File "c:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7{chr(92)}first project{chr(92)}hub.py", line 506, in code
    isinstance(input_o_code)
TypeError: isinstance expected 2 arguments, got 1""")
		print(f"PS C:{chr(92)}Users{chr(92)}liam.perl{chr(92)}Documents{chr(92)}Chronin7>",end="")
		time.sleep(10)
		print()
		type_text("gotem")
		quit()
	else:
		type_text ("ok sending you back to hubby")
def translate_word(input_word):
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	split = {}
	deleted = ""
	not_a_string = ""
	output = ""
	decoded = ""
	j = 0
	i = 0
	x = 0
	iteration = 1
	consonants = []
	if len(input_word) < 3:
		return(input_word)
	else:
		for x in input_word:
			if x == "a":
				deleted = "a"
				split = second_half(iteration, input_word)
				break
			if x == "e":
				deleted = "e"
				split = second_half(iteration, input_word)
				break
			if x == "i":
				deleted = "i"
				split = second_half(iteration, input_word)
				break
			if x == "o":
				deleted = "o"
				split = second_half(iteration, input_word)
				break
			if x == "u":
				deleted = "u"
				split = second_half(iteration, input_word)
				break
			if x == "y" and iteration > 1:
				deleted = "y"
				split = second_half(iteration, input_word)
				break
			iteration += 1
			consonants.append(x)
	for i in split:
		not_a_string = not_a_string + i
	for j in consonants:
		decoded = decoded + j
	output =deleted + not_a_string + decoded + "ay"
	return(output)
def second_half(num,word):
	return (word[num:])
def last_bit():
	while True:
		iteration = 1
		out = ""
		imput_o_word = betinput("what do you want to translate or type stop to go back to Hubby: ")
		if imput_o_word == "stop":
			type_text("Ok sending you back to hubby. Oink")
			time.sleep(1)
			break
		output = []
		intt = imput_o_word.split(" ")
		for i in intt:
			output.append(translate_word(i))
		for x in output:
			if iteration ==1:
				out = out + x
			else:
				out = out +" "+ x
			iteration += 1
		type_text(out)
def pig():
	type_text("Hi i am Pig")
	last_bit()
def change_settings():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		type_text("ok")
		type_text("0 to go back to the terminal")
		type_text("1 to toggle typing")
		type_text("2 to toggle debugging")
		type_text("3 to change typing speed")
		while True:
			imper = check_int(betinput("what do you want"))
			if imper != "":
				
				break
		if imper == 0:
			type_text("ok back to the terminal")
			break
		elif imper == 1:
			if typing == True:
				typing = False
			else:
				typing = True
		elif imper == 2:
			if debuging == True:
				debuging = False
			else:
				debuging = True
		elif imper == 3:
			while True:
				sett = check_float(betinput("what do you want to change the typing speed to: "))
				if sett != "":
					break
def farinhight451():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	type_text("hi this is Kelvin")
	while True:
		yes = betinput("would you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			while True:
				tempofcelsius = check_int(betinput("what is the temp in celsius: "))
				if tempofcelsius != "":
					break
			type_text("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = betinput("would you like celsius to fahrenheit (y/n): ")
			if no == "y":
				while True:
					tempforfahrenheit = check_int(betinput("what is the temp in fahrenheit: "))
					if tempforfahrenheit != "":
						break
				type_text("the temp for celsius when fahrenheit is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			elif no == "n":				
				type_text("Ok sending you back to Hubby.")
				break
			else:
				type_text("sorry i didn't understand")
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
def meet_o_code():
	global board
	for x in range(9):
		board[x]=None
	while True:
		board = choose_move(board, "X")
		if check_win(board) != None:
			print_board(board)
			if check_win(board) == "X":
				print("""
███         ███        ███                        ███   ██████████████████   ███            ███      █████████
  ███     ███          ███                        ███           ███          ██████         ███    ███
    ███ ███             ███                      ███            ███          ███   ███      ███    ███
     █████               ███                    ███             ███          ███      ███   ███      █████████
     █████                ███      ██████      ███              ███          ███         ██████              ███
    ███ ███                ███    ███  ███    ███               ███          ███            ███              ███
  ███     ███               ███  ███    ███  ███                ███          ███            ███              ███
███         ███              ██████      ██████         ██████████████████   ███            ███      █████████
	""")
			elif check_win(board) == "O":
				print("""
   █████████           ███                        ███   ██████████████████   ███            ███      █████████
 ███       ███         ███                        ███           ███          ██████         ███    ███
███         ███         ███                      ███            ███          ███   ███      ███    ███
███         ███          ███                    ███             ███          ███      ███   ███      █████████
███         ███           ███      ██████      ███              ███          ███         ██████              ███
███         ███            ███    ███  ███    ███               ███          ███            ███              ███
 ███       ███              ███  ███    ███  ███                ███          ███            ███              ███
   █████████                 ██████      ██████         ██████████████████   ███            ███      █████████
			""")
			break
		while True:
			print_board(board)
			if check_win(board) != None:
				if check_win(board) == "X":
					print("""
███         ███        ███                        ███   ██████████████████   ███            ███      █████████
  ███     ███          ███                        ███           ███          ██████         ███    ███
    ███ ███             ███                      ███            ███          ███   ███      ███    ███
     █████               ███                    ███             ███          ███      ███   ███      █████████
     █████                ███      ██████      ███              ███          ███         ██████              ███
    ███ ███                ███    ███  ███    ███               ███          ███            ███              ███
  ███     ███               ███  ███    ███  ███                ███          ███            ███              ███
███         ███              ██████      ██████         ██████████████████   ███            ███      █████████
	""")
				elif check_win(board) == "O":
					print("""
   █████████           ███                        ███   ██████████████████   ███            ███      █████████
 ███       ███         ███                        ███           ███          ██████         ███    ███
███         ███         ███                      ███            ███          ███   ███      ███    ███
███         ███          ███                    ███             ███          ███      ███   ███      █████████
███         ███           ███      ██████      ███              ███          ███         ██████              ███
███         ███            ███    ███  ███    ███               ███          ███            ███              ███
 ███       ███              ███  ███    ███  ███                ███          ███            ███              ███
   █████████                 ██████      ██████         ██████████████████   ███            ███      █████████
				""")
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
			while True:
				try:
					play_go = int(betinput("where do you want to go: "))
					break
				except:
					print("nope")
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
		if check_win(board) == None:
			print_board(board)
		else:
			if check_win(board) == "X":
				print("""
███         ███        ███                        ███   ██████████████████   ███            ███      █████████
  ███     ███          ███                        ███           ███          ██████         ███    ███
    ███ ███             ███                      ███            ███          ███   ███      ███    ███
     █████               ███                    ███             ███          ███      ███   ███      █████████
     █████                ███      ██████      ███              ███          ███         ██████              ███
    ███ ███                ███    ███  ███    ███               ███          ███            ███              ███
  ███     ███               ███  ███    ███  ███                ███          ███            ███              ███
███         ███              ██████      ██████         ██████████████████   ███            ███      █████████
	""")
			elif check_win(board) == "O":
				print("""
   █████████           ███                        ███   ██████████████████   ███            ███      █████████
 ███       ███         ███                        ███           ███          ██████         ███    ███
███         ███         ███                      ███            ███          ███   ███      ███    ███
███         ███          ███                    ███             ███          ███      ███   ███      █████████
███         ███           ███      ██████      ███              ███          ███         ██████              ███
███         ███            ███    ███  ███    ███               ███          ███            ███              ███
 ███       ███              ███  ███    ███  ███                ███          ███            ███              ███
   █████████                 ██████      ██████         ██████████████████   ███            ███      █████████
	""")
			break

def ask_questen(type_of_word):
	type_text("""
adverb: a word that describes and ends in -ly ex: loudly, angrily

adjective: describing word ex: big, smelly

noun: a person place or thing ex: france, hand sanitizer

plural noun: a noun but plural ex: printers, students

verb: an action ex: drive, print

silly word: something that sound funny ex: plorp, sizzle
""")
	return betinput(f"give me a {type_of_word.lower()}: ")
def madlib():
	libnum=1
	while libnum!=0:
		libnum=betinput("""hi i am libby, i have 13 madlibs 0 to quit, which one would you like to do (0-13): """)
		if libnum=="1": 
			print(f"""All children have {ask_questen("ADJECTIVE")} memories of the books their
	mothers and {ask_questen("pLURAL NOUN")} read to them. Here are some of the all-time {ask_questen("ADJECTIVE")} favorites:
	• The Giving {ask_questen("NOUN")} is a touching story about a friendship
	between a/an {ask_questen("NOUN")} and a tree. Throughout the boy's
	life, the {ask_questen("NOUN")} gives and gives. Kids between the ages of
	{ask_questen("NUMBER")} and {ask_questen("NUMBER")} love this story.
	• Goodnight Moon is a/an {ask_questen("ADJECTIVE")} book that captures
	a child's nightly ritual of saying good night to everything in his
	{ask_questen("NOUN")}. It's great for {ask_questen("pLURAL NOUN")} ages two through six.
	• Written in rhyme, Green Eggs and {ask_questen("TYPE OF FOOD")} made Dr. Seuss
	one of the best-loved children's {ask_questen("pLURAL NOUN")} of all time. While
	many {ask_questen("pLURAL NOUN")} have a moral or a/an {ask_questen("NOUN")}, the lesson
	in this classic is: If you've never tried something, you can't say you
	don't like it. A perfect read for all {ask_questen("ADJECTIVE")} kindergartners""")
		elif libnum=="2":
			print(f"""One of the things most {ask_questen("adJeCtIVe")} sports fans look
	forward to at American baseball {ask_questen("PLUraL NoUN")} is eating a/an
	{ask_questen("adJeCtIVe")} hot dog. There is nothing more traditional
	than watching a/an {ask_questen("adJeCtIVe")} ball game and eating a hot
	{ask_questen("NoUN")} drenched in mustard, relish, and {ask_questen("PLUraL NoUN")}.
	Some {ask_questen("NoUN")}-parks even have their own {ask_questen("adJeCtIVe")}
	specialties, such as the Dodger {ask_questen("NoUN")} in Los Angeles.
	(It's an oversize steamed or grilled {ask_questen("NoUN")}.)
	Hot {ask_questen("PLUraL NoUN")} were created at the end of the nineteenth
	century when a sausage-maker saw his {ask_questen("adJeCtIVe")} customers
	wearing gloves on their {ask_questen("Part of the Body (PLUraL)")} because the
	steaming sausages were too {ask_questen("adJeCtIVe")} to handle. He put
	them in a/an {ask_questen("adJeCtIVe")} roll, and that was the beginning
	of the {ask_questen("adJeCtIVe")} dog in a bun. The rest, as they say, is
	{ask_questen("NoUN")}!""")
		elif libnum=="3":
			print(f"""Thanks to social networking {ask_questen("PLUraL NoUN")} like My-{ask_questen("NoUN")}
	and {ask_questen("Part of the Body")}-book, everyone now has hundreds of
	{ask_questen("adJeCtIVe")} friends. But most people really have only one
	best {ask_questen("NoUN")}. A BFF is someone you tell your deepest,
	most {ask_questen("adJeCtIVe")} secrets to, knowing they won't tell a single
	{ask_questen("NoUN")}. You and your best {ask_questen("NoUN")} can pass
	{ask_questen("PLUraL NoUN")} in class and share a hot fudge {ask_questen("NoUN")} after
	school. And if your {ask_questen("adJeCtIVe")} friend wants some advice on the
	latest {ask_questen("NoUN")} in their life, you'll give them the {ask_questen("adJeCtIVe")}
	truth. And finally, if you ever need a/an {ask_questen("Part of the Body")} to cry
	on, your BFF will be there with a box of {ask_questen("PLUraL NoUN")} and a/an
	{ask_questen("NoUN")} of hot cocoa. Who could {ask_questen("VerB")} for
	anything more?""")	
		elif libnum=="4":
			print(f"""Wow! I bought a new smart-{ask_questen("NoUN")} today. It not only
	makes {ask_questen("NoUN")} calls—it also forecasts the {ask_questen("NoUN")}
	so I know whether to wear a/an {ask_questen("NoUN")} or carry a/an
	{ask_questen("NoUN")} in case it rains cats and {ask_questen("PLUraL NoUN")}.
	It can also read and send e-{ask_questen("PLUraL NoUN")} and even record a
	TV {ask_questen("NoUN")}. And I will never get lost again because I
	now have a global {ask_questen("VerB eNdING IN “ING”")} system that gets me from
	point A to {ask_questen("NoUN")} B in no time. I also received a/an
	{ask_questen("NoUN")}-reader for my birthday. Imagine not only being
	able to download any book in just {ask_questen("NUmBer")} seconds but
	view hundreds of magazines and {ask_questen("PLUraL NoUN")} from all
	over the {ask_questen("NoUN")}. How did we ever get through each
	{ask_questen("adJeCtIVe")} day before these {ask_questen("adJeCtIVe")} inventions?""")
		elif libnum=="5":
			print(f"""Do you remember radio, handwritten letters, and landline
	{ask_questen("PLUraL NoUN")}—all the technology used by your parents to
	communicate with their {ask_questen("PLUraL NoUN")}? These technologies
	are now as old as {ask_questen("NoUN")}. They've been replaced by
	Twitter and {ask_questen("Part of the Body")} -book. Twitter is a great way to stay
	in touch with all your {ask_questen("PLUraL NoUN")} and share {ask_questen("adJeCtIVe")}
	information about what is happening in your own {ask_questen("NoUN")}.
	Just remember to keep it to 140 characters. Facebook is a social
	{ask_questen("VerB eNdING IN “ING”")} service with more than five hundred million
	{ask_questen("PLUraL NoUN")}. You can create a/an {ask_questen("adJeCtIVe")} profile,
	add other {ask_questen("PLUraL NoUN")} as friends, and exchange {ask_questen("adJeCtIVe")}
	messages. Face-{ask_questen("NoUN")} was founded by {ask_questen("PersoN IN room")}
	and a few of his {ask_questen("adJeCtIVe")} college classmates. Social networks
	are popular on the {ask_questen("noun")} Wide Web, where they have
	their own {ask_questen("adJeCtIVe")} language, such as GTG (got to go),
	LOL (laughing out loud), or XOXO (hugs and {ask_questen("PLUraL NoUN")}).""")
		elif libnum=="6":
			print(f"""Although video {ask_questen("PLUraL NoUN")} have been around for over
	{ask_questen("NUmBer")} years, they've become more and more {ask_questen("adJeCtIVe")}
	as developers create more sophisticated {ask_questen("PLUraL NoUN")}. Today's
	{ask_questen("NoUN")} games are so complicated, they require really
	{ask_questen("adJeCtIVe")} attention at all times. They have you sitting
	on pins and {ask_questen("PLUraL NoUN")} throughout the entire game. Such
	{ask_questen("PLUraL NoUN")} as Final {ask_questen("NoUN")} XIII, Grand Theft
	{ask_questen("NoUN")}, and (the) {ask_questen("place")} Noire cost more
	to develop than many {ask_questen("adJeCtIVe")} movies produced by big
	Hollywood {ask_questen("PLUraL NoUN")}. If the technology in the video-gaming
	{ask_questen("noun")} continues to advance, imagine what future electronic
	{ask_questen("PLUraL NoUN")} will be like. It's {ask_questen("noun")}-boggling.""")
		elif libnum=="7":
			print(f"""Our Fourth of July started out {ask_questen("ADJECTIVE")} enough. Aunt
	{ask_questen("PERSON IN ROOM (FEMALE)")} and Uncle {ask_questen("PERSON IN ROOM (MALE)")} were coming
	over to spend the day with my family. We had a really {ask_questen("ADJECTIVE")}
	barbecue set up in the backyard, with lots of {ask_questen("TYPE OF FOOD (PLURAL)")}
	and {ask_questen("PLURAL NOUN")} right off the grill. The trouble started when
	my aunt and uncle arrived and we found out they had brought
	along the newest and most {ask_questen("ADJECTIVE")} member of their family:
	a/an {ask_questen("NUMBER")} -pound pet pig named {ask_questen("CELEBRITY (MALE)")}!
	The pig looked {ask_questen("ADJECTIVE")} enough, and he even made a noise
	that sounded like “{ask_questen("EXCLAMATION")}!” when I petted him on
	his {ask_questen("PART OF THE BODY")}. But when we put him in the backyard to
	{ask_questen("VERB")}, everything got totally out of hand! The pig took one
	sniff of all the {ask_questen("ADJECTIVE")} food and started to {ask_questen("VERB")} around
	like crazy. He knocked over all the tables and {ask_questen("PLURAL NOUN")}, destroyed
	my kid sister's playhouse, and took a swim in the {ask_questen("TYPE OF LIQUID")}.
	“That's it!” my father yelled. “Next time you bring a/an {ask_questen("ANIMAL ")}
	to a barbecue, we're going to cook him!”""")
		elif libnum=="8":
			print(f"""My best {ask_questen("NOUN")}, {ask_questen("PERsON IN ROOM ")}, is a pro at serving detentions
	and suggests bringing the following items to make it through the hour:
	• A/An {ask_questen("NOUN")} phone—but don't use it for
	{ask_questen("VERB ENDINg IN “INg”")}; instead, use it as a watch, a calculator, or a/
	an {ask_questen("NOUN")}. And be sure to turn it to “{ask_questen("VERB")}”
	so it doesn't ring.
	• An i-{ask_questen("NOUN")} to listen to music. Cover up the
	{ask_questen("PART OF THE BODY")}-phones by wearing a hooded {ask_questen("NOUN")} .
	• Some tissues, in case you need to blow your {ask_questen("PART OF THE BODY")}
	• Blank paper and something to {ask_questen("VERB")} with. Use
	these {ask_questen("ADJECTIVE")} items to compose love songs to your
	crush, {ask_questen("PERsON IN ROOM")}, draw a comic strip featuring
	{ask_questen("PERsON IN ROOM")} as the underwear-wearing superhero Captain
	{ask_questen("NOUN")}-pants, or even do something crazy, like your
	{ask_questen("NOUN")} homework
	• A pair of {ask_questen("NOUN")}-glasses—you might as well look
	{ask_questen("ADJECTIVE")} while you're there!""")
		elif libnum=="9":
			print(f"""Pack your bags! It's time to take a/an {ask_questen("ADJECTIVE")} road trip across
	the United States to visit some of the most {ask_questen("ADJECTIVE")} historical
	landmarks. First stop is Philadelphia, where you can visit Independence
	Hall to see where the Declaration of {ask_questen("PLURAL NOUN")} was signed. After
	that, check out the Liberty Bell. It's the most famous cracked
	{ask_questen("NOUN")} in history, and a symbol of freedom across America.
	Then head on up to Boston, where you can check out the USS
	Constitution, the oldest {ask_questen("VERB ENDINg IN “INg”")} naval vessel, and the
	{ask_questen("NOUN")} Hill Monument. In New York, you can climb to the
	top of the {ask_questen("NOUN")} of Liberty (or take a/an {ask_questen("VEHICLE")} to
	check out the view from the harbor!). Now it's time to head west, where
	you can see famous landmarks like Mount {ask_questen("SILLY WORD")}, which
	features carved statues of the {ask_questen("PART OF THE BODY (PLURAL)")} of some of our
	most {ask_questen("ADJECTIVE")} presidents. Or check out {ask_questen("COLOR")}-stone,
	our first national park, which includes the famous geyser Old
	{ask_questen("ADJECTIVE")} ! Just don't forget to pack a/an {ask_questen("NOUN")}—you'll
	want to take pictures to remember your {ask_questen("ADJECTIVE")} trip by!""")
		elif libnum=="10":
			print(f"""Are you a king, queen, or {ask_questen("OccUPAtION")} looking for that perfectly
	{ask_questen("AdjEctIvE")} new home? Then have we got a/an {ask_questen("AdjEctIvE")}
	place for you! King {ask_questen("PERSON IN ROOM (MALE)")} 's {ask_questen("AdjEctIvE")} castle
	has just come on the market! Originally built in the {ask_questen("AdjEctIvE")}
	Ages, this lakefront wonder has towers that rise high above (the)
	{ask_questen("place")} and a/an {ask_questen("AdjEctIvE")} view that will take your
	{ask_questen("PARt OF tHE BOdY")} away. In each and every room of this 25,000 square-
	{ask_questen("PARt OF tHE BOdY")} masterpiece, there are magnificent stained glass
	{ask_questen("PLURAL NOUN")} and splendid Gothic {ask_questen("NOUN")}-burning
	fireplaces. There's also a chef's state-of-the-art, {ask_questen("AdvERB")}
	modern {ask_questen("NOUN")} for those who love to {ask_questen("vERB")}.
	For security and {ask_questen("AdjEctIvE")} privacy, there is also a moat filled
	with {ask_questen("PLURAL NOUN")} and a drawbridge to keep out unwanted
	{ask_questen("PLURAL NOUN")}. Take advantage of the collapse in the castle
	market and make a/an {ask_questen("AdjEctIvE")} offer on this treasure. The
	asking price is a ridiculously low {ask_questen("NUMBER")} dollars. """)
		elif libnum=="11":
			the_odd_one=""
			the_odd_one=ask_questen("animal")
			print(f"""It is difficult not to envy a young woman who has everything her
	{ask_questen("PARt OF tHE BOdY")} desires. But history shows it isn't easy being a
	princess. You have to maintain {ask_questen("AdjEctIvE")} standards and abide
	by {ask_questen("AdjEctIvE")} rules. For example:
	• A princess should always be kind to, and understanding of, her
	royal {ask_questen("PLURAL NOUN")} . A princess knows that a/an {ask_questen("AdjEctIvE")}
	smile is preferable to a/an {ask_questen("AdjEctIvE")} frown.
	• A princess should be a patron of the arts, well-versed in classical
	{ask_questen("NOUN")} , and {ask_questen("AdvERB")} familiar with
	{ask_questen("AdjEctIvE")} authors and their {ask_questen("AdjEctIvE")} works.
	• A princess should never make a/an {ask_questen("AdjEctIvE")} decision. She
	should always think before {ask_questen("vERB ENdING IN “ING”")} . And when she
	does speak, she should be articulate and, if possible, very
	{ask_questen("AdjEctIvE")} .
	• And, of course, a princess must be prepared to marry a/an
	{ask_questen("AdjEctIvE")} prince and live {ask_questen("AdvERB")} ever after.""")
		elif libnum=="12":
			print(f"""It's summer, and you know what that means: {ask_questen("ADJECTIVE")}
	weather, icy-cold {ask_questen("NOUN")}-sicles, and big blockbusters. Check
	out what's coming to a/an {ask_questen("NOUN")} near you this summer!
	• {ask_questen("PLURAL NOUN")} of the Caribbean: Captain {ask_questen("PERSON IN ROOM (MALE)")}
	and his band of {ask_questen("ADJECTIVE")} scalawags take to the {ask_questen("ADJECTIVE")}
	seas in search of buried {ask_questen("PLURAL NOUN")}.
	• The Big {ask_questen("ADJECTIVE")} Ogre: A cranky ogre named
	{ask_questen("PERSON IN ROOM (MALE)")}, his sidekick—a/an {the_odd_one}
	named {the_odd_one}—and a/an {ask_questen("ADJECTIVE")} gang of
	fairy tale creatures go on a search and {ask_questen("VERB")} mission to
	rescue Princess {ask_questen("PERSON IN ROOM (FEMALE)")} from a tower guarded by a firebreathing {ask_questen("NOUN")}.
	• The Boy Wizard: A/An {ask_questen("ADJECTIVE")} boy discovers he
	possesses magical {ask_questen("PLURAL NOUN")} that he must use to defeat the
	evil wizard, Lord {ask_questen("PERSON IN ROOM (MALE)")}.""")
		elif libnum=="13":
			print(f"""Are you cheery and {ask_questen("PLURAL NOUN")} at the crack of dawn? Do you
	leap out of bed early in the morning, ready to greet the world with
	a dazzling {ask_questen("ADVERB")}? As a journalist, can you quickly switch
	gears from interviewing the ruler of (the) {ask_questen("VERB")} to quizzing
	an expert on the effects of global {ask_questen("ARTICLE OF CLOTHING")} on the planet to
	judging a beauty contest for {ask_questen("BODY PART")}? Then you could
	be the {ask_questen("ADJECTIVE")} morning show host we're looking for! The
	number one-ranked show Good Morning, {ask_questen("NOUN")} is
	searching for a cohost to join the current host, {ask_questen("PLURAL NOUN")}.
	The show combines {ask_questen("ANOTHER BODY PART")}, hard news stories with lighter
	pieces such as cooking and {ask_questen("PLURAL NOUN")} segments, interviews
	with A-listers like {ask_questen("ANOTHER BODY PART")} and {ask_questen("NOUN")}, and
	fashion tips such as one hundred stylish ways to wear a feathered
	{ask_questen("NOUN")}. Salary is {ask_questen("VERB ENDING IN “ING”")} a year plus a
	generous allowance for clothing and {ask_questen("ADJECTIVE")}. Are you
	qualified? Then {ask_questen("VERB")} today for an application!""")
		elif libnum=="0":
			return
def lists():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	type_text("hi i am listy (but evoryone calls me lil'lister)")
	clist = betinput("what is the name of your list: ")
	thelist = []
	while True:
		action = betinput("""what do you want to do
0 to stop
1 add item
2 remove item
3 to print and leave the list (note this also deletes it): """)
		if action != "1" and action != "2" and action != "3":
			type_text("i am not impressed with your efforts to brake me")
		if action == "1" or action == "2" or action == "3":	
			if action == "1":
				inpuy = betinput("what do you want to add: ")
				thelist.append(inpuy)
			elif action == "2":
				print(flush=True)
				print(f"          {clist}          ",flush=True)
				print("_",flush=True)
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("_",flush=True)
				while True:
					remove = int(betinput("what do you want to remove: "))
					if remove > len(thelist):
						type_text(f"you dont have a item at {remove}")
					elif remove < 1:
						type_text("i am not impressed with your efforts to brake me")
					else:
						del thelist[remove-1]
						break
			elif action == "3":
				print(flush=True)
				print(f"          {clist}          ",flush=True)
				print("_",flush=True)
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("_",flush=True)
				clist = betinput("what is the new name for the new list: ")
				thelist = []	
			elif action == "0":
				return
def initGame():
	global ep
	print("epilepsy warning")
	time.sleep(1)
	gointor = 1
	if ep == 0:
		while gointor != 2000:
			for x in range(random.randint(1,gointor)):
				print("  ",end="")
			for x in range(round(gointor/10)+1):
				print(random.randint(0,1),end="")
			print()
			time.sleep(random.uniform(0,3/gointor))
			if gointor %50 ==0:
				print(""" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                                                                              """)
			gointor+=1
		print(""" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                                                                              """)
		time.sleep(.7)
		for x in range(10000):
			print()
	global world
	global location
	global inventory
	global health
	global damage
	global color
	global name
	global playedAmount
	world = deepcopy(worldTemplate)
	location = world["field4"]
	inventory = []
	health = 100
	damage = 5
	name = betinput("whats your name adventurer (type your name then press enter to continue): ")
	color = betinput(f"hello {name} whats your favorite color: ")
	type_text(f"""hello {name} who likes the color {color}, your quest is "{quest}" good luck""")
	type_text("search for loot to get loot")
	type_text("battle monsters")
	type_text("get the holy grail")
	type_text("win")
	playedAmount+=1
	
def move(loc: str):
	global location
	global inventory
	for item in [item for item in inventory if item.life != None]:
			item.life -= 1
			if item.life == 0:
				type_text(f"Your {item.name} has expired")
				inventory.remove(item)
	location = world[loc]
	#print(f'moved to: {location}')

def selectOption(options: List[Tuple[str,any]], cancelable = True, noOptionText = "You can't do that.") -> any:
	options = [x for x in options if x[1] != None]
	if len(options) == 0:
		type_text(noOptionText)
		return None
	while True:
		try:
			type_text("Select an option:")
			if cancelable:
				type_text("0. Cancel")
			for i, option in enumerate(options):
				type_text(f"{i+1}. {option[0]}")
			value = int(betinput("Choose wisely: "))
			print()
			if cancelable and value == 0:
				return None
			elif value < 1 or value > len(options):
				type_text("try again")
			else:
				return options[value-1][1]
		except ValueError:
			type_text("Invalid input")

def randomItem(rarity = 0):
	if sum([item.luck for item in inventory]) > 0:
		rarity += 1
	if rarity == 1:
		return copy(random.choice(norm))
	elif rarity ==2:
		return copy(random.choice(rearer))
	elif rarity ==3:
		return copy(random.choice(goodLoot))
	elif rarity ==4:
		return Item("ball of thorns", health=50 ,type="consumable")
	raise Exception(f"Invalid rarity {rarity}")

def useItem():
	global health
	global inventory
	item:Item = selectOption([(item.name, item) for item in inventory if item.type == "consumable"], noOptionText="You have no items to use")
	if item == None:
		return False
	health += item.health
	if item.health > 0:
		type_text(f"You used {item.name} and gained {item.health} health")
	else:
		type_text(f"You used {item.name} and lost {-item.health} health")
	type_text(f"You have {health} health left")
	inventory.remove(item)

def BOD():
	global name
	global playedAmount
	global color
	nam = betinput("""you come to a rope bridge spanning a casum and a man stops you and says "Stop. Who would cross the Bridge of Death must answer me these questions three, ere the other side he see. What... is your name: """)
	if nam.lower() != name.lower():
		type_text("wrong *as you are thrown into the casum*")
		type_text("you die and aliens take your body and are diapointed that you cant play poker")

		type_text("game over")
		return "dead"
	else:
		nam = str(betinput("What... is your quest: "))
		if nam.lower().strip() != quest.lower().strip():
			type_text("wrong *as you are thrown into the casum*")
			type_text("you die and are turned into a lemon")
			type_text("game over")
			return "dead"
		if playedAmount >1:
			nam = betinput("What... is the air-speed velocity of an unladen swallow: ").lower()
			if nam == "What do you mean? An African or a European swallow?".lower():

				type_text(" Huh? I... I don't know that. AUUUUUUUGGGGGGGGGGGHHH!! *as he is thrown into the casum*")
				type_text("you successfully make it across the bridge")
				return "mountain5"
			else:
				type_text("wrong *as you are thrown into the casum*")
				type_text("you die and joe takes your apendix")
				type_text("game over")
				return "dead"
		else:
			nam = betinput("What... is your favorite colour: ").lower()
			if nam != color.lower():
				type_text("wrong *as you are thrown into the casum*")
				type_text("you die and billy the bird makes you into a nest")
				type_text("game over")
				return "dead"
			else:
				type_text("you may pass")
				type_text("you make it across the bridge")
				return "mountain5"
				
def holyGrail():
	type_text("You have found the Holy Grail!")
	if betinput("do you drink(y/n):")=="y":
		print("""Traceback (most recent call last):
  File "/Users/this is a joke/personal/pythonPlay/game.py", line ∞, in <all>
    item = banana
           ^^^^^^
  File "/Users/also a joke/personal/pythonPlay/game.py", line ∞, in lemon
    raise Exception(f"Invalid rarity {good food}")
Exception: Invalid rarity 2037946809832759832""")
		time.sleep(5)
		type_text("BACK FROM THE DEAD CODE")
		type_text("hahaha")
		type_text("P.S. you win")
		return"dead"
	else:
		return "dead"


def totalDamage():
	"""returns total damage"""
	return (sum([item.damagebuff for item in inventory ])+1)*damage

def battle():
	global health
	global inventory
	global location
	predamageItems = [item for item in inventory if item.predamage > 0]
	monster = location.monster
	type_text(f"A {monster.name} appears!")
	for item in predamageItems:
		type_text(f"you used an {item.name} and did {item.predamage} damage")
		monster.health-=max(item.predamage, 0)

	while True:
		type_text(f"The {monster.name} has {monster.health} health left")
		option = selectOption([
			("Fight", "fight"),
			("Use Item", "useItem")
		], cancelable=False)
		if option == "fight":
			type_text(f"You fight the {monster.name}")
			attack = totalDamage()
			type_text(f"You deal {attack} damage")
			monster.health = max(0, location.monster.health - attack)
			if monster.health <= 0:
				type_text(f"You have defeated the {monster.name}")
				item = randomItem(monster.lootLevel)
				type_text(f"{monster.name} dropped a {item.name} and you picked it up")
				inventory.append(item)
				location.monster = None
				return True
		elif option == "useItem":
			if useItem() == False:
				continue
		type_text(f"{location.monster.name} attacks!")
		health -= location.monster.damage
		if health <= 0:
			type_text("You have died and a antelope ate your earlobes")
			return False
		type_text(f"You have {health} health left")
def the_game():
	global ep
	
	while True:
		ep = 0
		if betinput("do you want to play(y/n)").lower()!="y":
			break
		if betinput("do you have epalepsy(y/n): ").lower() != "n":
			ep = 1
		initGame()
		while True:
			if location.description == "BODY":
				if BOD()=="dead":
					break
				else:
					move("mountain5")
			elif location.description == "grail":
				holyGrail()
			else:
				type_text(location.description)
				if location.monster:
					if battle() == False:
						break
				if health<0:
					type_text("you died")
					type_text("game over")
					break
				option = selectOption([
					("Move", "move"),
					("Search for loot", "search"),
					("Use Item", "useItem")
				], False)
				if option == "useItem":
					useItem()
				elif option == "search":
					if location.hasLoot:
						item = randomItem(location.itemRarity)
						location.hasLoot = False
						inventory.append(item)
						type_text(f"You found a {item.name}")
					else:
						type_text("You found nothing")
				elif option == "move":
					place = location.moves.selectMove()
					if place:
						move(place)
def rickle():
	type_text("""hi i am rickle the pickle
	
	
	
	
	you will regret pressing 15
	""")
	for x in [1,2,3,4]:
		time.sleep(2)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠉⠀⠀⠀⠀⠀⣀⠀⠀⠀⢀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⣦⡄⠠⠀⠄⠂⠄⡀⠀⠄⠀⠀⠀⠉⠈⠁⠀⠀⠀⠉⠉⠉⠓⠢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠠⠒⢀⡀⡉⠌⠡⠉⡁⠂⠤⢀⡴⠀⠀⠉⠐⣀⠈⠁⠀⠂⠀⠀⠐⠒⠒⠲⣦⣄⡀⠀⠀⠀⠀⠀⠘⣿⡄⢁⠈⡁⠢⠠⠡⠘⣀⡀⠀⠀⠀⠀⠀⠀⣀⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠠⢁⠂⠄⠒⣀⠲⢁⠈⡀⠁⢀⠀⠈⠀⠁⠆⡁⠄⡱⠊⠉⠀⠀⠀⠀⠀⠀⠉⠐⠆⠀⠀⠀⠀⠀⠉⠲⠌⡙⠿⢶⣦⣄⣀⣀⣀⣼⢃⠀⢂⠄⢡⠀⠀⠡⢀⠱⠦⣤⠤⢤⠶⢻⠁⢉⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠀⠀⠀⠀⠀⠀⢄⠂⡀⠀⠐⠀⠉⠒⠪⠤⠐⡄⠀⠀⡀⠏⠐⢠⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⡰⠨⡍⣉⠉⡀⠄⠌⡂⠜⡠⢂⠀⡀⠂⢄⣰⣠⢎⠔⠚⠦⠖⢤⠡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠂⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⡀⠡⠀⠍⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠁⠀⠀⢘⠠⠈⢆⠡⡘⡐⢠⣿⠾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠈⠄⠀⠁⠀⠀⠀⠀⠀⠀⠀⠙⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠆⠀⠀⠀⠀⠀⠀⠀⢈⠡⠈⠄⢂⠁⡘⢻⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣟⠃⠀⠀⠀⠀⠀⠀⠈⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⢡⠈⠄⢂⠐⡀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠐⠀⠀⢀⢠⣄⣄⠠⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠴⠤⠴⠂⠂⠄⠂⠙⠀⢠⡆⢈⡀⠄⡄⠈⣽⡻⢷⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠈⠉⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⣠⡔⠚⠛⠿⣶⣤⣄⠈⣰⡀⠀⠀⠀⡁⠀⠀⡀⢰⠀⠹⣿⣆⠈⠉⠻⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠉⠀⠀⠀⠀⠀⠀⠀⠁⠳⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⢀⣴⡾⠟⠀⠀⠀⠀⠀⠙⠻⢿⣼⠳⡄⠀⠀⢟⠀⠀⠐⢸⡄⠀⠈⢻⣧⡀⠀⠀⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠈⠹⢷⣦⡄⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⣠⣤⣤⣄⣾⡿⡿⠿⣿⣿⠿⣶⣦⠀⠀⣀⣰⣾⣧⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣴⡀⠀⡘⠆⢈⠐⣸⠂⠀⠀⠀⠹⣷⠀⠀⠂⢀⣀⠉⠻⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠈⠙⠿⣶⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣿⣿⠿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⡆⠀⠠⠀⢀⠒⠀⠀⠀⠀⣰⣿⣃⣠⣴⠞⠉⠉⠀⠀⠉⠙⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣾⣿⣻⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⡀⠡⠃⠀⢉⠀⠀⠀⠀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⢠⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⡐⠠⠑⡈⠌⠀⠀⠀⣠⣾⡿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⠍⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠡⡘⠀⣂⠐⣾⡿⠁⠰⣇⠙⣦⠄⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠈⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⢀⡀⠀⠀⠀⣀⣴⣿⠟⣫⣽⣿⣿⣿⣿⣿⣿⣿⡿⣿⠿⢟⡛⢫⡙⢍⡋⠟⣿⣿⣿⣿⣷⣤⣀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣟⠀⢡⠈⠁⠀⣼⣿⠃⠀⠀⠘⣷⣾⣇⠀⠀⠀⢠⡴⠂⡁⠈⠀⠀⠀⠀⠀⠀⠀⢀⠐⠠⠀⠄⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡁⠀⠀⠀⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⢷⡀⠀⢶⣿⣿⣿⣾⣽⣿⡿⡟⣭⠳⣍⢲⢡⠚⡤⣉⠖⣨⠡⡘⠤⡘⠒⣌⢾⣿⣿⣧⢻⠿⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠏⠁⢀⠰⡂⢀⠈⣿⡃⠀⠀⠀⠀⠈⠻⣿⠀⢶⣾⡯⠅⡐⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⢀⠠⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠢⣀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⢱⠀⠈⠻⣿⣿⣿⣿⡿⣳⢽⡌⠷⣌⠳⣎⠱⢢⠱⡘⢤⢃⡙⢂⠅⢣⢌⣻⣿⣿⣿⣧⡆⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠀⣼⡅⣰⠄⠀⠀⠆⡁⠄⡘⣿⡅⠀⠀⠀⠀⠀⠀⣿⣤⠿⠛⠀⠀⠀⠀⠃⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⣟⠀⠀⠀⢈⠃⠀⠀⣹⣿⣿⣿⢳⡭⢞⡹⣏⡞⣽⠸⣍⢣⠓⣍⣒⢢⣘⣤⣊⣥⣊⡽⣿⣿⡿⡹⢿⣶⣶⣽⣿⣦⣀⢀⣠⣤⣶⠟⠉⠀⠁⠀⠀⢈⠱⢀⠂⠄⣿⠆⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠐⠂⠀⠀⠣⠀⠂⠀⠀⠀⠀⠀⢀⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠈⠀⣤⡾⢿⣿⣿⣿⣧⢻⣭⣷⣿⣿⣿⣿⣷⣯⢞⡹⢿⣿⣿⣿⡻⣿⣿⣿⣿⣿⠃⡇⠀⠀⠈⢻⣯⢹⣿⣿⣯⣭⣤⣐⡈⠦⣄⠀⠀⠠⢂⠡⠈⠄⣻⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠘⠋⠀⣨⠋⠘⣿⣿⣿⣿⣿⣽⣶⣿⡿⣿⣿⣷⠰⣈⠻⢿⠿⡿⠟⢣⢰⣿⣿⣴⡗⠀⠸⠀⠐⣿⣿⠁⠀⠀⠉⠉⠛⢿⣧⡄⠡⠀⡐⠌⡄⢁⠂⡅⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⢘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡾⠏⢀⣴⣿⠛⣿⣿⡭⢏⡳⢧⣛⡶⣹⣿⡷⢠⠍⣂⣳⠀⢎⡐⢌⠋⡽⣿⣧⢀⣦⣀⣤⠂⣹⡄⠀⠀⠀⠀⠀⠀⠙⣿⣦⠁⡀⠂⠔⢂⠠⠐⠀⠀⠀⠂⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠑⠈⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⠹⣿⡀⠀⠀⠀⣸⡏⠻⣧⡀⠀⠀⡴⠀⠀⠀⢀⣾⡟⠁⠀⠀⢸⣿⡁⠎⣼⣿⣝⣫⡝⣧⢿⡗⣧⣏⣶⣭⣾⡟⢣⠉⣆⠰⢊⣵⣿⣟⣿⡟⠋⠉⠀⠀⡙⠿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢿⣦⠁⠌⡀⢂⢉⠀⠀⠀⠀⣠⣿⡇⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣽⣷⣀⣠⣾⡟⠀⠀⠙⢿⣆⠀⠃⠀⠀⠀⠀⢿⣇⠀⠀⠀⠈⢻⣿⣖⣰⣿⣿⠲⣝⡎⡷⣿⣿⠿⠟⡛⡅⠎⣄⠓⡄⢣⢾⣿⣿⣿⡿⠁⢀⡴⠀⠉⠑⣶⣉⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⡗⠠⠐⡀⠂⢀⣠⣴⣿⠟⠹⣷⡀⠀⠀⢠⣾⠃⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠞⠛⠋⠁⠉⢻⣍⣿⠁⠀⠀⠀⠈⠛⢿⣄⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⣠⡘⣿⣿⣿⣯⡽⣷⣽⣞⣿⣮⣼⣵⣌⣜⣰⣂⡱⢈⢽⣿⢿⣿⠏⡱⠂⢻⠀⠀⠀⠀⠈⢿⣆⠸⣷⠀⠀⠀⠀⠀⣰⣿⠋⠠⢁⠐⡈⢄⣽⡿⠃⠀⠀⠛⠿⣷⣤⣿⠃⣀⠀⠀⠀⠀⠀⠈⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⢈⣿⠀⠀⠀⠀⠀⠈⣿⣧⡀⠀⣽⡇⠙⣿⣞⣿⣿⣿⡛⣛⣻⢻⣿⣿⣿⣟⠛⡍⢆⡉⣾⣿⣺⣿⡆⠑⠀⠹⠀⠀⠀⠀⠀⠈⢿⣆⠹⣷⠀⠀⠀⣴⡟⠁⠠⠁⠂⠌⢰⣿⠛⠁⠀⠀⠀⢠⣴⣬⣿⠃⠀⠈⠛⠳⢤⣄⠀⠀⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⢸⣏⠀⠀⠀⠀⠀⠀⣿⣿⠿⠉⠁⠀⠈⠉⠁⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢨⠜⡹⢸⠹⣿⣷⠹⣿⡀⠐⢿⣀⡀⠀⠀⠀⠀⠸⣿⣦⡹⢁⠀⡙⠋⠀⠁⠢⡑⡈⠐⢸⡿⠀⠀⠀⠀⠀⠀⢘⣿⡃⠀⠀⠀⠀⠀⠀⢬⣷⡄⠀⡁⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⣠⠴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢿⣗⠛⠓⠊⠁⠀⢺⡧⠀⠀⠀⠄⢠⣴⠯⠻⢿⣦⡀⠀⠀⠀⢀⣀⣹⣿⡇⣿⣿⣿⣿⣿⣿⢉⣷⠏⡔⢣⡙⡜⣿⣇⠙⣿⣶⣄⠉⠻⢧⣀⣀⠀⠀⠈⠙⠁⢂⠐⠠⠀⣄⠠⠐⡠⠁⠌⣈⣧⠀⠀⠀⠀⠀⢠⣾⠟⠀⠀⠀⢠⡄⠀⠀⠀⠈⠻⢂⠀⠡⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠀⠈⣿⣄⠀⠀⠀⠀⢸⣟⠀⠀⠀⠀⢨⡇⠀⠀⠈⣿⣿⡆⠀⠀⠀⠀⠙⣿⡯⣿⣿⣿⣿⣿⣿⣾⣿⠩⣜⡡⠚⡌⣿⡟⠀⣿⣿⣿⣷⣶⣤⡉⡉⠛⠀⠀⠀⠰⠀⡌⠀⠀⠈⠁⠌⠐⡁⠐⠨⣗⠀⠀⠀⠀⠀⣾⡟⠀⠄⠀⠀⣰⣿⡄⠀⠀⠀⠀⠀⠈⠄⡡⢀⠁⢀⠀⠀⢀⡀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⢠⡀⠀⠘⣿⡄⠀⠀⠀⢸⣇⠀⠀⠀⠀⢹⡇⠀⠀⠀⢹⡏⠻⠷⣦⣤⡤⢼⣿⣗⣿⣿⣿⣿⣿⣿⣽⣇⠳⣜⢡⢋⣴⣿⠇⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣐⡀⠀⠀⠢⡴⣄⠠⠈⠄⣿⠀⠀⠀⠀⣼⡟⠀⠌⠀⠀⠀⢻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠁⠂⠀⠀⡀⠀⠀⠀
		⢀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠙⣷⡀⠀⠹⣷⠀⠀⠀⢸⡧⠀⠀⠀⠀⢸⣷⠀⠀⠀⠺⣿⠀⢂⠄⠉⠀⢀⣻⣼⣿⣿⣿⣿⣿⣿⣼⡏⣖⠩⢆⣻⣿⠏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠉⠒⣼⣷⠀⠀⠀⢐⣿⡁⢈⠐⠀⠀⠀⠸⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡀⠀⠀⠁⠂
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⢸⣏⠀⠀⢀⠀⠀⢿⣆⠀⠀⠀⣿⠀⠂⢈⣿⡟⣼⣿⣿⣿⣿⣿⣿⣟⣿⣿⣏⢦⣻⣾⣿⠏⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣈⢡⡀⣸⠛⢄⠠⡎⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠟⠄⠀⠀⣯⢽⡄⠀⠘⣧⠀⠈⠀⠄⠂⠈⢿⣇⢀⣴⣿⠧⣤⣶⣿⡏⢡⠚⣿⣿⣿⣿⣿⣿⣿⢿⣜⣾⣿⣿⠃⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣹⠇⠀⠈⣚⢷⡄⠀⠀⠀⠘⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠸⣿⣷⠀⢸⡗⠀⠀⠀⢛⠆⠀⠈⠻⣹⣾⣴⣿⣿⣿⣿⣷⢀⠀⠈⢿⣿⠿⠟⢻⣿⣟⣾⣿⠟⡁⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⠀⠀⣹⡘⠻⣧⡀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠁⠠⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⣤⣶⡀⠀⠀⢰⣦⡀⠀⢸⡿⠀⢸⠃⠀⢂⠐⡌⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⡏⣆⠀⠀⠀⠠⠀⣸⣿⣿⣿⠏⡀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠨⢇⡐⣿⡇⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠄⠁⠀⠀⠀⠁⠂⠀⠈⠀⠀⠀⠀⠀⠀⠜⣹⡿⠁⠀⠀⠈⠻⣿⣆⠘⠠⡐⠆⠀⢠⣀⡂⣄⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢸⣤⠀⠀⠡⠀⣿⣿⢟⢣⡐⢠⠀⠠⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠠⠄⠀⠀⠿⣿⡆⠀⠀⡸⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⡐⠀⠀⠀⠀⡀⠄⠂⠀⠀⠀⠀⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⣴⣿⠀⠀⠀⠀⠀⠀⠸⣿⣄⠀⠁⢂⠈⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡚⣻⣿⣀⡀⢠⣿⣯⣾⣶⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠹⣿⡄⢂⠐⠠⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠠⠈⢀⠐⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⡀⠀⢀⣤⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣌⢠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⣿⣿⣴⣿⣿⣿⣽⣭⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠂⠀⠀⠀⠻⣿⣄⡈⠄⠀⠂⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢀⠀
		⠀⢀⠀⡀⠠⠀⠀⡀⢀⡀⠀⣀⢀⠀⡀⢀⡀⣀⣀⣈⣿⣶⣿⣯⣤⣄⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡐⠠⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⣿⠁⠠⣿⡄⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠰⠶⠶⠶⠷⠲⠒⠰⠦⣾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠔⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⠈⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡇⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠙⣿⣧⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⠘⢭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⢠⣶⠟⠋⠀⠀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⠄⠀⠀⠘⢷⣄⠹⣷⣄⠀⢀⣤⣾⢿⣿⠂⠀⣍⠒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢀⠉⠁⠀⠀⠀⠀⢹⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⠀⠀⠀⠀⠈⠻⣦⡈⠛⠷⣿⡋⣠⣿⠇⠀⠈⣿⠌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠠⠀⢀⠴⠃⠀⠀⠀⠀⠀⠀⠸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠂⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠂⠀⠀⠀⠉⢻⣦⡀⣠⣿⠟⠁⠀⠀⠀⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠐⠀⡈⠠⡀⠃⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠊⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣿⠃⠀⠀⠀⠀⠀⣿⠳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠁⣀⠣⠀⠀⠀⠀⠀⢀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠛⢻⣦⠀⠀⠀⠀⢰⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠠⠀⡁⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⠀⠄⡀⠁⠉⠀⠁⠀⠁⠀⠈⠀⠀⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠚⠁⠀⠀⠀⠘⣿⣆⠀⠀⠘⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠡⠀⢄⡀⠀⠀⠀⠠⢀⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢤⣌⢿⣦⡀⠀⢻⡇⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠄⡁⢂⠄⢃⠀⠀⠀⢂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡄⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢶⠉⠛⠷⠂⠄⣸⣿⣿⠿⢛⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠈⠐⡂⠄⠠⢈⠀⠎⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠾⣦⠀⠀⢀⡚⠛⣉⣡⣰⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠐⠰⡈⡐⢠⠘⠤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⢻⣵⣿⣿⣿⣿⢻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠁⠀⠁⠢⠁⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⣏⢷⣣⢛⣶⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠂⢀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡿⣝⣞⡳⢮⡝⣶⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠠⠈⢀⠀⠂⠀⠀⠀⠀⠁⠈⠠⠁⢀⠀
		⠀⠀⢈⠁⠆⡀⠠⠀⠌⠠⠈⠄⠂⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣯⣿⣿⣿⡽⢮⣝⣧⢻⡜⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⠀⠀⠠⣉⠐⡀⠄⠂⢀⠡⠈⡀⠐⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣹⠾⣼⡻⣜⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠁⠀⡀
		⠀⠠⠡⠄⢂⠀⠠⠐⢀⠀⢂⠀⡁⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣷⣯⣟⡳⣝⢶⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⢀⠠⠀⠀
		⠀⠄⢡⠈⢄⢂⠡⡀⢆⠨⠄⢢⠐⠠⡐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠀⠀
		⠤⡘⠠⠌⢂⠌⠰⢁⠌⢂⠍⡀⢃⠱⠀⠄⢀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⠐⣀⠣⠌⠠⠈⠄⠂⠌⢂⠒⢌⠠⢌⡁⠂⢀⠂⠄⠈⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⡀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⡐⢀⠢⢈⠔⡩⠘⡈⠒⡌⡘⠄⢂⠆⡐⡈⠤⠈⢀⠐⠠⠐⢀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⡀⠠⠐⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⡿⣾⣻⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠄⢃⡐⠌⠰⠠⡁⠆⠱⣀⠱⡈⠆⡘⠤⡁⠄⡐⠠⢈⠀⠄⠂⡀⢁⠠⢈⠠⠀⠌⢀⠈⠄⡐⢃⠐⠠⠁⠠⠡⠉⠌⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢿⣽⡿⣯⣿⣻⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠌⠤⡘⠄⢡⢂⠡⠌⡐⢠⢂⠡⡘⢠⠂⠅⠢⣁⠃⢌⡘⠨⠄⡐⢂⠄⠢⢄⠩⠄⠂⠈⠄⡐⠀⠂⡁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣟⣿⣽⢷⣻⣽⡷⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⣘⠰⣀⠎⡰⢈⠆⡤⢑⠢⢌⠒⡄⠃⡜⠈⢡⠐⠨⡐⠌⡐⠄⡑⠈⡀⠅⠂⢀⠈⠀⠁⠂⠄⡈⠀⠄⠀⠄⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣻⢾⡽⣯⣟⡷⣿⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠃⠌⠒⠡⢉⠚⡐⠩⡘⢈⠑⡀⠃⠄⠡⠂⠌⡐⢀⢂⠰⢀⠁⠆⠠⠁⠌⠠⡀⠅⢂⠁⢂⠠⢈⡐⢠⠂⠀⣌⠀⡀⠀⠀⠀⣼⣿⣼⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢯⣟⣯⡽⣷⢯⡿⣽⢷⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠉⠀⠀⠀⠀⠀⣠⠀⢀⠀⣀⠀⠀⢠⣠⡀⠀⠀⡀⠀⢀⣀⣀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠉⠈⠙⠛⣦⡄⠠⠀⠄⠂⠄⡀⠀⡄⠀⠀⠀⠉⠈⠁⠀⠀⠀⠉⠉⠉⠓⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠤⠒⢁⡀⡉⠌⡁⢉⠉⠒⢤⣥⣼⠗⠂⠁⠂⢄⡀⠉⠙⠒⠂⠠⠴⠲⠖⠷⣦⣄⡀⠀⠀⠀⠀⠀⠘⣿⡄⠈⡐⢉⠐⠤⠡⠐⣀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⢀⠡⢀⠐⠀⠄⠒⡀⠲⢁⠈⡀⠄⠈⠀⠀⠁⡐⡀⠂⠌⡼⠟⠋⠁⠀⠀⠀⠀⠈⠙⠛⢆⠀⠀⠀⠀⠀⠙⠶⣉⠙⠿⢶⣦⣄⣀⣀⣀⠼⡄⢂⠐⡄⣈⠀⠀⠡⢀⠒⠤⢄⠤⢠⠖⡍⠃⠐⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠀⠀⠄⢊⠀⡀⠐⠈⠑⠓⠊⠤⠄⡌⠀⠀⣀⠓⠠⢁⠴⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⣄⠫⡭⢉⡉⠄⠰⡀⢊⠔⡠⢂⠀⡀⢂⠐⣠⣌⠢⠅⠺⠔⠦⢌⡡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠂⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠰⡈⠐⠤⢁⢂⠡⣀⡾⠴⠈⠙⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠡⠈⠄⠡⢈⠒⣹⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠤⠥⢈⠐⡀⠂⠄⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠠⠐⠈⠀⠀⢀⡀⢤⣠⠀⠀⠀⣶⣴⣦⣄⣠⡀⢀⣀⣀⣀⡀⠀⠀⠀⣀⡀⠀⠠⠀⠀⠀⠀⠀⠀⠠⠀⠂⠄⠂⠙⠀⢠⡆⢐⠠⠀⡌⠀⣽⣻⢷⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠀⠀⠀⠀⠀⣠⣾⣿⢿⣿⣿⣿⣿⣿⣟⣛⡻⠟⠿⣷⣶⣤⡀⠀⠀⠀⠀⠈⠀⠲⢶⣤⣄⠈⡐⠀⠀⠀⠀⠄⠀⠈⠀⠄⠀⠹⣿⣤⠈⠙⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠰⠁⠀⠀⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⣉⠿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣬⠃⡄⠀⠀⢋⠀⠀⠁⢸⠀⠀⠈⢿⣧⡀⠀⠀⠛⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠶⣦⣀⠀⢘⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⡀⠀⠌⡃⠌⡐⠬⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⣀⠉⠛⢿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⡆⠀⡀⢀⠀⡒⠀⠀⠀⠀⣰⣿⣁⣠⣴⠞⠉⠉⠀⠀⠈⠙⢳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣯⣟⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢃⢀⠘⡀⢀⠁⠀⠀⠀⠀⣾⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣟⣴⣿⣿⣿⡿⣟⢿⡻⢟⡻⡍⢯⠙⠦⡑⢌⠲⡐⣌⠚⣿⣿⣿⡿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠂⠄⡘⢄⠂⠈⠀⠀⣠⣾⡟⢧⡀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠈⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠘⣿⣿⣿⣿⣿⡻⣜⡱⣎⠵⣋⠴⣉⠦⡙⢆⡙⠤⢃⠒⠤⡙⠼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡠⠀⢐⠨⢀⠃⡐⣾⡿⠁⠘⣆⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⡀⢀⠀⠀⠀⣶⣄⡀⠀⡀⠀⠀⣹⣿⣿⣿⣿⡵⢫⡵⣋⣾⣵⣮⣴⣣⣑⠪⠜⢦⣉⣌⣴⣈⣖⣹⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡥⠀⡈⠒⠀⠀⣼⣿⠃⠀⠀⠈⣷⣮⡆⠀⠀⠀⢠⡄⠂⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⠀⠄⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠙⢿⣤⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⠀⠀⠀⢶⣭⢹⣿⠏⠀⠀⢹⣿⣿⣿⣿⡹⣓⣾⣝⣯⣝⣭⣛⠿⣿⣞⡌⣒⣼⣹⣏⣛⣿⣿⣿⣿⣯⠀⠀⠀⠂⠀⠀⠀⠀⣤⣤⠔⠋⠀⢀⠰⠡⠀⢈⣿⠃⠀⠀⠀⠀⠈⠻⣷⠀⢶⣿⡯⠄⡐⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠂⢀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠻⣿⣍⢶⣄⠀⠈⢿⣿⣿⣷⣿⣿⡿⢿⠿⣻⢿⣿⣾⡽⢻⠿⣿⣿⠿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣼⡅⢨⡀⠀⠀⡌⠐⡈⠐⣿⡃⠀⠀⠀⠀⠀⠀⣿⣤⠾⠛⠀⠀⠀⠀⠒⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⣏⠀⠀⠀⠀⠀⠀⠀⢈⡏⠀⠙⢿⣷⣿⣿⣯⡝⣣⢿⣿⡿⢿⢣⣾⣿⣿⣧⣃⢆⠿⠿⠿⠿⢁⠖⣿⣧⣽⣿⣿⡄⣀⢀⣠⣤⣶⠟⠉⠈⠁⠀⠀⠉⢐⠡⡀⠁⣿⠀⠀⠀⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠐⠂⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠸⠃⠀⠀⠀⠀⠀⣠⠾⢛⣡⣶⣿⠿⣿⣶⣿⡟⡼⣣⢟⡮⣝⣮⣿⣟⢧⣻⣝⣿⣿⣼⣦⣽⠠⠁⡎⣌⣿⡿⢻⣷⢹⣿⣿⣯⣭⣤⣂⡌⠤⣀⠀⠀⠠⢊⠐⠠⠁⢚⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠂⢀⣼⡟⠁⠀⠀⢻⣷⣻⣿⣷⣿⣮⣳⣽⠮⡵⣎⢯⣽⣿⣯⡍⡍⢩⢁⣧⠘⡔⣾⣿⠇⠀⠿⠀⠀⠀⠀⠉⠉⠛⢿⣶⡀⠄⡀⠀⢆⡑⠂⡁⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⢘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⠀⠀⠀⠀⠀⠹⣷⣬⣿⠿⣿⣿⢭⡳⣝⢾⠿⡿⣏⠱⡰⣬⡶⢏⠅⡎⣽⣿⣏⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⢁⠂⠰⠀⠄⠰⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠑⠈⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⠸⣿⡀⠀⠀⠀⣸⠏⠻⣧⡀⠀⠀⣀⠀⠀⠀⢀⣼⡟⠁⠀⠀⠀⠀⠀⣀⣀⣴⣿⡛⢿⣿⣝⣿⣯⣓⢮⣯⣽⣱⣎⣷⡡⡐⢌⢎⡒⣼⣿⡟⠋⠁⠀⠀⠀⠲⣦⣀⠀⠀⠀⠀⠀⠈⠛⢿⣦⠈⠄⠡⢈⡐⠀⠀⠀⠀⣠⣿⡇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣹⣿⣀⣤⣾⡟⠁⠀⠙⢿⣆⢠⠁⠀⠀⠀⠈⢿⡇⠀⠀⠀⠀⠀⠀⣸⣿⣏⣾⠟⠉⢹⣿⣿⣧⢛⣮⢓⣧⢫⡝⢡⠒⡉⠦⣈⢜⣿⣿⣿⣦⣄⠀⠀⠀⢀⡈⠛⣿⡆⠀⠀⠀⠀⠀⠈⢿⡧⢈⠐⡀⠄⠀⢀⣴⣾⠟⠉⣶⡀⠀⠀⢠⡾⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠒⠛⠋⠉⠉⢻⣍⣻⠁⠀⠀⠀⠈⠛⢷⣆⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⢀⣴⣿⣿⡟⠁⠀⠀⠈⣿⣿⣷⣯⣶⣏⣶⣇⠞⣥⣎⣑⣦⡑⠎⣿⣿⣿⣯⣿⣦⣄⠀⠀⠻⡆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠇⡀⠆⡐⠠⢈⣩⡟⠁⠀⠀⠛⠿⢷⣤⣿⠃⢀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠚⠁⠀⠀⠀⠀⠀⠀⠸⣿⡏⠀⠀⠀⠀⠀⠀⢀⣿⠂⠀⠀⠀⠀⠈⢿⣧⡀⢀⣿⡟⢈⣿⠃⠀⠀⠀⢰⣿⣟⡛⠛⠛⢛⣿⣿⣏⠶⣩⠛⡥⢊⡕⢚⣿⣯⠻⣿⣯⡝⠿⣶⣤⣡⡀⠘⢷⠀⠀⠀⣰⡟⠁⠠⢀⠡⢘⠠⠃⠈⠀⠀⠀⠀⢀⣠⣤⡛⠁⠀⠈⠙⠂⠤⡀⠀⠀⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⣽⣟⠻⠟⠋⠀⠘⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⢄⠫⡔⢣⠜⣬⣿⠇⣸⣿⣿⣿⣷⣮⣽⣛⣿⢿⣿⣶⣶⣮⣥⣀⡈⠐⠠⠂⠄⡘⠀⠀⠀⠀⠀⠀⠀⢈⣿⠇⠀⠀⠀⠀⠀⠀⠬⣥⡄⠀⠡⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⡀⠰⠚⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀⢿⣗⠛⠓⠂⠉⠀⢹⡧⠀⠀⠀⠄⢠⣴⠿⠻⢿⣦⡐⠀⠀⠀⠀⣀⢀⣀⣤⣿⣿⣧⡿⣿⣿⢹⣿⣿⠰⣉⠞⣹⢢⢻⣾⠿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣭⣛⣛⢿⣿⣷⣧⣀⣐⠀⠀⠀⠀⠀⠀⠀⣾⠛⠀⠀⠀⠀⡀⠀⠀⠀⠈⠛⠄⠀⢂⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠈⣿⣄⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠇⠀⠀⠈⣿⣿⡆⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣧⢿⣿⢧⢫⡔⣩⢆⣽⣿⡟⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣟⡿⣿⣶⣤⡀⠀⠀⠰⠃⠠⢀⠀⠀⣤⣿⡀⠀⠀⠀⠀⠀⠑⢂⡐⠠⠁⢀⠀⠀⣀⠀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠂⠀⠀⢀⠀⠀⠘⣿⡄⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⠄⠀⠀⠀⢸⠏⠻⢳⣦⣤⣤⣴⣾⣽⣿⣿⣷⣿⣿⣯⣿⣿⢎⡳⣜⣶⣿⣿⡟⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣯⣿⢿⡆⠤⢁⠘⡀⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⡀⠀⠀⠀⠀⠀
		⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠘⠷⠀⠀⠹⣷⡀⠀⠀⢸⡗⠀⠀⠀⠀⠀⢳⠀⠀⠀⠘⢃⠐⡠⢌⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣟⢮⡽⣺⣽⣿⠏⠀⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠀⠌⡰⢀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠁⠈⠀⠁
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⢸⡏⠀⠀⡀⢀⠀⢀⣀⠀⠀⢀⡰⣮⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⡿⠋⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡅⠀⠀⠀⠀⢹⡇⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⢾⣹⡄⠀⠘⣗⠀⠀⢁⠂⠈⠀⠻⣷⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠘⡛⢿⡟⢉⠹⣿⣿⣿⡟⢁⠀⢀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢶⡀⠀⠀⠀⠀⢿⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠄⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡷⠀⠈⠏⠀⠀⠀⢂⠠⣐⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠼⠿⠛⣻⣤⣹⣿⣿⣿⣶⣷⡾⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢈⠻⣷⡀⠀⠀⠈⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠀⠄⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡀⠀⠀⢠⣦⡀⠀⠘⠇⠀⢘⠳⠲⣤⣼⣦⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢂⠀⣽⣿⣿⣿⣷⣾⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠄⡀⢶⠄⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠐⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠐⠀⠀⠈⢱⡞⠁⠀⠀⠈⠻⣷⣄⠀⠠⢐⠂⢀⣣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡔⠠⢈⣿⣿⣻⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠀⠘⢏⣒⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠠⠀⠀⠀⠀⡀⠄⡈⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⣴⣿⠂⠀⠀⠀⠀⠀⠘⣿⣄⠀⠀⣈⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⢠⣿⣿⣟⣿⣻⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠙⡶⢀⠂⠄⡁⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠠⠁⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⢀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⣨⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠹⣧⡐⠠⠐⠀⠂⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢀⠀
		⠀⢀⠀⡀⠠⠀⠀⡀⢀⡀⠀⣀⢀⠀⡀⢀⠀⢀⣀⣀⣿⢤⣿⣯⣤⣄⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣨⣿⣧⢸⡳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⣽⣷⣻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠙⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡐⠠⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠹⣿⠁⠀⣿⡄⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⢉⣿⡿⠁⡒⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣿⣯⣿⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠰⠶⠶⠲⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠔⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⠈⠿⣦⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⠟⠁⠀⠬⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⢂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠙⣿⣧⠀⠀⠀⠀⠀⠀⣾⣿⡃⠀⠆⠀⠀⠌⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣾⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢀⡤⠂⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠈⢷⡄⠹⣷⣄⠀⢀⣤⡾⢟⣿⠳⣤⡌⠰⠀⢂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢀⠀⠀⠀⠄⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠻⣦⡈⠙⠷⠿⠋⢀⣾⠃⠀⢹⣿⠀⠐⠀⠂⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡚⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⣠⣾⠟⠁⠀⠀⠘⣿⡄⠀⠈⠠⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⠢⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠀⠀⣿⡇⠀⠀⠡⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠛⠿⣦⠀⠀⠀⠀⢸⣿⣷⠀⠀⢁⠂⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠌⠐⠀⠁⠈⠀⠁⠀⠁⠀⠈⠀⠀⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠚⠉⠀⠀⠀⠙⢿⣦⠀⠀⠈⣿⡏⠀⢀⠂⠈⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⡐⢀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢄⣀⢻⣧⡀⠀⣿⡏⠀⠂⠌⠠⡐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⡐⢀⠀⠀⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⡁⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡍⠛⠿⢿⡗⠀⣉⠠⣱⢌⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠑⢂⠐⡀⠂⠄⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠠⢾⣷⡀⠀⠀⠄⡐⢀⢚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠐⣀⢂⠰⡁⠜⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢁⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⣠⠈⡀⠄⠂⠾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠈⠠⠑⠨⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣥⣭⣍⣜⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠰⠀⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⠿⡛⡟⠿⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⡿⣯⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠀⠀⠁⠈⠠⠁⢀⠀
		⠀⠀⠀⠆⡐⠀⠠⠐⠈⠠⢈⠐⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣟⣯⣖⢣⠱⣌⢣⠱⡩⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣽⣻⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⠀⠀⠠⣁⠐⢀⠂⠄⠈⡀⠂⡀⠌⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣭⣒⠣⡜⢢⢹⡐⢫⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣳⣟⣾⢯⣷⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠁⢀⠀
		⠀⠠⠡⠄⡈⢀⠀⠄⠂⠀⢂⠀⡐⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣧⣓⡬⢃⠦⡙⢦⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣷⡿⣞⣯⢿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡝⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⢀⠁⠀⠀
		⠀⠠⢁⠂⢡⠀⡂⢄⠂⡅⠢⡐⢠⢈⠐⠠⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⢱⣩⠒⡍⣆⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⢿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⣾⣽⣻⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⠟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠐⠀
		⢠⢁⠂⡜⢀⠃⡘⢀⠎⡐⠡⠘⡀⠎⡐⠀⢀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⣣⢏⣷⣾⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣻⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣯⣷⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠐⠀⠀
		⢀⠂⠒⡠⢈⠐⡀⢂⠐⢠⠃⡒⢠⠑⡄⠁⠠⠐⠀⠈⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⢁⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠫⠉⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣾⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⡽⣟⣾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠄⣈⠐⡀⢆⠢⡑⢈⡐⠢⡑⠨⠄⡒⠠⢌⠠⠁⢂⠐⡀⠐⢀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠁⡀⠡⠀⠌⡘⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⡿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣯⢿⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡰⠀⢂⠅⠂⠥⠐⠂⢄⠃⢌⠱⡈⠔⡡⢂⠄⡐⡀⢂⠀⠄⡈⠀⡐⢀⠁⠂⡀⢂⠠⢈⠀⠌⠓⡈⠐⡀⠙⣿⣿⣿⡿⠋⠀⠀⠀⠀⣠⡿⢏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣟⣯⢿⣽⣻⣷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⡾⣿⡾⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠄⡑⠢⠌⡐⢢⠉⠔⣈⠰⠈⢆⡐⠢⢁⠆⠢⡐⠡⢈⠜⡐⢠⠁⡔⠠⠘⡄⢘⠠⠀⠄⠈⠄⠂⠁⡀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⣰⣿⣿⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣯⢿⣳⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⢯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡱⢈⢅⠂⣅⠢⣉⠔⡠⢣⠘⡤⢐⠡⢂⠌⡑⢈⠁⠎⡐⠰⠠⠁⠄⡁⠆⠈⢀⠀⠌⢀⠂⠐⠠⠀⢀⠀⠀⠄⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣞⣳⡿⣯⣟⡷⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⢿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢁⠊⠌⠱⢈⠁⡃⠎⠡⢃⠩⠐⠡⢈⠂⡐⠈⠄⠌⡐⠠⢁⠂⡉⠐⠠⢈⠐⡀⢢⠐⣄⠂⢡⡀⠂⠠⠐⡀⠠⣄⣦⣆⡀⣠⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣟⡾⣽⣻⢷⢯⡿⣽⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠈⠉⠀⠀⠀⠀⠀⣀⠀⢀⠀⣀⠀⠀⠀⡀⠀⠀⠀⡀⠀⢀⠀⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠉⠈⠙⠛⣦⡄⠠⠀⠄⠂⠄⡀⠀⡄⠀⠀⠀⠉⠈⠁⠀⠀⠀⠉⠉⠉⠑⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠤⠒⡀⢈⡁⢊⠡⠉⠉⠄⣠⣄⣶⡿⠓⠉⠀⣄⣈⡁⠀⠖⠠⠤⠶⠿⠾⢷⣶⣄⡀⠀⠀⠀⠀⠀⠘⣷⠄⢁⠨⠁⠆⠰⠁⠔⢂⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠠⠐⡀⠂⢀⠒⡀⠲⠈⡀⠁⠀⠠⠀⠁⠀⣁⠂⠌⡐⣼⡿⠋⠁⠀⠀⠀⠀⠈⠛⠻⢷⠀⠀⠀⠀⠀⠛⠷⢮⠙⠿⢷⣦⣤⣀⣀⣀⢈⠆⢀⠂⡡⠌⡀⠈⠰⢀⠡⠄⣠⢀⠤⡔⢊⠅⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠀⠀⡐⠠⢀⠀⠐⠀⠉⠓⠨⠔⠠⢄⠀⠀⡀⠣⢈⠐⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠂⢄⣈⠹⢭⠉⡁⠂⠌⡠⢘⠰⡐⢀⠀⡀⢂⠐⡠⣄⢪⠐⠜⠆⠦⢤⠡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠁⠂⠔⠈⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣄⣀⣀⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠡⢈⠐⡁⠆⡡⠘⣀⡦⠵⠊⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⡐⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠄⠘⠀⠀⠀⠀⠀⣠⣾⡿⣟⣿⣿⣯⣽⣿⣿⣿⣿⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⢂⠡⠈⠄⠃⢽⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠠⠌⡄⢂⠡⢈⠐⡀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠠⠈⠀⠀⢀⢀⠀⡀⠄⠀⣠⣶⡿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡀⠀⠂⠔⡀⠛⠀⢠⡆⠐⡀⠠⠄⢀⣹⡻⢷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⠀⠉⠀⠀⠀⠀⣰⣿⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠈⢔⡀⠀⠀⠀⠄⠐⠀⠁⠠⠀⠙⣿⣤⠀⠉⠻⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠃⠀⠀⠀⠀⠀⣸⣿⢏⣻⣿⣿⣿⣿⣿⣿⣿⡿⡿⢿⣿⣿⣿⣿⠿⢿⠿⡿⣿⣿⣿⣿⣿⡄⠉⠻⣷⣎⠒⡀⠀⠀⢃⠀⢀⠈⠰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢹⣿⣳⣿⣿⣿⣿⢻⡽⣿⣋⠖⣩⠒⣌⠲⡉⢄⠚⠄⠣⠔⡡⢞⣿⣿⣿⡇⠀⠀⠈⣿⣷⣄⡀⠀⠐⠎⠀⠂⡜⠀⠀⠀⠀⠹⣷⠀⠠⠀⢀⡀⡉⠙⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⣿⣿⡜⡧⢞⡳⣏⢿⣆⠳⡄⢣⢘⠢⣉⠜⡀⠎⠱⡘⣿⣿⣿⣧⠀⠀⠈⠀⠉⠙⢷⡆⠀⠠⠈⠀⡜⠀⠀⠀⠀⣰⣿⡁⣠⣴⠞⠉⠉⠀⠀⠈⠙⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⣜⡽⣩⢷⣜⣎⣿⣦⢑⠢⢡⠒⣁⠂⡐⢈⠱⡐⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠈⠄⠠⢁⠃⠠⠐⠀⠀⠀⢀⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⢷⣹⣾⣿⣿⣿⣿⣿⣿⣿⣎⢡⢛⣷⣿⣶⣶⣧⣽⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⡀⠢⠐⢨⠐⠡⠈⠀⠀⣠⣾⠟⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠒⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⢣⡟⣿⣿⣿⡿⢟⣻⣿⣿⣿⡆⡜⣸⣿⣿⣿⣽⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠐⡁⠀⡀⠎⡐⠠⠀⣿⡿⠁⠈⠄⠐⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⠀⢀⠀⠀⠀⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⡿⣿⣿⢧⣾⣿⢟⣣⠙⣦⣿⣿⣿⣿⢇⡰⠰⢘⡋⠌⠩⡙⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⡐⠡⠀⠁⣼⣿⠃⠀⠀⠈⢶⣄⠀⠀⠀⠀⢀⡤⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⢀⠐⡀⠁⢀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢤⣌⢹⣿⠁⠀⠀⠀⠀⠀⠐⢿⣯⡓⡖⣬⣿⣿⣿⡿⣬⣿⣿⣛⢿⣿⣿⣆⣴⣡⠦⡉⠜⠠⣜⢻⣿⠇⠘⠂⠀⠀⣤⣤⣼⠛⠀⢀⠸⠄⢀⠈⣿⠃⠀⠀⠀⠀⠀⠹⣆⠀⢴⣾⡏⠄⠠⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠈⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣴⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⡯⠀⠀⠀⠀⠀⠈⠻⣷⣬⣶⣄⡀⠀⠀⠀⠀⢼⣿⣿⣞⣶⣿⡛⡿⣱⣿⡿⣱⢯⣿⡿⠿⡛⢛⠻⡡⢼⠬⡱⢮⣿⡏⠀⠀⠀⠀⢀⣭⡁⢄⡀⠀⠀⠂⠌⠀⠌⣿⠂⠀⠀⠀⠀⠀⠀⣹⣤⠾⠋⠀⠀⠀⠂⠡⠀⠀⠀⠄⠠⠀⠀⠀⠀⠈⠀⠄⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢈⠅⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠙⢻⢿⣶⣶⣴⣾⣿⣿⠿⠿⢿⣿⣼⠿⣟⣵⣫⣾⣷⣬⣵⣈⣆⣣⣵⠊⠴⣱⣿⣏⣀⣀⣠⣤⣶⠏⠁⠀⠀⠀⠀⠈⠡⢈⠐⡀⢿⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠐⠡⠀⠀⠣⠐⠀⠀⠀⠀⠀⠀⢀⠀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠠⠶⠛⣣⣴⡿⠿⠛⠷⢶⣭⣿⣿⠉⢸⣷⣾⣿⣯⡻⣜⣻⠻⣟⠿⡻⢟⠟⡛⡛⢩⢌⣷⣿⣿⣿⣿⣿⣿⣭⣄⣐⡈⠄⢀⠀⠀⢀⠆⡁⠂⠄⡈⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⠟⠁⠀⠀⠀⠀⠀⢹⣿⣧⠀⠈⠙⣿⡟⢿⣿⣱⢣⡟⣜⢣⡓⢎⠲⡄⡱⢡⣾⣿⢿⣿⡅⠉⠀⠀⠈⠉⠛⢿⣦⡄⠂⡀⠄⠒⠤⠁⠂⡄⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⡏⠙⠆⠀⠃⣿⣿⢷⡲⣭⣗⡺⣭⢶⣩⣆⢃⣖⣩⣷⣾⣿⣿⡝⣿⣆⠀⠀⠀⠀⠀⠀⠙⣷⣆⠐⢈⠠⠡⠈⠄⠠⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠑⠈⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠹⣿⡀⠀⠀⠀⢸⡋⢻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠁⠀⠀⠀⠀⠀⣀⣠⣴⣿⠏⠀⢀⣈⢳⡓⢸⣿⣧⣛⠿⣿⢿⣿⣿⣿⣿⡿⢟⠻⣉⣾⣿⢻⣿⣦⠻⣷⣄⠀⠀⠀⠀⠀⠉⠻⢿⣆⠠⠁⡌⠠⡑⠀⠀⠀⠀⣀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣿⣀⣤⣾⡟⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠃⠀⠈⠻⣿⣿⣏⣿⣿⢭⢳⡎⣿⡿⡭⢍⢎⠱⣌⠣⣐⣿⣿⢸⣿⣿⣷⣮⡙⠛⠂⠀⠀⠀⠀⠀⠈⢿⠇⡐⠠⠁⠆⠀⢠⣴⡾⠟⠉⣤⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠄⠒⠋⠉⠁⠉⢫⣍⣿⠁⠀⠀⠀⠈⠛⢷⣄⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⣀⣴⡿⣿⠟⠁⠀⠀⠀⠀⠹⣿⣿⣼⣿⣎⡷⣹⢶⣻⡷⡌⢎⠷⡠⢓⣼⣿⠇⣾⣿⣿⣿⣿⣿⣷⣶⣤⣀⣀⠀⠀⠠⣼⣧⣔⡀⢁⠂⠌⢠⠒⠀⠀⠀⠘⠻⠆⣠⡿⠃⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀⢈⣿⠀⠀⠀⠀⠀⠈⢿⣧⡀⢀⣿⠏⠀⡌⠀⠀⠀⣠⣼⣿⣴⣞⠛⠛⠛⠻⣿⣷⣫⢞⡱⣜⠪⢇⡱⣣⣿⠇⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣌⣉⡉⠻⢷⣾⣦⠀⠀⠀⠀⠀⠀⣤⣀⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠉⠀⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣴⠋⠻⠟⠋⠀⠄⠡⢠⣴⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⢣⡟⡲⣍⣾⣶⣿⡿⠃⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣍⡉⠳⠆⠄⠀⠀⠀⡝⠀⠀⠀⠀⠀⠀⠀⠠⣤⡄⠀⠌⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⢿⡗⠒⠂⠀⠀⠀⢹⡏⠀⠀⠀⠀⠀⠐⠋⠀⠤⣀⢂⣱⣾⣿⣿⣿⣿⣿⣿⡧⣿⣿⣣⣏⣿⣟⣻⣿⢢⣝⣳⣿⣿⡿⠋⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠠⠀⡐⠀⠄⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠈⣿⣄⠀⠀⠀⠀⢸⡧⠀⠀⠀⠀⠀⠀⠀⣤⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⣿⣿⣷⢾⣿⣯⢿⣿⣖⣧⣿⣿⠟⠁⠀⠀⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠻⡀⠄⠂⠀⡤⣤⠀⠀⠀⠀⠀⠀⠑⠄⡡⡈⠄⠠⠀⠀⣀⠀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⢀⠀⠀⠘⣿⡄⠀⠀⠀⢠⡗⠀⠀⢠⠐⣨⣴⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣟⣿⣿⣿⠈⠿⣿⡿⠋⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠠⠌⠀⠀⢻⡷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⡀⠀⠀⠀⠀⠀
		⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠘⢂⠀⠀⠹⣷⠀⠀⠀⠀⣯⢀⣱⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣤⣾⣽⣳⣶⣶⣤⣀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢂⠀⠀⠸⣿⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠁⠈⠐⠁
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢻⡇⠀⠀⠀⣿⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣿⣿⣟⣿⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣫⢹⡀⠀⠀⡿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⢻⣿⡟⠿⢻⢟⠿⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡀⠀⠀⠀⠀⠱⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠄⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠃⠀⠀⠃⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠒⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠿⣷⠀⠀⠀⠐⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠠⢀⠀⠄⣀⠀⠀⠀⠀⠀⠀⠀⣠⠄⠀⠀⠀⢠⣦⠀⠀⠈⠁⠀⠀⢀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡃⢌⣿⣶⣶⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣀⣾⠀⠀⠀⠀⢢⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠐⠀⠀⠀⠀⠀⠂⠀⠈⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠻⣿⡄⠀⠀⠄⠃⣀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠜⢈⣿⣧⣺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⡝⣲⢭⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠿⣤⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠐⡀⠀⠀⠀⡀⠄⡈⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠈⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠂⢸⣿⣯⣛⣿⣻⣿⣿⣿⣿⣿⣿⣿⡿⣥⢫⡜⣧⢻⣜⡳⣎⠿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣇⡐⠠⠁⠌⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠀⠐⠀⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢀⠀⠀⢀⣤⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣄⠈⠐⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⣼⣿⡝⣮⡳⢎⡷⣩⣛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠸⣷⡄⠁⠂⠐⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀
		⠀⢀⡀⠈⠀⠂⠀⢀⠀⡀⠀⣀⢀⠀⡀⠀⠀⠀⠀⢀⣂⠠⣿⣏⣤⣀⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣘⣿⡇⠈⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⢯⣷⢫⡗⣟⢯⣗⡳⡜⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠉⠐⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠌⡀⠁⠂⠀⠀⠀⠁⠀⠀⠀⠀⠁⠈⠉⠙⣿⠃⠀⢿⡄⠀⠀⠀⠁⠉⠉⠉⠉⠉⠉⠁⠀⢀⣿⡿⠈⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣫⢿⡼⣯⢽⣫⢞⣦⢳⣙⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠰⠀⠀⠀⢀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠆⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⠈⠿⣦⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⠋⠀⠠⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢾⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣽⡞⣧⢻⡜⣧⢞⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡌⠠⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠸⣿⣧⠀⠀⠀⠀⠀⠀⣾⣿⠃⠀⡐⠀⠀⡐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⣭⢳⡻⣜⡯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠷⡄⠹⣷⣄⠀⢀⣤⣾⢟⡿⠃⣤⡠⠑⢀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⢷⣝⢧⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠛⣄⠈⠙⠷⠿⠋⢀⣿⠁⠀⢹⣷⠀⠂⠈⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⣠⣾⠟⠁⠀⠀⢸⣿⡀⠀⢈⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⡿⠁⠀⠀⠀⠀⢨⣿⡆⠀⠨⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠛⠻⣄⠀⠀⠀⠀⢰⣿⡇⠀⠩⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠁⠔⠠⠀⠁⠉⠀⠁⠀⠁⠀⠈⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢷⣄⠀⠀⠈⣿⡇⠀⠀⢢⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠰⠀⢂⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⢻⡇⢠⣼⣿⡿⢿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠠⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡨⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠈⠁⠂⣹⣧⣿⣿⢯⡝⣧⣛⢾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠌⠃⠄⢂⠁⢊⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠠⠴⢤⡀⢀⣽⣿⣿⡟⣮⡝⣶⢫⣟⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⣄⡡⠌⢠⠘⡀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣹⣿⡶⡹⡜⣧⠿⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠁⠘⠀⠆⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⣳⣿⡷⣱⠹⣬⢛⣮⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⠛⠛⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⠙⢿⣿⣿⣿⣥⡛⣴⣻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠐⠀⠀⠀⠈⠀⠁⠐⠠⠀⠀
		⠀⠀⠐⡀⠆⠁⠠⠐⠈⠄⢁⠂⡐⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⣦⠻⣿⣿⣷⣿⣾⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⠀⠠⡁⠌⢀⠂⠄⠠⠐⠠⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠹⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⢀⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠠⠈⠀⠀⠂
		⠀⠠⠡⠌⡐⠀⠀⠄⠐⡀⢁⠠⠐⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠳⠹⣿⣿⣿⣿⠟⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⢈⠀⠐⠀
		⠀⠠⢁⠂⢄⡁⠆⡐⠤⡐⢄⠢⡐⢈⠄⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠄⠡⠙⠻⠛⠁⠀⠀⠀⠀⢀⣾⣿⢣⢿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣻⣟⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢂⠀⠀
		⢠⢁⠂⠜⡀⠒⡈⡐⢂⠡⠌⢂⠁⠎⡐⠀⢀⠀⠄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠄⠂⡈⠄⡁⠆⢁⠂⠀⠀⠀⠀⣿⣿⢢⢃⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣻⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀
		⢀⠢⠘⠄⠠⠁⠄⡐⠀⢆⡉⠆⢡⠊⠔⠀⢂⠈⠄⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠀⠡⠌⡘⠐⠌⠒⠠⢈⠄⡀⠀⠀⠀⢠⣿⣿⡷⣬⣿⣿⣿⣿⣿⣟⣼⣿⣿⣿⣳⣯⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠄⢂⠡⢈⠆⡑⠢⢈⠑⢢⠐⡌⠂⡜⢠⠘⠠⢈⠀⡐⠠⠁⡀⠀⠀⠀⠀⠀⠀⠀⡀⢈⠀⠄⠠⢉⠐⠠⡁⠜⣀⠣⢐⠠⢀⠀⠁⠈⠀⣸⣿⣿⣷⣿⣿⣿⣿⣿⣿⡳⢾⣿⣿⡿⣷⣿⢿⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡌⢀⠢⢁⠢⠡⡁⠆⠡⢂⠱⣀⠃⡌⢢⠑⡠⢀⡐⠀⡀⠄⡀⠁⠠⢀⠂⡐⢀⠂⡐⠠⠈⢈⡑⠢⢉⠐⢠⠃⠔⠌⠂⠁⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣝⣻⣿⣿⡵⣫⣿⣯⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
		⡐⠌⡄⠃⠤⡁⠆⠌⣁⠢⢡⠐⡰⢠⠁⢆⠡⢂⠌⠡⠘⠰⢀⡁⢆⠠⠘⡄⡈⢆⠠⢁⠂⠄⢀⠁⠂⠈⡀⢀⠈⠀⠠⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡵⣻⣿⣯⢳⢯⣿⣯⣟⣯⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡌⠒⡌⠤⡑⢌⡌⡰⢀⢣⢂⡱⠐⡂⠍⠤⢑⠈⡂⠅⡉⠔⢂⠘⡀⢁⠒⡀⠄⠀⠐⠀⡈⠐⠈⢀⠈⠀⠄⠀⡐⠈⠀⠄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣟⣹⣿⡿⣝⢳⣻⣿⣿⡹⢮⣽⣷⣯⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢈⠑⡈⢃⠉⢂⠜⢁⠋⡔⢁⠊⡑⠈⠌⡐⢈⠐⠠⠒⠠⢈⠄⢂⡐⢈⠐⠠⠀⡌⠄⡁⠄⠠⠁⠀⠂⠁⢂⠁⠀⡐⠀⠠⢄⡀⢀⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⡟⣬⠳⣽⣿⣿⡩⢗⣭⣛⢿⣿⣟⡿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢤⡀⠄⠠⢀⠂⠄⢀⠀⠄⡀⠀⠀⠈⠀⠁⠀⠀⠀⠈⠈⠉⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠠⢂⠐⡀⡉⠌⢂⠉⡑⠠⠀⣄⣴⠦⠀⠁⠀⢀⠀⠀⠀⠀⠀⠠⠔⠒⠚⢷⣦⣄⡀⠀⠀⠀⠀⠀⠈⠣⠄⡁⠰⢈⠰⠀⠎⠰⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠄⠡⠀⠄⠢⢀⠲⠀⡀⠀⠁⢀⠀⠁⠀⢉⠄⠂⠄⣱⠟⠉⠁⠀⠀⠀⠀⠀⠈⠀⢀⠀⠀⠀⠀⠀⠉⠲⠌⠛⠿⢷⣤⣄⣀⠀⠀⠐⡠⠐⡀⠆⡐⡀⠈⠰⢀⠡⠄⡠⢀⠄⡴⢈⠃⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠀⠀⠀⠀⠀⠁⣈⠐⡀⠀⠐⠀⠉⠒⠌⠡⠐⣀⠀⠀⡀⠣⢈⠐⡈⠅⠀⠀⠀⠀⠀⠀⣀⠀⡀⠀⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠂⢠⢀⠆⡉⠄⡁⠂⠄⡡⢐⠡⢒⠀⡀⢀⠂⡐⢠⡑⡌⠰⠘⠆⠴⢀⡡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠄⠁⠂⠌⠀⠀⠀⠀⣠⣴⣾⢿⣿⣿⡿⣷⣿⣿⣤⣄⣀⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢈⡐⠁⢆⠡⠌⠂⢄⡡⠂⠂⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠄⠈⠀⠀⠀⠀⠀⣠⣾⣿⣯⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⢈⠐⡈⢁⠺⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠈⠤⣁⠂⡐⢀⠂⠄⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠠⠈⠀⠀⢀⢠⠀⡀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠠⠐⠠⠙⠀⢠⠆⡐⡀⠠⠌⠀⣹⢿⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠀⠀⠀⠀⢠⣿⣿⣵⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣧⡀⢡⠀⠀⠀⠀⡂⠀⠐⠀⠠⠀⠘⣿⣆⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠃⠀⠀⠀⠀⠀⠀⢸⣿⣭⣯⣿⣿⣿⡿⣿⣿⢻⡙⢫⡙⢛⠻⣛⠛⢍⠋⡝⢛⠛⣿⣿⣿⣿⡇⠹⢿⣦⠒⠀⠀⠀⠡⠀⢀⠈⠰⠀⠀⠈⢻⣧⡀⠀⠀⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣏⣟⡿⣍⣳⣼⡡⢜⢂⠓⡄⡉⠆⡱⠈⢄⠋⡜⣿⣿⣿⡷⠀⠘⣿⣦⣅⡀⠀⠐⡃⢀⠂⡜⠀⠀⠀⠀⠹⣷⠀⠀⠂⠀⣀⠉⠙⠻⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⢲⣍⢾⡱⢎⡝⢿⠎⢢⠙⠤⡑⠬⠐⡁⢎⠰⡈⢿⣿⣿⣟⠀⠀⠀⠉⠙⢷⡀⠀⡐⠀⢀⠒⠀⠀⠀⠀⣰⣿⡁⣠⣤⠓⠉⠁⠀⠀⠈⠉⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣏⠷⣮⣷⣿⣿⣾⣿⣾⣥⣊⠱⣼⣦⣡⣐⠠⢆⡑⣻⣿⣿⠏⠀⠐⠀⠀⠀⠀⢂⠀⡘⠄⠀⢉⠀⠀⠀⢀⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣎⣿⢿⣿⣿⣷⣿⣿⣿⣿⣧⢃⠽⣿⣿⣿⣿⣷⣾⣿⣿⠟⠀⠀⠀⠀⠀⠠⠐⡀⢂⠰⢈⠌⠀⠀⠀⣠⣾⠟⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⣿⣿⡿⢮⡝⣮⣝⣏⠻⣉⣿⣿⣿⣿⡎⡐⠹⢿⠿⠻⠿⢿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠰⡁⠀⠠⣁⠂⠌⠐⣾⡿⠁⠀⠂⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣟⣽⣟⠨⣿⡟⣦⣿⣆⣳⣿⡿⣿⣿⣿⢧⢡⠃⡌⢂⠱⠈⣌⢻⣿⡆⠀⠀⠀⠀⠀⠀⢠⡇⠀⢡⠐⠀⠂⣹⣿⠁⠀⠀⠀⢡⡄⠀⠀⠀⠀⢀⡀⢀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢀⣈⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣎⣿⣷⣿⢻⡴⣋⡟⡯⢏⣷⣿⣿⣿⣾⣷⡾⢌⠂⠤⡙⡌⣿⣿⠁⠀⠀⠀⣤⣤⡴⠛⠀⢀⠰⢂⠀⠠⣿⠃⠀⠀⠀⠀⠀⠉⡆⠀⠰⣾⠉⠄⠠⠐⠀⠀⠀⠀⠀⠀⠄⠀⠀⠈⢀⠀⠂⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⡗⠀⠀⠀⠀⠀⠀⠛⣷⣌⣶⣄⡀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡗⣮⢳⡭⣝⣿⡿⣫⠍⠭⠈⠍⠴⡧⢌⢒⡱⣾⡿⠃⠀⠀⠀⢀⡭⠁⢠⠀⠀⠀⠂⠄⡈⠐⣿⡃⠀⠀⠀⠀⠀⠀⣼⣠⠟⠋⠀⠀⠀⠂⠡⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠙⠻⣿⣶⣶⣴⣾⣿⣿⠿⣯⣶⣿⣿⣮⢳⣜⣳⣿⣿⣿⣿⣶⣷⣿⣾⣷⢈⣦⣿⣟⠁⣀⣀⣤⣶⠉⠐⠈⠀⠀⠀⠨⢁⠂⠄⡁⣿⠀⠀⠀⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠐⠀⠀⠀⠀⠀⠀⠄⡀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠐⠛⣠⣶⡾⠿⠛⠳⢮⣭⣿⡿⠁⠰⣏⢿⣯⢻⣿⣷⣎⠗⣮⠵⣊⠦⣑⠂⢆⠒⣌⣲⣿⣿⣿⣿⣿⣿⣭⣄⣐⠈⠄⢀⠀⠀⠠⢄⠈⡐⢀⠘⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⠀⠀⠀⠀⢹⣿⣧⠀⠘⡇⢸⣿⣧⢺⣟⡼⣛⣬⠳⣍⡒⢡⢊⠬⣸⣼⣿⢿⣿⡅⠀⠀⠀⠀⠉⠛⢿⣦⡄⠂⠀⠌⠰⡈⠐⡀⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⠏⠉⠀⢰⡇⢘⣿⣷⣋⣾⣷⣏⣶⣛⣶⣽⣧⣾⣾⡿⢿⣿⣿⣟⣿⣆⠀⠀⠀⠀⠀⠀⠙⣷⣌⡐⠈⡀⠡⠂⠄⡐⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠡⠈⠀⠡⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡀⠀⠀⠀⢸⠋⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠁⠀⠀⠀⠀⠀⢀⣤⣶⠿⠏⠀⠀⢀⣾⣿⣃⣿⣷⡹⣞⣱⢿⣿⡿⣛⢟⡩⠏⡅⠆⣿⣿⢻⣿⣌⠻⣧⣄⠀⠀⠀⠀⠀⠈⠻⢿⣤⠀⠡⢈⠐⠠⠀⠀⠀⠀⣀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢹⣷⣀⣠⣾⡟⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⣸⣿⡋⡌⠀⠀⢘⡿⠻⢿⣷⣺⣿⡵⢣⣏⢾⣿⡧⢍⠲⣐⠧⡘⢬⣿⡟⢸⣿⣿⣷⣌⠙⠟⠀⠀⠀⠀⠀⠀⠈⢿⡆⢁⠂⠌⠂⠀⢀⣴⡾⠟⠉⣤⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠊⠉⠀⠉⢫⣍⣽⠀⠀⠀⠀⠈⠛⢷⡄⠀⠀⠀⠀⠈⢻⣄⠀⠀⠀⢀⣴⣿⠿⠃⠀⣀⣴⣾⠇⠀⢺⣿⣧⣟⣼⣳⢎⡷⣻⡓⣎⠱⣃⠖⣩⣾⡿⠁⣼⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⢠⣼⣥⠂⡈⠄⠡⠈⣌⠞⠀⠀⠀⠈⠓⡀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠁⠀⠀⠀⠀⠀⠀⠘⣿⡏⠀⠀⠀⠀⠀⠀⢈⡿⠀⠀⠀⠀⠀⠈⠻⢧⣀⣀⣿⣟⣩⣶⣿⣿⣿⣿⣋⣀⣤⡙⠛⠛⠛⣿⣿⢎⡷⣣⣛⠤⣓⣌⣮⣿⡟⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠈⠀⠙⠿⣶⣧⣆⠀⠀⠀⠀⠀⢀⢠⢀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⡀⢄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡟⡎⡵⣛⣬⣳⣷⣾⡿⠃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⡉⠉⠀⠀⠠⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⡐⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢿⣇⠒⠀⠀⠀⠀⠸⡧⠀⠀⣀⢠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿⡷⣎⣿⣿⢻⣿⣔⡣⣝⣶⣿⠿⠋⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⡶⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⢂⠀⠄⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠀⠈⣿⣄⠀⠀⠀⠀⠀⣷⣾⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣿⣿⣽⣾⣿⣿⠈⢿⣿⣿⡿⠟⠁⠀⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⡓⠠⢀⠐⠀⣀⡀⠀⠀⠀⠀⠀⠀⠉⠆⣈⡐⠀⡀⠀⠀⢀⡀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⠀⠀⠀⢀⠀⠀⠘⣿⡄⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣷⣻⣿⣯⣰⣾⣿⡷⣄⡀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠿⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⢡⠀⠀⠀⢰⡇⡄⠀⠀⠀⠀⠀⠀⠀⠀⠓⠀⡀⠀⢀⠀⠀⠀
		⢀⣤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠆⠀⠀⠹⣷⠀⠀⠀⠈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⡿⣭⢛⣜⣣⢻⣜⡻⢿⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢆⠀⠀⠐⢻⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠑⠀
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⣿⣿⣷⣶⣷⣾⣿⣿⣿⣿⣿⣿⡟⢶⣣⢏⡞⣖⡣⢎⡝⢪⣳⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠈⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠿⢿⣿⣿⣿⣿⣿⣿⣷⣦⣬⣽⣿⣿⣿⣿⣿⣿⣳⢯⣳⢞⣮⡝⢦⡙⢦⡘⢧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣖⠀⠀⠀⠀⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⢀⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠀⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢏⠚⣿⣿⣿⣿⣿⣿⣯⣭⣟⣿⣿⣿⣿⣿⣿⣷⣿⣯⣟⡾⣶⡹⢦⡙⢦⡙⢦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠻⣷⠀⠀⠀⠐⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠀⠄⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⣀⠀⠀⠘⡷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢨⠐⣿⣷⣾⣿⣿⣟⣹⣛⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢶⡹⢦⡙⢦⡙⡞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠠⣿⡄⠀⠀⠀⠰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠂⢀⠐⠀⠀⠀⠀⠀⠐⠀⠉⠀⠀⠀⠀⠀⠀⠀⢠⠌⠀⠀⠀⠀⠛⣶⡄⠀⢄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠃⠄⣿⣏⣻⣿⣛⠿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡝⡧⣝⢢⡓⣭⢿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠐⠻⣅⠀⠀⠀⣂⠅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠂⠄⠀⢀⠀⠐⡈⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠀⠀⠀⠀⠀⠀⠘⣿⡄⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡌⢘⣿⡟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡳⣎⢧⡱⣊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⡇⠐⠠⢁⠊⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠠⠐⠀⡀⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⢀⣴⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣏⣶⣱⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠘⢣⡐⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⡀⠐⠀⠀⢀⠀⡀⠀⣀⠀⠀⢀⠀⡀⠀⠀⠀⡀⠠⣿⣋⣀⣀⣀⣀⣀⡀⢀⠀⢀⡀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠄⠡⠀⡁⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠙⣿⠁⠀⢾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠌⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠄⠀⠈⠿⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡐⢀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠂⠀⠀⠀⠘⡿⣷⠀⠀⠀⠀⠀⢠⣾⡿⠉⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠂⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠠⠀⠸⣷⣄⠀⢀⣤⡾⠋⢀⣴⡯⡽⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡐⠠⠀⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠀⠀⠀⠀⠀⠀⠈⠙⣶⣿⠋⠀⢠⡟⢨⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⠻⣭⣳⣟⣾⣟⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠐⢨⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣤⡈⠇⠀⠀⢠⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⡻⢌⣛⡶⡽⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡘⢂⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣉⠖⣡⣼⣟⢮⡳⣟⣽⣻⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠘⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠿⣷⣿⣿⣿⣿⣿⣿⡿⣜⣾⣽⣿⡿⣿⡹⢮⡽⡽⣾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠁⠆⠠⠀⠁⠈⠀⠀⠀⠁⠀⠈⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢸⣿⣻⣿⣿⣿⣿⣿⡟⣽⣿⣿⣿⣳⣳⡽⢧⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠠⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠹⣦⣄⢸⣿⣽⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣯⡷⣯⣛⢶⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⡁⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⢆⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠠⢀⠰⢁⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⢮⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⡁⢂⠰⡈⠤⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠁⠢⠁⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠐⠈⠻⣷⣾⣼⣭⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠉⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠀⠀⠐⡈⠄⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡀⠈⢀⠁⠄⡉⠛⠛⠿⠛⠉⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠂⠈⠀⠀⠀⠐⠈⢀⠀⢀⠀
		⠀⠀⠐⠤⢈⠐⠀⠐⠈⠄⠈⠄⠂⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢁⡀⠈⢄⠠⠁⢌⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀
		⠀⠀⠄⡘⠠⠀⠌⠀⢈⠀⠡⢀⠐⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠄⠁⢂⠤⠉⠄⢃⠀⠐⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣛⡾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠄⠀
		⠀⢀⠢⢁⠡⢀⠈⠄⢀⠈⠄⠂⡀⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠈⠔⡠⠂⣉⠐⠠⠀⠈⢲⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⢿⡽⣿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⢀⠁⠀⠀
		⠀⡀⠂⠌⡐⡀⠆⡠⠂⡌⠰⢠⠐⣀⠂⠄⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⡈⠐⠤⣀⠚⠀⠀⠠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣯⢿⣽⢯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⠀⠐⠀
		⠀⠤⢉⠰⠠⠑⡨⢀⠣⢈⠑⢂⠁⠆⠌⡀⢀⠀⠄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠂⡈⡁⠒⠤⢈⠃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣽⣻⣞⡿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⢈⠐⠠⠃⠌⡐⠀⠄⠒⢠⠉⡔⢨⠘⡐⠀⠄⠂⠌⠀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠀⢡⠂⠡⢂⠔⠡⡘⠐⣂⠁⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡟⣷⣻⠾⣽⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠠⠈⠤⢁⠒⡌⠱⠈⡑⢢⠑⡠⠂⠆⠡⢌⠠⠁⠄⡐⠠⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⡀⠄⡁⢂⠌⡁⠆⡌⠐⢠⠑⠠⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣿⡳⢯⣟⣯⢷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⢁⠢⠌⡰⠈⡄⠃⢌⢂⠱⢠⠉⡌⡑⢂⡐⠠⡐⠀⣀⠐⡈⠀⢈⠀⠂⠄⠠⠈⠄⡈⠄⠐⡡⠘⠄⢂⠡⠒⡈⠅⠢⠈⠀⡀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣷⣹⢻⡼⣯⣟⡷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⡐⡀⢆⠡⢠⠑⡌⠰⢈⠄⡊⠤⠘⡠⠘⡄⠢⡑⠄⢃⡐⠌⢠⠐⡂⠌⠰⣈⠱⢈⠐⡀⢂⠁⡀⠡⠈⠀⡐⠀⡀⠠⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⠲⣍⡗⣯⢻⣽⣷⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠤⡑⢄⠊⣄⠣⢌⡰⣈⠲⣈⠆⡱⢀⠃⠌⢡⠐⡉⠄⠂⢌⠀⡃⠌⠀⠥⠀⠠⠀⠂⠐⠀⠂⢁⠐⠈⠀⠄⠀⠐⠀⠠⠁⠀⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣿⣛⡴⡹⣬⣓⢯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⡈⠌⠓⡈⠌⢃⠒⠡⠓⡈⠘⠠⢁⠊⡐⠄⢂⠐⡈⠌⡀⠒⠠⢈⠁⢂⠡⠐⢠⠁⡈⠄⡁⠀⡐⠈⢀⠂⠁⠈⠐⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⣿⢇⠾⣱⢣⡟⣺⢼⣿⣻⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠁⠈⠀⠀⠀⠀⣀⠀⠀⠀⢀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠙⠛⢦⡄⠠⠀⠄⠂⠄⢀⠀⠄⡀⠀⠀⠈⠈⠁⠀⠀⠀⠉⠈⠉⠑⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠤⠒⡀⠈⡌⠡⠃⡉⠘⠠⢀⣄⣴⠶⠈⠐⠀⢄⣀⠈⠀⠖⠀⠤⠲⠛⠾⢷⣶⣄⡀⠀⠀⠀⠀⠀⠘⣷⠄⢁⡘⠐⠌⠠⠊⠔⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠡⢀⠰⠀⠀⠒⡀⢒⠂⢁⠈⠀⢀⠈⠁⠀⡁⠆⠠⠁⣶⡿⠋⠁⠀⠀⠀⠀⠀⠙⠻⣧⠀⠀⠀⠀⠀⠙⠷⢌⠛⠿⢷⣦⣤⣀⣀⡀⡈⠆⡀⢐⠨⠠⠁⠈⢐⡀⠢⠄⠤⣀⠤⡰⢊⠍⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠀⠀⠀⠀⠀⠀⢄⠂⠄⠀⠁⠀⠉⠒⠌⠤⠀⡄⢀⠀⢀⠓⠈⠄⢡⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠂⢠⣈⠹⡭⢉⠡⠐⠠⡁⢌⠢⡑⣀⠀⠠⢀⠂⡌⡒⡄⠆⠱⠆⠤⢄⠢⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠄⡈⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠠⠄⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢨⠐⠡⠌⢂⠆⡁⢄⡮⠑⠂⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⡐⠀⠁⠀⠀⠀⠀⠀⠀⠀⠘⠀⠐⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣷⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡐⠈⠄⠂⠌⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢀⣼⣿⣯⣽⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡔⠠⠁⠌⡐⢈⠀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⠁⠂⠀⠀⢀⠠⡀⠀⠄⠀⢠⣴⣾⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠰⢦⡦⠐⢀⠂⠄⠛⠀⢠⡇⠐⡀⠠⢈⠠⣽⣻⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠀⠀⠀⠀⢠⣿⣿⣷⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠹⣿⣦⡀⢮⡀⠀⠀⠀⡂⠀⠄⠁⣀⠀⠙⣿⣤⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⡰⠁⠀⠀⠀⠀⠀⠀⣾⣟⡌⡟⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⠹⢿⣎⠱⡀⠀⠀⠱⠀⠀⠐⢰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠐⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⣼⣿⣿⣿⠿⣟⡻⣟⡹⢋⢛⠻⠻⠟⡛⢩⠋⡝⢛⢿⣿⣿⣿⣿⡄⠀⠀⠈⣿⣷⣤⠀⠀⢈⠇⠐⠠⢸⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⡀⠉⠙⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⢭⡻⣜⡳⢧⡘⢆⡩⠒⡍⢒⡌⡂⢅⠂⠍⢢⠽⣿⣿⣿⡇⠀⠀⠈⠀⠉⠙⣿⡆⠀⠠⠈⢀⢡⠀⠀⠀⠀⣰⣿⡁⣠⡴⠞⠉⠉⠀⠀⠈⠙⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡿⣿⣿⣿⣟⡲⣝⠶⣹⢖⡹⢦⡑⢣⢘⠢⢌⡱⠀⠌⡘⢠⢋⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⠃⢀⠡⠃⠀⠂⠄⠀⠀⢀⣿⣿⠛⠉⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠢⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⢧⣻⣾⣿⣷⣿⣷⣷⣼⣄⠪⣔⣣⣦⣁⡌⢠⢃⡜⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠌⡐⢀⠢⢁⠊⠈⠀⠀⣠⣾⠟⢣⡄⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠒⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣛⢿⣻⣽⣯⣿⣿⣿⣿⣿⢅⠻⣿⣿⣿⣿⡿⣷⣾⣿⣿⠏⢨⡄⠀⠀⠀⠀⠀⢘⡄⠀⠠⣁⠂⠡⠀⣿⡿⠁⠈⢆⠐⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡙⠻⣿⣯⣟⢻⡛⢻⣹⣿⣿⣿⡎⠱⡠⠿⠿⠿⣿⠿⣿⣿⡋⠀⠘⠁⠀⠀⠀⠀⠀⣨⣟⠀⠡⠐⠀⠁⣼⣿⠃⠀⠀⠈⢶⣥⠂⠀⠀⠀⢀⡄⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⠐⡀⠁⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢤⣌⢹⣿⡁⠀⠀⠀⠀⠀⢸⣿⣏⠷⡓⣰⣿⣿⢻⣶⣽⣷⣟⡻⣿⣿⢇⢣⡁⢃⠄⡃⠄⡌⡙⣻⣷⡖⠘⠃⠀⠀⣤⣤⣼⠟⠁⠀⠸⡄⢀⠠⣿⡃⠀⠀⠀⠀⠈⠹⣧⠀⢴⣾⡏⠄⠠⠈⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⠀⡀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠻⢷⣭⣴⣄⡀⠀⠀⠀⠈⠻⣿⡳⣷⡟⣻⡱⣏⢮⣝⡳⢮⣽⣿⣿⣷⣿⡇⠆⣘⣴⠢⢔⡱⣾⣿⠁⠀⠀⠀⢀⣽⡏⢠⡀⠀⢈⠐⠠⠀⠂⣿⡅⠀⠀⠀⠀⠀⠀⣿⣠⠾⠛⠀⠀⠀⠀⠃⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠙⢻⣷⣶⣶⣴⣶⣿⣿⣿⢿⣷⣓⢮⡳⢮⣝⣻⣛⢛⠛⡩⢁⠃⣞⢡⠊⡔⣪⣿⣟⣁⢀⣠⣤⣶⠟⠃⠀⠁⠀⠀⢈⠡⢂⠡⠈⣿⡃⠀⠀⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠈⠂⠄⠀⠣⠀⠂⠀⠀⠀⠀⠀⠄⡀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠴⠛⣠⣶⡿⠿⠛⠶⣶⣭⣿⣿⠉⣿⣾⣿⣯⢶⡹⢧⣿⣿⣿⣿⣿⢷⣾⣿⡇⢆⣩⣲⣿⣿⣿⣿⣿⣿⣭⣤⣀⡂⠄⡀⠀⠀⠠⠂⠄⢂⠁⢿⠁⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠁⠀⠀⠀⠀⠀⢹⣿⡇⠀⢹⣿⡹⢿⣧⣛⡳⣜⢶⡳⢞⡠⢃⠆⡒⢌⢲⣼⡿⢻⣿⣿⠏⠀⠀⠈⠉⠛⢿⣶⡀⢂⠀⠠⠙⡄⢂⠈⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⢰⣿⣿⣎⢷⣭⣳⣮⣹⢣⢍⡰⢉⢆⣱⣾⣿⣿⣠⣾⠟⢹⣦⠀⠀⠀⠀⠀⠀⠙⣿⣤⡈⠐⡀⠒⠠⢈⠰⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠐⠁⠈⠐⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⢸⠋⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠁⠀⠀⠀⠀⠀⢀⣤⣶⠿⠏⠀⠀⣸⣾⣿⡟⣬⣛⢾⣿⣷⣿⣾⣶⣷⣾⣿⡻⢛⣿⣿⡟⠁⠀⠀⢹⣧⣀⠀⠀⠀⠀⠀⠈⠛⢿⣦⠀⡁⠆⡀⠆⠀⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⢀⡔⠀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣷⣀⣠⣶⡟⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⣸⣿⣏⡾⠁⠀⢸⣿⣿⣿⣛⠶⣹⢮⡹⣿⣿⠿⣛⠻⣉⠧⣑⠃⣿⣿⡯⠀⠀⠀⣤⡜⢻⣿⡆⠀⠀⠀⠀⠀⠈⢿⣇⠠⠐⡀⢂⠀⣠⣴⣿⠟⠙⣶⡀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠛⠉⠁⠈⢫⣍⣿⠁⠀⠀⠀⠈⠛⢷⣄⠀⠀⠀⠀⠈⢹⣆⠀⠀⠀⢀⣾⣿⣿⠋⢀⣠⣶⣿⣿⣧⣽⣭⣛⣵⣎⢷⣻⡏⡖⣩⠒⡥⢆⡱⢬⣿⣿⣷⣄⠀⠀⠈⢿⣧⢸⣷⡀⠀⠀⠀⠀⣰⣿⠇⡐⠠⠐⡀⠂⣭⡟⠃⠀⠀⠻⠿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠐⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠘⣿⡏⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠈⢿⣷⣤⣤⣿⣿⣠⣽⣷⣿⣿⡟⢰⣿⣛⠛⠛⠛⣿⣿⢧⡻⡽⡸⢤⡟⣌⠣⢆⣽⡿⠁⣿⣿⣶⡀⠀⠀⠻⣇⡻⣷⣄⠀⠀⣸⡟⠁⠀⠄⡁⠢⢀⣷⠉⠀⠀⠀⠀⠀⣠⣤⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⡀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢺⣿⣿⣿⣿⣿⣿⣿⣧⣳⢱⡙⢾⡑⢬⣸⣾⡿⠁⢰⣿⣿⣿⣿⣷⣦⣤⣀⡉⠉⠄⢀⠲⠋⠀⠀⢁⠊⠄⠡⢀⡎⠀⠀⠀⠀⠀⠀⢈⣿⠃⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⡁⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⣀⠴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢻⡗⠒⠀⠀⠉⠘⣻⣏⢀⣠⣶⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⣸⣿⣿⡷⣻⣿⡟⣿⡷⣭⢲⡙⢦⣹⣾⡿⠋⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣂⠐⠀⠀⠌⡠⠈⡐⠀⡍⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢂⠀⢂⠀⠄⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠂⠀⠀⢻⡄⠀⢠⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣼⣿⣿⡿⣽⣿⡇⣍⠳⣜⣧⣿⣿⡿⠋⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣌⡑⠛⠦⢡⡆⠀⠀⠀⠀⠀⣾⡏⠠⠀⠐⠀⣤⣤⠀⠀⠀⠀⠀⠀⠘⠄⣈⡐⠀⡀⠀⠀⢀⡀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⢀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢨⣽⣿⣿⣿⣻⣿⡇⣬⣷⣿⣿⠟⠋⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡘⠀⠲⠄⠀⣠⡟⠀⠄⠁⠀⠀⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠑⠂⠀⢀⠀⠀⠀⠀
		⢀⣤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠄⢂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣷⣿⣟⠉⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⢫⠄⠐⠨⠄⠀⠀⠸⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡀⠀⠈⠀⠁
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠐⡈⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⡀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠈⠄⢡⠀⠀⠀⠀⠀⢻⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣟⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠷⣭⢛⡼⡱⢎⡿⢿⣿⣿⣿⣿⣿⡇⠀⠈⠒⣧⡄⠀⠀⠀⠀⢿⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢟⠠⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢋⠾⣿⣷⣶⣥⣭⣙⣛⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⡽⣆⠿⣰⣙⢳⠺⣝⣿⣿⣿⣿⣿⣷⠀⠀⠐⠘⠻⣧⠀⠀⠀⠘⣭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⡞⠁⠰⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⡡⢲⣷⣮⣭⣛⣙⠻⠿⢿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⡳⣜⠣⡵⣈⠎⡝⢦⣻⣿⣿⣿⣿⣿⠀⠀⢀⠂⠁⣿⡇⠀⠀⠀⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠟⣿⣿⠋⠀⠀⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠠⠑⣠⣿⣛⠛⠿⠿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⡫⡕⢦⡑⢎⣙⢮⣿⣿⣿⣿⣿⡿⠀⠐⠌⠐⠈⢹⣷⡀⠀⠀⢠⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠐⡀⠀⠀⠀⡀⠐⡈⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⣼⣿⠃⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣠⡁⣼⣿⠿⣿⣿⣿⣶⣶⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡵⣋⢦⡙⡜⣬⢻⣿⣿⣿⣿⣿⡇⠀⠀⠀⠁⠀⠀⠸⣷⡀⢂⠡⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠀⡐⠀⡁⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⣤⡾⠛⠁⠀⠀⠠⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣷⣾⣶⣭⣝⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣭⢆⢳⢸⡱⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠻⣿⣄⠐⠀⠀⠁⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⡀⠀⠄⠀⠀⠀⡀⠀⡀⠀⠀⢀⠀⡀⠀⠀⠀⡀⢀⣾⣿⣤⣤⣤⣤⣄⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣯⣿⣛⡟⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣷⣊⢎⠶⣹⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠖⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠄⡁⢀⠂⠁⠀⠀⠀⠀⠁⠈⠀⠀⠀⠉⠙⢿⠀⠀⢻⡀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣿⣿⡿⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣞⡬⢳⢭⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠆⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠄⠀⠈⠓⠤⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠻⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣯⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⢈⠐⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠂⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⡿⣿⢿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠁⠀⠀⢠⣶⠆⠀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠁⠀⣬⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢯⡵⢫⢶⣽⣮⣷⣽⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢀⣾⠟⠀⠀⠄⠐⣨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣻⢞⡼⣙⢮⡝⣹⢫⡟⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⣀⡴⠋⢁⠠⠀⠀⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠐⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡷⣏⢿⡹⣝⡻⢞⢧⡳⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣌⠁⠌⠄⠀⠀⠀⢌⠀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⢊⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡽⣞⣯⠷⣯⣽⣯⣾⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠈⠄⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡽⣝⣮⣗⢧⣳⢧⣾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⢈⠀⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠠⠁⢂⠀⠁⠉⠀⠁⠀⠁⠀⠈⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠠⢀⠐⡀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠡⠀⠌⡁⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢀⠃⠌⡐⢠⠃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠌⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠉⠋⢩⠉⠔⡠⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠁⠘⠠⠁⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⢂⠈⠲⢷⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠂⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡈⠄⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⢃⠸⢌⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⡐⠈⠀⠀⠀⠁⠈⠠⠁⢀⠀
		⠀⠀⠐⠰⡀⠐⠀⠐⠈⠄⠈⠄⠂⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⠄⡈⢖⡨⢚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠿⠻⠿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⠀⠀⢈⠡⡐⠠⠈⠄⠈⡀⢁⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢐⠀⢆⡡⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠁⢀⠀
		⠀⢀⠢⢁⠐⡀⠁⡀⢂⠀⢂⠀⠄⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠡⠀⠊⠠⡑⠬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⢈⠀⠀⠀
		⠀⡀⠂⠌⡐⡀⠆⡠⠄⡌⠄⡌⡐⢈⠄⠂⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠘⡠⠀⢌⠱⢄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣳⢯⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠈⠀
		⠄⠤⢉⠰⠠⠑⣈⠐⠌⡐⢡⠂⡁⠎⡐⢀⠀⠀⠄⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⡱⠀⠌⡀⢇⠢⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡷⣯⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠐⠀⠀
		⢈⡐⠂⡅⢂⠁⠄⡈⢐⠠⡁⢆⠁⢆⠡⠀⠄⡈⠐⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠒⢠⠐⢂⠘⠦⡁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣷⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠄⡠⠡⢀⠆⣉⠒⡈⢐⠢⡑⠄⢊⠔⠂⡌⢐⠠⠁⠠⢈⠐⢀⠀⠀⠀⠀⠀⠀⠀⡀⠐⠀⠄⠂⡜⠠⢈⠤⢉⠂⠡⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣯⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡐⠠⡁⠆⠌⠤⡁⠆⠡⢂⠱⡈⠆⡘⠰⡈⠄⢠⠈⡐⢀⠀⢂⠀⠈⠄⢈⠐⡀⡐⠠⠁⠌⠐⡡⠐⡁⢂⠐⠂⡍⠐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣾⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠄⡑⢄⠃⢌⠰⡐⢈⠡⢂⡁⠒⠤⢁⠃⡔⢡⢂⡑⠐⠌⡘⢠⠈⡔⡈⢐⢂⠰⣀⠁⢂⠐⡀⠠⢁⠐⠀⠌⠐⠀⠡⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣳⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡘⠰⡈⡔⡈⢆⡱⢠⢊⠴⣈⠱⣀⠣⡘⠠⣁⠢⠐⡉⠄⡁⠢⠑⡀⠐⡌⠂⠐⠀⠈⠀⠄⠠⢁⠂⡐⠈⠀⠐⠈⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡾⣽⣻⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
		⠁⡃⠑⢂⢉⠂⡑⢃⠊⡒⢁⠃⠤⢁⠐⠡⢀⠂⠡⠐⡐⠠⢁⠒⡀⢃⠐⡀⢂⠐⡈⢀⠂⠄⠀⡐⢀⠂⠁⠈⠀⠀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠾⣝⣳⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠉⠀⠀⠀⠀⠀⣠⠀⠀⠀⡀⡀⠀⢀⣤⠀⠀⠀⡀⠀⢀⡀⣀⠀⠀⠀⠉⠀⠁⠀⠀⠀⠀⠀⠀⠈⠁⠉⠓⢦⡀⠄⠠⢀⠂⠄⢀⠀⠄⡀⠀⠀⠉⠈⠁⠀⠀⠀⠉⠉⠉⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⡀⠤⠒⢁⡀⢉⠌⠡⢁⠉⡐⢬⣤⣾⡟⠂⠉⠐⣀⠀⠉⠐⠒⠀⠠⠐⠒⠒⠲⣤⣄⠀⠀⠀⠀⠀⠀⠈⢷⠀⠡⠐⡨⠐⠄⡊⠔⣀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡀⠀⠀⠀⠀⠀⠀⠀⢈⠠⠐⠠⠀⠄⠒⡀⠖⡁⢊⠀⠀⠐⠀⠈⠀⣈⠐⡀⢂⣼⡟⠋⠁⠀⠀⠀⠀⠈⠙⠻⣆⠀⠀⠀⠀⠀⠉⠖⠤⠙⠻⠤⣄⣀⡀⢀⠀⢠⠃⠠⠑⡠⠡⠀⠐⠠⠄⠒⢠⠠⣀⠤⡔⢊⠅⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠀⠀⢌⠐⡀⠀⠂⠁⠙⠐⠊⠤⠄⡌⠀⠀⣀⠣⠐⢠⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀⠀⠀⠀⠀⠄⠂⡐⣠⠢⢍⠠⢉⠀⠌⡄⠣⡐⢡⠂⢀⠀⢂⠁⣂⡔⣠⠒⠜⠆⠤⣐⠠⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠐⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠠⢀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢈⡐⠈⠤⠑⡈⠄⣈⡔⠎⠀⠋⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⢈⠡⢈⠐⡹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠤⣁⠂⡐⢀⠂⠄⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠂⠈⠀⢀⣠⣤⣤⣴⣀⡄⢿⢶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⡤⠶⠂⠐⠠⠐⠙⠀⢀⡆⠐⡀⠠⠌⠀⣽⣻⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠊⠉⠁⢀⣤⣴⣾⡿⠿⢿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢷⣶⣥⡈⢴⡀⠀⠀⠀⡁⠀⠁⠀⢂⠀⠙⣿⣤⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠁⠀⢀⣴⣿⣻⣷⣿⢿⣿⣿⣿⣿⣿⣿⣿⢿⣶⣤⣄⡀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠈⠛⢿⣬⠳⡄⠀⠀⠱⠀⠀⠁⢸⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠘⠲⣤⣀⠀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣶⣀⠀⠰⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣤⡀⠀⡘⠅⡈⠰⢨⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⣀⢉⠹⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣦⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣯⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣷⡆⠀⡀⠄⢀⠣⠀⠀⠀⠀⣰⣿⡁⣠⣴⠞⠉⠉⠀⠀⠈⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⢠⠘⠠⠀⢂⠀⠀⠀⠀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢺⣿⡇⡚⣭⣿⣿⣿⠿⡿⢿⠿⣿⠿⣛⠻⠩⡍⢭⢉⡛⠿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡁⠂⢌⠂⠅⠀⠀⠀⣠⣾⡟⢣⡄⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⣾⣿⡛⣧⢚⡵⡹⡌⠖⡤⢣⠔⣣⠓⣌⠂⠃⡜⢌⣻⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠠⢊⠄⢃⠀⣿⡿⠁⠐⢆⠘⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⢀⡀⠀⠀⣷⣄⡀⣸⣿⣿⣿⢧⣙⢮⡹⣖⡱⢏⡜⡰⢃⠞⣰⠃⡌⠠⢁⡐⢊⣼⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⠀⢁⠂⠌⠀⣼⣿⠃⠀⠀⠈⢷⣼⡀⠀⠀⠀⣀⡤⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⠡⠀⠀⢿⣎⠹⣿⣿⣿⣿⣧⢫⣞⣵⣮⣝⣪⣔⢣⢍⣚⣤⣣⣤⣁⣆⣐⠣⢾⣽⣿⣿⡟⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⠟⠁⠀⠬⡄⠀⠈⣿⡃⠀⠀⠀⠀⠈⠹⣧⠀⢶⣿⡏⠄⠠⠐⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠌⠀⠁⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⣟⠀⠀⠀⠀⠀⠈⠻⣷⣿⣿⣿⣿⣧⣿⣿⡟⢿⣻⣿⣿⣿⡆⡍⢿⣿⣿⡿⣟⠿⣿⣶⣾⣿⡟⡁⠄⡀⠻⣷⣄⠀⠀⠀⠀⠀⠀⢀⣿⡏⣤⠀⠀⢀⠒⠠⠈⡐⣿⡅⠀⠀⠀⠀⠀⠀⣿⣤⠿⠛⠀⠀⠀⠀⠃⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⠏⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣟⠘⢿⣿⣿⣿⢿⣿⣛⢯⣿⣷⠘⡆⡛⠟⠿⡿⠟⡶⣉⣿⣿⣧⡿⠷⣶⣦⣽⣿⣦⣀⢀⣀⣤⣶⠿⠋⠉⠀⠀⠀⠈⢡⠃⡐⠀⣿⠂⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⣤⡾⠻⣿⣿⡇⠘⡄⣿⣿⢬⡳⢞⣻⣿⣾⣿⢃⢒⢩⣌⣱⣦⣋⠐⡔⢻⣿⣹⣿⠄⠀⠈⠻⣿⣹⣿⣿⣿⣯⣤⣐⡀⠦⣄⠀⠀⠐⢂⠘⡀⢁⠛⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢀⣴⡿⣿⣯⡐⠌⣿⣿⢎⡽⢫⣖⣧⣿⣶⣾⣾⣿⠟⣋⢙⡣⠿⢌⢢⣙⣿⡏⠀⠠⠀⠀⣿⣿⡟⠁⠀⠉⠉⠛⢿⣶⣀⠃⠠⠈⠆⡡⠐⡀⠋⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠏⠀⣘⢿⣿⣤⢻⣿⣏⣞⣳⣾⣿⠿⡛⠭⡑⢌⠒⡤⠿⡑⣌⢊⣵⣿⠟⠀⠀⢀⣠⣾⠿⢻⣇⠀⠀⠀⠀⠀⠀⠙⣿⣦⠁⡐⠈⠤⠁⠄⢡⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠁⠊⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠸⣿⡀⠀⠀⠀⢸⡋⢻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠁⠀⠀⠘⠉⠈⢹⣿⣶⣿⡷⣪⣽⣿⣶⣿⣼⣷⣾⣾⣼⡶⠱⡐⣬⣿⠟⠁⠀⣠⣶⡿⠋⠁⠀⠙⢿⣦⣄⠀⠀⠀⠀⠀⠈⠻⣿⣴⠈⠠⠁⠌⡰⠀⠀⠀⢀⣠⣿⡇⠀⠀⠀⠀⢀⡴⠂⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣹⣷⣀⣠⣾⡟⠁⠀⠛⣷⡄⠀⠀⠀⠀⠀⠈⢿⣇⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣷⣓⢮⡽⢭⠯⡽⡍⠦⣁⠦⡑⡱⣾⣿⡏⠀⢀⣼⠿⣉⣀⣴⠞⠙⠛⣾⣍⢿⣿⡄⠀⠀⠀⠀⠀⠈⢿⣧⠀⡁⠂⡁⢀⣠⣴⣾⠟⠹⣷⡀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠋⠁⠉⢫⣅⣿⠁⠀⠀⠀⠘⠻⣷⡄⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀⣠⣾⠿⠟⣿⣯⣿⣿⣾⣜⣫⣞⣱⣌⠱⡠⢎⣱⡯⢿⣿⣷⣶⡿⠋⣰⡛⢻⠁⠀⠀⠀⠈⢿⣦⡹⣷⡀⠀⠀⠀⠀⣰⣿⠓⣤⠀⡡⠐⣈⣽⡿⠃⠀⠀⠻⣿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠈⠐⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⢸⣟⠀⠂⠀⠀⠀⠈⣿⣿⣄⣠⣿⡏⢠⣴⣿⣿⣿⣏⣛⣿⡛⢛⠿⣿⣿⣶⣽⣷⡘⠼⣿⡟⣿⣦⡄⡿⠀⢸⠀⠀⠀⠀⠀⠈⢻⣧⠛⠿⣄⠀⠀⣼⡿⠁⢀⠠⠁⠒⢷⣿⠋⠀⠀⠀⠀⠀⣴⣹⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⢀⠀⣸⡟⠀⠀⠀⠀⠀⠀⣼⡏⠉⠟⢃⣶⣾⣿⠇⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⡟⣩⠒⡌⡒⣿⣿⣿⣿⠁⠀⠀⢻⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠁⠀⠾⠋⠀⠀⢢⠐⠠⠁⢸⣿⠀⠀⠀⠀⠀⠀⢘⣿⠇⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⡁⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⢠⠴⠟⠁⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⢿⣇⠒⠉⠛⠛⠛⢻⡿⠀⠀⢃⠀⠀⠸⠟⠓⢣⡼⠿⢫⣿⡿⢨⣿⣿⣧⢻⣿⣿⣯⣿⣿⣿⣷⢠⠓⡄⠳⣼⣿⠙⣿⣷⣄⡀⠹⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⡄⣘⠤⠀⡄⠀⠒⡈⠡⠌⢀⣿⠀⠀⠀⠀⠀⢠⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢂⠀⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠈⣧⠀⠈⢿⣆⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣴⣿⣿⡇⠰⣿⣿⣧⢿⣿⣿⣿⣿⣿⢻⣿⡆⠭⣐⢣⣿⡏⠀⣿⣿⣿⣿⣶⣤⣀⠀⠃⠐⠂⠀⠀⠀⣽⢣⠉⠀⠁⠐⠠⠑⡈⠔⡈⢀⢫⠀⠀⠀⠀⠀⣼⡟⠀⠄⠠⠀⣤⣴⡀⠀⠀⠀⠀⠀⠘⠄⢂⠌⡀⢀⠀⠀⣀⠀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠀⠀⢸⡁⠠⠈⣿⡆⠀⠀⠀⢸⣧⠀⠀⠠⢆⢠⣠⣴⣶⣿⣿⣿⣿⣿⡇⠀⢹⣿⣯⣿⣿⣿⣿⣿⣿⢹⣿⡇⡓⣼⣿⡟⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⣀⠻⠂⠀⠀⠀⠀⠀⠆⡁⠂⡐⠢⢁⠀⠀⠀⠀⣠⣿⠃⢈⠄⠀⠀⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⡀⠀⠀⠀⠀⠀
		⢀⣄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡏⠀⠀⠀⠘⣿⡄⠁⠸⣿⡀⠀⠀⢸⣷⢠⡾⣤⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣼⣿⢣⣽⣿⡟⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⣷⣦⣐⠠⢀⠃⠀⠀⠀⢀⣿⡏⢀⠂⠀⠀⠀⠸⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠈⠀⠁⠂
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠼⠃⠀⠀⠀⠀⣿⡇⠀⠀⠙⡁⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣴⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⡄⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⣈⠉⠇⡠⢎⠀⠀⠀⣼⡟⠙⢦⡌⠀⠀⠀⠀⢻⣏⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠟⢻⣀⢤⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⣿⠆⠀⠀⠈⠙⣿⡛⢟⣿⣿⣿⠟⠁⠀⠀⠐⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢹⠃⠀⠀⠤⠛⠀⠀⠘⢿⣄⠀⠀⠀⠈⢿⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡇⠀⠀⠀⡐⢣⠙⢼⣿⠏⠁⠀⠀⠀⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠡⠀⠀⡀⠌⠀⠀⠈⢈⠻⣶⡀⠀⠀⠈⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠈⢀⠀⠀⠀⠀⠀⠀⠄⠁⠀⢀⣴⣿⡇⠐⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡟⣀⠂⣼⣿⣵⣦⣦⣤⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠠⠓⠀⠀⠀⠀⠂⠠⢹⣇⠀⠀⠀⠰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠠⡿⣿⡿⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠂⣿⣿⣛⣛⣻⣙⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠤⠁⠀⣤⠰⠄⠁⠂⠹⣯⠀⠀⠀⡰⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠠⠀⠀⠀⠀⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢠⣷⡿⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣤⣐⠄⣿⣟⣛⣛⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠙⣯⠐⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠁⡀⠈⠄⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⢀⣴⡿⠋⠁⠀⢠⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣝⣻⣿⣮⡿⢟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠙⠀⠐⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠡⠈⠀⠂⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⡀⠐⠀⠀⢀⠀⡀⠀⣀⠀⠀⠀⡀⠀⠀⠀⢈⡳⢀⣿⣿⣤⣤⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⢿⣿⣿⢿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠄⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠄⡁⢀⠁⠀⠀⠀⠁⠀⠈⠀⠁⠀⠉⠉⠙⣿⡁⠘⢿⣄⠀⠀⠀⠀⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣶⣾⣿⣿⣭⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠒⠀⠒⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠆⠐⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠈⠻⣷⣄⡀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣼⣿⣯⣜⣹⣯⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣯⣛⠟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡈⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢀⣙⠛⠃⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⣿⣿⣻⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⠻⡿⣖⣧⡹⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⠡⠀⠂⠠⠀⠀⠀⠀⠀⢀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠁⠀⡉⠘⢿⣇⠀⢀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣶⣿⣴⣩⢶⡹⢵⡺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⣀⣿⡏⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠡⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⡁⠀⠈⢿⣧⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣵⣮⣙⡛⡿⢷⣯⠷⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠂⡀⠀⠀⡐⠄⢀⣴⠟⢉⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠄⠀⠀⠀⠛⢿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⡛⡿⢿⣷⣿⡼⣜⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠱⣀⠂⠌⡀⡾⠍⠀⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⢃⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠄⠠⠄⠀⠀⠀⠀⢈⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣵⣫⣎⡵⣻⢼⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢈⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣾⡽⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⢇⠈⠀⠀⠀⠀⠀⢈⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡀⠄⠈⠀⠉⠀⠁⠈⠉⠈⠀⠀⠀⠁⠀⠀⠠⠈⠄⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣳⣟⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠄⡈⠄⠂⡄⢀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠂⠀⠀⠀⣂⠐⠈⠔⣀⠂⠄⠀⠀⠈⠠⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠡⣇⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⡀⠀⠀⠀⠀⠀⠈⠰⢀⠂⢀⠈⠄⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡜⢻⣿⣿⣿⣿⠟⣥⣷⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠤⡈⠄⣈⠰⢁⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⣿⣿⠛⣭⣶⡿⣟⡱⡝⢮⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠐⠠⠂⠌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡐⠄⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣾⣿⡻⣜⢦⡝⡼⢣⡳⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠂⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⢹⣿⣟⢾⡹⣎⠷⡮⣕⡫⢵⢺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠂⠀⠀⠁⠀⠀⠈⠀⠁⠈⠄⠀⡀
		⠀⠀⢈⢂⠁⠂⠠⠐⠠⢀⠁⠂⠁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡩⠉⣿⣟⡮⢿⣹⠯⣕⣣⡝⣮⣓⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⠀⠠⠠⠌⠠⢀⠂⡐⢀⠀⠠⠈⠄⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⣷⣆⢻⣿⣿⣭⢳⣻⢮⡗⣮⡵⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠠⠈⢀⠠⠀
		⠀⠠⢁⠃⡐⢀⠀⠄⠐⠠⠀⢀⠂⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠇⢹⣿⣿⣯⡷⣯⡽⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠙⠛⠻⠿⠿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⢈⠀⠀⠀
		⠀⡐⢈⠐⣀⠂⡄⢢⠘⠤⡈⠄⢢⢀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠅⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠐⠀
		⢄⠰⢈⠰⢀⠃⠌⡐⠌⢂⠑⡈⠄⡊⠄⡁⠠⠀⠄⠠⠁⠀⠀⠀⠀⠀⠀⠘⢬⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠄⠢⠌⠂⠄⡈⠄⡐⢈⠢⡐⡐⢂⠱⡈⠐⠠⢁⠈⠐⡀⠀⠀⠀⠀⠀⠀⠀⠌⡉⢙⡛⠉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡭⣛⢽⡻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠤⠁⠌⡐⢌⡐⠢⠘⡀⠆⡡⢐⢀⠃⠤⣁⠢⢀⠂⠀⠄⠈⢀⠠⠀⠄⠁⡄⢂⠐⠠⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡙⡶⣹⢧⡿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡄⢃⠰⢈⠤⢈⡁⠆⢡⢂⠱⣈⠂⡩⠐⠤⡀⠄⠠⠁⢂⠀⢂⠀⠁⡈⢀⠠⠁⠂⠁⡈⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡹⣜⣳⣿⣻⡽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
		⡐⠨⢄⠃⡐⢄⠢⠌⡀⠆⡂⠤⠘⡄⣉⠒⠤⡉⠔⡉⠄⠣⢀⢂⠡⢀⠆⢂⠉⡔⠠⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡖⣱⠹⣎⣿⣷⣻⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡌⡑⠢⢌⠰⣈⠆⡤⠑⡬⣐⠡⢒⠰⠠⠉⠤⠑⢂⠡⠈⠆⡁⠊⠄⢂⠰⢀⠂⠄⠀⢢⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣆⠻⣼⣹⡷⣯⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⠡⢉⠂⢃⠘⡘⠐⡩⠐⠡⢉⠂⠡⠑⡈⠄⠡⢂⠡⠈⠔⡈⠡⡐⠌⠀⡀⠂⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡜⢢⢝⡲⣽⡹⢯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠉⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⡀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠓⢤⡀⠄⠠⢀⠂⠄⢀⠀⠄⡀⠀⠀⠉⠀⠁⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠠⠂⠄⡀⢌⠡⠃⠉⠌⡐⢠⢀⡴⠂⠈⠑⠂⢄⠈⠁⠀⠂⠀⠀⠄⠒⠐⠢⢤⡀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠡⠐⡈⠔⠠⠊⠔⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠠⠐⠠⠀⠄⠢⢀⠲⠀⠌⠀⠀⠐⠈⠈⠀⢠⠁⠌⡐⡰⠋⠈⠀⠀⠀⠀⠀⠀⠉⠲⢆⠀⠀⠀⠀⠀⠁⠒⢄⠉⠳⠤⣀⡀⡀⠀⠀⠠⡁⠂⢡⠐⠌⡀⠁⠢⢀⠢⠄⣠⠀⠤⡐⢎⠑⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠀⠀⣈⠐⡀⠀⠐⠀⠉⠚⠌⠤⠁⡄⡀⠀⣀⠃⠌⡐⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡐⣠⠑⠥⢉⠈⡐⠠⡁⠆⡩⢐⠀⡀⢀⠂⠄⣂⢄⢪⠐⠩⠆⠤⢤⠁⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠠⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠌⠐⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⡀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⡄⠑⡠⢁⠆⡁⢂⠴⠡⠈⠂⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠋⠀⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠁⠄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠁⠀⠀⠀⠀⠀⠀⠀⠠⢀⠡⢀⠁⠂⠌⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠴⡀⠂⠌⡐⠈⠄⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠈⠀⣠⣀⡄⢠⠀⠀⠐⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠴⠀⠄⡀⢂⠙⠀⢠⡅⢂⡐⠠⢈⠀⣹⣻⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠐⠉⠒⠶⣷⣦⣦⡐⢠⠀⠀⠀⠀⡀⠀⢀⠀⠄⠀⠙⣿⣤⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠁⠀⣀⣀⣀⣀⣀⣀⣻⣿⣶⣶⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠆⢀⣴⡿⠋⠀⠀⠀⠀⠀⠈⠛⢿⣮⠡⠄⠀⠀⢐⠀⠀⠈⠸⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠐⢲⣤⣀⠀⠹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠀⢀⣤⣾⣿⣿⣻⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣦⡄⠀⢀⣠⣶⣿⣿⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣆⡀⠀⠄⡊⠄⠡⢸⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⣀⠉⠛⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣏⣳⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⠋⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣷⡄⠀⠠⢀⠀⠣⠀⠀⠀⠀⣰⣿⡁⣠⣴⠞⠉⠉⠀⠀⠈⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠄⡑⠂⠈⢁⠀⠀⠀⠀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢁⠂⠰⢁⠊⠀⠀⠀⣠⣾⡟⢣⡀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⣼⣿⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠻⢟⢻⠻⢟⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣀⠀⠡⣈⠐⠂⡐⣾⡿⠁⠐⣂⠑⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⡀⢀⡀⠀⠀⣼⣿⣡⣾⣿⢟⣹⣏⠷⡹⢍⡹⢄⡒⣌⢳⡈⠦⢉⠦⡘⢿⣿⣿⣿⣿⡿⣷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣧⠀⠰⠀⠂⠁⣴⣿⠃⠀⠀⠀⢷⣔⠂⠀⠀⠀⢀⡄⢀⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠈⢧⡀⠀⣿⣿⣿⠿⡑⣾⣿⡿⣷⡕⢮⣐⢣⠚⡽⠙⢆⡑⠠⢂⠍⡺⣽⣿⣿⣿⣗⠀⢭⠙⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⠛⠀⠀⢡⠆⠀⢈⣿⡃⠀⠀⠀⠀⠈⠹⣧⠀⢶⣾⡯⠄⠠⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠂⠀⠁⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⢸⣟⠀⠀⠀⠀⠀⠻⣿⣏⠧⣑⢺⣿⢇⡳⡜⢣⠜⣢⢋⠴⡉⢦⣀⠁⠢⡘⣡⣿⣿⣿⣿⡿⠀⢨⣄⠠⢀⠙⣷⣆⠀⠀⠀⠀⠀⠀⢀⣿⡏⣠⠀⠀⠈⡄⠂⠌⡐⣿⡅⠀⠀⠀⠀⠀⠀⣿⣤⡾⠟⠀⠀⠀⠀⠃⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢈⠇⠀⠀⠀⠸⠀⠀⢹⣿⠳⢌⣮⣿⣿⣿⣿⣷⣾⣵⣾⣷⣿⣾⣿⣿⣷⣶⢡⢚⣽⣿⣿⠏⠀⠈⠻⢿⣶⣦⣼⣿⣧⡀⣀⣀⣤⣶⠟⠋⠑⠀⠀⠀⠑⢈⡁⠂⠄⣿⠄⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠈⠂⠄⠀⠣⠀⠂⠀⠀⠀⠀⠀⢀⠀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠐⠀⣠⣿⣿⢿⣾⣿⣿⣿⣿⣿⣛⣿⢡⢊⠽⣿⣿⣿⣿⠟⠆⠦⢹⣿⣿⡏⣸⣇⠀⠀⠀⠀⠈⠹⣿⣹⣿⣿⣿⣯⣤⣈⡐⠢⢄⠀⠀⠠⢂⠌⢁⠂⡹⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡃⠈⢹⣿⡿⣹⢞⡶⣹⣿⢲⢈⡒⠩⡍⡱⢠⠚⡘⡌⠜⡿⢟⢡⣿⡏⠀⠀⠀⠀⠀⠀⣿⣿⠏⠁⠀⠈⠉⠛⢿⣧⡌⠐⡀⠰⢈⡐⠂⠄⡃⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⢘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣧⣄⣸⣿⣷⠭⣞⡼⣹⣿⣀⣣⣌⣳⣰⡣⡑⠬⡑⢌⠮⡱⢌⣺⣿⠃⠀⠀⠀⢀⣠⣶⡿⢿⣇⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⠡⢀⠒⡈⠄⠰⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠁⠌⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠸⣿⡀⠀⠀⠀⢸⡏⢻⣦⡀⠀⠀⠀⠀⠀⠀⢠⣾⡏⠀⠘⣿⣿⡎⣿⣿⡹⣖⣿⣿⣿⡿⠿⣛⠛⡋⢕⡸⠴⣉⠆⡣⢜⣾⡿⠁⠀⠀⣲⣾⠿⠋⠁⠀⠈⠿⣧⣀⠀⠀⠀⠀⠀⠈⠻⣿⣦⠀⢂⠐⡈⠔⠀⠀⠀⢀⣠⣿⡇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣹⣷⣀⣠⣾⡟⠀⠀⠛⣷⡄⠀⠀⠀⠀⠀⠈⢿⣇⠀⠀⢸⣿⣿⣾⣿⣷⣙⢮⡹⣜⡰⢃⣤⣃⣍⠢⢔⢡⢂⢎⣵⣿⠛⠀⠀⢀⣾⠟⠁⣀⣴⠆⠙⠳⣾⣍⢻⣿⡄⠀⠀⠀⠀⠀⠈⢿⡗⡀⠂⠄⡉⢀⣠⣴⣾⠟⠹⣷⡀⠀⠀⢠⡾⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠋⠁⠉⢻⣍⣿⠁⠀⠀⠀⠘⠻⢷⡄⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⢨⣿⣿⣿⠾⣿⢿⣿⣿⣿⣟⡟⢫⣍⡆⣊⠴⣾⣿⠁⠀⣤⣶⠟⡉⢀⠂⠉⠀⠀⠀⠀⠈⢿⣇⣹⣷⡀⠀⠀⠀⠀⣰⣿⠏⡤⢁⠂⡐⢈⣽⡿⠃⠀⠀⠻⢿⣦⣤⣿⠃⠀⠀⠀⠀⠀⠀⠐⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⣿⣷⣄⣠⣿⣿⣿⣿⣟⡬⢿⣿⢉⣜⠛⠛⠛⠛⣻⣿⣾⣿⣷⣶⣾⠏⡀⢂⡔⠂⠀⢀⠀⠀⠀⠀⠀⠈⢻⣦⠛⠿⣆⠀⠀⣸⡿⠃⢀⠈⡁⠸⢶⣿⠋⠁⠀⠀⠀⠀⣴⣩⣿⠃⠀⠀⠐⠀⠀⠀⠀⠀⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⠀⠀⢠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⢀⠀⣸⣟⠀⠀⠀⡀⠀⠀⣹⠋⢉⠛⠁⣿⣿⣿⣮⣝⣻⣿⡯⣿⣿⣿⣿⣿⣿⣿⢫⣿⣿⣿⣷⡞⠀⠉⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠁⢠⣿⠟⠁⠀⢢⠐⡀⢁⠸⣿⠄⠀⠀⠀⠀⠀⢘⣿⠏⠀⠀⠀⠀⠀⠀⠀⢤⠀⠀⡁⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⡀⠴⠛⠁⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠈⢿⣗⠒⠛⠛⠛⠛⢻⣯⠀⠀⠃⠀⠀⢀⠋⠃⢶⣈⣼⡿⢻⣿⣷⡺⣽⣿⢳⣿⣿⣳⣯⣿⡟⣯⠆⡿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢠⠀⠀⠀⡀⠀⠀⠀⠀⠹⣷⣂⣾⠇⠀⡀⠀⢂⠱⢀⠂⡈⣿⠆⠀⠀⠀⠀⢠⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡐⠀⢂⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⣧⠀⠈⢿⣆⠀⠀⠀⠀⢸⡿⠀⠀⠀⠂⠄⠀⠀⠀⠀⣿⣿⢢⣹⣿⣷⢫⣿⣿⢘⣿⣿⣷⣿⣿⣇⣿⡘⠴⣿⣿⢹⣿⣷⣀⠀⠀⠀⢸⠀⠀⠀⠁⠀⠀⠀⠀⠀⢿⣿⠇⠀⠀⠐⠡⠀⢆⠠⠁⠄⣻⠀⠀⠀⠀⠀⣼⡟⢀⠀⠀⠀⣤⣤⡀⠀⠀⠀⠀⠀⠁⠆⣐⠠⠁⠀⠀⠀⢀⡀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⠀⠀⠀⢸⡀⢈⠘⣿⡆⠀⠀⠀⢸⣟⠀⠀⡐⠂⡐⠀⠀⠀⣠⣿⣿⡖⣹⣿⡾⣝⣾⣿⣸⣿⣿⣿⣿⣿⣇⣿⡬⣹⣿⠃⢸⣿⣿⣿⣷⣶⣤⣤⣀⣀⠀⠀⠀⠀⣠⣤⣴⠿⠁⠀⠀⠀⠈⠀⡇⢀⠂⠁⠦⡁⠀⠀⠀⠀⣰⣿⠃⠠⠈⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⡀⠂⠀⠀⠀⠀
		⢀⣄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡇⠀⠀⠀⠘⣿⡄⠀⠸⣿⡀⠀⠀⢸⣯⠀⢀⠐⠁⢠⣡⣶⣿⣿⣿⣿⠀⡹⢿⣿⡽⣾⣿⣹⣿⣿⣿⣿⣿⣯⣿⣷⣿⡏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣮⣍⣥⠀⠂⠀⠀⠀⢀⠀⢀⡌⢀⠂⠥⢀⠁⠀⠀⠀⢀⣿⡏⠀⠒⠀⠀⠀⠸⣿⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠁⠈⠄
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⣿⡇⠀⠀⢿⣧⠀⠀⢸⣿⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣅⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠈⢳⢆⡈⠰⠀⠎⠀⠀⠀⣼⡟⠁⠌⡀⠁⠀⠀⠀⠘⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠟⠁⠀⠀⢛⠻⣄⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⠀⠀⠻⣿⣿⣿⣿⣻⣟⡛⣿⣿⣿⡟⠁⠀⠀⠈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡌⢱⠂⠈⠔⠀⠀⢀⡛⠀⠀⠂⢱⡀⠀⠀⠀⠀⠑⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠋⠀⠀⠀⠀⣸⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢹⣦⠀⠀⠙⢻⣿⣿⠛⠋⠜⣿⣿⠏⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠱⡀⠄⠀⠀⡀⠌⠀⠀⠡⠂⠻⣶⠀⠀⠀⠈⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠐⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⢀⣴⣿⡇⠂⢌⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢢⠛⠇⠀⠀⠀⠈⠿⠃⠌⢸⣿⠁⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠄⠠⠀⠐⡘⠀⠀⠀⠨⠁⠄⠻⡅⠀⠀⠀⢂⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠂⠈⠀⠁⠀⠀⠀⠈⠀⠀⠈⠀⠀⠀⠀⠀⢠⣿⣿⡿⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡉⣔⣠⣤⣴⣶⣿⠈⠄⢸⣿⣀⣄⣀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠀⠀⠡⠀⠅⠂⠄⢤⠆⠁⠐⠀⠡⢒⠀⠀⠀⣈⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠠⠀⠀⠀⠀⡐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢠⣿⡿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣀⡀⣸⣿⠟⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡁⠐⠀⠈⠈⠀⠀⠀⠀⠀⠀⠉⢂⠐⡐⢈⠐⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠀⡁⠀⠆⠐⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⢀⠀⠀⢀⣴⡿⠋⠁⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠿⠻⣿⣿⣾⡟⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠘⠀⠉⠠⠌⠀⠀⠀⠀⠀⠀⠀⠈⢢⠐⠠⠈⠀⠂⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⠀
		⠀⣀⠀⡐⠀⠠⠀⠀⢀⡀⠀⡀⠀⠀⠀⡀⠀⠀⠀⣀⣤⢀⣿⣿⣤⣀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡐⠈⡀⠄⠁⠀⠀⠀⠀⠁⠈⠀⠀⠉⠈⠙⣿⠄⠈⢿⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣷⣿⣿⣷⣶⣿⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠜⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠤⠁⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⠈⠻⣦⡄⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⣿⣭⣿⣿⣯⣽⣿⣻⣽⣿⣿⣿⣫⢟⠻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⡐⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠈⠈⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⡟⣿⣿⣿⣻⢿⡿⣿⣿⣿⣿⣛⢏⡳⣱⣌⢳⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢠⠀⠀⢂⠀⠠⠀⠀⠀⠁⠀⠀⢀⣴⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠂⡐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠁⠀⠁⠘⠳⣆⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⡿⠼⣬⡑⢧⡚⣬⠓⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⡁⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠂⠀⠀⢻⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡵⣛⠴⣋⣟⠻⢶⡙⡼⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⡀⠀⠀⠀⠠⠀⠐⢆⢀⣠⠟⢋⡐⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠄⠀⠀⠀⠉⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣿⣿⣿⣿⣿⣯⡽⣻⢿⡷⣬⢫⡱⡹⣜⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠙⠀⠀⠀⠀⠀⠘⢢⠈⠠⢀⡲⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢘⠂⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠠⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⡿⣝⣻⣿⣿⣿⣿⣿⣷⣽⣎⡶⢥⡳⣓⠧⣝⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠎⠁⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢈⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢳⡍⣾⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡒⡄⠀⠀⠀⠀⠀⠀⠐⠌⡀⠀⠀⠀⠀⠀⢀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠁⡌⠀⠄⠁⠉⠀⠁⠈⠉⠀⠁⠀⠀⠁⠀⠀⠀⠌⠠⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣧⡻⣜⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠁⠀⠀⠀⠀⠀⠠⢈⠐⡀⠆⢀⠀⠀⠀⠠⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠞⠀⠀⠀⠀⡁⠂⠐⠠⡌⢀⠂⠀⠀⠀⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⢀⡀⠀⠁⠀⠀⠀⠈⠄⡂⠄⡀⠐⠠⡉⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠤⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⡟⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⣐⠠⠠⢁⠂⠥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣏⠲⢌⡜⡹⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠌⠢⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠤⠁⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣟⣼⡶⣉⠖⡸⢰⡑⢎⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⢁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢋⠴⢡⡚⡕⢣⠜⡬⢹⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢀⠂⠀⠀⠈⠀⠀⠈⠀⠁⠈⠄⠀⡀
		⠀⠀⠈⡅⠂⠄⠀⠐⠠⢈⠐⠠⠁⢂⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⡿⢎⠳⡱⢌⢣⠚⡔⢫⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⠀⠂⠤⢁⠠⠈⠄⡐⠀⠀⡀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣍⢧⣓⢎⡥⢋⡜⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠁⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀⠄
		⠀⠠⢑⡈⠄⡀⠀⠄⠠⢁⠀⠀⠂⠌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣮⣽⣾⣼⣳⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠈⠄⢈⠀⠠⠀
		⠀⡐⠠⠐⢠⠐⣀⠢⡐⠢⠄⡁⢆⠠⠐⡀⠀⠀⠀⢀⠀⡀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠠⠀⠀
		⠄⠤⠑⣈⠂⠡⠐⡠⢁⢃⠘⠠⠈⢆⠡⠀⢀⠀⠄⡀⠂⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀
		⠈⠤⠑⡠⢈⠁⠄⡁⢂⠆⡈⠆⢡⠊⡄⠁⢂⠀⠂⠐⡀⠀⠀⠠⠀⠀⠀⠈⢿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠌⠠⢁⡐⢄⠊⡔⠈⡔⠨⢐⠈⠄⡒⠠⢌⠠⢈⠀⡐⠀⢁⠠⠀⡄⡀⠄⠂⠠⠀⠄⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⡱⢎⡵⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢌⠐⡠⢐⠈⠒⡠⠑⢠⠑⠂⡌⠢⠡⢑⠂⡄⠠⠐⡀⢁⠀⡐⠄⠀⠁⠈⢀⠡⠈⠐⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡛⣜⢲⣙⢮⣟⡾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
		⠄⡊⢄⠃⠌⣂⠡⡘⢠⠘⡠⢐⠡⢃⠌⡒⢄⠣⣁⠢⢁⠒⢄⠐⡨⠄⡑⠂⠰⠀⢘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⡹⣌⠧⣎⢷⣫⢿⣽⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡘⠰⣈⠄⢣⠄⣃⠴⣀⠣⡐⢡⢂⠡⢊⠐⢨⠐⡀⠆⡁⢊⠔⡈⠄⡐⠀⠀⠀⠀⢚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠣⢎⡳⢌⡷⣭⡷⢯⡿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠁⠃⠌⢊⢁⠊⠱⠘⢠⠃⡉⠆⡀⢃⠐⡈⠄⠢⠐⠂⠤⢁⢂⠐⢠⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠣⡝⢬⡓⢼⣸⢳⣛⣯⢿⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠓⢤⡀⠄⠠⢀⠐⡀⢀⠠⢀⠀⠀⠀⠈⠀⠁⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⢂⠠⠀⡌⡑⠌⢉⠉⡐⠠⢀⠤⠂⠀⠉⠂⢄⠈⠁⠀⠀⠀⠀⠄⠒⠠⠒⢄⡀⠀⠀⠀⠀⠀⠀⠈⢳⠀⡁⢂⠡⠐⠄⠒⡈⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠡⢀⠡⠂⠐⠰⢀⠒⡀⠐⡀⠁⠠⠀⠉⠀⠐⡈⠄⢂⠰⠁⠈⠀⠀⠀⠀⠀⠀⠈⠐⠆⠀⠀⠀⠀⠀⠁⠊⠄⡐⠡⢄⣀⡀⡀⠀⠀⢠⠂⡐⠈⠤⢁⠂⠁⠰⢀⠡⠄⡠⡀⢤⡐⠎⠉⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠀⠀⢄⠂⡀⠠⠐⠈⠁⠓⠌⠤⠄⡄⠀⠀⢠⠋⢀⠂⣄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠐⠀⠀⠀⠀⠀⠂⢠⢠⠑⡌⠠⢉⠠⠐⡠⢉⠒⡌⢀⠀⡀⢂⠐⣠⢐⡡⠆⠘⠆⠦⢄⠤⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠄⠂⠌⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢀⠀⠀⠀⠀⠈⠀⠈⠁⠀⠀⠀⠀⠂⡄⠃⡄⢃⠌⡐⢠⡡⠒⠀⠉⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀⠀⠈⠄⠀⠁⠀⠀⠀⠀⠀⠀⠀⠉⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⢀⠐⠠⠈⠄⡈⠐⡹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡘⠤⠁⠂⠄⠡⠀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠂⠁⠀⠀⠀⣀⠀⡀⢀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢀⠐⠠⢀⠋⠀⢠⡅⠨⠐⢀⠡⠀⣽⡿⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠉⠀⠀⠀⠀⠀⣀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣀⠀⠈⠒⠶⣶⣦⣤⡈⢐⠀⠀⠀⠀⡀⠁⠈⠀⠄⠀⠙⣿⣆⡈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢾⠃⠀⠀⠀⠀⠀⠀⠀⠁⠒⠀⠀⠹⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣴⡗⣀⣴⡿⠋⠀⠀⠀⠀⠀⠉⠛⢿⣆⠂⠄⠀⠀⢐⠀⠠⠈⠸⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠘⢲⣤⣀⠀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠰⡎⢹⢿⣦⡀⠀⢀⣤⣶⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣄⠀⠀⠄⠆⠁⠂⠼⠀⠀⠀⠀⠹⣷⠀⢀⠀⡀⣀⢉⠛⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣦⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⢀⣠⣴⣶⣶⣶⣶⣷⣾⣶⣶⣶⣆⣀⠀⠀⠀⠀⠈⠷⡶⠟⢻⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⡄⠀⢠⠈⢀⠣⠀⠀⠀⠀⣰⣿⣁⣠⣴⠟⠉⠉⠀⠀⠈⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠃⣀⣴⣿⣿⣟⠳⣆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⣀⠀⣀⣀⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⢀⠆⠂⢀⠂⠀⠀⠀⠀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⣾⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⡙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⠠⢈⠂⡅⠈⠀⠀⣠⣾⡟⢳⡀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠓⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡜⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡁⠀⡀⢃⠄⢂⠐⣾⡿⠁⠐⢆⠑⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⢀⡀⠀⢸⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⢿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⢈⠐⠀⡀⣼⣿⠃⠀⠀⠈⣷⣦⠆⠀⠀⠀⢀⡄⠠⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⠀⠄⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠁⠀⣸⣿⡂⢍⣹⣿⣛⠟⣿⣿⠿⡛⢭⡋⢭⢋⠝⡛⢻⣿⣿⣿⣿⣿⣿⣿⡇⠐⢿⣯⠙⠻⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⠛⠁⠀⢨⠆⠀⢀⣿⠇⠀⠀⠀⠀⠈⠻⣷⠀⢶⣾⡯⠀⠄⠈⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⢀⠠⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠐⣿⣿⢃⠆⣿⡿⣌⠟⡴⢋⡖⣹⠶⣉⠆⡩⢂⢍⠢⢽⣿⣿⣿⣿⣿⣿⡇⠀⠈⢻⣧⠀⠄⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡏⣠⠄⠀⠈⡔⠠⠈⠄⣿⡃⠀⠀⠀⠀⠀⠀⣿⣤⠾⠟⠀⠀⠀⠁⠒⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠐⣿⣏⠈⣿⣿⠷⣩⢞⡱⢫⠞⣩⠛⣄⠚⡄⠂⡄⢣⢊⣽⣿⣿⣿⣿⣿⠀⢀⣤⡼⠿⠿⣶⣧⣼⣿⣆⡀⣀⣀⣤⣶⠿⠋⠉⠀⠀⠀⠘⠠⡁⠌⡀⣿⠅⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⠀⠀⠣⠐⠀⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⢈⣿⣎⣿⣿⣿⣵⣮⣱⣋⣾⣄⣣⢄⡋⠔⡡⠘⡄⢣⣻⣿⣿⣿⣿⣿⠁⠈⠁⠀⠀⠀⠀⠀⠹⣿⣹⣿⣿⣿⣯⣤⣐⡀⠦⠄⠀⠀⠠⠑⡐⠠⢀⠻⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠛⡿⣿⣿⣿⣿⣿⣷⣿⣾⢠⢹⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⠈⠉⠛⢿⣶⡌⠐⡀⠰⠁⠆⡁⠂⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡿⢟⣿⣿⢻⣿⣿⡿⡐⡅⢻⣿⣿⣿⣿⣿⠏⡍⢂⢾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢀⣠⣶⡿⢿⣆⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⢁⠘⠠⠄⡁⢌⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠁⠊⠐⠀⠄⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠸⣿⡀⠀⠀⠀⢸⡛⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣤⣿⣿⡱⢯⣿⣿⢇⡱⢈⢆⣹⣯⡔⠤⢂⢣⠘⢥⣺⣿⡿⠿⣿⣦⠀⠀⠀⠘⣳⣶⠿⠋⠁⠀⠈⢿⣦⣄⠀⠀⠀⠀⠀⠈⠻⢿⣦⠈⡐⠠⠐⣠⠀⠀⠀⢀⣠⣿⡇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣹⣷⣀⣠⣾⡟⠁⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀⠙⠛⢻⣿⡧⡝⣧⣿⣿⣶⣾⣶⣾⣾⣏⠰⢡⢋⠤⣉⢶⠿⡛⣿⣷⣿⠇⠀⠀⢀⣾⡿⢉⣀⡤⠀⠈⢻⣶⣌⢻⣿⡄⠀⠀⠀⠀⠀⠈⣿⡗⢀⠁⠂⠄⢀⣠⣴⣾⠟⠻⣷⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠋⠁⠉⢿⣍⣿⠁⠀⠀⠀⠈⠻⣷⡄⠀⢀⠀⠀⠀⢰⡈⣿⣷⡹⣞⠽⣹⢫⡙⢃⢎⡱⣌⣱⣃⣬⣩⣍⠦⡑⣼⣴⣿⠉⢀⣠⣶⠟⠋⠀⠂⢋⠀⠀⠀⠀⠘⢿⣦⣹⣷⡀⠀⠀⠀⠀⣰⣿⠛⣤⡈⠐⡈⢤⣹⡿⠋⠀⠀⠿⣿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠘⣿⡏⠀⠀⠀⠀⠀⠀⢸⣿⠌⠃⠀⠀⠀⠸⣿⣿⣿⢿⣿⣷⣷⣷⣾⣷⣮⣐⣿⣛⠛⠛⠛⢛⣿⣿⣿⣿⠁⠤⠞⢋⠀⡌⣄⠁⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⠻⣿⣦⠀⠀⣸⡿⠋⢀⠉⠂⠳⣼⣿⠟⠁⠀⠀⠀⠀⣴⣹⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⡰⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⣸⣟⠀⠀⠀⢀⠀⠀⣻⣿⣿⣧⢏⡿⣽⢶⡩⢎⣝⡻⣿⣿⣿⣿⣿⣿⣿⣏⠻⠿⣀⢆⡈⠐⠉⠈⠁⠀⠀⠘⠀⠀⠀⠀⠀⠀⠈⣿⣧⡀⡟⣠⣿⡟⠁⠈⠴⡈⠄⡁⢸⣿⠀⠀⠀⠀⠀⠀⢘⣿⠏⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠡⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⣠⡶⠿⠁⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠈⢿⣗⠒⠋⠛⠛⠛⢻⣿⠀⠀⢀⠂⠀⠰⠟⠃⢿⣿⣯⢷⣙⢮⡱⣋⣾⣳⣿⣿⣿⣯⣿⣿⠙⠻⠷⠀⢾⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣔⣿⡿⡀⠀⠀⠚⢀⠂⠄⢹⣿⡄⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡈⠄⠂⡀⢀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠈⣦⠀⠈⢿⣆⠀⠀⠀⠀⢸⣿⠀⠀⠈⠰⢠⠀⠀⠀⣸⣿⡟⣿⣿⣶⣧⣇⣿⣷⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⡀⠙⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠁⡌⠐⠠⠌⠐⣘⣿⠀⠀⠀⠀⠀⣼⣿⠐⡀⠀⠀⣤⣿⡄⠀⠀⠀⠀⠀⠀⢃⡐⡀⠂⠀⠀⠀⢀⠀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⠀⠀⠀⢸⡀⠁⠘⣿⡆⠀⠀⠀⢸⣯⠀⠀⢈⠂⢡⣄⣰⣶⣿⣿⣟⡾⣽⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⢀⢰⣾⡏⠀⡁⢀⠻⣶⣄⡀⠀⠀⢰⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠉⠀⠀⠀⠀⠘⣇⠐⠈⠄⢸⣿⡁⠀⠀⠀⣰⣿⠃⢂⠀⠀⠀⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⡀⠂⠀⠀⠀⠀
		⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀⠀⠘⣿⡄⠀⠸⣿⡄⠀⠀⢸⣷⠀⢀⠂⣄⣦⣿⡿⢻⣿⣿⢮⡽⡾⡽⣿⣿⣏⣾⣿⣿⣿⣿⣿⣿⣸⡏⢿⣷⣤⡐⠀⢂⠈⠛⢷⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⢁⠀⢌⠀⠀⠀⢀⣸⣏⠠⠁⡈⠰⣿⠀⠀⠀⢈⣿⣟⠀⠌⡀⠀⠀⠘⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠁⠈⠄
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⠇⠀⠀⠀⠀⣿⡇⠀⠀⠻⣧⠀⠀⣸⣿⣥⣶⣾⣿⣿⣿⣿⠠⢿⣿⣯⢷⡻⣝⡾⣹⡧⣿⣿⣿⣿⣿⣭⣿⣿⠁⢸⣿⣿⣿⣷⣶⣮⣤⣀⣀⠀⠀⠀⠀⢀⣴⣿⠏⢀⠰⡀⢌⡀⠀⠀⠀⢸⡟⠁⠄⡂⠄⠡⢞⠁⠀⠀⣼⡿⠁⠠⠈⠀⠀⠀⠀⠹⡇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣹⠏⠀⠀⠀⣀⣼⠟⠁⠀⠀⢄⣹⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠊⢻⣿⣷⢫⣽⢺⠵⡳⣜⣯⣹⣿⣟⣻⣿⡟⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣌⡉⠁⠠⠀⠠⠐⡀⠐⠀⠀⡰⠛⠁⠠⢀⠁⢂⠀⠃⠀⠀⣰⣿⠁⠀⢂⠡⠀⠀⠀⠀⠀⠙⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠀⠀⠀⠀⠀⢰⡟⡟⠀⠀⠀⠘⠟⠁⢠⣰⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡆⠀⠹⣿⣿⣌⢯⡹⢳⡜⣿⡟⠛⠻⣿⡟⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⠀⠁⠊⠔⠁⠀⢀⡒⠄⠂⡀⠖⡄⠀⠀⣾⠃⠀⠀⢢⠀⠻⢤⠀⠀⠀⠈⡐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀⠐⠀⠀⣀⠀⠀⣿⡇⠃⠀⢠⣶⣿⣶⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⠀⠀⠘⢿⣷⣦⢉⠷⣸⣿⡟⣤⡙⣿⡁⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣅⠈⠄⠀⠀⢀⠎⡐⠀⠐⠄⠀⠰⠁⠂⠀⢀⣼⠂⠐⠠⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠀⠀⠂⠀⠀⠀⢴⣿⢀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⡐⠀⠀⠀⠀⠙⢿⣿⣾⣵⣿⠇⠉⢸⣿⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠈⠐⠤⢁⠂⢌⢠⠀⠂⠄⣤⡿⠇⠀⠁⢂⠁⡀⠀⠀⣨⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠠⠄⠀⢀⠀⠐⠠⢁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣸⠏⡺⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣸⣴⣤⣤⣤⣤⣤⣿⡿⠟⠁⢀⣤⣾⣟⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠠⡐⢂⠁⡈⠂⠔⡈⠜⠁⠀⠀⠀⠀⠀⠈⠄⡁⠂⠄⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠀⠠⠀⠄⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣤⣯⡵⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣿⣿⣿⣏⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠈⠄⢁⠂⠄⡁⢂⡘⠀⠆⠀⠀⠀⠄⠀⠀⠀⠐⠠⡁⠘⠀⢀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⠌⠐⠀⠀⠀⢀⡀⠀⠀⡀⠀⢀⠀⡀⠀⣀⣸⣿⡼⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠐⠀⠊⠌⡐⢀⠠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡌⠀⠄⠁⠈⠀⠀⠀⠀⠁⠈⠀⠁⠀⠉⠉⣿⣿⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣬⣥⣹⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠌⢀⠰⢀⠂⡘⠀⠀⠀⠂⠀⠐⠀⠀⠂⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠄⠌⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⣝⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣬⣭⣉⣍⣋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠂⠐⠂⠄⠡⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⢿⣙⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⣛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠐⠀⡱⠈⠄⡁⢈⠘⠦⡄⠀⠀⠀⠀⠀⠀⠀⣠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢁⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⠺⣏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠠⠀⠀⠱⢌⠀⢂⠰⠀⡀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⢀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠸⠆⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠀⠀⠂⠀⡁⠀⠀⢣⠀⠀⠐⣄⠁⠐⢄⡀⣰⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⠈⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡍⠎⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣟⣯⣃⣷⢶⣲⣽⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣟⣻⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠄⠁⠀⠈⠀⠀⠀⠈⠿⣦⡀⢂⠀⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠔⠩⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣘⠢⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣶⣿⣾⣿⢟⡮⣗⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣋⣝⣿⡿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⢂⠀⠂⠁⠀⠀⠀⠀⠀⠙⢿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⢀⠁⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⡿⣯⣛⣮⢗⣯⢞⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡟⣾⡹⢧⣻⠽⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠻⢇⠀⠀⠀⠀⠀⠀⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠁⡄⠂⠀⠀⠁⠀⠁⠀⠉⠀⠁⠀⠀⠀⠀⠀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⣽⣿⣳⣟⢾⣹⢮⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⡵⣏⢯⣳⢻⡵⣻⣿⣿⣿⣿⡆⠀⠠⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⡄⢀⠂⠌⢣⠀⠀⠀⠀⠠⠁⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠘⡄⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣻⣞⡷⣯⡿⣟⡻⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⡞⣭⢳⡭⢷⣫⣟⣿⣿⣿⣿⣷⣀⠀⠀⠀⠠⠀⢀⠀⠀⠀⠀⠁⡐⠄⠈⠰⢀⠂⠁⠀⠀⠀⠡⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡄⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡥⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣽⣳⡽⣞⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡟⡽⡷⣯⣞⠷⣽⢾⣿⣿⣿⣿⣿⣿⣧⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠉⠰⡀⠄⠠⢀⠃⠆⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⠏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣯⣷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣛⡶⣭⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠐⠈⠀⠀⠀⠀⠀⠀⢀⠰⡈⠐⡠⠘⠤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠌⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⡁⠰⢁⠊⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡈⢁⠆⠀⠀⠠⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⡈⠠⢀⠀⠀⠀⢀⠀⠀⠀⠀⡀⠄⠀⠀⡒⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢈⠄⠀⠐⠈⠀⠀⠈⠀⠁⢈⠐⠀⠀
		⠀⠐⡠⠒⠄⠂⠀⠂⠄⡈⠄⠐⡀⠄⡀⠀⠀⡑⢼⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⠈⠀⡡⠂⠄⠂⠄⢂⠀⢀⠀⠄⢂⠐⡀⠐⠠⢸⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⡀⠂⠐⠀⠀⠀⠀⡀⠀⠠⠀⠄⠈⠀
		⠀⢀⠢⢁⠆⢀⠀⠌⡀⢈⠀⠀⠌⡀⠄⠀⠁⠀⠘⢿⣯⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠁⠂⠀⠀⠀⠀⠀⢀⠁⢈⠀⠀⡀
		⠀⡀⠂⠤⡈⢄⡀⢆⡐⠢⡐⢈⠤⠀⠄⢠⠀⡐⢂⠠⠁⢷⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠐⠀⠀⠀⠀⠀⠀⠀⠈⢀⠂⠀⠀
		⠠⠄⡉⠤⠑⠠⠐⢂⠌⡡⠐⡁⠢⡉⠌⡐⠰⢀⠢⣀⠁⠆⡐⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠐⠠⠐⡡⢉⠀⡁⠌⡐⠤⢁⠰⢁⠜⠠⢀⠁⠂⠄⠀⢆⡐⠀⠀⠈⠉⠉⠙⠉⠉⠉⡀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡤⢉⠈⡁⠂⠐⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠈⠄⠡⡐⢨⠐⡁⢊⠔⣈⠢⠐⡈⠆⢡⠂⠌⠐⡀⠁⠀⠐⠃⡄⠠⠁⡀⠐⣈⠠⠡⡄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀
		⢌⠠⢁⠜⠠⢂⠐⠌⡒⢄⠂⠥⡘⠤⢁⠎⡀⡐⢀⠁⠄⡀⢂⠈⠁⠀⠄⠁⠠⠐⠐⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⠿⢿⡟⢿⡻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠄⡌⢢⠈⠔⣂⠉⡔⢨⠐⣈⠰⠐⢢⢁⠢⢐⠡⠌⢌⠒⠠⢃⠐⡌⢀⠎⠄⠑⠀⠈⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠵⣋⠖⣜⢣⡽⣹⢾⣷⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡘⠤⢡⡘⠰⡠⢁⡔⡡⢊⡐⢠⠉⠄⠢⠁⢌⠐⠨⠄⢊⠡⢈⠂⠄⡀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡜⢣⢍⠺⣌⠳⡜⣭⢟⣾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢁⠊⡁⠊⠅⡁⢣⠈⢅⠃⡘⠄⡉⠄⠃⠌⠠⠘⠠⢑⠂⠌⡄⡈⢄⠀⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡍⢖⠪⡵⢨⣛⠼⣌⠟⣞⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠉⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⢠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠓⢤⡀⠄⠠⢀⠂⠄⢀⠠⢀⠀⠀⠀⠉⠈⠁⠀⠁⠀⠉⠉⠉⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⢂⠠⠀⡌⡑⠌⠡⢉⠐⠠⢀⠤⠀⠀⠉⠐⢀⠈⠁⠀⠂⠀⠀⠄⠢⠐⠢⢄⡀⠀⠀⠀⠀⠀⠀⠈⢗⡈⠄⠂⡌⠂⠔⠂⠌⣀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠡⢀⠐⠠⠀⠰⢀⠰⢀⠐⠠⠁⠠⠀⠉⠀⠐⣈⠐⠠⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠑⠢⠄⡘⠢⢄⣀⡀⡀⠀⠀⠰⡀⠄⠡⢄⠡⠂⠈⠰⢀⠒⠤⢀⡄⢤⠰⢊⠅⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠀⠀⠀⠀⠀⠀⢄⠈⡀⠄⠁⠂⠉⠒⠌⠡⢄⡠⠀⠀⢠⠓⠀⢌⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⡰⠰⢡⠉⠌⡐⠠⠌⢡⠂⡜⢀⠀⡀⠂⢄⢂⠆⡬⠠⠙⠆⠤⢄⡡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⠂⠄⠩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⠀⠈⡄⠑⡈⠆⢌⠐⢠⡑⠦⠁⠊⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠋⠀⠀⠀⠀⠈⡐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠉⠄⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠡⢈⠐⡈⠌⢹⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠦⢐⠀⢂⠐⡈⠀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠌⠀⠈⠀⢠⠀⡀⢀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠄⠠⠠⠙⠀⢀⡎⢀⠂⠀⡅⠠⣿⣻⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠉⠀⠀⠀⠀⢀⣀⡀⠀⠈⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣀⠀⠉⠒⠰⢶⣤⣆⡈⠤⠁⠀⠀⠀⠄⠀⠁⠠⢀⠀⠙⣿⣤⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠛⢷⣆⠀⠹⣷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣰⣇⢀⣴⡿⠋⠀⠀⠀⠀⠀⠉⠛⢿⣤⠁⡀⠀⠀⠌⡀⠀⠂⢹⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠘⠶⣦⣀⠀⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆⠐⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠻⢶⣾⣿⣿⣦⠀⠀⢀⣠⣶⣿⣿⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣶⣄⠀⠀⠰⡀⢁⠢⢸⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⣀⠉⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣶⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠀⠀⠀⠀⢠⣤⠀⢀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠉⣿⡽⠷⣶⠿⢻⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⡄⠀⠠⠀⠀⢆⠀⠀⠀⠀⣰⣿⡅⣠⣴⠞⠉⠉⠀⠀⠉⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢱⡆⠀⠀⢀⣀⣤⣶⣶⣶⣦⣤⣤⣀⣠⡇⠀⠀⠀⠀⠙⠁⠀⠀⡴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡐⠠⢁⠃⢈⢀⠀⠀⠀⢀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⡜⠀⣠⣾⣿⣟⢫⠔⣴⣷⣿⣿⣿⣻⣿⣿⣷⣤⡀⠀⠀⣀⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⡐⠨⠐⢂⠀⠀⠀⣠⣾⠟⢣⡄⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠈⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⢀⣧⣴⡿⣿⣿⣿⣾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⠋⠀⠐⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡁⠀⢠⠉⠄⢂⠀⣿⡿⠉⠐⣆⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⢀⡀⠀⠀⣿⣿⣳⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠋⢿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠠⠉⠀⠂⣼⣿⠃⠀⠀⠈⣷⣞⣆⠀⠀⠀⢠⡄⢀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠉⢷⣦⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢧⡀⣠⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣆⠀⠐⢿⣭⠙⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠏⠁⠀⢡⠆⢀⠈⣿⠇⠀⠀⠀⠀⠈⢻⣷⠀⢶⣿⡯⠀⠄⠐⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠂⠀⠁⠂⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠐⡿⣿⣿⡉⢼⣿⣿⢿⣿⣿⣿⢿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠈⢻⣧⠀⠄⠛⢿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡏⣰⠀⠀⠈⡔⢀⠂⠌⣿⡃⠀⠀⠀⠀⠀⠀⣿⣤⡿⠛⠀⠀⠀⠂⠡⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⡯⠀⠀⠀⠘⣿⡿⠁⣐⣾⣿⢣⢞⣫⠓⡌⢦⡘⢄⠣⡐⠄⣉⠻⣿⣿⣿⣿⣿⣿⣿⣧⢀⠀⠸⠻⠿⣶⣮⣼⣿⢀⠀⣀⣀⣤⣶⠿⠋⠉⠀⠀⠀⠡⢈⠄⢂⠐⣿⡁⠀⠀⠀⠀⠀⢸⣿⡏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⡀⠀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⢸⣿⣦⣿⣿⢧⢏⡞⡴⢻⡗⢦⡍⢢⠱⡐⡈⢄⠣⣽⣿⣿⣿⣿⣿⣿⡏⢈⠁⠀⠀⠀⠀⠀⠹⣿⣩⣿⣿⣿⣯⣤⣐⡈⠦⢄⠀⠀⠠⠌⡈⠄⠂⢿⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣿⣜⠲⣍⣳⢉⡒⢌⡡⢆⠡⡘⢌⠲⣹⣿⣿⣿⣿⣿⣿⠀⠈⠃⠀⠀⠀⠀⠀⠀⣿⣿⠏⠁⠀⠈⠉⠛⢿⣶⡌⠀⠄⠠⢃⠔⡈⠄⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⢘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡿⣾⣿⣷⣾⣦⣴⣊⡱⢈⠆⢣⢿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⢿⣆⠀⠀⠀⠀⠀⠀⠙⣿⣦⡈⠐⡈⡐⢀⠂⡘⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠌⠐⠈⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠸⣿⡀⠀⠀⠀⢸⡋⢻⣦⡀⠀⠀⢀⠀⠀⠀⠀⣿⡟⢛⣿⣿⣿⣿⣿⡑⢆⠻⣿⣿⣿⣿⣿⣿⣦⠙⢢⢻⣿⣿⣿⣿⣿⠁⠀⠀⠀⠈⣷⣶⠟⠋⠁⠀⠘⠿⣦⣄⠀⠀⠀⠀⠀⠈⠛⣿⣦⠐⡀⢂⠐⣨⠀⠀⠀⢀⣠⣿⡇⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣹⣷⣀⣠⣾⡟⠁⠀⠹⣷⡄⠀⠀⠀⠀⠀⠈⠿⢻⣿⠿⣜⣻⣿⡏⠱⡈⢒⡹⢿⡿⢿⢃⠛⢧⡉⢆⣿⣿⣿⣿⣿⠃⠀⠀⠀⢀⣾⡟⠁⡀⠤⠀⠘⢿⣶⣈⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⡷⢀⠂⡐⠄⢀⣠⣴⣾⠟⢻⣷⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠛⠋⠁⠉⢫⣍⣿⠁⠀⠀⠀⠈⠻⢷⣄⠀⣀⠀⠀⢠⣿⣿⣛⣬⣽⣿⣌⣱⣐⡷⣆⠣⡜⢢⢍⣚⣤⢛⣼⣿⣿⡛⢿⣿⡀⢀⣤⣶⠟⠋⢀⠘⠉⠀⠀⠀⠀⠙⢿⣆⠹⣷⡀⠀⠀⠀⠀⣰⣿⠋⡔⠠⠐⡈⢈⣽⡿⠋⠀⠀⢿⡿⣶⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠃⠀⠄⠸⣿⣿⡳⣜⣿⡿⡛⠿⠿⣿⣷⣧⢌⣡⣾⣛⠟⢻⠛⢋⣿⣿⣾⣿⣥⡾⠟⠀⢌⡐⠄⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⢻⣿⣄⠀⠀⣸⡿⢃⠐⡈⠁⠡⢸⣿⠛⠁⠀⠀⠀⠀⣷⣹⣿⠃⠀⠈⠙⠂⠀⠀⠀⠀⠀⠂⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⡰⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⡀⣸⣟⠀⠀⠀⠀⠀⢹⣿⣷⣿⣬⣷⣭⣖⣱⣄⣻⢣⡎⢿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⠟⠀⠌⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣦⡈⢏⣠⣾⡟⠁⠈⢶⠀⡁⠂⢹⣿⠀⠀⠀⠀⠀⠀⠙⣿⡇⠀⠀⠀⠀⠀⠀⢠⣵⡄⠀⠂⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⢠⡼⠿⠁⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠈⢿⣇⠒⠋⠛⠛⠛⢻⣯⠀⠀⢨⠆⠀⢾⣿⣯⣛⢿⣿⣟⣛⢻⢻⡿⢏⡼⣹⣿⣿⢧⣿⣿⡟⠉⠁⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣤⣿⡿⡀⠀⠀⡘⠤⢀⠁⢺⣿⡀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⢠⣄⠀⠀⠀⠈⠛⠄⠂⡐⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠈⢦⠀⠈⢿⣆⠀⠀⠀⠀⢸⣯⠀⠀⠀⠂⢌⣃⠻⣿⣯⡞⡵⢳⡌⢧⠳⣜⣫⣷⢹⣿⣿⣿⣹⣿⡇⠀⠀⢀⡸⠋⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡟⠀⠁⢩⡐⡀⢆⠂⠌⢸⣿⡁⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⣬⣿⡄⠀⠀⠀⠀⠈⠐⠄⢂⠌⡀⠀⠀⠀⢀⡀⠀
		⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠀⠀⢨⡄⠁⠈⣿⡆⠀⠀⠀⢸⣷⠀⠀⢀⠒⣼⣷⣼⣿⣻⣿⣯⣳⣜⢣⣛⣴⣿⣯⢽⣿⣿⣯⣷⣿⡇⠀⡘⠏⢀⠐⡈⠹⣦⣀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⢀⣠⣾⡟⢻⡅⠀⠀⠀⢻⣿⡀⢂⠐⢬⣿⡆⠀⠀⠀⣠⣿⠇⢸⠀⠀⠀⢻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠁⢀⠠⠀⠀⠀⠀⠀
		⣀⣤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀⠀⠘⣿⡄⠐⠸⣿⡄⠀⠀⢸⣿⠀⠀⢂⣾⡿⠋⣿⣿⣳⣞⣿⣿⣿⣿⣿⠿⡟⢣⣾⣿⣿⣿⣿⣿⣇⢰⣏⠠⠀⢂⠐⠠⢈⠻⣷⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠛⠉⠀⢘⠂⠀⠀⢀⣼⣿⠁⠠⢈⠘⣿⡇⠀⠀⢠⣿⡏⠠⢈⠄⠀⠀⠘⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠈⠀⠁⠂
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⠇⠀⠀⠀⠀⣸⡆⠀⠀⠻⣧⠀⠀⣸⣟⣠⣶⣿⣿⡇⣸⣿⣿⢳⡮⣟⡻⣟⣿⡥⣋⢜⣩⣿⣿⣿⣿⣿⣿⣿⣼⠏⠀⠘⡆⠀⠁⠢⣄⡈⢤⣀⠀⠀⠀⠀⣠⣾⡟⠃⡈⠄⢁⠊⠀⠀⠀⣸⣿⠋⡁⠃⠄⡈⣿⠃⠀⠀⣾⡟⠀⠡⠈⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡀⠀⠀⠀⠀⠀⠀⣸⣤⡏⠀⠀⠀⣀⣴⡟⠁⠀⢀⣡⣹⣶⣿⣿⣿⣿⣿⣿⣿⡁⠸⣿⣿⣏⢷⢯⡽⣞⠿⣧⠍⢮⡔⣹⣿⣿⣟⣿⠛⣿⣿⣦⠀⠀⡐⠀⠀⠀⠉⠛⣦⠍⠃⠀⣠⣾⠟⠉⠐⠀⠤⢌⠀⠂⠀⢀⣼⡿⠁⠐⡈⠄⠁⡠⠍⠀⠀⣼⣿⠁⠌⡀⢡⠀⠀⠀⠀⠈⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠀⠄⠀⠀⠀⠀⠀⢰⣿⡿⠁⠀⠀⢀⡻⣩⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠹⣿⣿⡞⣯⢳⣏⢿⡰⣋⢖⡩⢼⣿⡿⡿⠋⠀⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠈⠑⢲⠘⣛⣭⡰⠃⠀⠀⢀⡀⢈⠄⡁⢛⠋⠀⠀⡆⠐⠠⠑⢠⠂⠀⢀⣿⡿⠀⠀⢰⡀⠳⢤⠀⠀⠀⠠⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠘⠀⠣⢀⠀⠀⠀⠀⢀⣾⣏⠅⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣦⠀⠘⣿⣿⣎⢷⣚⣧⣗⠩⣎⠵⣻⣿⣷⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣾⣯⣗⡶⣄⢀⣀⡉⠉⠁⠀⠀⠀⠠⠃⡈⠄⢂⠰⠉⠀⠀⠀⢈⢁⠂⢌⠀⡂⠀⠾⣿⠃⠀⠀⣼⠃⠄⠂⡀⠀⠀⠀⢐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡐⠀⠀⠀⠀⠁⠈⠀⠄⠄⣈⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⣿⠀⠀⠈⢿⣿⣆⠳⡼⢭⠳⣬⣿⣿⡿⠃⠃⠠⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣻⢷⣦⣄⣀⠂⠁⠀⠀⠀⠀⠧⢀⠀⠀⠀⠀⠂⢌⠠⢀⢁⡐⠘⠄⣀⣤⣾⠷⠈⠀⠂⠔⡀⠀⠀⢈⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠄⡀⠀⠀⠐⡀⢂⠡⠀⠀⠀⠀⠀⠀⠀⠠⣈⠐⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠹⠇⠀⠀⠀⠀⠛⣿⣷⣜⣧⣿⣿⡿⠃⠀⢀⡀⢰⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣷⣦⣄⠀⠀⠀⠀⠈⠀⠁⡀⠀⠀⡄⢃⠈⠄⠡⢈⡐⢤⡟⠁⠀⠀⠀⠀⠁⢒⠀⠂⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⢠⠁⢈⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣥⣤⣤⣤⣤⣤⣬⣽⣿⠛⠉⠁⠀⠀⠀⢻⣧⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣷⡆⠀⠀⠠⠁⠂⠀⠀⠀⢘⠠⢉⠐⡁⢂⠤⠋⠀⠀⠀⠄⠀⠀⠀⠘⢢⠁⠌⠀⠠⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⡀⠀
		⢀⣀⡠⠠⠌⠂⠀⣀⠀⡀⠀⠀⢀⠀⠀⡀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠐⠈⡐⢂⠐⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠰⠀⠠⠁⠀⠀⠀⠁⠈⠀⠈⠁⠀⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⡇⠀⠀⠀⠂⠁⠀⠀⠄⠐⠂⡐⠡⠀⠀⠐⠒⠀⠒⠂⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠃⠌⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣡⣉⣙⠛⡻⠿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡗⠀⠀⠀⠀⠀⠀⠠⠐⠈⠆⠠⠱⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠆⡐⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣯⣛⣛⠿⠿⢿⣿⣷⣶⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡁⡀⠀⠄⠂⠀⠀⡀⠸⣀⠡⠀⠄⠛⠱⣂⠀⠀⠀⠀⠀⠀⠀⣤⡆⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠐⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⢿⣿⣿⣶⣶⣧⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠂⡁⠀⠀⠀⠀⡀⠀⠀⠤⡁⠌⠐⡈⡐⠀⡀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢂⠣⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣶⣷⣭⣹⣟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠇⡇⠀⠐⠀⠀⠀⠀⠁⡀⠈⣆⠁⠀⠐⣆⡀⠱⢄⣀⣴⡿⢋⡀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⢃⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢻⡛⣭⠳⣌⠳⣌⢻⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠇⠀⠀⠠⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠙⢷⣆⡀⠈⢠⣵⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⠢⠐⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣏⠷⣙⠖⣛⠞⡻⢜⣫⣿⡿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣞⠁⠂⠀⠀⠀⠀⠀⠀⢁⠠⠀⠈⠀⠀⠀⠀⠀⠘⢻⣷⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⣁⠂⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣛⢮⢇⡿⡼⢷⡽⢎⠶⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⠂⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠸⠿⢧⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢡⠂⠆⡀⠁⠉⠈⠀⠁⠉⠈⠀⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣳⣟⡮⡞⣴⣿⣦⣽⣮⣽⣿⣿⣿⣿⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⡿⠀⠀⠀⠀⠀⠨⡄⠀⠀⠀⠀⠂⠀⠀⠀⠀⢀⠀⡁⠂⠌⠳⠀⠀⠀⠀⠠⢀⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠘⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣿⣞⣵⡹⣎⠽⣩⢏⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠃⠀⠀⢀⣀⠀⠀⣷⡀⠀⠠⠐⡀⠀⠀⠀⠨⠀⢂⠔⠁⠒⡀⠁⡀⠀⠀⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢂⠁⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡾⣷⣿⣾⣷⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡒⠄⠀⠀⠀⠀⠀⠀⣙⣧⡀⠀⠀⠀⠀⢀⠀⠰⡀⠀⠀⠀⠀⠈⠡⢀⠀⠠⠀⠄⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⡎⢄⠀⠠⢀⠤⡐⠛⠻⢿⣶⣄⡀⠀⠀⢠⠗⠀⠀⠀⠀⠀⠀⠀⣠⠊⠡⢈⠐⠢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢂⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣌⠤⢁⢊⡐⠤⣉⠲⡰⣼⣿⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡐⠌⠢⠑⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠌⠠⡁⠀⠀⠀⡀⢀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⢢⢌⠳⡜⢲⣾⣷⣿⣿⣯⣿⣏⢿⣷⣦⠀⠀⠀⠀⠀⢀⠀⠀⠀⡀⠘⠄⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢈⠐⠡⢀⠁⠀⠀⠐⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⡎⣷⣾⣿⣿⣿⣿⣹⣾⣿⣯⣰⣿⣿⡇⠀⠀⠀⠁⠀⠌⠀⠀⡐⠠⢚⠀⠁⠀⠁⠀⠀⠈⠀⠁⠈⠄⠀⡀
		⠀⠠⠘⠄⡂⠠⠀⠌⠀⠐⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢿⡿⣯⢷⣯⣷⣿⣿⡟⠥⣺⣿⣿⡆⠀⠀⠀⠀⠀⠀⡀⠁⠀⡐⠀⡂⠄⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⢀⠣⢐⠠⠁⠄⠂⢈⠐⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⣻⢿⣾⣿⣿⠙⡜⠠⣿⣿⣿⠅⠀⠀⠀⠀⠀⠀⠠⠀⠀⢀⠡⠀⢂⠀⠀⠀⠀⠀⠀⠠⠈⠀⢀⠀
		⠀⠠⢈⠤⠁⠐⠀⠌⢀⠐⠀⠠⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⢿⡽⣟⣿⣿⣏⡒⢈⠰⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠂⠠⠁⠀⠀⠀⠀⠀⠀⠌⢀⠂⠀⡀⠀
		⠀⡐⢀⢂⠡⠌⡐⢄⠢⠌⡐⠄⣂⠀⢻⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⣲⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⡁⠐⠀⠀⠀⠀⠀⠀⠀⠀⢈⠀⠀⠀
		⢀⠐⡈⢄⠊⡐⠌⡄⠊⡔⢁⢂⡐⠌⡀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀
		⠀⠂⠌⡀⠎⠐⡀⠄⡱⠐⠂⠤⠘⠠⡐⢀⠈⠛⠋⠛⠻⠟⠻⠛⠛⠛⠋⠉⠁⠀⢀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
		⠀⡁⠂⢌⠰⠁⠆⠱⢠⢉⠂⠤⢁⢃⡐⠠⠈⠄⠡⠈⠄⠂⠡⢀⡁⠂⢄⠐⢨⠀⢌⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣽⣯⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⠡⢌⠢⢉⠢⡑⠢⢌⠒⣀⠊⡄⢢⢁⠀⡠⠐⡀⠠⢀⠁⠂⠄⡁⠊⠀⢃⠠⠈⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢿⠿⣿⠿⡿⢿⡛⢏⣻⣼⠿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠈⠔⠢⡐⠢⢁⠔⡡⢊⠐⠠⢌⠠⣁⠢⠀⡅⠂⢅⠂⡅⢂⡐⠤⠀⠑⠈⠠⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⡟⣹⡙⢦⣋⢾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡙⠋⠛⠏⠻⠙⠂⠙⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠁⡌⢂⡡⢁⠌⡰⢡⠈⡌⠐⠢⢁⠂⠄⠃⠌⡑⠠⠡⢐⠠⠌⠀⠠⠀⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⢺⣿⡗⡥⢚⠦⣙⠮⣗⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣧⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠁⡜⢀⠣⠐⠡⠌⡐⢂⠡⠐⡉⠰⢀⠡⠌⡘⡀⠆⡑⠐⣂⠐⡀⠂⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢹⣿⠣⡜⣡⠞⡬⢳⡌⢯⣻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣀⣤⡀⢀⣄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠁⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠓⢤⡀⠄⠠⢀⠂⠄⢀⠀⠄⠀⠀⠀⠉⠀⠁⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠠⢀⠂⡈⠤⢉⠂⡉⢁⠂⠌⢀⠤⠀⠀⠉⠀⢄⠀⠉⠀⠀⠀⠀⠤⠐⠀⠆⢄⠀⠀⠀⠀⠀⠀⠀⠈⢣⠄⢁⠰⢈⠰⠀⠎⠨⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⠡⠀⠄⠰⢀⠰⢀⠐⡀⠄⠠⠀⠁⠂⠐⡠⠐⠠⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠁⠊⠄⢂⠢⢀⣀⢀⠀⠀⠀⣀⠂⠄⠒⡠⢂⠁⠈⠰⠈⠡⠄⡠⡀⠤⡐⢎⠑⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠀⠀⠀⠀⠀⠀⡄⢂⠀⡀⠁⠂⠉⠒⠌⠤⢀⡄⠀⠀⢠⠓⢀⠡⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⡄⢊⠌⡄⠡⠀⠌⡄⠣⡐⢢⠀⡀⠠⢁⢂⠰⣠⢑⠢⠙⠄⠦⢀⠢⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⠁⡐⠌⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠀⠀⠀⠡⠘⡐⢠⠡⢄⠡⢐⡄⠣⠀⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠙⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⢀⠡⢀⠁⠂⠌⡐⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⡀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⡐⠆⡈⠐⠂⠄⡁⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠌⠀⠀⠀⡀⠄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠠⠐⠈⠀⠠⡄⢡⠈⠀⡄⠀⣹⢿⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠈⠐⠐⢶⣤⣅⡈⠄⠁⠀⠀⠀⡀⠀⠈⠀⠄⠀⠙⣿⣤⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠋⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠸⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⢀⣴⡿⠋⠀⠀⠀⠀⠀⠈⠛⢷⣌⠂⠄⠀⠀⠐⡀⠁⠈⠰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠐⠲⣤⣀⠀⢹⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠹⠶⣾⣿⣿⣦⠀⠀⢀⣠⣶⣿⣿⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⣄⠀⠀⠰⠄⡈⠔⡨⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⣀⠉⡙⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠤⣤⣤⡀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠉⣷⡻⠷⣶⠟⠻⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡄⠀⢠⠀⢀⠒⠀⠀⠀⠀⣰⣿⡁⣠⣴⠞⠉⠉⠀⠀⠈⠙⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢿⣆⠀⣀⣴⣶⣿⣿⢿⣿⣷⣦⣤⣄⣠⡇⠀⠀⠀⠀⠈⠁⠀⢀⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠐⢂⠌⠀⠌⠀⠀⠀⢀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠢⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡶⣓⠦⣶⣷⣾⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⢀⡔⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢂⠘⠤⠈⠆⠈⠀⠀⣠⣾⠟⢣⡀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⣼⣿⡟⢿⣿⣿⣿⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⡙⠃⠀⠐⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣀⠀⠠⡉⠐⡠⠀⣿⡿⠁⠈⠄⠐⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠋⢿⣶⣄⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣥⠀⠡⠐⠁⠀⣼⣿⠃⠀⠀⠈⢶⣤⠀⠀⠀⠀⢀⡄⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⣠⣿⣿⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠛⣶⣭⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡴⠛⠀⠀⡡⠆⢀⠈⣿⠇⠀⠀⠀⠀⠈⠹⣧⠀⢶⣾⡏⠄⡐⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⡈⢀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⢸⣟⠀⢠⣿⣿⣿⠠⢌⢋⣿⣟⠿⣻⣿⣿⣿⠿⠿⢿⠿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢻⣷⠀⢀⠛⣿⣄⠀⠀⠀⠀⠀⠀⢀⣽⡇⣀⠆⠀⠀⡅⠂⠄⡘⣿⡁⠀⠀⠀⠀⠀⠀⣿⣤⠾⠛⠀⠀⠀⠀⠒⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⡀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢈⠃⠀⢸⣿⣿⡏⠐⣠⣿⣿⡏⣞⡱⢫⡝⣠⠩⡜⢢⠑⡌⡐⢌⠻⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢸⠿⠿⣶⣦⣼⣿⣄⠀⣀⣀⣤⣶⠟⠋⠀⠁⠀⠀⠘⢠⢁⠂⠄⣿⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⢀⠀⠃⠄⠂⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠘⠀⠀⢸⣿⣿⠠⢡⣾⣟⡳⣜⢦⡙⢧⠾⣧⠳⡌⢥⠊⡔⢠⢈⢚⣽⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣹⣿⣿⣿⣭⣤⣂⡐⠢⠄⠀⠀⠠⢂⠌⡐⢀⠫⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⡄⢢⣿⣿⣷⣯⣖⡹⢎⣳⢂⢣⠉⢆⠓⡠⢃⠎⢆⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠈⠉⠛⢿⣧⡌⠐⡀⠰⢈⠰⠀⠂⡅⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⢷⣿⣿⣿⢿⣿⣿⣷⣿⣿⣿⣶⣿⣦⣭⣔⠣⡘⠬⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠿⢿⣇⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⢁⠂⠡⠌⡀⠰⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠁⠂⠁⠂⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⢐⠋⢿⣦⠀⠀⠀⠀⠀⠀⢹⣿⠀⡙⣻⣿⣿⣿⣿⣿⣿⠇⣌⢻⣿⣿⣿⣿⣿⡷⢡⢃⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠈⣲⣶⠟⠋⠁⠀⠘⠿⣦⣄⠀⠀⠀⠀⠀⠈⠛⣿⣦⢈⠐⠠⢀⠱⠀⠀⠀⢀⣠⣿⡇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣹⣷⣀⣠⣾⡟⠁⠀⠹⣷⡄⠀⠀⠀⠀⢸⣿⢀⣼⣿⣏⣞⡱⣿⣿⢏⠰⢀⠆⣍⡻⢿⢋⡜⢡⢃⢾⣿⣿⣿⣅⠀⠀⠀⠀⠀⢀⣴⡿⢋⣀⠀⠀⠈⢻⣶⣈⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⣧⠈⡐⠠⠁⢀⣠⣴⣾⠟⢻⣷⡀⠀⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠛⠋⠁⠉⢩⣅⣿⠀⠀⠀⠀⠈⠻⢷⣄⠀⠀⠈⣿⣇⣿⣟⠶⣜⣻⣽⣿⣦⣕⣪⣔⢪⡑⢮⢱⣌⣦⣩⣾⣿⣿⣼⣿⠀⠀⠀⣠⣶⡟⠋⠱⠛⠈⠀⠀⠀⠀⠙⢿⣆⠹⣷⠀⠀⠀⠀⠀⣰⣿⠣⡘⡀⢂⠡⢈⣽⡿⠋⠀⠀⢿⡿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠹⣿⣿⣿⡹⢎⣿⡟⣿⠿⢻⠿⢿⣷⣬⣦⣼⣛⡛⠛⠛⣛⣿⣿⣿⠦⢤⠾⢋⠁⣤⣌⠆⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠻⣷⡄⠀⠀⣼⡿⢃⠠⠑⠀⠃⢴⣿⠛⠁⠀⠀⠀⠀⣷⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⣸⡷⠀⠀⠀⠀⠘⣿⣿⣿⣿⣼⣿⣴⣯⣦⣍⣒⣏⡒⣻⣿⣿⣿⣿⣿⣿⡟⠉⠹⢄⡀⠂⠄⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣦⡘⢏⣠⣾⠟⠁⠀⢣⠄⠡⢈⢸⣿⠀⠀⠀⠀⠀⠀⢉⣿⠇⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⢠⠴⠟⠁⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠈⢿⣗⠒⠉⠚⠙⠋⢹⣿⠀⠀⠩⠀⢠⢿⣿⣞⣝⡻⣟⡿⣹⢛⡻⢿⣿⣵⣪⣿⣿⡷⣭⣿⣿⠀⠀⠀⠺⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣷⣤⣿⡿⡂⠀⠀⡘⢂⠡⠄⢺⣿⡀⠀⠀⠀⠀⠀⣾⡿⠁⠀⠀⠀⣀⠀⠀⠀⠀⠑⠂⠄⡈⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢇⠀⠀⢿⣆⠀⠀⠀⠀⢸⣿⠀⠀⠀⢠⣿⣷⡿⢿⣮⢻⡍⡟⡴⢫⡜⡱⢎⣵⣿⣿⣿⣿⣳⣿⣿⠀⠀⠀⢀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡟⠀⠀⠑⡠⠐⢠⠂⡐⢸⣿⠁⠀⠀⠀⠀⣸⣿⠑⡀⠀⠀⣤⣿⡄⠀⠀⠀⠀⠀⠒⠄⢂⡌⠀⠀⠀⠀⢀⡀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⠀⠀⠀⢨⡀⠁⠈⣿⣆⠀⠀⠀⢸⣯⠀⠀⣤⣿⣿⣿⣿⣏⢾⣿⣾⣱⣭⡳⣜⣭⣿⡾⢫⣿⣿⣯⣷⣿⣿⠀⠀⠏⠀⠌⠠⠑⣤⣀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⢀⣠⣾⡟⢻⠁⠀⠀⠀⠹⣷⠀⡐⠠⢸⣿⠄⠀⠀⠀⣠⣿⠇⡘⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠐⠂⠀⠄⠀⠀⠀⠀
		⣀⡤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀⠀⠙⢷⡌⠀⠸⣿⡀⠀⠀⢸⣯⢀⣴⣿⡟⢨⣿⡿⣽⣣⡟⣿⣿⣿⣿⠿⡿⢏⡱⣹⣿⣿⣿⣿⣿⣿⡀⠌⠠⠈⠄⡁⢂⠀⠛⢧⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠛⠉⠀⣈⠃⠀⠀⢀⣼⣿⠀⠄⡁⢚⣿⡄⠀⠀⢠⣿⡏⠄⢘⡀⠀⠀⠘⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠁⠈⠄
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣾⠇⠀⠀⠀⠀⢀⡆⠀⠀⢻⡇⣀⣤⣿⣿⣿⣿⣿⣏⢸⣿⣟⡶⢯⣝⢿⡻⢿⣯⢓⡍⢦⠱⣹⣿⣿⣿⣿⣽⣛⡡⠂⠁⠘⡔⠀⠀⠘⣀⠂⣀⡀⠀⠀⠀⠀⣠⣾⠟⠃⠄⡁⠂⠌⠀⠀⠀⢸⣿⠋⠰⢀⠐⡀⣿⠁⠀⠀⣾⡟⠀⠌⡀⠀⠀⠀⠀⢹⡿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠠⠀⠀⠀⠀⠀⠀⣼⠗⠀⠀⠀⠀⢀⣴⠟⣠⣤⣼⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⢻⣿⣿⣹⢞⣯⡽⣛⡾⡱⢎⡥⣓⠦⣉⣿⣟⣛⣿⣿⣷⣄⡀⠘⡄⠀⠀⠀⠀⠁⢀⠉⠀⠀⣠⣾⠟⠉⠐⠀⠤⠄⡁⠂⠀⢀⣼⡿⠃⠀⢃⠂⠁⢠⠇⠀⠀⣼⣿⠂⠁⠂⠄⠀⠀⠀⠀⠀⠻⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠀⠡⠀⠀⠀⠀⠀⣼⡿⠂⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⠀⢿⣿⡽⣚⢧⡟⣧⢻⡱⢎⡶⣉⠶⣹⣿⡟⠃⢸⣿⣿⣿⣿⣷⣮⣅⡀⠀⠀⠀⠀⠂⢒⠘⢛⣩⠰⠁⠀⠀⢀⠠⢀⡁⠂⢍⠋⠀⠀⡌⣀⠂⢈⠆⡉⠀⢀⣿⡟⠀⠀⢡⠈⠡⢤⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠣⡀⠄⠀⣀⣀⣰⣿⣧⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡇⠀⠻⣿⣿⠎⡽⣞⣧⡟⣌⢳⣽⣾⡿⠋⢇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠌⠌⠈⠀⠀⠀⠀⢀⠋⡐⠠⢀⠱⠈⠀⠀⠀⠠⠄⠂⠌⢀⡐⠀⣾⠟⡀⠀⠀⣸⠃⠄⠂⠀⠀⠀⠀⢂⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⢀⠂⠈⠠⠁⠀⠀⠀⠁⠈⠄⣉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⡇⠀⠀⠙⣿⣯⢰⢩⠮⣕⣮⣿⡿⠟⠀⠀⠙⠂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣈⡀⠤⢴⣄⠂⠠⠀⠀⠀⠀⠧⡀⠀⠀⠀⠀⠊⠔⡈⢀⠠⡰⠀⢃⡀⢤⡾⠇⠀⠈⠐⡁⡀⠀⠀⣀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠠⡀⠀⢀⠠⠀⠄⡁⠀⠀⠀⠀⠀⠀⠀⡴⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⢉⠱⠂⠀⠀⠈⠿⣷⣾⣷⣾⡿⠋⠀⠀⠀⠀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣈⠆⠀⠀⠀⠀⠀⠀⠈⠁⠂⠄⠀⠀⠤⢁⠊⠔⡁⠌⠠⣈⠇⠀⠀⠀⠀⠀⠀⠡⢈⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⢠⠁⠀⠆⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣶⣶⣾⣶⣿⣿⣭⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠠⢁⠂⠀⠉⢐⠡⢈⠂⠌⡰⠁⠎⠀⠀⠀⠀⠀⠀⠀⠐⢂⠌⡐⠀⠐⠠⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⢀⠀
		⠀⣀⠠⠀⢌⠘⠀⡀⢀⡀⠀⡀⢀⠀⢀⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠐⡂⠈⡄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡉⠀⡀⠂⠀⠀⠀⠀⠈⠀⠈⠀⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⣟⣻⠿⡿⣿⣾⣷⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠐⠀⠀⠐⠀⠀⠁⠀⠠⠀⢈⠄⠑⢨⠀⠀⠐⠂⠂⠐⠂⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⣿⣿⣶⣯⣭⣉⣙⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠊⡐⠈⠤⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡃⠄⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣮⣿⣙⣛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⢂⠰⣀⠁⠂⠌⠑⡉⢆⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⡐⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣯⣿⣟⣟⠻⠿⢿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠂⠀⠀⠀⠠⠀⠄⠈⡅⢈⠐⡠⠐⠠⠀⠀⠀⠀⠀⢀⣼⠁⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⣀⠂⠡⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣍⢛⣿⠿⡿⣿⣿⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⠀⠐⠀⠀⠀⠰⡀⠀⠈⡔⠀⠀⠙⣄⠁⠐⠄⠀⡠⠟⠁⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠘⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⡻⣍⣶⢲⣝⣯⣾⣿⣿⣿⣿⡿⠿⣿⣿⣷⣶⣦⣽⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠐⠀⠁⢀⠈⠀⠀⠀⠀⠊⠔⡈⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⢈⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣵⡞⣯⣽⣻⣼⣳⢾⡿⣿⣿⣿⣿⣿⣿⣿⣶⣽⣮⣽⣹⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠠⠀⠀⠀⠀⠀⠁⠀⠀⠀⠐⡀⠂⠀⠀⠀⠀⠀⠀⠈⠆⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡘⠤⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣯⠽⣞⡵⣫⢶⣫⢞⣽⣻⣿⣿⣿⣿⣿⣭⣽⣛⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⡀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠄⠂⡀⠀⠀⠀⠀⠀⡈⠗⡀⠀⠀⠀⠀⠀⠀⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢘⡐⠢⠈⠈⠁⠈⠁⠀⠈⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣞⣽⣣⠿⣽⡻⣭⢻⣞⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⡄⠐⣀⠒⢢⠀⠀⠀⠀⢀⠁⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⣈⠡⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣯⢶⢯⣻⣵⣻⣾⢿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠠⠀⠐⠀⠀⠀⠈⠐⡠⠑⠀⠒⡀⠄⡀⠀⠀⠀⢊⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡀⠆⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣯⣟⡶⣽⣳⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠁⢀⠀⠀⢀⠀⠀⠀⠂⠀⡀⠀⠀⠀⠀⠀⠌⠂⠁⠀⠀⠀⠉⠐⢀⠀⠄⡐⢈⠒⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢃⠰⢀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣗⣻⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠘⠀⠀⠁⠈⠀⠁⠀⠄⠁⠀⠀⢁⠊⠀⠀⠀⠀⠀⠀⠀⣄⢊⡐⠀⢆⠡⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⠢⢐⠠⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣀⣤⣤⣄⡀⠈⠀⠐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠉⠄⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⡔⠡⢀⠀⠀⢀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢀⣦⣶⣾⣿⣿⠿⢿⣿⣿⡀⠀⠐⡀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠄⠑⢌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⠠⠒⠀⠂⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⢛⠿⣿⠻⣿⣿⣾⣿⣿⣧⣀⠐⠠⠀⠀⠀⠐⠀⠀⠀⠀⠀⠐⠀⠀⠀⢀⠂⠆⣀⠡⠀⠁⠀⠀⠈⠀⠁⠈⠄⠀⡀
		⠀⢈⠡⠌⡐⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⢯⣻⣜⢻⡴⣿⣿⣿⣿⣿⣿⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠁⠀⠀⠂⠌⡀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⢂⠘⡠⠄⠠⠈⠀⠄⠁⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣞⡿⣜⣯⠳⣞⡻⣿⣿⣿⣿⣿⠀⢀⠡⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠂⡀⠂⢀⠁⠂⢀⠁⠀⠀⠀⠀⠀⠠⠈⠀⠀⠄
		⠀⠂⢡⠐⠠⢀⠀⠡⠈⠀⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢾⣽⢫⡞⡽⣹⣿⣿⣿⣿⣿⡿⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠂⢈⠐⠀⠀⠀⠀⠀⠀⠌⠠⢈⠀⠀⡀
		⠀⠈⡄⠈⢆⠀⣂⠁⠆⡐⢠⠀⠄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣻⢾⣹⡞⣷⣳⣿⠈⣟⣿⡟⠃⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠄⠀
		⠠⠁⠄⡑⢈⠂⡄⢃⠒⡈⢄⠨⠐⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣏⡷⣹⢞⡵⣿⣷⣿⠟⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠐⠠⢀⠀⠂⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀
		⠀⠡⠘⡀⠢⠐⡀⢂⡘⠤⢈⠤⠁⠤⢁⠠⠙⠛⠛⠻⠛⠟⠛⠛⠉⠉⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
		⠈⠄⠡⢠⢁⠣⡐⠁⠆⡌⠂⠄⢩⠐⡠⢀⠂⠌⠠⢁⠂⠌⡐⢠⠈⠄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⢈⠰⡀⢆⠢⢁⠎⡰⢈⠔⡈⠢⠑⡐⢂⡀⢀⠐⠠⠀⠄⠐⠠⢈⠐⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢋⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠀⠂⠤⡁⢆⠢⢁⠆⡱⢈⡐⠠⢁⠢⢁⠂⠄⡡⢊⠰⢉⠰⡁⠀⢂⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢦⡙⠴⣩⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠋⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢈⠐⢄⠂⡌⢄⠡⡘⢄⠡⡀⠑⢂⠡⠌⡈⠂⢅⠂⢁⠀⠀⠀⠈⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣘⠣⣽⣿⡷⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠉⠈⠉⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠈⠄⣊⠐⢠⠂⡑⠨⠐⡈⢁⠂⠔⠂⢄⠉⡄⢊⠀⠌⠀⠀⠠⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢡⢛⡸⣿⣿⢘⡱⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⣤⡀⢠⣄⣀⣤⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠁⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⢠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠓⢤⡀⠄⠠⢀⠐⡀⢀⠀⠄⠀⠀⠀⠉⠀⠁⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠠⠂⠄⡀⠌⡑⢈⠉⡉⠐⠤⢀⠤⠂⠀⠉⠀⠄⠈⠁⠀⠀⠀⠀⠄⠂⠔⠂⡄⡀⠀⠀⠀⠀⠀⠀⠈⢗⡈⠄⢂⠡⠐⠄⡊⠌⢄⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠠⢁⠂⢀⠲⢀⠲⢁⠈⠀⠁⠠⠀⠉⠀⢈⠄⠂⠄⡱⠈⠀⠀⠀⠀⠀⠀⠀⠁⠀⠂⠀⠀⠀⠀⠐⠈⠒⠠⠐⠡⠄⣀⡀⡀⠀⠀⠠⠄⢂⠈⠤⢁⠂⠀⠌⡀⠢⠄⣠⢀⠤⢒⠎⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠀⠈⢄⠂⡀⠀⠀⠂⠉⠒⠌⠤⠄⡄⠀⠀⢠⠃⡈⢐⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢂⡔⠰⠡⠉⠌⡐⠨⡀⠎⢢⢁⠂⡀⠠⢀⠡⣐⠠⣌⠂⠓⠦⠰⢄⡡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠄⡐⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠁⠀⠈⡄⠑⡠⢁⠆⡀⢢⡰⠅⠂⠑⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠟⠁⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠉⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠡⢀⠁⢂⠁⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⣿⡧⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡔⠄⠂⠌⡐⠈⠄⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠁⠀⠈⠀⣀⠀⡄⢀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠠⢀⠉⠀⢀⡇⠐⡠⠀⠌⠀⣹⢿⠷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠐⠉⠀⠀⠀⠀⠀⣀⠀⠀⠀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠒⠐⢶⣤⣄⡈⢐⠀⠀⠀⠀⢀⠐⠀⢀⠂⠀⠙⣿⣤⠈⠉⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠉⠢⠀⠀⠙⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⢀⣴⡿⠋⠀⠀⠀⠀⠀⠉⠛⢿⣌⠢⠀⠀⠀⢂⠀⠀⠂⠘⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡄⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣿⠿⢿⣿⢷⣶⣶⣶⣤⣤⣄⠀⠀⠀⠀⠀⠤⠙⠿⣦⠀⠀⢀⣠⣶⣿⣿⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⣄⠀⠀⠄⠢⢁⠂⡜⠀⠀⠀⠀⠹⣷⠀⠠⠀⢀⣀⢉⠹⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠈⠙⠿⣾⣷⡀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣶⢿⣛⣿⣏⣞⣬⣽⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⣄⠈⠳⠶⠟⠛⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⡀⠀⡁⢀⠀⠆⠀⠀⠀⠀⢰⣿⡁⣠⣴⠞⠉⠉⠀⠀⠈⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⠀⠀⠀⠀⢀⣼⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⢀⠀⡤⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⢠⠘⡀⢀⠊⠀⠀⠀⢀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⢀⠀⠀⠈⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⣿⡆⠀⣰⣶⣿⡿⣛⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠐⡀⠢⢁⠆⠐⠀⠀⣠⣾⠟⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣴⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣄⠀⠀⠰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣀⠀⡀⠃⠄⢂⠐⣾⡿⠉⠀⢂⠁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣻⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⢿⠿⣿⣿⣿⣿⣿⡇⠛⠀⢶⣦⡹⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡦⠀⣈⠑⠈⠀⣼⣿⠃⠀⠀⠀⢶⣄⡀⠀⠀⠀⢀⡤⠀⢀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠙⠶⣦⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣿⣿⢻⣹⠹⣎⠵⡩⢍⠭⡛⢏⠒⡌⠣⢄⠋⣌⠹⣿⣿⣿⣿⠀⠀⠀⠀⠉⠻⢶⣭⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡴⠋⠀⠀⠤⢂⠀⠈⣿⡃⠀⠀⠀⠀⠈⠹⣦⠀⢶⣿⡏⠄⠠⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⡈⢀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣻⣿⣿⣿⣏⡳⣼⣷⣮⣳⡑⠎⣆⠱⣌⡜⡰⢉⠆⡱⢀⢣⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠛⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡅⣀⠆⠀⠈⡔⠠⠈⡐⣿⡁⠀⠀⠀⠀⠀⠀⣿⣠⠾⠛⠀⠀⠀⠈⠒⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⢯⡱⣏⢧⣛⡽⣻⠿⣄⠣⡔⢢⡑⢎⠰⡁⢌⢂⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠸⠿⠷⣶⣦⣼⣿⣄⡀⢀⣀⣤⣶⠟⠉⠀⠁⠀⠀⠈⠔⡁⠂⠄⣿⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠃⠄⠂⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⢸⣿⡿⣿⣿⣟⡎⣷⣿⣿⣿⣷⣿⣎⡿⣷⡜⣱⣮⣂⠷⡿⠿⠾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣹⣿⣿⣿⣭⣤⣐⡈⠤⠄⠀⠀⠠⢊⠐⡁⠂⡹⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⣼⣿⣄⢹⣿⣿⣼⢿⣿⣫⢿⡿⢿⣿⣿⡦⡙⠼⢿⠿⣿⣿⣷⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠋⠀⠀⠈⠉⠛⢿⣶⡌⠐⡀⠰⠈⡔⠠⠁⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⣾⣿⡿⣩⠙⢿⣿⣿⡿⣛⢳⡚⢧⣛⣿⡧⡙⡌⢻⣿⣶⣮⣌⡙⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⢿⡆⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⠁⠌⡐⠠⢁⠈⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠌⠐⠂⠁⠂⠄⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⠀⢰⠛⢻⣦⠀⠀⠀⠻⣿⣷⣱⢊⣼⣿⡿⣳⠽⣶⣽⣧⢏⣿⣷⣱⣈⢅⠢⠤⡙⣋⠖⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣶⠟⠋⠁⢀⠘⠿⣦⣀⠀⠀⠀⠀⠀⠈⠛⢿⣶⠀⠄⡁⠂⢌⠀⠀⠀⢀⣠⣿⡇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣽⣷⣀⣠⣾⡏⠀⠀⠻⣷⡄⠀⠈⠛⢻⣿⣿⣿⣿⣧⢳⣛⡼⢳⣎⣿⣾⣵⣷⡿⣏⠦⡑⠢⢅⢪⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣉⣤⡔⠈⠙⢿⣦⡈⠻⣿⡆⠀⠀⠀⠀⠀⠈⢿⣯⠐⡀⠁⢂⠀⣠⣴⣾⠟⢻⣧⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠛⠋⠁⠉⢉⣡⣿⠀⠀⠀⠀⠈⠻⢶⣤⠆⠉⠈⢹⣿⣽⣗⣫⠶⣹⣳⣞⢿⣫⠙⣍⠲⣠⢃⢍⣳⣬⣿⣿⣿⠿⣶⣄⠀⠀⠀⣠⣶⡟⢋⠳⠛⠉⠀⠀⠀⠀⠙⢿⣆⠹⣧⠀⠀⠀⠀⠀⣰⣿⠃⡔⠠⢁⠂⢌⣹⡿⠋⠀⠀⠿⠿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠠⣿⣿⣧⣳⡹⣝⣿⣿⣿⣷⣿⣾⡟⣤⣼⣿⣿⡋⢉⣩⣄⢣⣄⠙⠀⣠⡾⠟⣡⣤⣦⠃⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠻⣷⡄⠀⠀⣼⡿⢃⠐⡈⠁⠢⢸⣾⠟⠁⠀⠀⠀⠀⣶⣩⣿⠃⠀⠀⠐⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⢠⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⢀⠀⣸⣯⠀⠀⠀⣀⣿⣿⡟⣷⣿⣲⣽⣚⣿⢇⡳⢢⡱⡘⣿⣿⣿⣿⣿⣿⡏⠈⠉⠺⣤⣰⡐⠞⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡙⢟⣠⣾⠟⠁⠈⢲⠀⡁⠂⢹⣿⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠌⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⣠⠶⠟⠁⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⢻⣗⠛⠉⠛⠋⠉⢻⡗⠀⠀⢠⣿⢿⣿⣟⡼⣭⢟⣧⣻⣼⡍⣞⡱⢎⡕⣺⣿⣿⣧⣻⣿⡇⠀⠀⠀⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣰⣿⡿⡂⠀⠀⡘⠂⠤⠁⢺⣿⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⡀⠀⠀⠀⠀⠉⡐⠀⠄⡁⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢀⠀⠀⢻⣆⠀⠀⠀⠀⢸⣟⠀⢠⣿⡿⣸⣿⣯⡽⣞⢿⣾⣷⣿⣿⣶⡙⣾⣥⢻⣿⣿⣽⣿⣿⡇⠀⠀⠀⠀⡘⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠁⠩⣐⠀⡑⠂⠌⢸⣿⠁⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⢤⣿⡄⠀⠀⠀⠀⠀⠘⠤⢀⡁⠂⠀⠀⠀⣀⠀⠀
		⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⢀⠂⢁⠀⢿⡄⠀⠀⠀⢸⣧⣾⣿⣿⣷⢹⣿⣷⡽⣫⢾⣝⣿⣿⡿⢥⢋⠴⣩⣿⣿⣿⣯⣿⣿⣧⣤⣤⣀⡂⠄⡈⠑⡀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⠉⠁⠀⠀⠀⢻⣿⠀⡁⠂⢼⣿⠄⠀⠀⠀⣠⣿⠇⢘⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⠠⠀⠀⠀⠀⠀
		⣀⣤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠀⠀⠀⠀⠈⠀⠄⢈⡷⣄⣤⣶⣿⣿⣿⣿⣿⣿⠀⠻⣿⣿⣵⡻⣾⢿⣿⣿⣏⢎⠶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢿⣿⣶⣧⣤⣁⠂⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠛⠉⠀⣈⠄⠀⠀⢀⣴⣿⠁⠠⠁⢺⣿⡂⠀⠀⢠⣿⡏⠀⢌⡀⠀⠀⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⠁⠘⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⢸⣿⢾⠃⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠻⣿⣶⣻⡵⣻⢾⣟⢬⡚⠴⣸⣿⣿⣿⣭⣯⣿⣿⣿⣿⣿⣷⣾⣭⣝⣛⠿⣿⣶⣦⣄⡀⠀⠀⢠⣾⠟⠁⡐⢈⠐⡀⠀⠀⠀⢨⣿⠋⠄⡁⠂⠄⣿⠁⠀⠀⣾⡟⠀⠡⠀⠀⠀⠀⠀⢹⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⢀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠙⣿⣿⡳⢭⡛⣼⡲⣍⢳⣴⣿⣿⣟⣛⡉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣙⠿⣿⣶⣾⡟⠉⠀⠀⠄⠢⠌⠐⠀⠀⣰⠟⠃⠐⡈⠄⠁⠢⣍⠀⠀⣼⣿⠂⠁⠂⠡⠀⠀⠀⠀⠀⠹⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⢂⠀⢂⠀⠀⠀⠀⢀⣼⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⠀⠀⠘⣿⣿⣧⡜⢸⣿⣔⣻⣿⠿⠉⡉⠍⠒⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣟⠿⣿⣆⠀⣀⠐⡈⠤⢁⠘⠄⠀⠀⡆⡐⠠⢁⠚⠄⠀⢀⣿⡟⠀⠀⢡⠂⠡⢤⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠁⠠⠁⠒⡠⢀⠀⡀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠌⠃⠀⠀⠀⠻⢿⡙⢢⣼⣿⡿⠋⠀⠀⠐⡈⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣌⠙⠣⠘⠄⡂⢆⠘⠀⠀⠀⠠⠄⡁⢂⠀⠎⢀⣾⡿⠁⠀⠀⣸⠆⠁⡀⠀⠀⠀⠀⢂⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠄⠈⠁⠀⠀⠐⠀⡂⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢅⠂⠀⠀⣀⣀⣠⣹⣿⡿⠋⠀⠀⠀⠀⠐⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠦⠐⡀⠀⠀⠀⠊⠐⠠⢀⠂⡤⠃⡐⠀⣤⡾⠧⠀⠁⠐⡁⠀⠀⠀⣀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠠⠄⠀⠀⠐⡀⠆⡡⠀⠀⠀⠀⠀⠀⠀⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣯⣴⣦⣤⣁⡈⠀⣤⣴⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠁⠂⠐⠀⠀⠀⡌⠄⠃⣉⠐⠠⢀⢣⠆⠀⠀⠀⠀⠀⠈⢁⠂⠡⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⣈⠁⢌⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣝⣩⣛⣛⣛⣛⣟⠿⢿⢛⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠠⠑⠂⠀⠁⠐⡌⠐⡀⢊⠡⢤⠋⠀⠀⠀⠀⠀⠀⠀⠐⢊⡐⠠⠀⠠⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⢀⠀
		⢀⣀⠠⠀⠌⢂⠀⡀⢀⡀⠀⣀⠀⠀⣀⠀⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⡛⢻⠛⡟⠻⡛⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⠃⡐⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡉⠠⠀⠂⠀⠀⠀⠀⠀⠈⠀⠀⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⠻⡞⢷⡹⢾⣳⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠐⠂⠀⠐⠀⠀⠁⠀⠐⠀⠠⠁⠄⢃⠀⠀⠐⠐⠂⠒⠂⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠠⠁⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⡽⢦⡳⣭⢶⣌⣧⣽⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠑⡈⠐⢨⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⡃⡐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢥⣓⣌⣧⢮⣽⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠈⠀⠀⠀⠀⠠⠀⠀⠀⢢⠐⠄⡁⠂⢈⠙⠻⡄⠀⠀⠀⠀⠀⠀⠀⣤⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠐⠠⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⢧⢋⣏⣛⣻⡟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠄⢨⠁⡌⢀⢂⡐⠈⡀⠀⠀⠀⠀⢀⣼⡟⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢄⠋⡀⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠮⣛⠾⣿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠀⡀⠈⠔⠀⠀⠘⡄⢀⠐⠄⢀⣰⠿⠋⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠊⡐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠂⠀⠁⠀⠀⠁⠀⠀⠡⠀⠀⠀⠈⠄⠀⠀⠈⠄⢂⡈⠀⠀⡐⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠆⠰⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⣾⣯⣿⣽⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠐⡀⠀⠀⠀⠀⠀⢣⠀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⡘⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣻⣟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⡀⠀⠠⠀⠄⡐⠀⠀⠀⠀⠀⠀⠀⢀⢋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠃⢆⠈⠈⠁⠉⠀⠀⠁⠈⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡿⣽⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⡀⢀⠂⠀⠀⢀⠀⠄⡀⢂⠈⠆⠀⠀⠀⠀⠠⢁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⡈⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢷⣻⡗⣯⢻⣭⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⢀⠠⠐⡀⠄⠀⠀⢈⠀⠒⡌⠐⠢⠌⠀⢀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠁⠆⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣵⣿⢯⣷⢻⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⢷⣻⡵⣻⢼⡳⣯⣟⡿⣿⣿⣿⣿⣿⣇⠀⠀⢀⠀⠀⠀⠀⠀⠀⠂⢀⠂⠄⡐⠀⢀⠀⠂⡄⠁⠀⠀⠀⠈⠁⠀⢀⠀⠄⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⠉⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢯⣿⣿⡹⢧⣏⠿⡾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣯⣟⣧⢻⡵⣫⢷⣻⣼⣻⣽⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠈⠀⠁⠀⠁⡀⠈⠐⠠⢂⠀⢂⠡⠀⠀⠀⠀⠀⠀⠀⡘⠄⡂⠌⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠣⢐⠠⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⠟⣥⣻⢳⣎⣟⡹⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣛⢾⣹⢞⡿⣿⣷⣯⣷⣞⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⢀⠀⠀⡀⠀⠄⠐⠀⠀⠂⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠐⢈⠢⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠂⢁⠂⠀⠀⢀⠀⢀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣟⣯⢳⡳⣜⢦⡻⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣮⢿⡽⣝⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠐⡈⠠⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⢀⠂⢅⠂⡀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀
		⠀⠠⠘⠠⠈⠄⠀⠀⠠⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣞⣧⢻⡜⣧⢳⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣯⣟⣿⣿⣿⣾⣽⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⢀⠈⠀⠀⢀⠂⠠⠐⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⠄⠀⠀⢀⠂⠆⡁⠄⠀⠁⠀⠀⠀⠈⠀⢡⠈⠀⠀
		⠀⠡⢘⠠⡁⠀⠀⠐⠠⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣞⣧⡟⣼⣻⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⡂⠄⢀⠀⠂⠀⠀⠀⠀⠀⡀⠄⡀⠀⢈⠀⠀⠀⠄⡑⢀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠈⠀
		⠀⡁⢢⠐⠠⠁⠄⠂⠄⠈⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣻⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡐⢀⠠⠀⠈⠀⠀⠀⠀⠌⠠⢀⠀⠀⡀⠂⠄⠐⡀⠄⠀⠂⠀⠀⠀⠀⠀⠠⢀⠀⠄⠀
		⠀⠐⢠⠈⡁⠄⠂⠀⠄⠐⠈⠐⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣭⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⠀⠀⠈⠀⠀⠀⠀⠈⠀⠀⠀⠈⠄⠐⠠⠀⠂⠠⠀⡁⠀⠀⠀⠠⠀⠈⠄⢀⠀⠀⡀
		⠀⡈⠄⢂⠔⡀⠆⡡⢈⠐⣀⠂⡄⠁⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣡⣿⡖⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠈⠄⠁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠐⡀⠀⡁⠐⠀⠀⠀⠀⠀⠀⠀⠈⢀⠂⠀⠀
		⢀⠐⡈⠔⢂⠔⡈⠔⡈⠔⡀⢂⠔⡈⢀⠂⠹⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡻⢿⡻⣍⣳⣬⣷⣷⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠂⢀⠂⠄⡀⠂⡀⠄⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⠂⠌⡘⠄⠂⠄⠒⣈⠰⠈⠄⠢⢁⠂⢈⠀⡐⠠⢈⠉⠉⣉⢿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠙⠷⡷⢾⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠠⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠀⡁⠒⡠⢉⠜⡀⠣⠐⣂⠡⢈⠁⢆⡈⠄⠘⠀⡁⢂⠐⣨⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⢿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⠡⡐⢡⠂⠰⡁⠡⢄⠢⣀⠉⠆⠰⣈⠀⠄⠐⠀⢢⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣩⢲⠱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠈⠤⠑⡄⢊⠁⢆⠱⢈⡐⠠⠌⡠⢁⠄⡘⠤⠁⠌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢥⡛⣏⠼⣿⣿⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⢁⠢⢁⠌⡄⢉⠄⢃⠂⠄⠡⢂⠑⠨⠄⠡⠀⠄⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢦⡹⣌⠞⣿⣿⣖⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢁⠢⠑⠌⠂⠌⠄⠊⠄⡉⠘⠄⢢⠁⢃⡌⢡⠈⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⠱⣌⢚⣿⣿⡖⢧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠉⠈⠀⠀⠀⢀⣠⢀⢀⠀⣀⠀⠀⢀⣤⡄⠀⠀⡀⠀⢀⣀⡀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠛⣤⡀⠄⠠⢀⠂⠄⢀⠀⠄⠀⠀⠀⠉⠈⠁⠀⠁⠀⠉⠉⠉⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠄⠀⠀⠀⠀⠀⢀⣠⠤⠖⡁⢈⡈⠌⡁⢉⠉⠂⢭⣤⣼⠗⠁⠁⠒⣄⡀⠉⠁⠒⠀⠠⠀⠒⠒⠒⣤⡀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠡⠐⡈⠔⠠⠊⠌⢄⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⡐⠈⠄⠐⠤⠂⠔⠉⠂⠀⠀⠀⠈⠀⠀⢂⡐⠠⠈⡼⠛⠉⠁⠀⠀⠀⠀⠀⠙⠻⢆⠀⠀⠀⠀⠂⠁⠒⠄⡉⠳⠆⣄⣀⡀⢀⠀⠰⣀⠂⢡⠐⠤⠁⠈⠰⢀⠒⠤⢠⠄⡤⢒⢎⡁⠊⠀⠀⠀⢀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠠⠀⠀⠀⠀⠀⢄⠂⡀⠀⠂⠈⠉⠒⠬⠄⠄⡡⠀⠀⢠⠃⠄⢡⡐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠐⠀⠀⠀⠀⠀⠀⢂⡰⠠⢍⠈⡁⠂⠄⡌⠰⡈⠆⡁⢀⠀⢂⠐⣠⢂⡜⠄⠳⠢⠔⢤⠡⠀⠈⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠌⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠘⡈⠐⡄⢃⠌⡒⢀⡧⠞⠀⠋⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠃⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠖⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠡⠐⡈⠐⡈⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣿⣯⠤⠀⠀⠀⠀⠀⢸⣷⣶⣤⣤⣤⣄⣀⡀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢂⠡⢀⠡⠐⡀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⢨⣿⠟⠀⠀⠀⠀⣠⣶⣿⣿⣿⣽⣿⣿⣿⢿⣿⠿⣿⣿⣿⡿⠟⠿⠷⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠐⠠⠀⠛⠀⢀⡆⢀⠂⠠⠄⠠⣽⣻⢷⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠒⠋⠀⠀⠀⣰⡿⠁⠀⠀⠀⣤⣾⣿⡿⢋⡝⣿⣿⣿⣿⣿⣾⣿⣷⣿⣿⣿⣿⣿⣷⣦⣄⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠑⠲⢶⣤⣄⡁⢢⠁⠀⠀⠀⠂⠀⠁⢀⠂⠀⠹⣿⣤⠈⠙⠛⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⣼⣿⣿⣯⣜⡹⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣦⣀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡇⢀⣴⡿⠋⠀⠀⠀⠀⠀⠉⠻⢿⣮⠳⡄⠀⠀⠣⠀⠈⠀⢸⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠈⠛⢷⣦⡄⠀⣻⡇⠀⠀⠀⣼⣿⢻⡹⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⢹⢿⣆⠀⠀⢀⣤⣶⣿⣿⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⡀⠀⠰⡁⠌⡐⢬⠀⠀⠀⠀⠹⣷⠀⠀⠄⢀⣀⡉⠛⠿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⠙⢷⣼⣧⠀⢀⣾⣿⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⡅⠀⠀⢀⠈⠳⠶⠟⠛⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⣀⠀⠀⢆⠀⠀⠀⠀⣰⣿⣁⣠⣴⡟⠉⠉⠀⠀⠉⠙⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⠿⢻⣿⣿⡁⠀⠀⠈⠣⣄⣀⡠⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡁⠠⢐⠈⢀⠂⠀⠀⠀⢀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠠⢾⣷⠋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢟⡫⡙⣌⠢⢀⠃⠄⢂⠉⡄⡛⣿⡅⠀⠀⠀⣠⠿⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡐⠐⣈⠐⢂⠈⠀⠀⣠⣾⠟⢣⡀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⠛⢶⣀⠀⠀⠀⣠⣴⡿⠃⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⣎⢳⣮⠱⣇⠦⣑⠂⢌⡀⠆⢌⠠⠑⣿⣧⠀⢀⣾⠋⠀⠀⠀⢲⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠠⡘⠀⢂⠀⣿⡿⠉⠀⣇⠐⠦⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣦⠀⢸⡟⠋⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⠳⣎⠳⣌⠲⣡⠚⡄⠒⢬⠀⢆⠩⢼⣿⣦⣼⣧⡄⠀⠀⢰⣤⡻⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠡⠐⠁⠀⣼⣿⠃⠀⠀⠈⣷⣦⣃⠀⠀⠀⢠⡤⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⡀⠁⢀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣯⡀⠀⠀⠀⠀⢛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⢒⣻⣬⣷⣬⣷⣶⣿⣾⣿⡆⢻⣶⣿⣾⣿⣿⡟⠉⠀⠀⠀⠀⠈⠻⣶⣭⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠏⠁⠀⠸⡄⠀⠂⣿⠇⠀⠀⠀⠀⠈⠻⣧⠀⢶⣿⡯⠄⠠⠐⠀⠀⠀⠀⠀⠀⠄⠀⠀⠈⠀⡀⠂⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⣄⠀⠀⣼⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⣏⡿⣿⣿⣿⣯⣭⣶⡿⣿⣿⣆⠻⢿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣯⠀⢀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡍⣠⠂⠀⢈⡐⠠⠈⡐⣿⡃⠀⠀⠀⠀⠀⠀⣿⣤⠿⠛⠀⠀⠀⠀⠆⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⣯⡀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⢏⡾⣔⣫⡳⢍⣋⢛⡹⢡⠖⣿⣿⣿⡎⢆⣹⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⣶⣤⣼⣿⣆⡀⣀⣀⣤⣶⠟⠋⠉⠀⠀⠀⠠⠡⣁⠂⡐⣿⡁⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠐⠂⡀⠀⢣⠀⠂⠀⠀⠀⠀⠀⠀⡀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠈⢻⣿⡿⣟⣶⣏⢿⡹⣎⠷⣎⡽⣿⣷⣮⢄⠳⡩⣾⣿⣿⣿⣏⣶⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠹⣿⢩⣿⣿⣿⣭⣦⣐⡐⠢⢄⠀⠀⠠⢡⠀⠂⠄⢻⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⢿⣷⣭⣿⣎⡷⢿⡟⣷⢭⣞⣱⢻⣿⣿⠰⡡⢛⣿⡿⠿⣛⡟⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⠉⠉⠛⢿⣷⣈⠐⠀⡐⢂⠡⠊⡀⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⣤⡽⣿⣿⣼⣹⣓⠾⣽⡾⣜⣧⢻⣿⡟⡥⢃⣿⣷⣬⣱⣌⣻⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⣷⡆⠀⠀⠀⠀⠀⠀⠙⣿⣦⡁⠠⢈⠐⡁⠄⢨⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠐⠁⠈⠐⢀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠼⣿⡀⠀⠀⠀⣠⣿⣿⣦⠀⠀⠀⠘⠃⠈⣿⣿⡧⣟⡽⣲⡽⢾⣧⢯⣿⡜⣥⢋⡟⣛⢻⢛⠿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣶⠿⠛⠉⣀⠘⢿⣦⣀⠀⠀⠀⠀⠀⠈⠛⢿⣦⢀⠂⡐⠈⢄⠀⠀⠀⢀⣠⣿⠇⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣿⠀⣀⣼⡟⠁⠈⠻⣷⣄⠀⠀⠀⠀⣼⣿⣿⣎⣿⣳⢯⡷⢮⡻⣽⣿⣴⣩⢒⠭⡒⡍⣼⣿⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⢉⣠⡴⠈⠛⢿⣦⣈⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⣧⠐⠠⠁⠌⢀⣠⣴⣾⡿⢹⣶⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡶⠟⠛⠁⠉⠀⠉⣿⡇⠀⠀⠀⠘⠻⣦⣀⠀⣀⣧⣽⣿⢾⣱⡟⣧⣟⣯⢳⣏⡿⣿⣿⣮⣲⣡⣾⣿⠋⠙⠧⠙⢿⣶⣤⡀⠀⢀⣤⣶⠿⠋⠼⠛⠉⠀⠀⠀⠀⠙⢿⣆⠹⣷⡀⠀⠀⠀⠀⣰⣿⠣⣘⠠⠁⠌⣀⣿⣿⠋⠀⠈⠿⠿⣶⣠⣿⠃⣀⠀⠀⠀⠀⠀⠀⠁⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⡻⠋⠀⠀⡀⠀⠈⠀⠃⣼⡟⠀⠀⠀⠀⠀⠀⢈⣿⣿⣧⣿⣿⣿⣿⢧⣿⣎⢷⣺⢟⣾⣽⣿⠿⣟⢻⢻⣿⣇⣄⣠⣀⢈⠀⡈⢙⡿⠶⠿⠋⠁⢄⡢⠄⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠻⣷⣄⠀⠀⣼⡿⢃⠠⠈⠂⠉⢴⣿⠟⠁⠀⠀⠀⠀⣶⣩⣿⠃⠀⠈⠛⠳⢤⣄⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠉⠀⠀⠀⠀⡅⠈⠄⠡⠁⢹⣧⡀⢀⣀⠀⠀⠀⢨⣼⣿⣿⣘⣿⣿⣟⡳⣮⣽⣫⡽⣞⢧⣛⡬⣓⢬⠒⣽⣿⣿⢿⡿⣿⣿⣿⣶⣥⣘⣤⠁⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡙⢯⣰⣾⠟⠁⠈⢦⠁⠌⡈⢸⣿⠀⠀⠀⠀⠀⠀⠈⣿⡏⠀⠀⠀⠀⠀⠀⢬⣷⣆⠀⠌⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠴⠀⠀⠀⡀⠰⠂⠀⠀⠀⠀⠀⢸⡇⢈⠀⢂⠡⠈⡙⠟⠛⠛⠛⣛⣽⣿⣿⣿⣿⣯⡘⣿⣯⣷⣹⢖⣯⢷⣭⡷⣏⠶⣉⠶⣩⢾⣿⣿⣏⢾⣱⢏⢸⣿⣿⣿⣿⣿⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣴⣿⠿⡀⠀⠀⠘⡈⠔⠀⣹⣿⡀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠠⣄⠀⠀⠀⠈⠻⠆⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⣾⣟⠀⠀⠀⢂⡥⢰⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⢿⣿⣧⡟⣮⣛⡼⢻⡜⣫⢕⣫⣽⣿⣿⣿⣯⢷⣯⢗⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⢉⡆⡁⠰⢈⠐⢸⣿⠁⠀⠀⠀⠀⣸⣿⠃⠄⠀⠀⡴⣿⡄⠀⠀⠀⠀⠀⠑⠂⢌⠠⠁⠀⠀⠀⢀⠀⠀
		⠈⠉⠀⡠⠀⠀⠀⠂⠈⠁⠂⠀⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡃⠀⠀⣀⣴⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠻⣿⣟⡶⣍⠞⣣⢛⢦⢋⣶⣿⣿⣿⣿⢯⣟⣞⡳⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢀⣠⣶⡿⠋⠀⠀⠀⠀⢹⡿⠀⠂⠄⢺⣿⡅⠀⠀⠀⣠⣿⠇⡘⠀⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠁⠄⠐⠀⠀⡀⠀⠀
		⢀⣐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⢋⣔⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠉⠻⣿⣿⡘⢤⢋⠮⣽⣿⣿⣼⣿⣿⣿⣾⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢀⠛⠋⠉⢀⠒⠀⠀⠀⢠⣿⡟⢀⠡⠈⠼⣿⡄⠀⠀⢠⣿⡏⢀⠘⡄⠀⠀⠘⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠂⠁
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠄⠀⠀⠀⠀⠀⢀⣨⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠄⠀⠀⠙⠻⣿⣦⣍⣾⣿⣿⠟⠻⠿⣿⣿⣶⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠠⠐⡈⠔⡀⠎⠀⠀⠀⢸⡿⠋⢁⠂⠌⡀⣿⠃⠀⠀⣾⡟⠀⠂⠌⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⡘⠠⠀⠆⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⠠⠀⠀⠀⠀⠈⠙⠿⣿⢏⡁⡀⢀⢀⣘⣿⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠠⠁⠦⠔⢀⠒⠀⠀⣴⠟⠁⠐⡈⠄⢁⢠⡛⠀⠀⣼⣿⡃⠌⠐⠠⠀⠀⠀⠀⠈⢿⢿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡐⢠⠑⡌⠠⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢀⡀⣤⣴⣶⣾⣶⣶⡮⢿⠿⣿⣿⡿⡋⢌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⢀⡰⠠⢈⠐⢌⡁⠀⢀⡒⡀⢂⠀⠦⡉⠀⢀⣿⣿⠀⠀⢌⠄⠳⢤⠀⠀⠀⠈⣾⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢂⠐⡌⠁⠘⣤⣑⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣶⣶⣶⣶⣶⣶⣾⣾⣿⡟⢡⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠌⡄⠁⠢⠌⠂⠀⠀⠀⠀⠥⢀⠘⢀⠒⢀⣾⣿⠇⠀⢀⣼⠇⡀⢂⠀⠀⠀⠀⠢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⢠⠂⡐⠠⠉⠀⠀⠀⠀⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣩⣍⣥⣭⣭⣦⣽⣭⣷⣿⣿⡇⠈⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠘⠬⡁⠀⠀⠀⠀⠓⠠⢈⢀⣈⣾⠛⠁⡀⣤⣿⠿⠂⠐⠀⡃⠀⠀⠀⢈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢠⠀⠠⠄⡠⢐⠈⠄⣂⠡⠀⠀⠀⠀⠠⡜⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣋⣛⣏⣻⣝⣻⣿⣿⣿⣴⣦⣑⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠈⠁⠠⠀⣀⠀⡰⢀⠊⠌⡀⢂⠡⣰⡟⠁⠀⠀⠀⠀⠈⢁⠂⠌⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠂⠥⠐⢂⡘⠐⠀⠁⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠻⠛⠟⡛⢿⣻⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠐⡰⠈⠀⠀⠑⡠⢈⠐⠌⡐⡤⠟⠀⠀⠀⠀⠀⠀⠀⠈⢆⡈⠐⠀⠀⠀⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠀⠤⠑⢂⠀⡀⢀⡀⠀⣀⢀⡀⢬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⠿⣿⢿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠘⠀⠆⡈⢤⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⢆⠁⡂⠌⠀⠁⠀⠀⠀⠀⠈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣮⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠐⠀⠀⠂⠀⠁⠠⠘⠠⢈⠛⠀⠀⠐⠒⠲⠶⠳⠖⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⢢⠈⡐⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣩⣝⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠑⠂⠄⠹⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⢀⠰⢀⡁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣭⣻⣜⣣⢯⣙⣛⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠳⢀⠌⡐⠠⢀⠙⠻⠤⠀⠀⠀⠀⠀⠀⢀⣴⡾⠋⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⢈⠀⠆⠀⠀⠀⠀⠀⠀⠈⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠿⡿⢿⠿⣟⡳⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⡄⠈⡔⢀⠂⡰⢀⠘⠀⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⣸⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⢃⠈⢀⠂⠀⠀⠀⠀⠀⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣶⣮⡕⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡄⢀⠀⠀⠀⠀⠀⠈⠄⠀⢢⡐⠀⠁⠐⣈⠀⠀⠘⡠⠁⠐⠄⣀⣴⡿⢋⡔⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠜⠠⠈⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⢯⣷⣩⣎⠵⡲⡜⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⠄⠠⠀⠂⠀⠀⠀⠀⠀⠀⠱⠀⠀⠀⠈⡀⠀⠀⠀⠡⠌⡀⠀⢠⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠜⢠⢁⠂⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⡽⣭⣙⢮⢫⣕⢻⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡐⠀⠀⠀⠀⠀⠐⠀⠀⠰⡀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠡⢄⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠌⡄⠂⠌⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣮⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠀⡐⠀⠁⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠰⢈⠒⡈⠈⠁⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠂⠄⢀⠂⠀⠀⠀⠀⠄⢂⠀⠑⢂⠀⠀⠀⠀⠠⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡘⠤⢁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⢡⠈⠀⠄⠂⠀⠀⠉⠄⢨⠄⠃⠬⡀⠀⢀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠐⠄⠀⠀⠀⠀⠀⠌⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⠆⡀⠈⠄⠡⠀⢀⠂⠌⠀⠀⠀⠀⠈⠀⠀⠀⠄⡀⠄⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠎⡈⠄⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠈⠀⠀⠁⠈⠀⠀⠀⠀⠀⠡⠌⣀⠐⠠⢈⠄⠀⠀⠀⠀⠀⠀⡰⣀⠒⠠⠘⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⡔⢈⠐⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠀⠂⠈⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠌⠠⠑⡈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⡠⢁⠂⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣳⢿⡹⢯⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⡀⠀⠂⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡐⠠⠈⠐⠠⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⠌⢡⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⢀⠀⠀
		⠀⡐⠰⠈⠄⠁⠀⠁⠀⠈⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣮⡟⣥⢻⡜⣧⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠈⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⢀⠀⠀⢀⠀⠀⢀⠂⠠⠁⠄⠐⠀⠈⠀⠀⠀⠁⠀⠁⠂⠀⠀⢀⠂⢆⠁⡄⠐⠈⠀⠀⠈⠐⠀⢡⠂⠀⠀
		⠀⠄⡡⢉⠄⠈⠀⠈⠐⠈⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⡿⣟⣷⣛⢶⡹⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣂⠀⠐⠀⢀⠀⠀⠀⡀⠆⠀⠄⠠⠀⢈⠀⠀⠀⠄⡉⢀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⢂⠡⠂⠌⢀⠂⡀⠌⠐⠀⡀⠐⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣻⣮⡽⣞⡽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡐⠈⡀⠄⠀⠀⠠⠀⢀⠐⡈⠀⠀⠄⠂⠐⠀⠂⠄⠀⠂⠀⠀⠀⡀⠀⠠⠀⠄⠈⠀
		⠀⠂⢡⠡⠈⠀⠀⠄⠀⠂⢀⠠⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣷⣻⡼⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠂⠀⢀⠀⠀⠀⠀⠀⠁⢀⠀⠀⠌⡐⠀⢈⠀⢈⠐⢈⠀⠀⠀⠀⠀⠀⠄⡁⢈⠀⠀⠄
		⠀⠌⣀⠂⢡⠈⠔⡠⠌⡐⣀⠂⠄⠂⠄⠀⠂⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠠⠁⠈⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠠⠀⠀⠄⠂⢈⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⢀⠂⠄⡘⠀⠎⡐⢠⠘⢄⡐⢈⡘⠀⡌⡀⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢾⡽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠂⢀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⡐⠠⠈⠀⠀⠠⠀⠀⠀⠀⠀⠀⠰⠈⠀⠀
		⠀⠌⡐⠡⣈⠐⡀⢂⠌⠤⠐⠂⠄⠡⢀⠐⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⠿⣽⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠀⠐⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠀⠂⠄⢡⠀⠆⡑⠈⡔⢨⠀⡁⢊⠔⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣿⡹⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀
		⠀⠡⡈⠔⡈⠔⡠⢃⠌⡐⡐⢀⠃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠾⣿⣽⢳⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀
		⠈⡐⢠⠁⡔⢂⠁⢆⡘⢠⠐⠂⠌⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⡝⣲⢩⠟⣿⢿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⡀⢂⠌⡐⣀⠃⡔⡈⠆⣈⠐⠈⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢎⣼⡹⢧⣙⢦⢻⣽⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
		⠠⢀⠃⠆⠡⡀⠌⡐⣡⢊⠔⣠⡄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠇⢮⡝⢧⡚⣬⡓⢾⣿⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠉⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⡀⠀⡀⠀⠀⢀⡤⣀⠀⠀⠀⠀⢠⣀⣄⠀⠀⠈⠉⠈⠀⠀⠀⠀⠀⠀⠀⠉⠈⠉⠛⢤⡀⠄⠠⢀⠂⠄⢀⠠⢀⠀⠀⠀⠉⠈⠁⠀⠁⠀⠉⠉⠉⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⡉⠄⠃⡉⢉⠂⢤⣠⣴⠞⠂⠉⠂⣄⣈⠉⠑⠖⠂⠤⠰⠒⠒⠒⣤⣀⠀⠀⠀⠀⠀⠀⠘⢷⠈⡀⢂⠁⠎⡀⠆⠌⣀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠠⢀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠡⠀⠐⠀⠀⠂⠀⠄⠀⠀⢀⠀⠁⠈⠐⠀⢁⢂⠐⠠⢌⠚⠉⠁⠀⠀⠀⠀⠈⠙⠻⣧⠀⠀⠀⠀⠀⠘⠢⠄⡉⠳⠆⣄⣀⡀⢀⠀⢠⠁⠄⠂⡌⡐⠀⠈⠐⡠⠁⠆⢤⠠⣄⠲⢎⠁⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠀⠀⠀⠀⠀⠀⠡⠀⠈⠀⠀⠐⠈⠐⠠⠄⠠⢀⠀⠀⢀⠋⠀⠌⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⡐⠤⡉⠌⡁⠂⠌⡄⠣⡐⢌⢀⠀⡐⠠⢈⡐⣢⠡⠄⠳⠆⠦⢤⠁⠀⠈⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣤⣀⣀⡠⢶⣄⣀⣀⣀⢀⣤⡐⣠⣌⠶⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠀⠀⠀⢈⡐⠡⣀⠃⡌⡐⢠⣣⠖⠁⠃⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠃⠀⠀⣠⣶⣿⣿⣿⣿⣿⣶⣿⣾⣿⣿⣾⣿⣿⣿⣅⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠠⢀⠡⢀⠑⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⠋⠁⢀⣤⣿⡿⢟⢿⣛⢯⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠬⡐⠄⠂⠄⡈⠄⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠃⠀⣼⣿⠫⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠠⠀⠄⠙⠀⢀⡆⢁⠂⠀⡄⠠⣽⣻⢷⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠁⢀⣼⡿⢥⣛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠓⠲⢦⣤⣤⡀⢣⠀⠀⠀⠀⡀⠀⠌⠀⣀⠀⠙⣿⣤⠈⠉⠻⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⣰⣿⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⢀⣴⡿⠃⠀⠀⠀⠀⠀⠉⠛⢿⣎⠳⡀⠀⠀⠰⠀⠀⠐⢠⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠁⠀⠀⠀⠀⠀⠀⠂⢀⠀⠀⠈⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠿⠿⡿⢿⣿⣿⣱⣾⡟⠀⠐⠀⠀⠀⢀⣠⣶⣿⣿⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⠀⠀⠄⡃⠌⠐⢬⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⣀⢉⠛⠿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⢠⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡏⢏⡱⡘⠤⡁⠒⠈⠄⡈⢻⣿⡅⠀⠀⢀⠀⠐⠶⠟⠻⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⡀⠠⠈⠤⠀⠀⠀⠀⣰⣿⡁⣠⣴⡟⠋⠉⠀⠀⠉⠙⢳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡶⣹⠜⣦⠱⣉⠒⡄⠡⢈⠄⡠⠁⣿⣧⠀⠀⠉⠃⣄⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⢌⠁⠠⢁⠀⠀⠀⢀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠳⣝⡺⣍⠳⢌⡒⣌⣁⣃⠐⡄⢣⢼⣿⡄⠀⠀⣠⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠡⠈⢄⠊⡐⠀⠀⠀⣠⣾⠟⣃⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠓⢦⣀⠀⠀⠀⣼⣧⣤⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢛⡶⣹⣼⣿⣾⣿⣿⣿⣿⣿⣄⣣⣿⣿⡇⠀⣿⠉⠀⠀⠀⢲⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣂⠀⠠⡑⠀⡂⠀⣿⡿⠁⠐⢄⠑⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀⣾⣿⠋⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⣛⡾⢿⡛⢟⠻⣟⡽⡛⢛⢿⣷⣜⣿⡟⢠⣼⣷⡤⠀⠀⢠⣤⡻⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⠀⢁⠂⠁⢀⣹⣿⠃⠀⠀⠈⣶⣖⡄⠀⠀⠀⢠⡄⠠⢀⠁⠀⠀⠀⠀⠀⠀⠀⢀⡐⠀⠂⢀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢲⣿⡟⠀⠀⠀⠀⢹⣿⣿⡿⣻⣝⣻⢿⣿⣿⣿⡝⣮⢵⣹⢦⡙⡬⡑⠬⣠⠑⡊⡜⣿⣿⣷⣤⣾⡿⠋⠀⠀⠀⠀⠈⠻⢶⣭⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⠟⠁⠀⠨⠔⠀⠀⣿⠇⠀⠀⠀⠀⠈⠹⣧⠀⢶⣿⡏⠄⡐⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠂⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⡀⡠⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠨⢿⣿⣗⡿⢴⢻⡿⡼⣹⢧⣻⡜⣯⢟⡶⣭⣳⣌⠲⣁⠎⠴⣿⣿⣏⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡯⣀⠆⠀⠈⠄⡡⠈⡐⣿⠃⠀⠀⠀⠀⠀⠀⣿⣤⠾⠛⠀⠀⠀⠐⠂⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⠈⢻⣿⣿⣧⢣⣛⢵⣛⢾⣷⡹⡞⣎⢷⡹⣿⢻⡗⡂⢎⠹⠿⠻⠿⢿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⢿⣶⣤⣼⣿⣆⢀⡀⣀⣤⣶⠿⠋⠉⠁⠀⠀⠈⡑⠠⠁⠄⣿⠀⠀⠀⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠸⣷⡀⠀⠀⠀⠀⢀⢻⣿⣏⢿⣛⠾⣼⡻⣭⠷⣹⢎⣟⡳⡽⣦⣋⠜⣾⣧⣯⣖⡡⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠻⣿⣩⣿⣿⣿⣯⣤⣀⡂⠢⠄⠀⠀⠠⠌⡁⠌⡀⡙⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⢿⣧⠀⠀⠀⠀⠀⠾⢿⣿⣿⡜⣯⢷⡻⣼⣯⣳⢯⣜⡳⣽⣣⢃⠮⠽⢿⠿⣟⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠛⠁⠀⠈⠉⠛⢿⣧⡌⠡⢀⠀⠣⡐⠂⠄⡡⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⣸⡯⢽⣿⣞⣥⣳⡝⣧⢏⡿⣷⢾⣝⣻⣷⣭⣶⡉⢆⠣⢼⣿⣧⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢷⡄⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⠌⠠⢁⠂⡐⠠⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠐⠈⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⣰⡟⠻⣧⣤⣀⡀⢻⣧⡘⣿⣿⣚⢿⣝⢾⣹⡽⣎⢿⣹⢧⣟⣿⣿⣿⣼⣼⣿⠟⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣶⠟⠋⠁⢀⠘⠿⣦⣀⠀⠀⠀⠀⠀⠈⠛⢿⣦⠁⠄⠂⠄⠡⠀⠀⠀⢀⣠⣿⠇⠀⠀⠀⠀⢀⡶⠁⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣤⣤⣾⠟⠀⠀⠙⣿⣿⣿⡾⣿⣷⣹⢶⣫⢟⡾⣭⠷⣽⢾⣭⣯⣿⣾⣿⣿⣿⡟⠿⣿⠶⣀⢆⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠟⡁⢀⠄⠀⠛⢿⣦⡌⠻⣿⡆⠀⠀⠀⠀⠀⠈⢿⣯⠀⠡⠈⡐⢀⣠⣴⣾⡿⢹⣶⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠾⠟⠋⠀⠀⠙⢋⠀⠀⢀⣠⣤⣽⣿⣿⣷⢹⣿⣧⡟⣼⣫⢷⣯⠿⣭⢿⣿⢫⠝⣩⢻⣿⠟⣿⣷⣦⣤⣤⣮⣽⣿⣶⣤⣀⠀⣀⣤⣶⠟⠉⠀⠀⠈⠀⠀⠀⠀⠙⢿⣆⠹⣧⡀⠀⠀⠀⠀⣰⣿⠣⢌⡁⢂⠐⣈⣽⣿⠋⠀⠀⠿⠿⣶⣀⣿⠃⢀⠀⠀⠀⠀⠀⠀⠁⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⣾⣿⣿⠀⡀⠀⠂⠁⢂⡐⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠹⣿⣟⣶⣻⣿⡙⡞⣥⢻⡛⢧⡋⠴⣿⣿⠀⢸⣿⣏⣭⣽⣯⣭⣿⣿⣿⣥⣄⡛⠉⡀⠤⣈⡄⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠻⣷⣄⠀⠀⣼⡿⢃⠀⢂⠐⠠⢚⣿⠛⠁⠀⠀⠀⠀⣶⣸⣿⠋⠀⠈⠙⠃⠤⣀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⣰⡿⠋⠁⠀⠀⠀⣤⣥⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠹⣿⣷⣯⢳⡽⡸⢬⡷⡹⢦⣙⣿⣿⣿⠀⠈⣿⣿⣟⣻⣟⡻⠿⣿⣿⣿⣿⣿⣷⣶⣤⣁⠀⠀⠒⠀⠀⠀⠀⠀⠀⠘⣿⣦⡙⢿⣠⣾⠟⠁⠈⢲⠀⢂⠁⣸⣿⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⢬⣷⣄⠀⠌⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠄⠀⣀⠀⠀⢀⠀⠄⡁⠂⠞⠛⠁⠀⠀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⢻⣿⣷⣻⡱⢋⠷⡙⢦⣿⣿⣿⠇⠀⠀⣿⣿⣿⡹⣿⢽⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣐⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣦⣿⠯⣀⠀⠀⠘⡈⠄⡐⢸⣿⡀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⡄⠀⠀⠀⠈⠛⠆⠀⢂⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⢀⠢⠀⠀⠌⡀⠐⠀⠀⠀⠀⢀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠙⢿⣷⣧⢋⠲⣭⣿⣿⣿⠏⠀⠀⠀⣿⣿⣷⣻⢿⣞⠦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠩⣄⠡⡐⢂⠐⢸⣿⠁⠀⠀⠀⠀⣸⣿⠑⡀⠀⠀⣮⣿⡄⠀⠀⠀⠀⠈⠐⠂⡐⡀⠂⠀⠀⠀⢀⠀⠀
		⠀⠀⢠⠀⠂⠀⠀⠂⠀⠁⠂⠀⠀⠁⢀⣤⣐⣾⣳⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⠗⡀⠀⠀⠙⠿⣷⣷⣿⣿⡿⠃⠀⠀⠀⠸⣿⣿⣿⣽⣻⣟⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⢀⣀⣤⣾⡟⢉⠀⠀⠀⠀⢹⡷⢀⠂⡐⢨⣿⠃⠀⠀⠀⣠⣿⠇⢘⠀⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⡀⠄⠀⠀⠀⠀
		⢀⣌⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⣾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠌⡀⠀⠀⠀⠀⠈⠿⣿⣷⣤⡀⠀⠀⠀⣼⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣽⡟⠋⢁⠀⠆⡄⠀⠀⢠⣿⡏⣀⠐⠠⠙⣿⡅⠀⠀⢠⣿⡏⠀⢌⠀⠀⠀⠘⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠁⠈⠐
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣠⣤⣭⣥⣮⣴⣯⣙⡿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⡿⠋⠐⡈⢀⠂⠌⠀⠀⠀⢘⡿⠉⡐⡈⠐⠈⣿⠃⠀⠀⣾⡟⠀⠌⡀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣫⣋⣝⣋⣛⣛⣛⣛⣡⣶⣿⣿⣿⣿⣿⡗⡴⢬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠋⢄⠂⠁⠰⠠⠌⠒⠀⠀⣰⠟⠁⠐⠠⠁⠡⢈⠧⠀⠀⣼⣿⠂⠡⠐⠠⠀⠀⠀⠀⠈⢿⠿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣻⢭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢛⠻⣛⢟⣻⣛⣏⣣⡽⣭⣿⣿⣿⣿⠅⡘⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠠⠑⠊⠀⠀⢀⠰⢠⠈⡐⢘⠀⠀⠠⡌⡐⠁⡐⠨⡁⠀⢀⣿⡿⠀⠀⢡⠂⠱⢤⠀⠀⠀⠈⣜⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠐⠨⣝⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠷⠻⠿⡛⢟⢫⡛⣽⣻⣿⣿⣿⣿⢂⡜⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⡌⠡⠂⠰⡀⠉⡀⠀⠀⠀⠤⢁⠰⠁⡐⠀⣾⡿⠇⠀⢀⣾⠇⢀⠂⡀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠀⠀⠀⠀⠀⠌⠄⢂⠁⡓⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣞⠿⡿⢿⠻⡖⣻⢻⢿⣿⣿⣿⣿⠀⠀⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠤⠘⠀⠀⠀⠀⠑⠬⡐⠀⠀⠀⠀⠓⠈⢄⠠⡀⡔⢋⠐⡀⣤⣿⠿⠀⠂⢈⠡⠀⠀⠀⡀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢠⡐⠈⡄⠠⠠⠌⡐⢨⢀⠰⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣳⣵⣮⣷⣾⣷⣿⣿⣿⣿⣿⣿⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢀⠀⠁⠀⠀⠀⠀⠀⠀⠈⠐⠀⠆⢀⠀⣌⠂⠔⡁⠂⠄⠂⣼⡿⠁⠀⠀⠀⠀⠀⢃⡐⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⢈⠡⢂⠤⠑⠀⠀⣼⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣴⣼⣤⣯⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠄⠣⠘⠁⠀⢀⠎⡐⠠⢉⢰⣭⡿⠀⠀⠀⠀⠀⠀⠀⠐⠤⡁⠂⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠀⢄⠡⢂⡀⢀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣟⣹⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠀⠈⠰⢀⠁⣦⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⢆⡁⠂⠄⠁⠈⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣻⠻⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠈⠀⠉⢀⠐⠂⠌⢛⠂⠐⠲⠛⠟⠻⠷⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡔⠠⢁⠂⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠘⠠⠈⠼⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢐⠠⢂⠄⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢿⡿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢣⠐⣁⠂⠄⡈⠙⠿⢦⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⢂⠌⠠⠀⢀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣷⡄⠀⠀⠀⠀⠀⠀⠄⠁⠀⡐⠀⠀⢠⠀⠠⣁⠂⡐⠈⠄⠒⡀⠀⠀⠀⠀⢀⣾⡟⠁⠀⠀⠀⢸⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⠠⠈⡄⠁⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣞⣧⣛⣦⣑⢦⣹⣿⣆⠀⠀⠀⠀⢀⠀⠀⠀⠄⠀⢌⡀⠀⡁⠀⡒⠀⠁⠚⣀⠐⠠⣤⣀⣴⡿⢋⡴⠀⠀⠀⠀⠸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡑⠈⠔⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⡻⣟⢿⡻⣟⡻⣿⣿⡿⢂⠔⡈⠄⠂⠄⠀⠀⠠⠀⠀⢘⡀⠀⠀⠈⠄⠀⠀⠀⠘⡄⡀⠉⢁⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡘⢠⠂⢂⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣯⣷⣿⣿⡇⢣⠐⠰⠈⡄⠀⠀⠀⠐⠀⠀⠰⠀⡀⠀⡀⠂⠀⠀⠀⠀⠐⠣⢄⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠔⡠⢈⠄⠀⢸⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣵⣯⣻⣽⣿⡿⠜⡤⠉⢦⣱⡞⠀⠀⠀⠀⠀⠀⠄⠃⠀⡐⠀⡀⠀⠀⠀⠀⠀⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠰⢡⠈⠄⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣽⣳⣯⣟⣿⣽⣷⢿⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢓⡴⢉⣾⡷⠀⠀⠀⠀⠀⠀⠀⠌⡀⠒⠀⠀⠆⠀⠀⢀⠀⠄⠡⢀⠁⠖⠀⠀⠀⠀⠀⡁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠒⠤⡈⠄⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣟⣯⣿⢷⣯⠿⣽⣻⣽⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡘⣬⢱⣼⡟⠁⠀⠀⠀⠀⠀⠀⠄⠠⠂⠄⠡⢀⠂⠀⠀⠈⡐⢈⠔⠀⠢⠄⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠁⢆⠠⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣻⣽⣞⣳⡞⣿⡽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣝⣲⣿⣿⠁⠀⠀⢀⠀⠀⠀⡀⠀⠑⡈⠄⡀⠂⠄⠠⢀⠡⠐⠈⠀⠀⠀⠈⠐⠀⠀⠄⡀⠀⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠩⠠⢀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⣷⢯⡷⣝⣮⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣧⣷⣿⣼⣿⠟⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⠁⠀⠐⠠⠁⢂⠐⢀⠂⠁⠀⠀⠀⠀⠀⠀⡐⣀⠒⠠⠑⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢈⠰⢁⠂⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⢾⡿⣽⢾⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠙⠛⠛⠛⠛⠉⠣⢙⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠠⠁⠀⠀⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠌⡐⠡⠂⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠒⡈⠄⠀⠀⢀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⡀⠄⢁⠂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⠄⣡⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀
		⠀⠄⠸⠐⠈⠀⠁⡀⠀⢀⠀⠈⠙⠿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠠⠀⢀⠂⠠⠈⠀⠄⠀⠈⠀⠀⠈⠀⠈⠐⠀⠀⡀⠀⢂⠐⡈⠄⠂⠁⠀⠀⠈⠀⠁⢠⠈⠀⠀
		⠀⠌⢢⠉⠄⠂⠀⠀⠐⠠⠀⠀⠀⠀⠈⠉⠙⠳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠈⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣂⠀⢀⠀⢀⠀⠀⠀⢠⠀⠀⠄⡀⠀⠂⢀⠀⠀⠄⡑⠈⠀⠀⠀⠀⠀⠀⠀⢀⠂⠈⠀
		⠀⠌⠰⠀⠌⢀⠀⠂⢀⠡⠀⡀⠁⠀⠂⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠄⠠⠀⠄⠂⠀⠀⠠⠀⠀⡁⢂⠀⠀⠌⢀⠐⠀⠂⠄⠐⠈⠀⠀⠀⠀⠀⠠⠈⢀⠀⠀
		⠀⡈⢡⠈⡐⠀⠀⠄⠀⠀⠐⠠⠈⠀⠐⠠⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠐⠈⠀⠈⢀⠀⠀⠀⠀⠁⠐⢀⠀⠈⡐⠈⢀⠀⠈⡐⢀⠁⠀⠀⠀⠀⠀⠌⡀⢈⠀⠀⠀
		⠀⠐⡠⢈⠐⠠⢁⠢⠌⡐⡈⢄⠠⠘⡀⠀⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠐⠈⢀⠀⠀⠀⠀⠀⠁⠀⠀⠐⠠⠀⢀⠠⠀⠄⠂⢈⠀⠀⠀⠀⠀⠀⠀⠄⠂⠈⠀
		⠠⢁⠐⠤⠉⠂⡄⠣⠐⠡⠐⠂⠑⠠⡐⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢈⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⠄⡀⢂⠠⠀⠠⠀⠀⠀⠀⠀⠀⠨⠐⠀⠀
		⠀⢂⠘⠄⡡⠂⠄⠡⠌⡡⠌⢠⠁⠂⡐⠈⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠐⠠⢈⡐⠤⠑⡈⠱⡈⠔⡈⠄⡈⠄⠐⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡁⠂⡔⠠⢃⠰⡁⢌⠒⠄⠠⠀⠀⠀⢎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠐⠀⠀⠀
		⠀⠄⡡⠂⢅⢂⠡⡘⢠⠉⠤⢁⠂⠀⢘⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠈⡐⢠⠑⡈⢄⠂⡅⢢⠘⠠⠁⠀⠀⢌⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⢦⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⠠⠁⠎⡘⢠⠘⢠⠃⠌⡁⠂⠄⠀⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢌⢳⡚⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠉⠡⠀⠁⠀⠄⠀⠐⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⢀⠀⠀⢀⣀⠀⠀⠀⡀⠀⢀⣀⣀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠃⢦⠀⠄⡐⢀⠂⠄⢈⠀⠄⡀⠀⠀⠉⠈⠁⠀⠉⠀⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⡀⠠⢀⠀⠌⡁⠎⢁⠊⠄⠠⢀⡴⠊⠀⠁⠐⣀⠀⠈⠐⠂⠀⠀⠄⠢⠐⠂⡄⠀⠀⠀⠀⠀⠀⠀⠀⢋⠄⢀⠢⠈⠆⠰⢈⠒⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠈⠄⠡⠈⠐⠀⠂⣛⠋⠀⠁⠀⠀⠁⠈⠀⡐⢄⠂⡐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠆⠀⠀⠀⠀⠀⠑⠢⠄⡁⠢⢀⡀⣀⠀⠀⠀⠠⡈⠄⢠⠃⢌⠀⠀⠆⠄⠃⢄⠠⡀⠤⡐⢌⠂⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠈⠐⠈⢀⠐⡀⠐⠀⠛⠃⠘⠀⠆⠁⠀⠀⢀⠁⢂⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡠⡐⠤⡉⠌⣁⠂⠔⡈⢄⠊⡔⢀⠀⠠⢈⠐⡠⢂⡑⠢⠙⠄⠦⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣠⣴⣍⣀⣀⣤⡀⠀⠀⠀⢸⣧⣔⣤⣸⣤⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠈⠀⠀⠀⠐⡈⠂⢅⠂⡡⠐⡈⡄⠃⠀⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⣀⣴⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠌⠠⠘⢀⠡⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠋⠀⣀⣴⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠱⠈⠄⢃⠐⠠⢁⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠂⠀⢠⠶⠂⢀⣿⣿⠿⣍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠠⢀⠐⠈⠀⢀⡃⠤⢈⠠⠄⠀⣹⢿⢶⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⣴⣿⣿⣫⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠐⠤⣤⣀⡁⢂⠀⠀⠀⠀⠀⠀⠂⢀⠠⠀⠙⣿⣤⠈⠙⠹⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⢀⣾⣟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢀⣠⡾⠂⠀⠀⠀⠀⠀⠈⠙⢷⡌⠐⡀⠀⠀⢂⠁⠀⠂⠰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⡛⠛⠿⠿⣿⣿⣧⣾⡏⠀⠀⠀⠀⠀⢀⣠⣶⣿⣯⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣤⡀⠀⠀⠄⡂⢁⠒⠰⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⡀⡉⠙⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡱⢌⢎⡹⠤⡑⠈⠄⡐⠠⠹⣿⡇⠀⠀⠀⠀⠀⠐⠛⠛⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢢⠀⢀⠀⠄⢀⠃⠀⠀⠀⠀⢰⣿⡁⣠⣴⠞⠉⠁⠀⠀⠈⠉⠳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢎⡷⣩⢎⠦⣑⠢⢄⠁⡂⢄⠂⡡⢿⣧⠀⠀⠙⠂⠀⠀⠀⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⢊⠐⠀⠡⠀⠀⠀⠀⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠶⣓⢮⠓⣌⢲⣈⣦⣑⣂⡌⡰⢹⣿⠀⠀⢀⣠⠟⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡁⠂⠔⡈⠌⠐⠀⠀⣠⣾⠟⠡⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⣀⠀⠀⠀⣼⡋⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣎⢯⣵⣮⣿⣿⣿⣟⣻⣿⣿⣿⣰⣿⣿⠆⠀⣾⠉⠀⠀⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡀⢀⠈⡔⢀⠂⡀⣾⡿⠁⠈⠀⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠹⠷⣦⠸⠟⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⣝⠾⡻⢭⡙⠿⡟⠿⠿⢟⣸⣿⣿⡿⠁⠀⣸⣷⡆⠀⠀⠀⣤⡻⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡵⠀⡐⠐⠀⡀⣴⣿⠃⠀⠀⠈⢤⡀⠀⠀⠀⠀⢀⡄⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡆⠀⠀⠀⠘⣿⣿⣿⣳⣿⢉⣿⣿⡻⣿⣿⣏⢷⣩⢗⡹⢢⣍⡒⣈⢦⠑⠢⢌⣿⣿⣷⣬⣾⡿⠉⠀⠀⠀⠀⠈⠻⢷⣭⠉⠿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠏⠁⢀⠨⠔⠀⠀⣿⠃⠀⠀⠀⠀⠀⠉⠆⠀⢰⣾⡋⠄⡐⠠⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠄⠀⡁⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣆⡀⠆⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠸⣿⣿⣿⣧⢊⠹⣿⣿⣽⡳⣞⢧⣛⢮⡝⣯⣛⣿⠿⢋⠇⣜⣼⣿⣏⣽⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⣯⣰⠌⠀⢀⠂⡌⠠⠁⣿⠀⠀⠀⠀⠀⠀⠀⣹⣠⠿⠋⠀⠀⠀⠀⠂⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣆⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣧⣌⣻⢿⣷⣹⢮⡝⣮⢽⡲⣟⠼⣏⢒⡸⢘⠛⡛⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠷⣶⣤⣼⣿⡀⠀⣀⣀⣤⣶⠿⠋⠁⠁⠀⠀⠀⢣⢀⠁⢂⢳⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠹⣿⣿⣿⢻⠿⣿⢻⡞⣧⡻⡜⣧⢯⡳⢎⡳⡍⠦⣿⣦⣯⣼⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠹⣧⢩⣿⣿⣿⣯⣤⣀⡒⠠⠄⠀⠀⠀⢆⠈⡐⠠⢈⠀⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⢹⣿⣯⢏⡷⣎⠿⣜⣧⡷⣽⢶⣣⠿⣍⡳⣍⠒⣩⢙⡛⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠟⠁⠀⠈⠉⠛⢿⣧⡌⠒⠀⡐⠨⡐⠠⠁⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⢀⠸⣷⡀⠀⠀⠀⠀⢸⣿⠀⠀⣴⣶⣶⢾⣿⣏⢾⣱⢭⣻⡜⣶⢫⣷⢫⡾⣝⢯⣳⣌⠳⡄⢣⢜⣿⡇⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⠀⠀⠀⠀⠀⠀⠀⠙⣿⣦⡁⢀⠂⠡⢂⠁⡐⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠊⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡘⣿⡄⠀⠀⠀⣸⡷⢀⣾⣿⣿⣷⣾⢿⡜⣧⢻⣏⢷⣹⡞⣽⢮⣗⣻⣭⣿⣷⣿⣿⣾⣷⣿⡿⢻⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⠟⠋⠁⢀⠈⠿⣦⣀⠀⠀⠀⠀⠀⠈⠛⢿⣦⠈⡐⢀⠂⡐⠀⠀⠀⢀⣠⣿⠃⠀⠀⠀⠀⢀⡤⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣀⣤⣾⣿⣡⣾⣿⣿⡇⢿⣿⣧⡻⣜⡷⣞⠯⣇⠿⣥⢟⣾⣷⣿⣿⣿⣸⣿⠉⠙⠿⣷⣏⣀⢢⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⢉⣠⡄⠈⠙⢻⣦⡌⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⡷⢀⠂⡐⠀⢀⣠⣴⣾⡟⢱⣦⡀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⢖⠲⠻⠥⣝⣻⣿⣷⣿⣿⣿⣿⣿⣿⠀⠻⣿⣷⡭⣿⢩⠞⣌⠳⣌⢯⡩⢍⠲⣸⣿⡿⣿⣦⣀⠀⠈⠉⠛⠿⣿⣷⣦⣄⡀⠀⢀⣤⣶⠟⠋⠐⠋⠉⠀⠀⠀⠀⠙⢿⣆⢸⣧⠀⠀⠀⠀⠀⣰⣿⠋⡰⠀⡄⠡⣈⣽⡿⠋⠀⠀⠻⠛⣦⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⣂⠿⠿⠛⢁⣀⣦⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⣿⣾⡵⣫⠞⣌⠷⣞⢲⡙⡌⢧⣹⣿⠁⢹⣿⣿⣿⣶⣤⣤⣄⣠⣈⡝⠿⣷⣶⡿⠋⢀⠐⣈⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠻⣷⣄⠀⠀⣼⡿⠃⢀⠡⠁⡐⢡⣿⠋⠁⠀⠀⠀⠀⣴⣨⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢀⠐⡘⢉⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠈⢿⣷⣏⡞⣌⠞⣬⠳⡞⣌⣧⣿⡏⠀⠈⣿⣿⢿⣻⡟⣿⠿⣿⢿⣿⣦⣤⣉⠡⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡉⢟⣠⣾⠟⠁⠈⠴⡀⠂⠄⢹⣿⠀⠀⠀⠀⠀⠀⠈⣿⠏⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠌⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠠⠤⠞⠋⣐⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣂⠀⠀⠻⣿⣷⡘⡜⣚⠟⣴⣺⣿⡿⠁⠀⠀⢿⣿⣿⣳⢿⣹⢟⡦⢸⣿⣿⣿⣿⣷⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣴⣿⡏⠠⠀⠀⠰⠁⠌⡠⢹⣿⡀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠂⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠠⢁⠐⠀⡐⣤⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠟⡀⠀⠀⠈⠻⣿⣦⣑⣮⣿⣿⠿⠁⠀⠀⠀⣽⣿⣿⣿⢯⣟⣾⢧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⡟⠀⠁⠊⣄⠡⠘⠠⠐⢸⣿⠁⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⣤⣿⡀⠀⠀⠀⠀⠀⠘⠄⣂⠌⠀⡀⠀⠀⢀⡀⠀
		⠀⠀⠀⠄⠈⠀⠀⠂⠀⠈⠔⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠈⠻⣿⡿⠟⠃⠀⠀⠀⠀⣰⣿⣿⣿⣿⣟⡾⣽⠮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡟⠩⠀⠀⠀⠀⢹⡇⠈⠄⡁⢬⣿⠄⠀⠀⠀⣠⣿⠃⠤⠁⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠘⠀⢀⠀⠀⡀⠀⠀
		⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⠿⣿⣿⣿⣷⣶⣤⣤⣄⣀⣀⠀⣰⣿⣿⣿⣿⣿⣿⣿⢿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢀⣼⡿⠋⢁⠀⡒⡀⠀⠀⢠⣿⣋⠀⢂⠐⠨⣿⡀⠀⠀⢠⣿⠏⡀⠘⡄⠀⠀⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠑⠠
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣽⣿⣟⣻⣟⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣰⣿⠛⢀⠢⢀⠂⡁⠀⠀⠀⣘⡟⠁⡉⠤⠈⠄⠻⠁⠀⠀⣾⡟⠀⡐⠈⠀⠀⠀⠀⠹⡏⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣤⣭⣽⣿⣛⠻⠿⠿⣿⣾⣿⣿⣿⣿⣿⣿⢴⡨⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣾⠛⡁⠐⠀⠄⠂⠆⠡⠀⠀⣴⠟⠁⠐⡐⠂⢁⠠⡃⠀⠀⢸⡟⠠⠁⠠⢁⠀⠀⠀⠀⠀⠙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣟⣿⣿⢿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣏⢂⡉⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠠⠄⠖⠀⠀⠀⢀⡌⠰⢀⠁⢚⠀⠀⠀⡆⡐⠁⡀⠆⠡⠀⠀⣻⠑⠀⠀⠡⠂⠒⢤⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣿⢿⡿⣷⣶⣶⣭⣽⣿⣿⣿⣿⣿⡇⢢⠔⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⠀⠀⠀⢈⠆⠰⢁⠢⡘⠌⠀⠀⠀⠀⠤⢁⠰⠀⡁⠀⡰⠃⠄⠀⠀⣰⠁⠌⠠⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
		⠰⠀⠀⠀⠀⠀⠀⡰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣶⣦⣯⣝⣻⣿⣿⣿⣿⣿⡇⠈⢀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠔⣈⠠⠀⠀⠀⠀⠥⡂⠁⠀⠀⠀⠃⠢⠐⡄⡀⠤⠑⢈⠀⣠⣾⠯⠀⠈⠄⢁⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⣁⠃⠄⡠⢐⠂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣮⣭⣽⣛⡻⢿⣿⣿⣿⣿⣿⣧⣶⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⡐⠠⢀⠀⡌⠡⠐⡈⠄⡁⠂⢬⡛⠀⠀⠀⠀⠀⠈⠐⡀⢂⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠘⡠⢁⠆⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣭⣽⣻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠐⡄⠃⠁⠀⠈⡅⠘⠠⠌⠠⣡⠞⠀⠀⠀⠀⠀⠀⠀⠀⠒⡠⠀⠀⠀⠠⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠀⡄⠃⢈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠡⢀⠃⡐⢠⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠐⠡⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠱⢀⠂⠰⢁⠂⠀⠒⠒⠒⠶⠖⠶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠌⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⢥⡄⠂⡁⢂⠡⣆⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠐⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⡻⣝⢫⢟⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⡃⠄⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠷⢀⡐⠠⠀⠌⠛⠿⣷⡄⠀⠀⠀⠀⠀⢀⣴⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠶⡱⢮⣵⣾⣿⣾⣷⣶⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠁⢂⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡒⠀⠀⠐⡀⠈⢡⠈⡀⢂⠄⠸⡄⠀⠀⠀⠀⢀⣿⠏⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡁⠂⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⣾⣭⠷⣍⢧⢫⡝⢮⡱⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠙⣠⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⢄⡃⠀⠄⠂⣡⠀⠀⠈⡀⠌⠑⣦⣀⣴⡿⢋⡐⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠁⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣽⢯⣿⡻⣜⢎⠷⣚⠷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠆⠀⠉⠁⠂⠉⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⡄⠀⠀⠀⠓⢦⡈⠉⢡⣶⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡁⢂⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⣽⢿⣾⢷⡭⣎⣷⣽⡾⣵⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⡀⠀⠈⠁⠀⠐⠂⠀⠀⠀⠀⠀⠀⢩⠆⠀⢈⠀⡀⠀⠀⠀⠀⠈⢻⣦⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣯⣟⣯⡟⣼⣡⢯⣹⣱⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⢀⡘⠀⠀⠀⠀⠀⠀⠘⠆⠁⠠⠀⡀⠀⠀⠀⠀⠀⣸⠿⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠌⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣽⣿⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣬⣀⠈⠁⠀⠀⠀⠀⠀⣠⣼⣆⣈⡀⠀⠆⠀⠀⠀⡠⠐⢀⠀⠈⠳⢀⠀⠀⠀⠀⠀⣀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⢤⣶⣿⣿⣿⠟⠿⠿⠿⠗⠀⠠⢿⣷⡈⠄⠈⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡀⠡⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⠿⣿⣿⣿⣿⣿⣿⣶⣾⣥⣥⣠⣄⠀⠘⠷⠀⠀⠀⢀⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⡁⠆⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⡼⣛⣧⣟⣶⣭⢟⡿⣿⣿⢉⠛⠿⣿⣿⣶⣤⣧⡄⠂⠤⢈⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠔⡈⠄⠀⠀⠙⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣳⠿⣝⡾⣽⢿⣿⣾⣷⣿⣿⣷⣮⣤⣀⠀⠈⠙⡟⠃⢈⠐⠠⠊⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⡔⢁⠂⠀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⣿⡹⣷⣫⢏⡿⣿⣿⣷⣦⡉⠻⢿⣿⣷⣶⣬⣿⡆⠀⠈⢄⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡐⢈⠂⡈⠀⠐⠀⠄⠈⠀⠀⠤⠀⠀⠄⢠⠀⠠⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡾⣝⣷⣻⣿⣾⣧⡙⠻⣿⣿⣶⣀⠀⠙⠻⢿⣿⣷⠀⠈⡀⢀⠡⠀⠀⠈⠀⠈⠀⠁⠈⠄⠀⡀
		⠀⡐⢌⡐⠀⠌⠀⠀⠂⠈⠀⠀⡀⠀⠁⠂⠠⠁⠄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠿⣿⣿⣧⠈⠹⢿⣿⣿⣤⣴⠿⠉⠃⠀⠀⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⡐⠤⡀⢃⠀⡈⠄⠠⠁⠂⢀⠀⠀⠀⠄⠑⡈⠠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠄⠐⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⢿⣿⣿⣿⡿⠁⠀⠀⠘⠿⠟⠁⠰⠶⠚⠉⠛⠈⠀⠀⢀⠀⠀⠡⠀⢀⠂⠀⠈⠀⠀⠁⢀⠈⠀⠠⠀
		⠀⠐⢠⠁⠂⠀⠄⡀⠄⠂⠀⠂⠄⡀⠄⡈⢄⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠠⠀⠁⡐⠀⠀⠀⠀⠀⠀⠀⠌⢀⠈⠀⢀⠀
		⠀⠌⣀⠊⣁⠂⠔⡠⠐⡐⠈⢄⠠⠐⠠⢀⠈⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠡⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠐⠀⠀⠐⡈⠐⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⢀⠂⠄⡘⢠⠈⡐⡁⠣⠐⡁⠂⠱⠈⠔⡈⠠⠈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠠⠁⠄⡁⠀⠀⠄⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠠⢈⠰⢁⠂⡁⠄⢠⠡⢡⠐⡁⢆⠉⠄⠠⠁⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠄⠀⠈⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⡐⡀⢂⠂⠱⢈⠔⠡⠒⡄⢂⠐⡀⠌⠀⢀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀
		⡐⢀⠂⢍⠰⢈⠢⣁⠣⢐⠂⠄⢀⠠⠈⢀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣹⣟⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀
		⠄⠃⡌⡀⠒⠤⢁⠄⢣⢈⡐⢈⠀⡀⠐⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⢟⡾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡌⡑⢠⠈⠥⡈⢆⡘⢄⢂⠈⠀⡀⠀⠂⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡵⢮⡝⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⡑⠌⡊⠡⠘⠤⢈⠢⠈⢀⠁⠀⠈⠄⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⢦⢻⣜⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠉⠡⠀⠁⠀⠄⠀⠐⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⢀⠀⠀⢀⣀⠀⠀⠀⡀⠀⢀⣀⣀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠃⢦⠀⠄⡐⢀⠂⠄⢈⠀⠄⡀⠀⠀⠉⠈⠁⠀⠉⠀⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⡀⠠⢀⠀⠌⡁⠎⢁⠊⠄⠠⢀⡴⠊⠀⠁⠐⣀⠀⠈⠐⠂⠀⠀⠄⠢⠐⠂⡄⠀⠀⠀⠀⠀⠀⠀⠀⢋⠄⢀⠢⠈⠆⠰⢈⠒⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠈⠄⠡⠈⠐⠀⠂⣛⠋⠀⠁⠀⠀⠁⠈⠀⡐⢄⠂⡐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠆⠀⠀⠀⠀⠀⠑⠢⠄⡁⠢⢀⡀⣀⠀⠀⠀⠠⡈⠄⢠⠃⢌⠀⠀⠆⠄⠃⢄⠠⡀⠤⡐⢌⠂⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⠈⠐⠈⢀⠐⡀⠐⠀⠛⠃⠘⠀⠆⠁⠀⠀⢀⠁⢂⠐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡠⡐⠤⡉⠌⣁⠂⠔⡈⢄⠊⡔⢀⠀⠠⢈⠐⡠⢂⡑⠢⠙⠄⠦⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣠⣴⣍⣀⣀⣤⡀⠀⠀⠀⢸⣧⣔⣤⣸⣤⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠈⠀⠀⠀⠐⡈⠂⢅⠂⡡⠐⡈⡄⠃⠀⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⣀⣴⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠌⠠⠘⢀⠡⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠋⠀⣀⣴⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠱⠈⠄⢃⠐⠠⢁⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠂⠀⢠⠶⠂⢀⣿⣿⠿⣍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠠⢀⠐⠈⠀⢀⡃⠤⢈⠠⠄⠀⣹⢿⢶⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⣴⣿⣿⣫⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠐⠤⣤⣀⡁⢂⠀⠀⠀⠀⠀⠀⠂⢀⠠⠀⠙⣿⣤⠈⠙⠹⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⢀⣾⣟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢀⣠⡾⠂⠀⠀⠀⠀⠀⠈⠙⢷⡌⠐⡀⠀⠀⢂⠁⠀⠂⠰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⡛⠛⠿⠿⣿⣿⣧⣾⡏⠀⠀⠀⠀⠀⢀⣠⣶⣿⣯⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣤⡀⠀⠀⠄⡂⢁⠒⠰⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⡀⡉⠙⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡱⢌⢎⡹⠤⡑⠈⠄⡐⠠⠹⣿⡇⠀⠀⠀⠀⠀⠐⠛⠛⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢢⠀⢀⠀⠄⢀⠃⠀⠀⠀⠀⢰⣿⡁⣠⣴⠞⠉⠁⠀⠀⠈⠉⠳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢎⡷⣩⢎⠦⣑⠢⢄⠁⡂⢄⠂⡡⢿⣧⠀⠀⠙⠂⠀⠀⠀⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⢊⠐⠀⠡⠀⠀⠀⠀⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠶⣓⢮⠓⣌⢲⣈⣦⣑⣂⡌⡰⢹⣿⠀⠀⢀⣠⠟⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡁⠂⠔⡈⠌⠐⠀⠀⣠⣾⠟⠡⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⣀⠀⠀⠀⣼⡋⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣎⢯⣵⣮⣿⣿⣿⣟⣻⣿⣿⣿⣰⣿⣿⠆⠀⣾⠉⠀⠀⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡀⢀⠈⡔⢀⠂⡀⣾⡿⠁⠈⠀⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠹⠷⣦⠸⠟⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⣝⠾⡻⢭⡙⠿⡟⠿⠿⢟⣸⣿⣿⡿⠁⠀⣸⣷⡆⠀⠀⠀⣤⡻⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡵⠀⡐⠐⠀⡀⣴⣿⠃⠀⠀⠈⢤⡀⠀⠀⠀⠀⢀⡄⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡆⠀⠀⠀⠘⣿⣿⣿⣳⣿⢉⣿⣿⡻⣿⣿⣏⢷⣩⢗⡹⢢⣍⡒⣈⢦⠑⠢⢌⣿⣿⣷⣬⣾⡿⠉⠀⠀⠀⠀⠈⠻⢷⣭⠉⠿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠏⠁⢀⠨⠔⠀⠀⣿⠃⠀⠀⠀⠀⠀⠉⠆⠀⢰⣾⡋⠄⡐⠠⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠄⠀⡁⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣆⡀⠆⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠸⣿⣿⣿⣧⢊⠹⣿⣿⣽⡳⣞⢧⣛⢮⡝⣯⣛⣿⠿⢋⠇⣜⣼⣿⣏⣽⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⣯⣰⠌⠀⢀⠂⡌⠠⠁⣿⠀⠀⠀⠀⠀⠀⠀⣹⣠⠿⠋⠀⠀⠀⠀⠂⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣆⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣧⣌⣻⢿⣷⣹⢮⡝⣮⢽⡲⣟⠼⣏⢒⡸⢘⠛⡛⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠷⣶⣤⣼⣿⡀⠀⣀⣀⣤⣶⠿⠋⠁⠁⠀⠀⠀⢣⢀⠁⢂⢳⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠹⣿⣿⣿⢻⠿⣿⢻⡞⣧⡻⡜⣧⢯⡳⢎⡳⡍⠦⣿⣦⣯⣼⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠹⣧⢩⣿⣿⣿⣯⣤⣀⡒⠠⠄⠀⠀⠀⢆⠈⡐⠠⢈⠀⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⢹⣿⣯⢏⡷⣎⠿⣜⣧⡷⣽⢶⣣⠿⣍⡳⣍⠒⣩⢙⡛⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠟⠁⠀⠈⠉⠛⢿⣧⡌⠒⠀⡐⠨⡐⠠⠁⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⢀⠸⣷⡀⠀⠀⠀⠀⢸⣿⠀⠀⣴⣶⣶⢾⣿⣏⢾⣱⢭⣻⡜⣶⢫⣷⢫⡾⣝⢯⣳⣌⠳⡄⢣⢜⣿⡇⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⠀⠀⠀⠀⠀⠀⠀⠙⣿⣦⡁⢀⠂⠡⢂⠁⡐⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠊⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡘⣿⡄⠀⠀⠀⣸⡷⢀⣾⣿⣿⣷⣾⢿⡜⣧⢻⣏⢷⣹⡞⣽⢮⣗⣻⣭⣿⣷⣿⣿⣾⣷⣿⡿⢻⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⠟⠋⠁⢀⠈⠿⣦⣀⠀⠀⠀⠀⠀⠈⠛⢿⣦⠈⡐⢀⠂⡐⠀⠀⠀⢀⣠⣿⠃⠀⠀⠀⠀⢀⡤⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣀⣤⣾⣿⣡⣾⣿⣿⡇⢿⣿⣧⡻⣜⡷⣞⠯⣇⠿⣥⢟⣾⣷⣿⣿⣿⣸⣿⠉⠙⠿⣷⣏⣀⢢⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⢉⣠⡄⠈⠙⢻⣦⡌⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⡷⢀⠂⡐⠀⢀⣠⣴⣾⡟⢱⣦⡀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⢖⠲⠻⠥⣝⣻⣿⣷⣿⣿⣿⣿⣿⣿⠀⠻⣿⣷⡭⣿⢩⠞⣌⠳⣌⢯⡩⢍⠲⣸⣿⡿⣿⣦⣀⠀⠈⠉⠛⠿⣿⣷⣦⣄⡀⠀⢀⣤⣶⠟⠋⠐⠋⠉⠀⠀⠀⠀⠙⢿⣆⢸⣧⠀⠀⠀⠀⠀⣰⣿⠋⡰⠀⡄⠡⣈⣽⡿⠋⠀⠀⠻⠛⣦⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⣂⠿⠿⠛⢁⣀⣦⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⣿⣾⡵⣫⠞⣌⠷⣞⢲⡙⡌⢧⣹⣿⠁⢹⣿⣿⣿⣶⣤⣤⣄⣠⣈⡝⠿⣷⣶⡿⠋⢀⠐⣈⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠻⣷⣄⠀⠀⣼⡿⠃⢀⠡⠁⡐⢡⣿⠋⠁⠀⠀⠀⠀⣴⣨⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢀⠐⡘⢉⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠈⢿⣷⣏⡞⣌⠞⣬⠳⡞⣌⣧⣿⡏⠀⠈⣿⣿⢿⣻⡟⣿⠿⣿⢿⣿⣦⣤⣉⠡⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡉⢟⣠⣾⠟⠁⠈⠴⡀⠂⠄⢹⣿⠀⠀⠀⠀⠀⠀⠈⣿⠏⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠌⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠠⠤⠞⠋⣐⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣂⠀⠀⠻⣿⣷⡘⡜⣚⠟⣴⣺⣿⡿⠁⠀⠀⢿⣿⣿⣳⢿⣹⢟⡦⢸⣿⣿⣿⣿⣷⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣴⣿⡏⠠⠀⠀⠰⠁⠌⡠⢹⣿⡀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠂⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠠⢁⠐⠀⡐⣤⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠟⡀⠀⠀⠈⠻⣿⣦⣑⣮⣿⣿⠿⠁⠀⠀⠀⣽⣿⣿⣿⢯⣟⣾⢧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⡟⠀⠁⠊⣄⠡⠘⠠⠐⢸⣿⠁⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⣤⣿⡀⠀⠀⠀⠀⠀⠘⠄⣂⠌⠀⡀⠀⠀⢀⡀⠀
		⠀⠀⠀⠄⠈⠀⠀⠂⠀⠈⠔⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠈⠻⣿⡿⠟⠃⠀⠀⠀⠀⣰⣿⣿⣿⣿⣟⡾⣽⠮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡟⠩⠀⠀⠀⠀⢹⡇⠈⠄⡁⢬⣿⠄⠀⠀⠀⣠⣿⠃⠤⠁⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠘⠀⢀⠀⠀⡀⠀⠀
		⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⠿⣿⣿⣿⣷⣶⣤⣤⣄⣀⣀⠀⣰⣿⣿⣿⣿⣿⣿⣿⢿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢀⣼⡿⠋⢁⠀⡒⡀⠀⠀⢠⣿⣋⠀⢂⠐⠨⣿⡀⠀⠀⢠⣿⠏⡀⠘⡄⠀⠀⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠑⠠
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣽⣿⣟⣻⣟⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣰⣿⠛⢀⠢⢀⠂⡁⠀⠀⠀⣘⡟⠁⡉⠤⠈⠄⠻⠁⠀⠀⣾⡟⠀⡐⠈⠀⠀⠀⠀⠹⡏⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣤⣭⣽⣿⣛⠻⠿⠿⣿⣾⣿⣿⣿⣿⣿⣿⢴⡨⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣾⠛⡁⠐⠀⠄⠂⠆⠡⠀⠀⣴⠟⠁⠐⡐⠂⢁⠠⡃⠀⠀⢸⡟⠠⠁⠠⢁⠀⠀⠀⠀⠀⠙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣟⣿⣿⢿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣏⢂⡉⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠠⠄⠖⠀⠀⠀⢀⡌⠰⢀⠁⢚⠀⠀⠀⡆⡐⠁⡀⠆⠡⠀⠀⣻⠑⠀⠀⠡⠂⠒⢤⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣿⢿⡿⣷⣶⣶⣭⣽⣿⣿⣿⣿⣿⡇⢢⠔⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⠀⠀⠀⢈⠆⠰⢁⠢⡘⠌⠀⠀⠀⠀⠤⢁⠰⠀⡁⠀⡰⠃⠄⠀⠀⣰⠁⠌⠠⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
		⠰⠀⠀⠀⠀⠀⠀⡰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣶⣦⣯⣝⣻⣿⣿⣿⣿⣿⡇⠈⢀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠔⣈⠠⠀⠀⠀⠀⠥⡂⠁⠀⠀⠀⠃⠢⠐⡄⡀⠤⠑⢈⠀⣠⣾⠯⠀⠈⠄⢁⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⣁⠃⠄⡠⢐⠂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣮⣭⣽⣛⡻⢿⣿⣿⣿⣿⣿⣧⣶⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⡐⠠⢀⠀⡌⠡⠐⡈⠄⡁⠂⢬⡛⠀⠀⠀⠀⠀⠈⠐⡀⢂⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠘⡠⢁⠆⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣭⣽⣻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠐⡄⠃⠁⠀⠈⡅⠘⠠⠌⠠⣡⠞⠀⠀⠀⠀⠀⠀⠀⠀⠒⡠⠀⠀⠀⠠⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠀⡄⠃⢈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠡⢀⠃⡐⢠⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠐⠡⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠱⢀⠂⠰⢁⠂⠀⠒⠒⠒⠶⠖⠶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠌⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⢥⡄⠂⡁⢂⠡⣆⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠐⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⡻⣝⢫⢟⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⡃⠄⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠷⢀⡐⠠⠀⠌⠛⠿⣷⡄⠀⠀⠀⠀⠀⢀⣴⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠶⡱⢮⣵⣾⣿⣾⣷⣶⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠁⢂⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡒⠀⠀⠐⡀⠈⢡⠈⡀⢂⠄⠸⡄⠀⠀⠀⠀⢀⣿⠏⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡁⠂⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⣾⣭⠷⣍⢧⢫⡝⢮⡱⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠙⣠⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⢄⡃⠀⠄⠂⣡⠀⠀⠈⡀⠌⠑⣦⣀⣴⡿⢋⡐⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⠁⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣽⢯⣿⡻⣜⢎⠷⣚⠷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠆⠀⠉⠁⠂⠉⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⡄⠀⠀⠀⠓⢦⡈⠉⢡⣶⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡁⢂⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⣽⢿⣾⢷⡭⣎⣷⣽⡾⣵⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⡀⠀⠈⠁⠀⠐⠂⠀⠀⠀⠀⠀⠀⢩⠆⠀⢈⠀⡀⠀⠀⠀⠀⠈⢻⣦⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣯⣟⣯⡟⣼⣡⢯⣹⣱⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⢀⡘⠀⠀⠀⠀⠀⠀⠘⠆⠁⠠⠀⡀⠀⠀⠀⠀⠀⣸⠿⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠌⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣽⣿⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣬⣀⠈⠁⠀⠀⠀⠀⠀⣠⣼⣆⣈⡀⠀⠆⠀⠀⠀⡠⠐⢀⠀⠈⠳⢀⠀⠀⠀⠀⠀⣀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⢤⣶⣿⣿⣿⠟⠿⠿⠿⠗⠀⠠⢿⣷⡈⠄⠈⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡀⠡⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⠿⣿⣿⣿⣿⣿⣿⣶⣾⣥⣥⣠⣄⠀⠘⠷⠀⠀⠀⢀⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⡁⠆⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⡼⣛⣧⣟⣶⣭⢟⡿⣿⣿⢉⠛⠿⣿⣿⣶⣤⣧⡄⠂⠤⢈⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠔⡈⠄⠀⠀⠙⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣳⠿⣝⡾⣽⢿⣿⣾⣷⣿⣿⣷⣮⣤⣀⠀⠈⠙⡟⠃⢈⠐⠠⠊⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⡔⢁⠂⠀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⣿⡹⣷⣫⢏⡿⣿⣿⣷⣦⡉⠻⢿⣿⣷⣶⣬⣿⡆⠀⠈⢄⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡐⢈⠂⡈⠀⠐⠀⠄⠈⠀⠀⠤⠀⠀⠄⢠⠀⠠⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡾⣝⣷⣻⣿⣾⣧⡙⠻⣿⣿⣶⣀⠀⠙⠻⢿⣿⣷⠀⠈⡀⢀⠡⠀⠀⠈⠀⠈⠀⠁⠈⠄⠀⡀
		⠀⡐⢌⡐⠀⠌⠀⠀⠂⠈⠀⠀⡀⠀⠁⠂⠠⠁⠄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠿⣿⣿⣧⠈⠹⢿⣿⣿⣤⣴⠿⠉⠃⠀⠀⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠀⡐⠤⡀⢃⠀⡈⠄⠠⠁⠂⢀⠀⠀⠀⠄⠑⡈⠠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠄⠐⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⢿⣿⣿⣿⡿⠁⠀⠀⠘⠿⠟⠁⠰⠶⠚⠉⠛⠈⠀⠀⢀⠀⠀⠡⠀⢀⠂⠀⠈⠀⠀⠁⢀⠈⠀⠠⠀
		⠀⠐⢠⠁⠂⠀⠄⡀⠄⠂⠀⠂⠄⡀⠄⡈⢄⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠠⠀⠁⡐⠀⠀⠀⠀⠀⠀⠀⠌⢀⠈⠀⢀⠀
		⠀⠌⣀⠊⣁⠂⠔⡠⠐⡐⠈⢄⠠⠐⠠⢀⠈⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠡⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠐⠀⠀⠐⡈⠐⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⢀⠂⠄⡘⢠⠈⡐⡁⠣⠐⡁⠂⠱⠈⠔⡈⠠⠈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠠⠁⠄⡁⠀⠀⠄⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠠⢈⠰⢁⠂⡁⠄⢠⠡⢡⠐⡁⢆⠉⠄⠠⠁⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠄⠀⠈⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⡐⡀⢂⠂⠱⢈⠔⠡⠒⡄⢂⠐⡀⠌⠀⢀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀
		⡐⢀⠂⢍⠰⢈⠢⣁⠣⢐⠂⠄⢀⠠⠈⢀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣹⣟⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀
		⠄⠃⡌⡀⠒⠤⢁⠄⢣⢈⡐⢈⠀⡀⠐⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⢟⡾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡌⡑⢠⠈⠥⡈⢆⡘⢄⢂⠈⠀⡀⠀⠂⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡵⢮⡝⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⡑⠌⡊⠡⠘⠤⢈⠢⠈⢀⠁⠀⠈⠄⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⢦⢻⣜⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠉⠡⠈⠁⠀⠄⠀⠐⠆⠀⠀⠀⠉⠉⠈⠁⠈⠁⠈⠉⠀⢀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⡀⠀⢀⠀⡀⠉⠀⠀⠉⠀⠉⠀⠀⠀⠀⠀⠀⠉⠀⠉⠑⢤⠀⠄⠠⠐⡀⠂⡀⠄⠠⠀⠀⠀⠉⠀⠁⠀⠁⠈⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠈⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠄⡠⠈⡄⠱⠈⡁⠃⠒⠠⢀⠤⠃⠀⠁⠀⢄⠈⠁⠀⠂⠀⠀⠄⠀⠆⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⢃⠌⠐⡠⢁⠒⠠⢊⠁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠈⠄⠒⠀⠐⠠⠂⡐⠀⡀⠀⠁⠐⠀⠁⠀⠁⢆⠠⠁⠌⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠆⠀⠀⠀⠀⠐⠈⠒⡀⢂⠂⠄⣀⠀⡀⠀⠀⡀⢂⡐⠀⢆⡈⠄⠀⠊⠄⠢⠄⢠⠀⡄⢤⠂⡑⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠂⠀⠀⠀⠀⠁⡈⠀⠂⠌⠀⠂⠙⠓⠒⠶⣬⢄⠀⠀⠠⢋⠀⢄⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⡠⢃⠥⢈⠡⠐⠤⡀⠍⡂⠔⡀⢀⠈⠄⠡⣈⢂⡱⠈⠒⠔⠤⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⣂⠀⠀⠀⠀⠀⠀⠀⢘⡄⠐⠀⠂⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠡⢈⠂⠤⡁⢌⠐⡈⠤⠈⠂⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⠀⣠⣾⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣾⣿⣷⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠌⡐⠈⠄⡈⠜⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠏⠀⠀⣴⣿⣿⣿⣿⠟⣏⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠑⠂⠤⠁⠒⠠⢈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠀⠀⣠⣿⠃⠀⣼⣿⢿⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠠⠐⠈⠀⢈⡔⢈⡐⢀⠂⠀⣩⢿⢶⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⢀⣼⣿⢏⠶⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠐⠠⣄⣠⠈⢐⠀⠀⠀⠀⠀⠀⠐⠀⠠⠀⠘⢿⣤⠈⠉⠹⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⣰⡿⣏⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢀⣠⠶⠁⠀⠀⠀⠀⠀⠀⠙⠳⡌⠠⠀⠀⠀⠐⡀⠀⠁⠢⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⡿⠀⠀⠀⠀⠀⠀⣠⣶⣿⣧⡶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣁⢂⠀⠀⠰⢁⠈⠆⡑⠀⠀⠀⠀⠹⣷⠀⢀⠀⢀⡀⠉⠙⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣟⠫⡝⡩⢉⡌⢁⠋⠙⠻⢿⣧⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢢⠀⠁⡀⠠⠐⠠⠀⠀⠀⠀⢰⣿⡁⣠⣴⠞⠉⠉⠀⠀⠈⠉⠳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡳⣵⢪⡕⠬⣑⠢⡐⢀⠂⠡⢈⠜⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡐⢨⠐⠀⢡⠀⠀⠀⢀⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣓⢮⠳⣜⠳⣨⠑⡌⢢⢉⡁⠆⣌⢿⣧⠀⠀⠀⣠⠞⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠐⢂⠤⠉⠀⠀⠀⣠⣾⠟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠳⢦⣀⠀⠀⠀⣼⣋⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣹⢮⡽⣌⣳⣤⣯⣴⣧⣶⣼⣦⢁⣾⣿⠀⢀⡿⠉⠀⠀⠀⠰⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡁⠀⡀⠆⡁⢂⠀⣾⡿⠁⠀⢀⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠻⠷⣦⠸⠟⠉⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⡝⣶⢿⠿⢿⣿⣿⣿⣿⠿⣿⣇⣻⣿⡟⠀⣸⣤⡀⠀⠀⠀⣤⡻⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡥⠀⡐⠈⠄⠀⣼⣿⠃⠀⠀⠀⢢⡀⠀⠀⠀⠀⢀⡄⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⡆⠀⠀⠀⠸⣿⣿⣿⢿⣏⢻⠿⣿⣿⣿⣿⡳⣽⡙⢦⢫⡜⢪⡙⢋⡍⠰⡈⠞⣿⣿⣏⣷⣾⡿⠋⠀⠀⠀⠀⠈⠻⢷⣭⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡴⠋⠀⠀⠌⡔⠀⠀⣿⠇⠀⠀⠀⠀⠀⠉⡆⠀⢰⣾⠋⠄⡐⠠⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠄⢀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⣀⠀⡀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⢻⣿⣿⣟⠤⣫⣿⣯⢟⣿⢣⡟⣶⡹⣣⢳⢼⣷⣌⡾⢌⠱⡈⣽⣿⠟⡿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⢀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡯⣐⠌⠀⢈⠐⡠⠈⡐⢿⠀⠀⠀⠀⠀⠀⠀⣵⣠⠿⠋⠀⠀⠀⠐⠠⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣇⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⢻⣿⣿⣧⣦⠽⡟⡾⣜⡻⢾⣱⢳⣭⣛⠾⣿⡿⡞⡄⢣⢼⣿⣿⣾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢷⣦⣤⣼⡿⠀⠀⣀⣀⣤⣶⠿⠋⠁⠁⠀⠀⠀⢣⠀⠡⠀⢯⠀⠀⠀⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠀⠡⠀⢀⠃⠄⠂⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⢻⣿⣿⣿⣶⣽⡗⣾⡹⣏⣗⣫⢶⢫⡳⢭⣷⠩⣜⣦⣉⠒⡌⣽⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣯⢨⣿⣿⣿⣯⣤⣀⡂⠂⠄⠀⠀⠀⠆⡁⢂⠡⢈⠀⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⢿⣿⣽⢫⢯⡽⢶⡻⣼⢶⡳⣮⣳⣝⠺⣌⠳⠸⣿⣿⠾⣶⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠟⠁⠀⠈⠉⠛⢿⣧⡌⠐⡀⠐⢨⠐⡀⠂⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡀⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⢀⣸⣿⣯⣛⠶⣭⣳⡝⣧⡻⢷⣹⢶⣿⣝⡺⣍⠳⢠⢃⢎⣿⡟⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢻⡀⠀⠀⠀⠀⠀⠀⠙⣿⣆⡠⠁⢂⠡⠄⡁⠐⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠁⠂⠁⠂⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠘⣿⡄⠀⠀⠀⣼⡿⠑⣦⣶⣿⣿⢻⣿⣷⢫⡿⡽⢧⣻⣼⣹⣻⡼⣏⣿⣻⣷⣜⣆⣃⠎⣼⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⠟⠋⠁⠀⠈⠷⣦⣀⠀⠀⠀⠀⠀⠈⠻⢷⣦⠀⢂⠐⠠⢉⠀⠀⠀⢀⣠⣿⠇⠀⠀⠀⠀⢀⡤⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠹⣿⣄⣠⡿⠏⠁⠀⣼⣿⡟⣿⣿⣿⢫⡳⣽⡹⢧⡳⣎⡗⣧⢻⡼⣧⣿⣿⣿⣿⣿⠿⠿⣿⣟⡀⢰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⢁⣠⠄⠀⠙⢻⣦⡌⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⣯⠀⠌⡐⠀⢀⣠⣴⣾⡟⢱⣦⡀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⢀⣠⣴⣶⠾⢛⠋⠄⢸⡿⡟⢡⣄⣤⣿⣿⣿⣿⠘⣿⣯⢷⣹⢯⣝⢻⠳⣏⡜⣎⢿⣿⠿⢿⣿⣷⣯⡀⠀⠀⠀⠉⠛⠿⢿⣿⣦⣄⡀⠀⢀⣠⣶⠟⠋⢀⠋⠉⠀⠀⠀⠀⠙⢿⣆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠃⡘⠠⢀⠡⢈⣽⡿⠋⠀⠀⠻⠟⣦⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢀⠘⠛⠛⡛⡉⠄⠂⠄⠈⣠⣤⣷⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘⣿⣿⣜⡳⣎⢧⢫⠴⡹⡜⣒⢦⡙⢆⣿⣿⢿⣿⣾⣿⣦⣤⣤⣄⣠⣌⣍⡹⣷⣶⠿⠋⢁⢤⣈⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠙⣷⣄⠀⠀⣼⡿⠃⢀⠡⠁⢊⢰⣿⠋⠁⠀⠀⠀⠀⣴⣨⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢀⠂⠌⠌⠁⠀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠈⢿⣷⣽⡹⢎⡲⢩⢳⣱⡇⢲⡉⣾⣿⠃⠀⣿⣿⣿⣻⡟⣿⣿⣿⣬⣏⡙⠷⣤⣦⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡘⠯⣰⣾⠟⠁⠈⢆⡐⢀⠂⢸⣿⠀⠀⠀⠀⠀⠀⠈⣿⠏⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠠⠄⠡⠐⠠⠈⢀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠈⠻⣿⣝⢧⡉⢧⢋⠷⡙⢦⣹⣿⡿⠀⠀⢿⣿⣷⣯⣽⣳⢿⡇⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣴⣿⡏⢀⠀⠀⠰⠈⠄⠌⣸⣿⡀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⡐⠀⠌⡀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠐⠠⠈⠀⢌⠒⣈⡰⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣇⠀⠀⠙⢿⣷⡍⢆⢫⡒⣝⣾⣿⣿⠃⠀⠀⢹⣿⣿⣷⣻⣞⣿⡇⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠊⣄⠡⠘⡀⢂⠸⣿⠀⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⣤⣿⡀⠀⠀⠀⠀⠀⠑⠢⢠⡁⠂⠀⠀⠀⢀⡀⠀
		⠀⠀⢀⡐⠈⠀⠁⠈⠐⠀⢙⠊⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠠⠀⠀⠀⠈⠙⣿⣮⣆⣵⣿⣿⠟⠁⠀⠀⠀⣸⣿⣿⣯⣷⣻⣾⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⢩⠀⠀⠀⠀⢹⣇⠐⢀⠂⢸⣿⠄⠀⠀⠀⣠⣿⠃⠤⠁⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⠐⠀⠀⡀⠀⠀
		⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢀⠀⠀⠀⠈⠹⠿⠟⠛⠁⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢀⣼⡿⠋⠁⠌⢄⠠⠀⠀⢠⣿⡃⠄⠂⠌⠘⣿⡀⠀⠀⢠⣿⠏⡀⢘⡀⠀⠀⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠑⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣦⣤⣤⣀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣰⣿⠛⠀⢂⠁⠂⡌⠀⠀⠀⣘⡟⠉⡘⠠⠈⠄⢻⠁⠀⠀⣾⡟⠀⡐⠀⠀⠀⠀⠀⠸⡏⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣶⣶⣮⣭⣽⣏⣟⣛⡟⠻⣿⣿⣿⣿⣿⣏⢶⡩⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢾⠛⢁⠠⠁⠂⠌⠒⠠⠀⠀⡴⠟⠁⠀⢂⠡⠁⢂⡅⠀⠀⢸⡟⡀⠂⠄⠡⠀⠀⠀⠀⠀⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣭⣍⣛⣿⡻⠿⠿⣿⣿⣿⣿⣿⣿⡏⣂⠡⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢀⠦⠜⠀⠀⠀⢀⡤⢁⠂⡁⢢⠁⠀⠠⡘⠄⢂⠈⡄⢂⠀⠀⠹⠐⠀⠀⢌⠀⠣⢤⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⣀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣷⣭⣭⣛⣻⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⡇⣄⠃⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠈⠔⡀⠆⠒⡄⠃⡀⠀⠀⠠⠌⡀⠢⢀⠂⠀⣈⠓⠀⠀⠀⣰⠈⠄⠂⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠰⠀⠀⠀⠀⠀⠀⡜⠡⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⣛⣛⠛⠿⢿⣷⣶⣮⣽⣿⣿⣿⣿⣿⡇⠈⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠴⢈⠠⠀⠀⠀⠈⠔⡠⠁⠀⠀⠀⠂⡁⠆⡠⠐⡠⠂⠡⢀⢠⣾⠗⠀⠈⠄⡁⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⡁⢃⠄⡠⢀⠆⠐⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣶⣭⣭⣿⣿⣿⣿⣿⣿⣧⣶⣁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⢀⠐⠀⠀⠀⠀⠀⠀⠀⠁⠈⠠⢀⠠⠀⡄⠃⢄⠡⢁⠂⡁⢦⡟⠁⠀⠀⠀⠀⠈⢁⠂⠌⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢃⠰⣀⠡⠐⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣯⣯⣙⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠂⠈⠀⠀⠀⠀⠀⠀⠀⠈⠔⠂⠁⠀⢈⠜⠠⠘⡀⢂⡰⠏⠀⠀⠀⠀⠀⠀⠀⠀⢌⡐⠀⠀⠀⠠⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⠠⠐⡄⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣛⠿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠀⠂⢈⠄⠡⡐⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠠⡑⠤⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠂⠐⠀⠀⠀⠁⠈⠁⠙⠠⢈⠐⠡⠀⠀⠐⠐⠀⠒⠒⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢠⠡⠀⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⣯⣯⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠑⢂⠈⠰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠂⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡐⠠⠀⠀⠀⠀⠀⠀⠀⠀⡆⠢⠁⠀⠐⠣⠐⡠⢈⠐⠠⠉⠛⠤⠀⠀⠀⠀⠀⠀⠀⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠘⡀⢂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠐⡀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡐⠀⠀⠐⡀⠁⢆⠈⡐⠠⢁⠘⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⣽⣚⢯⣳⣯⣷⣯⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠑⠄⡀⠀⡀⠄⡀⠂⠀⠀⠀⠀⠤⡁⠀⠁⠂⡡⠀⠀⠁⡂⠉⠰⣆⣀⣴⡿⢋⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣳⣛⠶⡹⢏⡻⣝⢿⡻⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠘⠀⠁⠐⠁⠀⠁⠀⠀⠀⠀⠀⢑⠂⠀⠀⠀⠂⠀⠀⠀⠓⣤⠈⠉⢡⣷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡁⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢾⣯⢗⡮⢯⡵⣫⣷⡾⣎⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠈⠀⠠⠐⠂⠀⠀⠀⠐⠀⠀⠈⠆⠀⠀⡀⠁⠀⠀⠀⠀⠈⢿⣦⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡽⣿⢾⣹⡚⢧⡝⣭⢳⣙⣮⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⡀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢈⠄⠂⠐⠀⠁⠀⠀⠀⠀⠀⠠⠟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⣯⡿⢧⡻⢭⣞⡳⣏⢷⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠈⠀⠀⠀⠁⠁⡀⠀⠀⠀⠀⠠⠀⠀⠂⠈⡐⢀⠀⠂⠀⠀⠀⡀⠄⡁⢀⠐⠒⡀⠀⠀⠀⢀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⣷⣟⣯⣝⣳⣎⣷⣹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠁⠀⠀⢌⡑⢠⠘⠀⠠⢀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡀⠂⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣾⣽⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⢠⢠⣤⣤⣤⣶⣿⡾⠖⢢⣤⣤⣄⠀⠠⠐⠀⠀⠀⠀⠈⠀⠀⠀⢀⠀⡀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠄⢃⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢿⣿⣷⣶⣤⣄⣀⣈⠀⠁⠀⠀⠀⠀⠀⢀⠰⠀⢂⡐⢀⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠄⢣⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣞⣷⡽⣻⡼⢯⡿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠀⠀⠈⠀⠉⠠⡐⢂⠑⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢈⠰⡁⠂⠀⠀⠘⠛⠿⠿⠿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣯⢿⣿⣽⣳⣟⣻⣼⢻⡿⣼⣯⣤⣉⣉⢻⣿⣷⡄⠀⠀⢀⠀⡐⡀⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⠢⠑⡈⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠈⠉⠌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣻⣯⢿⣿⣷⢯⢷⣞⣯⣿⣾⣿⡩⠙⠿⣿⣿⣿⡤⠀⠀⠀⠠⠀⡑⠈⡄⠐⠀⠈⠀⠀⠁⠈⢠⠁⠂⠀
		⠀⠌⡐⠡⢀⠐⠀⠀⢂⠈⠀⠀⡀⠀⠁⠂⠈⠄⠡⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⢾⣹⢯⣞⣯⢞⣽⣿⡿⠿⣿⣿⣿⣿⣿⠏⠁⠀⠀⠀⠠⠐⠀⡡⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⢂⠱⢀⠡⠀⠈⠄⠠⠀⠂⠀⠀⠀⠀⢀⠈⠆⠁⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠈⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣶⣿⡄⠙⠉⠉⠀⠀⠀⠀⠀⢁⠀⡀⠂⠀⠠⠁⠀⠀⠀⠀⠀⠠⢀⠠⠐⠀
		⠀⢂⠘⡀⢂⠀⠁⠄⠠⠀⠄⠁⠂⡀⠀⠄⢢⠈⠐⠠⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠛⠛⠁⠀⠀⠀⡀⠐⠈⠀⠁⠠⠀⠀⠄⠁⢀⠀⠀⠀⠀⠀⠈⠄⢀⠀⠀⠀
		⠀⠄⢂⠁⠆⡈⠔⡠⠒⡈⠄⠂⡄⠐⠡⠀⢂⠡⢈⠰⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠄⠀⠀⠄⠁⢂⠡⠀⠀⠀⠀⠀⠀⠀⠈⢀⠂⠈⠀
		⠠⠈⠄⣉⠒⡈⠄⡑⠢⠁⠌⡐⢈⠂⠥⣈⠐⠂⠄⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠐⠠⠐⠀⠀⠐⢀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⠡⢈⠐⠤⠐⡀⠄⡑⢨⠐⡀⢆⠘⠠⠀⠬⠁⠂⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠁⠀⠀⠄⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⢈⠐⡀⢊⠄⠣⠐⢡⠘⢠⠂⡐⠀⠂⠁⠀⡐⠠⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡀⠃⠤⢁⢊⠑⡈⢆⠩⢄⠂⠄⢁⠀⠁⡐⢀⠐⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀
		⠄⢃⠄⡃⠄⣊⠐⡄⠣⡐⢈⠄⠂⡀⠂⠀⢀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⢳⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡘⠤⡈⠔⡨⠄⡌⠰⢡⠘⠠⠈⠀⠀⠄⠀⠂⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠷⣎⡟⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢁⠢⠉⡜⠠⢑⠨⠑⠂⠌⠁⠀⠁⠈⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠳⢮⣽⣻⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠈⠁⠀⠀⠀⠑⠒⠀⠀⠀⠉⠁⠈⠀⠀⠁⠀⠀⠀⣠⠀⠀⠀⢀⠀⠀⢀⣤⡀⠀⢀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠓⢤⡀⠄⠠⢀⠂⠄⢀⠠⢀⠀⠀⠀⠉⠀⠁⠀⠀⠀⠉⠁⠈⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡈⠄⠁⠈⠄⠀⠀⠀⠀⠀⢀⣀⠠⠐⣀⠠⢌⠡⠃⠉⠌⠂⠌⣠⡴⠋⠀⠉⠀⢄⠈⠉⠀⠂⠀⠀⠄⠒⠐⠂⡄⡀⠀⠀⠀⠀⠀⠀⠈⢣⠄⢁⠰⢈⠰⢈⠰⠈⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠐⠄⡐⢈⠐⠈⠐⠲⠂⢞⡉⠈⠀⠀⠁⠀⠁⠈⢠⠁⠌⠠⡑⠈⠁⠀⠀⠀⠀⠀⠀⠉⠐⠆⠀⠀⠀⠀⠐⠈⠒⠠⠐⠡⠄⣀⡀⡀⠀⠀⡀⠆⡀⠒⡠⠂⠄⠀⠡⢂⠢⠄⣠⠠⢄⡔⢊⡑⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠲⢄⠀⠀⠀⠀⠄⠐⡀⢂⠀⠁⠊⠑⠺⠰⢥⡄⠀⠀⠀⠇⡈⢄⡡⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢂⡔⠰⣁⠉⡐⠠⢈⠄⡱⢠⠉⠄⡀⠐⠠⢀⢢⡐⢢⠆⠜⠆⠤⢄⠂⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣷⠄⠀⠈⠀⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⢂⠐⠈⡐⠰⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠀⠀⠀⠈⡄⠁⢆⡐⢂⠁⢂⡴⠁⠂⠃⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠀⠀⠀⠛⠋⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠁⠂⠄⡁⢊⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣷⠤⠀⠀⣀⣶⣴⣿⣿⣷⣦⣤⣤⣄⣀⣀⣀⣀⣤⣴⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡔⠨⠐⠠⠐⡀⠂⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠶⠋⠉⣸⣿⠏⠀⠀⣠⣾⡿⣿⣻⣿⣿⣟⣫⣿⣿⢻⣿⣿⣿⣿⣦⣉⡙⠻⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠐⠠⢀⠙⠀⢀⡇⠠⡁⠀⡌⠀⣹⣿⢷⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠈⠀⠀⠀⣼⡟⠁⠀⠀⣼⣿⠻⡜⡽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠐⢤⣤⣄⡈⢐⠀⠀⠀⠀⠀⠀⠄⠁⢀⠀⠙⣿⣤⠈⠉⠻⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⣀⣾⣿⢥⣻⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠙⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⡄⢀⣴⡾⠃⠀⠀⠀⠀⠀⠉⠛⢿⣄⠃⡀⠀⠀⠡⢀⠀⠈⠰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣴⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠐⢶⣾⣿⣷⣦⠀⠀⢀⣤⣶⣿⣿⣾⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣶⣄⠀⠀⡐⢂⠈⠔⡘⠀⠀⠀⠀⠹⣷⠀⢀⠀⡀⣀⡉⠹⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠙⣧⡈⠓⠶⠛⠛⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡄⠀⡀⠠⢀⠱⠀⠀⠀⠀⣰⣿⣁⣠⣴⡟⠋⠉⠀⠀⠈⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡿⢟⠛⡛⠛⠿⢛⢉⠋⠽⣿⣿⠀⠀⠀⠀⠘⠳⣦⣀⡴⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⢀⠌⡁⠀⢂⠀⠀⠀⢀⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠒⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⡻⣔⢣⡙⡔⢣⠘⡀⠡⠀⢆⠌⢢⠡⢿⣿⠀⠀⠀⠀⠀⣠⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠂⠄⠒⡀⢃⠀⠀⠀⣠⣾⠟⢣⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠐⠳⢦⣄⠀⠀⠀⣼⣃⡀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⡳⣭⢳⣎⡧⡜⢬⡑⠦⡔⢡⢈⠢⢌⠃⠴⢹⣿⡇⠀⠀⢀⣿⠟⠁⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣈⠀⠠⡑⠀⡂⠐⣾⡿⠁⠈⠄⠐⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠈⢻⠷⣦⠾⡿⠋⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣓⢮⣕⣺⣰⣘⣦⣼⣤⣊⠔⣊⢜⣰⣽⣿⣥⣠⣴⣾⣧⡶⠈⠁⠶⣦⡻⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⠀⠡⠘⠀⠀⣹⣿⠃⠀⠀⠈⢶⣤⠀⠀⠀⠀⢀⡄⢀⠠⠈⠀⠀⠀⠀⠀⠀⠀⢀⠐⡀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣶⡇⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣯⡝⣶⣭⣾⣾⣿⣿⢿⣟⣿⣿⣿⡛⢼⣿⣿⣿⡏⠭⣥⣾⠟⠉⠀⠀⠀⠀⠉⠻⢷⣬⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⠏⠁⠀⠬⡐⠀⠠⣿⠇⠀⠀⠀⠀⠈⠹⣆⠀⢶⣾⡏⠄⠠⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⡀⠄⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣀⠀⡀⠀⠀⠀⠀⠀⠀⢹⣷⠀⠀⠀⢠⣿⡿⣿⣿⣿⣿⣿⣷⣛⢾⠿⣛⠭⡿⢿⠿⠿⣋⣜⣻⣷⣌⠛⡛⠿⣿⣷⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡯⣠⠐⠀⢀⠂⡁⠌⠐⣿⠃⠀⠀⠀⠀⠀⠀⣿⣤⠾⠛⠀⠀⠀⠈⡐⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣇⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⢿⣿⡹⣿⡿⣿⣟⠳⣎⢯⣳⣍⣚⡔⢣⠎⡑⢆⣿⣛⣿⣿⣼⣴⣹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢷⣶⣤⣼⣿⣄⠀⣀⣀⣤⣶⠿⠋⠉⠁⠀⠀⠈⡡⠐⠠⠁⣿⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠐⠠⠀⠀⢃⠐⠀⠀⠀⠀⠀⠀⡀⠀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠈⢿⣷⣹⣷⡳⢮⡿⣜⢯⡟⣞⠿⡟⡟⢮⣵⣿⣿⣿⣿⣿⣾⡏⣼⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠙⣿⢩⣿⣿⣿⣯⣤⣐⡀⠆⡀⠀⠀⠠⡁⠌⠠⢁⠩⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠻⣿⣯⣿⡻⣵⢫⣾⡹⣮⡟⣵⢏⡞⣴⣉⢛⡛⠫⢍⡩⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⠟⠁⠀⠈⠉⠛⢿⣶⣈⠐⠀⠠⠑⡌⠐⡀⠃⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⢹⣿⣷⡹⣖⢯⡶⣹⢧⡿⣜⠮⡜⣼⣿⣷⣷⣿⣶⣶⣿⣿⠁⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⡀⠀⠀⠀⠀⠀⠀⠙⣿⣆⡁⠂⠡⠠⠁⠄⠡⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠊⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠥⠘⣿⡄⠀⠀⠀⣸⡎⠻⣦⣀⠀⠀⣸⣿⣿⣳⠽⡾⣝⢧⡯⣽⢿⣿⡵⣨⠝⣭⠹⡍⠦⣙⣿⣿⣿⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣾⠟⠋⠉⢀⠘⠿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢿⣦⠁⢂⠡⢈⠐⠀⠀⠀⠀⣠⣿⠃⠀⠀⠀⠀⢀⡼⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣿⣄⣠⣾⡿⠁⠀⠙⢿⣷⣶⣿⢻⣿⣷⣏⢷⣫⢿⡼⣧⣟⡻⣿⣵⡚⡤⢃⠜⣰⣿⡿⢿⠃⠠⢱⣆⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⢉⣠⡴⠈⠛⢿⣦⡌⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⣏⠠⠐⡀⠌⢀⣠⣴⣾⡿⢹⣦⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡾⠟⡛⠁⢀⠻⣯⣿⠇⠀⠀⠀⠈⣿⣿⣵⣦⣿⣿⡟⣮⢽⣎⠷⣏⡾⣵⢯⣿⣿⣼⣿⣾⣿⠋⠀⠀⠈⠱⠳⢿⣿⣶⣄⡀⠀⢀⣠⣶⠿⠋⠰⠟⠋⠀⠀⠀⠀⠙⢿⣆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠋⠤⡁⠄⢂⢈⣽⡿⠋⠀⠀⠿⠿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢁⢂⣻⣿⣿⡏⠐⠠⢀⠡⠀⠄⣾⡟⠀⠀⠀⠀⣠⣿⣿⠸⣿⣯⢽⡹⣎⢷⣞⣻⡭⣿⣽⡿⢿⢛⢫⢿⣿⣿⣇⣸⣿⣤⣶⣦⣴⣿⣍⠙⣷⣶⡿⠋⢡⣄⣦⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠙⣿⣄⠀⠀⣼⡿⢃⠠⠑⠀⡘⢠⣿⠛⠁⠀⠀⠀⠀⣴⣸⣿⠃⠀⠀⠑⠂⠀⠀⠀⠀⠀⠂⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡐⣠⣾⠟⠁⠀⠀⠈⡐⢀⠂⠡⢀⠒⠀⢀⣠⣴⣾⣿⣿⣿⣇⢻⣿⣾⡱⢯⡟⣼⣳⣿⢿⡛⡜⣥⢊⠇⢾⣿⠏⣿⣿⣿⣿⢻⡿⣿⡿⠋⠶⣤⣤⡐⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣦⡘⠟⣠⣾⠟⠁⠈⠴⡀⠡⢀⢹⣿⠀⠀⠀⠀⠀⠀⠈⣿⡏⠀⠀⠀⠀⠀⠀⠠⣦⡄⠀⠂⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⠠⠐⡈⣔⣶⡿⠟⠉⠀⠀⠀⠀⠠⠐⢂⠈⣴⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠹⣿⣟⡧⣝⢦⡹⣹⣎⢽⣘⣦⢋⠼⣽⣿⠀⢸⣿⣿⡽⣯⢿⣽⠿⣶⣾⣍⣉⠉⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣼⣿⡟⠀⢀⠀⠘⠤⠁⡀⢺⣿⡀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⢀⡄⠀⠀⠀⠀⠙⠄⠂⡁⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠐⣀⠂⠀⠌⠠⢱⣾⠿⠋⠀⠀⠀⠀⠀⠀⢀⣠⣾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠘⣿⣿⣞⢦⢃⢷⣯⠖⣭⢢⢋⣾⣿⠏⠀⠀⣿⣿⡿⣽⢯⡟⡜⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠈⢲⣦⡁⠢⠐⠠⢸⣿⡁⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⣦⣿⡄⠀⠀⠀⠀⠀⠁⠆⠤⡈⠄⠀⠀⠀⢀⠀⠀
		⠀⠀⢀⡐⠈⠀⠁⠂⠀⠂⠡⠈⢄⠋⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⢿⣿⣧⡞⡨⢿⡏⡖⣣⣿⣿⡿⠀⠀⠀⢿⣿⣿⡽⣯⣟⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠹⠀⠀⠀⠈⢻⡷⠁⡈⠄⢒⣿⡅⠀⠀⠀⣠⣿⠇⢘⠀⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠠⠀⢀⠀⠀⠀
		⢀⡌⠂⠀⠀⠀⠀⠀⠀⠀⠀⢁⠢⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⡆⠀⠀⠙⢿⣷⣕⢢⡱⣽⣿⣿⠏⠀⠀⠀⠀⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣼⡿⠋⠁⠌⠰⡁⠀⠀⣠⣿⡗⠠⠐⢈⠨⣿⡅⠀⠀⢠⣿⠏⡀⢌⡄⠀⠀⠘⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡀⠀⠀⠁⠂
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡐⠂⠌⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢡⠀⠀⠀⠀⠙⠻⣿⣿⣿⠟⠉⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢠⡿⠛⠀⡄⠡⠈⠆⠀⠀⠀⣸⡿⠉⢂⠁⠂⠄⣿⠃⠀⠀⣾⡟⠀⡐⢈⠀⠀⠀⠀⢻⡟⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠑⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⣀⣤⣤⣤⣤⣶⣥⣭⣤⣄⣀⣀⡀⠀⣸⣿⣿⣿⡷⣸⠴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠌⠠⠑⠂⠠⠄⢃⠒⠀⠀⣼⠟⠁⢀⠊⠐⠁⢂⡭⠀⠀⣼⡿⠀⠡⠐⢨⠀⠀⠀⠀⠀⠻⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⡁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣻⣿⣿⣻⣛⠿⣻⡛⠿⣿⣿⣿⣿⣿⡃⠤⣁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠁⠀⠀⢀⡔⢠⠈⡐⢈⠃⠀⠀⡆⡘⠠⢈⠄⡒⠀⢠⣿⠧⠁⠀⢡⠂⠳⣤⠀⠀⠀⠀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠆⡐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣙⣋⣙⣛⢻⠟⡿⠿⠿⣿⣿⣿⣿⣿⣿⡑⠢⣐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠠⠉⠄⠢⡐⢄⠋⠀⠀⠀⠀⠤⠁⠢⣀⠒⠀⣾⠿⠃⠀⢀⣾⡇⠐⢨⡆⠀⠀⠀⢂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠀⠀⠀⠀⠀⢀⠐⠂⠄⠂⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠻⠻⠟⠿⠿⢿⠿⣿⣿⣶⣿⣿⣿⣿⣿⠄⢁⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⡌⠁⠀⠀⠀⠈⠦⡈⠀⠀⠀⠀⠃⠡⢂⠀⢂⠔⡉⠄⡀⣤⣾⡿⠀⠈⠆⡱⠀⠀⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⡁⢊⠄⡠⢐⠠⢈⠰⢉⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣶⣿⣶⣦⣭⣿⣿⣿⣿⣿⣶⣆⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠐⠀⠀⠀⠀⠀⠀⠁⠉⠀⠄⡠⠀⡄⢃⡘⠄⢊⠐⢠⣱⣿⠋⠀⠀⠀⠀⠙⢆⠐⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠃⢌⡐⠂⠌⠀⠂⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣦⣭⣬⣍⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠁⠀⠐⡡⠐⡈⢂⢸⣴⡿⠁⠀⠀⠀⠀⠀⠀⠈⢆⡡⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠰⢀⠆⠉⣀⠀⣀⢀⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣭⣭⣛⣟⣛⢻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠀⠈⠠⢁⠐⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡌⠢⠐⡀⠈⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣟⡻⠿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠁⠈⠈⠙⢀⠂⠌⡙⠀⠀⠐⠲⠖⠾⠳⠶⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⠤⠁⠠⠄⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⢿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠂⠌⠠⠐⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢘⠠⠐⢀⠂⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠂⠆⠀⠐⡈⠐⠌⡐⠠⢀⠉⠚⠤⠀⠀⠀⠀⠀⠀⢀⣴⠆⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⢂⠐⠂⠀⠀⠀⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⡀⠀⠀⠀⠀⠀⠀⠐⡀⠀⢄⠀⠀⢠⠈⠐⡠⠁⠄⣈⠐⢈⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢃⠤⠈⡐⠀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠘⠐⡠⠀⢀⠀⠄⢂⠀⠀⠀⡀⠀⢌⡀⠀⠡⠀⠍⡀⠀⠉⡄⠂⠰⠄⢀⣰⡿⢋⡔⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡌⠠⠐⡀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⡐⢁⠀⠘⠀⠂⠁⠀⠀⠀⠀⠀⠘⣀⠀⠀⠈⡀⠀⠀⠀⠱⢀⠈⠀⢠⣼⠟⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠔⡈⠐⠠⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣯⡟⣽⣛⠿⣿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠠⠀⠂⠀⠀⠀⠐⠀⠀⠌⡀⠃⢀⠂⠄⠀⠀⠀⠀⠈⠣⢀⠆⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡀⠆⠘⠠⠁⠀⠄⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⢖⣭⢛⣬⢳⢮⡝⣿⣿⣆⠀⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡀⠐⠀⠰⠀⠀⠀⠀⠀⠀⣀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠁⢘⠨⢄⠡⠈⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⠾⡼⢭⡖⢯⡲⣝⠶⣹⣿⠀⠄⢠⢁⠂⠄⠐⠀⠀⠀⠀⡀⠀⠂⠁⠌⡀⠄⠂⠀⠀⠀⡀⠄⠠⢀⠁⠒⠀⠀⠀⠀⠀⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢂⠰⡀⢂⠐⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣝⣻⣝⡳⣞⢧⣛⣬⢻⣽⣿⠀⠌⡐⠢⠌⢀⠀⡀⠀⠀⠀⠀⠀⠀⠠⠈⠔⠀⡀⠀⠀⢢⠡⢈⠔⠀⠢⡈⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡁⠆⠐⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡷⣯⢷⣏⢾⣱⢮⣟⣿⣇⠀⠂⠀⠀⠀⠀⠐⠀⡀⠀⠄⠀⠡⢈⠤⠁⢀⡐⠠⡀⠀⠄⡂⠁⠀⠀⠀⠈⠁⡀⠀⠄⡀⠀⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠔⡈⠄⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣞⣧⣛⣞⣾⣿⣯⠀⠀⠐⠀⠀⠀⠀⠀⠄⠁⠀⠀⠐⢀⠂⡉⠄⡄⠡⢀⠁⡌⠀⠀⠀⠀⠀⠀⠀⢠⡐⠰⢀⠓⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢈⠰⢀⠄⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠠⠐⠀⠀⠣⠐⢂⠤⠁⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠐⣂⠢⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢆⠁⡂⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠐⡡⢂⠐⡠⠂⠀⠀⠀⢀⠀⠀⡀⠀⠀⠀⢀⠀⠄⡂⢅⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀
		⠀⠌⠠⢃⠀⠁⠀⡀⠀⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣻⣽⣿⣻⣟⡿⣏⠿⣭⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠁⠢⠌⢀⠀⠀⠀⠀⠀⠠⠐⡀⠀⠀⠀⠀⠈⠠⠑⡈⡀⠂⠈⠀⠁⠈⠀⠁⢌⡀⠀⠀
		⠀⠌⢒⠠⢂⠈⠀⠀⠄⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⡿⣽⡷⣯⢷⣻⢾⣽⢫⢷⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠡⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠐⠀⠀⢀⠀⡀⠀⠀⠄⢀⠁⠄⠀⠡⠀⠂⠀⠄⠐⠠⠑⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠁
		⠀⠌⢂⠆⡀⠂⡀⢂⠠⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⣯⣿⡽⣟⣯⣿⢯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠈⠉⠉⠉⠉⠁⠀⠈⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠄⠁⢀⠠⠀⠀⠄⠀⠈⡀⠌⠀⠄⠁⠀⢈⠐⠀⠐⡀⠂⢈⠐⠀⠈⠀⠀⠀⠠⠈⠀⠀⠀
		⠀⠌⡐⢂⠐⠀⠀⠄⠐⢀⠐⠀⠄⠀⠀⢉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣞⣷⣿⣻⢯⣿⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡀⠀⠐⠀⠀⠀⠁⠀⠀⡈⠀⠈⡐⠀⠠⠈⠀⠄⠁⠂⠀⠀⠀⠀⠀⠈⠄⢈⠀⠀⠁
		⠀⡐⢈⠄⠌⡠⢁⠢⢈⠄⢂⡐⡀⠂⠄⠀⠠⠐⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣟⣾⣟⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠈⠀⠀⠀⠀⠁⠀⠀⠐⠠⠀⠐⡀⠀⢂⠁⢂⠀⠀⠀⠀⠀⠀⠈⢀⠂⠈⠀
		⢀⠐⡈⠔⡈⠔⠠⢁⠊⡐⠄⠠⠑⠠⠘⣀⠓⡈⠄⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⠐⢀⠐⠠⠀⠀⠠⠀⠀⠀⠀⠀⠀⡐⠠⠀⠀
		⠀⢂⠘⠄⡡⠈⠄⢂⡘⢠⠘⠠⡑⠂⠡⠀⠒⡀⠠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠐⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
		⠐⠠⢈⠢⠄⠣⠘⣀⠒⠤⠈⠄⡁⠌⢀⠀⢂⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀
		⠀⡁⠂⡜⠠⢃⠢⢄⠩⢄⢁⠂⢀⠀⠀⠄⡀⠀⠁⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀
		⠠⠀⠥⡐⢡⢂⠰⡈⢆⡈⠄⡈⠄⡀⠌⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢟⡿⣿⣿⣿⢿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠌⢡⠂⠤⣁⠢⠄⡑⢢⠈⠄⠁⠀⠠⠀⠀⠈⠀⠀⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢮⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
		⠈⡄⢉⠒⠠⢡⠘⡀⠃⠌⠐⠀⠁⠀⠐⠀⠂⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢾⡹⣯⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠡⠈⠉⠀⠂⠀⠙⠦⠁⠀⠀⠀⠁⠈⠀⠀⠁⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠓⢤⡀⠄⠠⢀⠂⠄⢀⠠⢀⠀⠀⠀⠉⠀⠁⠀⠀⠈⠉⠁⠈⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡀⢁⠀⢈⠡⠀⠀⠀⠀⠀⠀⣀⠠⢂⠐⡀⡉⠌⢂⠉⡉⠐⡄⢀⠤⠁⠈⠁⠂⠄⠈⠉⠀⠀⠀⠀⠄⠂⠒⠂⠤⡀⠀⠀⠀⠀⠀⠀⠈⢗⠠⠁⡰⢈⠰⢀⠒⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠠⢀⠀⡀⠀⠀⠀⠀⠀⠰⢆⠠⢈⠰⠀⠁⠶⠆⡲⠌⠑⠀⠀⠀⠈⠀⠁⡈⠄⠂⠄⡡⠂⠈⠀⠀⠀⠀⠀⠀⠁⠀⠆⠀⠀⠀⠀⠀⠁⠎⠐⡀⠣⠄⣀⡀⡀⠀⠀⡈⠄⢂⠐⡄⠢⠀⠐⠠⠌⠡⠄⣠⢠⠠⡔⢊⠑⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠷⣤⡀⠀⠀⠈⡀⠐⠄⢂⠈⠂⠉⠓⠪⠕⢦⡄⠀⠀⢠⠓⢈⠐⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⡐⠰⢡⠉⡐⠠⠉⡄⠒⡄⢣⠀⡀⠠⢈⠐⣠⢂⢆⠡⠚⠤⠆⢄⠢⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣷⡄⠀⠀⠐⠀⠌⠂⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠂⡐⠌⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠀⠀⠀⠠⠑⠂⡄⢃⠰⢀⢂⡴⠁⠂⠑⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠂⠌⠠⢁⠂⡹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣶⡄⠀⠀⠀⠄⠈⠀⠀⠤⣤⣤⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠰⡈⠄⡁⢂⠐⡀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⣩⣿⠟⠁⠉⡗⠀⠀⠀⠀⠀⠀⠡⠀⠀⠉⠉⢉⣻⣻⣥⡀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠠⠐⠊⠀⢀⡆⠐⡠⠀⠄⡀⣹⡿⢷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠐⠉⠁⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⣀⣴⣦⣤⣤⣤⣴⣂⣰⣊⡉⠉⠉⠁⠁⠀⣀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠐⢤⣤⣤⡈⢐⠀⠀⠀⠀⢀⠀⠁⠀⠠⠀⠙⣿⣤⠈⠙⠻⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⣴⣶⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡷⢷⣤⡀⠀⠛⣷⣄⠀⠘⢻⣄⠀⠀⠀⠀⠀⠀⠀⢀⣰⠆⢀⣤⡾⠂⠀⠀⠀⠀⠀⠈⠛⢷⣎⠐⡀⠀⠀⢂⠀⡀⠁⢒⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠁⠀⠀⠀⠀⠀⠀⠀⣄⡀⠀⢻⡄⠀⠀⠀⣼⣿⣿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⠛⠿⢷⣾⣿⢿⣆⠀⠀⢀⣤⣶⣿⣿⣾⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⣄⠀⠀⠄⡂⠐⠤⢨⠀⠀⠀⠀⠹⣷⠀⢀⠀⡀⣀⡉⠹⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣴⠃⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡄⠀⠀⠈⠹⣷⡈⠳⠶⠟⠛⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡄⠀⡀⠄⠀⠥⠀⠀⠀⠀⢰⣿⣁⣠⣴⡟⠋⠉⠀⠀⠈⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣴⣿⢿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠙⠿⣦⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠐⣈⠂⠈⠄⠀⠀⠀⢀⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠈⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢂⠐⢠⠘⠠⠈⠀⠀⣠⣾⠟⢣⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠘⠷⢦⣄⠀⠀⠀⣠⣀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⡿⡟⡿⢻⢍⠻⣙⠛⡩⢑⠢⢌⠱⢠⠻⣿⣿⣿⣿⡄⠀⠄⢀⣿⠟⠁⠀⠀⢳⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡂⠀⡀⠎⠐⡠⠐⣾⡿⠉⠀⢂⠐⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠈⢛⠷⣦⠼⠿⠉⠀⠀⢹⣿⣿⣿⣿⣟⢧⢣⢳⡹⡜⣡⠎⡑⡌⢦⡑⢣⠎⢤⠃⠦⣑⣹⣿⣿⣿⢀⣠⣴⣿⣧⡤⠀⠀⠲⣦⡻⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡷⠀⢀⠃⠐⠀⣼⣿⠃⠀⠀⠀⢶⣄⠀⠀⠀⠀⢀⡤⠀⢀⠈⠀⠀⠀⠀⠀⠀⠀⢀⠐⠠⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣶⡆⠀⠀⠀⢸⣿⣿⣿⣿⣯⢞⡱⣏⢶⡙⢦⡛⠴⡘⠤⢌⡡⢊⠤⢉⠒⣄⠚⣿⣿⡟⠺⣿⣿⠟⠉⠀⠀⠀⠀⠉⠻⢷⣬⠉⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡴⠏⠁⠀⠬⡐⠀⠀⣿⡇⠀⠀⠀⠀⠀⠹⣆⠀⢶⣾⡯⠀⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⢀⠀⠂⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⡀⠀⡀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠘⣿⣿⣿⣿⡝⣮⢳⣝⣮⣽⣶⣿⣧⡹⣘⡴⣈⣧⣾⣾⣷⣶⣿⣿⡿⠀⢖⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⡯⣐⠄⠀⢀⠒⠠⠈⡐⣿⠂⠀⠀⠀⠀⠀⠀⣻⣤⡾⠛⠀⠀⠀⠂⠐⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣇⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠛⣿⣿⣿⡼⣳⣿⣿⣿⣿⣷⣿⣾⡿⢿⡟⠽⣻⣿⣿⢿⣷⣾⣿⣷⣸⠘⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢷⣶⣤⣼⡿⣄⠀⣀⣀⣤⣶⠿⠋⠉⠀⠀⠀⠈⡘⠠⠁⠄⣿⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠐⠀⠀⠀⠀⠀⠀⢀⠀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⣾⡿⣿⣿⣱⢏⣶⣿⡿⢟⢯⣓⠿⣽⡖⣬⣓⡿⢛⡛⡷⣀⠮⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠙⣿⢩⣿⣿⣿⣯⣤⣐⡀⠆⡄⠀⠀⠠⣁⠡⠈⠄⠹⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢿⣇⠀⠸⣿⣦⠹⣿⣟⣾⣿⢧⡻⡼⣶⣿⡿⢷⠿⣙⡍⠲⣡⠘⠴⣡⠊⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⠟⠁⠀⠈⠉⠛⢿⣷⡄⠁⠄⠐⢠⠂⠡⠈⡅⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠸⣿⡆⠀⠹⣿⣕⣻⣿⢞⣬⣳⢳⣝⢮⣳⣽⣎⣷⣽⣾⣷⠆⡙⢲⠡⣞⣿⡿⠁⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⡀⠀⠀⠀⠀⠀⠀⠙⣿⣦⡈⠐⠠⠑⠂⡁⠠⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠁⠂⠁⠂⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠢⠘⣿⡄⠀⠀⠀⣸⡿⠿⣦⡀⠘⢻⣿⣿⣟⢮⣛⢯⡟⣎⢷⣿⡿⣟⢫⡑⢌⢣⠡⣃⠵⣾⣿⢁⠟⠛⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣶⠿⠛⠉⣀⠘⠿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢿⣦⠁⠌⡐⠠⢁⠀⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⢀⡶⠀⠀⠀⠀⠀⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡿⣿⣄⢠⣾⡟⠁⠀⠙⠿⣇⡙⠛⢿⣿⣧⣯⢳⣽⡹⣾⣶⣷⣞⣦⣿⣿⣏⠓⢤⣾⡿⢿⣷⣌⡐⢰⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⢋⣠⡄⠂⠙⢿⣦⡌⠻⣿⡆⠀⠀⠀⠀⠀⠈⢿⣯⠀⡐⢀⠂⢀⣠⣴⣾⡿⢹⣦⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠛⠋⠁⠈⢻⣿⣿⠁⠀⠀⠠⠞⠛⠻⣦⣼⣿⣿⣟⡳⣾⣱⢯⣿⠿⡟⢯⠍⡍⠦⣙⣾⣿⠁⠀⣈⠉⠹⠞⢻⣿⣷⣄⠀⠀⢀⣠⣶⡟⠋⡘⠟⠋⠀⠀⠀⠀⠙⢿⣆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠃⡜⢀⠂⠌⢠⣽⣿⠋⠀⠀⠿⠿⣶⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠐⣚⣿⠟⠀⢀⠀⠄⠠⢀⠉⣿⡟⠀⠀⠀⠀⠀⠀⠀⣿⡟⣿⣿⣏⢷⡳⢯⣞⣯⢟⡜⣣⠚⡤⢓⣼⣿⡇⠀⢸⣿⣦⣶⣦⣦⣿⣍⠻⢷⣶⡿⠋⣁⣤⣴⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠙⣿⣄⠀⠀⣼⡿⢃⠠⠘⠀⠌⣰⣿⠋⠁⠀⠀⠀⠀⣴⣸⣿⠃⠀⠈⠑⠂⠀⠀⠀⠀⠀⠁⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⣈⡾⠋⠀⠀⠀⠀⡍⠠⢁⠀⢂⢹⣷⣀⣀⣀⣀⠀⠀⢰⣿⠇⣿⣿⡾⣭⣛⡷⣺⣜⢯⣾⣥⡟⣘⢧⡘⣿⣿⢷⣾⣿⣟⣿⡿⣿⣿⠏⠐⡆⠠⠐⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣦⡘⢏⣰⣾⠟⠁⠈⠴⡀⢁⠂⢸⣿⠀⠀⠀⠀⠀⠀⠈⣿⠏⠀⠀⠀⠀⠀⠀⠠⣦⡄⠀⠌⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⠀⠠⠰⠀⠌⢠⣱⠾⠉⠀⠀⠀⠀⠀⣸⡇⠐⠀⠌⡀⠌⢿⡿⠛⠛⠛⠋⠐⣿⣿⡏⣿⣿⡷⣽⢿⡽⣳⢯⣻⣿⡷⡸⡅⢦⡙⣼⣿⠈⣿⣿⣟⡾⣿⣞⣿⡄⠀⠛⠰⠡⠀⠀⠠⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣴⣿⡏⠠⠀⠀⠘⡐⠠⠈⢼⣿⡀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠠⣄⠀⠀⠀⠈⠙⠄⡀⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⢀⠀⠀⠐⠠⠁⠀⠡⢀⢁⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠄⠀⠐⠠⢀⠂⠁⢀⣀⣴⣶⣿⣿⣿⣷⢹⣿⣿⣹⢮⢷⣻⣏⢷⣿⣷⡓⡼⣣⠞⣼⣿⠃⣹⣿⣯⣟⣿⡞⡿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠁⢳⣬⡐⠠⠑⢈⠸⣿⠁⠀⠀⠀⠀⣸⣿⠡⠀⠀⠀⣦⣿⡄⠀⠀⠀⠀⠀⠈⠆⢄⡈⠄⠀⠀⠀⢀⠀⠀
		⠈⠀⢀⡐⠀⠂⠁⠈⠑⠀⠣⡐⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⣐⣠⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⡄⢹⣿⣷⣫⢞⡷⣹⢾⣹⢻⡱⢣⡒⣭⣿⣿⠀⢸⣿⣿⣞⡷⣯⣳⣽⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠠⠠⠀⠀⣀⣠⣾⡟⠩⠀⠀⠀⠀⣻⣟⠀⠌⡀⢜⣿⠆⠀⠀⠀⣠⣿⠇⢂⠁⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⡀⠂⠀⠀⠀⠀
		⢠⡜⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠁⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⣿⣿⣎⠷⣙⢮⢳⣯⣱⢣⣽⣿⣿⠇⠀⢸⣿⣿⡿⢿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠛⠉⡁⠄⡘⠄⠀⠀⢠⣿⡇⠈⠄⡐⠸⣿⠀⠀⠀⢀⣿⡏⠀⢌⡄⠀⠀⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠁⠘⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⡀⠂⡄⠀⠀⠀⠀⠀⠀⠀⣼⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠻⣿⣿⡌⢎⡹⢻⢶⣿⣿⣿⡏⠀⠀⠘⠻⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠈⠄⡑⠠⠐⠄⠀⠀⠀⣸⡿⠁⢃⠐⠠⢈⣿⠁⠀⠀⣾⡟⠀⠌⡐⠀⠀⠀⠀⢹⡟⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠅⠃⡌⠐⠀⠀⠀⣀⣴⣾⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣄⠀⠀⠙⢻⣿⣮⣜⣭⣿⣿⡿⠋⠀⠀⠀⠀⣼⣿⡷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠂⠠⠅⠚⢠⠀⠀⣼⠟⠁⢀⠊⠄⠃⠠⡭⠀⠀⣼⡿⠀⠌⠠⢐⠀⠀⠀⠀⠀⠛⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠄⢣⠠⢁⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⠻⠀⠀⠀⠀⠈⢻⣿⣿⠿⢋⠀⠀⠀⠀⢀⣼⣿⡏⡐⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢀⠤⢁⠢⠐⡈⠆⠀⠀⡆⡈⠄⢠⢁⠣⠀⢠⣿⠇⠀⠀⢡⠈⠳⣤⠀⠀⠀⠈⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠆⡁⠎⠁⠒⢄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣁⢦⣴⣶⣶⣶⣶⣶⣿⣿⣷⣦⣶⣤⣤⣾⣿⣿⡧⠑⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⢈⠂⠄⣂⠒⠌⠀⠀⠀⠀⡅⠈⠤⢀⠳⠀⣾⡟⠁⠀⢀⣾⠇⠠⠐⡆⠀⠀⠀⠌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⢀⠀⠀⠀⠀⢀⠰⠈⡐⢠⠑⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣾⡵⢯⣭⢻⣿⣿⣿⣿⠇⢀⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡧⠀⠀⠀⠀⠮⡀⠁⠀⠀⠀⠘⠡⡀⠌⣀⠒⠃⠄⡀⢤⣾⡿⠀⠁⠎⠡⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⣀⠊⡄⢠⠐⠂⠄⡡⠘⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢶⣖⡲⡔⢦⡜⣬⢓⡬⣟⣿⣿⣿⣿⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⢉⠀⠄⡠⠀⢄⡁⠢⠄⣉⠐⢂⣽⡿⠋⠀⠀⠀⠀⠉⠆⡁⢂⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠊⡔⠁⢌⡐⠂⠁⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡟⣼⡱⣏⠧⣞⠶⣫⣼⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠂⠔⡂⠁⠀⢂⠰⠁⠒⡀⢎⣼⡿⠁⠀⠀⠀⠀⠀⠀⠐⠰⣀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠠⠠⢉⠂⢀⠀⣀⡀⣀⣀⠀⡀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⣼⣷⣮⣷⣳⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼⡀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠀⠀⢂⠁⢂⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⡱⠈⡐⠀⠁⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣏⣻⣹⣏⣽⣭⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⡟⠀⠀⠐⠂⠀⠂⠀⠉⠀⠉⠉⠀⠌⠸⣛⠃⠀⠒⠲⠶⠞⠷⠶⠶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠆⠡⠘⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣛⠿⣻⢟⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣯⠀⠀⠀⠀⠀⠀⠀⠄⠀⢀⣀⠈⠄⡁⠼⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⡈⠔⡁⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⡀⠀⠀⠀⠀⡄⠐⠠⠀⠀⠌⠐⡠⠀⠄⡀⠛⠿⣶⠀⠀⠀⠀⠀⠀⢀⣴⡞⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⡀⢒⠀⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣮⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣳⣛⠿⢻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⡄⠀⠀⠀⠐⡀⠀⡄⠀⠀⡈⠄⠠⡉⠄⡐⢠⠀⠰⣄⠀⠀⠀⠀⢀⣾⡏⠀⠀⠀⠀⢸⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢃⠰⡀⠌⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⡵⣾⣾⣷⣾⣷⣶⣬⢹⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⡇⠀⠀⠆⢀⠀⠀⠀⠀⢤⡁⠀⡁⠀⣃⠀⠀⠙⡠⠈⠓⢤⣀⣴⡿⢋⡴⠀⠀⠀⠀⠈⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡌⢂⠐⠠⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣷⣻⢧⣛⣬⣙⣬⣑⢎⡏⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣿⡇⠀⠈⠠⠁⠀⠀⠀⠀⠀⠱⣀⠀⠀⠀⠂⠀⠀⠀⠑⡈⠀⠀⢈⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠜⢠⠈⠄⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣭⡟⡽⢛⠿⠻⡟⡟⢞⡴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣨⡿⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠰⠈⠄⠀⠠⠁⠀⠀⠀⠀⠈⠡⢄⠭⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣈⠘⡠⢀⠂⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣿⣿⡿⣿⣷⣾⣾⣶⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠌⠐⠀⠀⠀⠀⠀⠀⢠⠋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢡⠐⡂⠐⠈⠁⠈⠁⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣦⣣⢭⡹⣹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠠⠀⠐⠀⠘⠠⢀⠀⠆⠀⠀⠀⡀⠄⢂⠀⢀⠣⠀⠀⠀⠀⢀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢂⠆⠤⠁⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠠⠁⠂⠄⠀⠀⠀⢢⠡⢈⠔⠈⠠⡄⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡡⢈⠄⡁⠀⠀⠀⠀⠀⠀⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠠⠀⠐⠈⢄⠡⢂⠀⠌⠠⡀⠀⠄⡂⠌⠀⠀⠀⠈⠐⠀⠀⠄⡀⠀⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠠⢐⠈⠄⠀⠀⠀⠀⠀⠀⠠⣿⢞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⠋⠁⠀⠀⠀⠈⠀⠀⠂⠈⠐⢂⠡⢈⠌⠐⡀⢁⠠⠁⠀⠀⠀⠀⠀⠀⠰⣀⠒⠠⠑⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⠡⠌⡀⠀⠀⠀⠀⠀⠀⠐⡿⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠁⠀⠀⠀⠀⠀⠈⠀⢂⠠⠀⠈⠆⡐⠂⢌⠐⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠌⣂⠱⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⡔⠁⠆⡀⠠⠀⠀⡀⠀⠜⣼⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠘⡠⠉⠄⡂⠄⠀⠀⠀⢀⡀⠀⡀⠀⠀⠀⢀⠀⠄⡡⠒⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡐⠠⢉⠐⠀⠁⠄⠂⢀⠀⠈⠱⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⠉⠃⠘⠉⠀⢀⠠⠀⠈⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠐⠩⠐⠠⠀⠀⠀⠀⠀⠀⠄⠠⠐⠀⠀⠀⠈⠠⢑⠈⡐⠀⠐⠈⠀⠈⠀⠁⡈⠄⠁⠀
		⠀⠄⠱⢀⠂⠄⠀⠄⠂⢀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠈⠁⠀⠀⠀⠀⢀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⠀⢀⠠⠀⠀⠀⠄⡀⠡⠀⠁⠠⢀⠀⠠⠀⠄⠂⡑⠀⠀⠀⠀⠀⠀⠀⠀⠐⡈⠀⠀
		⠀⠌⢢⠀⡃⠀⠂⡀⢈⠀⠄⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢻⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⠁⢀⠀⠀⠂⠀⠀⠄⠡⠈⠄⠁⠀⠈⠄⠂⢀⠂⠄⠀⡁⠀⠈⠀⠀⠀⠠⠈⢀⠀⠀
		⠀⠌⢠⠡⠀⢁⠀⠄⠠⠀⠠⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣳⣝⡳⣽⣞⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠂⠀⠁⠈⠀⠄⠀⠀⠈⡐⠈⠠⠀⠂⠠⠐⠀⠀⠀⠀⠀⠀⠌⡀⢈⠀⠀⠀
		⠀⠌⣀⠂⡉⠄⡂⠔⡂⠌⡐⢠⠀⢂⠈⢉⢿⣿⣿⣿⣿⡿⣟⡿⡿⣭⢳⡓⣎⠷⡱⣞⡽⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠐⠀⠀⠀⠀⠀⠀⠀⠂⡐⠀⠠⠐⠀⠡⠀⠡⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠁
		⢀⠂⠄⡘⠄⢃⠈⡔⠈⡔⠠⢁⠘⠀⠄⢂⠠⠟⢻⣿⣿⡽⣽⢺⡵⣩⢖⡹⢬⡓⡵⣪⢽⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠂⠐⢀⠂⠠⠀⠂⠠⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀
		⠀⠌⡐⠁⠎⡀⠆⠠⡑⢠⠁⢂⠆⠡⠈⠄⠂⠌⠀⡘⣿⣿⣿⣿⣾⢷⣫⠽⣏⠷⣱⡝⡾⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⡯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠂⠀⠐⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
		⠀⠂⠄⡩⠐⡡⢈⠑⡐⠢⠌⠠⠈⠀⠁⠠⠈⠠⠀⠀⣿⣿⣿⣿⣿⣿⣞⡽⣎⢷⣣⢟⣽⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡲⡽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡁⠢⡐⢡⠂⢢⠑⢨⠁⢌⠠⠁⠀⠐⠀⡁⠄⠁⠀⢾⣿⣿⣿⣿⣿⣿⡾⣽⢮⣷⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⡟⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠠⠀⠀⠀
		⠀⠄⣁⠒⠤⡘⢀⠎⠤⠉⠄⡂⠄⡁⠈⠀⠀⡀⠀⠍⣺⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⢮⢷⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⡈⠐⡠⢈⠤⡁⢌⠰⡈⠜⠠⠁⠀⠀⠀⠀⠁⠀⠀⠠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡝⡭⢖⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⣁⠰⡁⠂⠌⠄⠡⠘⠀⡁⠀⠀⠐⠀⠀⠈⠀⠀⠠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢮⣱⢋⣿⣿⣷⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠈⠠⠀⠉⠀⠀⠀⠉⠒⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⡀⡀⠀⠀⠀⠀⢀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠓⢤⡀⠄⠠⢀⠐⡀⢀⠀⠄⠀⠀⠀⠉⠀⠀⠀⠀⠀⠉⠁⠈⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠈⡁⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⡀⢌⠱⠈⠡⢉⠐⠠⠀⠤⠀⠀⠂⠂⠄⠈⠉⠀⠀⠀⠀⠤⠐⠀⠆⠄⡀⠀⠀⠀⠀⠀⠀⠈⢳⠀⡁⢂⠡⠐⢄⠊⠌⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠐⠆⡐⠠⠑⠀⢁⠲⠄⢢⡐⠠⠁⠀⠈⠀⠉⠀⢂⡁⠂⠄⡌⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠀⠀⠀⠀⠀⠈⠢⠐⡀⠒⠠⣀⢀⡀⠀⠀⢠⠁⡐⠈⡄⢃⠀⠈⠰⢀⠢⠄⡠⣀⢄⠲⠌⠃⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠲⢀⠀⠀⠀⠀⡁⠐⠂⡄⠐⠈⠁⠑⠲⠤⠧⡄⠀⠀⢈⠆⠠⢁⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠐⠀⠀⠀⠀⠀⠁⢂⣐⠢⢌⠈⡁⠂⢌⠠⡑⢌⠢⢀⠀⡀⠂⠄⣂⢔⡠⠌⠲⠌⠤⢄⡡⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡆⠀⠂⢈⠀⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠠⠈⠆⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠘⡈⠐⣂⠐⡂⢁⠂⡴⠀⠃⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠈⠁⡀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠛⠂⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠠⢀⠡⢀⠡⠈⠄⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠴⣀⠂⠄⠡⠈⠄⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠈⣡⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠈⠀⠀⢠⣤⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠂⠄⠠⠋⠀⢀⡆⠨⠐⠀⡌⠀⣹⡿⢷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠐⠋⠁⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡞⠋⠉⠁⠀⠀⢀⣀⡀⠀⠀⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠂⠒⢤⣤⣤⡈⠤⠁⠀⠀⠀⢀⠀⠁⡀⠄⠀⠙⣿⣤⠈⠙⠻⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠚⠉⠀⠀⠀⠀⠀⠀⠈⠛⢷⣆⠀⠘⢳⣤⠀⠀⠀⠀⠀⠀⠀⢀⣰⡆⢀⣴⡿⠃⠀⠀⠀⠀⠀⠈⠙⢷⣌⠢⠀⠀⠀⢂⠀⡀⠐⢨⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣄⣀⢉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⢷⣾⣽⢿⣦⠀⠀⢀⣤⣶⣿⣿⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⣅⠀⠀⠄⠆⠐⠄⠲⠀⠀⠀⠀⠹⣷⡀⠠⠀⢀⣀⡉⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⠙⠻⣾⡇⠀⠀⠀⠀⣠⣴⣾⣿⡿⢿⣿⣿⣛⣿⣿⣶⣦⣤⣠⣄⣀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣷⡙⠷⡾⠟⠛⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠈⠀⠌⢀⠱⠀⠀⠀⠀⢰⣿⡄⣠⣴⡿⠋⠉⠀⠀⠉⠙⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠿⠂⠀⠀⣼⡿⣫⣿⣷⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣤⣴⠟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡐⠠⢉⠂⢀⠂⠀⠀⠀⢀⣿⣿⠟⠛⠉⠀⠀⠀⠀⠀⠠⠀⠀⠈⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠢⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⢲⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⢀⣠⣿⠿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠐⡀⠣⢈⠂⠈⠀⠀⣠⣾⠟⢣⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠘⠷⢦⣄⠀⠀⠀⣼⣧⡄⠀⠀⠀⣸⣿⣍⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣆⠀⠀⠀⠚⠋⠁⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⣀⠣⠀⢃⠀⣾⡿⠉⠀⠆⠁⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠈⢻⠷⣦⢴⣿⠃⠀⠀⠀⢀⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⣤⠀⠀⠀⠰⣦⡻⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⢀⠂⠁⠀⣼⣿⠃⠀⠀⠈⢶⣈⠄⠀⠀⠀⢠⡤⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣾⡟⠀⠀⠀⠀⠸⣿⣇⢻⣿⣿⢿⡿⢿⡻⣿⠿⣛⠻⣩⢉⠬⣁⠒⢌⠻⣿⣿⣿⣿⣿⣿⣾⡷⠛⠁⠀⠀⠀⠀⠉⠻⣷⣬⠙⠻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⠟⠁⠀⣨⠔⠀⠁⣿⡇⠀⠀⠀⠀⠀⠻⣦⠀⣶⣿⣯⠄⠠⠁⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⢀⠀⠁⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⡀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠸⣿⣷⣿⠟⣿⢮⡝⣆⠳⣌⠳⣄⡳⢆⣎⡖⢠⠉⢂⡱⢻⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⢀⣿⣿⣡⠆⠀⠀⡄⠂⠌⡐⣿⡅⠀⠀⠀⠀⠀⠀⣻⣴⡿⠛⠀⠀⠀⠐⠂⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⡀⠄⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣇⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⣿⣿⣏⢞⣱⢻⡾⣎⠷⣨⠳⢥⠓⠎⡬⢑⠠⢈⠰⢄⡋⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢷⣶⣤⣼⡿⡄⢀⡀⣀⣤⣶⠿⠛⠋⠁⠀⠀⠘⡠⢁⠂⡐⣿⠂⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠐⠒⢻⣿⣿⢮⣷⣫⣟⣻⡜⣡⢫⣷⣯⣜⣤⣋⣴⣦⢘⠢⠜⣹⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠙⣿⢩⣿⣿⣿⣯⣥⣀⡂⠤⡀⠀⠀⠠⢃⠄⠂⠄⣻⠁⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⣿⣿⢘⣿⣿⣿⣿⣿⣿⣧⠙⠿⣿⣿⣿⣿⣿⣿⢿⡷⡘⣿⣿⣟⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠟⠁⠀⠈⠉⠛⢿⣷⡄⠁⠄⠠⣉⠂⡁⠂⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⢸⣿⣄⠀⠀⠀⣸⣿⣿⣿⡿⡿⣟⣿⣿⣿⣘⠢⡹⣿⠿⣟⡛⠿⢋⠔⡹⣿⣿⢿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡿⢿⡆⠀⠀⠀⠀⠀⠀⠙⣿⣎⡠⠁⡀⠒⠠⢁⠘⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠁⠂⠁⠂⠄⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⢹⣷⡀⠀⠀⠀⣼⡿⠹⣦⡀⣾⡟⠩⣿⣷⣏⢷⡻⣿⣽⣿⠇⢣⠑⡤⢃⡜⡈⠶⣅⡊⠔⡙⢿⣇⣻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣾⡿⠛⢉⣀⡘⢿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢷⣶⡀⢁⠂⠄⡘⠀⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣷⣀⣰⣾⡿⠁⠀⠘⢿⣿⣿⣆⢻⣿⣟⣮⢗⣻⣿⣯⣼⣦⣷⣬⣅⠒⣍⠒⠤⡘⢬⣑⣪⣽⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⢋⣠⣴⠟⠛⢿⣦⡌⠻⣿⡆⠀⠀⠀⠀⠀⠈⢿⣏⠠⢈⠐⡈⢀⣠⣴⣾⡿⢹⣦⡀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢀⣠⣶⡾⠛⠋⠉⠉⣿⣿⣿⠃⠀⠀⠀⠚⠛⠿⣿⣼⣿⣿⡯⣞⡽⣏⠿⣏⠹⣉⠿⣿⢊⠤⢋⡴⣉⣦⡿⠟⠋⠉⠉⠽⣿⣷⣄⡀⠀⠀⣠⣶⡟⠋⢴⡿⢟⠁⠀⠀⠀⠙⢿⣆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠋⡐⠄⢂⠐⣈⣽⣿⠋⠀⠈⠿⠿⣶⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠂⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⣼⣿⣿⣥⢀⠀⠄⠀⡀⠈⣿⡟⠀⠀⠀⠀⠀⠀⢀⣻⣿⣿⣿⡷⣹⣞⣽⣾⣷⣧⣶⣾⣷⣎⠜⣢⠱⡩⢿⣿⣆⣄⣤⣤⣶⢹⣿⣿⠷⣴⡾⠟⣡⣤⣾⠇⠀⠈⠀⠀⠀⠀⠀⠈⢿⣇⠙⢿⣄⠀⠀⣼⡿⢃⠠⠉⠂⠡⢸⣿⠟⠁⠀⠀⠀⠀⣴⣸⣿⠋⠀⠀⠐⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⣬⣿⠟⠁⠀⠀⠈⠉⠄⠁⢠⡙⣿⣇⠀⢀⡀⣀⣀⣀⣸⣿⠀⠽⣿⣿⡵⣫⢞⣿⡟⢯⡙⣌⢛⣿⣇⠲⣅⢳⣻⣿⣿⣿⣿⣿⣿⠈⠙⢿⣶⣁⣆⠟⠛⠉⠁⠀⠀⠘⠀⠀⠀⠀⠀⠀⠘⣿⣦⡘⢋⣤⣿⠟⠁⠈⢴⡀⢁⠂⢹⣿⠀⠀⠀⠀⠀⠀⠈⣿⡏⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠌⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠤⠐⠈⣄⣵⡿⠟⠁⠀⠀⠀⠀⢠⡇⠀⠈⣶⡅⠘⣿⣟⠛⠛⠛⠋⠛⢻⣯⠀⠀⢹⣿⣷⣹⢫⡽⡟⢦⡱⢌⢆⡣⢌⡳⣘⠧⣾⣿⣿⣯⢿⣿⡯⠀⠀⠀⢿⠿⠟⠀⠀⠤⡀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣤⣿⡯⠐⠀⠀⡐⠌⠀⠄⢹⣿⡀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠠⣄⠀⠀⠀⠀⠑⢂⠀⢂⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠐⡠⠂⠁⠈⠄⣈⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⣾⣧⡆⠀⠹⣷⡂⠈⢿⣆⠀⠀⠀⠀⢸⣿⠀⢠⣿⣿⣧⢯⠷⣾⣿⣶⣷⣮⣗⢬⠓⡴⣉⠞⣽⣿⣿⣿⢯⣿⣷⠀⠀⢀⡼⠂⠄⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠣⣦⡀⢂⠡⠈⢸⣿⡁⠀⠀⠀⠀⣼⣿⠑⡀⠀⠀⣖⣿⡄⠀⠀⠀⠀⠀⠘⠄⢂⡐⠀⡀⠀⠀⢀⠀⠀
		⠈⠀⠀⡄⠑⠈⠀⠃⠀⠂⠥⠈⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⣽⣅⠈⠌⣿⣆⠀⠀⠀⢸⣿⣶⣿⢃⣿⣿⣏⡿⣽⣿⣿⣿⡟⣭⢎⡹⢰⠡⢞⣽⣿⣿⣿⣿⣿⣿⣤⣴⣿⣉⠒⠙⢶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⢉⠀⠀⠀⠀⢻⣟⠀⠄⠡⢘⣿⠆⠀⠀⠀⣠⣿⠇⠒⠀⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⡀⠀⢀⠀⠀⠀
		⢠⣌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠈⠙⣿⡄⠀⢹⣿⡀⠀⠀⣿⣿⣿⣿⠠⣿⣿⡾⣝⡷⣾⣹⢿⣿⢆⡏⡼⣡⢋⠬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣼⣥⣄⣀⡀⠀⠀⠀⠀⠀⣀⣼⠟⠉⠠⠐⠤⠀⠀⠀⣠⣿⡏⠠⢈⠐⢨⣿⠂⠀⠀⢠⣿⡏⠀⢌⡄⠀⠀⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠁⠂
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠇⠀⠀⠀⠀⣽⠇⠀⠀⣿⡇⣠⣴⣿⣿⣿⣿⡀⢽⣿⣿⢭⣻⢧⡟⣯⢿⣯⡜⡲⣅⠫⣜⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣉⡁⠄⢨⡐⡠⠒⠀⠀⠀⣼⡿⠀⡁⠂⠄⢂⣿⠇⠀⠀⣾⡟⠀⠌⡈⠀⠀⠀⠀⢹⡟⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠆⡈⠄⡡⠀⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⣀⡀⠛⠀⣄⣹⣶⣿⣿⣿⣿⣿⣿⣿⡇⠀⢻⣿⣷⡹⣞⡽⣽⣺⣿⡷⡱⣌⢳⣾⣿⠇⢨⣭⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⠉⡅⠒⠀⠀⡼⠟⠁⠀⠜⠠⠁⢠⡿⠀⠀⣼⣿⠀⠌⡐⢠⠀⠀⠀⠀⠀⠛⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡐⢀⠒⢠⠃⠀⠀⠀⠀⣼⣿⠻⠁⠀⠀⠀⢀⣱⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠙⢿⣿⣮⡕⣣⠿⣿⢳⡳⣼⣿⣿⠏⠀⠀⠌⡑⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠱⠈⡌⠁⠀⠠⡘⠀⠆⢈⠄⡻⠀⢠⣿⡟⠀⠀⢰⡀⠣⣤⠀⠀⠀⠈⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠎⡐⠤⠃⠨⢀⠂⢄⣠⠀⠀⣿⡇⠄⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠈⠻⣿⣿⣤⢋⡖⣯⣿⣿⣿⠋⠀⠀⠀⢮⠱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠁⠒⡍⠀⠀⠀⠈⠥⠐⡈⢀⠳⠀⣿⡿⠇⠀⢀⣿⠇⠠⢐⡆⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠰⢈⠐⡐⠈⠀⠀⠀⠀⠈⠄⡉⠷⣼⣿⢆⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣇⠀⠀⠈⠛⢿⣿⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⢑⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠡⡌⣁⠀⠀⠀⠃⠂⡔⠀⠂⡜⢋⠡⢀⣤⣿⡿⠀⠑⢢⡑⡀⠀⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⠌⡑⠂⡄⢠⠘⢀⢂⠱⠀⠀⠀⠀⠀⠀⠀⡒⣤⣊⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠠⢃⠀⠀⢀⣀⣀⣹⡻⣿⣡⣀⣀⣀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⢀⠂⠄⢠⠀⡐⠄⡉⢂⠡⠂⡄⣫⣿⠏⠀⠀⠀⠀⠘⢡⠐⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠢⢡⠐⠠⠌⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠁⠛⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣾⣷⣿⡿⢿⡿⣿⣷⢿⡿⣿⢿⣿⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠒⠌⡀⠀⠘⡐⠐⡈⠄⣱⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢊⠔⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⠠⠡⢈⠥⠀⣀⢀⡀⣀⣀⣀⡀⢀⠀⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⠿⡿⢿⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⠀⠐⠀⠑⠈⡐⢀⣶⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠐⡅⢃⠠⠁⠀⠂⠀⠀⠀⠀⠈⠀⠁⠀⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠉⠀⠁⠉⢐⠀⠚⠟⠡⠐⠲⠻⠟⠳⠟⠶⠶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⡌⢂⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣥⣧⣜⣴⣌⣶⣭⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⡀⠀⠀⣄⠊⠠⠁⠚⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠰⡀⠆⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⣙⣛⣋⣏⣛⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠰⠁⠀⠐⢠⠐⠡⠈⠄⠉⠛⠿⣷⡄⠀⠀⠀⠀⠀⢀⣴⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠡⡅⢨⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠿⠿⠿⢿⠿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⡔⠀⠀⠤⡈⠠⢡⠈⡐⠈⡄⢹⣷⣄⠀⠀⠀⢀⣾⡏⠀⠀⠀⠀⢸⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢣⠀⠆⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠤⢁⠀⠁⢀⠣⠀⠀⠙⣆⡙⠻⣦⣄⣴⡿⢋⡴⠀⠀⠀⠀⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢢⠉⠄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣦⣷⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠈⠐⢂⠀⠀⠈⠄⠀⠀⠈⢷⣦⡙⠛⢩⣷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢣⠘⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣿⣹⣛⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠘⡈⠂⢀⠀⠃⠀⠀⠀⠀⠙⢿⣧⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⡈⠔⣈⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢀⠀⠰⠐⡀⠂⢀⠂⠀⠀⠀⠀⠀⢸⠟⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠒⡄⢊⡐⠀⠉⠈⠁⠈⠁⠁⠈⠀⠁⠀⠈⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣞⢧⠯⣝⡻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠛⠀⠠⠁⠄⡀⠠⠀⠀⠀⠀⡠⠄⠂⡀⠈⠒⠀⠀⠀⠀⠀⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⡀⠆⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣞⡽⢎⡟⣼⠳⣭⠶⣹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡔⠀⠁⠂⡐⠀⡁⠀⠀⠨⡅⢐⡐⠀⠰⡈⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢃⠰⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣻⣼⢫⡞⣵⣛⢦⣻⡱⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠈⠀⠐⡠⠀⠄⢀⠰⡀⠃⠀⠀⠀⠈⠁⡀⠀⡀⣀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⡌⠰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⡟⣽⡟⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣻⢮⢷⡹⢶⣙⢮⡱⣳⡝⣾⣿⣿⣿⣿⣿⣿⣿⡟⠋⠐⠠⡀⠑⠠⠁⠌⢀⠠⠁⠀⠀⠀⠀⠀⠀⡐⡄⠰⢀⠊⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠘⢄⠣⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣟⠶⣹⡱⢭⡚⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣻⢾⣝⢧⣛⢮⣓⢧⣻⣽⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⡀⠡⢈⡐⠁⠂⠀⠈⠀⠀⠀⠀⠀⠀⠀⠁⠈⠐⢢⠰⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢈⠰⡈⠆⠀⠀⡀⠄⠠⠀⠀⡀⠀⡀⠀⠀⢠⣿⣿⢫⡝⣥⢛⢦⡙⡴⣋⢯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣯⣞⣧⣛⡾⣷⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠰⠐⠠⠠⢁⠂⠀⠀⠀⢀⡀⠀⢀⠀⠀⠀⢀⠠⢀⠡⢃⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠄⢂⠱⠈⠀⠡⠐⠈⡀⠀⠀⡀⠂⠄⠀⡀⢨⣿⣿⢆⣿⢦⢋⢦⡹⡰⡍⡞⢮⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠐⠀⠠⠁⠃⠁⢂⠀⠀⠀⠈⠀⠀⢀⠂⠀⠀⠀⠀⠂⢀⢃⢈⡐⠀⠐⠈⠀⠈⠀⠁⡈⠄⠁⠀
		⠀⠌⠠⢃⡐⠀⠁⠀⢂⠐⡀⠀⠠⠁⠌⠀⠄⠹⣿⣿⡹⢎⠦⣉⠮⡱⢱⡘⡌⢧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠂⠀⠁⢀⠀⢀⠀⠀⠀⠀⠄⡀⢁⠂⠀⠡⠀⠂⠀⠄⡀⠄⠂⠄⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠂
		⠀⠌⣁⠢⠐⠀⢂⠐⠠⠐⠀⠀⠀⡡⢂⠀⠄⣀⢻⣿⣗⢎⠲⣥⡷⣡⠳⣘⢌⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⡀⠂⠀⠀⠄⠀⠈⡀⠄⠀⡐⠠⠀⠄⠁⠀⢈⠐⠀⢀⠐⠠⠐⠈⠀⠀⠀⠀⠀⠠⢈⠀⠀⠀
		⠀⠂⢄⡑⢈⠀⠀⠌⢀⠡⠀⠁⠂⠀⠄⡈⠄⠠⢘⣿⣿⣎⢿⡹⡜⣥⠓⡥⢞⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡀⠀⠈⢀⠀⠀⠂⠀⠀⡀⠈⠀⡁⠂⠠⠈⠀⡐⠀⠂⠀⠀⠀⠀⠀⠈⠄⢀⠀⠈⠀
		⠀⠌⢠⠐⣀⠢⠐⡄⢢⠐⡄⢁⠎⠡⡀⢐⠨⣁⠂⢽⣿⣿⣮⢷⣹⣖⣻⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠙⠻⠿⠟⠣⢀⠁⠂⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠁⠀⠀⠐⠠⠀⠠⠐⠀⠄⡈⠐⠀⠀⠀⠀⠀⠀⠈⢀⠂⠀⠀
		⠠⠌⢠⠘⢠⠁⡘⢠⠃⢒⠈⠄⡈⡑⢀⠢⡐⠠⢊⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠁⠀⠀⠀⠠⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠡⠐⢀⠂⠠⠀⠐⠀⠄⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⠌⡐⠌⡀⠂⠄⡁⢌⠂⡡⠂⠔⡐⢀⠂⠐⠡⠂⠄⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠐⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠈⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
		⠀⢂⠐⢂⠡⡉⠆⠑⠢⢌⠠⢁⠂⢀⠂⠄⠀⢂⡉⠠⠐⡈⠻⠿⠟⢋⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⠠⠘⢄⠒⠄⡘⠌⡑⢂⠡⠀⠃⠂⠉⠐⠈⢀⠒⢀⠡⠐⠡⢊⠐⠡⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⠧⡹⣿⣿⠧⣏⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠠⠀⠀⠀
		⠠⢁⠊⡄⠌⠤⢁⠒⢌⠰⢠⠁⡌⠀⠌⢂⠐⠀⠌⢂⡐⢈⠐⠠⠈⢤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⡲⣽⣿⣿⢏⡜⢮⣱⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠒⠠⣁⠆⡌⢢⢁⡌⢢⠑⡂⠁⠀⠄⠀⠀⠀⠠⠀⠐⠀⠀⠀⢀⠘⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⡕⣻⣿⣿⣇⠺⣐⠧⣛⠼⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢈⠐⠄⡚⠈⡄⢣⠘⡥⠊⠐⠀⠀⠈⠀⡀⠂⢀⠠⣀⠂⣤⠀⣠⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢳⢹⣿⣿⢎⡱⢊⡖⡩⢞⡽⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠈⠠⠈⠁⠀⠀⠀⠉⠒⠀⠀⠀⠈⠁⠈⠀⠈⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠃⢴⡀⠠⠀⠄⡐⠀⡀⠀⠄⠀⠀⠀⠉⠀⠀⠀⠀⠀⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠈⢁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⡀⢌⡘⠠⠉⠒⡀⠆⢀⠰⠀⠀⠂⠂⢄⠈⠁⠀⠀⠀⠀⠤⠐⠀⠆⠄⡀⠀⠀⠀⠀⠀⠀⠈⢳⠀⡁⠒⡠⠡⢐⠡⠊⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠂⠄⡑⠂⠀⠲⡀⢰⠀⡐⠀⠁⠀⠈⠈⠀⢠⠁⠌⡐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⠐⡀⠢⢀⡀⣀⠀⠀⠀⢠⠁⠄⢡⠐⢡⠀⠀⠡⢂⠂⠤⢀⢠⠠⡔⠌⡑⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⠀⠀⠀⠀⠁⠠⠐⠂⠌⠁⠀⠁⠓⠸⠰⢦⠄⡀⠀⢈⠆⡈⢐⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠐⠀⠀⠀⠀⠀⠁⢄⡰⢀⠇⡈⢁⠂⠌⡐⠂⡍⢄⠂⡀⠐⠠⢈⡐⢌⢢⠐⠜⠢⠤⢀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠐⠈⠁⢂⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠈⢠⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠁⠀⠀⠀⢈⡐⠡⢂⠱⢈⡀⢂⡔⠁⠂⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠈⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠛⠄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⢀⠐⠠⠁⠌⠠⠐⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡼⣟⠇⠀⠀⠀⠀⠄⠀⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢌⠢⠁⠌⡐⠁⠂⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠈⠀⢀⢠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠄⠠⠉⠀⠠⡅⢂⡐⠈⠄⡀⣼⣻⢷⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠉⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠂⠤⢤⣠⠈⢄⠁⠀⠀⠀⡀⠀⠀⠄⠠⠀⠘⣿⣤⠈⠉⠻⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⠆⢀⣤⡾⠃⠀⠀⠀⠀⠀⠀⠙⢿⡄⠂⠄⠀⠀⠐⡀⠀⠈⠰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢷⣾⣟⢿⣦⠀⠀⢀⣤⣶⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣥⣂⠀⠀⠰⢁⠘⠠⣘⠀⠀⠀⠀⠹⣷⡀⠠⠀⢀⣀⡉⠹⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣷⡘⠳⠾⠟⠛⡟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡄⠀⠠⠀⠁⠤⠀⠀⠀⠀⣰⣿⢄⣠⣴⠟⠋⠉⠀⠀⠈⠙⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢷⣄⠀⠀⠀⠀⢀⣠⣶⣿⣷⣦⣶⣶⣾⣷⣦⣴⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⣀⣴⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⣀⠣⠁⠈⠄⠀⠀⠀⢀⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠒⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⢿⣄⠀⣠⣶⣿⣿⡿⢿⣧⣶⣦⣷⣾⣿⣾⣿⣿⣿⣿⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀⢀⡾⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠄⠢⠑⠌⠐⠀⠀⣠⣾⠟⢣⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠘⠷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣾⣮⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⡁⠎⠐⢂⠐⣾⡿⠉⠀⢂⠐⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠈⢻⠷⠦⣄⡐⠀⠀⠀⠀⠀⠀⠈⢻⣷⣮⣝⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣤⡀⠀⠀⠀⣤⡻⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣟⠀⣀⠃⠌⠀⣼⣿⠃⠀⠀⠀⢶⣠⠀⠀⠀⠀⣀⡄⠀⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠈⢶⣼⣇⠀⠀⠀⠀⠀⠀⠀⣼⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠈⠻⢷⣬⠉⠻⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⠏⠁⢀⠠⠆⠀⢀⣿⡇⠀⠀⠀⠀⠀⠹⣦⠀⣶⣿⡯⢀⠐⠠⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠂⢀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⣾⣿⣣⣿⣿⣿⣿⣿⣿⣿⡿⢟⠟⡻⡙⠍⢫⡙⢹⠻⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢻⡷⠀⠀⠙⢷⣆⠀⠀⠀⠀⠀⠀⢀⣿⡿⣀⠆⠀⠀⡌⡐⠈⠄⣿⡆⠀⠀⠀⠀⠀⠀⣻⣤⡿⠛⠀⠀⠀⠐⠠⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢺⣇⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⣿⣿⡿⣹⣿⣷⣋⠶⣱⢢⡙⡌⢎⠱⣈⠆⡁⠆⠡⢎⡹⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢷⣶⣬⣼⣿⣄⡀⣀⣀⣤⣶⠿⠛⠉⠉⠀⠀⠘⡐⠠⢁⠂⣿⠂⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠃⡀⠀⠃⠄⠂⠀⠀⠀⠀⠀⠄⡀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⣿⣿⣗⣿⣿⡷⣮⣿⠦⡗⣼⣘⢬⡦⠥⠶⣬⠜⡠⢂⠱⣻⣿⣿⣿⣿⣣⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⢩⣿⣿⣿⣯⣴⣀⡂⠤⠄⠀⠀⠠⢡⠁⠂⠄⡻⠁⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⣿⣿⡿⢏⣾⣿⣿⣯⢳⡱⣘⣿⣦⣱⣌⡱⣀⠜⣠⢃⠱⣹⣿⣿⣿⡏⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⠈⠉⠛⢿⣷⡌⠐⡀⠄⢃⠜⢀⠂⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⢸⣿⣄⠀⠀⠀⠀⢿⣿⢃⣴⣿⣿⣿⣿⣿⣷⣇⠚⣿⣿⣿⣿⣿⣿⣶⣮⣦⣱⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⡄⠀⠀⠀⠀⠀⠀⠙⣿⣦⡐⠈⡀⠊⠄⢂⠘⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠀⠒⠈⠐⠀⠂⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢹⣷⡀⠀⠀⠀⣸⡟⠻⣷⣄⠀⠀⢸⣿⣿⣿⣿⡿⣿⣿⢿⣿⣿⡜⣠⠚⡿⠿⠿⠿⠿⠧⡩⢼⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⡿⠛⠉⣀⠘⢿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢿⣦⢠⠁⠌⠠⢘⠀⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣷⣀⣠⣾⡟⠁⠀⠘⢿⣧⠀⣾⣆⠁⡙⢿⣿⣶⣝⡞⣿⣿⡍⠤⡋⠜⢣⡃⢎⠥⢣⡒⠩⡍⣯⡙⣿⣿⡄⠀⠀⠀⠀⠀⠀⢀⣼⡿⢃⣠⣴⠈⠙⢿⣦⡌⠻⣿⡆⠀⠀⠀⠀⠀⠈⢿⣧⠈⠄⡁⠂⢀⣠⣴⣿⡟⢳⣶⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢀⣠⣶⠾⠛⠋⠉⠉⢻⣿⣿⠁⠀⠀⠀⠘⠛⠿⣾⣿⡆⠩⣿⣿⡿⢿⣿⣧⣽⣽⣆⣱⡉⠦⡙⣌⠲⡩⢜⣱⣬⣹⣿⣿⣿⣿⣄⡀⠀⠀⣠⣶⠿⠋⢴⠿⢛⠀⠀⠀⠀⠙⢿⣆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠃⡜⠠⢀⠡⣈⣽⣿⠋⠀⠀⠿⠿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⢂⣼⣿⣿⡄⢀⠀⠀⡀⠀⠘⣿⡏⠀⠀⠀⠀⠀⠀⠀⣿⢿⣿⣡⢻⣷⣏⢿⣹⢻⣿⣟⢛⠻⠿⣇⡜⢤⢣⣱⣿⣟⣛⣛⣋⣿⢋⣻⡿⠷⣤⣾⢛⣡⣦⣼⠎⠀⠈⠀⠀⠀⠀⠀⠈⢿⣧⠙⣿⣄⠀⠀⣼⡿⢃⠠⠘⠁⠂⢴⣿⠛⠁⠀⠀⠀⠀⣴⣸⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣸⣿⠏⠁⠀⠀⠈⠀⠡⠀⠠⠘⣿⣆⠀⠀⢀⠀⡀⠀⣰⡟⠈⠻⢿⣾⣿⡞⣧⣿⣷⣼⣿⣷⣬⣵⣦⢋⢆⠣⣾⣿⣿⣿⣿⣿⣿⠏⠘⠻⣧⡐⡄⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡘⠿⣠⣿⠟⠁⠈⢶⠁⡈⠐⣸⣿⠀⠀⢀⠀⠀⠀⠈⣿⡏⠀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠄⠠⢀⣡⣼⡿⠟⠁⠀⠀⠀⠀⠀⠃⠀⠰⣧⡀⠙⣿⡗⠛⠛⠛⠛⠛⢻⣏⠀⠀⠈⢻⣿⡿⣍⠿⣿⣿⣿⠏⣭⢙⡻⢟⡬⢣⣽⣿⣿⡿⣿⣿⣿⠀⠀⠀⠹⠿⠇⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣶⣿⡿⠀⠄⠀⠘⠂⠄⡁⢼⣿⡀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⢀⣀⠀⠀⠀⠀⠐⢀⠂⠌⡀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⢀⠂⠌⠀⠡⠈⡐⡲⠛⠁⠀⠀⠀⠀⠀⠀⠀⣴⣦⡆⠀⠹⣷⡄⠘⣿⣆⠀⠀⠀⠀⣸⣯⠀⠀⠀⠀⣿⣿⣿⣷⣎⣿⢧⢫⠔⡣⢞⡢⣜⡱⢾⣿⣿⣿⣿⣿⣿⠀⠀⢀⡐⠈⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠉⠾⣦⡅⢌⠐⠠⢸⣿⡁⠀⠀⠀⠀⣼⣿⠡⠀⠀⠀⣦⣿⡄⠀⠀⠀⠀⠀⠈⠆⢠⡁⠂⢀⠀⠀⢀⡀⠀
		⠈⠀⢀⡐⠈⠀⠁⠂⠈⠀⠱⠀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⣼⣆⠁⠘⣿⡆⠀⠀⠀⢸⡷⠀⠀⢀⣦⣿⣯⣝⡿⣿⣿⣮⣓⣮⣱⣎⡵⢢⡱⣿⣿⣿⣿⣿⣿⣿⠀⢀⠈⡀⢉⠠⠹⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠩⠁⠀⠀⠀⣻⡿⢀⠈⠄⢸⣿⠆⠀⠀⠀⣠⣿⠃⠰⠁⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⠀⠀⡀⠀⠀⠀
		⢠⡜⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠀⠹⣿⡄⠁⢹⣿⡀⠀⠀⢹⣟⠀⠀⣼⣿⣿⣿⣿⢷⣏⣿⣻⣿⣿⣿⢻⡑⢣⠒⣽⣿⣿⣿⣿⣿⣿⣆⠄⠂⡐⣀⠂⡁⠠⠹⡇⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠁⠄⠡⠄⠀⠀⣠⣿⡗⠀⡈⠐⢨⣿⠀⠀⠀⢠⣿⠏⡀⢡⠂⠀⠀⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠁⠂
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣟⣿⠇⠀⠀⠀⠀⣿⡇⠀⠀⣿⣇⠀⠀⣸⡿⢀⣰⣿⡇⢸⣿⡿⣏⡾⢶⡯⣟⣿⣧⢃⡞⣡⢋⠾⣿⣿⣿⣷⣯⣿⣿⣿⣦⣄⣀⡀⠀⡁⠈⠻⣦⠀⠀⠀⠀⠀⣰⣿⠟⠀⠄⡡⠈⠔⠀⠀⠀⣼⡿⠀⡑⠠⠁⢂⣿⠃⠀⠀⣾⡟⠀⡐⠈⠁⠀⠀⠀⠹⡏⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠄⡘⢤⠀⠀⠀⠀⠀⠀⣽⣻⣿⠀⠀⠀⣀⣼⡿⠁⠀⠀⣿⡿⣀⢀⣿⣿⣴⣿⣿⡇⠹⣿⣿⢭⣛⢯⣷⢫⣿⣿⡱⡜⣴⢉⠖⣤⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣷⣾⣴⣣⣄⡤⣤⣤⣴⡿⠋⠁⠄⠈⠀⠔⡉⢐⠀⠀⣼⠟⠁⠀⠆⠁⢂⠠⣿⠀⠀⣼⣿⠀⠡⢀⠡⠀⠀⠀⠀⠀⠙⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡁⠢⠐⡈⠇⠀⠀⠀⠀⣼⣿⣽⠇⠀⠀⢈⣿⠋⠀⡀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿⣷⢭⢿⣞⣯⡟⣧⢳⣼⠟⣌⢲⣾⣿⠏⠉⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣄⣀⡀⠐⠰⣀⠂⡙⠄⠀⠠⡘⠠⢁⠠⠘⢧⠀⢠⣿⡟⠀⠀⢦⠈⠳⢤⠀⠀⠀⠈⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠒⢠⠘⠁⠂⠡⠘⢶⣤⡀⢀⣿⣿⡟⠀⣀⣴⡿⠃⠀⣤⣹⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠹⣿⣯⡞⡞⣿⣿⣼⣿⢧⢫⣼⣿⣿⠇⠄⠡⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣦⣄⠐⠻⢠⠀⠀⠀⠀⡅⠂⠌⣀⠳⠀⣾⡿⠇⠀⢀⣾⡇⢀⠊⡄⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠰⠈⠄⡘⠀⠀⠀⠀⠁⠈⠄⠛⣿⣼⣿⣿⢀⣾⢟⡡⣐⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠙⢿⣿⣷⡌⢏⣿⣿⣹⣾⣿⡿⠋⠀⠈⠠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡑⢂⣃⠀⠀⠀⠘⠄⢢⠀⠄⡒⢋⠁⡀⢤⣿⡟⠀⠀⠎⡐⠀⠀⠀⢈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢠⡘⠨⠄⡠⠠⠌⢁⡘⢌⠀⠀⠀⠀⠀⠀⠀⢌⡐⢀⠉⢤⣆⣦⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠜⣿⣆⠀⠀⠻⣿⣿⣜⣶⣽⣿⣿⠟⠀⠀⢀⣤⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⡁⠄⢠⠀⡈⠄⡌⠢⢁⠂⠤⣹⣿⠏⠀⠀⠀⠀⠈⠅⠂⠄⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠣⢌⠠⢁⠌⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡒⢤⠉⠃⠀⠀⠀⠙⣿⣿⡟⠋⠁⠀⠀⠀⠘⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠴⠊⢀⠀⠡⡘⢀⠡⢈⢐⣶⣿⠃⠀⠀⠀⠀⠀⠀⠀⠃⡌⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⢀⠢⠘⡠⢀⡀⢀⣀⡀⣀⣀⡀⢀⢀⣀⣀⣀⡀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣶⣶⣿⣿⣷⣶⣾⣷⣶⣦⣤⣀⡀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⢀⠀⡀⠑⡀⠆⠐⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠣⠑⠠⠀⠈⠀⠀⠀⠀⠀⠈⠀⠀⠁⠉⠉⠡⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣭⣿⣿⣿⣭⣿⣿⣯⣥⠤⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠋⠀⠈⠑⢈⠀⠚⢻⠀⠀⠒⠲⠟⠶⠷⠶⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢀⠎⡐⢁⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡴⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣍⣩⣍⣯⡹⣙⠯⡹⡍⣏⠞⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠆⢀⠐⠈⢂⠁⠺⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡔⡐⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠻⣛⠻⣛⠟⡻⢵⡙⡾⢿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢂⠘⡄⠈⠄⡈⠹⠿⣷⡄⠀⠀⠀⠀⠀⢀⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⠠⢈⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣾⣿⣾⣿⡷⢶⡽⣜⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠐⡀⠀⡀⠤⡉⠄⡐⠠⡀⢹⣷⡄⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢡⠃⠌⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢠⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣥⣳⡜⣮⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠐⠀⠀⠀⠂⠈⡔⠀⠀⠙⣄⠙⠻⣶⣀⣴⡿⢋⡴⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡡⢊⠡⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣎⣥⣹⣌⡿⣭⣻⠵⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠂⢀⠡⠀⠀⠈⡄⠀⠀⠀⢳⣦⣉⠛⢩⣷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡑⠢⠁⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⣯⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⢏⠽⣙⢷⣛⣯⢿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠠⠄⠃⠀⡐⠀⠀⠀⠀⠀⠉⢿⣦⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⡠⢁⠣⠈⡀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡅⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⢻⡼⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⢿⢿⡿⣿⣿⣿⢾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠑⠠⠐⢀⠰⠀⠀⠀⠀⠀⠀⠸⠿⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⢢⢁⠃⠄⠁⠉⠀⠁⠈⠁⠁⠈⠁⠈⠀⠁⠉⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣾⣿⠿⡿⢿⣻⣟⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡷⣮⣷⡿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠀⡄⠠⢁⠀⠀⠂⠀⠀⠀⣠⠀⢂⠀⢀⠓⡀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠢⠄⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡯⢥⣛⡼⣳⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣮⣽⡷⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⡃⠴⡃⠀⠌⣀⠁⠀⠀⠘⡄⢈⠔⠈⠠⢀⠀⠀⠀⠀⠀⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢃⡘⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣿⠻⣝⡺⡵⣯⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⢿⣝⣯⣿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢆⠀⡜⠀⠄⡠⠀⠒⡐⠈⠀⠀⠀⠈⠀⠀⠀⠄⡀⢀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⠢⠌⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣜⢯⢶⡹⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣻⣽⡻⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⠂⠀⢂⠁⡀⢡⠀⠀⠀⠀⠀⠀⠀⡘⡠⠐⡁⢂⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠨⢑⠢⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣻⢮⡳⣝⡾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣳⢿⣟⡿⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⡔⠢⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⢂⠜⠠⠀⠀⠠⢀⠄⠀⠀⡀⠀⡀⠀⠠⢀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢯⡟⣵⢫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢭⠀⠀⠀⠆⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢀⠀⠄⡡⢃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠌⡐⠌⡁⠂⠁⡁⠄⠂⠀⠀⠀⠆⡀⠠⢀⢈⣼⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣯⣟⡾⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣯⣿⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⠠⠀⠀⠀⠈⠀⢀⠈⠠⠐⠀⠀⠀⢈⠠⢁⠄⡂⠀⠐⠈⠀⠈⠀⠁⣈⠐⠀⠀
		⠀⢂⠰⠁⡔⠀⠀⠀⢂⠐⡀⠀⠉⠠⠐⠀⠂⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣯⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣿⣿⣆⠀⠀⠀⠀⠀⢂⠀⠂⠀⠁⢀⠀⠂⠀⠄⠀⠄⢊⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⠂⡄⠣⠐⠀⢂⠐⠠⠐⠀⠀⠀⠡⠀⠄⡀⠂⢿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣽⢷⣻⠾⡽⣿⣦⣄⠀⠀⠀⠠⠄⠁⠄⠠⠀⠀⢈⠠⠈⠀⠌⡀⠠⠈⠀⠀⠀⠀⠀⠠⢀⠀⠈⠀
		⠀⠡⢀⠃⠡⢀⠀⠌⠠⠀⠈⠐⡀⠁⠌⠠⠐⠠⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣻⣞⣯⢏⣿⡱⣏⠟⣿⣷⣆⠀⠀⠀⠀⠠⠁⠐⡀⠂⠠⠀⢁⠐⠀⠄⠀⠀⠀⠀⠀⠈⠄⢀⠠⠐⠀
		⠀⠂⢄⠊⡡⢀⠂⡔⠰⠈⡄⠡⢄⠡⢀⠡⢘⡀⠂⠌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢷⣻⢾⡹⣖⡳⢎⠒⡄⠺⣿⠿⣷⡄⠀⠀⠀⠐⡀⠀⠀⠌⠀⠠⠁⢈⠀⠀⠀⠀⠀⠀⠈⠠⠀⠀⠀
		⠀⠅⠂⠜⢠⠁⡘⠠⢃⠑⡀⢃⠈⠒⡀⠒⠠⠘⠥⣂⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢷⣫⢷⣙⣞⢌⠒⠠⠑⡈⠐⣾⡟⠀⠀⠀⠐⠀⠡⠐⢀⠂⠁⠄⠀⠠⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⠈⠄⠩⠌⢂⠐⡀⠡⡈⢆⢁⠢⠌⠒⢀⠡⠘⠠⡁⠄⡀⠛⠿⣿⣿⡿⠿⠿⠿⠿⠛⠋⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠡⠈⠔⠠⡹⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⠀⠐⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠀⠌⡐⢂⠡⢂⡑⢂⠱⡈⠄⢂⠘⠠⢌⡀⠠⢃⡐⠠⠐⡈⢄⠀⡀⢀⠐⠠⠀⠄⠐⠠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠣⡔⠩⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠃⠌⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠂⠰⢈⠔⢂⠰⢈⠢⡁⠌⠠⢈⡑⠢⡐⢁⠢⡐⢠⠁⡘⢊⠞⠑⢂⠩⠐⠈⠠⠈⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡓⠤⠁⠈⠉⠉⠘⠛⠿⣿⣿⣿⡟⡟⡨⢐⠩⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠠⠀⠀⠀
		⠠⠈⠔⡁⢂⠆⡁⠆⢂⠡⢌⡀⢢⠈⢡⠐⠡⠂⠁⢂⠐⠠⠀⠂⠌⡀⢈⠁⠈⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣟⠻⡟⣭⠳⣜⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⡀⠀⠀⠀⠀⠀⠀⠈⠉⠿⢾⣷⣶⣥⣦⣵⣠⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠌⡁⢆⡘⢄⡊⢔⡈⢆⡑⠂⠌⢀⠐⠀⠠⠂⠁⠐⠀⡁⠠⠁⠘⡄⠀⠄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠰⢆⠜⣿⣿⡓⣌⠳⡍⣆⠳⣌⢳⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠐⡈⠄⠣⢈⠰⣉⠘⠦⠈⡑⢂⠀⢈⠀⡀⠃⠀⠌⢂⠀⣡⡀⡐⠀⠀⡀⠀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⡬⢊⣿⣿⠱⣌⠳⣘⠬⡓⣌⢣⠵⣣⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡬⡅⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠁⠀⠀⠀⠁⡒⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠁⢤⡀⠄⠠⢀⠐⡀⢀⠀⠄⠀⠀⠀⠈⠀⠀⠀⠀⠀⠉⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢁⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⡈⠤⡉⠄⡉⠒⠠⠂⠄⠡⠀⠀⠒⠀⢂⠈⠁⠀⠀⠀⠀⠤⠐⠀⠆⠄⡀⠀⠀⠀⠀⠀⠀⠈⢒⡈⠄⢂⠡⠐⠄⡊⠌⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠐⠆⠠⢈⠒⠈⠐⠲⢀⠰⡀⢀⠂⠁⠀⠈⠀⠁⠐⡄⠠⢁⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠆⡐⠠⢀⡀⡀⠀⠀⠀⠠⠄⢂⠈⡄⢃⠄⠐⠨⢀⠒⠠⣀⠠⢠⠔⠌⡑⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠒⠀⠀⠀⠀⠁⡀⠂⠆⠠⠁⠂⠁⠑⠎⠰⠦⡄⠀⠀⢈⠃⠄⢡⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠐⠀⠀⠀⠀⠀⠁⡄⣠⠑⡩⢀⢉⠐⢨⠀⡅⢒⡈⠄⡀⠠⢁⠠⣁⢢⠑⠢⠘⠆⠤⢀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⡀⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠡⠈⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠀⢈⡐⢂⠡⡐⢂⠐⢠⠐⠁⠂⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠛⠆⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠠⠁⠄⠡⢈⠚⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠠⠀⠈⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢌⠢⠁⠌⠒⡀⠌⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠀⠀⢀⠀⣄⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠠⠄⠉⠀⢀⡇⠠⡁⠠⠄⠀⣼⣿⢶⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⠁⠀⠀⠀⠀⣀⠀⠀⠈⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠒⠐⠠⣤⣄⡈⢡⠀⠀⠀⠀⢀⠀⠐⠀⠄⠀⠘⣿⣤⠈⠉⠻⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠈⢻⣤⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⢀⣴⡾⠋⠀⠀⠀⠀⠀⠀⠙⢷⡆⠂⠄⠀⠀⢂⠀⡀⠈⢰⠀⠀⠈⢻⣧⡀⠀⠈⠙⠷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⣹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠻⢷⣶⣿⢿⣆⠀⠀⢀⣤⣶⣿⣿⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣄⠀⠀⠄⠆⠠⢁⢢⠀⠀⠀⠀⠹⣷⠀⢀⠀⡀⣀⡈⠛⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠙⣷⡽⠷⠾⠟⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣷⡄⠈⠐⡀⠀⢆⠀⠀⠀⠀⣰⣿⣁⣠⣴⠟⠋⠉⠀⠀⠈⠙⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠙⠋⠀⠀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠄⠠⢑⠠⠈⢀⠀⠀⠀⢀⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣶⣶⣶⣿⣿⣿⣿⣦⣼⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡈⠐⢌⡀⢃⠀⠀⠀⣠⣾⠟⢣⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣂⠀⠠⡈⠄⢂⠀⣿⡿⠉⠐⢂⠐⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠠⠀⠀⠀⠀⠀⠀⠈⢻⣇⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠰⣦⡸⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⠡⠐⠀⠂⣼⣿⠃⠀⠀⠈⢶⣄⠂⠀⠀⠀⢀⡠⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣤⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣥⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠈⠻⢷⣬⠉⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⠛⠁⠀⢱⠂⢀⠀⣿⡇⠀⠀⠀⠀⠈⢹⣧⠀⢴⣾⡯⠄⡐⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠂⢀⠐⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢀⣿⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠈⢻⣧⠀⠀⠙⢷⣆⠀⠀⠀⠀⠀⠀⢀⣿⡿⣁⠆⠀⠈⡄⢁⠂⡐⣿⡃⠀⠀⠀⠀⠀⠀⣿⣤⡿⠟⠀⠀⠀⢈⠐⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣦⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⢸⣟⠀⠀⢸⣿⣇⠙⣾⣿⣿⣿⠿⡻⢿⠻⣟⠻⠩⢍⠣⡉⠆⡜⢨⢛⣿⣿⣿⣿⣿⠀⠀⠀⠀⠸⠻⢷⣶⣤⣞⣿⣆⠀⣀⣀⣤⣶⠿⠛⠉⠁⠀⠀⠘⡰⢀⠂⡐⣿⠅⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠂⠄⠀⠃⠄⠂⠀⠀⠀⠀⠀⠄⡀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢸⣿⣷⣾⣿⠏⡶⣩⠳⣕⢪⢱⢊⠖⡩⢄⠣⡑⠌⠰⡁⢎⡜⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⢩⣿⣿⣿⣿⣤⣀⣂⠢⢀⠀⠀⠰⣁⠂⡐⠀⡿⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⣼⠁⠀⠀⢸⣿⣿⣿⣯⢞⣱⢣⡛⣬⢣⠏⣮⠘⣅⠪⠔⢣⠈⠆⡘⠤⣊⣽⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠠⠀⠀⢿⣿⠟⠁⠀⠈⠉⠛⢿⣷⡄⠂⡀⠐⠄⡃⠠⠁⠇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⢘⣿⣆⠀⠀⠀⠀⣷⠀⠀⠀⠸⣿⣿⣿⣿⡚⣶⣧⣟⣶⣍⡞⣤⢫⣴⣇⣾⣤⣇⣒⣡⠒⡡⢞⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⡄⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⠡⢈⠐⡁⠌⠰⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠂⠁⠐⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⢹⣷⡀⠀⠀⠀⣸⡿⠹⣷⣄⠀⠀⣿⠀⠀⠀⠀⠹⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣧⠛⠻⢿⣿⣿⣿⣻⣿⠿⠷⣎⣿⣿⠏⠀⠀⠀⠀⠀⣶⣶⠟⠋⠁⣀⠘⢿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢿⣦⢀⠂⡐⢈⠰⠁⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣷⡀⣠⣾⡟⠁⠀⠘⢿⣦⡀⠀⠀⠀⠀⠀⣰⡟⠙⢿⣿⡿⣿⢿⡟⣿⣿⣿⡍⢆⢣⡙⠿⣛⠛⠿⡉⠖⣿⣿⣿⣷⣄⠀⠀⢀⣼⡿⢁⣀⡤⠀⠙⢿⣦⣍⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⣧⠂⠐⡀⠊⢀⣠⣴⣿⡟⢱⣶⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢀⣠⣶⠾⠛⠋⠁⠉⠻⣿⣿⠃⠀⠀⠀⠘⠻⢷⣄⠀⠀⠀⠀⣿⣷⡂⢄⣩⣿⡜⢧⣻⢭⡻⣿⡗⡌⢦⢱⣒⣬⣘⣴⣑⣊⡴⢉⣧⣼⣿⣠⣴⠿⠋⠀⠋⢉⠀⠀⠀⠀⠙⢿⣆⠸⣷⡀⠀⠀⠀⠀⣰⣿⠃⡘⠄⠠⠁⢌⣽⣿⠋⠀⠀⠿⠿⣦⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⢀⣶⣿⡿⠁⠀⠀⡀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠐⡘⢿⣷⡐⢺⣿⡝⣧⢿⣻⣿⣿⣶⣿⣆⣿⣟⣛⣛⣛⠛⣿⣿⣿⣿⣿⣿⡟⣁⣤⣆⠁⠀⠈⠀⠀⠀⠀⠀⠈⢿⣦⠹⣿⣄⠀⠀⣼⡿⢃⠠⠉⠂⠡⢸⣿⠛⠁⠀⠀⠀⠀⣶⣩⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣼⣾⠟⠁⠀⠀⠀⠁⠀⠁⠠⠘⣿⣇⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠈⣿⣧⠩⣿⡟⣼⢫⡟⣿⢟⣍⠣⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⠁⠉⠈⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠸⣿⣦⡙⢿⣠⣾⠟⠁⠈⢶⠁⡈⠐⢸⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠂⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⠀⢀⠠⠀⣌⣴⡿⠟⠁⠀⠀⠀⠀⠀⠌⠀⠄⣧⡀⠘⢿⣖⠋⠁⠈⠁⠀⢻⣧⠀⠈⠸⣆⠀⡠⠙⢿⣧⣻⣿⡼⣷⣿⣿⣯⣾⣷⣼⣿⣿⣯⣿⢿⣿⣻⡿⠛⠵⡉⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣲⣿⡿⡀⠄⠀⠸⢁⠠⠁⢺⣿⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠠⣄⠀⠀⠀⠀⠈⠐⡀⢂⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⢀⢀⠉⠀⡈⠄⢂⠼⠙⠁⠀⠀⠀⠀⠀⠀⠀⣾⣤⡆⠀⠹⣷⡀⠘⢿⣆⠀⠀⠀⠀⢸⣷⠀⠀⠀⣿⣾⡇⠀⠀⢻⣿⣿⣏⣟⡻⢯⣟⣯⣝⣻⣿⣿⣿⣿⣿⣿⡏⠀⠀⢀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⡟⠀⠈⢿⣦⡅⢢⠐⠈⢸⣿⡁⠀⠀⠀⠀⣼⣿⠡⠀⠀⠀⣖⣿⡄⠀⠀⠀⠀⠀⠘⠄⢂⡔⠀⢀⠀⠀⢀⡀⠀
		⠈⠀⠀⡄⠑⠈⠐⠈⠀⠈⠐⠀⢄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣅⠀⠚⣿⡆⠀⠀⠀⢸⡷⠀⠀⠀⠂⣿⡇⠀⠀⠀⣿⣟⢿⣾⡝⣯⣛⡛⢿⣻⣿⣿⣿⣿⣿⣿⡗⠀⡈⠄⠡⢈⠙⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡟⠹⠃⠀⠀⠀⣻⡿⠀⠠⢁⠸⣿⠆⠀⠀⠀⣠⣿⠃⠤⠁⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⡀⠀⠀⠀⠀⠀
		⢠⣌⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠙⣿⡄⠂⢹⣿⠀⠀⠀⢸⣟⠀⠀⡼⠁⢸⣿⠀⠀⠀⢻⣿⣷⡿⣟⣾⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⡀⢠⡌⠐⡀⢂⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⢁⠠⠘⣀⠀⠀⣠⣿⡗⠈⡐⠠⢸⣿⡀⠀⠀⢠⣿⠏⡀⢰⡀⠀⠀⠘⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠈⠐⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠄⡀⠀⠀⠀⠀⠀⠀⠀⣸⡟⣿⠇⠀⠀⠀⠀⣿⡗⠀⠈⣿⣇⠀⠀⢸⣯⠀⠀⠀⠀⢻⢏⣀⡀⠀⣸⣿⣿⡿⣭⢿⣿⣿⣿⢏⣿⣿⣿⣿⣿⣿⣿⣿⢿⣷⣄⠐⠀⢂⠀⠻⣧⡀⠀⠀⠀⠀⣰⣿⠟⠀⡐⠠⢀⠃⠀⠀⠀⣸⡿⠀⡁⠄⠂⠄⣿⠃⠀⠀⣾⡟⠀⡐⡘⠀⠀⠀⠀⠹⣏⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢂⠐⡈⢥⠀⠀⠀⠀⠀⠀⣿⢹⡟⠀⠀⠀⢀⣼⡿⢇⠀⠀⣿⣿⡀⠀⢸⣿⠀⠀⠄⣡⠚⢀⣿⣷⠂⣿⣿⣿⣳⣭⡟⣾⡽⣓⢎⠴⣈⣻⣿⣿⣯⣽⣿⠀⣿⣿⣿⣤⣀⠈⠀⠈⢁⢀⠀⣠⣾⠏⠁⠐⠂⠠⠁⠆⡐⠀⠀⣴⠟⠁⢀⠒⠈⠄⢈⣿⠀⠀⣼⣟⠂⠡⢀⠸⠀⠀⠀⠀⠀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⢂⡐⢈⠃⠀⠀⠀⠀⣰⣿⢭⠁⠀⠀⢀⣿⠏⠀⠉⠀⠀⢸⣿⣷⠀⢹⣿⡆⣬⣼⣿⣿⣿⣿⣿⠠⣿⣿⣿⣳⢮⣽⣳⢯⡝⣎⢷⣿⠟⡉⢋⣹⣾⡿⠀⢻⣿⣿⣿⣿⣿⣶⣦⣦⣌⠘⠛⠋⡀⠀⠀⠀⢀⠈⡐⠠⢁⠘⡀⠀⠀⢆⠘⡀⠈⡄⢫⠀⢠⣿⡟⠀⠀⣲⠈⠳⢤⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠒⠠⠌⠁⠢⢀⠂⢤⣤⡀⠀⣿⣯⡟⠀⢀⣴⣿⡏⠀⠀⠳⣶⠀⠀⠹⣿⣧⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣰⣿⣿⣿⣳⢏⡶⣯⣳⢻⣜⢻⣿⢀⠐⣸⣿⡿⠁⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣀⠀⠃⠄⠀⠁⠢⠌⠀⠀⠀⠈⡔⠀⠡⢀⠣⠀⣾⡿⠃⠀⢀⣽⡧⠐⠸⡄⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠰⠈⠄⡁⠃⠀⠀⠀⠀⠈⠄⠙⣷⣾⠿⢧⠀⣴⣿⣿⠟⠀⠀⠀⠀⣀⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡷⠈⢿⣿⣏⣷⣳⣭⠷⣎⢿⣿⠀⠀⣾⡟⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⠐⠨⣷⡀⠀⠀⠘⢀⠃⠄⢠⠐⡉⠄⡀⣠⣿⡿⠀⠈⢧⣙⠀⠀⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢠⠂⡉⢄⠠⢀⠌⢁⡘⡰⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠄⡀⠂⣠⣿⣿⠏⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼⣷⠀⠈⠻⣿⣶⠱⡞⡽⢮⣿⣿⣦⣶⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡙⠦⡖⠁⣀⠃⠌⢂⠱⢀⠂⣴⣿⠏⠀⠀⠀⠀⠘⠣⠐⡀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⡈⠐⠠⠌⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢮⣄⣐⣰⣿⠟⠋⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢾⣿⡄⠀⠀⠙⢿⣷⣼⣵⣿⣿⡿⣿⣿⡿⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠁⠀⢠⠊⠔⡈⠐⣌⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠡⡐⠀⠀⠀⠁⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⣀⢀⠌⡁⢃⡀⢀⡀⣀⡀⣀⡀⢀⢀⣀⢀⡀⢀⢀⣻⣿⣿⠃⠀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣬⣉⠄⡀⠀⣀⣀⣹⣿⣿⠟⠉⠀⢾⣿⡇⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠢⠌⡐⠠⣡⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢈⠂⠅⢂⠠⠁⠀⠀⠀⠀⠈⠀⠀⠀⠈⠈⠛⢻⣿⡿⠃⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⣿⣿⣅⢀⡚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠰⢀⠒⡙⠀⠀⠀⠐⠐⠒⠒⠖⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀
		⠀⠀⢀⠃⡐⠀⠆⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⣼⣿⠁⠀⠀⢠⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣛⣿⣿⣿⣿⡿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⢃⠂⠄⡘⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡔⠠⢁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⠀⠠⠑⡂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣛⡛⢿⡿⠿⢿⣿⣿⣷⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠬⡐⠠⢀⠂⠙⠿⣦⡀⠀⠀⠀⠀⠀⢀⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠱⡈⠄⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠁⢀⡁⠐⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⡻⠟⡿⠿⣿⣿⣷⣾⣿⣷⣬⣽⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠰⡁⢂⠠⠁⡄⠘⣧⡀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢢⠡⡈⠄⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡷⠀⠠⡀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⢿⣷⣶⣶⣬⣿⣿⣏⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠰⢁⠀⠀⠘⡤⠈⠙⢦⡀⣰⡿⢋⡔⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢢⠑⡀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠐⡁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣷⣶⣾⣤⣭⣭⣛⣻⣿⡿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠠⠈⠄⠀⠀⠀⠳⣌⡀⠀⢀⣷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢆⠣⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠰⣿⡅⠐⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⡵⣬⣟⡾⣷⣾⣿⣿⣿⣽⣯⣝⣛⣛⠟⡿⢿⣿⢿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠠⠀⠃⠀⠀⠀⠀⠈⢿⣦⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⡈⢄⠢⠁⡀⠀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣾⣿⣷⣿⣽⣾⣽⣷⣿⣿⣿⣿⣛⣛⡿⠿⣿⢿⣿⣿⣿⣿⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠄⠁⠀⠀⠀⠀⠀⢈⠟⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠰⡈⠅⠄⠉⠁⠈⠀⠁⠉⠁⠀⠁⠈⠀⠈⠉⣿⡧⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣛⣟⡻⣟⢻⡛⡟⢻⢿⣿⣿⣿⣿⣿⠿⣿⣷⣶⣿⣾⣽⣿⣞⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠂⠀⠀⠀⡠⠐⠠⢀⠀⠳⠀⠀⠀⠀⠀⡁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡱⢈⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⠂⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⡷⣾⣜⣳⣽⣮⣷⣽⣦⣎⣴⣋⢿⣿⣿⣷⣶⣯⣿⣿⣿⣿⣿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⡄⠀⠀⠘⢀⢁⡚⠀⠠⢂⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢂⠡⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⠆⠠⢈⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣝⡳⣎⠿⣍⢯⣙⡟⡻⢿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠠⢀⠂⠄⠂⠀⠀⠀⠈⠀⡀⠀⠄⡀⢀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⡌⢂⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠂⠁⡆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⣜⡳⣭⣻⠾⣷⢛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠁⢀⠈⠀⠀⠀⠀⠀⠀⡐⣀⠒⠠⢁⠢⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠘⢠⠃⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡷⠀⡱⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣫⢷⣳⣭⣷⣮⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⡁⢆⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⢈⠰⠈⡄⠀⠀⡀⠄⠠⠀⠀⢀⠀⢀⠀⠀⡀⠚⡁⠴⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⡀⠀⡀⠀⠀⠀⢀⠀⡐⢨⠐⠄⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
		⠀⠄⠨⡑⠀⠁⡐⠀⠌⡀⠀⠀⠀⠤⠀⠄⡠⠀⡀⠰⡠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠡⠀⢀⠀⠄⠀⠀⠀⠀⠂⠄⣁⢈⡐⠀⠀⠈⠀⠀⠁⠈⢠⠁⠀⡀
		⠀⠌⢂⠡⠂⠄⠀⠐⠠⢀⠀⠀⠉⠄⡈⠐⠠⠁⠄⡑⠡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠄⡀⠂⠄⠂⠀⠐⡀⠀⠌⠀⡀⠆⡀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀
		⠀⠌⡠⢡⠁⠄⠂⡐⠠⢀⠂⠀⠀⠒⠠⠐⠠⠌⠀⠄⡁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠀⠀⠀⠀⠁⠀⠄⠀⠀⡀⠁⠐⡀⠄⡀⠀⠁⠀⠀⠀⠀⠈⢀⠀⠀⠐⠀
		⠀⢂⠑⡠⢈⠀⠀⠄⢁⠀⠀⠡⠐⠈⠡⢀⡁⠆⠈⠠⢀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠄⠈⠀⠠⠁⠀⢈⠀⠄⡐⠀⠁⠀⠀⠀⠀⠀⢈⠀⢈⠀⠠⠀
		⠀⠄⢂⠐⡄⢂⠡⡐⢄⠊⠠⢁⠆⠡⠐⠠⢐⠠⡁⠂⠄⡈⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠂⠀⠀⠀⠀⠁⠀⢀⠈⠀⡀⠌⠐⠀⠀⠀⠀⠀⠀⠈⠠⠀⠀⠀
		⠠⠌⢠⠡⠘⡀⢂⠡⢊⠐⣁⠊⢀⠃⠜⡐⢂⠑⣈⠒⠠⠈⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⡐⠠⠐⠀⡀⠠⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀
		⠐⡈⠄⡡⢂⠐⡀⢁⠂⠱⠀⠆⠢⠌⢂⠐⠠⠒⡀⠌⡡⠌⠐⡈⠙⠻⠿⠿⢿⣿⣿⣿⣿⠿⠿⠛⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣿⣦⣤⡄⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠀⠀⠄⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠀⡐⠈⡄⢂⠆⠱⠈⡌⢡⠊⡄⠑⠤⡈⢄⠠⠃⠤⢁⠒⡌⢄⡐⠠⡐⠀⠄⡀⢀⠀⡀⠀⡀⠄⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣻⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠠⢀⠱⠠⠌⢂⡁⠒⡈⢆⠡⠄⠩⡐⢡⠂⡘⠤⡁⠂⡜⠐⠢⠜⡑⢂⡙⠤⠘⢠⠀⡱⠃⡀⠐⠈⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣟⣾⣵⣻⣜⣷⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀
		⢀⠂⠔⡡⢈⠄⢢⠑⡈⢄⠂⡘⠄⡡⢂⡑⢨⠀⡱⢈⠄⢈⠐⠠⠄⡁⠀⠀⠀⠀⡀⠄⠁⠀⠈⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⡿⢿⢛⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣟⣿⣾⡟⡿⣿⣿⡿⢟⠫⢿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠂⠜⡠⢂⢅⡊⢄⠦⡑⡈⢆⠑⠤⠁⢂⠈⠰⡈⠄⡃⢀⠂⠈⠐⠠⠀⠄⠁⠠⢀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡛⢭⢋⠏⡭⢓⠦⡙⢦⠹⣜⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⢿⣯⡷⣿⣾⣱⡷⣾⣿⣾⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠈⠄⡁⠣⢈⠘⣊⠰⢡⠙⠈⠎⠘⠠⠁⠌⠠⠐⠀⡀⠂⠀⠀⠈⠁⠀⠀⠀⠐⡀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠳⡌⣿⡷⡉⢆⠸⠰⢌⡙⢶⣉⠖⢣⢎⢯⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⢿⢿⣿⣿⡿⣽⣻⣾⡽⣷⣻⡿⣿⣷⣷⣶⣴⣾⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
		time.sleep(0.1)
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠉⠀⠀⠀⠉⠒⠁⠀⠀⠁⠁⠈⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⡀⡀⠀⠀⠀⠀⢀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠓⢤⡀⠄⠠⢀⠐⡀⢀⠀⠄⠀⠀⠀⠁⠀⠀⠀⠀⠀⠉⠁⠈⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⢂⠠⠀⡌⠡⠃⠌⠑⠂⠤⠀⠔⠀⠈⠐⠂⢄⠈⠁⠀⠀⠀⠠⠀⠆⠐⠂⡄⡀⠀⠀⠀⠀⠀⠀⠈⢷⠈⡀⢂⠥⠐⠄⡊⠌⢄⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠐⠆⠐⠠⠑⠈⠐⠲⡀⢆⠄⡐⠈⠀⠀⠀⠉⠀⠑⡈⠄⠡⠌⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠄⠀⠀⠀⠀⠀⠈⠒⠠⠐⠡⢄⣀⡀⠀⠀⠀⢨⠐⡀⠢⠄⢃⡀⠐⠨⢀⠒⠠⡀⢄⡠⢖⠸⠁⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠂⠀⠀⠀⠀⠉⡀⠌⢂⠀⠁⠐⠈⠒⠜⡰⢬⠄⠀⠀⢈⠓⠠⢈⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠐⠀⠀⠀⠀⠈⠠⢀⢤⠘⡡⠉⠌⡀⠢⠄⡱⢈⠆⡀⢀⠀⠂⠌⣐⡈⠴⡀⠞⠄⠦⢠⠄⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⡠⠐⢈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠐⠈⠠⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⢈⡐⠁⢆⡁⠆⡐⢈⡔⠌⠂⠑⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠛⠆⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠄⡁⢂⠐⡈⠐⣹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠴⠟⠁⠀⠀⠀⠀⠐⠈⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠴⣀⠂⡐⠠⢁⠀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠈⠀⣀⣤⣤⣄⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠂⠄⠠⠛⠀⢀⡆⠠⡁⠠⢈⠀⣿⡿⢷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⠟⠉⠀⠀⠀⢀⣀⡀⠀⠐⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⣀⠀⠀⠐⠲⢶⣤⣴⡈⢢⠁⠀⠀⠀⠄⠁⠀⡀⠡⠀⠙⣿⣆⡈⠙⠻⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⠁⠀⠀⠀⠀⠀⠈⠛⢷⣆⠀⠘⠻⣦⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⢀⣴⡿⠛⠀⠀⠀⠀⠀⠉⠛⢿⣎⠳⡀⠀⠀⠌⡀⠀⠀⢱⠀⠀⠈⢻⣧⡀⠀⠈⠙⠿⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠁⠀⠀⠀⠀⠀⠀⠂⣀⢀⠀⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠳⢶⣶⣽⣿⣦⠀⠀⢀⣴⣾⣿⣿⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⡀⠀⠰⡀⢁⠂⠼⠀⠀⠀⠀⠹⣷⡀⠀⡀⢀⣀⡉⠛⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠰⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣴⣦⣤⣤⣄⣀⣀⡙⢿⠶⠟⠻⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣷⡆⠀⢀⠄⢀⠣⠀⠀⠀⠀⣰⣿⣄⣠⣴⡿⠋⠉⠀⠀⠈⠙⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣽⣭⣛⠻⢿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠃⢀⠎⠠⠀⢂⠀⠀⠀⢀⣿⣿⠟⠛⠉⠀⠀⠀⠀⠀⠂⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠲⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠘⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⣾⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠤⠘⢠⠡⠀⠀⠀⣠⣾⠟⢣⡀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠳⢦⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣅⠀⠈⡔⠀⡂⠄⣿⡿⠉⠐⣇⠐⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠰⠁⠀⠀⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⠀⣁⠂⠁⠀⣼⣿⠃⠀⠀⠈⣷⣮⣆⠀⠀⠀⢠⣤⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠈⠙⢶⣤⡅⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⣰⣿⣿⢛⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⢛⡛⠿⢻⠟⣿⣿⣿⣿⣿⣿⡌⠟⠿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⠟⠉⠀⢰⠂⠀⠄⣿⡇⠀⠀⠀⠀⠈⢻⣧⠀⣶⣾⣿⠄⠠⠁⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠂⠀⠁⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⢸⣿⡟⣬⣿⣿⢿⡛⣏⠟⣭⢋⡍⣋⠆⣍⣆⠡⡜⡐⢣⠘⡔⣻⣿⣿⣿⣿⣇⣄⡀⠈⠙⣿⣆⠀⠀⠀⠀⠀⠀⢀⣿⣿⣥⠎⠀⠈⡄⠡⠈⡐⣿⡃⠀⠀⠀⠀⠀⠀⣿⣴⡿⠟⠀⠀⠀⠀⠃⠀⠀⠀⠄⠠⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣇⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⢾⡄⠀⢿⣷⣿⣿⣛⠦⡝⣼⢋⢦⠣⡜⠤⢋⡜⣉⠲⡁⠤⠁⡌⠒⡽⣿⣿⣿⣿⠋⠻⢷⣶⣦⣼⣿⣆⡀⣀⣀⣤⣶⠿⠛⠋⠉⠀⠀⢩⡑⠄⠡⠐⣿⡅⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠃⡀⠀⠣⠀⠂⠀⠀⠀⠀⠀⢀⠀⠄⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠏⠀⣰⣿⣿⣿⣿⣳⢿⡼⣙⣞⣬⣷⣌⣃⡣⢒⡤⢣⣼⣤⣵⣌⣱⣾⣿⣿⣿⡟⠀⠀⠀⠁⠈⠹⣿⣩⣿⣿⣿⣿⣤⣂⡘⠤⢄⠀⠀⠰⡍⠠⠁⠌⣿⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠻⣷⡀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣧⣯⣼⣿⣿⣿⣿⣟⣿⣿⣷⣬⣷⣿⣿⣿⣮⣗⠏⣿⣿⣿⠃⠀⠀⠀⠹⠀⠀⣿⣿⠟⠁⠀⠈⠉⠛⢿⣷⡌⠠⢀⠀⢣⠁⠌⡀⡏⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⠹⣧⡀⠀⠀⠀⠀⢘⣿⣄⠀⠀⠀⠀⣿⠀⠀⠀⠃⠀⣠⣴⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣉⠛⣿⣿⣿⡿⢉⠇⡸⢹⣿⣇⠰⣶⡀⠀⢀⣠⣴⡿⢿⡄⠀⠀⠀⠀⠀⠀⠙⣿⣦⡀⠌⠀⠎⡐⢀⠸⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠁⠊⠐⠀⠄⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⢹⣷⡀⠀⠀⠀⣸⣿⠻⣷⣄⠀⠀⣿⡄⠀⠀⠀⣾⡿⠁⠀⠀⣿⣿⠋⣽⣿⣟⢯⡳⣎⢿⣿⡗⢬⠑⡤⠩⢍⠱⡈⢆⢡⠻⠟⣻⣿⡿⣿⣶⠟⠋⢡⣀⠘⢿⣦⣀⠀⠀⠀⠀⠀⠈⠻⢿⣦⢁⠂⡐⠠⢘⡀⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣷⡀⣠⣾⡟⠁⠀⠙⣿⣦⠀⠈⠀⠀⠀⠀⢽⣇⠀⠀⣾⣿⣿⣸⡜⣿⣿⣎⠷⣭⢏⣯⡝⢢⠓⡾⢷⠪⢇⠱⣎⠢⢡⢓⣾⡿⢱⠋⣯⣀⣴⠞⠛⢿⣦⡜⠻⣿⡄⠀⠀⠀⠀⠀⠈⢿⣧⠐⠠⠁⢂⠀⣠⣴⣿⡿⢹⣶⡀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣠⣶⡾⠟⠋⠁⠉⢻⣿⣿⠃⠀⠀⠀⠘⠻⢿⣄⠀⠀⠀⠀⠘⣿⣄⠀⢹⣿⡌⢻⣷⣽⣿⣎⠿⣼⣯⣾⣿⣧⣯⣴⣁⣎⠤⠓⠤⢃⡵⣾⣿⠇⠂⣸⣿⢿⠁⠀⠀⠀⠙⢿⣆⠸⣿⡀⠀⠀⠀⠀⣰⣿⠃⡜⡀⡁⠂⢌⣽⣿⠋⠀⠈⠿⡿⣶⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣾⣿⢿⡁⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⢈⣿⠆⠀⠀⠀⠀⠘⣿⣦⠀⠹⣿⣌⢿⣷⣿⣿⣻⣿⢋⣿⣏⠛⢛⡛⣻⡿⠿⠟⣈⣷⣿⣿⣿⣤⣶⡛⠀⢹⠀⠀⠀⠀⠀⠈⢿⣦⠙⣿⣄⠀⠀⣼⡿⠃⢀⠂⠁⠄⣩⣿⠛⠁⠀⠀⠀⠀⣷⣹⣿⠋⠀⠈⠑⠂⠀⠀⠀⠀⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣼⣿⠋⠀⠀⠀⠀⠁⠌⠀⠁⠀⣿⣧⠀⠀⢀⠀⡀⠀⢸⣿⠀⠀⠀⠀⠀⠀⣿⡟⡇⠀⠿⠿⢿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⡿⣶⢁⠲⣿⣿⡿⠋⠉⠁⠀⠀⢸⠀⠀⠀⠀⠀⠀⠘⣿⣦⡙⢿⣤⣿⠟⠁⠈⢰⠈⡐⠠⢸⣿⠀⠀⠀⠀⠀⠀⠙⣿⠏⠀⠀⠀⠀⠀⠀⠠⢦⣀⠀⠌⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⠄⠀⠄⠠⠀⢌⣰⠿⠛⠁⠀⠀⠀⠀⠀⠎⠀⠰⣥⠀⠈⢿⣗⠛⠛⠛⠛⠛⢻⣗⠀⠀⠐⠀⢰⣿⠟⠛⢿⣶⡠⠀⠀⢹⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⠐⣯⠜⣸⣿⣿⡇⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣂⣿⠇⠠⠀⠀⠘⠤⠐⠠⢸⣿⡀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀⢰⣄⠀⠀⠀⠈⠑⢂⠀⢂⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⢀⠀⡄⠀⠌⠠⢁⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣧⡆⠀⠹⣷⡀⠈⢿⣆⠀⠀⠀⠀⢸⣯⠀⠀⠀⠀⣾⡇⠀⠀⠈⣿⣷⣆⠀⢸⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⢨⣿⢨⠹⣿⣿⣧⠀⣀⡀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠡⣌⡐⠠⠌⠐⠸⣿⡃⠀⠀⠀⠀⣼⡿⠐⡀⠀⠀⣮⣿⡄⠀⠀⠀⠀⠀⠘⠄⢂⡐⠀⠄⠀⠀⢀⠀⠀
		⠈⠀⠀⡄⠑⠈⠐⠈⠀⠀⠡⠂⣀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠀⠀⠀⣹⡄⠐⠸⣿⡆⠀⠀⠀⢸⡷⠀⠀⠀⠂⢹⡇⠀⠀⠀⣻⣷⣸⠀⢸⣿⣽⣿⣿⡞⣿⣿⣿⣿⣿⣿⢰⡟⢢⢃⣿⣿⣿⡆⢻⣷⣦⣄⡘⠀⠀⠀⠀⠀⣀⣀⣤⣾⠿⠙⠀⠀⠀⠀⣹⣇⠀⢂⠡⢘⣿⡇⠀⠀⠀⣰⣿⠃⡐⠀⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠁⠂⢀⠀⠀⡀⠀⠀
		⢠⡔⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠀⠀⠀⠙⣿⡄⠀⢹⣿⠀⠀⠀⢺⣟⠀⠀⣬⠁⠸⡇⠀⠀⠀⠻⣿⣼⠂⢸⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣼⡏⢆⢃⢻⣿⢹⣿⣴⣿⡙⠿⣿⣦⣄⣀⠀⣀⡙⠟⠉⠠⠀⠜⡀⠀⠀⣠⣿⠁⢈⠠⠀⢬⣿⡀⠀⠀⢠⣿⠏⢀⠰⠀⠀⠀⠘⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠈⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⠠⢀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠇⠀⠀⠀⠀⣼⡟⠀⠀⣿⣧⠀⠀⢸⣯⠀⠀⠀⠀⡉⢃⠀⠀⢀⣠⣾⣿⣿⢋⣽⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⠏⡜⡌⣾⣿⠀⢿⣿⣿⣿⣷⣬⣍⣛⡻⢿⣿⣷⣶⣬⣤⣁⣂⠀⠀⠀⠀⠁⡀⠣⢀⠃⢰⣿⠁⠀⢀⣾⡟⠀⠂⡜⠁⠀⠀⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠁⠌⣡⠀⠀⠀⠀⠀⠀⣻⣻⣿⠀⠀⠀⣀⣴⡿⢇⠀⠀⣿⣿⡄⠀⢸⣟⠀⠀⠄⡁⢚⣘⣶⣾⣿⣿⣿⣿⣼⡃⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣋⠞⣰⣼⣿⠏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣍⣉⡛⠻⢿⢿⣿⣶⣶⣶⠀⡀⢁⠂⠄⢸⣿⠀⠀⣼⡟⠠⠈⠄⢹⡄⠀⠀⠀⠈⢿⡹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⡐⢂⠰⠀⠀⠀⠀⠀⣴⣿⣿⠇⠀⠀⢰⣿⠏⠀⢎⠀⠀⢸⣿⣷⠀⠺⢿⠆⣬⣶⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⡇⢻⣿⡝⢿⣿⣿⡿⠟⠡⣿⡷⡱⢎⣿⣿⠋⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣎⡝⡛⡛⠿⣿⣷⣶⣬⣔⠿⠀⢠⣿⠃⠀⠀⢺⡘⠿⣦⡀⠀⠀⠘⣼⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠆⢠⠘⠁⠢⠐⡀⢢⣤⡀⠀⣿⣿⠏⠀⣀⣴⣿⣿⠎⠀⠺⣷⣄⠀⠙⣟⣧⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠻⣿⣌⠛⣿⡇⠐⡀⢻⣷⣽⣿⡿⠁⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⣤⣃⠛⡿⢻⣿⣷⠀⢸⠃⠀⠀⠀⣽⡇⠀⢻⣇⠀⠀⠀⢟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⠀⠀⠀⠀⠀⠀⠠⠈⠄⡘⠀⠀⠀⠀⠁⠐⠀⠹⣷⣾⣿⠇⢀⣴⣿⣿⣿⠋⠀⠀⠀⢙⣛⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣆⠀⠀⠙⢿⣷⣿⠇⠁⠀⣻⣿⣿⠋⠀⠀⠀⠀⢀⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣉⢾⣿⡆⠈⠆⡀⢠⣿⡟⠀⠑⢮⣿⡆⠀⠀⢈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢠⠌⠑⡄⢀⠠⠘⡀⠱⡈⠀⠀⠀⠀⠀⠀⠀⢈⡔⠀⠉⠀⡀⠠⣿⣽⣿⠁⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣷⠀⠀⠀⠙⢿⣄⡀⣠⣿⠟⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠚⣿⣧⠀⠂⢴⣿⠋⠀⠀⠀⠀⠹⣿⣐⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠂⠌⡀⢂⠅⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⣅⠂⣤⣿⠿⠋⠁⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣿⣦⣦⣤⣦⣦⣟⣿⣿⣿⡟⠀⠄⠠⠀⢠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢿⣿⠀⣼⡿⠃⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠠⡄⠀⠀⠀⠀⠀⠀⠀⠄⠀
		⠀⣀⢀⡘⠀⠆⣀⢀⢀⡀⣀⣀⢀⡀⢀⡀⣀⣀⣀⣨⣿⣼⣿⣷⣤⣄⣠⣄⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⡘⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠀⠎⠡⢈⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠛⢿⣿⠻⣿⣆⠀⠀⠈⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣾⣵⣭⣬⣭⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⣿⡗⠒⠲⠳⠶⠚⠷⠶⠖⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⡔⠠⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡯⠀⢈⣿⣷⣤⡀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣻⣿⣿⣉⣍⣛⣽⡻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠌⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠈⠔⣈⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡅⠀⠂⣧⣹⢿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⢛⠿⣻⢿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡣⢌⣟⠀⠛⢶⠀⠀⠀⠀⠀⠀⢀⣶⡟⠉⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⢡⠂⠄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⠁⠀⠂⠙⣿⣎⢿⣤⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠿⣿⣿⡿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣉⢾⡀⠀⢸⣦⡀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⢸⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠤⣃⠈⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⢀⠃⠀⠈⢿⣦⣍⡁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣾⣿⣽⣮⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠢⣹⡇⠀⢠⣛⠻⣆⠀⣰⡿⠋⡀⠀⠀⠀⠀⠘⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠣⢄⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⢀⠃⠀⠀⠈⠙⢿⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣶⣿⣿⣧⣯⣽⣯⣟⣿⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⠸⣷⠀⠀⠹⣧⣀⠂⣠⣷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⠳⡈⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣽⣿⣿⣛⣿⣻⣟⡿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠡⢿⡆⠀⠀⠙⢿⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⡈⢅⠢⠁⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠁⢀⠀⠀⠀⠀⠀⣼⡿⢹⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⢿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡑⢎⡇⠀⠀⠀⢸⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠈⠰⡈⢆⠀⠉⠉⠈⠁⠈⠉⠁⠈⠀⠁⠁⠈⠁⠀⠰⠀⠀⠀⠀⠰⠞⠉⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣶⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢎⠴⠀⠀⠠⢀⠀⠘⠿⣆⡀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡱⠐⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠠⠁⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣽⣯⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠲⣸⠀⠀⠡⠂⠈⠠⢄⠀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠀⡡⢉⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⢠⣾⡿⢻⣿⣿⣿⠿⣏⣟⡯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡡⢲⡀⠀⠐⠀⠀⠀⠀⠂⠀⠀⠀⡀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠠⡑⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠟⠀⢰⣿⠇⣴⣿⣿⣻⣭⣟⣾⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣻⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⡑⣧⠀⠀⠀⠀⠀⠀⠀⡐⢀⠂⠄⠡⢂⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⡡⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠈⠀⠀⣿⣿⣿⣿⡳⢧⣛⠾⣽⣛⠿⣽⣚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣹⣇⠀⠀⠀⠀⠀⠀⠁⠀⢈⠄⡃⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⠀⠐⢠⠃⠄⠀⠠⠀⠄⠠⠀⠀⢀⠀⢀⠀⠀⠠⠀⠄⡀⠀⠀⠀⠀⠀⢰⣿⣿⣿⢷⡹⣏⢾⣙⠦⣏⠿⣶⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣾⣭⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⡇⠀⢀⠠⠀⠀⠀⢀⠀⡐⢠⠂⠅⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
		⠀⠌⡐⠌⡘⠀⡁⠂⠈⡀⠀⠀⢀⠠⠀⠤⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⣎⡷⣝⣮⡝⡞⣜⡻⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣟⣻⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢀⠂⠀⠀⠄⠈⠐⠀⡁⠌⡠⠀⠀⠀⠀⠁⠈⠀⢡⠈⠀⠀
		⠀⢂⠰⠁⡄⠂⠀⠀⠡⢀⠁⠀⠂⠄⡁⢂⠁⠂⠈⡄⠀⠀⠀⠀⠀⠠⣿⣿⣿⡿⣽⣹⢞⡶⣹⡜⡲⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⡀⠂⢀⠀⠌⠀⡀⠃⠄⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠁
		⠀⠂⡄⠣⡐⠠⢀⠂⢁⠂⠄⠀⠀⢂⡐⠠⠀⠀⠠⠄⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣷⣻⢮⣗⢧⣻⣱⢻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣯⣿⣽⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠐⠀⠄⡀⠀⠀⡀⠐⠀⡐⠀⠂⠀⠌⠀⠀⠀⠀⠈⢀⠀⠄⠐⠀
		⠀⠡⢈⡁⠄⡀⠂⠠⠀⠠⠈⡐⠀⠀⠌⡰⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣿⣿⣞⣧⢷⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⡀⠀⠠⠁⠀⠐⠀⠄⡈⠀⡁⠀⠀⠀⠀⠀⢈⠀⢈⠀⠀⡀
		⠀⠂⡄⠰⣀⠐⡌⡀⠆⡁⠆⡰⢈⡐⠠⣀⠃⠄⠀⠡⠀⠀⠀⠀⠀⠀⠰⠈⣿⣿⣿⣿⣿⣞⣾⣻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣽⡻⣟⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠁⠀⠀⠀⠡⠀⢈⠐⠀⠄⡁⠠⠀⠀⠀⠀⠀⠀⠈⠀⠄⠀⠀
		⠠⡁⢄⠡⢂⠁⠢⢁⠎⡐⠌⠠⢁⡐⠡⡐⠈⠆⡁⠈⡀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣽⣳⡟⡽⣞⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠄⡐⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀
		⠐⠠⢈⠂⠌⡀⠅⢂⠐⠤⡉⢄⠣⢀⠃⢄⠡⢒⠀⡑⠠⠀⠄⠀⠀⠄⡀⠀⠀⠈⠉⠻⢿⣿⢿⣿⣿⡿⣟⠋⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣞⡷⣯⢽⡾⣽⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠐⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
		⠠⢁⠂⢌⠰⠁⠎⡐⢈⠆⡱⢈⠐⡄⢊⠤⡀⠎⡐⢀⠆⡡⠀⡄⢠⠀⡐⠤⢁⠂⠠⠉⠚⠿⠿⠿⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢿⣽⣻⢾⣽⣿⣿⠋⢄⡡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀
		⠐⠠⢈⠄⢢⠉⡰⢀⠣⠘⡐⢄⠊⡔⢡⠒⣈⠒⣈⠀⠎⡐⡐⡈⢄⠢⢁⠢⠐⡌⠀⣌⠐⠠⠐⠀⠁⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢟⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⡾⣽⢯⣿⡿⡁⠎⠠⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀
		⡈⠄⡡⠊⢄⢂⡁⠆⡠⠑⡈⢄⠂⢌⠂⠥⣀⠣⡐⢌⠐⠠⢁⠐⠠⠈⢀⠀⠁⠀⠠⢀⠀⠀⠌⠂⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣫⠙⡩⠜⣠⠃⢆⠎⡔⢫⡜⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡑⢌⠢⣹⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢌⠒⡠⢑⡨⠄⣌⠰⣠⢡⡙⢄⡘⠤⠉⡔⠠⢂⠁⠎⠀⠀⠂⢈⠒⠀⡀⠀⠠⢀⠡⠀⠀⠀⢈⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⢄⠣⡑⢎⠤⣋⡜⡸⢌⡣⢜⣣⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢂⡍⠒⠤⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀⢂⠁⠣⠘⡈⠎⡑⢂⠁⠙⢂⠉⢀⠃⠄⡁⠂⢀⠈⢀⠁⠀⠀⠌⠀⠀⠀⠀⠄⠀⣀⠀⢀⠠⢀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⡌⢒⡉⠲⡌⢒⠬⡑⢎⡔⢫⡜⣣⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡎⡅⢒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
	type_text("LOL YOU JUST GOT RICKROLLED")
	return
def luge():
	type_text("work in progress")
def stat_len_mod(size,data):
	length=len(size)-len(str(data))
	out=str(data)
	for x in range(0,length):
		out=out+"_"
	return out
def pp():
	print(f"""
        ,),,)
      {chr(92)}'     ',)
     ,`  ,--.  ',  ,                        /------._,------{chr(92)}
     :  /    {chr(125)}  G{chr(125)}'   DUNGEONS & DRAGONS   [ PLAYER NAME: {stat_len_mod("",player_name)} ]
    ',  {chr(92)}    ',,V     5E CHARACTER SHEET   [        RACE: {stat_len_mod("",race)} ]
    _{chr(92)}_{chr(92)};;l  [  BACKGROUND: {stat_len_mod("",backround)} ]
  _/          ';/  CHARACTER NAME       {chr(92)}{chr(92)} [   ALIGNMENT: {stat_len_mod("",alingment)} ]
 //| {stat_len_mod("",dndname)}  {chr(92)}{chr(92)}[ CLASS: {stat_len_mod("",classs)} LEVEL: {stat_len_mod("",level)} ]
// ;                       ,---.      ,  //[ EXPERIENCE POINTS: {stat_len_mod("",xp)} ]
{chr(92)}{chr(92)} {chr(92)}/  _  {chr(92)}_,'/_//  {chr(92)},-------------------./ 
 {chr(92)}{chr(92)}_'/            VZ{chr(92)}  `'  /  {chr(92)}  `.' /  
/------{chr(92)}         +FAR`.,'    `.,'       _.._    .------------. .-----------.
| STR: |  .--------------------------.    _/    {chr(92)}_  |/          {chr(92)}| |/         {chr(92)}|
[  {stat_len_mod("","+"+str(strengthmod))}  ] {chr(123)}   {stat_len_mod("",insperation)}   INSPIRATION         {chr(125)}  )   AC   ( | INITIATIVE | |   SPEED   |
[ ({stat_len_mod("",strength)}) ] {chr(123)}   {stat_len_mod("",profishansy)}   PROFICIENCY BONUS   {chr(125)}  |   {stat_len_mod("",ac)}   | |    {stat_len_mod("",initative)}    | |   {stat_len_mod("",speed)} ft   |
{chr(92)}{chr(92)}<''>// {chr(123)}                            {chr(125)}   {chr(92)}      /  |{chr(92)}          /| |{chr(92)}         /|
/------{chr(92)}  '--------------------------'     `-.,-`   '------------' '-----------'
| DEX: |  .--------------------------.    .-----------------------------------.
[  {stat_len_mod("","+"+str(dexmod))}  ] {chr(123)}       SAVING  THROWS       {chr(125)}  {chr(123)} HIT POINTS:  [**********]  {stat_len_mod("",chp)} / {stat_len_mod("",hp)}  {chr(125)}
[ ({stat_len_mod("",dex)}) ] {chr(123)} {stat_len_mod("_",(strengthmod+profishansy))} STR {stat_len_mod("",strength)}  .:/{chr(92)}:.  {stat_len_mod("",intelegance)} INT {stat_len_mod("_",(intelegancemod+profishansy))} {chr(125)}  {chr(123)} TEMP HIT POINTS:{stat_len_mod("                    ",temphp)}{chr(125)}
{chr(92)}~:><:~/ | {stat_len_mod("_",(dexmod+profishansy))} DEX {stat_len_mod("",dex)} :{chr(92)}/20{chr(92)}/: {stat_len_mod("",wis)} WIS {stat_len_mod("_",(wismod+profishansy))} |   '-----------------------------------'
/------{chr(92)} {chr(123)} {stat_len_mod("_",(conmod+profishansy))} CON {stat_len_mod("",con)} :/{chr(92)}``/{chr(92)}: {stat_len_mod("",cha)} CHA {stat_len_mod("_",(chamod+profishansy))} {chr(125)}{chr(125)}  .-------------. .---------------------.
| CON: | {chr(123)}          `._{chr(92)}/_.'          {chr(125)}  |/           {chr(92)}| |/                   {chr(92)}|
[  {stat_len_mod("","+"+str(conmod))}  ]  '--------------------------'   |  HIT DICE   | |     DEATH SAVES     |
[ ({stat_len_mod("",con)}) ]  .--------------------------.   |   {stat_len_mod("  _  ",hitdice)}   | |  < - - - + - - - >  |
{chr(92)}_{chr(92)}()/_/ {chr(123)}           SKILLS           {chr(125)}  |{chr(92)}           /| |{chr(92)} death        life /|
/------{chr(92)} {chr(123)} {stat_len_mod("_",acrobaticsprof)} Acrobatics      {stat_len_mod("",acrobatics)} (dex) {chr(125)}  '-------------' '---------------------'
| INT: | | {stat_len_mod("_",animalprof)} Animal Handling {stat_len_mod("",animal)} (wis) |   .-----------------------------------.
[  {stat_len_mod("","+"+str(intelegancemod))}  ] | {stat_len_mod("_",arcanaprof)} Arcana          {stat_len_mod("",arcana)} (int) |  {chr(123)}       ATTACKS & SPELLCASTING        {chr(125)}
[ ({stat_len_mod("",intelegance)}) ] | {stat_len_mod("_",athleticsprof)} Athletics       {stat_len_mod("",athletics)} (str) |  {chr(123)} {stat_len_mod("_",weponl1)} {chr(125)}
{chr(92)}+/{chr(125)}{chr(123)}{chr(92)}+/ | {stat_len_mod("_",deseptionprof)} Deception       {stat_len_mod("",deseption)} (cha) |  | {stat_len_mod("_",weponl2)} |
/------{chr(92)} | {stat_len_mod("_",historyprof)} History         {stat_len_mod("",history)} (int) |  | {stat_len_mod("_",weponl3)} |
| WIS: | | {stat_len_mod("_",insightprof)} Insight         {stat_len_mod("",insight)} (wis) |  | {stat_len_mod("_",weponl4)} |
[  {stat_len_mod("","+"+str(wismod))}  ] | {stat_len_mod("_",intimidationprof)} Intimidation    {stat_len_mod("",intimidation)} (cha) |  | {stat_len_mod("_",weponl5)} |
[ ({stat_len_mod("",wis)}) ] | {stat_len_mod("_",investigationprof)} Investigation   {stat_len_mod("",investigation)} (int) |  | {stat_len_mod("_",weponl6)} |
{chr(92)}+_/{chr(92)}_+/ | {stat_len_mod("_",medesenprof)} Medicine        {stat_len_mod("",medicine)} (wis) |  | {stat_len_mod("_",weponl7)} |
/------{chr(92)} | {stat_len_mod("_",natureprof)} Nature          {stat_len_mod("",nature)} (int) |  | {stat_len_mod("_",weponl8)} |
| CHA: | | {stat_len_mod("_",preseptionprof)} Perception      {stat_len_mod("",preseption)} (wis) |  | {stat_len_mod("_",weponl9)} |
[  {stat_len_mod("","+"+str(chamod))}  ] | {stat_len_mod("_",preformanceprof)} Performance     {stat_len_mod("",preformance)} (cha) |  | {stat_len_mod("_",weponl10)} |
[ ({stat_len_mod("",cha)}) ] | {stat_len_mod("_",perswasonprof)} Persuasion      {stat_len_mod("",perswason)} (cha) |  | {stat_len_mod("_",weponl11)} |
{chr(92)}"{chr(123)}--{chr(125)}"/ | {stat_len_mod("_",relegionprof)} Religion        {stat_len_mod("",relegion)} (int) |  | {stat_len_mod("_",weponl12)} |
/------{chr(92)} | {stat_len_mod("_",slightofhandprof)} Sleight of Hand {stat_len_mod("",slightofhand)} (dex) |  | {stat_len_mod("_",weponl13)} |
| PAS. | | {stat_len_mod("_",stelthprof)} Stealth         {stat_len_mod("",stelth)} (dex) |  {chr(123)} {stat_len_mod("_",weponl14)} {chr(125)}
[ WIS: ] {chr(123)} {stat_len_mod("_",servivalprof)} Survival        {stat_len_mod("",servival)} (wis) {chr(125)}  {chr(123)}                                     {chr(125)}
[  {stat_len_mod("",paswis)}  ] {chr(123)}                            {chr(125)}   '-----------------------------------'
{chr(92)}::[]::/  '--------------------------'    /------._,------{chr(92)}
+-------------------------------------+  [              APPEARANCE             ]
|   OTHER PROFICIENCIES & LANGUAGES   |  [    AGE: {stat_len_mod("_",age)} ]
| {stat_len_mod("_",profl1)} |  [ GENDER: {stat_len_mod("_",gender)} ]
| {stat_len_mod("_",profl2)} |  [ HEIGHT: {stat_len_mod("_",hight)} ]
| {stat_len_mod("_",profl3)} |  [ WEIGHT: {stat_len_mod("_",weight)} ]
| {stat_len_mod("_",profl4)} |  [   EYES: {stat_len_mod("_",eyes)} ]
| {stat_len_mod("_",profl5)} |  [   SKIN: {stat_len_mod("_",skin)} ]
| {stat_len_mod("_",profl6)} |  [   HAIR: {stat_len_mod("_",hair)} ]
+-------------------------------------+   {chr(92)},---------------------./ 
*------------------------------------------------------------------------------*
|                                                                   EQUIPMENT
| Belt Pouch:
| * {stat_len_mod("",belt_pouch)}
| Clothing:
| * {stat_len_mod("",clohting)}
| Weapons & Armor:
| * {stat_len_mod("",wepons_aromor)}
| Backpack:
| * {stat_len_mod("",backpack)}
| Strapped to backpack:
| * {stat_len_mod("",straped_to_sayd_backpack)}
| ...
*------------------------------------------------------------------------------*
|                                                                      SPELLS
| Cantrips:
| * {stat_len_mod("",camtris)}
| Level 1 ({stat_len_mod("",lv1)} slots):
| * {stat_len_mod("",lv1spells)}
| Level 2 ({stat_len_mod("",lv2)} slots):
| * {stat_len_mod("",lv2spells)}
| Level 3 ({stat_len_mod("",lv3)} slots):
| * {stat_len_mod("",lv3spells)}
| Level 4 ({stat_len_mod("",lv4)} slots):
| * {stat_len_mod("",lv4spells)}
| Level 5 ({stat_len_mod("",lv5)} slots):
| * {stat_len_mod("",lv5spells)}
| Level 6 ({stat_len_mod("",lv6)} slots):
| * {stat_len_mod("",lv6spells)}
| Level 7 ({stat_len_mod("",lv7)} slots):
| * {stat_len_mod("",lv7spells)}
| Level 8 ({stat_len_mod("",lv8)} slots):
| * {stat_len_mod("",lv8spells)}
| Level 9 ({stat_len_mod("",lv9)} slots):
| * {stat_len_mod("",lv9spells)}
*------------------------------------------------------------------------------*
|                                                           FEATURES & TRAITS
| Race ({stat_len_mod("_",race)}):
| * {stat_len_mod(" ",racetrate)}
| Subrace ({stat_len_mod("_",subrace)}):
| * {stat_len_mod(" ",subracetrate)}
| Background ({stat_len_mod("_",backround)}):
| * {stat_len_mod(" ",backroundtrate)}
| Class ({stat_len_mod("_",classs)}):
| * {stat_len_mod(" ",classtrate)}
| Level 1:
| * {stat_len_mod(" ",lv1trate)}
| Level 2
| * {stat_len_mod(" ",lv2trate)}
| Level 3
| * {stat_len_mod(" ",lv3trate)}
| Level 4
| * {stat_len_mod(" ",lv4trate)}
| Level 5
| * {stat_len_mod(" ",lv5trate)}
| Level 6
| * {stat_len_mod(" ",lv6trate)}
| Level 7
| * {stat_len_mod(" ",lv7trate)}
| Level 8
| * {stat_len_mod(" ",lv8trate)}
| Level 9
| * {stat_len_mod("  ",lv9trate)}
*------------------------------------------------------------------------------*
|                                                    PERSONAL CHARACTERISTICS
| Personality traits:
| * {stat_len_mod("  ",personalitytrate)}
| Ideals:
| * {stat_len_mod("  ",ideals)}
| Bonds:
| * {stat_len_mod("  ",bonds)}
| Flaws:
| * {stat_len_mod("  ",flaws)}
*------------------------------------------------------------------------------*
|                                                                   BACKSTORY
| * {stat_len_mod("  ",backstory)}
| 
*                                                                              *
'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
""")
globals_list = [
"age", "dndname", "player_name", "race", "backround", "alingment", "classs", "xp", "level",
"strengthmod", "strength", "insperation", "profishansy", "ac", "initative", "hp", "chp",
"speed", "dexmod", "dex", "con", "conmod", "wis", "wismod", "cha", "chamod", "intelegance",
"intelegancemod", "acrobaticsprof", "eyes", "temphp", "hitdice", "acrobatics",
"animalprof", "animal", "arcanaprof", "arcana", "athleticsprof", "athletics",
"weponl1", "weponl2", "weponl3", "weponl4", "weponl5", "weponl6", "weponl7", "weponl8",
"weponl9", "weponl10", "weponl11", "weponl12", "weponl13", "weponl14", "deseptionprof",
"deseption", "historyprof", "history", "insightprof", "insight", "intimidationprof",
"intimidation", "investigationprof", "investigation", "medesenprof", "medicine",
"nature", "natureprof", "preseptionprof", "preseption", "preformance", "preformanceprof",
"perswasonprof", "perswason", "relegionprof", "relegion", "slightofhandprof",
"slightofhand", "stelthprof", "stelth", "servivalprof", "servival", "paswis", "profl1",
"profl2", "profl3", "profl4", "profl5", "profl6", "gender", "hight", "weight", "skin", "hair",
"belt_pouch", "clohting", "wepons_aromor", "backpack", "straped_to_sayd_backpack",
"camtris", "lv1", "lv2", "lv3", "lv4", "lv5", "lv6", "lv7", "lv8", "lv9", "lv1spells", "lv2spells",
"lv3spells", "lv4spells", "lv5spells", "lv6spells", "lv7spells", "lv8spells", "lv9spells",
"racetrate", "subrace", "subracetrate", "backroundtrate", "classtrate", "lv1trate",
"lv2trate", "lv3trate", "lv4trate", "lv5trate", "lv6trate", "lv7trate", "lv8trate",
"lv9trate", "personalitytrate", "ideals", "bonds", "flaws", "backstory"]
def inportsave(longvar):
	longlist = longvar.split(",")  # Split by comma
	globals_list = [
		"age", "dndname", "player_name", "race", "backround", "alingment", "classs", "xp", "level",
		"strengthmod", "strength", "insperation", "profishansy", "ac", "initative", "hp", "chp",
		"speed", "dexmod", "dex", "con", "conmod", "wis", "wismod", "cha", "chamod", "intelegance",
		"intelegancemod", "acrobaticsprof", "eyes", "temphp", "hitdice", "acrobatics",
		"animalprof", "animal", "arcanaprof", "arcana", "athleticsprof", "athletics",
		"weponl1", "weponl2", "weponl3", "weponl4", "weponl5", "weponl6", "weponl7", "weponl8",
		"weponl9", "weponl10", "weponl11", "weponl12", "weponl13", "weponl14", "deseptionprof",
		"deseption", "historyprof", "history", "insightprof", "insight", "intimidationprof",
		"intimidation", "investigationprof", "investigation", "medesenprof", "medicine",
		"nature", "natureprof", "preseptionprof", "preseption", "preformance", "preformanceprof",
		"perswasonprof", "perswason", "relegionprof", "relegion", "slightofhandprof",
		"slightofhand", "stelthprof", "stelth", "servivalprof", "servival", "paswis", "profl1",
		"profl2", "profl3", "profl4", "profl5", "profl6", "gender", "hight", "weight", "skin", "hair",
		"belt_pouch", "clohting", "wepons_aromor", "backpack", "straped_to_sayd_backpack",
		"camtris", "lv1", "lv2", "lv3", "lv4", "lv5", "lv6", "lv7", "lv8", "lv9", "lv1spells", "lv2spells",
		"lv3spells", "lv4spells", "lv5spells", "lv6spells", "lv7spells", "lv8spells", "lv9spells",
		"racetrate", "subrace", "subracetrate", "backroundtrate", "classtrate", "lv1trate",
		"lv2trate", "lv3trate", "lv4trate", "lv5trate", "lv6trate", "lv7trate", "lv8trate",
		"lv9trate", "personalitytrate", "ideals", "bonds", "flaws", "backstory"
	]
	for i, var_name in enumerate(globals_list):
		 globals()[var_name] = longlist[i]
def exportchar():
	data = [
		age, dndname, player_name, race, backround, alingment, classs, xp, level,
		strengthmod, strength, insperation, profishansy, ac, initative, hp, chp,
		speed, dexmod, dex, con, conmod, wis, wismod, cha, chamod, intelegance,
		intelegancemod, acrobaticsprof, eyes, temphp, hitdice, acrobatics,
		animalprof, animal, arcanaprof, arcana, athleticsprof, athletics,
		weponl1, weponl2, weponl3, weponl4, weponl5, weponl6, weponl7, weponl8,
		weponl9, weponl10, weponl11, weponl12, weponl13, weponl14, deseptionprof,
		deseption, historyprof, history, insightprof, insight, intimidationprof,
		intimidation, investigationprof, investigation, medesenprof, medicine,
		nature, natureprof, preseptionprof, preseption, preformance, preformanceprof,
		perswasonprof, perswason, relegionprof, relegion, slightofhandprof,
		slightofhand, stelthprof, stelth, servivalprof, servival, paswis, profl1,
		profl2, profl3, profl4, profl5, profl6, gender, hight, weight, skin, hair,
		belt_pouch, clohting, wepons_aromor, backpack, straped_to_sayd_backpack,
		camtris, lv1, lv2, lv3, lv4, lv5, lv6, lv7, lv8, lv9, lv1spells, lv2spells,
		lv3spells, lv4spells, lv5spells, lv6spells, lv7spells, lv8spells, lv9spells,
		racetrate, subrace, subracetrate, backroundtrate, classtrate, lv1trate,
		lv2trate, lv3trate, lv4trate, lv5trate, lv6trate, lv7trate, lv8trate,
		lv9trate, personalitytrate, ideals, bonds, flaws, backstory
	]
	# Convert all to strings, join by comma
	return ",".join(map(str, data))
def dnd():
	pp()
	choice=""
	unsued=""
	choice=betinput("""1 to change
2 to inport
3 to export
4 to roll dice
5 to quit: """)
	if choice=="2":
		inportsave(betinput("input the save here: "))
	if choice=="3":
		print(exportchar())
		unsued=input()
	if choice=="4":
		typeofdice=betinput("1 for disavantage roll, 2 for normal roll, 3 for advantage roll")
		countdice=int(betinput("input the number of dice: "))
		dicetype=int( betinput("what is the highest number that can be rolled on that dice type: "))
		result=0
		for x in range(0,countdice):
			result+=random.randint(1,dicetype)
		if countdice==1 and dicetype==20 and result==20:
			for t in [1,2,3]:
				for x in confetty_animation:
					for x in range(0,99):
						print("""""")
					time.sleep(.1)
					print(x)
					type_text("YOU GOT A 20!")
		else:
			type_text(f"you got {result}")
			input()
	if choice=="5":
		return
	if choice=="1":
		print("""age
dndname
player_name
race
backround
alingment
classs 
xp
level
strengthmod
strength
insperation
profishansy
ac
initative
hp
chp
speed
dexmod
dex
con
conmod
wis
wismod
cha
chamod
intelegance
intelegancemod
acrobaticsprof
eyes
temphp
hitdice
acrobatics
animalprof
animal
arcanaprof
arcana
athleticsprof
athletics
weponl1
weponl2
weponl3
weponl4
weponl5
weponl6
weponl7
weponl8
weponl9
weponl10
weponl11
weponl12
weponl13
weponl14
deseptionprof
deseption
historyprof
history
insightprof
insight
intimidationprof
intimidation
investigationprof
investigation
medesenprof
medicine
nature
natureprof
preseptionprof
preseption
preformance
preformanceprof
perswasonprof
perswason
relegionprof
relegion
slightofhandprof
slightofhand
stelthprof
stelth
servivalprof
servival
paswis
profl1
profl2
profl3
profl4
profl5
profl6
gender
hight
weight
skin
hair
belt_pouch
clohting
wepons_aromor
backpack
straped_to_sayd_backpack
camtris
lv1
lv2
lv3
lv4
lv5
lv6
lv7
lv8
lv9
lv1spells
lv2spells
lv3spells
lv4spells
lv5spells
lv6spells
lv7spells
lv8spells
lv9spells
racetrate
subrace
subracetrate
backroundtrate
classtrate
lv1trate
lv2trate
lv3trate
lv4trate
lv5trate
lv6trate
lv7trate
lv8trate
lv9trate
personalitytrate
ideals
bonds
flaws
backstory""")
		change=input("what do you whant to change:")
		iteration=0
		if change in globals_list:
			for x in globals_list:
				if x==change:
					break
				else:
					iteration+=1
		if input(f"change {globals_list[iteration]}?(y/n):")=="n":
			type_text("ok noting is changed")
		else:
			changeto=input(f"change {globals_list[iteration]} to: ")
			if iteration==0:
				age=changeto
			if iteration==1:
				dndname=changeto
			if iteration==2:
				player_name=changeto
			if iteration==3:
				race=changeto
			if iteration==4:
				backround=changeto
			if iteration==5:
				alingment=changeto
			if iteration==6:
				classs=changeto
			if iteration==7: 
				xp=changeto
			if iteration==8:
				level=changeto
			if iteration==9:
				strengthmod=changeto
			if iteration==10:
				strength=changeto
			if iteration==11:
				insperation=changeto
			if iteration==12:
				profishansy=changeto
			if iteration==13:
				ac=changeto
			if iteration==14:
				initative=changeto
			if iteration==15:
				hp=changeto
			if iteration==16:
				chp=changeto
			if iteration==17:
				speed=changeto
			if iteration==18:
				dexmod=changeto
			if iteration==19:
				dex=changeto
			if iteration==20:
				con=changeto
			if iteration==21:
				conmod=changeto
			if iteration==22:
				wis=changeto
			if iteration==23:
				wismod=changeto
			if iteration==24:
				cha=changeto
			if iteration==25:
				chamod=changeto
			if iteration==26:
				intelegance=changeto
			if iteration==27:
				intelegancemod=changeto
			if iteration==28:
				acrobaticsprof=changeto
			if iteration==29:
				eyes=changeto
			if iteration==30:
				temphp=changeto
			if iteration==31:
				hitdice=changeto
			if iteration==32:
				acrobatics=changeto
			if iteration==33:
				animalprof=changeto
			if iteration==34:
				animal=changeto
			if iteration==35:
				arcanaprof=changeto
			if iteration==36:
				arcana=changeto
			if iteration==37:
				athleticsprof=changeto
			if iteration==38:
				athletics=changeto
			if iteration==39:
				weponl1=changeto
			if iteration==40:
				weponl2=changeto
			if iteration==41:
				weponl3=changeto
			if iteration==42:
				weponl4=changeto
			if iteration==43:
				weponl5=changeto
			if iteration==44:
				weponl6=changeto
			if iteration==45:
				weponl7=changeto
			if iteration==46:
				weponl8=changeto
			if iteration==47:
				weponl9=changeto
			if iteration==48:
				weponl10=changeto
			if iteration==49:
				weponl11=changeto
			if iteration==50:
				weponl12=changeto
			if iteration==51:
				weponl13=changeto
			if iteration==52:
				weponl14=changeto
			if iteration==53:
				deseptionprof=changeto
			if iteration==54:
				deseption=changeto
			if iteration==55:
				historyprof=changeto
			if iteration==56:
				history=changeto
			if iteration==57:
				insightprof=changeto
			if iteration==58:
				insight=changeto
			if iteration==59:
				intimidationprof=changeto
			if iteration==60:
				intimidation=changeto
			if iteration==61:
				investigationprof=changeto
			if iteration==62:
				investigation=changeto
			if iteration==63:
				medesenprof=changeto
			if iteration==64:
				medicine=changeto
			if iteration==65:
				nature=changeto
			if iteration==66:
				natureprof=changeto
			if iteration==67:
				preseptionprof=changeto
			if iteration==68:
				preseption=changeto
			if iteration==69:
				preformance=changeto
			if iteration==70:
				preformanceprof=changeto
			if iteration==71:
				perswasonprof=changeto
			if iteration==72:
				perswason=changeto
			if iteration==73:
				relegionprof=changeto
			if iteration==74:
				relegion=changeto
			if iteration==75:
				slightofhandprof=changeto
			if iteration==76:
				slightofhand=changeto
			if iteration==77:
				stelthprof=changeto
			if iteration==78:
				stelth=changeto
			if iteration==79:
				servivalprof=changeto
			if iteration==80:
				servival=changeto
			if iteration==81:
				paswis=changeto
			if iteration==82:
				profl1=changeto
			if iteration==83:
				profl2=changeto
			if iteration==84:
				profl3=changeto
			if iteration==85:
				profl4=changeto
			if iteration==86:
				profl5=changeto
			if iteration==87:
				profl6=changeto
			if iteration==88:
				gender=changeto
			if iteration==89:
				hight=changeto
			if iteration==90:
				weight=changeto
			if iteration==91:
				skin=changeto
			if iteration==92:
				hair=changeto
			if iteration==93:
				belt_pouch=changeto
			if iteration==94:
				clohting=changeto
			if iteration==95:
				wepons_aromor=changeto
			if iteration==96:
				backpack=changeto
			if iteration==97:
				straped_to_sayd_backpack=changeto
			if iteration==98:
				camtris=changeto
			if iteration==99:
				lv1=changeto
			if iteration==100:
				lv2=changeto
			if iteration==101:
				lv3=changeto
			if iteration==102:
				lv4=changeto
			if iteration==103:
				lv5=changeto
			if iteration==104:
				lv6=changeto
			if iteration==105:
				lv7=changeto
			if iteration==106:
				lv8=changeto
			if iteration==107:
				lv9=changeto
			if iteration==108:
				lv1spells=changeto
			if iteration==109:
				lv2spells=changeto
			if iteration==110:
				lv3spells=changeto
			if iteration==111:
				lv4spells=changeto
			if iteration==112:
				lv5spells=changeto
			if iteration==113:
				lv6spells=changeto
			if iteration==114:
				lv7spells=changeto
			if iteration==115:
				lv8spells=changeto
			if iteration==116:
				lv9spells=changeto
			if iteration==117:
				racetrate=changeto
			if iteration==118:
				subrace=changeto
			if iteration==119:
				subracetrate=changeto
			if iteration==120:
				backroundtrate=changeto
			if iteration==121:
				classtrate=changeto
			if iteration==122:
				lv1trate=changeto
			if iteration==123:
				lv2trate=changeto
			if iteration==124:
				lv3trate=changeto
			if iteration==125:
				lv4trate=changeto
			if iteration==126:
				lv5trate=changeto
			if iteration==127:
				lv6trate=changeto
			if iteration==128:
				lv7trate=changeto
			if iteration==129:
				lv8trate=changeto
			if iteration==130:
				lv9trate=changeto
			if iteration==131:
				personalitytrate=changeto
			if iteration==132:
				ideals=changeto
			if iteration==133:
				bonds=changeto
			if iteration==134:
				flaws=changeto
			if iteration==135:
				backstory=changeto#25,Kaelthar Emberfain,liam,Dragonborn,Soldier,Neutral Good,Ranger,0,1,2,15,0,2,16,2,13,13,30,3,16,14,2,12,1,12,1,10,0,0,Gold,0,1d10,5,1,0,3,0,2,0,2,1,15,0,0,Longbow (1d8+3 Piercing),Shortsword (1d6+3 Slashing),Dagger (1d4+3 Piercing),,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,13,Leather Armor,Explorer's Pack,Ranger's gear,,0,,,,,,,,,,,,,,,,,,Draconic Ancestry (Fire Breath),,Darkvision,Military Rank,monstrosotys,Primeval Awareness,,,,,,,,,,Brave,Always loyal to my allies,I fight for honor and freedom,My anger burns as hot as dragonfire,Kaelthar was born from an ancient draconic bloodline trained as a soldier before bonding with a drake companion. When the bond deepened his essence fused with the drake's granting him primal power and draconic might. He wanders the world seeking justice with dragonfire in his breath and the instincts of a hunter in his soul.
def hub():
	global turn
	global runhub
	global debuging
	global invertedP
	global iterationP
	global runnerP
	global var
	global hubo
	global operation
	global easterEggCount
	global maxGuessCount
	global minGuess
	global maxGuess
	global playCount
	global playAgain
	global debuging
	global typing
	global type_speed
	global player_score
	global com_score
	while True:
		type_text("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		type_text("0 to stop")
		type_text("1 for settings")
		type_text("2 for calculator")
		type_text("3 for number game")
		type_text("4 for palindrome detector")
		type_text("5 for pig latin translator")
		type_text("6 for anagram maker")
		type_text("7 for averager")
		type_text("8 for temperature calculator")
		type_text("9 for area calculator")
		type_text("10 for list maker")
		type_text("11 for tic tac toe game")
		type_text("12 for rock paper scissors")
		type_text("13 for text adventure game (made by mis larose)")
		type_text("14 THE PROGRAMER (made by liam (Note from hubby: i am scared of this program))")
		type_text("15 for rickle the pickle")
		hubo = betinput("what do you want: ")
		if check_int(hubo) == "":
			type_text("invalid input")
		else:
			hubo = int(hubo)
			if hubo == 0:
				type_text("Goodby please come back soon! ##connection terminated by:Hubby##, end sequance initiated:")
				time.sleep(4)
				print("""
		  		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		  		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-.......     ......:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-......:::--==++++===--:::....  .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@#...-=-::-+++*++++++++++++++++++++-.. :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@..-+=...=-...=++++++++++++++++++++++++-. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%.-++.+@@@@@@+.=++++++++++++++=+++++++++=. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.+*+.@@@@@@@@=-+++++++++++++++++=++=+====..@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.*++.@@@@@@@@--++++++++++++++++++++++++++:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.+++:.@@@@@@..=++++++++=++++++=++++++====:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-.**++:... ..:=+++++++++++++++++++++=+++++:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@-:*+++++++++++++++++++++++++++++=+===+====:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@      .              ..==++++++++++++++==+:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-*=+=========+==++=:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@%*#########%###################@=:=++++++++++=++++==:.@@@%%@@@@@@%@@@@@@@@@@@@@@@@
				@@@@@@@@@@@+.....:..............................-=+=++=+=+==========:.@@@*##########*#@@@@@@@@@@@@
				@@@@@@@@@...-+***++++++++++++++++++++=+++++++++++++++++++++++++++===:.@@@#@@@@@@@%%@%%##%@@@@@@@@@
				@@@@@@@..-+*+++++++++++++++++++++++++++++++++++=++==+==+====+=======:.@@@#%@@@%@@@@@@@@%##@@@@@@@@
				@@@@@@..=+++*++++++*++++++++++++++++++++++++++++++++++=+=++++=======:.@@@#%@@@%@@@@@@@@@@#%@@@@@@@
				@@@@@.:+**+++++++++++++++++++++++++++++++++=+++++====+==+===========:.@@@#%%%@%@@@@%%%%%%%#@@@@@@@
				@@@@@.+*+++++++++++++++++++++++++++++++++++++++=+++++++++=+=======++..@@@#%@@@%@@%%@@%%%@%##@@@@@@
				@@@@.:++++++++++++++++++++++++++++++++++++=========================- *@@%%@@@@%%%%%%%%%%%%%#@@@@@@
				@@@@.+++++++++++++++++++++++++++++++++++++++++++++=++++===========: .@@@%%%@@@@@%%%%@%%%@%%##@@@@@
				@@@*.*++++++++++++++++++++=++++++++++++++======+=++=+=========+=:. -@@@##%%%%%%%%%%%%%%%%%%%#@@@@@
				@@@.-++++*+*+*+*+++++++++++++++++-=-:........................    :@@@@#%%@%%@%%%%%%%@%%%%%%%#%@@@@
				@@@.=+++++++++++++++++++=++++-:.    ........................-*#@@@@@###%%%%%%%%@@%%%%%@@@%%%#%@@@@
				@@@+++++++++++++++++++++++:. .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###%%%@@@%%%%%%%%%%%%%%%%%%##@@@@@
				@@@.=+*++++++++++++++++++-. +@@@@@@%#%%%%%%%%%%##############*####%%%%%%%%%%%%%%%%%@@%%%%%%%##@@@@
				@@@.:+++++++++++++=+++++:.-@@@@####%%%%%%%%%%%%%%%%%%%%%%%%%%%@%@%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@@
				@@@#.*++++++++++++++++=:.@@@@##%%@@@@@@@@@@@@@@@%%@@@@@@@%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%##@@@@@
				@@@@ =*+++++++++++++++=.%@@@%%@@@@@@@@@@@@@@%%%@@@@@@@@%%@@%%@%%@@%%%%%%%%%%%@%%%%%%%%%%%%%#*@@@@@
				@@@@.:++++++++++++++++::@@@%%%@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%@@@%%@@%%%%%%%%%%%%%%%%%*@@@@@@
				@@@@@.=+++++++++++++++.:@@##@@@@@@@@@@@@%%%@%@@@@@@@@@@%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*@@@@@@
				@@@@@..=++++++++++=+++.:@@%%@@@@@@@@@%%%%%@@%%%%%%%%%@%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%#*@@@@@@@
				@@@@@@ .=++=++++++++++.:@@%%%@@@%%%%@@@@@@@%%@@%%%@%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*@@@@@@@@
				@@@@@@@..-++++++=+++++.:@@%%@@@@@@@@@@@@@%%%%%%%%%%%%@@%%%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%#*%@@@@@@@@
				@@@@@@@@-..:-*++++++++.:@@%%@%%%@@@@%@@@%%@@%@@@%%@%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%###**@@@@@@@@@@
				@@@@@@@@@@*   ........ .@@%%@%@@@%%%%%%%%%%%%%%%###########***######****#****####*****%@@@@@@@@@@@
				@@@@@@@@@@@@@@@%*@####=*@@%#%@@@@@@@@%@@%%%%%%%#@@%@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@%%%%%%%%%%%%@%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%@%%%%@%%%%%%%%%%%##*******++++++++++++++@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%@@%@@@%%@%%%@%%%%%%%%%%%%%%%%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%##***+**#%%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@##@%%%%%%%%%%%%%%@%%%%%%%%%%%%*@@@@@@%*#%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%*@@@@@@@@@#%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%%%%@@%%%%%%%%%%%%%%%%%%%#@@@@@@@@@#%%*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@#*%%%%%%%%%%%%%%%%%%%%%%%%%%##@@@@@@@*##**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*#%%%%%%%%%%%%%%%%%%%%%%%%###*###*###*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**#%%%%%%%%%%%%%%%%%%%%%%%%###****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#****####%%%%%%%%%%%%%###*+***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**++++**++*++***#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				""")
				type_text("made in python")
				time.sleep(3)
				type_text("mostly by Liam")
				time.sleep(3)
				type_text("tested by Jonas")
				time.sleep(3)
				type_text("text based adveture game by Miss Larose")
				time.sleep(3)
				type_text("help from my dad")
				time.sleep(3)
				type_text("literaly everything i learned from stack overflow or some other website")
				time.sleep(3)
				type_text("great ideas made by my bothers and teacher thanks ;)")
				time.sleep(3)
				type_text("goodby comeback soon")
				time.sleep(3)
				thecountofsomthing=0
				while thecountofsomthing<1100:
					print()
					thecountofsomthing+=1
				quit()
			elif hubo ==1:
				change_settings()
			elif hubo ==2:
				type_text("Ok sending you to Calcu.")
				time.sleep(1)
				calculator()
			elif hubo ==3:
				type_text("Ok sending you to Guessy.")
				time.sleep(1)
				game()
			elif hubo ==4:
				type_text("Ok sending you to Pally.")
				time.sleep(1)
				palindrome()
			elif hubo ==5:
				type_text("Ok sending you to Pig.")
				time.sleep(1)
				pig()
			elif hubo ==6:
				type_text("Ok sending you to Anny.")
				time.sleep(1)
				anagram()
			elif hubo ==7:
				type_text("Ok sending you to AV (she is a bit crazy).")
				avrage()
			elif hubo ==8:
				type_text("Ok sending you to Kelvin.")
				farinhight451()
			elif hubo ==9:
				type_text("Ok sending you to Arion.")
				area()
			elif hubo ==10:
				type_text("Ok sending you to lil'lister")
				lists()
			elif hubo ==11:
				type_text("Ok sending you to The Gamer")
				meet_o_code()
			elif hubo == 12:
				type_text("ok sending you to The Rock")
				dwane_the_rock()
			elif hubo == 13:
				type_text("ok sendig you to The DM")
				play_gamre()
			elif hubo == 14:
				type_text("ok sending you to THE PROGRAMER (be carfull)")
				the_game()
			elif hubo == 15:
				type_text("here is rickle the pickle")
				rickle()
			elif hubo == 16:
				type_text("here is dnd tracker")
				dnd()
			elif hubo == 7232010:
				code()
			else:
				type_text("Sorry this option is not available yet.")
if debuging == False:
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("connection successful")
	time.sleep(1)
	hub()
else:
	hub()