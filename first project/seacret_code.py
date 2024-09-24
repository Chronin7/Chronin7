code_decode = int(input("would you like to code (1) or decode (2): "))
coded_list = []
coded = ""
if code_decode == 1:
    code = input("what is the uncoded word: ")
    for i in code:
        coded_list.append(ord(i))
    for x in coded_list:
        coded = coded + str(x)
print(coded)