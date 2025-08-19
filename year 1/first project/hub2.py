age=0
gen=""
hight=""
whegit=""
eyes=""
skin=""
hair=""
weponsarmor=[]
loot=[]
cash=[]
spells0=[]
spells1=[]
spells2=[]
spells3=[]
spells4=[]
spells5=[]
spells6=[]
spells7=[]
spells8=[]
spells9=[]
stran=0
dex=0
con=0
intel=0
wis=0
cha=0
paswis=0
name="joe"
plyname=""
race=""
subrace=""
backr=""
alig=""
classs=""
lvl=1
exp=0
ac=0
initiative=0
speed=0
hpd=""
deathsave=["O","O","O","|","O","O","O"]
insperation=0
profbomn=0
temphp=0
hp=0
strs=0
ints=0
cons=0
wiss=0
chas=0
aacro=0
anim=0
arcana=0
athletics=0
decep=0
history=0
insight=0
intimidation=0
medisin=0
nature=0
perception=0
performance=0
religion=0
slihtohand=0
stealth=0
stats=['0', '""', '""', '""', '""', '""', '""', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '0', '0', '0', '0', '0', '0', '0', '""', '""', '""', '""', '""', '""', '""', '1', '0', '0', '0', '0', '""', '["O","O","O","|","O","O","O"]', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',"0"]
class Format:
	end = '\033[0m'
	underline = '\033[4m'
def pc():
	it=-1
	for x in ['age', 'gen', 'hight', 'whegit', 'eyes', 'skin', 'hair', 'weponsarmor', 'loot', 'cash', 'spells0', 'spells1', 'spells2', 'spells3', 'spells4', 'spells5', 'spells6', 'spells7', 'spells8', 'spells9', 'stran', 'dex', 'con', 'intel', 'wis', 'cha', 'paswis', 'name', 'plyname', 'race', 'subrace', 'backr', 'alig', 'classs', 'lvl', 'exp', 'ac', 'initiative', 'speed', 'hpd', 'deathsave', 'insperation', 'profbomn', 'temphp', 'hp', 'strs', 'ints', 'cons', 'wiss', 'chas', 'aacro', 'anim', 'arcana', 'athletics', 'decep', 'history', 'insight', 'intimidation', 'medisin', 'nature', 'perception', 'performance', 'religion', 'slihtohand', 'stealth']:
		print(x,end=": ")
		it+=1
		print(stats[it])
it=-1
pc()









def pp():
	global age
	global gen
	global hight
	global whegit
	global eyes
	global skin
	global hair
	global weponsarmor
	global loot
	global cash
	global spells0
	global spells1
	global spells2
	global spells3
	global spells4
	global spells5
	global spells6
	global spells7
	global spells8
	global spells9
	global stran
	global dex
	global con
	global intel
	global wis
	global cha
	global paswis
	global name
	global plyname
	global race
	global subrace
	global backr
	global alig
	global classs
	global lvl
	global exp
	global ac
	global initiative
	global speed
	global hpd
	global deathsave
	global insperation
	global profbomn
	global temphp
	global hp
	global strs
	global ints
	global cons
	global wiss
	global chas
	global aacro
	global anim
	global arcana
	global athletics
	global decep
	global history
	global insight
	global intimidation
	global medisin
	global nature
	global perception
	global performance
	global religion
	global slihtohand
	global stealth

	print(f"""
        ,),,)
      {chr(92)}'     ',)
     ,`  ,--.  ',  ,                        /------.___________________,------{chr(92)}
     :  /    {chr(125)}  G{chr(125)}'   DUNGEONS & DRAGONS   [ PLAYER NAME: {name} ]
    ',  {chr(92)}    ',,V     5E CHARACTER SHEET   [        RACE: ____________________ ]
    _{chr(92)}___{chr(92)}____;;l________________________  [  BACKGROUND: ____________________ ]
  _/          ';/  CHARACTER NAME       {chr(92)}{chr(92)} [   ALIGNMENT: ____________________ ]
 //| {name}  {chr(92)}{chr(92)}[ CLASS: ________________ LEVEL: __ ]
// ;                       ,---.      ,  //[ EXPERIENCE POINTS: ______________ ]
{chr(92)}{chr(92)} {chr(92)}______________________/  _  {chr(92)}___,'/_//  {chr(92)}______,-------------------.______/ 
 {chr(92)}{chr(92)}_'/            VZ{chr(92)}  `'  /  {chr(92)}  `.' /  
/------{chr(92)}         +FAR`.__,'    `.__,'       _.._    .------------. .-----------.
| STR: |  .--------------------------.    _/    {chr(92)}_  |/          {chr(92)}| |/         {chr(92)}|
[  __  ] {chr(123)}   __   INSPIRATION         {chr(125)}  )   AC   ( | INITIATIVE | |   SPEED   |
[ (__) ] {chr(123)}   __   PROFICIENCY BONUS   {chr(125)}  |   __   | |    ____    | |   __ ft   |
{chr(92)}{chr(92)}<''>// {chr(123)}                            {chr(125)}   {chr(92)}      /  |{chr(92)}          /| |{chr(92)}         /|
/------{chr(92)}  '--------------------------'     `-.,-`   '------------' '-----------'
| DEX: |  .--------------------------.    .-----------------------------------.
[  __  ] {chr(123)}       SAVING  THROWS       {chr(125)}  {chr(123)} HIT POINTS:  [**********]  __ / __  {chr(125)}
[ (__) ] {chr(123)} _ STR __  .:/{chr(92)}:.  __ INT _ {chr(125)}  {chr(123)} TEMP HIT POINTS:                    {chr(125)}
{chr(92)}~:><:~/ | _ DEX __ :{chr(92)}/20{chr(92)}/: __ WIS _ |   '-----------------------------------'
/------{chr(92)} {chr(123)} _ CON __ :/{chr(92)}``/{chr(92)}: __ CHA _ {chr(125)}{chr(125)}  .-------------. .---------------------.
| CON: | {chr(123)}          `._{chr(92)}/_.'          {chr(125)}  |/           {chr(92)}| |/                   {chr(92)}|
[  __  ]  '--------------------------'   |  HIT DICE   | |     DEATH SAVES     |
[ (__) ]  .--------------------------.   |     ___     | |  < - - - + - - - >  |
{chr(92)}_{chr(92)}()/_/ {chr(123)}           SKILLS           {chr(125)}  |{chr(92)}           /| |{chr(92)} death        life /|
/------{chr(92)} {chr(123)} _ Acrobatics      __ (dex) {chr(125)}  '-------------' '---------------------'
| INT: | | _ Animal Handling __ (wis) |   .-----------------------------------.
[  __  ] | _ Arcana          __ (int) |  {chr(123)}       ATTACKS & SPELLCASTING        {chr(125)}
[ (__) ] | _ Athletics       __ (str) |  {chr(123)} ___________________________________ {chr(125)}
{chr(92)}+/{chr(125)}{chr(123)}{chr(92)}+/ | _ Deception       __ (cha) |  | ___________________________________ |
/------{chr(92)} | _ History         __ (int) |  | ___________________________________ |
| WIS: | | _ Insight         __ (wis) |  | ___________________________________ |
[  __  ] | _ Intimidation    __ (cha) |  | ___________________________________ |
[ (__) ] | _ Investigation   __ (int) |  | ___________________________________ |
{chr(92)}+_/{chr(92)}_+/ | _ Medicine        __ (wis) |  | ___________________________________ |
/------{chr(92)} | _ Nature          __ (int) |  | ___________________________________ |
| CHA: | | _ Perception      __ (wis) |  | ___________________________________ |
[  __  ] | _ Performance     __ (cha) |  | ___________________________________ |
[ (__) ] | _ Persuasion      __ (cha) |  | ___________________________________ |
{chr(92)}"{chr(123)}--{chr(125)}"/ | _ Religion        __ (int) |  | ___________________________________ |
/------{chr(92)} | _ Sleight of Hand __ (dex) |  | ___________________________________ |
| PAS. | | _ Stealth         __ (dex) |  {chr(123)} ___________________________________ {chr(125)}
[ WIS: ] {chr(123)} _ Survival        __ (wis) {chr(125)}  {chr(123)}                                     {chr(125)}
[  __  ] {chr(123)}                            {chr(125)}   '-----------------------------------'
{chr(92)}::[]::/  '--------------------------'    /------._____________________,------{chr(92)}
+-------------------------------------+  [              APPEARANCE             ]
|   OTHER PROFICIENCIES & LANGUAGES   |  [    AGE: ___________________________ ]
| ___________________________________ |  [ GENDER: ___________________________ ]
| ___________________________________ |  [ HEIGHT: ___________________________ ]
| ___________________________________ |  [ WEIGHT: ___________________________ ]
| ___________________________________ |  [   EYES: ___________________________ ]
| ___________________________________ |  [   SKIN: ___________________________ ]
| ___________________________________ |  [   HAIR: ___________________________ ]
+-------------------------------------+   {chr(92)}______,---------------------.______/ 
*------------------------------------------------------------------------------*
|                                                                   EQUIPMENT
| Belt Pouch:
| * 
| Clothing:
| * 
| Weapons & Armor:
| * 
| Backpack:
| * 
| Strapped to backpack:
| * 
| ...
*------------------------------------------------------------------------------*
|                                                                      SPELLS
| Cantrips:
| * 
| Level 1 (__ slots):
| * 
| ...
*------------------------------------------------------------------------------*
|                                                           FEATURES & TRAITS
| Race (_____):
| * 
| Subrace (_____):
| * 
| Background (_____):
| * 
| Class (_____):
| * 
| Level 1:
| * 
| ...
*------------------------------------------------------------------------------*
|                                                    PERSONAL CHARACTERISTICS
| Personality traits:
| * 
| * 
| Ideals:
| * 
| Bonds:
| * 
| Flaws:
| * 
| ...
*------------------------------------------------------------------------------*
|                                                                   BACKSTORY
| * 
| ...
*                                                                              *
'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
""")
pp()