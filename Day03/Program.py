def getPoints(wire):
    dx = {'L': -1, 'R': 1, 'D': 0, 'U': 0}
    dy = {'L': 0, 'R': 0, 'D': -1, 'U': 1}
    x = 0
    y = 0
    points = []
    for way in wire:
        direction = way[0]
        distance = int(way[1:])

        for step in range(distance):
            x += dx[direction]
            y += dy[direction]
            points.append((x, y))
    return points

lines = open('Day03\input.txt').read().split('\n')
wire1, wire2 = [x.split(',') for x in lines]

points1, points2 = [getPoints(wire) for wire in [wire1, wire2]]
intersections = set(points1) & set(points2)

# part 1
minDistance = min([abs(x) + abs(y) for (x, y) in intersections])
print(minDistance)

# part 2
def getStepsSum(points1, points2, intersection):
    return points1.index(intersection) + 1  + points2.index(intersection) + 1

stepsSums = [getStepsSum(points1, points2, i) for i in intersections]
print(min(stepsSums))