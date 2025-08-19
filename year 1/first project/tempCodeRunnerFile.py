
imp = int(input())
coma = "{:,}"
print(coma.format(imp))
per = "{:%}"
print(per.format(imp))
per = "{:3f}"
print(per.format(imp))
per = "${:2d}"
print(per.format(imp))
