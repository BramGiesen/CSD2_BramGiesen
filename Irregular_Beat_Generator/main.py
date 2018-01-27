import beatAlgo as ba
import player
import midiProcessing as midi

midiKick  = []
midiSnare = []
midiHihat = []


def makeAbeat(beatsPerMeasure, tempo):

    kickKansList  = []
    SnareKansList = []
    kick  = []
    snare = []
    snareDef = []

    h = [1] * beatsPerMeasure

    kansPMListKick = ba.kansPerMaatsoort(beatsPerMeasure, kickKansList, "kick")
    kansPMListSnare = ba.kansPerMaatsoort(beatsPerMeasure, SnareKansList, "snare")

    NewkickKansList   = ba.transformKansList(kansPMListKick)
    NewSnareKansList   = ba.transformKansList(kansPMListSnare)


    uitkomst = ba.makeRandomList(beatsPerMeasure)
    newKick   = ba.generateList(NewkickKansList , kick, uitkomst, beatsPerMeasure)
    newSnare  = ba.generateList(NewSnareKansList , snare, uitkomst, beatsPerMeasure)

    newSnares = ba.checkList(newSnare, newKick, snareDef, beatsPerMeasure)

    sumSnare = sum(newSnares)

    if sumSnare == 0:
        newSnares = ba.addASnare(newKick, newSnares, beatsPerMeasure)


    global midiKick, midiSnare, midiHihat, midiTempo

    midiTempo = tempo

    midiKick = midi.convertListForMidi(newKick, midiKick, beatsPerMeasure)
    midiSnare = midi.convertListForMidi(newSnares, midiSnare, beatsPerMeasure)
    midiHihat = midi.convertListForMidi(h, midiHihat, beatsPerMeasure)

    tempo = 60 / tempo
    player.play(newKick, newSnares, h, beatsPerMeasure, tempo)

def midiGen(beatsPerMeasure, MIDIname):
    global midiKick, midiSnare, midiHihat, midiTempo
    midi.generateMIDI(midiKick, midiSnare, midiHihat, beatsPerMeasure, MIDIname, midiTempo)
