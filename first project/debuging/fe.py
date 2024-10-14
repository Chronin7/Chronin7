# an integer with the comma to separate the thousands
# a float with 4 decimal places
# a percentage
# and then a dollar amount
format
inp = int(input("imput numbers to chace there format:"))
pr = "{:%}"
print(pr.format(0.54))
pr ="{:,}"
print(pr.format(inp))
pr =str(inp)[:4], str(".")+str(str(inp)[:4])
print(pr[1])