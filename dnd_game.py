#lp combaty 1
import random,math,time
level=1
class Fighter:
    def __init__(self):
        self.max_hp=30
        self.hp=30
        self.ac=13
        self.heal_count=15
        self.speshal_atakc_mana_cost=10
        self.bonus=0
        self.mana=0
    def level_up(self):
        self.max_hp+=30
        self.hp=self.max_hp
        self.ac+=1
        self.heal_count=15
        self.bonus+=10
    def norm_atack(self):
        print("you do your normail atack")
        self.mana+=3
        return dice(6,2,self.bonus)
    def speshail_atack(self):
        print("you do your speshil atack")
        self.mana+=3
        return dice(6,3,self.bonus)
class Barbarean:
    def __init__(self):
        self.max_hp=40
        self.hp=40
        self.ac=15
        self.heal_count=5
        self.speshal_atakc_mana_cost=15
        self.bonus=0
        self.mana=0
    def level_up(self):
        self.max_hp+=100
        self.hp=self.max_hp
        self.ac+=1
        self.heal_count=5
        self.bonus+=30
    def norm_atack(self):
        print("you do your normail atack")
        self.mana+=3
        return dice(12,2,self.bonus)
    def speshail_atack(self):
        print("you do your speshil atack")
        self.mana+=3
        return dice(12,3,self.bonus)
class Mage:
    def __init__(self):
        self.max_hp=20
        self.hp=20
        self.atack=200
        self.ac=14
        self.heal_count=20
        self.speshal_atakc_mana_cost=50
        self.bonus=0
        self.mana=25
    def level_up(self):
        self.max_hp+=50
        self.hp=self.max_hp
        self.atack+=10
        self.ac+=1
        self.heal_count=20
        self.bonus+=10
    def norm_atack(self):
        print("you do your normail atack")
        self.mana+=10
        return dice(4,5,self.bonus)
    def speshail_atack(self):
        print("you do your speshil atack")
        self.mana+=10
        return dice(6,8,self.bonus)
class Rouge:
    def __init__(self):
        self.max_hp=15
        self.hp=15
        self.ac=15
        self.heal_count=15
        self.speshal_atakc_mana_cost=13
        self.bonus=0
        self.mana=0
    def level_up(self):
        self.max_hp+=5
        self.hp=self.max_hp
        self.ac+=1
        self.heal_count=15
        self.bonus+=5
    def norm_atack(self):
        print("you do your normail atack")
        self.mana+=3
        return dice(6,2,self.bonus)
    def speshail_atack(self):
        print("you do your speshil atack")
        self.mana+=3
        return dice(16,2,self.bonus)
class Debuger:
    def __init__(self):
        self.max_hp=10000
        self.hp=10000
        self.ac=10000
        self.heal_count=10000
        self.speshal_atakc_mana_cost=0
        self.bonus=0
        self.mana=0
    def level_up(self):
        self.max_hp+=100
        self.hp=self.max_hp
        self.ac+=1
        self.heal_count=15
        self.bonus+=5
    def norm_atack(self):
        print("you do your normail atack")
        self.mana+=3
        return dice(15,15,self.bonus)
    def speshail_atack(self):
        print("you do your speshil atack")
        self.mana+=3
        return dice(15,15,self.bonus)
class xp_dude:
    def __init__(self):
        self.hp=1
        self.ac=1
        self.xp=persentage(10,level**level)
        self.atack=0
    def name(self):
        return "HOW DARE YOU USE MY OWN DEBUGGING FEATURES AGENST ME"
class Dragon:
    def __init__(self):
        self.hp=persentage(15,level)
        self.ac=persentage(16,level)
        self.xp=dice(10,3,0,5)
        self.atack=persentage(10,level)
    def name(self):
        return "dragon"
class Goblin:
    def __init__(self):
        self.hp=persentage(5,level)
        self.ac=persentage(10,level)
        self.xp=dice(3,1,0,1)
        self.atack=persentage(3,level)
    def name(self):
        return "goblin"
class Vampier:
    def __init__(self):
        self.hp=persentage(20,level)
        self.ac=persentage(15,level)
        self.xp=dice(7,3,0,4)
        self.atack=persentage(5,level)
    def name(self):
        return "vampier"
class Beholder:
    def __init__(self):
        self.hp=persentage(25,level)
        self.ac=persentage(19,level)
        self.xp=dice(15,2,0,10)
        self.atack=persentage(10,level)
    def name(self):
        return "beholder"
class Cyclops:
    def __init__(self):
        self.hp=persentage(30,level)
        self.ac=persentage(8,level)
        self.xp=dice(6,3,0,2)
        self.atack=persentage(10,level)
    def name(self):
        return "cyclops"
class Worm:
    def __init__(self):
        self.hp=persentage(50,level)
        self.ac=persentage(18,level)
        self.xp=dice(30,5,0,15)
        self.atack=persentage(15,level)
    def name(self):
        return "worm"
class Mimic:
    def __init__(self):
        self.hp=persentage(5,level)
        self.ac=persentage(5,level)
        self.xp=dice(4,3,0,1)
        self.atack=persentage(2,level)
    def name(self):
        return "mimic"
class Skeleton:
    def __init__(self):
        self.hp=persentage(10,level)
        self.ac=persentage(10,level)
        self.xp=dice(3,2,0,2)
        self.atack=persentage(10,level)
    def name(self):
        return "skeleton"
class Tarrasque:
    def __init__(self):
        self.hp=persentage(100,level)
        self.ac=persentage(20,level)
        self.xp=dice(100,10,0,50)
        self.atack=persentage(30,level)
    def name(self):
        return "Tarrasque"
class Troll:
    def __init__(self):
        self.hp=persentage(12,level)
        self.ac=persentage(14,level)
        self.xp=dice(3,3,0,1)
        self.atack=persentage(9,level)
    def name(self):
        return "troll"
class Zombie:
    def __init__(self):
        self.hp=persentage(1,level)
        self.ac=persentage(1,level)
        self.xp=dice(2,1,0,1)
        self.atack=persentage(1,level)
    def name(self):
        return "zombie"
def persentage(hole,part):
    return int((part/hole)*100)
def dice(upper_bound,count,bonus,lowwer_bound=1):
    for x in range(0,count):
        bonus+=random.randint(lowwer_bound,upper_bound)
    return bonus
def heal(heath,total_heal,max_heal):
    heal_amount=random.randint(1,persentage(4,level))+random.randint(1,persentage(4,level))+random.randint(1,persentage(4,level))
    heal_amount=min(max_heal,heal_amount)
    print(f"you healed {heal_amount}, your hp is now {heath+heal_amount}, you have {total_heal-1} heals left")
    return heath+heal_amount,total_heal-1
def get_random_word():
    return ["destroyed","murdered","dispatched","slaughtered","slew","assassinated","felled","carried off","wasted","croaked","executed","neutralized","massacred","did in","did for","finished","did away with","made away with","butchered","snuffed","annihilated","decimated","cut down","whacked","terminated","killed off","put away","smote","rubbed out","mowed","blotted out","knocked off","took out","euthanized","bumped off","scragged","euthanized","put down","unalived"][random.randint(0,38)] #494 chars
xp=0
def print_stats(class_chosen):
    print(f"""
__________your stats__________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
[][][][][][][][][][][][][][][]
|                            |
| hp: {class_chosen.hp}             
|                            |
| max hp: {class_chosen.max_hp}
|                            |
| ac: {class_chosen.ac}   
|                            |
| heals left: {class_chosen.heal_count}      
|                            |
| special atack cost: {class_chosen.speshal_atakc_mana_cost}
|                            |
| mana: {class_chosen.mana}
|                            |
| damage bonus: {class_chosen.bonus}
|                            |
| level: {level}
|                            |
[][][][][][][][][][][][][][][]
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
===press enter to continue===""")
    input()
    return

def combat(monster_class,class_chosen):
    global xp
    global level
    monster = monster_class()
    monster_name=monster.name()
    turn = random.randint(1,2)
    while class_chosen.hp > 0 and monster.hp > 0:
        if turn ==1:
            while True:
                print(f"""
______choose your atack______
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
[][][][][][][][][][][][][][][]
|                            |
|     1 for heal             |
|                            |
|     2 for normal atack     |
|                            |
|     3 for special atack    |
|     cost:{class_chosen.speshal_atakc_mana_cost}    
|     mana:{class_chosen.mana}                   
|     4 to check stats       |
|                            |
[][][][][][][][][][][][][][][]
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
==============================
""",end="",flush=True)
                choise=input("\r")
                if choise in ["1","2","4"] or (choise=="3" and class_chosen.mana>class_chosen.speshal_atakc_mana_cost):
                    if choise=="2":
                        damage=class_chosen.norm_atack()
                        print(f" and deal {damage}")
                    if choise=="3" and class_chosen.mana>=class_chosen.speshal_atakc_mana_cost:
                        damage=class_chosen.speshail_atack()
                        print(f" and deal {damage}")
                        class_chosen.mana-=class_chosen.speshal_atakc_mana_cost
                    if choise=="1" and class_chosen.heal_count>0:
                        class_chosen.hp,class_chosen.heal_count=heal(class_chosen.hp,class_chosen.heal_count,class_chosen.max_hp)
                    turn=2
                    monster.hp-=damage
                    if monster.hp<0:
                        print(f"the {monster_name} has been {get_random_word()}")
                        xp+=monster.xp
                        while xp>(persentage(10,level)):
                            xp=xp-persentage(10,level)
                            level+=1
                            class_chosen.level_up()
                            print("you leveled up")
                        return
                    if choise=="4":
                        print_stats(class_chosen)
                    else:
                        break
                if choise=="4":
                    print_stats(class_chosen)
        print(f"you have {class_chosen.hp} hp left")
        print(f"the {monster_name} has {monster.hp} hp left")
        if turn==2 and monster.hp>0:
            print(f"the {monster_name} atacks ",end="")
            if dice(20,1,persentage(1,level))>=class_chosen.ac:
                if monster.name()=="HOW DARE YOU USE MY OWN DEBUGGING FEATURES AGENST ME":
                    damage=0
                else:
                    damage=dice(monster.atack,level,0)
                class_chosen.hp-=damage
                turn=1
                print(f"you take {damage} damage ",end="")
            else:
                print(f"the {monster_name} misses ")
            if class_chosen.hp<0:
                print("you have... oh no. You died")
                return
            print(f"you have {class_chosen.hp} hp left")
        else:
            print(f"the {monster_name} has been {get_random_word()}")
            xp+=monster.xp
            while xp>(persentage(10,level)):
                xp=xp-persentage(10,level)
                level+=1
                class_chosen.level_up()
                print("you leveled up")
            return
def main():
    dificulty=input("hard mode (y/n): ")=="y"
    choise=0
    while choise not in ["1","2","3","4","67"]:
        print("""
______choose your class______
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
[][][][][][][][][][][][][][][]
|                            |
|      1 for Fighter         |
|                            |
|     2 for Barbarian        |
|                            |
|       3 for Mage           |
|                            |
|       4 for Rouge          |
|                            |
[][][][][][][][][][][][][][][]
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
==============================
              {}  {}  {}  {}  """,end="",flush=True)
        choise=input("\r")
    if choise=="1":
        class_chosen=Fighter()
    elif choise=="2":
        class_chosen=Barbarean()
    elif choise=="3":
        class_chosen=Mage()
    elif choise=="4":
        class_chosen=Rouge()
    elif choise=="67":
        class_chosen=Debuger()
    while class_chosen.hp>0:
        choise=0
        while choise not in ["1","2","3","4"]:
            print("""
______choose your move_______
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
[][][][][][][][][][][][][][][]
|                            |
|    1 to fight monster      |
|                            |
|        2 to heal           |
|                            |
|    3 to check stats        |
|                            |
|        4 to quit           |
|                            |
[][][][][][][][][][][][][][][]
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
==============================
              {}  {}  {}  {}  """,end="",flush=True)
            choise=input("\r")
        if choise=="1":
            choise=0
            if dificulty==False:
                while choise not in ["1","2","3","4","5","6","7","8","9","10","11","12","13"]:
                    print("""
    _____choose your oponent______
    |XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
    [][][][][][][][][][][][][][][]
    |                            |
    |    1 to fight a Dragon     |
    |                            |
    |    2 to fight a Goblin     |
    |                            |
    |    3 to fight a Vampier    |
    |                            |
    |    4 to fight a Beholder   |
    |                            |
    |    5 to fight a Cyclops    |
    |                            |
    |    6 to fight a Worm       |
    |                            |
    |    7 to fight a Mimic      |
    |                            |
    |    8 to fight a Skeleton   |
    |                            |
    |    9 to fight the Tarrasque|
    |                            |
    |    10 to fight a Troll     |
    |                            |
    |    11 to fight a Zombie    |
    |                            |
    |    12 to return            |
    |                            |
    [][][][][][][][][][][][][][][]
    |XXXXXXXXXXXXXXXXXXXXXXXXXXXX|
    ==============================
                {}  {}  {}  {}  """,end="",flush=True)
                    choise=input("\r")
                    if choise !="12":
                        monsters = ["a Dragon.", "a Goblin.", "a Vampier.", "a Beholder.", "a Cyclops.","a Worm.", "a Mimic.", "a Skeleton.", "the Tarrasque.", "a Troll.","a Zombie.",None,"a enemy that has no name"]
                        print(f"you will now fight {monsters[int(choise) - 1]}")
                        monster=[Dragon,Goblin,Vampier,Beholder,Cyclops,Worm,Mimic,Skeleton,Tarrasque,Troll,Zombie,None,xp_dude][int(choise)-1]
                        if 1==1:
                            combat(monster,class_chosen)
                    else:
                        pass
            else:
                monster=[Dragon,Goblin,Vampier,Beholder,Cyclops,Worm,Mimic,Skeleton,Tarrasque,Troll,Zombie,None,xp_dude][random.randint(0,10)]
                print(f"you will fight a {monster.name(monster)}")
                combat(monster,class_chosen)
        if choise=="2" and class_chosen.heal_count>0:
            class_chosen.hp,class_chosen.heal_count=heal(class_chosen.hp,class_chosen.heal_count,class_chosen.max_hp)
        if choise=="3":
            print_stats(class_chosen)
        if choise=="4":
            print("goodbye")
            quit()
if __name__=="__main__":
    main()

