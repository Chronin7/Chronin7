import pyaudio
import numpy as np
import math
import time

# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024 # Number of frames per buffer
REFERENCE_VALUE = 1 # For digital audio normalized to -1 to 1

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Measuring sound levels...")

try:
    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Normalize to -1 to 1 range (assuming 16-bit audio)
        normalized_audio_data = audio_data / 32768.0

        # Calculate RMS
        rms = np.sqrt(np.mean(normalized_audio_data**2))

        # Convert to Decibels
        if rms > 0:
            db = 20 * math.log10(rms / REFERENCE_VALUE)
        else:
            db = -60 # Or a very low number to represent silence

        print(f"Current Decibel Level: {db:.2f} dB")
        time.sleep(0.1) # Adjust refresh rate as needed

except KeyboardInterrupt:
    print("Measurement stopped.")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()

class YoMamaSoFatTheCoputerBrokeWarning(Exception):
    print(Exception)
    pass
raise YoMamaSoFatTheCoputerBrokeWarning("Mother canot be fat")