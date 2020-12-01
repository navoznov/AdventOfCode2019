import math

lines = open('Day02\input.txt').read().split(',')
numbers = [int(line) for line in lines]
codes = numbers

codes[1] = 12
codes[2] = 2

counter = 0
while True:
    code = codes[counter]

    if code == 99:
        break

    number1 = codes[codes[counter + 1]]
    number2 = codes[codes[counter + 2]]
    if code == 1:
        result = number1 + number2
    elif code == 2:
        result = number1 * number2

    targetIndex = codes[counter + 3]
    codes[targetIndex] = result
    counter = counter + 4

print(codes[0])
