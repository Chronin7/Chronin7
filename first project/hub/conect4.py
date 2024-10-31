t=1
r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
r6=[]
for i in range(6):
    r1.append("  ")
    r2.append("  ")
    r3.append("  ")
    r4.append("  ")
    r5.append("  ")
    r6.append("  ")
def pb():
    print("  1     2      3      4      5     6")
    for i in [5,4,3,2,1,0]:
        print(" ",end= "")
        print(f"{r1[i]}  |  {r2[i]}  |  {r3[i]}  |  {r4[i]}  |  {r5[i]}  |  {r6[i]}")
pb()
while True:
    if t == 1:
        p = "🔴"
    else:     
        p ="🟡"
    while True:
        try:
            g = int(input(f"{p} where do you want to go: "))
            for i in [1,2,3,4,5,6]:
                q=i
                if i==g:
                    w=-1
                    if q==1:
                        l=r1[0]
                        while True:
                            w=w+1
                            l=r1[w]
                            if l =="  ":
                                r1[w] = p
                                break
                        break
                    if q==2:
                        l=r2[0]
                        while True:
                            w=w+1
                            l=r2[w]
                            if l =="  ":
                                r2[w] = p
                                break
                        break
                    if q==3:
                        l=r3[0]
                        while True:
                            w=w+1
                            l=r3[w]
                            if l =="  ":
                                r3[w] = p
                                break
                        break
                    if q==4:
                        l=r4[0]
                        while True:
                            w=w+1
                            l=r4[w]
                            if l =="  ":
                                r4[w] = p
                                break
                        break
                    if q==5:
                        l=r5[0]
                        while True:
                            w=w+1
                            l=r5[w]
                            if l =="  ":
                                r5[w] = p
                                break
                        break
                    if q==6:
                        l=r6[0]
                        while True:
                            w=w+1
                            l=r6[w]
                            if l =="  ":
                                r6[w] = p
                                break
                        break
                    break
        except:
            print("no")
        if t == 1:
            t=2
        else:
            t=1
        pb()
