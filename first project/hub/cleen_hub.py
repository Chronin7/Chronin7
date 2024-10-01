
debuging = 1
hubo = 0
import time
import temp_calculater_hub
import calculater_hub
import number_game_hub
import paladrome_hub
import pig_hub
import anagram_hub
import avrage_hub
def hub():
	while True:
		print("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		print("quit:0")
		print("calculater:1")
		print("guessing game:2")
		print("paladrome detector:3")
		print("pig latin transater:4")
		print("anagram maker:5")
		print("avrager:6")
		print("tempiture calculater:7")
		hubo = int(input("what do you want: "))
		if hubo == "":
			print("opps looks like you are a bit trigerhappy")
		else:
			if hubo ==0:
				print("Goodby please come back soon! ##connection terminated by:Hubby##")
				time.sleep(1)
				quit()
			if hubo ==1:
				print("Ok sending you to Calcu.")
				time.sleep(1)
				- calculater_hub.calculater()
			elif hubo ==2:
				print("Ok sending you to Guessy.")
				time.sleep(1)
				- number_game_hub.num_game()
			elif hubo ==3:
				print("Ok sending you to Pally.")
				time.sleep(1)
				- paladrome_hub.paladrome()
			elif hubo ==4:
				print("Ok sending you to Pig.")
				time.sleep(1)
				- pig_hub.pig()
			elif hubo ==5:
				print("Ok sending you to Anny.")
				time.sleep(1)
				- anagram_hub.anagram()
			elif hubo ==6:
				print("Ok sending you to AV (she is a bit crazy).")
				- avrage_hub.avrage()
			elif hubo ==7:
				print("Ok sending you to Kelven.")
				- temp_calculater_hub.temp()
			elif hubo ==8:
				print("Sorry this option is not available yet.")
			elif hubo ==9:
				print("Sorry this option is not available yet.")
			elif hubo ==10:
				print("Sorry this option is not available yet.")
			elif hubo ==3.141:
				print("Sorry this option is not available yet.")
			else:
				print("Sorry this option is not available yet.")


if debuging == 0:
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("connection successful")
	time.sleep(1)
	hub()
else:
	hub()