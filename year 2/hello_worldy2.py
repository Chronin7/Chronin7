#hello world prgram, liam perl (you shold copy and paste it into your code space and run it for the lol's)
import time
import random
import threading
typing =True
reading_code=False #as far as i know lol
type_speed=.1
times_up=False
def countdown():
	global times_up
	print(f"""  _______
 /  12   \ 
|    |    |
|9   |   3|
|     \   |
|         |
 \___6___/
10""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|     /   |
|9   /   3|
|     \   |
|         |
 \___6___/
9""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|         |
|9   ____3|
|     \   |
|         |
 \___6___/
8""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|         |
|9       3|
|     \   |
|      \  |
 \___6___/
7""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|         |
|9       3|
|    |\   |
|    |    |
 \___6___/
6""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|         |
|9       3|
|    /\   |
|   /     |
 \___6___/
5""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|         |
|9___    3|
|     \   |
|         |
 \___6___/
4""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|   \     |
|9   \   3|
|     \   |
|         |
 \___6___/
3""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|    |    |
|9   |   3|
|    |    |
|         |
 \___6___/
2""")
	time.sleep(1)
	print(f"""  _______
 /  12   \ 
|      /  |
|9    /  3|
|    |    |
|         |
 \___6___/
1
""")
	times_up=True
	return
def type_text(textt):
	if typing == True:
		for x in textt:
			print(x, end = "", flush = True)
			time.sleep(random.uniform(.01,type_speed))
		print("")
	else:
		print(textt,flush=True)
name=input("what is your name: ")
type_text(f"hello {name}")
time.sleep(3)
type_text("i see you have ran file hello_world.py")
type_text("but that is not all i can see")
frame = 0
clock = 0
clock = time.time()
time.sleep(0.01)
framee= time.time()
frame = framee-clock
type_text(f"for example your frame rate is running at {frame*6000} frames a second")
type_text("yes that is your frame rate")
type_text("also you only have 10 seconds to stop this program")
typed = "" 
thread1 = threading.Thread(target=countdown, args=())
thread1.start()
while True:
	if reading_code==True:
		print("just doing a little jig here")
	if times_up==True:
		time.sleep(1)
		type_text("out of time beter luck next time")
		time.sleep(.7)
		for x in range(1,100):
			print()
		thread1.join()
		quit()
		