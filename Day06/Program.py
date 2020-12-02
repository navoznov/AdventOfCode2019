input = [x.split(')') for x in open('Day06\input.txt').read().split('\n')]

com = 'COM'

# part 1
totalOrbitsCount = 0
levelCounter = 1
planets = [com]

while True:
    thisLevelOrbits = [x for x in input if x[0] in planets]
    orbitsCount = len(thisLevelOrbits)
    totalOrbitsCount += orbitsCount * levelCounter
    if orbitsCount == 0:
        break

    planets = [x[1] for x in thisLevelOrbits]
    levelCounter += 1

print(totalOrbitsCount)

# part 2
prevLevelWays = [com]
allWays = [com]
planets = [com]
levelCounter = 1

while True:
    thisLevelWays = []
    for way in prevLevelWays:
        planet = way[-3:]
        planetWays = [way+x[1] for x in input if x[0] == planet]
        thisLevelWays.extend(planetWays)

    if len(thisLevelWays) == 0:
        break

    levelCounter += 1
    allWays.extend(thisLevelWays)
    prevLevelWays = thisLevelWays

ways = [x for x in allWays if x[-3:] in ['YOU', 'SAN']]

for i in range(0, len(ways[0]), 3):
    planet1, planet2 = [ways[n][i:i+3] for n in range(2)]
    if planet1 != planet2:
        distance = int((len(ways[0]) + len(ways[1]) - i*2)/3)-2
        print(distance)
