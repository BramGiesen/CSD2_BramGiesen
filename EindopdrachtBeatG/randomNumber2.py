import random
import time


#creates empty list
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
#the list "uitkomst" is compared with these lists, 10 is 100% possibility, 0 is no possibility
kansKick =  []
kansSnare = []
kansHihat = []
generateList = True
a = 0

#this function generates a list of 'random' events with possibility
def generateList(lijstKans, lijstAppend, uitkomst,beatsPerMeasure):
    counter = 0
    x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(a, beatsPerMeasure):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == beatsPerMeasure:
            generateList = False
        else:
            #print(lijstKans[i], uitkomst[i], lijstKans[i] >= uitkomst[i])#-> list 'uitkomst' compared to 'kans<instrument>'
            if lijstKans[i] >= uitkomst[i]:#'i' is indexnumber
                lijstAppend.append(i)#'i' is time of event
                counter += 1
            else:
                pass


def printList():

    print(sequenceKick)
    print(sequenceSnare)
    print(sequenceHihat)
