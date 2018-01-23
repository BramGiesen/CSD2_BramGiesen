import random
import itertools
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
        lijst.append(lijst3)
        lijst.append(lijst2)
    if beatsPerMeasure == 7:
        lijst.append(lijst2)
        lijst.append(lijst3)
        lijst.append(lijst2)
    if beatsPerMeasure == 9:
        x = random.randint(0,1)
        if x == 1:
            lijst.append(lijst3)
            lijst.append(lijst2)
            lijst.append(lijst2)
            lijst.append(lijst1)
        else:
            lijst.append(lijst3)
            lijst.append(lijst4)
            lijst.append(lijst1)

    return lijst

###############################################################################

#function that rotates a list
def rotate(l, n):
    return l[n:] + l[:n]

def transformKansList(kansList):
    y = random.randint(0,3)#generates random number to rotate the "building blocks" of 4,3,2 and 1 in the list
    rotate(kansList, y)
    kans = list(itertools.chain(*kansList))#from a list within a list to a flat list
    #kansKick.extend(lijst1) # om een bug "op te lossen?"
    #kansSnare.extend(lijst5)

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
    a = 0
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(a, beatsPerMeasure):
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

# check for similarities and remove them.
def checkList(lijstSnare, lijstKick, lijstAppend, beatsPerMeasure):
    global sequenceHihat, sequenceKick, sequenceSnareNotchecked, sequenceHihatNotchecked
    counter = 0
    x = counter
    a = 0
    for i in range(a, beatsPerMeasure):
        if lijstKick[i] == lijstSnare[i]:
            lijstAppend.append(0)
        else:
            lijstAppend.append(lijstSnare[i])
    return lijstAppend
