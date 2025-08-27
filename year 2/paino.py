import winsound, threading, time
def note1():
	winsound.Beep(440,100)
def note2():
	winsound.Beep(587,100)
def note3():
	winsound.Beep(659,100)
def note4():
	winsound.Beep(784,100)
thread1 = threading.Thread(target=note1, args=())
thread2 = threading.Thread(target=note2, args=())
thread3 = threading.Thread(target=note3, args=())
thread4 = threading.Thread(target=note4, args=())
thread1.start(), thread2.start(), thread3.start(), thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
winsound.MessageBeep()
quit()
