import winsound, time, random
while True:
	try:
		time.sleep(random.uniform(.01,.3))
		winsound.PlaySound('P:\perl,liam\Chronin7\mphg-ni (1).wav', winsound.SND_FILENAME)
	except KeyboardInterrupt:
		winsound.PlaySound('P:\perl,liam\Chronin7\you think you can st.wav', winsound.SND_FILENAME)