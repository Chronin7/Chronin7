import pyttsx3, time

def text_init():
	"""initeates the text to speach reader"""
	global engine
	engine = pyttsx3.init()
def set_volume(sound):
	"""sound needs to be a float 0.0-1.0"""
	global engine
	engine.setProperty('volume',sound)
	text_init()
def set_speed(speed):
	global engine
	text_init()
	engine.setProperty('rate',speed)
def add_to_que(text):
    engine.say(text)
def speak():
    """speaks all text in the que"""
    global engine
    engine.runAndWait()
    engine.stop()
text_init()
add_to_que("hi this is faster then fast")
speak()
for stuff in [1,2,3,4,5]:
    print(stuff)