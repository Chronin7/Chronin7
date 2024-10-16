import time
iteration = 0
countback = False
while True:
	if countback == True:
		iteration -= 1
	else:
		iteration += 1
	if countback == True and iteration == -1:
		break
	else:
		print(iteration)
		if iteration == 20:
			countback = True
	time.sleep(.01)