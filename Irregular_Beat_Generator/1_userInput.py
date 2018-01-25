import main
import player
import midiProcessing as midi


import sys
from sys import stdin
import _thread
import threading
import time
import random



# import samplerMidiRythm as midi



def welkom():

    print("""
//    ___                       _            ___           _      ___                       _
//   |_ _|_ _ _ _ ___ __ _ _  _| |__ _ _ _  | _ ) ___ __ _| |_   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _
//    | || '_| '_/ -_) _` | || | / _` | '_| | _ \/ -_) _` |  _| | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
//   |___|_| |_| \___\__, |\_,_|_\__,_|_|   |___/\___\__,_|\__|  \___\___|_||_\___|_| \__,_|\__\___/_|
//                   |___/ """)


myinteger = 0
result = str(myinteger)
startSampler = False
player.playbackLoop = False
BPM = float(myinteger)

def audioThreadFunction():

    while True:
        if startSampler:
            main.makeAbeat(beatsPerMeasure, tempo)
            time.sleep(1)
        else:
            time.sleep(1)

welkom()#prints 'random beat generator' banner

try:#try's to start program
   _thread.start_new_thread(audioThreadFunction,())
except:# if the program doesn't work
   print("Error: unable to start thread")

while True:#select a time signature

  result = input("Choose time signature: (1) 5/4  (2) 7/8 : \n")
  if result == 'q':
    sys.exit()

  elif result == 'y':
    midi.printMIDI()

  else:
      if result.isdigit() and 1 <= int(result) <= 10:#sets a range for the user input between 1 and 3
        player.playbackLoop = False
        beatsPerMeasure = int(result)#user input from string to int
        BPM = input("Choose a BPM : \n")
        if BPM.isdigit() and 1 <= float(BPM) <= 600:
            global tempo
            tempo = float(BPM)
            print("if you like this beat, PRESS Y to export")
            player.playbackLoop = True
            startSampler = True




        else:#when the user input is wrong it prints this message
            print("Choose a number between 1 and 3 or press q to quit")



  time.sleep(0.1)
