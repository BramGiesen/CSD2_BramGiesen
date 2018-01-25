import beatAlgo as ba
import player
import midiProcessing as midi


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
    # TODO bpm conversion
    tempo = (tempo / 100 * -1 + 5) / 10 * 1

    midiKick  = []
    midiSnare = []
    midiHihat = []

    midiKick = midi.convertListForMidi(newKick, midiKick, beatsPerMeasure)
    midiSnare = midi.convertListForMidi(newSnares, midiSnare, beatsPerMeasure)
    midiHihat = midi.convertListForMidi(h, midiHihat, beatsPerMeasure)

    midi.generateMIDI(midiKick, 35, beatsPerMeasure)
    midi.generateMIDI(midiSnare, 38, beatsPerMeasure)
    midi.generateMIDI(midiHihat, 42, beatsPerMeasure)

    player.play(newKick, newSnares, h, beatsPerMeasure, tempo)
