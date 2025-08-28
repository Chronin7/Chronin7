import winsound, time, threading
note_names=["c0"
,"c^0"
,"db0"
,"d0"
,"d^0"
,"eb0"
,"e0"
,"f0"
,"f^0"
,"gb0"
,"g0"
,"g^0"
,"ab0"
,"a0"
,"a^0"
,"bb0"
,"b0"
,"c1"
,"c^1"
,"db1"
,"d1"
,"d^1"
,"eb1"
,"e1"
,"f1"
,"f^1"
,"gb1"
,"g1"
,"g^1"
,"ab1"
,"a1"
,"a^1"
,"bb1"
,"b1"
,"c2"
,"c^2"
,"db2"
,"d2"
,"d^2"
,"eb2"
,"e2"
,"f2"
,"f^2"
,"gb2"
,"g2"
,"g^2"
,"ab2"
,"a2"
,"a^2"
,"bb2"
,"b2"
,"c3"
,"c^3"
,"db3"
,"d3"
,"d^3"
,"eb3"
,"e3"
,"f3"
,"f^3"
,"gb3"
,"g3"
,"g^3"
,"ab3"
,"a3"
,"a^3"
,"bb3"
,"b3"
,"c4"
,"c^4"
,"db4"
,"d4"
,"d^4"
,"eb4"
,"e4"
,"f4"
,"f^4"
,"gb4"
,"g4"
,"g^4"
,"ab4"
,"a4"
,"a^4"
,"bb4"
,"b4"
,"c5"
,"c^5"
,"db5"
,"d5"
,"d^5"
,"eb5"
,"e5"
,"f5"
,"f^5"
,"gb5"
,"g5"
,"g^5"
,"ab5"
,"a5"
,"a^5"
,"bb5"
,"b5"
,"c6"
,"c^6"
,"db6"
,"d6"
,"d^6"
,"eb6"
,"e6"
,"f6"
,"f^6"
,"gb6"
,"g6"
,"g^6"
,"ab6"
,"a6"
,"a^6"
,"bb6"
,"b6"
,"c7"
,"c^7"
,"db7"
,"d7"
,"d^7"
,"eb7"
,"e7"
,"f7"
,"f^7"
,"gb7"
,"g7"
,"g^7"
,"ab7"
,"a7"
,"a^7"
,"bb7"
,"b7"
,"c8"
,"c^8"
,"db8"
,"d8"
,"d^8"
,"eb8"
,"a0"]
notes_sound=["37"
,"37","37"
,"37"
,"37","37"
,"37"
,"37"
,"37","37"
,"37"
,"37","37"
,"37"
,"37","37"
,"37"
,"37"
,"37","37"
,"38"
,"39","39"
,"41"
,"44"
,"46","46"
,"49"
,"52","52"
,"55"
,"58","58"
,"62"
,"65"
,"69","69"
,"73"
,"78","78"
,"82"
,"87"
,"93","93"
,"98"
,"104","104"
,"110"
,"117","117"
,"123"
,"131"
,"139","139"
,"147"
,"156","156"
,"165"
,"175"
,"185","185"
,"196"
,"208","208"
,"220"
,"233","233"
,"247"
,"262"
,"277","277"
,"294"
,"311","311"
,"330"
,"349"
,"370","370"
,"392"
,"415","415"
,"440"
,"466","466"
,"494"
,"523"
,"554","554"
,"587"
,"562","622"
,"659"
,"698"
,"740","740"
,"784"
,"831","831"
,"880"
,"932","932"
,"988"
,"1047"
,"1109","1109"
,"1175"
,"1245","1245"
,"1319"
,"1397"
,"1480","1480"
,"1568"
,"1661","1661"
,"1760"
,"1865","1865"
,"1976"
,"2093"
,"2217","2217"
,"2349"
,"2489","2489"
,"2637"
,"2794"
,"2960","2960"
,"3136"
,"3322","3322"
,"3520"
,"3729","3729"
,"3951"
,"4186"
,"4435","4435"
,"4699"
,"4978","4978"]
def playnote1(note,duration):
	if note == 37:
		time.sleep(duration/1000)
	else:
		winsound.Beep(note,duration)
		time.sleep(duration/1000)
def playnote2(note1,duration1):
	if note1 == 37:
		time.sleep(duration1/1000)
	else:
		winsound.Beep(note1,duration1)
		time.sleep(duration1/1000)
def playnote3(note2,duration2):
	if note2 == 37:
		time.sleep(duration2/1000)
	else:
		winsound.Beep(note2,duration2)
		time.sleep(duration2/1000)
def playnote4(note3,duration3):
	if note3 == 37:
		time.sleep(duration3/1000)
	else:
		winsound.Beep(note3,duration3)
		time.sleep(duration3/1000)
def conpilesound(list_o_notes):
	compiledlist=[]
	for x in list_o_notes:
		iteration=0
		for y in note_names:
			if y==x:
				compiledlist.append(int(notes_sound[iteration]))
			else:
				iteration+=1
	return compiledlist

		
notesl1=conpilesound(["d4","d4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","c4","c4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","b4","b4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","bb4","bb4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4""d4","d4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","c4","c4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","b4","b4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","bb4","bb4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","d4","d4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","c4","c4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","b4","b4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4","bb4","bb4","d5","a4","c0","g^4","c0","g4","c0","f4","d4","f4","g4"])
notesl2=conpilesound(["c0","c0","c0","c0","c0","c0","c0","c0","d5","d5","d6","a5","c0","g^5","c0","g5","c0","f5","d5","f5","g5","c5","c5","d5","a5","c0","g^5","c0","g5","c0","f5","d5","f5","g5","b5","b5","d6","a5","c0","g^5","c0","g5","c0","f5","d5","f5","g5","bb5","bb5","d6","a5","c0","g^5","c0","g5","c0","f5","d5","f5","g5"])
notesl3=conpilesound(["c0","c0","c0","c0","d3","d3","d3","d3","c0","d3","c0","d3","c0","d3","d3","d3","d3","c3","c3","c3","c3","c0","c3","c0","c3","c0","c3","c3","c3","c3","a3","a3","a3","a3","c0","a3","c0","a3","c0","a3","a3","a3","a3","ab3","ab3","ab3","ab3","c0","ab3","c0","ab3","c0","ab3","ab3","ab3","ab3","d3","d3","d3","d3","c0","d3","c0","d3","c0","d3","d3","d3","d3","c3","c3","c3","c3","c0","c3","c0","c3","c0","c3","c3","c3","c3","a3","a3","a3","a3","c0","a3","c0","a3","c0","a3","a3","a3","a3","ab3","ab3","ab3","ab3","c0","ab3","c0","ab3","c0","ab3","ab3","ab3","ab3"])
notesl4=conpilesound(["c0","c0","c0","c0","c0","c0","c0","c0","d2","d2","d2","d2","c0","d2","c0","d2","c0","d2","d2","d2","d2","c2","c2","c2","c2","c0","c2","c0","c2","c0","c2","c2","c2","c2","a2","a2","a2","a2","c0","a2","c0","a2","c0","a2","a2","a2","a2","ab2","ab2","ab2","ab2","c0","ab2","c0","ab2","c0","ab2","ab2","ab2","ab2"])
durataionlistl1=[63,63,125,125,63,63,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63,125,125,63,63,63,63,63,125,63,63,63,63,63]
durataionlistl2=[1000,1000,1000,1000,1000,1000,1000,1000,63,63,125,125,63,63,63,63,63,63,63,125,125,63,63,63,63,63,63,63,125,125,63,63,63,63,63,63,63,125,125,63,63,63,63,63]
durataionlistl3=[1000,1000,1000,1000,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125]
durataionlistl4=[1000,1000,1000,1000,1000,1000,1000,1000,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125,125,125,63,63,63,63,63,63,63,63,63,63,125]
go=False
def playstrin1():
	global notesl1
	global durataionlistl1
	global go
	while go == True:
		go=False
	for x,y in zip(notesl1,durataionlistl1):
		playnote1(x,y)
def playstrin2():
	global notesl2
	global go
	global durataionlistl2
	while go == True:
		go=False
	for a,s in zip(notesl2,durataionlistl2):
		playnote2(a,s)
def playstrin3():
	global notesl3
	global durataionlistl3
	global go
	while go == True:
		go=False
	for d,f in zip(notesl3,durataionlistl3):
		playnote3(d,f)
def playstrin4():
	global notesl4
	global durataionlistl4
	global go
	while go == True:
		go=False
	for g,h in zip(notesl4,durataionlistl4):
		playnote4(g,h)
def threadgo():
	threads = []
	threads.append(threading.Thread(target=playstrin1()))
	threads.append(threading.Thread(target=playstrin2()))
	threads.append(threading.Thread(target=playstrin3()))
	threads.append(threading.Thread(target=playstrin4()))
	for thread in threads:
		thread.start()
		go=False
go=True
start=threading.Thread(target=threadgo())
start.start
#Quarter Note Duration = 60,000 / 120 = 500 ms
#Eighth Note Duration = 500 ms / 2 = 250 ms
#Sixteenth Note Duration = 500 ms / 4 = 125 ms