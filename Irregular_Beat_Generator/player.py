import time
import simpleaudio as sa

samples = ['/Users/BramGiesen/Documents/HKU/CSD2a/Irregular_Beat_Generator/samples/kick.wav',
'/Users/BramGiesen/Documents/HKU/CSD2a/Irregular_Beat_Generator/samples/snare.wav',
'/Users/BramGiesen/Documents/HKU/CSD2a/Irregular_Beat_Generator/samples/hihat.wav',
'/Users/BramGiesen/Documents/HKU/CSD2a/Irregular_Beat_Generator/samples/electric_kick.wav',
'/Users/BramGiesen/Documents/HKU/CSD2a/Irregular_Beat_Generator/samples/electric_snare.wav',
'/Users/BramGiesen/Documents/HKU/CSD2a/Irregular_Beat_Generator/samples/electric_hihat.wav']

# kick  = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/kick.wav'
# snare = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/snare.wav'
# hihat = '/Users/BramGiesen/Documents/HKU/CSD2a/EindopdrachtBeatG/hihat.wav'

s = 0
#function to select the samples that are played, if s = 0 it playes the samples 0 t/m 2 from samples list.
#if s = 3 it plays samples 3/5 in samples list
def setGlobalS(value):
    global s
    s = value

#player takes lists containing 1 and 0, if index of list is 1 sample is played
#count starts at 0 and + 1 is added ever beat. The count is used to calculate the next beat.
#index is the count variable with a % so it goes from 0 to the beatsPerMeasure.
def play(kickList, snareList, hihatList, beatsPerMeasure, tempo):
	global s
	startTime = time.time()
	triggerLenght = tempo
	index = 0
	count = 0
	if playbackLoop == True:
			while playbackLoop:
				triggerTime = startTime + (triggerLenght * count)

				if time.time() > triggerTime:
					if kickList[index] == 1:
						waveObj1 = sa.WaveObject.from_wave_file(samples[s])
						playObj1 = waveObj1.play()
					if snareList[index] == 1:
						waveObj2 = sa.WaveObject.from_wave_file(samples[s+1])
						playObj2 = waveObj2.play()
					if hihatList[index] == 1:
						waveObj3 = sa.WaveObject.from_wave_file(samples[s+2])
						playObj3 = waveObj3.play()
					count = count + 1
					index = count % beatsPerMeasure
					time.sleep(0.01)
