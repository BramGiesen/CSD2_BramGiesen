import simpleaudio as sa

x = int(input("hoe vaak wilt u het geluid horen? "))
count = 0
while count < x:

		wave_obj = sa.WaveObject.from_wave_file("/Users/BramGiesen/Documents/HKU/bliep.wav")
		play_obj = wave_obj.play()
		play_obj.wait_done()
		count = count + 1
