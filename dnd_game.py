#lp combaty 1
import random,math
class player_class:
    class Fighter:
        def __init__(self):
            self.max_hp=15
            self.hp=15
            self.atack=20
            self.ac=13
            self.heal_count=15
            self.speshal_atakc_mana_cost=10
            self.bonus=0
            self.mana=0
        def level_up(self):
            self.hp+=10
            self.hp=self.max_hp
            self.atack+=10
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
            return dice(10,2,self.bonus)
    class Barbarean:
        def __init__(self):
            self.max_hp=30
            self.hp=30
            self.atack=20
            self.ac=15
            self.heal_count=5
            self.speshal_atakc_mana_cost=15
            self.bonus=0
            self.mana=0
        def level_up(self):
            self.hp+=15
            self.hp=self.max_hp
            self.atack+=15
            self.ac+=1
            self.heal_count=5
            self.bonus+=10
        def norm_atack(self):
            print("you do your normail atack")
            self.mana+=3
            return dice(6,2,self.bonus)
        def speshail_atack(self):
            print("you do your speshil atack")
            self.mana+=3
            return dice(10,2,self.bonus)
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
            return dice(6,2,self.bonus)
        def speshail_atack(self):
            print("you do your speshil atack")
            self.mana+=10
            return dice(10,2,self.bonus)
    class Rouge:
        def __init__(self):
            self.max_hp=15
            self.hp=15
            self.atack=15
            self.ac=15
            self.heal_count=15
            self.speshal_atakc_mana_cost=13
            self.bonus=0
            self.mana=0
        def level_up(self):
            self.hp+=10
            self.hp=self.max_hp
            self.atack+=10
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
            return dice(10,2,self.bonus)
    # the dm is for testing
    class The_DM:
        def __init__(self):
            self.max_hp=15
            self.hp=15
            self.atack=15
            self.ac=15
            self.heal_count=15
            self.speshal_atakc_mana_cost=13
            self.bonus=0
            self.mana=0
        def level_up(self):
            self.hp+=10
            self.hp=self.max_hp
            self.atack+=10
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
            return dice(10,2,self.bonus)
class Monster:
    class Dragon:
        
    class Goblin:

    class Vampier:
    
    class Beholder:

    class Cyclops:

    class Worm:

    class Mimic:

    class Skeleton:

    class Tarrasque:

    class Troll:

    class Zombie:
        
def dice(upper_bound,count,bonus,lowwer_bound=1):
    for x in range(0,count):
        bonus+=random.randint(lowwer_bound,upper_bound)
    return bonus
def heal(heath,total_heal,heal_amount=random.randint(1,4)+random.randint(1,4)+random.randint(1,4)):
    print(f"you healed {heal_amount}, your hp is now {heath+heal_amount}, you have {total_heal-1} heals left")
    return heath+heal_amount
