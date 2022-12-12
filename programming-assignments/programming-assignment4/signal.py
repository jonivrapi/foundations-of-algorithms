class Signal:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.xSet = []
        self.ySet = []
        self.noiseSet = []
        self.xMovingIndex = 0
        self.yMovingIndex = 0
        self.xCompleted = 0
        self.yCompleted = 0
    
    def moveYIndex(self):
        if (self.yMovingIndex >= len(self.y) - 1):
            self.yMovingIndex = 0
            self.yCompleted += 1
        else:
            self.yMovingIndex += 1

    def moveXIndex(self):
        if (self.xMovingIndex >= len(self.x) - 1):
            self.xMovingIndex = 0
            self.xCompleted += 1
        else:
            self.xMovingIndex += 1

    def isIthCharacterOfX(self, character):
        return self.x[self.xMovingIndex] == character

    def isIthCharacterOfY(self, character):
        return self.y[self.yMovingIndex] == character

    def prune(self):
        largestIndex = self.noiseSet[len(self.noiseSet) - 1]

        self.xMovingIndex = 0
        self.yMovingIndex = 0
        self.xSet[:] = [x for x in self.xSet if x < largestIndex]
        self.ySet[:] = [y for y in self.ySet if y < largestIndex]
    
    def process(self):
        for index in range(len(self.s)):
            if (self.isIthCharacterOfX(self.s[index]) and self.isIthCharacterOfY(self.s[index])):
                if (self.xCompleted > self.yCompleted):
                    self.ySet.append(index + 1)
                    self.moveYIndex()
                elif (self.xCompleted == self.yCompleted):
                    if(self.xMovingIndex > self.yMovingIndex):
                        self.xSet.append(index + 1)
                        self.moveXIndex()
                    else:
                        self.ySet.append(index + 1)
                        self.moveYIndex()
                else:
                    self.xSet.append(index + 1)
                    self.moveXIndex()
                continue
            
            if (self.isIthCharacterOfX(self.s[index])):
                self.xSet.append(index + 1)
                self.moveXIndex()
                continue

            if (self.isIthCharacterOfY(self.s[index])):
                self.ySet.append(index + 1)
                self.moveYIndex()
                continue

            if (not self.isIthCharacterOfX(self.s[index]) and not self.isIthCharacterOfY(self.s[index])):
                self.noiseSet.append(index)
                self.prune()

        if (len(self.noiseSet)):
            self.noiseSet = [x for x in range(1, len(self.s) + 1) if x not in self.xSet and x not in self.ySet]
        
        print(f'xSet: {self.xSet}')
        print(f'ySet: {self.ySet}')
        print(f'noiseSet: {self.noiseSet}')

s1 = Signal("101", "0", "100010101")
s1.process()

s2 = Signal("101", "010", "101010101010101")
s2.process()

s3 = Signal("101", "010", "001100110101011001100110010101111")
s3.process()

s4 = Signal("101", "010", "100110011001")
s4.process()