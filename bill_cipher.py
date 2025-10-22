import user_check
def change(letter,number):
    startup =0
    if number<0:
        for num in range(0,number):
            if startup+number<97:
                startup=122
            if startup!=0:
                startup-=1
        if startup!=0:
            return chr(startup)
        else:
            return chr(ord(letter)+number)
    for num in range(0,number):
        if startup+number>122:
            startup=97
        if startup!=0:
            startup+=1
    if startup!=0:
        return chr(startup)
    else:
        return chr(ord(letter)+number)
print("hi im bill cipher forced to make codes for people for all eternity after weirdmageden")
while user_check.use_it()=="y":
    seed=int(input("what is the seed (how much it moves over):"))
    out=[]
    encdec=input("1 for decode 2 for encode: ")
    if encdec=="2":
        for x in input("what is your secret message (no numbers): "):
            if x == " ":
                out.append(" ")
            else:
                out.append(change(x,seed))
    elif encdec =="1":
        for x in input("what is your encoded message (no numbers): "):
            if x == " ":
                out.append(" ")
            else:
                out.append(change(x,26-seed))
    for x in out:
        print(x)
        