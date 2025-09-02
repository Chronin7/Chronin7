# manualy make a wave file UGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG THIS IS GOING TO BE TOURCHER
import winsound
wav_data_in_memory = b'RIFF\x00\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00D\xac\x00\x00\x88L\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00' 

winsound.PlaySound(wav_data_in_memory, winsound.SND_MEMORY)