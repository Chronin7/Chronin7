import time
import random
def type(text):
    lists = []
    for i in text:
        lists.append(i)
    for x in lists:
        print(x, end = "")
        time.sleep(random.uniform(.01,.2))
    print("")
type("banana")


lists = []
for i in "banana":
	lists.append(i)
for x in lists:
	print(x, end = "")
time.sleep(random.uniform(.1,.2))
print("")