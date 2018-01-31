import random
import itertools

getNewSnare = []

#rythmic blocks of 2, 3, or 4 beats; for example a 7/4 time signature can be build from one block of 3 and of 4 or from two blocks of 2 and one of 3
def selectList(name):
    global lijst1, lijst2, lijst3, lijst4, lijst5
    lijst5 = [6]
    if name == 'kick':# the numbers in the list are probability, 10 is 100%, 0 is 0%
        lijst1 = [0]
        lijst2 = [10,0]
        lijst3 = [7,0,3]
        lijst4 = [10,0,0,1]
    if name == 'snare':
        lijst1 = [0]
        lijst2 = [10,2]
        lijst3 = [10,7,3]
        lijst4 = [10,7,4,2]


#puts building blocks in list
def kansPerMaatsoort(beatsPerMeasure, lijst, name):
    selectList(name)
    if beatsPerMeasure == 5:
        lijst = [lijst3] + [lijst2]
    if beatsPerMeasure == 7:
        lijst = [lijst2] * 2 + [lijst3]
    if beatsPerMeasure == 9:
        x = random.randint(0,1)
        if x == 1:
            lijst = [lijst3] + ([lijst2] * 3)
        else:
            lijst = [lijst3]+[lijst4]+[lijst2]
    return lijst

###############################################################################

#function that rotates a list
def rotate(l, n):
    return l[n:] + l[:n]

def transformKansList(kansList):
    y = random.randint(0,3)#generates random number to rotate the "building blocks" of 4,3,2 and 1 in the list
    rotate(kansList, y)
    kans = list(itertools.chain(*kansList))#from a list within a list to a flat list
    return kans

###############################################################################


def makeRandomList(beatsPerMeasure):
    #generates random list of numberen between 1 and 10, the outcome is compared to the probability
    uitkomst = [ random.randint(1, 10) for _ in range(beatsPerMeasure) ]
    return uitkomst



def generateList(lijstKans, lijstAppend, uitkomst,beatsPerMeasure):
    global sequenceHihat, sequenceKick, sequenceSnareNotchecked, sequenceHihatNotchecked
    counter = 0
    x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(beatsPerMeasure):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == beatsPerMeasure:
            #printList()
            generateList = False
        else:
            #print(lijstKans[i], uitkomst[i], lijstKans[i] >= uitkomst[i])#-> list 'uitkomst' compared to 'kans<instrument>'
            if lijstKans[i] >= uitkomst[i]:#'i' is indexnumber
                lijstAppend.append(1)#'i' is time of event
                counter += 1
            else:
                lijstAppend.append(0)
    return lijstAppend

#==============================================================================
# check for similarities and remove them.
def checkList(lijstSnare, lijstKick, lijstAppend, beatsPerMeasure):
    global sequenceHihat, sequenceKick, sequenceSnareNotchecked, sequenceHihatNotchecked
    counter = 0
    x = counter
    for i in range(beatsPerMeasure):
        if lijstKick[i] == lijstSnare[i]:
            lijstAppend.append(0)
        else:
            lijstAppend.append(lijstSnare[i])
    return lijstAppend

def addASnare(kickList, snareList, beatsPerMeasure):
    for i in range(beatsPerMeasure):
        if kickList[i] == 0:
            getNewSnare.append(i)#if index in listKick is 0, add position of 0 in getNewSnare list

    indexSnare = (random.choice(getNewSnare))#choose a random index number
    del snareList[-1]#trim list
    snareList.insert(indexSnare, 1)#add a new snare
    return snareList

def countTriggers(newKick,newSnares, hihat, beatsPerMeasure):#puts every potion when there is a trigger from the kick and hihat in one list
    kickSnareTriggers = []
    for i in range(beatsPerMeasure):
        if newKick[i] + newSnares[i] > 0:
            kickSnareTriggers.append(1)
        else:
            kickSnareTriggers.append(0)
    hihat = addHihats(kickSnareTriggers, hihat, beatsPerMeasure)
    return hihat

def addHihats(kickSnareTriggers, hihat, beatsPerMeasure):
    for i in range(beatsPerMeasure):
        if kickSnareTriggers[i] == 0:
            chance = random.randint(0,100)
            if chance > 25:
                hihat[i] = 1
        if kickSnareTriggers[i] == 1:
                chance = random.randint(0,100)
                if chance > 50:
                    hihat[i] = 0
                # chance = random.randint(0,100) TODO nog naar kijken!

    return hihat

#==============================================================================
#double note intensity

def doubleNotes(lijst, beatsPerMeasure, times):
    index = 1
    while True:
        if index > beatsPerMeasure * times:
            return lijst
        if index % 2 == 1:
            lijst.insert(index, 0)
            index =  index + 2
