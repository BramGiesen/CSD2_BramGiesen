import time 
import simpleaudio as sa 

empty = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/empty.wav'
kick  = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/kick.wav'
snare = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/snare.wav'
hihat = '/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/hihat.wav'

h = [empty, hihat, hihat, hihat, hihat]
s = [empty, empty, empty, snare, empty]
k = [empty, kick, empty, empty, empty]
a = 0
b = 3
while True:
	for x in range(a, b + 1):
		x = x - a + 1;
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


