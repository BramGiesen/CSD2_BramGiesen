from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile
import random


track    = 0
#used midi channel
channel  = 9
#set time, in beats
time     = 0
#set duration in beats, 0.5 -> .../8 time signature
duration = 0.5
#set bpm
bpm    = 120
#set velocity
velocity   = 100  # 0-127, as per the MIDI standard

#number of beats

#create a track - defaults to format 2 - to enable addTimeSignature functionality
MyMIDI = MIDIFile(2, adjust_origin=True)
#set track, tempo and time
MyMIDI.addTempo(track, time, bpm)

def convertListForMidi(lijstA, lijstB):
    for i in range(beatsPerMeasure):
        if lijstA[i] == 1:
            lijstB.append(i)
    return lijstB


def generateMIDI(lijst, midiNote, beatsPerMeasure):
    counter = 0 #sets counter to zero
    # x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(beatsPerMeasure):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == beatsPerMeasure:
            generateList = False
        else:
            if i in lijst:
                MyMIDI.addNote( track, channel, midiNote, (time + i) * duration, duration, velocity)#In this line 'i' is time of event
                counter += 1
            else:
                pass



def printMIDI():#Write a MIDI file
    print('MIDI file is saved')
    with open("beat.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)


# print(midiList)
