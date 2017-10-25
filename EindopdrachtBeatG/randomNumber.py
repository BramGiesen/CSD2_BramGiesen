import random
import time


#creates empty list
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
kansKick =  []
kansSnare = []
kansHihat = []
generateList = True
a = 0

#this function generates a list of 'random' events with possibility
def generateList(lijstKans, lijstAppend, uitkomst,beatsPerMeasure):
    global sequenceHihat, sequenceKick, sequenceSnareNotchecked, sequenceHihatNotchecked
    counter = 0
    x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(a, beatsPerMeasure):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == beatsPerMeasure:
            #printList()
            generateList = False
        else:
            #print(lijstKans[i], uitkomst[i], lijstKans[i] >= uitkomst[i])#-> list 'uitkomst' compared to 'kans<instrument>'
            if lijstKans[i] >= uitkomst[i]:#'i' is indexnumber
                lijstAppend.append(i)#'i' is time of event
                counter += 1
            else:
                pass



def check(lijstA, lijstB, appendList):
    listCheck = [x for x in lijstB if x not in lijstA]
    appendList.extend(listCheck)
