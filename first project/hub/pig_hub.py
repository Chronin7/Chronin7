def pig():
    while True:
        input_word = input("I am Pig what do you want to translate (one word at a time):")
        if input_word == "":
            print ("oops looks like you are a bit trigerhappy")
        else:
            checks = 0
            split = []
            deleted = ""
            not_a_string = ""
            output = ""
            not_a = ""
            while True:
                iteration = 1
                if len(input_word) < 3:
                    print(input_word)
                    
                else:
                    for x in input_word:
                        
                        if x == "a":
                            split = input_word.split("a",1)
                            deleted = "a"
                            
                            break
                        if x == "e":
                            split = input_word.split("e",1)
                            deleted = "e"
                            
                            break
                        if x == "i":
                            split = input_word.split("i",1)
                            deleted = "i"
                            
                            break
                        if x == "o":
                            split = input_word.split("o",1)
                            deleted = "o"
                            
                            break
                        if x == "u":
                            split = input_word.split("u",1)
                            deleted = "u"
                            
                            break
                        if x == "y" and iteration > 1:
                            split = input_word.split("y",1)
                            deleted = "y"
                            
                            break
                        iteration += 1
                
                not_a_string = split[:iteration]
                for i in not_a_string:
                    not_a = not_a +''+i
                output = not_a + deleted +"ay"
                print(output)
                go = input("Do you want to translate anoter word? (y/n): ")
                if input_word == "":
                    print ("oops looks like you are a bit trigerhappy")
                else:
                    if go != "y":
                        print("Ok sending you back to Hubby")
                        break
                    else:
                        input_word = ""
                        input_word = input("What do you want to translate (one word at a time):")
                        if input_word == "":
                            print ("oops looks like you are a bit trigerhappy")
                        else:
                            chr(123)
pig()