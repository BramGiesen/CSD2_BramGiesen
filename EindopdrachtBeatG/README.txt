Irregular Beat Generator, by Bram Giesen

Handleiding NL

1. De beat generator vraagt om een maatsoort, hierbij is er keuze uit 3/4, 5/4
en 7/7.
2. Kies een BPM tussen 1 en 200.
3. Wanneer je een beat wilt opslaan als .MIDI kan je op 'y' drukken en wordt
het bestand opgeslagen.
4. Voor een nieuwe beat kan je gewoon weer een nieuwe maatsoort en BPM invullen
en begint de procedure weer opnieuw.




Hoe werkt het algoritme? stap voor stap.
1. Wanneer de gebruiker de maatsoort selecteert worden er drie nieuwe lijsten
aangemaakt door middel van kans berekening.

de eerste is een lijst voor de kick, de tweede een lijst voor de snare en de
derde een lijst voor de hihat.

Dit gaat weer aan de hand van een aantal stappen.

1. Maatsoort(beatsPerMeasure) wordt doorgegeven aan script samplePlayer.py
hier wordt de functie kansPerMaatsoort aangeroepen.

kansPerMaatsoort stelt een lijst samen uit verschillende "bouwblokken",
dit zit zo:

een 3/4 maat kan je opbouwen uit één blokje van 3 tellen, een 5/4 kan je
samenstellen uit één blokje van 3 en één van 2 tellen. Bij een 7/4 heb je nog
wat meer opties. Namenlijk  één blokje van 4 en één blokje van 3 of twee blokjes
van 2 en één blokje van 3.

Dit wordt dus geregeld in de functie kansPerMaatsoort, hier worden deze blokjes
in de vorm van lijsten samengevoegd tot een lijst.

ter illustratie:

5/4 = 3+2 = [10, 1, 4] [10, 2] (de waarden in de lijst  worden gebruikt in de
kansberekening, 10 is 100% kans 0% is geen kans)

Vervolgens worden ze door transformKansList random geroteerd naar bijv:
[[10, 2] ,[10, 1, 4]]
hierna maakt de functie hier een platte lijst van:
[10, 2, 10, 1, 4]

vervolgens wordt er een lijst gemaakt met random getallen tussen 1 en 10 bijv:
[1,3,6,3,5]
De volgende stap is dat deze lijst wordt vergeleken met de lijst die uit transformKansList
komt.

dus:  [10, 2, 10, 1, 4] en [1, 3, 6, 3, 5]

Dit gaat op basis van index, en er wordt gekeken of de getalen gelijk aan of kleiner zijn.
Index[0] is 10 en 1, en omdat 1 kleiner of gelijk aan 10 is wordt er een event 0 in de volgende lijst gezet.
Als de de hele index is langsgeweest worden de nieuwe lijsten met de uitkomsten voor Kick en Snare en Hihat nog
met elkaar vergeleken, zo mag er geen snare komen op de plaats waar al een kick staat en mag er geen Hihat komen op de
plek waar al een snare staat.
De uitkomsten van deze check gaan naar een definitieve lijst en deze lijst wordt omgezet naar een lijst met time events
en door de sampler afgespeeld.
