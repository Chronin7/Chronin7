
#dnd charicter sheat (its a nitemare but you know what is hapaning)
import random, time
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
name=""
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
def stat_len_mod(size,data):
	length=len(size)-len(str(data))
	out=str(data)
	for x in range(0,length):
		out=out+"_"
	return out
#change the addition vars
def pp():
	print(f"""
        ,),,)
      {chr(92)}'     ',)
     ,`  ,--.  ',  ,                        /------.___________________,------{chr(92)}
     :  /    {chr(125)}  G{chr(125)}'   DUNGEONS & DRAGONS   [ PLAYER NAME: {stat_len_mod("____________________",player_name)} ]
    ',  {chr(92)}    ',,V     5E CHARACTER SHEET   [        RACE: {stat_len_mod("____________________",race)} ]
    _{chr(92)}___{chr(92)}____;;l________________________  [  BACKGROUND: {stat_len_mod("____________________",backround)} ]
  _/          ';/  CHARACTER NAME       {chr(92)}{chr(92)} [   ALIGNMENT: {stat_len_mod("____________________",alingment)} ]
 //| {stat_len_mod("__________________________________",name)}  {chr(92)}{chr(92)}[ CLASS: {stat_len_mod("________________",classs)} LEVEL: {stat_len_mod("__",level)} ]
// ;                       ,---.      ,  //[ EXPERIENCE POINTS: {stat_len_mod("______________",xp)} ]
{chr(92)}{chr(92)} {chr(92)}______________________/  _  {chr(92)}___,'/_//  {chr(92)}______,-------------------.______/ 
 {chr(92)}{chr(92)}_'/            VZ{chr(92)}  `'  /  {chr(92)}  `.' /  
/------{chr(92)}         +FAR`.__,'    `.__,'       _.._    .------------. .-----------.
| STR: |  .--------------------------.    _/    {chr(92)}_  |/          {chr(92)}| |/         {chr(92)}|
[  {stat_len_mod("__","+"+str(strengthmod))}  ] {chr(123)}   {stat_len_mod("__",insperation)}   INSPIRATION         {chr(125)}  )   AC   ( | INITIATIVE | |   SPEED   |
[ ({stat_len_mod("__",strength)}) ] {chr(123)}   {stat_len_mod("__",profishansy)}   PROFICIENCY BONUS   {chr(125)}  |   {stat_len_mod("__",ac)}   | |    {stat_len_mod("____",initative)}    | |   {stat_len_mod("__",speed)} ft   |
{chr(92)}{chr(92)}<''>// {chr(123)}                            {chr(125)}   {chr(92)}      /  |{chr(92)}          /| |{chr(92)}         /|
/------{chr(92)}  '--------------------------'     `-.,-`   '------------' '-----------'
| DEX: |  .--------------------------.    .-----------------------------------.
[  {stat_len_mod("__","+"+str(dexmod))}  ] {chr(123)}       SAVING  THROWS       {chr(125)}  {chr(123)} HIT POINTS:  [**********]  {stat_len_mod("__",chp)} / {stat_len_mod("__",hp)}  {chr(125)}
[ ({stat_len_mod("__",dex)}) ] {chr(123)} {stat_len_mod("_",(strengthmod+profishansy))} STR {stat_len_mod("__",strength)}  .:/{chr(92)}:.  {stat_len_mod("__",intelegance)} INT {stat_len_mod("_",(intelegancemod+profishansy))} {chr(125)}  {chr(123)} TEMP HIT POINTS:{stat_len_mod("                    ",temphp)}{chr(125)}
{chr(92)}~:><:~/ | {stat_len_mod("_",(dexmod+profishansy))} DEX {stat_len_mod("__",dex)} :{chr(92)}/20{chr(92)}/: {stat_len_mod("__",wis)} WIS {stat_len_mod("_",(wismod+profishansy))} |   '-----------------------------------'
/------{chr(92)} {chr(123)} {stat_len_mod("_",(conmod+profishansy))} CON {stat_len_mod("__",con)} :/{chr(92)}``/{chr(92)}: {stat_len_mod("__",cha)} CHA {stat_len_mod("_",(chamod+profishansy))} {chr(125)}{chr(125)}  .-------------. .---------------------.
| CON: | {chr(123)}          `._{chr(92)}/_.'          {chr(125)}  |/           {chr(92)}| |/                   {chr(92)}|
[  {stat_len_mod("__","+"+str(conmod))}  ]  '--------------------------'   |  HIT DICE   | |     DEATH SAVES     |
[ ({stat_len_mod("__",con)}) ]  .--------------------------.   |   {stat_len_mod("  ___  ",hitdice)}   | |  < - - - + - - - >  |
{chr(92)}_{chr(92)}()/_/ {chr(123)}           SKILLS           {chr(125)}  |{chr(92)}           /| |{chr(92)} death        life /|
/------{chr(92)} {chr(123)} {stat_len_mod("_",acrobaticsprof)} Acrobatics      {stat_len_mod("__",acrobatics)} (dex) {chr(125)}  '-------------' '---------------------'
| INT: | | {stat_len_mod("_",animalprof)} Animal Handling {stat_len_mod("__",animal)} (wis) |   .-----------------------------------.
[  {stat_len_mod("__","+"+str(intelegancemod))}  ] | {stat_len_mod("_",arcanaprof)} Arcana          {stat_len_mod("__",arcana)} (int) |  {chr(123)}       ATTACKS & SPELLCASTING        {chr(125)}
[ ({stat_len_mod("__",intelegance)}) ] | {stat_len_mod("_",athleticsprof)} Athletics       {stat_len_mod("__",athletics)} (str) |  {chr(123)} {stat_len_mod("___________________________________",weponl1)} {chr(125)}
{chr(92)}+/{chr(125)}{chr(123)}{chr(92)}+/ | {stat_len_mod("_",deseptionprof)} Deception       {stat_len_mod("__",deseption)} (cha) |  | {stat_len_mod("___________________________________",weponl2)} |
/------{chr(92)} | {stat_len_mod("_",historyprof)} History         {stat_len_mod("__",history)} (int) |  | {stat_len_mod("___________________________________",weponl3)} |
| WIS: | | {stat_len_mod("_",insightprof)} Insight         {stat_len_mod("__",insight)} (wis) |  | {stat_len_mod("___________________________________",weponl4)} |
[  {stat_len_mod("__","+"+str(wismod))}  ] | {stat_len_mod("_",intimidationprof)} Intimidation    {stat_len_mod("__",intimidation)} (cha) |  | {stat_len_mod("___________________________________",weponl5)} |
[ ({stat_len_mod("__",wis)}) ] | {stat_len_mod("_",investigationprof)} Investigation   {stat_len_mod("__",investigation)} (int) |  | {stat_len_mod("___________________________________",weponl6)} |
{chr(92)}+_/{chr(92)}_+/ | {stat_len_mod("_",medesenprof)} Medicine        {stat_len_mod("__",medicine)} (wis) |  | {stat_len_mod("___________________________________",weponl7)} |
/------{chr(92)} | {stat_len_mod("_",natureprof)} Nature          {stat_len_mod("__",nature)} (int) |  | {stat_len_mod("___________________________________",weponl8)} |
| CHA: | | {stat_len_mod("_",preseptionprof)} Perception      {stat_len_mod("__",preseption)} (wis) |  | {stat_len_mod("___________________________________",weponl9)} |
[  {stat_len_mod("__","+"+str(chamod))}  ] | {stat_len_mod("_",preformanceprof)} Performance     {stat_len_mod("__",preformance)} (cha) |  | {stat_len_mod("___________________________________",weponl10)} |
[ ({stat_len_mod("__",cha)}) ] | {stat_len_mod("_",perswasonprof)} Persuasion      {stat_len_mod("__",perswason)} (cha) |  | {stat_len_mod("___________________________________",weponl11)} |
{chr(92)}"{chr(123)}--{chr(125)}"/ | {stat_len_mod("_",relegionprof)} Religion        {stat_len_mod("__",relegion)} (int) |  | {stat_len_mod("___________________________________",weponl12)} |
/------{chr(92)} | {stat_len_mod("_",slightofhandprof)} Sleight of Hand {stat_len_mod("__",slightofhand)} (dex) |  | {stat_len_mod("___________________________________",weponl13)} |
| PAS. | | {stat_len_mod("_",stelthprof)} Stealth         {stat_len_mod("__",stelth)} (dex) |  {chr(123)} {stat_len_mod("___________________________________",weponl14)} {chr(125)}
[ WIS: ] {chr(123)} {stat_len_mod("_",servivalprof)} Survival        {stat_len_mod("__",servival)} (wis) {chr(125)}  {chr(123)}                                     {chr(125)}
[  {stat_len_mod("__",paswis)}  ] {chr(123)}                            {chr(125)}   '-----------------------------------'
{chr(92)}::[]::/  '--------------------------'    /------._____________________,------{chr(92)}
+-------------------------------------+  [              APPEARANCE             ]
|   OTHER PROFICIENCIES & LANGUAGES   |  [    AGE: {stat_len_mod("___________________________",age)} ]
| {stat_len_mod("___________________________________",profl1)} |  [ GENDER: {stat_len_mod("___________________________",gender)} ]
| {stat_len_mod("___________________________________",profl2)} |  [ HEIGHT: {stat_len_mod("___________________________",hight)} ]
| {stat_len_mod("___________________________________",profl3)} |  [ WEIGHT: {stat_len_mod("___________________________",weight)} ]
| {stat_len_mod("___________________________________",profl4)} |  [   EYES: {stat_len_mod("___________________________",eyes)} ]
| {stat_len_mod("___________________________________",profl5)} |  [   SKIN: {stat_len_mod("___________________________",skin)} ]
| {stat_len_mod("___________________________________",profl6)} |  [   HAIR: {stat_len_mod("___________________________",hair)} ]
+-------------------------------------+   {chr(92)}______,---------------------.______/ 
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
| Level 1 ({stat_len_mod("__",lv1)} slots):
| * {stat_len_mod("",lv1spells)}
| Level 2 ({stat_len_mod("__",lv2)} slots):
| * {stat_len_mod("",lv2spells)}
| Level 3 ({stat_len_mod("__",lv3)} slots):
| * {stat_len_mod("",lv3spells)}
| Level 4 ({stat_len_mod("__",lv4)} slots):
| * {stat_len_mod("",lv4spells)}
| Level 5 ({stat_len_mod("__",lv5)} slots):
| * {stat_len_mod("",lv5spells)}
| Level 6 ({stat_len_mod("__",lv6)} slots):
| * {stat_len_mod("",lv6spells)}
| Level 7 ({stat_len_mod("__",lv7)} slots):
| * {stat_len_mod("",lv7spells)}
| Level 8 ({stat_len_mod("__",lv8)} slots):
| * {stat_len_mod("",lv8spells)}
| Level 9 ({stat_len_mod("__",lv9)} slots):
| * {stat_len_mod("",lv9spells)}
*------------------------------------------------------------------------------*
|                                                           FEATURES & TRAITS
| Race ({stat_len_mod("_____",race)}):
| * {stat_len_mod(" ",racetrate)}
| Subrace ({stat_len_mod("_____",subrace)}):
| * {stat_len_mod(" ",subracetrate)}
| Background ({stat_len_mod("_____",backround)}):
| * {stat_len_mod(" ",backroundtrate)}
| Class ({stat_len_mod("_____",classs)}):
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
"age", "name", "player_name", "race", "backround", "alingment", "classs", "xp", "level",
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
		"age", "name", "player_name", "race", "backround", "alingment", "classs", "xp", "level",
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
		age, name, player_name, race, backround, alingment, classs, xp, level,
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

while True:
	pp()
	choice=""
	unsued=""
	choice=input("""1 to change
2 to inport
3 to export
4 to roll dice
5 to quit: """)
	if choice=="2":
		inportsave(input("input the save here: "))
	if choice=="3":
		print(exportchar())
		unsued=input()
	if choice=="4":
		typeofdice=input("1 for disavantage roll, 2 for normal roll, 3 for advantage roll")
		countdice=int(input("input the number of dice: "))
		dicetype=int(input("what is the highest number that can be rolled on that dice type: "))
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
					print("YOU GOT A 20!")
		else:
			print(f"you got {result}")
			input()
	if choice=="5":
		quit()
	if choice=="1":
		print("""age
name
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
			print("ok noting is changed")
		else:
			changeto=input(f"change {globals_list[iteration]} to: ")
			if iteration==0:
				age=changeto
			if iteration==1:
				name=changeto
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
				backstory=changeto


			
			


#25,Kaelthar Emberfain,liam,Dragonborn,Soldier,Neutral Good,Ranger,0,1,2,15,0,2,16,2,13,13,30,3,16,14,2,12,1,12,1,10,0,0,Gold,0,1d10,5,1,0,3,0,2,0,2,1,15,0,0,Longbow (1d8+3 Piercing),Shortsword (1d6+3 Slashing),Dagger (1d4+3 Piercing),,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,13,Leather Armor,Explorer's Pack,Ranger's gear,,0,,,,,,,,,,,,,,,,,,Draconic Ancestry (Fire Breath),,Darkvision,Military Rank,monstrosotys,Primeval Awareness,,,,,,,,,,Brave,Always loyal to my allies,I fight for honor and freedom,My anger burns as hot as dragonfire,Kaelthar was born from an ancient draconic bloodline trained as a soldier before bonding with a drake companion. When the bond deepened his essence fused with the drake's granting him primal power and draconic might. He wanders the world seeking justice with dragonfire in his breath and the instincts of a hunter in his soul.