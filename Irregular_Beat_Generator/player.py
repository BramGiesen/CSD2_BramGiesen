import time
import simpleaudio as sa

kick  = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/kick.wav'
snare = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/snare.wav'
hihat = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/hihat.wav'

# kickList = []
# snareList = []
# hihatList = []


def play(k, s, h, beatsPerMeasure, tempo):
	global kickList, snareList, hihatList
	kickList = k
	snareList = s
	hihatList = h


	a = 0
	if playbackLoop == True:
		while playbackLoop:

			for x in range(a, beatsPerMeasure):
				x = x - a;
				if kickList[x] == 1:
					waveObj1 = sa.WaveObject.from_wave_file(kick)
					playObj1 = waveObj1.play()
				if snareList[x] == 1:
					waveObj2 = sa.WaveObject.from_wave_file(snare)
					playObj2 = waveObj2.play()
				if hihatList[x] == 1:
					waveObj3 = sa.WaveObject.from_wave_file(hihat)
					playObj3 = waveObj3.play()
					time.sleep(tempo)
#
# def clear():
# 	del kickList[:]
# 	del snareList[:]
# 	del hihatList[:]
