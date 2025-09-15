import threading
import time

user_input = None

def get_input():
	global user_input
	user_input = input("Enter something: ")

# Start input in a separate thread
input_thread = threading.Thread(target=get_input)

input_thread.daemon = True # Allow main program to exit even if thread is running
while True:
	try:
		input_thread.start()
	except:
		pass
	# Main program continues execution
	print("Doing other work...")
	time.sleep(.1)
	if user_input == "e":
		print("var e added")
	else:
		print("none")

	print("More work...")
	user_input=""