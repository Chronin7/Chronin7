import time
import random
def typee(text):
    lists = []
    for i in text:
        lists.append(i)
    for x in lists:
        print(x, end = "", flush = True)
        time.sleep(random.uniform(.01,.2))
    print("")
typee("hiiiii")