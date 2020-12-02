import re
input = '278384-824795'
min, max = [int(x) for x in input.split('-')]

# part 1


def validatePasswordPart1(password):
    hasTwoEqualAdjacentDigits = False
    for i in range(1, len(password)):
        this = password[i]
        prev = password[i-1]
        if this == prev:
            hasTwoEqualAdjacentDigits = True
        if prev > this:
            return False

    return True if hasTwoEqualAdjacentDigits else False


validPasswords1 = [password for password in range(min, max+1) if validatePasswordPart1(str(password))]
print(len(validPasswords1))

# part 2


def validatePasswordPart2(password):
    threeDigits = re.findall(r'(\d)\1{2,}', password)
    twoDigits = re.findall(r'(\d)\1', password)
    # match2 - matchThreeDigits
    doubledDigits = [d for d in twoDigits if d not in threeDigits]
    if len(doubledDigits) == 0:
        return False

    for i in range(1, len(password)):
        this = password[i]
        prev = password[i-1]
        if prev > this:
            return False

    return True


validPasswords2 = [password for password in range(min, max+1) if validatePasswordPart2(str(password))]
print(len(validPasswords2))
