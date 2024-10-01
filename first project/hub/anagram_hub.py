def anagram():
    import random
    while True:
        anagram = []
        output = ""
        doit = "12345"
        word = input("hi i am Anny what is the word that you want into anagram or type stop to stop: ")
        if word == "stop":
            print("sending you back to Hubby")
            break
        if word == "":
            print("oops looks like you are a bit trigerhappy")
        else:
            rand = len(word)
            for y in doit:
                output = ""
                anagram = []
                for x in word:
                    anagram.insert(random.randint(1,rand),x)
                for i in anagram:
                    output = output + i
                print (output)
anagram()