
#setup
#Define mid
#Make team manager
#	Make init
#		Hp
#		Damage
#		Drops
#		Resistance
#		Teir
#		Name
#		Description
#		Level
#		Mana
#		Xp
#		
#	Make get description
#		Get description
#	Make heal
#		Add heal to hp max at max hp
#	Make damage
#		If tier is not 0
#			If damage type is resistant
#				Subtract half damage from hp min at 0
#				Output damage
#		Subtract damage from hp min at 0
#		Output damage
#	Make if dead
#		remove
#	Make remove
#		If tier is 0
#			Output person damaged is unconscious
#			Set person damaged to unconscious
#			Remove person damaged from targets
#		Else
#			Grant player drops
#			
#			Output you got x and killed monster
#			Remove enemy
#	Make level up
#		Add one to level
#		Add 10 to max hp
#		Hp is max hp
#		Add 10 to max mana
#		Mana is max mana
#		Monster spawn rate +5 max at 70
#		Add 10 to bace damage
#	Make add buff
#		Damage to bace damage
#	Make atack
#		If player team go
#			Iterate thru conchis players
#			Get chose from enemies remaining use item or run
#			If atack
#				Set damage to bace damage
#				Damage enemies by damage
#			If use item
#				Output inventory
#				Use what player inputs what to use
#			If run
#				If randomnumber 1-5 is 5
#					Output run failed
#		Else
#			Iterate thru enemies
#				num=Randomnumber 1-tier
#				If num is 1
#					Damage random player
#				If num is 2
#					Damage all players
#				If num is 3
#					Damage random player with damage type of resistant
#				If num is 4
#					Damage all players with damage type of resistant
#
#				
#
#Make inventory manager
#Make init
#	Inventory = startin invintory
#Make use
#	If item useable
#		Pass item into evect func
#	Else
#		Raise error you found a error
#Make grant
#	Inventory add item if useable
#	Else
#		
#Make get length
#	Return length of inventory
#Make get inventory
#	Return inventory
#Make effect function with parameters of effect and person
#	If heal is in list effect 
#		Team manager target heal
#	Or if bomb is in list efect
#		Team manager tartget take damage
#Make prosses position function with x,y,description,speshal is defalt to none, item is defalt to none
#	pos=location on mid
#	If pos is watter
#		output(“not a valid location
#		Location is iligal
#		Monster spawn rate is 2
#	If pos is lava
#		output(“not a valid location
#		Location is iligal
#		Monster spawn rate is 2
#	If pos is item
#		Grant item
#	Ect
#func setup
#	Init inventory with 3 potions and 1 magic weppon
#	party=team manager starting stats
#If in file main
#	Input =Get do you want to play
#	If input is yes
#		setup
#		Set pos to 15,18
#		Set battal chance to 20
#		While length of continuous players is not 0
#			Chose from north,south,east,west (remove inposipble options)
#			If north subtract 1 from y pos
#			If south add 1 to y pos
#			If east add 1 to x
#			If west subtract 1 from x
#			Process position
#			Battal chance add monster spawn rate times 10
#			num=Radom number 1-100
#			If is num less than battal chance
#				Iterate thru range (1,min(round((random num-num)/33),3)
#					Random monster 1-min(level,4)add to monsters
#					Monster team=team manager(unpacked monsters)
#While length of monster team is not 0 and length of continuous players is not 0
#	Attack plater turn
#	Atack monster turn
#While xp>= 25
#	Level up
#	xp-25
#			Elif position is speshal
#				If speshal = something
#					Do something
#				ect
#			Elif position is item
#				Grant item
#			Elif position is town
#				While true
#					Options are shop gamble and leave
#					If shop
#						Options are x y and z for x y and z
#					If gamble 
#						How much to gamble max gold
#						Optins are heads tails
#						if random num=1 and heads
#							Gold =gamble+gamble
#						If random num=2 and tails
#							Gold =gamble+gamble
#						Else
#							Lost
#					If leave 
#						Add one to x
#				
#	Else
#	Output goodbye

import util_functions
import random
class LogicError(Exception):
	if util_functions.get_linenumber() != 168:
		print(f"logic error at line {util_functions.get_linenumber()}")
mid=[["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","l","i1","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","h","h","h","l","h","h","speshal","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","h","h","h","h","ni1","l","l","h","h","i2","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","h","u","h","h","l","l","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","u","u","h","l","h","s","l","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","u","c","h","b","h","h","l","l","h","u","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","h","h","h","h","h","l","h","h","h","h","h","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","h","u","f","f","f","f","f","f","f","f","f","f","h","u","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","h","f","f","f","f","f","f","s","f","f","f","f","f","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","f","f","f","f","f","f","c","f","f","f","t","p","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","f","f","s","f","f","f","f","f","f","f","f","p","f","f","ni2","f","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","f","i3","f","f","f","f","f","f","f","i4","p","p","p","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","f","f","f","f","f","f","f","f","f","f","p","p","p","f","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","r","f","f","f","f","f","f","f","f","f","p","p","p","f","f","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","t","p","r","f","r","f","f","p","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","p","t","w","w","i5","w","w"],
["w","w","w","w","w","w","p","f","b","r","f","f","p","p","p","p","p","p","c","u","f","f","f","f","f","f","f","f","f","f","w","w","f","f","f","w"],
["w","w","w","w","w","f","p","f","f","t","r","f","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","b","w","f","p","f","f","w"],
["w","w","w","w","f","p","p","p","f","f","f","b","r","c","p","spawn","p","p","p","p","f","f","f","f","f","f","f","f","r","s","p","p","p","p","f","w"],
["w","w","w","w","f","p","p","p","p","p","p","p","p","r","t","t","p","p","p","p","r","f","f","f","f","f","f","f","r","p","t","p","p","p","f","w"],
["w","w","w","w","f","c","f","f","p","p","p","p","p","r","t","t","r","r","p","r","p","f","f","f","f","f","f","f","f","r","p","p","p","p","w","w"],
["w","w","w","w","f","f","f","f","p","p","p","p","p","p","r","r","p","c","r","p","t","f","f","s","f","f","f","c","f","f","f","f","f","w","w","w"],
["w","w","w","w","f","f","f","f","p","p","p","p","p","p","p","p","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","w","w","w"],
["w","w","w","w","f","f","f","f","f","f","f","f","f","f","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","f","f","w","w","w"],
["w","w","w","w","w","s","s","f","f","s","s","s","s","s","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","f","w","w","w","w"],
["w","w","w","w","w","w","s","s","s","s","s","w","w","s","s","s","f","f","f","f","f","f","f","f","f","f","f","w","aw","aw","aw","aw","w","w","w","w"],
["w","w","w","w","w","w","s","s","s","s","w","w","w","w","s","s","s","f","f","f","f","s","s","s","s","s","w","aw","aw","aw","aw","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","s","s","w","w","w","w","w","s","s","s","s","s","s","s","s","s","s","s","w","w","aw","aw","i6","aw","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","s","s","w","w","w","s","s","s","s","s","s","s","s","s","i7","s","s","s","w","w","aw","aw","aw","aw","aw","aw","w","w","w"],
["w","w","w","w","w","i8","s","s","w","w","w","s","s","s","s","s","s","s","s","t","s","s","s","s","w","w","w","w","aw","aw","ni3","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","s","s","s","s","s","s","s","s","s","s","s","s","w","w","w","w","w","w","aw","aw","aw","w","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","s","s","s","s","s","i9","s","s","s","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","w","s","s","s","s","s","s","s","ni4","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]
upper=[["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","sk","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","sk","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","b","b","b","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","g","b","b","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","g","sk","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","u","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","boss","boss","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","boss","boss","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","g","","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","boss","boss","u","u","u","u","u","u","u","u","u","u","g","s","g","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","puzzle","g","g","g","ni","u","u","u","u","u","u","u","u","u","u","g","u","u","b","b","b","g","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","g","g","g","g","g","u","u","u","u","u","u","u","u","u","u","g","g","g","b","b","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","g","spehsal","g","g","u","u","u","u","u","u","u","u","u","u","g","t","s","g","g","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","b","b","g","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","u","u","g","g","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u","u","u","g","g","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","g","g","u","u","u","u","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","b","g","g","g","g","g","g","g","u","u","u","u","g","puzzle","g","speshal","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","s","g","b","u","g","ni","g","g","g","g","b","u","u","g","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","u","u","u","g","g","u","u","u","b","b","g","g","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"]]
underground=[["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","u","u","u","u","u","u","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","u","u","u","h","h","h","l","i","h","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","u","h","u","h","h","u","h","l","l","h","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","h","h","u","h","u","h","h","h","h","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","h","h","u","h","h","u","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","h","c","h","u","h","u","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","h","h","h","h","h","u","h","h","u","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","u","h","h","h","u","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","g","u","h","h","h","u","g","g","g","ui","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","c","g","u","h","h","u","g","g","g","ui","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","g","g","u","h","h","u","g","g","g","ui","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","g","g","g","g","g","g","u","g","u","i","g","g","g","ni","u","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","i","g","g","g","g","g","g","u","g","g","u","u","u","g","g","ui","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","g","u","g","u","i","g","g","u","u","g","g","g","u","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","g","g","g","g","u","g","g","boss teleport","u","g","g","g","g","g","g","g","i","u","u","u","u","u","u","u","u","w","w"],
["w","w","w","w","w","w","u","g","g","g","g","g","u","g","g","g","g","u","c","u","g","g","g","g","g","u","g","g","g","g","g","g","g","ni","u","w"],
["w","w","w","w","w","u","g","g","g","g","g","u","g","g","g","g","g","g","u","u","g","g","g","g","g","u","g","g","g","g","g","g","g","g","u","w"],
["w","w","w","w","u","g","g","g","g","g","g","u","g","c","g","g","g","g","g","g","g","g","g","g","g","i","u","g","g","g","g","g","g","g","u","w"],
["w","w","w","w","u","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","g","u","w"],
["w","w","w","w","u","c","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","u","w","w"],
["w","w","w","w","u","g","g","g","g","g","g","g","g","g","u","g","g","c","g","g","g","g","g","g","g","u","t","c","g","g","g","g","u","w","w","w"],
["w","w","w","w","u","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","u","w","w","w"],
["w","w","w","w","u","g","g","i","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","u","w","w","w"],
["w","w","w","w","w","u","g","g","g","g","g","u","u","g","g","g","u","g","g","g","g","g","g","g","g","g","g","u","u","u","u","u","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","g","u","w","w","u","g","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","u","w","w","w","w","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","g","c","u","w","w","w","w","w","u","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","g","g","u","w","w","w","u","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","i","u","w","w","w","u","g","g","g","g","g","i","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","u","w","w","w","w","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","u","w","w","w","w","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","u","w","w","w","w","w","u","u","u","u","u","u","u","g","g","i","u","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","u","u","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]

class TeamManager:
	def __init__(self,hp,dmg,drops,resistance,teir,name,description,level=1,mana=10,xp=0):
		self.hp_max=hp
		self.hp=hp
		self.dmg=dmg
		self.drops=drops
		self.resistance=resistance
		self.teir=teir
		self.name=name
		self.description=description
		if teir[0]<0:
			self.level=level
			self.mana_max=mana
			self.mana=mana
			self.xp=xp
			self.type={"team member 1":{"hp:":self.hp[0],"dmg":self.dmg[0],"name":self.name[0],"description":self.description[0],"level":self.level[0],"mana":self.mana[0],"xp":self.xp[0]},
"team member 2":{"hp:":self.hp[1],"dmg":self.dmg[1],"name":self.name[1],"description":self.description[1],"level":self.level[1],"mana":self.mana[1],"xp":self.xp[1]},
"team member 3":{"hp:":self.hp[2],"dmg":self.dmg[2],"name":self.name[2],"description":self.description[2],"level":self.level[2],"mana":self.mana[2],"xp":self.xp[2]}}
		else:
			if hp[0]!=None:
				self.type=None
			elif hp[1]!=None:
				self.type=None
			elif hp[2]!=None:
				self.type=None
	def getattribute(self, name):
		return self.description
	def heal(self,heal_amount,person):
		self.hp[person]=min(self.hp[person]+heal_amount,self.hp_max[person])
	def damage(self,damage_amount,damage_type,person):
		if self.teir[person]!=0:
			self.hp[person]=max(self.hp[person]-damage_amount,0)
			print(f"{self.name[person]} took {damage_amount} damage")
			return
		self.hp[person]=max(self.hp[person]-damage_amount,0)
		print(f"{self.name[person]} took {damage_amount} damage")
	def if_dead(self,person,targets):
		if self.hp[person]<=0:
			self.remove(person,targets)
	def remove(self,person,targets):
		if self.teir[person]==0:
			print(f"{self.name[person]} is unconscious")
			self.hp[person]=-1
			
		else:
			print(f"You got {self.drops[person]} and killed {self.name[person]}")
			targets.pop(person)
	def level_up(self,person):
		self.level[person]+=1
		self.hp_max[person]+=10
		self.hp[person]=self.hp_max[person]
		self.mana_max[person]+=10
		self.mana[person]=self.mana_max[person]
		if self.level[person]%7==0:
			monster_spawn_rate=min(monster_spawn_rate+5,70)
		self.dmg[person]+=10
	def add_buff(self,damage_buff,person):
		self.dmg[person]+=damage_buff
	def attack(self,players_go,continuous_players,enemies,inventory):
		if players_go:
			for i in range(len(continuous_players)):
				print("Choose from attack, use item, or run")
				choice=util_functions.get_valid_type(str,"Choose action","that is not a valid action",["attack","use item","run"])
				if choice=="attack":
					damage=self.dmg[i]
					target=random.randint(0,len(enemies)-1)
					enemies.damage(damage,"normal",target)
				elif choice=="use item":
					print(inventory.get_inventory())
					print("What do you want to use?")
					item_choice=util_functions.get_valid_type(str,"Choose item","that is not a valid item",list(inventory.get_inventory().keys()))
					inventory.use(item_choice,continuous_players,i)
				elif choice=="run":
					if random.randint(1,5)==5:
						print("Run failed")
		else:
			for i in range(len(enemies.hp)):
				num=random.randint(1,enemies.teir[i])
				if num==1:
					target=random.randint(0,len(continuous_players)-1)
					enemies.damage(enemies.dmg[i],"normal",target)
				elif num==2:
					for j in range(len(continuous_players)):
						enemies.damage(enemies.dmg[i],"normal",j)
				elif num==3:
					target=random.randint(0,len(continuous_players)-1)
					enemies.damage(enemies.dmg[i]//2,"resistant",target)
				elif num==4:
					for j in range(len(continuous_players)):
						enemies.damage(enemies.dmg[i]//2,"resistant",j)
	def get_continuous_players(self):
		continuous_players=[]
		for i in range(3):
			if self.hp[i]>0:
				continuous_players.append(i)
		return continuous_players
	def gain_mana(self,mana_amount,person):
		self.mana[person]=min(self.mana[person]+mana_amount,self.mana_max[person])
	def magic_attack_choise(self,person,inventory):
		gems=[]
		print("all mana atacks cost 10 mana")
		prompt="Choose a chaos gem to use:\n0 to cancel"
		for gem in inventory.get_inventory():
			if gem["type"]=="chaos gem":
				gems.append(gem)
		for iter,x in enumerate(gems):
			prompt+=f"\n{iter} for {x['name']}: {x['description']}"
		util_functions.get_valid_type(int,prompt,"that is not a gem that is available",list(range(0,len(gems)+1)))-1
		if choice==-1:
			return
		if self.mana[person]>=10:
			self.mana[person]-=10
		choice=gems[choice]
		if choice =="water":
			enemies.damage(choice["damage"],"water",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="fire":
			enemies.damage(choice["damage"],"fire",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="wind":
			enemies.damage(choice["damage"],"wind",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="darkness":
			enemies.damage(choice["damage"],"darkness",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="frost":
			enemies.damage(choice["damage"],"ice",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="lightning":
			enemies.damage(choice["damage"],"electric",util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(enemies.hp)))))
		elif choice =="resurrection":
			party.heal(choice["heal"],util_functions.get_valid_type(int,"Choose target","that is not a valid target",list(range(0,len(party.get_continuous_players())))))
enemies=TeamManager([50,50,50],[10,15,20],[{"name":"bomb core","quantity":1,"useable":True,"effect":{"bomb core":30}},{"name":"lightning core","quantity":1,"useable":True,"effect":{"lightning core":30}},{"name":"blizzard core","quantity":1,"useable":True,"effect":{"blizzard core":30}}],[ "fire","electric","ice"],[1,2,3],["Goblin","Orc","Troll"],["A weak goblin","A strong orc","A huge troll"])
class InventoryManager:
	def __init__(self,starting_inventory):
		self.inventory=starting_inventory
	def use(self,item,continuous_players,person):
		if item in self.inventory and self.inventory[item]["useable"]:
			self.effect_function(self.inventory[item]["effect"],continuous_players,person)
			self.inventory[item]["quantity"]-=1
			if self.inventory[item]["quantity"]<=0:
				self.inventory.pop(item)
		else:
			raise LogicError
	def grant(self,item):
		if item["useable"]:
			if item["name"] in self.inventory:
				self.inventory[item["name"]]["quantity"]+=item["quantity"]
			else:
				self.inventory[item["name"]]=item
	def get_length(self):
		return len(self.inventory)
	def get_inventory(self):
		return self.inventory
	def effect_function(self,effect,continuous_players,person):
		if "heal" in effect:
			party.heal(effect["heal"],person)
		if "heal+" in effect:
			party.heal(effect["heal+"],person)
		if "heal++" in effect:
			party.heal(effect["heal++"],person)
		if "ether" in effect:
			party.gain_mana(effect["ether"],person)
		if "elixir" in effect:
			party.gain_mana(effect["elixir"],person)
			party.heal(effect["elixir"],person)
		if "hi-ether" in effect:
			party.gain_mana(effect["hi-ether"],person)
		if "hi-elixir" in effect:
			party.gain_mana(effect["hi-elixir"],person)
			party.heal(effect["hi-elixir"],person)
		if "ඞ" in effect:
			party.heal(party.hp_max[person],1)
			party.heal(party.hp_max[person],2)
			party.heal(party.hp_max[person],3)
			party.gain_mana(party.mana_max[person],1)
			party.gain_mana(party.mana_max[person],2)
			party.gain_mana(party.mana_max[person],3)
			enemies.damage(effect["debug item"],"normal",1)
			enemies.damage(effect["debug item"],"normal",2)
			enemies.damage(effect["debug item"],"normal",3)
		elif "bomb core" in effect:
			enemies.damage(effect["bomb core"],"fire",1)
			enemies.damage(effect["bomb core"],"fire",2)
			enemies.damage(effect["bomb core"],"fire",3)
		elif "lightning core" in effect:
			enemies.damage(effect["lightning core"],"electric",1)
			enemies.damage(effect["lightning core"],"electric",2)
			enemies.damage(effect["lightning core"],"electric",3)
		elif "blizzard core" in effect:
			enemies.damage(effect["blizzard core"],"ice",1)
			enemies.damage(effect["blizzard core"],"ice",2)
			enemies.damage(effect["blizzard core"],"ice",3)
		elif "fire core" in effect:
			enemies.damage(effect["fire core"],"fire",person)
		elif "electric core" in effect:
			enemies.damage(effect["electric core"],"electric",person)
		elif "ice core" in effect:
			enemies.damage(effect["ice core"],"ice",person)
		elif "chaos gem" in effect:
			party.magic_attack_choise(person,self,inventory)
location_dict={
"h":{"name":"hot land","description":"a land of heat","special":None},
"l":{"name":"lava land","description":"a land of lava","special":"not valid location"},	
"w":{"name":"water","description":"a body of water","special":"Not valid location"},
"i":{"name":"item","description":["You found an item!","youv already sherched here"],"special":"item"},
"ni":{"name":"nessasary item","description":["You found a nessasary item!","youv already sherched here"],"special":"item"},
"c":{"name":"cave","description":"a dark cave","special":["desend","ascend"]},
"sk":{"name":"sky lift","description":"a sacred place with powerfull lifting runes","special":["ascend","desend"]},
"b":{"name":"bridge","description":"a rickety bridge","special":None},
"t":{"name":"town","description":"a small town","special":"town"},
"f":{"name":"feild","description":"a wide open feild","special":None},
"r":{"name":"river","description":"a flowing river","special":"passable with gem of water"},
"spawn":{"name":"spawn point","description":"the place where your adventure begins","special":None},
"s":{"name":"snow","description":"a cold snowy area","special":None},
}
monster_dict={
"dragon":{"tier":2,"hp":150,"dmg":30,"drops":{"name":"dragon tooth","quantity":1,"useable":False,"effect":{"buff":50,"xp":50}},"resistance":"fire","description":"A large fire-breathing dragon.","speshal spwan location":["~water","~lava","hot","~river","~snow"]},
"blob":{"tier":1,"hp":80,"dmg":15,"drops":{"name":"slime gel","quantity":1,"useable":True,"effect":{"heal":20,"xp":25}},"resistance":"water","description":"A gooey blob that oozes around.","speshal spwan location":["~water","~lava","~river","~snow"]},
"orc":{"tier":2,"hp":120,"dmg":25,"drops":{"name":"orc tusk","quantity":1,"useable":True,"effect":{"buff":10,"xp":25}},"resistance":"wind","description":"A brutish orc warrior.","speshal spwan location":["~lava","~water","~river"]},
"troll":{"tier":2,"hp":130,"dmg":28,"drops":{"name":"troll club","quantity":1,"useable":False,"effect":{"buff":10,"xp":50}},"resistance":"wind","description":"A large and strong troll.","speshal spwan location":["~lava","~water","bridge","~river"]},
"goblin":{"tier":1,"hp":30,"dmg":12,"drops":{"name":"goblin ear","quantity":1,"useable":False,"effect":{"buff":5,"xp":15}},"resistance":"darkness","description":"A sneaky goblin.","speshal spwan location":["~water","~lava","cave","~river"]},
"knight":{"tier":3,"hp":200,"dmg":40,"drops":{"name":"knight's shield","quantity":1,"useable":False,"effect":{"buff":20,"xp":75}},"resistance":"light","description":"A heavily armored knight.","speshal spwan location":["~water","~lava","town","bridge","~river"]},#if spawn on brige have speshal dialog (none shall pass, its only a flesh wound, tis but a scratch, ive had worse)
"construct":{"tier":3,"hp":180,"dmg":35,"drops":{"name":"mechanical gear","quantity":1,"useable":False,"effect":{"buff":15,"xp":60}},"resistance":"electric","description":"A mechanical construct brought to life.","speshal spwan location":["~water","~lava","cave","~river"]},
"Animated statue":{"tier":2,"hp":140,"dmg":22,"drops":{"name":"stone shard","quantity":1,"useable":False,"effect":{"buff":10,"xp":40}},"resistance":"wind","description":"A statue that has come to life.","speshal spwan location":["~water","~lava","cave","hot","~river"]},
"Possessed cow":{"tier":1,"hp":90,"dmg":18,"drops":{"name":"haunted horn","quantity":1,"useable":False,"effect":{"buff":8,"xp":30}},"resistance":"darkness","description":"A cow possessed by a spirit.","speshal spwan location":["~water","~lava","feild","~river"]},
"mermaid":{"tier":2,"hp":110,"dmg":20,"drops":{"name":"song of the sea","quantity":1,"useable":True,"effect":{"heal":15,"xp":35}},"resistance":"water","description":"A mystical mermaid.","speshal spwan location":["water","~lava","~hot","~feild","~cave","~bridge","river","~town","~snow"]},
"Lava monster":{"tier":2,"hp":160,"dmg":27,"drops":{"name":"lava core","quantity":1,"useable":True,"effect":{"bomb core":12,"xp":45}},"resistance":"fire","description":"A creature made of molten lava.","speshal spwan location":["~water","lava","hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"Fish lord":{"tier":3,"hp":190,"dmg":33,"drops":{"name":"trident of the deep","quantity":1,"useable":False,"effect":{"buff":25,"xp":80}},"resistance":"water","description":"The ruler of all fish.","speshal spwan location":["water","~lava","~hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"Lava warden":{"tier":3,"hp":210,"dmg":38,"drops":{"name":"ember shield","quantity":1,"useable":False,"effect":{"buff":30,"xp":90}},"resistance":"fire","description":"A guardian of the lava realms.","speshal spwan location":["~water","lava","hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"blain":{"tier":100,"hp":9999,"dmg":500,"drops":{"name":"debug item","quantity":1,"useable":True,"effect":{"ඞ":9999}},"resistance":"darkness","description":"one of the makers of the game","speshal spwan location":["debug"]},
"liam":{"tier":100,"hp":9999,"dmg":500,"drops":{"name":"debug item","quantity":1,"useable":True,"effect":{"ඞ":9999}},"resistance":"darkness","description":"one of the makers of the game","speshal spwan location":["debug"]},
"yeti":{"tier":2,"hp":150,"dmg":30,"drops":{"name":"yeti fur","quantity":1,"useable":False,"effect":{"buff":20,"xp":50}},"resistance":"ice","description":"A large ape-like creature covered in fur.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"ice cube":{"tier":1,"hp":70,"dmg":12,"drops":{"name":"frost shard","quantity":1,"useable":True,"effect":{"heal":15,"xp":20}},"resistance":"ice","description":"A small cube of ice that has come to life.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"Nyx-spawn":{"tier":3,"hp":200,"dmg":40,"drops":{"name":"shadow essence","quantity":1,"useable":False,"effect":{"buff":30,"xp":75}},"resistance":"darkness","description":"A creature born from the shadows.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"phoenix":{"tier":3,"hp":180,"dmg":35,"drops":{"name":"phoenix feather","quantity":1,"useable":True,"effect":{"heal++":30,"xp":60}},"resistance":"fire","description":"A mythical bird that rises from its ashes.","speshal spwan location":["~water","lava","hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"shadow beast":{"tier":2,"hp":140,"dmg":22,"drops":{"name":"dark fang","quantity":1,"useable":False,"effect":{"buff":15,"xp":40}},"resistance":"darkness","description":"A beast that lurks in the shadows.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"ghost":{"tier":1,"hp":60,"dmg":10,"drops":{"name":"ectoplasm","quantity":1,"useable":True,"effect":{"heal":10,"xp":15}},"resistance":"darkness","description":"A wandering spirit.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"zombie":{"tier":1,"hp":50,"dmg":8,"drops":{"name":"rotting flesh","quantity":1,"useable":False,"effect":{"buff":5,"xp":10}},"resistance":"darkness","description":"A reanimated corpse.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"lord king":{"tier":10,"hp":1000,"dmg":100,"drops":{"name":"king's crown","quantity":1,"useable":False,"effect":{"buff":100,"xp":500}},"resistance":"light","description":"The ultimate ruler.","speshal spwan location":["debug"]},
"lord king's guard":{"tier":5,"hp":500,"dmg":50,"drops":{"name":"guard's emblem","quantity":1,"useable":False,"effect":{"buff":50,"xp":250}},"resistance":"light","description":"The elite guard of the lord king.","speshal spwan location":["debug"]},
"shadow dragon":{"tier":10,"hp":1200,"dmg":120,"drops":{"name":"shadow scale","quantity":1,"useable":False,"effect":{"buff":120,"xp":600}},"resistance":"darkness","description":"A dragon born from shadows.","speshal spwan location":["debug"]},
"samus aran":{"tier":50,"hp":3000,"dmg":300,"drops":{"name":"power suit","quantity":1,"useable":False,"effect":{"buff":3000,"xp":1500}},"resistance":"electric","description":"A legendary bounty hunter.","speshal spwan location":["debug"]},#nentendo pleese dont sue me
"korock":{"tier":0,"hp":1,"dmg":1,"drops":{"name":"the soul of a korock you monster","quantity":1,"useable":False,"effect":{"buff":9999,"xp":9999}},"resistance":"wind","description":"A small plant-like creature from the land of hyrule.","speshal spwan location":["debug"]},
"nintendo":{"tier":100000000000000000000000000000000000000000000000,"hp":999999999999999999999999999999999999999999999999,"dmg":999999999999999999999999999999999999999999999999,"drops":{"name":"no one can get this item","quantity":1,"useable":False,"effect":{"buff":100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,"xp":100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}},"resistance":"light","description":"the ultimate being","speshal spwan location":["debug"]}}
def get_random_monsters(party_level,location):
	monsters=[]
	possible_monsters=[]
	for monster in monster_dict:
		speshal_locations=monster_dict[monster]["speshal spwan location"]
		valid_location=False
		for loc in speshal_locations:
			if loc.startswith("~"):
				if loc[1:]!=location["position"]:
					valid_location=True
			else:
				if loc==location["position"]:
					valid_location=True
		if valid_location:
			possible_monsters.append(monster)
	for i in range(len(party_level)):
		level=party_level[i]
		eligible_monsters=[]
		for monster in possible_monsters:
			if monster_dict[monster]["tier"]<=level:
				eligible_monsters.append(monster)
		if len(eligible_monsters)==0:
			monster_choice="goblin"
		else:
			monster_choice=random.choice(eligible_monsters)
		monsters.append({"hp":monster_dict[monster_choice]["hp"],"dmg":monster_dict[monster_choice]["dmg"],"drops":monster_dict[monster_choice]["drops"],"resistance":monster_dict[monster_choice]["resistance"],"teir":monster_dict[monster_choice]["tier"],"name":monster_choice,"description":monster_dict[monster_choice]["description"]})
	return monsters
def setup_enemy_party(monster_list):
	hp=[]
	dmg=[]
	drops=[]
	resistance=[]
	teir=[]
	name=[]
	description=[]
	for monster in monster_list:
		hp.append(monster["hp"])
		dmg.append(monster["dmg"])
		drops.append(monster["drops"])
		resistance.append(monster["resistance"])
		teir.append(monster["teir"])
		name.append(monster["name"])
		description.append(monster["description"])
	return TeamManager(hp,dmg,drops,resistance,teir,name,description)
def debug_spawn():
	global monster_dict
	for x in monster_dict:
		print(x)
	choice=util_functions.get_valid_type(str,"Choose monster to spawn from: ","that is not a valid monster",list(monster_dict.keys()))
def process_position(x,y,description,special=None,item=None):
	pos=mid[y][x]
	if pos=="w":
		print("not a valid location")
		location="illegal"
		monster_spawn_rate=2
	elif pos=="l":
		print("not a valid location")
		location="illegal"
		monster_spawn_rate=2
	elif pos=="i":
		inventory.grant(item)
	elif pos=="speshal":
		if special=="something":
			pass
	elif pos=="r":
		if "gem of water" in inventory.get_inventory():
			print("you use the gem of water to pass the river")
		else:
			print("not a valid location")
			location="illegal"
			monster_spawn_rate=2
	elif pos=="c":
		if layer=="mid":
			layer="low"
			print("you desend into the cave to the lower layer")
		else:
			layer="mid"
			print("you ascend out of the cave to the mid layer")
	elif pos=="sk":
		if "gem of wind" not in inventory.get_inventory():
			print("not a valid location")
			location="illegal"
			monster_spawn_rate=2
		else:
			if layer=="mid":
				layer="high"
				print("you ascend the sky lift to the high layer")
			else:
				layer="mid"
				print("you desend the sky lift to the mid layer")
	elif pos=="t":
		print("you enter the town, you can rest here and buy items")
		while True:
			choice=util_functions.get_valid_type(str,"do you want to rest, buy items, save, or leave: ","that is not a valid action",["rest","buy items","save","leave"])
			if choice=="rest":
				for i in range(len(party.get_continuous_players())):
					party.heal(party.hp_max[i],i)
					party.gain_mana(party.mana_max[i],i)
				print("your party has been fully healed")
			elif choice=="buy items":
				print("welcome to the shop, what do you want to buy?")
				while True:
					print(f"you have {inventory.get_inventory().get('gold',{'quantity':0})['quantity']} gold")
					shop_choice=util_functions.get_valid_type(str,"do you want to buy a potion for 10 gold, ether for 15 gold, or leave: ","that is not a valid action",["potion","ether","leave","debug"])
					if shop_choice=="potion" and inventory.get_inventory().get("gold",{"quantity":0})["quantity"]<10:
						inventory.grant({"name":"potion","quantity":1,"useable":True,"effect":{"heal":20}})
						print("you bought a potion")
						inventory.get_inventory()["gold"]["quantity"]-=10
					elif shop_choice=="ether" and inventory.get_inventory().get("gold",{"quantity":0})["quantity"]<15:
						inventory.grant({"name":"ether","quantity":1,"useable":True,"effect":{"ether":15}})
						print("you bought ether")
						inventory.get_inventory()["gold"]["quantity"]-=15
					elif shop_choice=="leave":
						print("you leave the shop")
						break
			elif choice=="leave":
				print("you leave the town")
				break
			elif choice=="save":
				print("generating save code")
				save_code=""
				save_code+=f"{x_pos},{y_pos},{layer};"
				for i in range(3):
					save_code+=f"{party.hp[i]},{party.hp_max[i]},{party.mana[i]},{party.mana_max[i]},{party.dmg[i]},{party.level[i]};"
				for item in inventory.get_inventory():
					save_code+=f"{item},{inventory.get_inventory()[item]['quantity']};"
				print(f"your save code is:\n{save_code}")
	return {"position":pos,"description":description,"special":special,"item":item}
def load_save(save_code):
	global x_pos,y_pos,layer,party,inventory
	sections=save_code.split(";")
	pos_section=sections[0].split(",")
	x_pos=int(pos_section[0])
	y_pos=int(pos_section[1])
	layer=pos_section[2]
	for i in range(3):
		stats=sections[i+1].split(",")
		party.hp[i]=int(stats[0])
		party.hp_max[i]=int(stats[1])
		party.mana[i]=int(stats[2])
		party.mana_max[i]=int(stats[3])
		party.dmg[i]=int(stats[4])
		party.level[i]=int(stats[5])
	inventory_items=sections[4:]
	inventory.inventory={}
	for item in inventory_items:
		if item=="":
			continue
		item_stats=item.split(",")
		inventory.inventory[item_stats[0]]={"name":item_stats[0],"quantity":int(item_stats[1]),"useable":True,"effect":{}}
inventory=InventoryManager({"potion":{"name":"potion","quantity":3,"useable":True,"effect":{"heal":20}},"ether":{"name":"ether","quantity":2,"useable":True,"effect":{"ether":15}},"gold":{"name":"gold","quantity":50,"useable":False,"effect":{}},"gold":{"name":"gold","quantity":50,"useable":False,"effect":{}}})
party=TeamManager([100,100,100],[10,10,10],[None,None,None],[None,None,None],[-1,-1,-1],["Zack","Amilia","Clang"],["your friend","you","a compiler for the language c++ that is also a deity"],[1,1,1],[10,0,20],[0,0,0])
monster_spawn_rate=20
debug=False
layer="mid"
if __name__=="__main__":
	input_play=	util_functions.get_valid_type(str,"Do you want to play: ","that is not a valid answer",["yes","no"])
	if input_play.lower()=="yes":
		x_pos=15
		y_pos=18
		battle_chance=20
		layer="mid"
		while len(party.get_continuous_players())>0:
			if debug:
				print(f"You are at position x:{x_pos} y:{y_pos} in layer:{layer}")
			if mid[y_pos][x_pos+1]=="w":
				print("You see a large body of water to the east")
			if mid[y_pos][x_pos-1]=="w":
				print("You see a large body of water to the west")
			if mid[y_pos+1][x_pos]=="w":
				print("You see a large body of water to the south")
			if mid[y_pos-1][x_pos]=="w":
				print("You see a large body of water to the north")
			if mid[y_pos][x_pos+1]=="l":
				print("You see a large body of lava to the east")
			if mid[y_pos][x_pos-1]=="l":
				print("You see a large body of lava to the west")
			if mid[y_pos+1][x_pos]=="l":
				print("You see a large body of lava to the south")
			if mid[y_pos-1][x_pos]=="l":
				print("You see a large body of lava to the north")
			if mid[y_pos][x_pos+1]=="r":
				print("You see a flowing river to the east")
			if mid[y_pos][x_pos-1]=="r":
				print("You see a flowing river to the west")
			if mid[y_pos+1][x_pos]=="r":
				print("You see a flowing river to the south")
			if mid[y_pos-1][x_pos]=="r":
				print("You see a flowing river to the north")
			if mid[y_pos][x_pos+1]=="s":
				print("You see a snowy area to the east")
			if mid[y_pos][x_pos-1]=="s":
				print("You see a snowy area to the west")
			if mid[y_pos+1][x_pos]=="s":
				print("You see a snowy area to the south")
			if mid[y_pos-1][x_pos]=="s":
				print("You see a snowy area to the north")
			if mid[y_pos][x_pos+1]=="h":
				print("You see a volcanic area to the east")
			if mid[y_pos][x_pos-1]=="h":
				print("You see a volcanic area to the west")
			if mid[y_pos+1][x_pos]=="h":
				print("You see a volcanic area to the south")
			if mid[y_pos-1][x_pos]=="h":
				print("You see a volcanic area to the north")
			if mid[y_pos][x_pos+1]=="f":#forest
				print("You see a forest to the east")
			if mid[y_pos][x_pos-1]=="f":
				print("You see a forest to the west")
			if mid[y_pos+1][x_pos]=="f":
				print("You see a forest to the south")
			if mid[y_pos-1][x_pos]=="f":
				print("You see a forest to the north")
			if mid[y_pos][x_pos+1]=="t":#town
				print("You see a town to the east")
			if mid[y_pos][x_pos-1]=="t":
				print("You see a town to the west")
			if mid[y_pos+1][x_pos]=="t":
				print("You see a town to the south")
			if mid[y_pos-1][x_pos]=="t":
				print("You see a town to the north")
			if mid[y_pos][x_pos+1]=="c":#cave
				print("You see a cave to the east, it could bring you underground")
			if mid[y_pos][x_pos-1]=="c":
				print("You see a cave to the west, it could bring you underground")
			if mid[y_pos+1][x_pos]=="c":
				print("You see a cave to the south, it could bring you underground")
			if mid[y_pos-1][x_pos]=="c":
				print("You see a cave to the north, it could bring you underground")
			if mid[y_pos][x_pos+1]=="sk":#sky lift
				print("You see a sky lift to the east, it could bring you to higher ground")
			if mid[y_pos][x_pos-1]=="sk":
				print("You see a sky lift to the west, it could bring you to higher ground")
			if mid[y_pos+1][x_pos]=="sk":
				print("You see a sky lift to the south, it could bring you to higher ground")
			if mid[y_pos-1][x_pos]=="sk":
				print("You see a sky lift to the north, it could bring you to higher ground")
			if mid[y_pos][x_pos+1]=="b":#bridge
				print("You see a bridge to the east")
			if mid[y_pos][x_pos-1]=="b":
				print("You see a bridge to the west")
			if mid[y_pos+1][x_pos]=="b":
				print("You see a bridge to the south")
			if mid[y_pos-1][x_pos]=="b":
				print("You see a bridge to the north")
			if mid[y_pos][x_pos+1]=="spawn":#spawn point
				print("You see where you started this quest to the east")
			if mid[y_pos][x_pos-1]=="spawn":
				print("You see where you started this quest to the west")
			if mid[y_pos+1][x_pos]=="spawn":
				print("You see where you started this quest to the south")
			if mid[y_pos-1][x_pos]=="spawn":
				print("You see where you started this quest to the north")
			if mid[y_pos][x_pos+1]=="i":#item
				print("You see something shiny to the east")
			if mid[y_pos][x_pos-1]=="i":
				print("You see something shiny to the west")
			if mid[y_pos+1][x_pos]=="i":
				print("You see something shiny to the south")
			if mid[y_pos-1][x_pos]=="i":
				print("You see something shiny to the north")
			if mid[y_pos][x_pos+1]=="ni":#nessasary item
				print("You feal something big to the east")
			if mid[y_pos][x_pos-1]=="ni":
				print("You feal something big to the west")
			if mid[y_pos+1][x_pos]=="ni":
				print("You feal something big to the south")
			if mid[y_pos-1][x_pos]=="ni":
				print("You feal something big to the north")
			if mid[y_pos][x_pos+1]=="aw":#acsesable water
				print("You see some water that looks save enugh to swim in to the east")
			if mid[y_pos][x_pos-1]=="aw":
				print("You see some water that looks save enugh to swim in to the west")
			if mid[y_pos+1][x_pos]=="aw":
				print("You see some water that looks save enugh to swim in to the south")
			if mid[y_pos-1][x_pos]=="aw":
				print("You see some water that looks save enugh to swim in to the north")
			if mid[y_pos][x_pos+1]=="g":#floating ground
				print("You see some floating ground to the east")
			if mid[y_pos][x_pos-1]=="g":
				print("You see some floating ground to the west")
			if mid[y_pos+1][x_pos]=="g":
				print("You see some floating ground to the south")
			if mid[y_pos-1][x_pos]=="g":
				print("You see some floating ground to the north")
			if mid[y_pos][x_pos+1]=="u":#open sky(top layer)basalt(mid layer)cave wall(underground) (untraversable)
				if layer=="top":
					print("You see open sky to the east")
				elif layer=="mid":
					print("You see a basalt cliff to the east")
				else:
					print("You see a cave wall to the east")
			if mid[y_pos][x_pos-1]=="u":
				if layer=="top":
					print("You see open sky to the west")
				elif layer=="mid":
					print("You see a basalt cliff to the west")
				else:
					print("You see a cave wall to the west")
			if mid[y_pos+1][x_pos]=="u":
				if layer=="top":
					print("You see open sky to the south")
				elif layer=="mid":
					print("You see a basalt cliff to the south")
				else:
					print("You see a cave wall to the south")
			if mid[y_pos-1][x_pos]=="u":
				if layer=="top":
					print("You see open sky to the north")
				elif layer=="mid":
					print("You see a basalt cliff to the north")
				else:
					print("You see a cave wall to the north")
			if mid[y_pos][x_pos+1]=="p":
				print("You see a feald to the east")
			if mid[y_pos][x_pos-1]=="p":
				print("You see a feald to the west")
			if mid[y_pos+1][x_pos]=="p":
				print("You see a feald to the south")
			if mid[y_pos-1][x_pos]=="p":
				print("You see a feald to the north")
			print("Choose from north, south, east, west")
			while True:
				choice=util_functions.get_valid_type(str,"Choose direction: ","that is not a valid direction",["north","south","east","west"])
				if choice=="north":
					y_pos-=1
				elif choice=="south":
					y_pos+=1
				elif choice=="east":
					x_pos+=1
				elif choice=="west":
					x_pos-=1
				# normalize token for location_dict lookup (strip digits and handle synonyms)
				token = mid[y_pos][x_pos]
				# strip trailing digits (e.g., i1 -> i)
				if isinstance(token, str):
					while len(token)>0 and token[-1].isdigit():
						token = token[:-1]
					# map 'p' (field shorthand) to 'f' key
					if token == 'p':
						token = 'f'
				# guard against missing keys
				loc_info = location_dict.get(token, {"description":None, "special":None})
				if process_position(x_pos,y_pos,loc_info["description"],loc_info["special"],None)["position"]=="illegal":
					print("You cant go that way")
					if choice=="north":
						y_pos+=1
					elif choice=="south":
						y_pos-=1
					elif choice=="east":
						x_pos-=1
					elif choice=="west":
						x_pos+=1
				else:
					break
			# build normalized location info for current tile
			token = mid[y_pos][x_pos]
			if isinstance(token, str):
				while len(token)>0 and token[-1].isdigit():
					token = token[:-1]
				if token == 'p':
					token = 'f'
			loc_info = location_dict.get(token, {"description":None, "special":None})
			location = process_position(x_pos,y_pos,loc_info["description"],loc_info["special"],None)
			battle_chance += monster_spawn_rate*10
			num = random.randint(1,100)
			# trigger battle when random number is within chance
			if num <= battle_chance:
				monster_list = get_random_monsters(party.level,location)
				monster_team = setup_enemy_party(monster_list)
				while len(monster_team.hp) > 0 and len(party.get_continuous_players()) > 0:
					party.attack(True, party.get_continuous_players(), monster_team, inventory)
					party.attack(False, party.get_continuous_players(), monster_team, inventory)
				while party.xp>=25:
					party.level_up(1)
					party.level_up(2)
					party.level_up(3)
					party.xp-=25
	else:
		print("Goodbye")