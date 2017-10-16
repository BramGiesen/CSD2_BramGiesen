import random
import time

maatsoort = 8


uitkomst = [ random.randint(1, 10) for _ in range(maatsoort) ]
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
kansKick = [10, 2, 7, 3, 3, 2, 10, 10]
kansSnare = [0, 2, 2, 2, 7, 2, 2, 2]
kansHihat = [10, 10, 10, 10, 10, 10, 10, 10]#10 is honderdprocent kans
#het eerste elememt zou de outcome moeten zijn, tweede is kas kans
generateList = True
a = 0
b = 8

def generateList(lijstKans, lijstAppend, selected_index):
    counter = 0
    x = counter
    for i in range(a, b):
        if counter == selected_index:
            generateList = False
        else:
            if lijstKans[i] >= uitkomst[i]:#altijd een kick op de één
                lijstAppend.append(i)#zorgen dat de uitkomst naar 3 verschillende lijsten kan
                counter += 1
            else:
                pass


def printList():

    print(sequenceKick)
    print(sequenceSnare)
    print(sequenceHihat)



generateList(kansKick, sequenceKick,  8)
generateList(kansSnare,sequenceSnare, 8)
generateList(kansHihat,sequenceHihat, 8)

printList()
