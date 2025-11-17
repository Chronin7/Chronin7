import util_functions
util_functions.alternate_random()
util_functions.clear_term()
util_functions.factorial()
util_functions.fibonacci()
util_functions.is_prime()
def add(*nums):
    x=0
    for y in nums:
        x+=y
    return x
def subtract(n1,n2):
    return n1-n2
def multiply(*nums):
    x=0
    for y in nums:
        x*=y
    return x
def devide(n1,n2):
    return n1/n2
def ave(*nums):
    leng=len(nums)
    tot=add(*nums)
    return tot/leng
while __name__=="__main__":
    choise=util_functions.get_valid_type(int,"what do you want to do\n0 to stop\n1 for add\n2for subtract\n3 for multiply\n4 for devide\n5 for sum\n6 for avrage\n7 for max\n8 for min\n9 for max\n10 for product\n11 for random num\n12 for factorial\n13 to get nth of fibonoci sequance\n14 to check if prime: ",valid=(0,14))
    if choise==0:
        print("goodbye")
        break
    elif choise==1:
        num1=util_functions.get_valid_type(int,"what is num1:")
        num2=util_functions.get_valid_type(int,"what is num2:")
        print(f"{num1}+{num2}={num1+num2}")