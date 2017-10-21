import sys
from sys import stdin
import _thread
import time
import samplePlayerVersie6 as sp


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
            sp.makeList(tempo, beatsPerMeasure)#set BPM and beatsPerMeasure in samplePlayerVersie6.py
            sp.playBack()#starts sampler in samplePlayerVersie6.py
            time.sleep(1)
        else:
            pass
welkom()#prints 'random beat generator' banner

try:#try's to start program
   _thread.start_new_thread(audioThreadFunction,())
except:# if the program doesn't work
   print("Error: unable to start thread")

while True:#select a time signature
  result = input("Choose time signature: (1) 3/4  (2) 5/4  (3) 7/4 : ")
  if result == 'q':
    print("User typed q. Leaving program.")
    sys.exit()
  else:
      if result.isdigit() and 1 <= int(result) <= 3:

         maatsoort = int(result)
         signature = [3, 5, 7]
         sp.beatsPerMeasure=signature[maatsoort]
         BPM = input("Choose a BPM : ")
      if BPM.isdigit() and 1 <= int(BPM) <= 200:
             tempo = int(BPM)
             sp.bpm=tempo
             #sp.makeList(tempo)
             startSampler = 1


      else:
         print("Choose a number between 1 and 3 or press q to quit")



  time.sleep(0.1)
