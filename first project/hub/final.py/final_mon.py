import random
import time
from asccii_art import *
def sumon(monhp,monname,descrion,montype):
	ascii_art(f"name: {monname}")
	ascii_art(f"health: {monhp}")
	ascii_art("descrion:")
	ascii_art(descrion)
def mon_damage(mon_name,diedamage):
	damage = random.randint(1,diedamage)
	ascii_art(f"{mon_name} dealt {damage}@damage")
	return damage
mon_damage("bob",20)
sumon("100","killer","will kill you","human")