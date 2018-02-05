import random
import itertools


#===============================================================================
#Snare algorithm

getNewSnare = []


#rythmic blocks of 2, 3, or 4 beats; for example a 7/4 time signature can be build from one block of 3 and of 4 or from two blocks of 2 and one of 3
def selectList(name):
    global lijst1, lijst2, lijst3, lijst4, lijst5
    lijst5 = [6]
    if name == 'kick':# the numbers in the list are probability, 10 is 100%, 0 is 0%
        # lijst1 = [0]
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

#===============================================================================
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
#===============================================================================
#Hihat algorithm
def countTriggers(newKick,newSnares, hihat, beatsPerMeasure):#puts every position off a trigger for kick and snare in one list
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

#===============================================================================
#double note intensity

def doubleNotes(lijst, beatsPerMeasure, times):
    index = 1
    while True:
        if index > beatsPerMeasure * times:
            return lijst
        if index % 2 == 1:
            lijst.insert(index, 0)
            index =  index + 2


#===============================================================================
#Kick algorithm

def searchForNotSnare(snareList):#returns all index number where there is no snare, if there is a snare it returns None
    index  = 0
    lijst = []
    for i in snareList:
        if i == 0:
            lijst.insert(index, index)
            index = index + 1
        else:
            lijst.insert(index, None)
            index = index + 1
    return lijst

def _itersplit(l, splitters):#split function for list
    current = []
    for item in l:
        if item in splitters:
            yield current
            current = []
        else:
            current.append(item)
    yield current

def split(l, *splitters):
    return [subl for subl in _itersplit(l, splitters) if subl]


def getKickPosition(*argv):#takes list with all index numbers where there is no snare en chooses random
    l = []
    for arg in argv:
        n = len(arg) #checks lenght of list
        for i in range(0, n):
            argEven = arg[i][::2]
            argOneven = arg[i][1::2]
            if len(arg[i]) >= 5:
                kansEven =  random.randint(1, 2)
                kansOneven =  random.randint(0, 1)
                resultEven = random.sample(argEven, kansEven)#take 2 random elements out of list
                resultOneven = random.sample(argOneven, kansOneven)
                l.append(resultEven)
                l.append(resultOneven)
            if len(arg[i]) <= 4 and len(arg[i]) > 1:
                kansOneven =  random.randint(0, 1)
                resultEven = random.sample(argEven, 1)#take 2 random elements out of list
                resultOneven = random.sample(argOneven, kansOneven)
                l.append(resultEven)
                l.append(resultOneven)
            if len(arg[i]) == 1:# TODO checken wat ik met 1 wil doen
                resultEven = argEven #take 2 random elements out of list
                resultOneven = argOneven
                l.append(resultEven)
                l.append(resultOneven)
            if  arg[i] == []:
                l.append(0)
    merged = list(itertools.chain(*l))
    merged.sort()
    return merged


def eventsToIndex(lijst, beatsPerMeasure, newSnares):#set event index message 0, 2 to 1,0,1 etc....
    kickList= [0] * beatsPerMeasure
    for i in lijst:
        kickList[i] = 1
    if newSnares[0] == 0:
        kickList[0] = 1
    return kickList
