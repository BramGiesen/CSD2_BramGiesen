import simpleaudio as sa
import time
import random
import itertools
import randomNumber as rm
import pathlib
import samplerMidiRythm as midi

current_dir = str(pathlib.Path(__file__).parent)#sets path to samples

test = []
events = []
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
#create a list to hold the events, in de ze lijst komen als eerste element een tijd en tweede element,
#een getal die staat voor welke sample er wordt afgespeeld
#de lijst "uitkomst" wordt vergeleken met deze lijsten, 10 is 100% kans, 1 weinig kans
#kansKick  = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#kansSnare = [0, 2, 2, 4, 7, 2, 4, 6, 2, 3, 5, 6, 7, 2, 2, 2, ]
#kansHihat = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
sequenceSnareNotchecked = []
kansKick  = []
kansSnare = []
kansHihat = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

global kansListKick, kansListSnare
kansListKick  = []
kansListSnare = []
#lijstKickKans = []
#lijstSnareKans = []
#lijstHihatKans = []

def callKansPerMaatsoort(beatsPerMeasure):
    kansPerMaatsoort(beatsPerMeasure, kansKick, 'kick')
    kansPerMaatsoort(beatsPerMeasure, kansSnare,'snare')

#def selectList(name)



def kansPerMaatsoort(beatsPerMeasure, lijst, name):
    global lijst0, lijst2, lijst3, lijst4
    lijst1 = [6]
    lijst2 = [10,2]
    lijst3 = [7,2,2]
    lijst4 = [10,3,5,2]
    if beatsPerMeasure == 4:
        lijst.append(lijst(3+x))
        lijst.append(lijst1)
        print("kansKick=", kansKick)
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

def callcheck():
    print("sequenceSnareN", sequenceSnare)
    check(sequenceKick, sequenceSnare, test)
    print("sequenceSnare", sequenceSnare)
def check(lijstKick, lijstSnare, appendList):
    #global sequenceSnare
    #print(sequenceSnare)
    listCheck = [x for x in lijstSnare if x not in lijstKick]
    appendList.extend(listCheck)
    print("test", test)

def transformKansList():
    global kansListKick, kansListSnare
    random.shuffle(kansKick,random.random)
    random.shuffle(kansSnare,random.random)
    kansListKick  = list(itertools.chain(*kansKick))
    kansListSnare = list(itertools.chain(*kansSnare))

#hier wordt een functie aangeroepen uit 'randomNumber2.py' die een lijst aanmaakt door de kans lijst hierboven te
#vergelijken met een random lijst die wordt gegenereerd in randomNumber2.py
def makeRandomList(beatsPerMeasure):
    #print(kansListKick)
    #print(kansListSnare)#events = []
    #beatsPerMeasure = 10
    #generates random list of numberen between 1 and 10, the outcome is compared to the probability
    uitkomst = [ random.randint(1, 10) for _ in range(beatsPerMeasure) ]
    #calls function in randomNumber2.py to generate list
    rm.generateList(kansListKick, sequenceKick, uitkomst, beatsPerMeasure)
    rm.generateList(kansListSnare, sequenceSnareNotchecked, uitkomst, beatsPerMeasure )
    rm.generateList(kansHihat, sequenceHihat, uitkomst, beatsPerMeasure)
    #cals function in samplerMidiRythm.py to generate MIDI file
    midi.generateMIDI(kansListKick,35,  uitkomst, beatsPerMeasure)
    midi.generateMIDI(kansListSnare,38, uitkomst, beatsPerMeasure)
    midi.generateMIDI(kansHihat,42, uitkomst, beatsPerMeasure)
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
    print("sequenceSnareNot in makeList",sequenceSnareNotchecked)
    listCheck = [x for x in sequenceSnareNotchecked if x not in sequenceKick]
    sequenceSnare.extend(listCheck)
    print("sequenceSnare in makeList",sequenceSnare)
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

def clearLists():
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
