import sys
from sys import stdin
import _thread
import time


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
BPM = str(myinteger)

def audioThreadFunction():

    while True:
        if startSampler == 1:
            print("sampler")
            time.sleep(1)
        else:
            pass
welkom()

try:
   _thread.start_new_thread(audioThreadFunction,())
except:
   print("Error: unable to start thread")

while True:
  result = input("Choose time signature: (1) 5/4  (2) 7/4  (3) 9/4 : ")
  if result == 'q':
    print("User typed q. Leaving program.")
    sys.exit()
  else:
      if result.isdigit() and 1 <= int(result) <= 3:
         result = result
         resultNumber = result
         BPM = input("Choose a BPM : ")
      if BPM.isdigit() and 1 <= int(BPM) <= 200:
             startSampler = 1
             result = resultNumber


      else:
         print("Choose a number between 1 and 3 or press q to quit")



  time.sleep(0.1)
