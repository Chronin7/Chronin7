import random
import time
from asccii_art import *
def sumon(monhp,monname,descrion):
	ascii_art(f"name: {monname}")
	ascii_art(f"health: {monhp}")
	ascii_art("descrion:")
	ascii_art(descrion)
	return monhp
def mon_damage(mon_name,diedamage):
	damage = random.randint(1,diedamage)
	ascii_art(f"{mon_name} dealt {damage}@damage")
	return damage
