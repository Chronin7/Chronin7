
word = str(input("what is the word you are translating: ")).lower
voul = False
def pig():
    word = str(input("what is the word you are translating: ")).lower
    iteration = 1
    while voul == False:
        if word[iteration] == "a":
            voul = True
            break
        if word[iteration] == "e":
            voul = True
            break
        if word[iteration] == "i":
            voul = True
            break
        if word[iteration] == "o":
            voul = True
            break
        if word[iteration] == "u":
            voul = True
            break
        if word[iteration] == "y" and iteration != 1:
            voul = True
            break
        consenints =+ word[iteration]


spit_word = word.split("a",1)
