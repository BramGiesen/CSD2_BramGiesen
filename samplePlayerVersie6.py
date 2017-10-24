import simpleaudio as sa
import time
import random
import randomNumber2 as rm
import pathlib
import samplerMidiRythm as midi

current_dir = str(pathlib.Path(__file__).parent)#sets path to samples

#TODO: #check MIDI function

#maatsoort = 10
bpm = 120
#beatsPerMeasure = 3

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
def makeRandomList(beatsPerMeasure):
    #beatsPerMeasure = 10
    uitkomst = [ random.randint(1, 10) for _ in range(beatsPerMeasure) ]
    rm.generateList(kansKick, sequenceKick, uitkomst, beatsPerMeasure)
    rm.generateList(kansSnare, sequenceSnare, uitkomst, beatsPerMeasure )
    rm.generateList(kansHihat, sequenceHihat, uitkomst, beatsPerMeasure)
    midi.generateMIDI(kansKick,35,  uitkomst, beatsPerMeasure)
    midi.generateMIDI(kansSnare,38, uitkomst, beatsPerMeasure)
    midi.generateMIDI(kansHihat,42, uitkomst, beatsPerMeasure)
    #midi.printMIDI()

#load 3 audioFiles and store it into a list
samples = [
            sa.WaveObject.from_wave_file(current_dir + "/kick.wav"),
            sa.WaveObject.from_wave_file(current_dir + "/snare.wav"),
            sa.WaveObject.from_wave_file(current_dir + "/hihat.wav"), ]

notes = [
    'kick',
    'snare',
    'hihat'
]


startTone = sa.WaveObject.from_wave_file(current_dir + "/empty.wav")




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



def playStartTone():#plays a silent sample to prevent the first sample to stutter
    startTone.play()



def playBack(originalEvents):
    events = originalEvents[:]
    events.sort()
    startTime = time.time()


    #play the sequence
    while True:
        currentTime = time.time()
        # for each sample check if needs to played
        for event in events:#puts together
            index = events.index(event)
            eventTime = event[0]
            sample = samples[event[1]]

            if (currentTime - startTime >= eventTime):#checks time, plays sample
                sample.play()
                events.pop(index)#pops first element of index events

        if not events:#if events is empty
            events = originalEvents[:]#retrieve new list(copy)
            events.sort()
            startTime = time.time()#sets new start time
