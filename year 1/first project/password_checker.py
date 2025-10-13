#import random
# def check num(peramaters):
#	if peramaters is in 1,2,3,4,5,6,7,8,9,0
#	then	
#		return True
#	else
#		return False
# def check upper(peramaters)
#	if peramater is upper
#	then	
#		return True
#	else
#		return False
# def check lowwer(peramaters)
#	if peramater is lowweer
#	then	
#		return True
#	else
#		return False
# def make password():
# 	
#reapet untill user quits:
#	password=input(whast your passord)
#	printit(password)
# def printit(password):
# 	score=5
#	for x in [length,syimble,cap,low,num]:
#		if password not have x:
#			score-=1
#			recemended=x
#	print(f"""
# {stren[4]}          {recemended}
# {stren[3]}          recomendations
# {stren[2]}          {bet password}
# {stren[1]}          a better password
# {stren[0]}          {password}
# strength   password
# """)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def check_num(peramaters):
	if peramaters in ["1","2","3","4","5","6","7","8","9","0"]
		return True
	else:
		return False
def check_upper(peramaters):
	return str(peramaters).isupper()
def check_lowwer(peramaters):
	return str(peramaters).islowwer()
def check_symble(peramaters):
	return not (ord(peramaters)>47 and ord(peramaters)<57)or(ord(peramaters)>65 and ord(peramaters)<90)or(ord(peramaters)>97 and ord(peramaters)<122):
		
def printit(password):
	score=5
	if check_lowwer:
		recemended="add a lowercase letter"
		score-=1
	if check_upper:
		recemended="add a uppercase letter"
		score-=1
	if check_num:
		recemended="add a number"
		score-=1
	if check_symble:
		recemended="add a symbol"
		score-=1
	print(f"""
 {stren[4]}          {recemended}
 {stren[3]}          recomendations
 {stren[2]}          {bet_password}
 {stren[1]}          a better password
 {stren[0]}          {password}
 strength   password
 """)
while True:
	password=input("whats your passord")
	
