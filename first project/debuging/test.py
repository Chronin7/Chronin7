# an integer with the comma to separate the thousands
# a float with 4 decimal places
# a percentage
# and then a dollar amount

uot = ""
inp = input("imput numbers to chace there format:")
le = len(inp)
lis = []
out = []
it = 0
itt = -1
outt = []
first = inp[1]
for x in inp:
	outt.append(x)
while le-1 != it:
	it += 1
	lis.append(inp[it])
for r in lis:
	itt += 1
	if itt % 3 == 0:
		out.append("""'""")
		out.append(r)
	else:
		out.append(r)
for x in out:
	first += x
print(first)
outt [:4] = str(".")+str(outt[:4])
u = ""
for x in outt:
	u += x
print(x)
uot [:2] = str(".")+str(outt[:2])
print(f"%{inp}")
print(f"${uot}")