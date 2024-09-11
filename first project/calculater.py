operation = 0


print("Hi this is Calcu. What do you want me to calculate today")
def calcu():
    operation = 0
    a = "n/a"
    b = "n/a"
    operation = input("Do you want to do devison, mutipulcation, subtration, addition, modulo, factoring or just type stop to quit:  ")
    if operation == "devison" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        if b == 0 :
            print("devide by 0 error")
            calcu()
        conferm = input("is this what you want",a,"/",b,"(y/n):")
        if conferm == "y" :
            print(a,"/",b,"=",a/b)
        else:
            calcu()
    if operation == "mutipulcation" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        conferm = input("is this what you want",a,"X",b,"(y/n):")
        if conferm == "y" :
            print(a,"X",b,"=",a*b)
        else:
            calcu()
    if operation == "subtration" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        conferm = input("is this what you want",a,"-",b,"(y/n):")
        if conferm == "y" :
            print(a,"-",b,"=",a-b)
        else:
            calcu()
    if operation == "addition" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        conferm = input("is this what you want",a,"+",b,"(y/n):")
        if conferm == "y" :
            print(a,"+",b,"=",a+b)
        else:
            calcu()
    if operation == "modulo" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        conferm = input("is this what you want",a,"mod",b,"(y/n):")
        if conferm == "y" :
            print(a,"mod",b,"=",a/b)
        else:
            calcu()
    if operation == "factoring" :
        print("idk")
    if operation == "quit" :
        quit
    print("Sorry I dident understand")
    calcu()
    
    