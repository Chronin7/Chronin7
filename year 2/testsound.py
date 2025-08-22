import winsound
# Play a WAV file asynchronously
winsound.PlaySound('ding-101492.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)


winsound.PlaySound(None, 0)
winsound.Beep(15000,100)