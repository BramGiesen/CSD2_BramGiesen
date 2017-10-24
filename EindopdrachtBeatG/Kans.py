import itertools
import random

beatsPerMeasure = 8
lijstKickKans = []
lijstSnareKans = []
lijstHihatKans = []

def maatsoort(beatsPerMeasure):
    lijst2 = [10,4]
    lijst3 = [10,4,4]
    lijst4 = [10,4,6,4]
    if beatsPerMeasure == 4:
        lijstKickKans.append(lijst3)
    if beatsPerMeasure == 6:
        lijstKickKans.append(lijst2)
        lijstKickKans.append(lijst3)
    if beatsPerMeasure == 8:
        x = random.randint(0,1)
        print(x)
        if x == 1:
            lijstKickKans.append(lijst3)
            lijstKickKans.append(lijst2)
            lijstKickKans.append(lijst2)
        else:
            lijstKickKans.append(lijst3)
            lijstKickKans.append(lijst4)



maatsoort(beatsPerMeasure)
random.shuffle(lijstKickKans,random.random)
merged = list(itertools.chain(*lijstKickKans))
print(merged)





#checks for equals in list and removes them
def check(lijstA, lijstB, appendList):
    listCheck = [x for x in lijstB if x not in lijstA]
    appendList.extend(listCheck)



check(lijstKick, lijstSnare, lijstSnareA)
print(lijstSnareA)#checkList(lijstSnare, lijstKick)
