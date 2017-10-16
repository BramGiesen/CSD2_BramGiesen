import random
import time

maatsoort = 8 #bepaald de hoeveeldheid "beats"

#genereert een lijst gelijk met het aantal beats met getallen tussen 1 en 10
uitkomst = [ random.randint(1, 10) for _ in range(maatsoort) ]
sequenceKick  = []
sequenceSnare = []
sequenceHihat = []
#de lijst "uitkomst" wordt vergeleken met deze lijsten, 10 is 100% kans, 1 weinig kans
kansKick = [10, 2, 7, 3, 3, 2, 10, 10]
kansSnare = [0, 2, 2, 2, 7, 2, 2, 2]
kansHihat = [10, 10, 10, 10, 10, 10, 10, 10]
generateList = True
a = 0

#hier wordt de lijst gegenereert
def generateList(lijstKans, lijstAppend):
    counter = 0
    x = counter
    #bepaald de range, dus hoe vaak de procedure wordt doorlopen
    for i in range(a, maatsoort):
    #wanneer de counter het aantal gegeven beats heeft doorlopen stopt de functie
        if counter == maatsoort:
            generateList = False
        else:#hier wordt lijst 'uitkomst' met lijst 'kans<instrument>' vergeleken
            if lijstKans[i] >= uitkomst[i]:#'i' staat hier voor het indexnummer
                lijstAppend.append(i)#'i' staat hier voor de tijd van het event
                counter += 1
            else:
                pass


def printList():

    print(sequenceKick)
    print(sequenceSnare)
    print(sequenceHihat)



generateList(kansKick, sequenceKick)
generateList(kansSnare,sequenceSnare)
generateList(kansHihat,sequenceHihat)

printList()



# import randomNumber.py as randN

# randN.generateList(randN.kansKick, randN.sequenceKick, 8)
