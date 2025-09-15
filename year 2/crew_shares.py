# lp 1 crew shares
while True:
    try:
        booty=int(input("wha' be the amount o' booty: "))
        break
    except:
        print("dat ain't a valid input")
while True:
    try:
        hands=int(input("how many crew hands be thar: "))
        break
    except:
        print("dat ain't a valid input")
share=round(booty/(10+hands),2)
print(f"capitan gets: {share*7} booty")
print(f"first mate gets: {share*3} booty")
print(f"each hand gets {share-500} booty")

