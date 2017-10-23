from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile
import random

"""
Documentation about midiutil:
http://midiutil.readthedocs.io/en/stable/
This script contains an example from https://pypi.python.org/pypi/MIDIUtil/.
It generates a midi file with a major scale.
HANDS-ON TIPS
...
"""
#TODO - add HANDS-ON TIPS

listMidi = [[0.0, 'kick'], [0.0, 'hihat'], [0.15, 'hihat'], [0.3, 'hihat'], [0.44999999999999996, 'hihat'], [0.6, 'hihat'], [0.75, 'hihat'], [0.8999999999999999, 'hihat'], [1.05, 'hihat'], [1.2, 'hihat'], [1.3499999999999999, 'hihat']]
print(listMidi[1])

a = 0
maatsoort = 7
counter = 0
x = counter

#uitkomst = [ random.randint(1, 10) for _ in range(maatsoort) ]

#kansKick =  [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#kansSnare = [0, 2, 2, 2, 7, 2, 2, 2, 0, 2, 2, 2, 7, 2, 2, 2, ]
#kansHihat = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

listElement = listMidi[0]
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
MyMIDI = MIDIFile(2)
#set track, tempo and time
MyMIDI.addTempo(track, time, bpm)

#set time signature
"""
addTimeSignature(track, time, numerator, denominator, clocks_per_tick, notes_per_quarter=8)
The denominator should be specified as a power of 2, with a half note being
one, a quarter note being two, and eight note being three, etc. Thus, for
example, a 4/4 time signature would have a numerator of 4 and a denominator of
2. A 7/8 time signature would be a numerator of 7 and a denominator of 3.
The clocks_per_tick argument specifies the number of clock ticks per metronome
click. By definition there are 24 ticks in a quarter note, so a metronome click
per quarter note would be 24. A click every third eighth note would be
3 * 12 = 36.
"""
"""
MyMIDI.addTimeSignature(track, 0, 7, 3, 24)

#adding a 7/8 rhythm
#add bassdrum
MyMIDI.addNote(track, channel, 35, 0, duration, velocity)
#add snare
MyMIDI.addNote(track, channel, 38, 3 * duration, duration, velocity)
#add hi-hat
for i in range(7):
    MyMIDI.addNote( track, channel, 42, (time + i) * duration, duration,
                    velocity)
"""
def generateMIDI(lijstKans, midiNote, uitkomst, beatsPerMeasure):
    counter = 0
    x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(a, maatsoort):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == maatsoort:
            generateList = False
        else:
            #print(lijstKans[i], uitkomst[i], lijstKans[i] >= uitkomst[i])#hier wordt lijst 'uitkomst' met lijst 'kans<instrument>' vergeleken
            if lijstKans[i] >= uitkomst[i]:#'i' staat hier voor het indexnummer
                MyMIDI.addNote( track, channel, midiNote, (time + i) * duration, duration, velocity)
                counter += 1
            else:
                pass



def printMIDI():
    with open("beat.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)


#generateMIDI(kansKick,35)
#generateMIDI(kansSnare,38)
#generateMIDI(kansHihat,42)
#write to MIDIfile
#with open("beat.mid", "wb") as output_file:
    #MyMIDI.writeFile(output_file)
