import random
import itertools


#===============================================================================
#algorithm for basic measure layout

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

#function that rotates a list
def rotate(l, n):
    return l[n:] + l[:n]

def transformKansList(kansList):
    y = random.randint(0,1)#generates random number to rotate the "building blocks" of 4,3,2 and 1 in the list
    rotate(kansList, y)
    kans = list(itertools.chain(*kansList))#from a list within a list to a flat list
    return kans

###############################################################################
#random part

#makes a list of random values between 1 and 10, the size of the list is equal to the beatsPerMeasure
def makeRandomList(beatsPerMeasure):
    #generates random list of numberen between 1 and 10, the outcome is compared to the probability
    uitkomst = [ random.randint(1, 10) for _ in range(beatsPerMeasure) ]
    return uitkomst

#compares the list with the chance variables with the random generated list
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
#snare algorithm

# check for similarities and remove the snares that have the same index number as the kick
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

#if there are no snares left after the function, checkList, this function adds one snare
def addASnare(kickList, snareList, beatsPerMeasure):
    for i in range(beatsPerMeasure):
        if kickList[i] == 0:
            getNewSnare.append(i)#if index in listKick is 0, add position of 0 in getNewSnare list

    indexSnare = (random.choice(getNewSnare))#choose a random index number
    del snareList[-1]#trim list
    snareList.insert(indexSnare, 1)#add a new snare
    return snareList

#if there is only one snare on the 11th beat this function adds to "random" snares
def addMoreSnares(newKick, newSnares, beatsPerMeasure):
    lijst = []
    for i in range(beatsPerMeasure):
        if i > 3 and i < 10 and newKick[i] == 0:
            lijst.append(i)
    lijst = random.sample(lijst, 2)
    lijst.append(10)
    lijst.sort()
    dif = (lijst[2] - lijst[1]) + (lijst[1] - lijst[0])
    if dif <= 2:
        element = lijst[1]
        element = element - random.randint(2,4)
        lijst[1] = element
        lijst.sort()
    return lijst

#===============================================================================
#Hihat algorithm

#puts every position off a trigger for kick and snare in one list
def countTriggers(newKick,newSnares, hihat, beatsPerMeasure):
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
    return hihat

#===============================================================================
#if the generator is in modus 2 this function doubles note intensity

#converts list [1,1,1,1] to [1,0,1,0,1,0] etc...
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

#returns all index number where there is no snare, if there is a snare it returns None
def searchForNotSnare(snareList):
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

#split function for list
def _lsplit(l, splitters):
    lijst = []
    for element in l:
        if element in splitters:
            yield lijst
            lijst = []
        else:
            lijst.append(element)
    yield lijst

def split(l, *splitters):
    return [subl for subl in _lsplit(l, splitters) if subl]

#takes list with all index numbers where there is no snare en chooses random
def getKickPosition(*argv):
    l = []
    for arg in argv:#splits argv in seperate arguments
        n = len(arg) #checks lenght of list
        for i in range(0, n):
            argEven = arg[i][::2] #gets all "on-beat" indexes in list
            argOneven = arg[i][1::2] #gets all "off-beat" indexes
            if len(arg[i]) >= 5:#takes a amount of random indexes from list depending on it's size
                kansEven =  random.randint(1, 2)
                kansOneven =  random.randint(0, 1)
                resultEven = random.sample(argEven, kansEven)#take 2 or 1 random elements out of list
                resultOneven = random.sample(argOneven, kansOneven)
                l.append(resultEven)
                l.append(resultOneven)
            if len(arg[i]) <= 4 and len(arg[i]) > 1:
                kansOneven =  random.randint(0, 1)
                resultEven = random.sample(argEven, 1)#take 1 random elements out of list
                resultOneven = random.sample(argOneven, kansOneven)
                l.append(resultEven)
                l.append(resultOneven)
            if len(arg[i]) == 1:
                resultEven = argEven
                resultOneven = argOneven
                l.append(resultEven)
                l.append(resultOneven)
            if  arg[i] == []:
                l.append(0)
    merged = list(itertools.chain(*l))
    merged.sort()
    return merged


def eventsToIndex(lijst, beatsPerMeasure):#set event index message 0, 2 to 1,0,1 etc....
    indexList= [0] * beatsPerMeasure
    for i in lijst:
        indexList[i] = 1
    return indexList
