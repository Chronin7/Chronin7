code_decode = int(input("would you like to code (1) or decode (2): "))
list_o_coded = []
output =""
decoded = ""
iteration = 1
loops_o_codeing = 0
list_o_decoding = []
if code_decode == 1:
    code = input("what is the uncoded word: ")
    seed = int(input("what is the decoding seed (whole numbers pleese): "))
    for x in code:
        list_o_coded.append(((ord(x))))
    for y in list_o_coded:
        if loops_o_codeing == 0:
            output = str(int(y)+seed)
        else:
            output = output +","+ str(int(y)+seed)
        loops_o_codeing += 1
    print(output)
if code_decode == 2:
    coded_decoder = str(input("what is the coded thing: "))
    seed_o_decodeing = int(input("what is the seed: "))
    list_o_decoding = (coded_decoder.split(","))
    for z in list_o_decoding:
        var = str(chr(int(z)-seed_o_decodeing))
        decoded = decoded + var
    print(decoded)