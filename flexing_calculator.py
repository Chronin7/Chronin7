import util_functions
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
    choise=util_functions.get_valid_type(int,"what do you want to do\n0 to stop\n1 for add\n2 for subtract\n3 for multiply\n4 for devide\n5 for factor\n6 for sum\n7 for avrage\n8 for max\n9 for min\n10 for product\n11 for random num (under construction)\n12 for factorial\n13 to get nth of fibonoci sequance\n14 to check if prime: ",valid=(0,14))
    if choise==0:
        print("goodbye")
        break
    elif choise==1:
        num1=util_functions.get_valid_type(int,"what is num1:")
        num2=util_functions.get_valid_type(int,"what is num2:")
        print(f"{num1}+{num2}={num1+num2}")
    elif choise==2:
        num1=util_functions.get_valid_type(int,"what is num1:")
        num2=util_functions.get_valid_type(int,"what is num2:")
        print(f"{num1}-{num2}={num1-num2}")
    elif choise==3:
        num1=util_functions.get_valid_type(int,"what is num1:")
        num2=util_functions.get_valid_type(int,"what is num2:")
        print(f"{num1}X{num2}={num1*num2}")
    elif choise==4:
        num1=util_functions.get_valid_type(int,"what is num1:")
        num2=util_functions.get_valid_type(int,"what is num2:")
        print(f"{num1}/{num2}={num1/num2}")
    elif choise==5:
        num1=util_functions.get_valid_type(int,"what is num1:")
        num2=util_functions.get_valid_type(int,"what is num2:")
        print(f"{num1}^{num2}={num1**num2}")
    elif choise==6:
        nums=[]
        itera=0
        while True:
            itera+=1
            nums.append(util_functions.get_valid_type(int,f"what is num{itera}:"))
            if util_functions.get_valid_type(str,"continue? (y/n): ",valid=["y","n"])=="n":
                break
        print(f"the sum of the numbers {nums} is {add(*nums)}")
    elif choise==7:
        nums=[]
        itera=0
        while True:
            itera+=1
            nums.append(util_functions.get_valid_type(int,f"what is num{itera}:"))
            if util_functions.get_valid_type(str,"continue? (y/n): ",valid=["y","n"])=="n":
                break
        print(f"the avrage of the numbers {nums} is {ave(*nums)}")
    elif choise==8:
        nums=[]
        itera=0
        while True:
            itera+=1
            nums.append(util_functions.get_valid_type(int,f"what is num{itera}:"))
            if util_functions.get_valid_type(str,"continue? (y/n): ",valid=["y","n"])=="n":
                break
        print(f"the bigest number from the numbers {nums} is {max(*nums)}")
    elif choise==9:
        nums=[]
        itera=0
        while True:
            itera+=1
            nums.append(util_functions.get_valid_type(int,f"what is num{itera}:"))
            if util_functions.get_valid_type(str,"continue? (y/n): ",valid=["y","n"])=="n":
                break
        print(f"the smallest number from the numbers {nums} is {max(*nums)}")
    elif choise==10:
        nums=[]
        itera=0
        while True:
            itera+=1
            nums.append(util_functions.get_valid_type(int,f"what is num{itera}:"))
            if util_functions.get_valid_type(str,"continue? (y/n): ",valid=["y","n"])=="n":
                break
        print(f"the product of the numbers {nums} is {multiply(*nums)}")
    elif choise==11:
        try:
            print(f"your random number is {util_functions.alternate_random((util_functions.get_valid_type(int,"what is the lowwer bound"),util_functions.get_valid_type(int,"what is the upper bound")),util_functions.get_valid_type(int,"what is the seed"),int)}")
        except:
            print("try again")
    elif choise==12:
        num=0
        print(f"the anwer to {(num:=util_functions.get_valid_type(int,"what is the number to factorial"))}! is {util_functions.factorial(num)}")
    elif choise==13:
        num=0
        print(f"the {(num:=util_functions.get_valid_type(int,"what is the number to factorial"))}th of the fibonacci sequance is {util_functions.fibonacci(num)}")
    elif choise==14:
        if util_functions.is_prime(num:=util_functions.get_valid_type(int,"what number do you want to check if prime: ")):
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")