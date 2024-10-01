def calculater():
    operation = 0
    conferm = 0
    a = "n/a"
    b = "n/a"
    print("Hi this is Calcu. What do you want me to calculate today")
    while True:
        operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ").lower()
        if operation == "":
            print("opps looks like you are a bit trigerhappy")
        else:
            if operation == "stop":
                print("ok sending you back to Hubby.")
                break
            if operation == "division" :
                    while True:
                        a = int(input("what is the first number:"))
                        if a == "":
                            print("oops looks like you are a bit trigerhappy")
                        else:
                            while True:
                                b = int(input("what is the second number:"))
                                if b == "":
                                    print("oops looks like you are a bit trigerhappy")
                                else:
                                    if b == 0 :
                                        print("division by 0 error")
                                    else:
                                        print(a,"/",b,"=",a/b)
                                        break
            if operation == "multiplication" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"X",b,"=",a*b)
            if operation == "subtraction" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"-",b,"=",a-b)
            if operation == "addition" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"+",b,"=",a+b)
            if operation == "modulo" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"%",b,"=",a%b)
            if operation == "factoring" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"^",b,"=",a**b)
                                break
            if operation == "stop" :
                print("sending you to Hubby.")
                break
calculater()