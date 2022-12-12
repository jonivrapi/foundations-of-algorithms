# s = "100010101"
# s = "101010101010101"
# s = "100110011001"
s = "001100110101011001100110010101111"


x = "101"
# y = '0'
y = "010"

xSet = []
ySet = []
noiseSet = []

xMovingIndex = 0
yMovingIndex = 0

xCompleted = 0
yCompleted = 0

def moveYIndex():
    global yMovingIndex
    global yCompleted

    if (yMovingIndex >= len(y) - 1):
        yMovingIndex = 0
        yCompleted += 1
    else:
        yMovingIndex += 1

def moveXIndex():
    global xMovingIndex
    global xCompleted
    
    if (xMovingIndex >= len(x) - 1):
        xMovingIndex = 0
        xCompleted += 1
    else:
        xMovingIndex += 1

def isIthCharacterOfX(character):
    isIthCharacter = x[xMovingIndex] == character
    return isIthCharacter

def isIthCharacterOfY(character):
    isIthCharacter = y[yMovingIndex] == character
    return isIthCharacter

def prune():
    global xSet
    global ySet
    global xMovingIndex
    global yMovingIndex
    global noiseSet

    # noiseSet = noiseSet + xSet + ySet

    largestIndex = noiseSet[len(noiseSet) - 1]

    xMovingIndex = yMovingIndex = 0
    xSet[:] = [x for x in xSet if x < largestIndex]
    ySet[:] = [y for y in ySet if y < largestIndex]


for index in range(len(s)):
    if (isIthCharacterOfX(s[index]) and isIthCharacterOfY(s[index])):
        if (xCompleted > yCompleted):
            ySet.append(index + 1)
            moveYIndex()
        elif (xCompleted == yCompleted):
            if(xMovingIndex > yMovingIndex):
                xSet.append(index + 1)
                moveXIndex()
            else:
                ySet.append(index + 1)
                moveYIndex()
        else:
            xSet.append(index + 1)
            moveXIndex()
        continue
    
    if (isIthCharacterOfX(s[index])):
        xSet.append(index + 1)
        moveXIndex()
        continue

    if (isIthCharacterOfY(s[index])):
        ySet.append(index + 1)
        moveYIndex()
        continue

    if (not isIthCharacterOfX(s[index]) and not isIthCharacterOfY(s[index])):
        noiseSet.append(index)
        prune()

if (len(noiseSet)):
    noiseSet = [x for x in range(1, len(s) + 1) if x not in xSet and x not in ySet]

print(f'xSet: {xSet}')
print(f'ySet: {ySet}')
print(f'noiseSet: {noiseSet}')