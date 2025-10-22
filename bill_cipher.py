#lp chipher 1
#def change(number,letter)
#   add number to position of letter in alhpebet and if position is grater then 26 roll over
#   return new letter
#main loop:
#   get operation
#   if decode
#       print(change(-seed,loop thru user input))
#   else:
#       print(change(seed,loop thru user input))
alphebet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def change(letter,number,code_or_decode):
    global alphebet
    if code_or_decode=="code":
        pos=alphebet.index(letter)
        if pos+number>25:
            newpos=(pos+number)-25
        else:
            newpos=pos+number
        return alphebet[newpos]
    else:
        pos=alphebet.index(letter)
        if pos+number<0:
            newpos=(pos+number)+25
        else:
            newpos=pos+number
        return alphebet[newpos]
while input("do you want to use (y/n): ").lower()=="y":
    out=[]
    if input("1 for encode, 2 for decode: ")=="1":
        seed=int(input("whats the seed: "))
        code=input("whats the secret code: ").lower()
        for x in code:
            if x ==" ":
                out.append(" ")
            else:
                out.append(change(x,seed,"code"))
        for x in out:
            print(x,end="")
        print()
    else:
        seed=int(input("whats the seed: "))
        code=input("whats the secret code: ").lower()
        for x in code:
            if x ==" ":
                out.append(" ")
            else:
                out.append(change(x,0-seed,"decode"))
        for x in out:
            print(x,end="")
        print()

    