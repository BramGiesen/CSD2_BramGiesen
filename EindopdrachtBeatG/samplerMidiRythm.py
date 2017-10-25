from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile
import random

#TODO Check of er een bepaald getal in de event lijst staat dus bij 'i' is 1, check of er een 1 in de event lijst staat
#myList = [1,2,3,4,5]
#
#if 3 in myList:
#    print("3 is present")


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

def generateMIDI(lijst, midiNote, beatsPerMeasure):
    beatsPerMeasure =  beatsPerMeasure - 1 #corrects offset beatsPerMeasure
    counter = 0 #sets counter to zero
    a = 0 #start counting from 0
    x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(a, beatsPerMeasure):
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


#generateMIDI(kansKick,35)
#generateMIDI(kansSnare,38)
#generateMIDI(kansHihat,42)
#write to MIDIfile
#with open("beat.mid", "wb") as output_file:
    #MyMIDI.writeFile(output_file)
