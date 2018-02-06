import beatAlgo as ba
import player
import midiProcessing as midi
import bcolors as colors
# from userInput import ask

midiKick  = []
midiSnare = []
midiHihat = []
previousBeat = []

main = False
modus = 2


def setModus(number):
    global modus
    number = int(number)
    modus = number

def makeAbeat(beatsPerMeasure, tempo):
    global previousBeat, beatsPerMIDI, modus


    while main:

        kickKansList  = []
        SnareKansList = []
        kick  = []
        snare = []
        snareDef = []

        kansPMListKick = ba.kansPerMaatsoort(beatsPerMeasure, kickKansList, "kick")

        kansPMListSnare = ba.kansPerMaatsoort(beatsPerMeasure, SnareKansList, "snare")

        NewkickKansList   = ba.transformKansList(kansPMListKick)

        NewSnareKansList   = ba.transformKansList(kansPMListSnare)


        uitkomst = ba.makeRandomList(beatsPerMeasure)

        newKick   = ba.generateList(NewkickKansList , kick, uitkomst, beatsPerMeasure)
        # print("newKick : ", newKick)
        newSnare  = ba.generateList(NewSnareKansList , snare, uitkomst, beatsPerMeasure)
        # print("beforeCheckList : ", newSnare)
        newSnares = ba.checkList(newSnare, newKick, snareDef, beatsPerMeasure)
        # print("afterCheckList : ", newSnares)
        sumSnare = sum(newSnares)

        if sumSnare == 0:#checks if there are snares in the generated beat
            newSnares = ba.addASnare(newKick, newSnares, beatsPerMeasure)
            newSnares = ba.checkList(newSnare, newKick, snareDef, beatsPerMeasure)
            # print("ADDASNARE : ", newSnares)
            # sumSnare = sum(newSnares)
        else:
            beat = newSnares + newKick
            if beat == previousBeat:#check if the new beat is the same as te last beat
                makeAbeat(beatsPerMeasure, tempo)#generate a new Beat if they are the same
            else:#play the beat and covert list to a "midiList" with time events
                global midiKick, midiSnare, midiHihat, midiTempo

                previousBeat = newSnare + newKick

                # print("beatsPerMeasure : ", beatsPerMeasure)
                midiTempo = tempo

                if beatsPerMeasure == 7:
                    tempo = tempo * 2

                h = [1] * beatsPerMeasure
                if modus == 1:
                    newKick = ba.doubleNotes(newKick, beatsPerMeasure, 2)
                    newSnares = ba.doubleNotes(newSnares, beatsPerMeasure, 2)
                    h = ba.doubleNotes(h, beatsPerMeasure, 2)
                    beatsPerMeasure = beatsPerMeasure * 2
                    tempo = tempo * 2
                if modus == 2:
                    newKick = ba.doubleNotes(newKick, beatsPerMeasure, 2)
                    newSnares = ba.doubleNotes(newSnares, beatsPerMeasure, 2)
                    h = ba.doubleNotes(h, beatsPerMeasure, 2)
                    h = ba.countTriggers(newKick,newSnares, h, beatsPerMeasure)
                    beatsPerMeasure = beatsPerMeasure * 2
                    tempo = tempo * 2
                    notSnare = ba.searchForNotSnare(newSnares)
                    splitNotSnare = ba.split(notSnare, None)
                    kick = ba.getKickPosition(splitNotSnare)
                    newKick = ba.eventsToIndex(kick, beatsPerMeasure)
                    if newSnares[0] == 0:
                        newKick[0] = 1
                    if beatsPerMeasure == 14:
                        if sum(newSnares) == 1 and newSnares[10] == 1:
                            print("voeg nog wat snartjes toe")
                            moreSnares = ba.addMoreSnares(newKick, newSnares, beatsPerMeasure)
                            newSnares = ba.eventsToIndex(moreSnares, beatsPerMeasure)
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
                # ui.ask = True

                beatsPerMIDI = beatsPerMeasure
                midiKick = midi.convertListForMidi(newKick, midiKick, beatsPerMeasure)
                midiSnare = midi.convertListForMidi(newSnares, midiSnare, beatsPerMeasure)
                midiHihat = midi.convertListForMidi(h, midiHihat, beatsPerMeasure)

                tempo = 60 / tempo
                player.play(newKick, newSnares, h, beatsPerMeasure, tempo)

def midiGen(MIDIname):
    global midiKick, midiSnare, midiHihat, midiTempo, beatsPerMIDI
    midi.generateMIDI(midiKick, midiSnare, midiHihat, beatsPerMIDI, MIDIname, midiTempo)
