width = 25
height = 6
image = []


input = open('Day08\input.txt').read()

rowCounter = 0
totalRowCounter = 0
rows = []
while totalRowCounter*width < len(input):
    row = input[totalRowCounter*width:(totalRowCounter+1)*width]
    rows.append(row)
    totalRowCounter += 1
    rowCounter += 1
    if rowCounter == height:
        image.append(rows)
        rows = []
        rowCounter = 0

# part 1
minZerosCountLayer = None
minZerosCount = width * height


def getCountOfCharacterOnLayer(layer, character):
    return sum(layer[i].count(character) for i in range(len(layer)))


for i in range(len(image)):
    layer = image[i]
    zerosCount = getCountOfCharacterOnLayer(layer, '0')
    if zerosCount < minZerosCount:
        minZerosCount = zerosCount
        minZerosCountLayer = layer

print(getCountOfCharacterOnLayer(minZerosCountLayer, '1') * getCountOfCharacterOnLayer(minZerosCountLayer, '2'))

# part 2


def renderImage(layers):
    image = []

    for y in range(height):
        row = ['2']*width
        for x in range(width):
            for i in range(len(layers)):
                if layers[i][y][x] != '2':
                    row[x] = layers[i][y][x]
                    # меняем 0 на пробел, чтобы легче читалось сообщение в картинке
                    if row[x] == '0':
                        row[x] = ' '
                    break
        image.append(row)

    return image


renderedImage = renderImage(image)
print(renderedImage)
