import time
a = 0
b = 1
infinite = True
while infinite == True:
	print(a)
	print(b)
	a += b
	b += a
	time.sleep(.01)