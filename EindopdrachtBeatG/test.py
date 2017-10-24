

kick = [0]
snare = [0]

def kansPerMaatsoort(beatsPerMeasure, lijst):
    global lijst0, lijst2, lijst3, lijst4
    if lijst == 'kick':
        lijst0 = [6]
        lijst2 = [10,2]
        lijst3 = [7,2,2]
        lijst4 = [10,3,5,2]
    if lijst == 'snare':
        lijst0 = [4]
        lijst2 = [10,2]
        lijst3 = [7,2,2]
        lijst4 = [10,3,5,2]

kansPerMaatsoort(4, 'snare')
print(lijst0)
