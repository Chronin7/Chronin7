#lp combaty 1
import random,math
level=1
class Fighter:
    def __init__(self):
        self.max_hp=15
        self.hp=15
        self.ac=13
        self.heal_count=15
        self.speshal_atakc_mana_cost=10
        self.bonus=0
        self.mana=0
    def level_up(self):
        self.hp+=10
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
        self.max_hp=30
        self.hp=30
        self.ac=15
        self.heal_count=5
        self.speshal_atakc_mana_cost=15
        self.bonus=0
        self.mana=0
    def level_up(self):
        self.hp+=15
        self.hp=self.max_hp
        self.ac+=1
        self.heal_count=5
        self.bonus+=10
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
        self.max_hp=8
        self.hp=8
        self.atack=40
        self.ac=14
        self.heal_count=20
        self.speshal_atakc_mana_cost=50
        self.bonus=0
        self.mana=25
    def level_up(self):
        self.hp+=10
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
        self.hp+=10
        self.hp=self.max_hp
        self.ac+=10
        self.heal_count=15
        self.bonus+=10
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
        self.hp+=10
        self.hp=self.max_hp
        self.ac+=10
        self.heal_count=15
        self.bonus+=10
    def norm_atack(self):
        print("you do your normail atack")
        self.mana+=3
        return dice(15,15,self.bonus)
    def speshail_atack(self):
        print("you do your speshil atack")
        self.mana+=3
        return dice(15,15,self.bonus)
class Dragon:
    def __init__(self):
        self.hp=persentage(15,level)
        self.ac=persentage(16,level)
        self.xp=dice(10,3,0,5)
        self.atack=persentage(10,level)
class Goblin:
    def __init__(self):
        self.hp=persentage(5,level)
        self.ac=persentage(10,level)
        self.xp=dice(3,1,0,1)
        self.atack=persentage(3,level)
class Vampier:
    def __init__(self):
        self.hp=persentage(20,level)
        self.ac=persentage(15,level)
        self.xp=dice(7,3,0,4)
        self.atack=persentage(5,level)
class Beholder:
    def __init__(self):
        self.hp=persentage(25,level)
        self.ac=persentage(19,level)
        self.xp=dice(15,2,0,10)
        self.atack=persentage(10,level)
class Cyclops:
    def __init__(self):
        self.hp=persentage(30,level)
        self.ac=persentage(8,level)
        self.xp=dice(6,3,0,2)
        self.atack=persentage(10,level)
class Worm:
    def __init__(self):
        self.hp=persentage(50,level)
        self.ac=persentage(18,level)
        self.xp=dice(30,5,0,15)
        self.atack=persentage(15,level)
class Mimic:
    def __init__(self):
        self.hp=persentage(5,level)
        self.ac=persentage(5,level)
        self.xp=dice(4,3,0,1)
        self.atack=persentage(2,level)
class Skeleton:
    def __init__(self):
        self.hp=persentage(10,level)
        self.ac=persentage(10,level)
        self.xp=dice(3,2,0,2)
        self.atack=persentage(10,level)
class Tarrasque:
    def __init__(self):
        self.hp=persentage(100,level)
        self.ac=persentage(20,level)
        self.xp=dice(100,10,0,50)
        self.atack=persentage(30,level)
class Troll:
    def __init__(self):
        self.hp=persentage(12,level)
        self.ac=persentage(14,level)
        self.xp=dice(3,3,0,1)
        self.atack=persentage(9,level)
class Zombie:
    def __init__(self):
        self.hp=persentage(1,level)
        self.ac=persentage(1,level)
        self.xp=dice(2,1,0,1)
        self.atack=persentage(1,level)

def persentage(hole,part):
    return int((part/hole)*100)
def dice(upper_bound,count,bonus,lowwer_bound=1):
    for x in range(0,count):
        bonus+=random.randint(lowwer_bound,upper_bound)
    return bonus
def heal(heath,total_heal,heal_amount=random.randint(1,4)+random.randint(1,4)+random.randint(1,4)):
    print(f"you healed {heal_amount}, your hp is now {heath+heal_amount}, you have {total_heal-1} heals left")
    return heath+heal_amount
def get_class_stat(num,stat):
    if num==1:
        class_choise=Fighter
    if num==2:
        class_choise=Barbarean
    if num==3:
        class_choise=Mage
    if num==4:
        class_choise=Rouge
    if num==67:
        class_choise=Debuger
    if stat=="max_hp":
        return class_choise.max_hp
    elif stat=="hp":
        return class_choise.hp
    elif stat=="ac":
        return class_choise.ac
    elif stat=="heal_count":
        return class_choise.heal_count
    elif stat=="speshal_atakc_mana_cost":
        return class_choise.speshal_atakc_mana_cost
    elif stat=="bonus":
        return class_choise.bonus
    elif stat=="mana":
        return class_choise.mana
def get_mon_stat(monster,stat):
    pass
def main():
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
        Fighter.__init__(Fighter)
        class_chosen=Fighter
    elif choise=="2":
        Barbarean.__init__(Barbarean)
        class_chosen=Barbarean
    elif choise=="3":
        Mage.__init__(Mage)
        class_chosen=Mage
    elif choise=="4":
        Rouge.__init__(Rouge)
        class_chosen=Rouge
    elif choise=="67":
        Debuger.__init__(Debuger)
        class_chosen=Debuger
    while get_class_stat(choise,"hp")>0:
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
            while choise not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                print("""
______choose your move_______
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
                print(f"you will now fight {["a Dragon.","a Goblin.","a Vampier.","a Beholder.","a Cyclops.","a Worm.","a Mimic.","a Skeleton.","the Tarrasque.","a Troll.","a Zombie."](["1","2","3","4","5","6","7","8","9","10","11"].index(choise))}")#250 chars
                monster=[Dragon,Goblin,Vampier,Beholder,Cyclops,Worm,Mimic,Skeleton,Tarrasque,Troll,Zombie][int(choise)]
                while get_class_stat(class_chosen,"hp")>0 or 
            else:
                pass
            
if __name__=="__main__":
    main()