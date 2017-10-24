import sys
from sys import stdin
import _thread
import time
import samplePlayerVersie6 as sp
import random
import samplerMidiRythm as midi
import threading


def welkom():

    print("""
//    ___                       _            ___           _      ___                       _
//   |_ _|_ _ _ _ ___ __ _ _  _| |__ _ _ _  | _ ) ___ __ _| |_   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _
//    | || '_| '_/ -_) _` | || | / _` | '_| | _ \/ -_) _` |  _| | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
//   |___|_| |_| \___\__, |\_,_|_\__,_|_|   |___/\___\__,_|\__|  \___\___|_||_\___|_| \__,_|\__\___/_|
//                   |___/ """)

ask = True
myinteger = 0
result = str(myinteger)
startSampler = False
BPM = int(myinteger)
tempo = 0
beatsPerMeasure = 0
startSampler = 0
sp.playbackLoop = False

def audioThreadFunction():
    global beatsPerMeasure, tempo, events


    while True:
        # print("fiets", tempo, beatsPerMeasure)


        # print("startSampler = ", int(startSampler))
        if startSampler:
            # print("      startSampler is 1!!!!")
            #sp.makeRandomList(beatsPerMeasure)
            #events = sp.makeList(tempo, beatsPerMeasure, )#set BPM and beatsPerMeasure in samplePlayerVersie6.py
            sp.playBack(events)#starts sampler in samplePlayerVersie6.py
            time.sleep(1)
        else:
            time.sleep(1)

sp.playStartTone()
welkom()#prints 'random beat generator' banner

try:#try's to start program
   _thread.start_new_thread(audioThreadFunction,())
except:# if the program doesn't work
   print("Error: unable to start thread")

while True:#select a time signature

  result = input("Choose time signature: (1) 3/4  (2) 5/4  (3) 7/4 : \n")
  if result == 'q':
    x = 0.0
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
  elif result == 'y':
    midi.printMIDI()
  else:
    # print("auto")
    if result.isdigit() and 1 <= int(result) <= 3:#sets a range for the user input between 1 and 3
        #_thread.stop(audioThreadFunction,())
        sp.playbackLoop = False
        maatsoort = int(result)#user input from string to int
        signature = [0, 4, 6, 10]#list with time signatures
        beatsPerMeasure=signature[maatsoort]#selects element from list signature
        BPM = input("Choose a BPM : ")
        startSampler = False
        if BPM.isdigit() and 1 <= int(BPM) <= 200:
            tempo = int(BPM)#input to int
            #print("ik ben nu hier")#sp.bpm=tempo#adjusts variable tempo in 'samplePlayerVersie6'
            sp.makeRandomList(beatsPerMeasure)
            events = sp.makeList(tempo, beatsPerMeasure, )#set BPM and beatsPerMeasure in samplePlayerVersie6.py
            startSampler = True #is linked to 'audioThreadFunction' which is linked to the sample player 'samplePlayerVersie6' aanspreekt
            sp.playbackLoop = True
            #print("startSampler = ", int(startSampler))

    else:#when the user input is wrong it prints this message
        print("u fucked up")
        print("Choose a number between 1 and 3 or press q to quit")



  time.sleep(0.1)
