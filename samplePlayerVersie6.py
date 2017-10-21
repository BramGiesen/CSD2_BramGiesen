import simpleaudio as sa
import time
import random
import randomNumber2 as rm

sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
#de lijst "uitkomst" wordt vergeleken met deze lijsten, 10 is 100% kans, 1 weinig kans
kansKick =  [10, 2, 7, 3, 3, 2, 10, 10, 0, 2, 7, 3, 3, 2, 10, 10]
kansSnare = [0, 2, 2, 2, 7, 2, 2, 2, 0, 2, 2, 2, 7, 2, 2, 2, ]
kansHihat = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#hier wordt een functie aangeroepen uit 'randomNumber.py'
rm.generateList(kansKick, sequenceKick)
rm.generateList(kansSnare, sequenceSnare)
rm.generateList(kansHihat, sequenceHihat)

#create a list to hold the events
events = []
#create lists with the moments (in 16th) at which we should play the samples
sequence1 = sequenceKick
sequence2 = sequenceSnare
sequence3 = sequenceHihat



#load 3 audioFiles and store it into a list
samples = [
            sa.WaveObject.from_wave_file("/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/kick.wav"),
            sa.WaveObject.from_wave_file("/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/snare.wav"),
            sa.WaveObject.from_wave_file("/Users/BramGiesen/Documents/HKU/Jaar2/CSD/audioBestanden/hihat.wav"), ]


bpm = 120
beatsPerMeasure = 3
quarterNoteDuration = 60 / bpm
#calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0
#calculate the duration of a measure
measureDuration = beatsPerMeasure  * quarterNoteDuration
#def makeList():
def makeList(bpm, beatsPerMeasure):

    #calculate the duration of a quarter note
    quarterNoteDuration = 60 / bpm
    #calculate the duration of a sixteenth note
    sixteenthNoteDuration = quarterNoteDuration / 4.0
    #calculate the duration of a measure
    measureDuration = beatsPerMeasure  * quarterNoteDuration


#transform the sixteenthNoteSequece to an eventlist with time values
    for sixteenNoteIndex in sequence1:
        events.append([sixteenNoteIndex * sixteenthNoteDuration, 0])

#transform the sixteenthNoteSequece to an eventlist with time values
    for sixteenNoteIndex in sequence2:
        events.append([sixteenNoteIndex * sixteenthNoteDuration, 1])

#transform the sixteenthNoteSequece to an eventlist with time values
    for sixteenNoteIndex in sequence3:
        events.append([sixteenNoteIndex * sixteenthNoteDuration, 2])
        #events.sort()





def playBack():
    #retrieve first event
    #NOTE: pop(0) returns and removes the element at index 0
    event = events.pop(0)
    events.sort()
    #retrieve the startime: current time
    startTime = time.time()
    keepPlaying = True
    #play the sequence
    while keepPlaying:
  #retrieve current time
        currentTime = time.time()
        #check if the event's time (which is at index 0 of event) is passed
        if(currentTime - startTime >= event[0]):
            #play sample -> sample index is at index 1
            samples[event[1]].play()
            #if there are events left in the events list
            if events:
                #retrieve the next event
                event = events.pop(0)
            else:# if events list is empty
                while True:
                    currentTime = time.time()#set new current time
                    if currentTime - startTime >= measureDuration:
                        startTime = time.time()#set new start time
                        makeList(bpm, beatsPerMeasure)#generate new list
                        events.sort()
                        event = events.pop(0)
                        break;
                    else:
                        #wait for a very short moment
                        time.sleep(0.001)
                        continue
