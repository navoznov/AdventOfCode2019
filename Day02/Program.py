import math


def getResult(codes, noun, verb):
    counter = 0
    codes[1] = noun
    codes[2] = verb
    while True:
        code = codes[counter]

        if code == 99:
            return codes[0]

        number1 = codes[codes[counter + 1]]
        number2 = codes[codes[counter + 2]]
        if code == 1:
            result = number1 + number2
        elif code == 2:
            result = number1 * number2

        targetIndex = codes[counter + 3]
        codes[targetIndex] = result
        counter = counter + 4


lines = open('Day02\input.txt').read().split(',')
codes = [int(line) for line in lines]

#part 1
part1 = getResult(codes[:], 12, 2)
print(part1)

#part 2
for noun in range(100):
    for verb in range(100):
        if getResult(codes[:], noun, verb) == 19690720:
            print(100*noun + verb)
