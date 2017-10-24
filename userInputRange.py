import sys
from sys import stdin
import _thread
import time
import samplePlayerVersie6 as sp
import random
import samplerMidiRythm as midi

#TODO wanneer de beat gaat afspelen, vraag of deze omgezet moet worden in MIDI
#zorg voor een beatsPerMeasure in alle bestanden

def welkom():

    print("""
//    ___                       _            ___           _      ___                       _
//   |_ _|_ _ _ _ ___ __ _ _  _| |__ _ _ _  | _ ) ___ __ _| |_   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _
//    | || '_| '_/ -_) _` | || | / _` | '_| | _ \/ -_) _` |  _| | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
//   |___|_| |_| \___\__, |\_,_|_\__,_|_|   |___/\___\__,_|\__|  \___\___|_||_\___|_| \__,_|\__\___/_|
//                   |___/ """)

myinteger = 0
result = str(myinteger)
startSampler = 0
BPM = int(myinteger)
tempo = 0
beatsPerMeasure = 0

def audioThreadFunction():

    while True:
        if startSampler == 1:
            #beatsPerMeasure = 6
            #calculate = [ random.randint(1, 10) for _ in range(maatsoort) ]
            sp.makeRandomList(beatsPerMeasure)
            events = sp.makeList(tempo, beatsPerMeasure, )#set BPM and beatsPerMeasure in samplePlayerVersie6.py
            midi = sp.convertEventsToMidi(events)
            time.sleep(1)
            sp.playBack(events)#starts sampler in samplePlayerVersie6.py
            time.sleep(1)

            # give midi to lib#
            # for note in midi:
            #     MyMIDI.addNote(track, channel, note[1], note[0], duration, volume)

        else:
            pass

sp.playStartTone()
welkom()#prints 'random beat generator' banner

try:#try's to start program
   _thread.start_new_thread(audioThreadFunction,())
except:# if the program doesn't work
   print("Error: unable to start thread")

while True:#select a time signature
  result = input("Choose time signature: (1) 3/4  (2) 5/4  (3) 7/4 : ")
  if result == 'q':
    x = 0.1
    print("░░░░░░░░░░░░░░░░░░░░░░█████████")
    time.sleep(x)
    print("░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███")
    time.sleep(x)
    print("░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███")
    time.sleep(x)
    print("░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    time.sleep(x)
    print("░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███")
    time.sleep(x)
    print("░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██")
    time.sleep(x)
    print("░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    time.sleep(x)
    print("░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██")
    time.sleep(x)
    print("░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██")
    time.sleep(x)
    print("██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██")
    time.sleep(x)
    print("█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██")
    time.sleep(x)
    print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    time.sleep(x)
    print("░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    time.sleep(x)
    print("░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█")
    time.sleep(x)
    print("░░████████████░░░█████████████████ Bye!")
    sys.exit()
  if result == 'y':
    midi.printMIDI()

  else:
      if result.isdigit() and 1 <= int(result) <= 3:#sets a range for the user input between 1 and 3
         maatsoort = int(result)#user input from string to int
         signature = [0, 4, 6, 10]#list with time signatures
         beatsPerMeasure=signature[maatsoort]#selects element from list signature

         BPM = input("Choose a BPM : ")
      if BPM.isdigit() and 1 <= int(BPM) <= 200:
             tempo = int(BPM)#input to int
             sp.bpm=tempo#adjusts variable tempo in 'samplePlayerVersie6'
             startSampler = 1 #is linked to 'audioThreadFunction' which is linked to the sample player 'samplePlayerVersie6' aanspreekt
             print("""♫ Do you want to save this beat? ♫
pres y
♫ If you want a different beat? ♫
please give a new time signature and BPM """)#het saven van de beat moet door midi te exporten maar dit heb ik nog niet gemaakt

      else:#when the user input is wrong it prints this message
         print("Choose a number between 1 and 3 or press q to quit")



  time.sleep(0.1)
