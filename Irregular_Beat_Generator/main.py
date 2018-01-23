import beatAlgo as ba
import player


def makeAbeat(beatsPerMeasure, tempo):

    kickKansList  = []
    SnareKansList = []
    kick  = []
    snare = []
    snareDef = []

    h = [1, 1, 1, 1, 1, 1, 1]


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
    player.play(newKick, newSnares, h, beatsPerMeasure, tempo)
