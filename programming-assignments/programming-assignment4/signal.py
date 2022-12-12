# s = "100010101"
# s = "101010101010101"
# s = "100110011001"
s = "001100110101011001100110010101111"


x = "101"
# y = '0'
y = "010"

xSet = []
ySet = []

xMovingIndex = 0
yMovingIndex = 0

xCompleted = 0
yCompleted = 0
lastChecked = 'x'

def moveYIndex():
    global yMovingIndex
    global yCompleted
    if (yMovingIndex >= len(y) - 1):
        yMovingIndex = 0
        yCompleted += 1
    else:
        yMovingIndex += 1

    print(f'yMovingIndex: {yMovingIndex}')

def moveXIndex():
    global xMovingIndex
    global xCompleted
    if (xMovingIndex >= len(x) - 1):
        xMovingIndex = 0
        xCompleted += 1
    else:
        xMovingIndex += 1

    print(f'xMovingIndex: {xMovingIndex}')

def isIthCharacterOfX(character):
    isIthCharacter = x[xMovingIndex] == character
    return isIthCharacter

def isIthCharacterOfY(character):
    isIthCharacter = y[yMovingIndex] == character
    return isIthCharacter



for index in range(len(s)):
    print(f"Character index: {index} | Character: {s[index]}")

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
        print(f'length of xSet: {len(xSet)}')
        xSet.append(index + 1)
        moveXIndex()
        lastChecked = 'x'
        continue

    if (isIthCharacterOfY(s[index])):
        print(f'length of ySet: {len(ySet)}')
        ySet.append(index + 1)
        moveYIndex()
        lastChecked = 'y'
        continue

print(f'xSet: {xSet}')
print(f'ySet: {ySet}')