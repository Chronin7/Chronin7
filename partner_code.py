#----sudocode----
#print this will tell you the factorial number
#answer
#
#def 
#make a while True loop:
# number = int(input("what num do you want?"))
#   if num == int:
#     True
#   else:
#	  print("not an integer")
#	  continue
#for loop number in numbers
#	if number<1
#	  brake
#----code----
# changed this will tell you the factorial number to this is a factorial calculator
#      vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print("this is a factorial calculator")
# finished function (was originally just given "def")
#  vvvvvvvvvvvvvvv
def multiply(a,b):
    return a*b
while True:
	#added try except for extra error handling
	#vvv
	try:
		#made more user friendly
		#                                     vv
		number=int(input("what num do you want: "))
		#added negative number handling
		#vvvvvvvvvvvvvvvvvvv
		negitive=False
		if "-" in str(number):
			negitive=True
			number=abs(number)
		#removed unnecessary and confusing code
		#vvvvvvvvvvvvvvvvvvvv
		#if num==int
			#True
		#else:
			#print("not an integer")
			#continue
		#added variable definitions
		total=1
		#added underscore and range 
		#       v           vvvvvv      v
		for loop_numbers in range(number):
			#removed incorrect code
			#if number<1:
				#brake
			#added functioning code
			#vvvvvvvvvvvvvvvvv
			total=multiply(total,loop_numbers)
		#second half of 
		#vvvvvvvvvvvvvvvvvv
		if negitive:
			total*-1
		print(f"num")
