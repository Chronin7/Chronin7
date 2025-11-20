exec('import util_functions as u;l=[];v=1\nwhile v==1:c=u.get_valid_type(int,"");l.append(c)if bool(c) else([print(f"{l[i]}:{x}")for i,x in enumerate(map(lambda n:n*n,l))]);v=1 if bool(c)else 0')
#set nums to empty list
#set var to 1
#while var is 1
# set choice to user input
# if choice is 0
#  for index,x in nums
#	output index of nums and lamda num:num*num,nums
#	set var to 0
# otherwise
#  add choice to nums