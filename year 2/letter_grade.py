# lp 1 what is my grade:
#signal line version
print(f"your grade in letter: {"A" if (percent := int(input("what is your grade percentage: "))) >= 90 else "B" if percent >=80 else "C" if percent >70 else "D" if percent>60 else "F"}")
#multi line version of sadness and depression
num_grade=int(input("what is your grade percentage: "))
let_grade=""
if num_grade>90:
    let_grade="A"
elif num_grade>80:
    let_grade="B"
elif num_grade>70:
    let_grade="C"
elif num_grade>60:
    let_grade="D"
else:
    let_grade="F"
print(f"your grade in letter: {let_grade}")