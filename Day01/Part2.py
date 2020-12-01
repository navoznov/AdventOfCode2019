import math

def getFuel(mass):
    sum = 0
    while mass > 0:
        fuel = math.floor(mass/3) - 2
        fuel =  0 if fuel < 0 else fuel
        sum = sum + fuel
        mass = fuel

    return sum

lines = open('Day01\input.txt').read().split('\n')
numbers = [int(line) for line in lines]
sum = 0
for number in numbers:
    sum = sum + getFuel(number)

print(sum)