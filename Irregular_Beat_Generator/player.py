import time
import simpleaudio as sa


kick  = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/kick.wav'
snare = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/snare.wav'
hihat = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/hihat.wav'



def play(kickList, snareList, hihatList, beatsPerMeasure, tempo):
	startTime = time.time()
	triggerLenght = 0.2
	index = 0
	count = 0
	if playbackLoop == True:
			while playbackLoop:
				triggerTime = startTime + (triggerLenght * count)

				if time.time() > triggerTime:
					if kickList[index] == 1:
						waveObj1 = sa.WaveObject.from_wave_file(kick)
						playObj1 = waveObj1.play()
					if snareList[index] == 1:
						waveObj2 = sa.WaveObject.from_wave_file(snare)
						playObj2 = waveObj2.play()
					if hihatList[index] == 1:
						waveObj3 = sa.WaveObject.from_wave_file(hihat)
						playObj3 = waveObj3.play()
					index = index + 1
					count = count + 1
					if index == beatsPerMeasure:
						index = 0
					else:
						time.sleep(0.01)
