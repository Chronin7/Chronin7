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
# 	out.append(str(random_num(0,9)))
#	out.append([q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m][random_num(1,26)])
#	out.append([Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M][random_num(1,26)])
# 	out.append(chr(random_num(100,500)))
#	out.append(str(random_num(0,9)))
#	out.append([q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m][random_num(1,26)])
#	out.append([Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M][random_num(1,26)])
# 	out.append(chr(random_num(100,500)))
# 	for x in out:
#		returned = returned+x
#	return returned
# def make strength meater(score):
#	if score==0:
#		stren=["⬛️","⬛","⬛️","⬛️","⬛️"]
#	if score==1:
#		stren=["🟥","⬛️","⬛️","⬛️","⬛️"]
#	if score==2:
#		stren=["🟥","🟧","⬛️","⬛️","⬛️"]
#	if score==3:
#		stren=["🟥","🟧","🟨","⬛️","⬛️"]
#	if score==4:
#		stren=["🟥","🟧","🟨","🟩","⬛️"]
#	if score==5:
#		stren=["🟥","🟧","🟨","🟩","🟦"]
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

import random
def check_num(peramaters):
	for x in peramaters:
		if x  in ['1','2','3','4','5','6','7','8','9','0']:	
			return True
	return False
def check_upper(peramaters):
	for x in peramaters:
		if str(x).isupper():
			return True
	return False
def check_lowwer(peramaters):
	for x in peramaters:
		if str(x).isupper():
			return True
	return False
def make_password():
	out=[]
	returned=""
	out.append(str(random.randint(0,9)))
	out.append(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'][random.randint(0,25)])
	out.append(['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'][random.randint(0,25)])
	out.append(chr(random.randint(100,500)))
	out.append(str(random.randint(0,9)))
	out.append(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'][random.randint(0,25)])
	out.append(['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'][random.randint(0,25)])
	out.append(chr(random.randint(100,500)))
	for x in out:
		returned = returned+x
	return returned
def check_sym(password):
	for x in password:
		if x in ["""~""","""`""","""!""","""@""","""#""","""$""","""%""","""^""","""&""","""*""","""(""",""")""","""-""","""_""","""=""","""+""","""[""","""{""","""]""","""\\""","""|""",""";""",""":""","""'""",""",'''"''',""","""<""",""".""",""">""","""/""","""?""","""`"""]:
			return True
	return False
def printit(password):
	recemended=""
	score=5
	recemended="good job"
	if len(password)<8:
		recemended="make it longer"
		score-=1
	if check_lowwer(password):
		recemended="add a lowercase letter"
		score-=1
	if  not check_num(password):
		recemended="add a number"
		score-=1
	if not check_upper(password):
		recemended="add a uppercase letter"
		bet_password=make_rand()
		score-=1
	if not check_sym(password):
		recemended="add a special character"
		score-=1
	if score==0:
		stren=["⬛️","⬛","⬛️","⬛️","⬛️"]
	if score==1:
		stren=["🟥","⬛️","⬛️","⬛️","⬛️"]
	if score==2:
		stren=["🟥","🟧","⬛️","⬛️","⬛️"]
	if score==3:
		stren=["🟥","🟧","🟨","⬛️","⬛️"]
	if score==4:
		stren=["🟥","🟧","🟨","🟩","⬛️"]
	if score==5:
		stren=["🟥","🟧","🟨","🟩","🟦"]
	print(f"""
strength meater
{stren[4]}          recomendations
{stren[3]}          {recemended}
{stren[2]}          a better password
{stren[1]}          {make_password()}
{stren[0]}          password
           {password}
""")
while input("do you want to use (y/n): ")=="y":
	password=input("whats your passord: ")
	printit(password)


	
