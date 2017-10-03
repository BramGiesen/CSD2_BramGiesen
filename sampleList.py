import time 
import simpleaudio as sa 


#aNumber = int(userInput)/.isDigit
# '10'.isdigit()
#userInput.isdigit()

empty = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/empty.wav'
kick  = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/kick.wav'
snare = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/snare.wav'
hihat = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/hihat.wav'

h = [hihat, hihat, hihat, hihat]
s = [empty, empty, snare, empty]
k = [kick, empty, empty, empty]
a = 0
b = 4
while True:
	for x in range(a, b):
		x = x - a;
		y = h[x]
		q = s[x]
		z = k[x]
		waveObj1 = sa.WaveObject.from_wave_file(y)
		waveObj2 = sa.WaveObject.from_wave_file(q)
		waveObj3 = sa.WaveObject.from_wave_file(z)
		playObj1 = waveObj1.play()
		playObj2 = waveObj2.play()
		playObj3 = waveObj3.play()
		time.sleep(0.5)


