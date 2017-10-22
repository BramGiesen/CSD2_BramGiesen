import simpleaudio as sa
import time
import random
import randomNumber2 as rm
import pathlib

current_dir = str(pathlib.Path(__file__).parent)

#TODO: #BPM versnelt het afspelen van de noten maar de loop blijft even lang, misschien delen door?
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
#create a list to hold the events, in de ze lijst komen als eerste element een tijd en tweede element,
#een getal die staat voor welke sample er wordt afgespeeld
#de lijst "uitkomst" wordt vergeleken met deze lijsten, 10 is 100% kans, 1 weinig kans
kansKick =  [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
kansSnare = [0, 2, 2, 2, 7, 2, 2, 2, 0, 2, 2, 2, 7, 2, 2, 2, ]
kansHihat = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#hier wordt een functie aangeroepen uit 'randomNumber2.py' die een lijst aanmaakt door de kans lijst hierboven te
#vergelijken met een random lijst die wordt gegenereerd in randomNumber2.py
rm.generateList(kansKick, sequenceKick)
#rm.generateList(kansSnare, sequenceSnare)
rm.generateList(kansHihat, sequenceHihat)

#load 3 audioFiles and store it into a list
samples = [
            sa.WaveObject.from_wave_file(current_dir + "/kick.wav"),
            sa.WaveObject.from_wave_file(current_dir + "/snare.wav"),
            sa.WaveObject.from_wave_file(current_dir + "/hihat.wav"), ]

notes = [
    'c',
    'c#',
    'd'
]


startTone = sa.WaveObject.from_wave_file(current_dir + "/empty.wav")


bpm = 120
beatsPerMeasure = 3



def makeList(bpm, beatsPerMeasure):
    events = []
    #calculate the duration of a quarter note
    quarterNoteDuration = 60 / bpm
    #calculate the duration of a sixteenth note
    sixteenthNoteDuration = quarterNoteDuration / 4.0
    #calculate the duration of a measure
    measureDuration = beatsPerMeasure  * quarterNoteDuration


#transform the sixteenthNoteSequece to an eventlist with time values
    for sixteenNoteIndex in sequenceKick:
        events.append([sixteenNoteIndex * sixteenthNoteDuration, 0])

#transform the sixteenthNoteSequece to an eventlist with time values
    for sixteenNoteIndex in sequenceSnare:
        events.append([sixteenNoteIndex * sixteenthNoteDuration, 1])

#transform the sixteenthNoteSequece to an eventlist with time values
    for sixteenNoteIndex in sequenceHihat:
        events.append([sixteenNoteIndex * sixteenthNoteDuration, 2])
        #events.sort()

    return events




def convertEventsToMidi(events):
    # [s1, s2, s3, s1, s2, s3, etc...]
    # s[0] = time
    # s[1] = indexOfSample
    midi = []

    for event in events:
        time = event[0]
        note = notes[event[1]]
        midi.append([time, note])

    return midi



def playStartTone():
    startTone.play()



def playBack(originalEvents):
    events = originalEvents[:]
    events.sort()
    startTime = time.time()


    #play the sequence
    while True:
        currentTime = time.time()
        # for each sample check if needs to played
        for event in events:
            index = events.index(event)
            eventTime = event[0]
            sample = samples[event[1]]

            if (currentTime - startTime >= eventTime):
                sample.play()
                events.pop(index)

        if not events:
            events = originalEvents[:]
            events.sort()
            startTime = time.time()



        # currentTime = time.time()
        # #check if the event's time (which is at index 0 of event) is passed
        # if(currentTime - startTime >= event[0]):
        #     #play sample -> sample index is at index 1
        #     # samples[event[1]].play()
        #     print("play", event[0])
        #     #if there are events left in the events list
        #     if events:
        #         #retrieve the next event
        #         event = events.pop(0)
        #     else:# if events list is empty
        #         events = originalEvents[:]
        #         startTime = time.time()
            #     while True:
            #         currentTime = time.time()#set new current time
            #         if currentTime - startTime >= measureDuration:
            #             startTime = time.time()#set new start time
            #             makeList(bpm, beatsPerMeasure)#generate new list
            #             events.sort()
            #             print(events)
            #             event = events.pop(0)
            #             break;
            #         else:
            #             #wait for a very short moment
            #             time.sleep(0.001)
            #             continue
