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
ask = True


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
ask = True


def ask():
    global ask
    ask == True

while True:

  while ask:
      noError = False
      result = input(colors.bcolors.BLUE + "enter 'g' for beat, enter 'setDrum' to select a different drumsound or 'q' to quit : \n" + colors.bcolors.ENDC)
      if result == 'q':
          sys.exit()
      if result =='setDrum':
          settingDrums = True
          while settingDrums:
              setDrum = input(colors.bcolors.BLUE + "choose drumsamples : (1) acoustic (2) electric : \n" + colors.bcolors.ENDC)
              if setDrum.isdigit() and 1 <= int(setDrum) <= 2:#sets a range for the user input between 1 and 3
                  setDrum = int(setDrum)
                  if setDrum == 1:
                      player.setGlobalS(0)
                      print(colors.bcolors.GREEN + "selected drumsound : acoustic" + colors.bcolors.ENDC)
                  else:
                      player.setGlobalS(3)
                      print(colors.bcolors.GREEN + "selected drumsound : electic" + colors.bcolors.ENDC)
                  noError = True
                  settingDrums = False
              else:
                  print(colors.bcolors.RED + "please enter '1' or '2'" + colors.bcolors.ENDC)
      if result == 'g':
          g = True
          while g:
              result = input(colors.bcolors.BLUE + "Choose time signature: (1) 5/4  (2) 7/8 : \n" + colors.bcolors.ENDC)
              if result.isdigit() and 1 <= int(result) <= 2:#sets a range for the user input between 1 and 2
                player.playbackLoop = False
                main.main = False
                beatsPerMeasure = beatsPerMeasureList[(int(result)-1)]#user input from string to int
                g = False
                noBPM = True
                while noBPM:
                    BPM = input(colors.bcolors.BLUE + "Choose a BPM : \n" + colors.bcolors.ENDC)
                    if BPM.isdigit() and 1 <= float(BPM) <= 600:
                        global tempo
                        tempo = float(BPM)
                        noBPM = False
                        # modus = input(colors.bcolors.BLUE + "choose smallest note value: (1) Quarter note (2) Eight note : \n" + colors.bcolors.ENDC)
                        noModus = True
                        while noModus:
                            modus = input(colors.bcolors.BLUE + "choose smallest note value: (1) Quarter note (2) Eight note : \n" + colors.bcolors.ENDC)
                            if modus.isdigit() and 1 <= int(modus) <= 2:
                                modi = int(modus)
                                main.setModus(modi)
                                noModus = False
                                main.main = True
                                player.playbackLoop = True
                                startSampler = True
                                ask = False
                            else:
                                print(colors.bcolors.RED + "invalid answer, please enter number 1 or 2" + colors.bcolors.ENDC)
                    else:
                       print(colors.bcolors.RED + "choose a bpm between 1 and 600" + colors.bcolors.ENDC)
              else:#when the user input is wrong it prints this message
                    print(colors.bcolors.RED + "invalid answer, please enter number 1 or 2" + colors.bcolors.ENDC)
      else:
          if noError == False:
              print(colors.bcolors.RED + "invalid choice, please enter again" + colors.bcolors.ENDC)
  else:
      result = input()
      main.main = False
      player.playbackLoop = False
      if result == 'q':
          sys.exit()
      if result == 'y':
          notSaved = True
          while notSaved:
              MIDIname = input((colors.bcolors.RED + "name your MIDI file and press ENTER : \n" + colors.bcolors.ENDC))
              str = MIDIname;
              if "/" not in MIDIname:
                  suffix = ".mid";
                  if str.endswith(suffix) == False:#adds .mid to filename
                    MIDIname += '.mid'
                    main.midiGen("midi/"+MIDIname)
                    notSaved = False
                    ask = True
                  else:
                    main.midiGen("midi/"+MIDIname)
                    notSaved = False
                    ask = True
              else:
                  print(colors.bcolors.RED + "Filename can't contain /" + colors.bcolors.ENDC)
      else:
          ask = True
          # except SyntaxError:
          #     pass
  time.sleep(0.1)
