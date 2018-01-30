import main
import player
import midiProcessing as midi
import bcolors as colors


import sys
from sys import stdin
import _thread
import threading
import time
import random

global beatsPerMeasure
beatsPerMeasureList = [5, 7, 9]
myinteger = 0
result = str(myinteger)
BPM = float(myinteger)

startSampler = False
player.playbackLoop = False


print(colors.bcolors.PINK + """


//    ___                       _            ___           _      ___                       _
//   |_ _|_ _ _ _ ___ __ _ _  _| |__ _ _ _  | _ ) ___ __ _| |_   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _
//    | || '_| '_/ -_) _` | || | / _` | '_| | _ \/ -_) _` |  _| | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
//   |___|_| |_| \___\__, |\_,_|_\__,_|_|   |___/\___\__,_|\__|  \___\___|_||_\___|_| \__,_|\__\___/_|
//                   |___/


"""+ colors.bcolors.ENDC)


def audioThreadFunction():

    while True:
        if startSampler:
            # generate & play a beat
            main.makeAbeat(beatsPerMeasure, tempo)
        else:
            time.sleep(1)

try:#try's to start program
   _thread.start_new_thread(audioThreadFunction,())
except:# if the program doesn't work
   print("Error: unable to start thread")

while True:#select a time signature

  result = input(colors.bcolors.BLUE + "Choose time signature: (1) 5/4  (2) 7/8 (3) 9/8 : \n" + colors.bcolors.ENDC)
  if result == 'q':
    sys.exit()
  elif result == 'y':
    MIDIname = input((colors.bcolors.RED + "name your MIDI file and press ENTER : \n" + colors.bcolors.ENDC))
    str = MIDIname;
    suffix = ".mid";
    if str.endswith(suffix) == False:
        MIDIname += '.mid'
    main.midiGen(beatsPerMeasure, "midi/"+MIDIname)
  else:
      if result.isdigit() and 1 <= int(result) <= 3:#sets a range for the user input between 1 and 3
        player.playbackLoop = False
        beatsPerMeasure = beatsPerMeasureList[(int(result)-1)]#user input from string to int
        BPM = input(colors.bcolors.BLUE + "Choose a BPM : \n" + colors.bcolors.ENDC)
        if BPM.isdigit() and 1 <= float(BPM) <= 600:
            global tempo
            tempo = float(BPM)
            print(colors.bcolors.WELKOM + "if you like this beat, press 'y' to export or enter new time signature for a new beat"+ colors.bcolors.ENDC)
            player.playbackLoop = True
            startSampler = True
        else:#when the user input is wrong it prints this message
            print("Choose a number between 1 and 3 or press q to quit")

  time.sleep(0.1)
