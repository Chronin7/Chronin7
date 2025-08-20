#dnd charicter sheat (its a nitemare but you know what is hapaning)
age=0
str=0
def stat_len_mod(size="",data=""):
	length=len(size)-len(data)
	out=data
	for x in range(0,length):
		out=out+"_"
	return out
#add this to all nums
"stat_len_mod("""
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
[  {stat_len_mod("__",strengthmod)}  ] {chr(123)}   {stat_len_mod("__",insperation)}   INSPIRATION         {chr(125)}  )   AC   ( | INITIATIVE | |   SPEED   |
[ ({stat_len_mod("__",strength)}) ] {chr(123)}   {stat_len_mod("__",profishansy)}   PROFICIENCY BONUS   {chr(125)}  |   {stat_len_mod("__",ac)}   | |    {stat_len_mod("____",initative)}    | |   {stat_len_mod("__",speed)} ft   |
{chr(92)}{chr(92)}<''>// {chr(123)}                            {chr(125)}   {chr(92)}      /  |{chr(92)}          /| |{chr(92)}         /|
/------{chr(92)}  '--------------------------'     `-.,-`   '------------' '-----------'
| DEX: |  .--------------------------.    .-----------------------------------.
[  {stat_len_mod("__",dexmod)}  ] {chr(123)}       SAVING  THROWS       {chr(125)}  {chr(123)} HIT POINTS:  [**********]  __ / __  {chr(125)}
[ ({stat_len_mod("__",dex)}) ] {chr(123)} {stat_len_mod("_",strengthmod+profishansy)} STR {stat_len_mod("__",strength)}  .:/{chr(92)}:.  {stat_len_mod("__",intelegance)} INT {stat_len_mod("_",intelegancemod+profishansy)} {chr(125)}  {chr(123)} TEMP HIT POINTS:{stat_len_mod("                    ",temphp)}{chr(125)}
{chr(92)}~:><:~/ | {stat_len_mod("_",dexmod+profishansy)} DEX {stat_len_mod("__",dex)} :{chr(92)}/20{chr(92)}/: {stat_len_mod("__",wis)} WIS {stat_len_mod("_",wismod+profishansy)} |   '-----------------------------------'
/------{chr(92)} {chr(123)} {stat_len_mod("_",conmod+profishansy)} CON {stat_len_mod("__",con)} :/{chr(92)}``/{chr(92)}: {stat_len_mod("__",cha)} CHA {stat_len_mod("_",chamod+profishansy)} {chr(125)}{chr(125)}  .-------------. .---------------------.
| CON: | {chr(123)}          `._{chr(92)}/_.'          {chr(125)}  |/           {chr(92)}| |/                   {chr(92)}|
[  {stat_len_mod("__",conmod)}  ]  '--------------------------'   |  HIT DICE   | |     DEATH SAVES     |
[ ({stat_len_mod("__",con)}) ]  .--------------------------.   |   {stat_len_mod("  ___  ",hitdice)}   | |  < - - - + - - - >  |
{chr(92)}_{chr(92)}()/_/ {chr(123)}           SKILLS           {chr(125)}  |{chr(92)}           /| |{chr(92)} death        life /|
/------{chr(92)} {chr(123)} {stat_len_mod("_",acrobaticsprof)} Acrobatics      {stat_len_mod("__",acrobatics)} (dex) {chr(125)}  '-------------' '---------------------'
| INT: | | {stat_len_mod("_",animalprof)} Animal Handling {stat_len_mod("__",animal)} (wis) |   .-----------------------------------.
[  {stat_len_mod("__",intelegancemod)}  ] | {stat_len_mod("_",arcanaprof)} Arcana          {stat_len_mod("__",arcana)} (int) |  {chr(123)}       ATTACKS & SPELLCASTING        {chr(125)}
[ ({stat_len_mod("__",intelegance)}) ] | {stat_len_mod("_",athleticsprof)} Athletics       {stat_len_mod("__",athletics)} (str) |  {chr(123)} {stat_len_mod("___________________________________",weponl1)} {chr(125)}
{chr(92)}+/{chr(125)}{chr(123)}{chr(92)}+/ | {stat_len_mod("_",deseptionprof)} Deception       {stat_len_mod("__",deseption)} (cha) |  | {stat_len_mod("___________________________________",weponl2)} |
/------{chr(92)} | {stat_len_mod("_",historyprof)} History         {stat_len_mod("__",history)} (int) |  | {stat_len_mod("___________________________________",weponl3)} |
| WIS: | | {stat_len_mod("_",insightprof)} Insight         {stat_len_mod("__",insight)} (wis) |  | {stat_len_mod("___________________________________",weponl4)} |
[  {stat_len_mod("__",wismod)}  ] | {stat_len_mod("_",intimidationprof)} Intimidation    {stat_len_mod("__",intimidation)} (cha) |  | {stat_len_mod("___________________________________",weponl5)} |
[ ({stat_len_mod("__",wis)}) ] | {stat_len_mod("_",investigationprof)} Investigation   {stat_len_mod("__",investigation)} (int) |  | {stat_len_mod("___________________________________",weponl6)} |
{chr(92)}+_/{chr(92)}_+/ | {stat_len_mod("_",medesenprof)} Medicine        {stat_len_mod("__",medicine)} (wis) |  | {stat_len_mod("___________________________________",weponl7)} |
/------{chr(92)} | {stat_len_mod("_",natureprof)} Nature          {stat_len_mod("__",nature)} (int) |  | {stat_len_mod("___________________________________",weponl8)} |
| CHA: | | {stat_len_mod("_",preseptionprof)} Perception      {stat_len_mod("__",preseption)} (wis) |  | {stat_len_mod("___________________________________",weponl9)} |
[  {stat_len_mod("__",chamod)}  ] | {stat_len_mod("_",preformanceprof)} Performance     {stat_len_mod("__",preformance)} (cha) |  | {stat_len_mod("___________________________________",weponl10)} |
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
| {stat_len_mod("___________________________________",profl1)} |  [ HEIGHT: {stat_len_mod("___________________________",hight)} ]
| {stat_len_mod("___________________________________",profl1)} |  [ WEIGHT: {stat_len_mod("___________________________",weight)} ]
| {stat_len_mod("___________________________________",profl1)} |  [   EYES: {stat_len_mod("___________________________",eyes)} ]
| {stat_len_mod("___________________________________",profl1)} |  [   SKIN: {stat_len_mod("___________________________",skin)} ]
| {stat_len_mod("___________________________________",profl1)} |  [   HAIR: {stat_len_mod("___________________________",hair)} ]
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
| * {stat_len_mod("",racetrate)}
| Subrace ({stat_len_mod("_____",subrace)}):
| * {stat_len_mod("",subracetrate)}
| Background ({stat_len_mod("_____",backround)}):
| * {stat_len_mod(""backroundtrate)}
| Class ({stat_len_mod("_____",classs)}):
| * {stat_len_mod("",classtrate)}
| Level 1:
| * {stat_len_mod("",lv1trate)}
| Level 2
| * {stat_len_mod("",lv2trate)}
| Level 3
| * {stat_len_mod("",lv3trate)}
| Level 4
| * {stat_len_mod("",lv4trate)}
| Level 5
| * {stat_len_mod("",lv5trate)}
| Level 6
| * {stat_len_mod("",lv6trate)}
| Level 7
| * {stat_len_mod("",lv7trate)}
| Level 8
| * {stat_len_mod("",lv8trate)}
| Level 9
| * {stat_len_mod("",lv9trate)}
*------------------------------------------------------------------------------*
|                                                    PERSONAL CHARACTERISTICS
| Personality traits:
| * {stat_len_mod("",personalitytrate)}
| Ideals:
| * {stat_len_mod("",ideals)}
| Bonds:
| * {stat_len_mod("",bonds)}
| Flaws:
| * {stat_len_mod("",flaws)}
*------------------------------------------------------------------------------*
|                                                                   BACKSTORY
| * {stat_len_mod("",backstory)}
| 
*                                                                              *
'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
""")
print(stat_len_mod("_____________","5"))
pp()
