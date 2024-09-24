input_word = input("what do you want to translate:")
checks = 0
split = {}
deleted = ""
not_a_string = ""
output = ""
decoded = ""
j = 0
i = 0
x = 0
def second_half(num):
    return (input_word[num:])
def check():
    print(f"#iteration: {iteration}")
    print(f"#input_word: {input_word}")
    print(f"#split: {split}")
    print(f"#deleted: {deleted}")
    print(f"#not_a_string: {not_a_string}")
    print(f"#output: {output}")
    print(f"#concinints {consinints}")
    print(f"#decoded {decoded}")
    print(f"#")
    print(f"#")
    print(f"#")
iteration = 1
consinints = []
if len(input_word) < 3:
    print(input_word)
    check()
else:
    for x in input_word:
        check()
        if x == "a":
            deleted = "a"
            split = second_half(iteration)
            check()
            break
        if x == "e":
            deleted = "e"
            split = second_half(iteration)
            check()
            break
        if x == "i":
            deleted = "i"
            split = second_half(iteration)
            check()
            break
        if x == "o":
            deleted = "o"
            split = second_half(iteration)
            check()
            break
        if x == "u":
            deleted = "u"
            split = second_half(iteration)
            check()
            break
        if x == "y" and iteration > 1:
            deleted = "y"
            check()
            split = second_half(iteration)
            break
        iteration += 1
        consinints.append(x)
check()
for i in split:
    check()
    not_a_string = not_a_string + i
    check()
for j in consinints:
    check()
    decoded = decoded + j
output =deleted + not_a_string + decoded + "ay"

print(output)