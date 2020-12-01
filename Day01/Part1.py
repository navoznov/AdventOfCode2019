import math
lines = open('Day01\input.txt').read().split('\n')
numbers = [int(line) for line in lines]
sum = 0
for number in numbers:
    sum = sum + math.floor(number/3)-2
print(sum)