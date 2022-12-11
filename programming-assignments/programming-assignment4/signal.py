# s = "100010101"
# s = "101010101010101"
# s = "100110011001"
s = "001100110101011001100110010101111"


x = "101"
# y = '0'
y = "010"

xSet = []
ySet = []
noise = []

xMovingIndex = 0
yMovingIndex = 0
noiseMovingIndex = 0

lastChecked = 'x'

def moveYIndex():
    global yMovingIndex
    if (yMovingIndex >= len(y) - 1):
        yMovingIndex = 0
    else:
        yMovingIndex += 1

    print(f'yMovingIndex: {yMovingIndex}')

def moveXIndex():
    global xMovingIndex
    if (xMovingIndex >= len(x) - 1):
        xMovingIndex = 0
    else:
        xMovingIndex += 1

    print(f'xMovingIndex: {xMovingIndex}')

def moveNoiseIndex():
    global noiseMovingIndex
    if (noiseMovingIndex >= len(noise) - 1):
        noiseMovingIndex = 0
    else:
        noiseMovingIndex += 1

    print(f'xMovingIndex: {xMovingIndex}')

def isIthCharacterOfX(character):
    isIthCharacter = x[xMovingIndex] == character
    return isIthCharacter

def isIthCharacterOfY(character):
    isIthCharacter = y[yMovingIndex] == character
    return isIthCharacter



for index in range(len(s)):
    print(f"Character index: {index} | Character: {s[index]}")

    if (lastChecked == 'x'):
        if (isIthCharacterOfX(s[index])):
            print(f'length of xSet: {len(xSet)}')
            xSet.append(index + 1)
            moveXIndex()
            lastChecked = 'x'

        elif (isIthCharacterOfY(s[index])):
            print(f'length of ySet: {len(ySet)}')
            ySet.append(index + 1)
            moveYIndex()
            lastChecked = 'y'
        else:
            noise.append(index + 1)
            moveNoiseIndex()
            lastChecked = 'noise'

    elif (lastChecked == 'y'):
        if (isIthCharacterOfY(s[index])):
            print(f'length of ySet: {len(ySet)}')
            ySet.append(index + 1)
            moveYIndex()
            lastChecked = 'y'

        elif (isIthCharacterOfX(s[index])):
            print(f'length of xSet: {len(xSet)}')
            xSet.append(index + 1)
            moveXIndex()
            lastChecked = 'x'
        else:
            noise.append(index + 1)
            moveNoiseIndex()
            lastChecked = 'noise'
    elif (lastChecked == 'noise'):
        if (not isIthCharacterOfX(s[index]) and not isIthCharacterOfY(s[index])):
            noise.append(index + 1)
            moveNoiseIndex()
            lastChecked = 'noise'
        elif (isIthCharacterOfX(s[index])):
            print(f'length of xSet: {len(xSet)}')
            xSet.append(index + 1)
            moveXIndex()
            lastChecked = 'x'

        elif (isIthCharacterOfY(s[index])):
            print(f'length of ySet: {len(ySet)}')
            ySet.append(index + 1)
            moveYIndex()
            lastChecked = 'y'
            


print(f'xSet: {xSet}')
print(f'ySet: {ySet}')
print(f'noise: {noise}')