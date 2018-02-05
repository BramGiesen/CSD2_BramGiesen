from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile
import random
from sys import stdin

import bcolors as colors

# converts list for the sample player to time events for midi file
def convertListForMidi(lijstA, lijstB, beatsPerMeasure):
    del lijstB[:]
    for i in range(beatsPerMeasure):
        if lijstA[i] == 1:
            lijstB.append(i)
    return lijstB

def generateMIDI(lijstKick, lijstSnare, lijstHihat, beatsPerMeasure, MIDIname, tempo):

    track    = 0
    #used midi channel
    channel  = 9
    #set time, in beats
    time     = 0
    #set duration in beats, 0.5 -> .../8 time signature
    duration = 0.5
    #set bpm
    bpm    = tempo
    #set velocity
    velocity   = 100  # 0-127, as per the MIDI standard
    #create a track - defaults to format 2 - to enable addTimeSignature functionality

    if beatsPerMeasure > 7:
        n = 2
    else:
        n = 1

    numerator = int(beatsPerMeasure / n)
    
    if not(beatsPerMeasure % 5):
        d = 2
    else:
        d = 3

    denominator = d

    MyMIDI = MIDIFile(2, adjust_origin=True)
    #set track, tempo and time
    MyMIDI.addTempo(track, time, bpm)
    #set timeSignature
    MyMIDI.addTimeSignature(track, time, numerator, denominator, clocks_per_tick=24, notes_per_quarter=8)

    counter = 0 #sets counter to zero

    for i in range(beatsPerMeasure):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == beatsPerMeasure:
            generateList = False
        else:
            if i in lijstKick:
                MyMIDI.addNote( track, channel, 35, (time + i) * duration, duration, velocity)#In this line 'i' is time of event
                # counter += 1
            if i in lijstSnare:
                MyMIDI.addNote( track, channel, 38, (time + i) * duration, duration, velocity)#In this line 'i' is time of event
                # counter += 1
            if i in lijstHihat:
                MyMIDI.addNote( track, channel, 42, (time + i) * duration, duration, velocity)#In this line 'i' is time of event
                counter += 1
            else:
                pass

    # export a midi file
    with open(MIDIname, "wb") as output_file:
        MyMIDI.writeFile(output_file)

    print(colors.bcolors.GREEN + 'MIDI file is saved as: "'+ MIDIname + '"' + colors.bcolors.ENDC)
