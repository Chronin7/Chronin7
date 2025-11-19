import util_functions
nums=[]
while (bool(choise:=util_functions.get_valid_type(int,"input 1 number to square (0 to get results): "))):([print(f"{nums[index]}^2={x}") for index,x in enumerate(map(lambda num: num*num,nums))]) if choise else nums.append(choise)