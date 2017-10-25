import simpleaudio as sa
import time
import random
import itertools
import randomNumber as rm
import pathlib
import samplerMidiRythm as midi

current_dir = str(pathlib.Path(__file__).parent)#sets path to samples
#TODO = Werk de MIDI functie bij waardoor deze dezelfde output genereert als de sampler/maakt dubbele lijsten aan(dubbel geluid)
#empty list for events and probability
events = []
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
sequenceSnareNotchecked = []
sequenceHihatNotchecked = []
kansKick  = []
kansSnare = []
#the hihat is just straight forward, because 10 is 100% probability--> hit on every beat
kansHihat = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 4, 10]

global kansListKick, kansListSnare
kansListKick  = []
kansListSnare = []


def callKansPerMaatsoort(beatsPerMeasure):#function that is called from the userInput file
    kansPerMaatsoort(beatsPerMeasure, kansKick, 'kick')
    kansPerMaatsoort(beatsPerMeasure, kansSnare,'snare')


#rythmic blocks of 2, 3, or 4 beats; for example a 7/4 time signature can be build from one block of 3 and of 4 or from two blocks of 2 and one of 3
def selectList(name):
    global lijst1, lijst2, lijst3, lijst4
    if name == 'kick':# the numbers in the list are probability, 10 is 100%, 0 is 0%
        lijst1 = [6]
        lijst2 = [10,0]
        lijst3 = [7,0,3]
        lijst4 = [10,0,0,1]
    if name == 'snare':
        lijst1 = [10]
        lijst2 = [10,2]
        lijst3 = [10,7,3]
        lijst4 = [10,7,4,2]


#puts building blocks in list
def kansPerMaatsoort(beatsPerMeasure, lijst, name):
    selectList(name)
    if beatsPerMeasure == 4:
        lijst.append(lijst3)
        lijst.append(lijst1)
    if beatsPerMeasure == 6:
        lijst.append(lijst2)
        lijst.append(lijst3)
        lijst.append(lijst1)
    if beatsPerMeasure == 8:
        x = random.randint(0,1)
        if x == 1:
            lijst.append(lijst3)
            lijst.append(lijst2)
            lijst.append(lijst2)
            lijst.append(lijst1)
        else:
            lijst.append(lijst3)
            lijst.append(lijst4)
            lijst.append(lijst1)
            print(kansKick)


def transformKansList():
    global kansListKick, kansListSnare
    random.shuffle(kansKick,random.random)# shuffles the building blocks of 4,3,2
    random.shuffle(kansSnare,random.random)
    kansListKick  = list(itertools.chain(*kansKick))#from a list within a list to a flat list--> list is send to function makeRandomList()
    kansListSnare = list(itertools.chain(*kansSnare))

#hier wordt een functie aangeroepen uit 'randomNumber.py' die een lijst aanmaakt door de kans lijst hierboven te
#vergelijken met een random lijst die wordt gegenereerd in randomNumber.py
def makeRandomList(beatsPerMeasure):
    #generates random list of numberen between 1 and 10, the outcome is compared to the probability
    uitkomst = [ random.randint(1, 10) for _ in range(beatsPerMeasure) ]
    #calls function in randomNumber2.py to generate list
    rm.generateList(kansListKick, sequenceKick, uitkomst, beatsPerMeasure)
    rm.generateList(kansListSnare, sequenceSnareNotchecked, uitkomst, beatsPerMeasure )
    rm.generateList(kansHihat, sequenceHihatNotchecked, uitkomst, beatsPerMeasure)
    #cals function in samplerMidiRythm.py to generate MIDI file
    #midi.generateMIDI(kansListKick,35,  uitkomst, beatsPerMeasure)
    #midi.generateMIDI(kansListSnare,38, uitkomst, beatsPerMeasure)
    #midi.generateMIDI(kansHihat,42, uitkomst, beatsPerMeasure)
    print("""♫ Do you want to save this beat? ♫
pres y""")


#load 3 audioFiles and store it into a list
samples = [
            sa.WaveObject.from_wave_file(current_dir + "/kick.wav"),
            sa.WaveObject.from_wave_file(current_dir + "/snare.wav"),
            sa.WaveObject.from_wave_file(current_dir + "/hihat.wav"), ]

#loads a silent start tone to prevent a stutter at the first atack of the drumbeat(loading issue?)
startTone = sa.WaveObject.from_wave_file(current_dir + "/empty.wav")



#function that converts the list events wich is generated in 'def makeRandomList' to a appended list with time calculation for the sampler
def makeList(bpm, beatsPerMeasure):
    #print("sequenceSnareNot in makeList",sequenceSnareNotchecked)

    #Checks of the list with snare events has the same event times as the list with the kick events
    listCheck = [x for x in sequenceSnareNotchecked if x not in sequenceKick]
    #Only the snare events that don't have the same event time as the kick events are put in the list 'sequenceSnare'
    sequenceSnare.extend(listCheck)
    #print("sequenceSnare in makeList",sequenceSnare)

    listCheck = [x for x in sequenceHihatNotchecked if x not in sequenceSnare]
    sequenceHihat.extend(listCheck)

    midi.generateMIDI(sequenceKick,35,  beatsPerMeasure)
    midi.generateMIDI(sequenceSnare,38, beatsPerMeasure)
    midi.generateMIDI(sequenceHihat,42, beatsPerMeasure)
    #empty list events
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


def playStartTone():#plays a silent sample to prevent the first sample to stutter
    startTone.play()

def clearLists():#when the user sets a new time signature en BPM the lists who contain the old beat are cleared
    del events[:]
    del sequenceKick[:]
    del sequenceSnare[:]
    del sequenceHihat[:]

def playBack(originalEvents):#
    global playbackLoop
    events = originalEvents[:]#makes a copy of list events
    events.sort()
    startTime = time.time()#set start time

    #play the sequence
    while playbackLoop:
        currentTime = time.time()
        # for each sample check if needs to played
        for event in events:#puts together in index
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
