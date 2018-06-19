import beatAlgo as ba
import player
import midiProcessing as midi
import bcolors as colors

midiKick  = []
midiSnare = []
midiHihat = []
previousBeat = []

main = False
modus = 2

#sets modus to 1 or 2, function is called from userInput.py
def setModus(number):
    global modus
    number = int(number)
    modus = number

#function to make and play a beat, function is called from userInput.py
def makeAbeat(beatsPerMeasure, tempo):
    global previousBeat, beatsPerMIDI, modus


    while main:

        kickKansList  = []
        SnareKansList = []
        kick  = []
        snare = []
        snareDef = []

        #makes a list with "building blocks" --> 5/4 is list with 3 elements and a list with 2 elements.
        #7/4 is list with 2*list of 2 elements en 1* list of 3 elements. All the elements contain numbers define the chance
        kansPMListKick = ba.kansPerMaatsoort(beatsPerMeasure, kickKansList, "kick")

        kansPMListSnare = ba.kansPerMaatsoort(beatsPerMeasure, SnareKansList, "snare")

        #rotates list with building blocks, so 5/4 can be 3+2 or 2+3 etc..
        NewkickKansList   = ba.transformKansList(kansPMListKick)

        NewSnareKansList   = ba.transformKansList(kansPMListSnare)

        #generate a random list to compare with the chances defined in new<>KansList
        uitkomst = ba.makeRandomList(beatsPerMeasure)

        #generate kickList
        newKick   = ba.generateList(NewkickKansList , kick, uitkomst, beatsPerMeasure)

        #generate snareList
        newSnare  = ba.generateList(NewSnareKansList , snare, uitkomst, beatsPerMeasure)

        #looks for similarity in the kick and snare lists, if there is kick the snare is removed
        newSnares = ba.checkList(newSnare, newKick, snareDef, beatsPerMeasure)

        # sums all snares
        sumSnare = sum(newSnares)

        if sumSnare == 0:#checks if there are snares in the generated beat
            newSnares = ba.addASnare(newKick, newSnares, beatsPerMeasure)
            newSnares = ba.checkList(newSnare, newKick, snareDef, beatsPerMeasure)
        else:
            beat = newSnares + newKick
            if beat == previousBeat:#check if the new beat is the same as te last beat
                makeAbeat(beatsPerMeasure, tempo)#generate a new Beat if they are the same
            else:#play the beat and covert list to a "midiList" with time events
                global midiKick, midiSnare, midiHihat, midiTempo

                #stores previousBeat to compare with the most recent beat, if they are the same a new beat is generated
                previousBeat = newSnare + newKick

                # print("beatsPerMeasure : ", beatsPerMeasure)
                midiTempo = tempo

                if beatsPerMeasure == 7:#because 7/8 counts in 8th notes the tempo is twice is fast as 5/4
                    tempo = tempo * 2

                h = [1] * beatsPerMeasure
                if modus == 1:
                    #double note function doubles the note depth, in modus 1 the 8th notes are not used
                    newKick = ba.doubleNotes(newKick, beatsPerMeasure, 2)
                    newSnares = ba.doubleNotes(newSnares, beatsPerMeasure, 2)
                    h = ba.doubleNotes(h, beatsPerMeasure, 2) #because the note depth is twice as high te tempo and beatsPerMeasure is * 2
                    beatsPerMeasure = beatsPerMeasure * 2
                    tempo = tempo * 2
                if modus == 2:#note depth is set to eighth notes
                    newKick = ba.doubleNotes(newKick, beatsPerMeasure, 2)
                    newSnares = ba.doubleNotes(newSnares, beatsPerMeasure, 2)
                    h = ba.doubleNotes(h, beatsPerMeasure, 2)
                    #generate a hihat pattern with 8th notes
                    h = ba.countTriggers(newKick,newSnares, h, beatsPerMeasure)
                    beatsPerMeasure = beatsPerMeasure * 2
                    tempo = tempo * 2
                    #checks where there is no snare and if there is a snare it adds none to the list.
                    # for example [0,1,2,3,none,5,6,none] etc..
                    notSnare = ba.searchForNotSnare(newSnares)
                    #splits list for example [0,1,2,3] [5,6] etc..
                    splitNotSnare = ba.split(notSnare, None)
                    #generate a kick pattern with 8th notes, choses from the splitted lists
                    kick = ba.getKickPosition(splitNotSnare)
                    #from timestamp to a list with 1 and 0
                    newKick = ba.eventsToIndex(kick, beatsPerMeasure)
                    #if there is no snare on the first beat, kick is add on index 0
                    if newSnares[0] == 0:
                        newKick[0] = 1
                    if beatsPerMeasure == 14:
                        if sum(newSnares) == 1 and newSnares[10] == 1: #add some snares if there is only 1 snare on index 10
                            moreSnares = ba.addMoreSnares(newKick, newSnares, beatsPerMeasure)
                            newSnares = ba.eventsToIndex(moreSnares, beatsPerMeasure)

                #print generated beat
                print(" ")
                print("===================================================")
                print(" ")
                print("HIHAT : ", h)
                print("SNARE : ", newSnares)
                print("KICK  : ", newKick)
                print(" ")
                print("===================================================")
                print(" ")
                print(colors.bcolors.WELKOM + "if you like this beat, press 'y' to export or PRESS 'enter' for a new beat or 'q' to quit"+ colors.bcolors.ENDC)


                #convert list from 1 and 0 to timestamps
                beatsPerMIDI = beatsPerMeasure
                midiKick = midi.convertListForMidi(newKick, midiKick, beatsPerMeasure)
                midiSnare = midi.convertListForMidi(newSnares, midiSnare, beatsPerMeasure)
                midiHihat = midi.convertListForMidi(h, midiHihat, beatsPerMeasure)

                tempo = 60 / tempo #form BPM to time millis
                player.play(newKick, newSnares, h, beatsPerMeasure, tempo)

def midiGen(MIDIname):#function that calls the midi generate function
    global midiKick, midiSnare, midiHihat, midiTempo, beatsPerMIDI
    midi.generateMIDI(midiKick, midiSnare, midiHihat, beatsPerMIDI, MIDIname, midiTempo)
