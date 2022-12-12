class Signal:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        # keeps track of sets of indexes for each input + noise
        self.xSet = []
        self.ySet = []
        self.noiseSet = []
        # keeps track of the current index of x and y that needs to be found
        self.xMovingIndex = 0
        self.yMovingIndex = 0
        # keeps track of how many times we have found a complete x and y
        self.xCompleted = 0
        self.yCompleted = 0

        self.iterations = 0
    
    # moves yMovingIndex by 1
    def moveYIndex(self):
        if (self.yMovingIndex >= len(self.y) - 1):
            self.yMovingIndex = 0
            self.yCompleted += 1
        else:
            self.yMovingIndex += 1
    
    # moves xMovingIndex by 1
    def moveXIndex(self):
        if (self.xMovingIndex >= len(self.x) - 1):
            self.xMovingIndex = 0
            self.xCompleted += 1
        else:
            self.xMovingIndex += 1

    # checks if the input character is the ith character of x
    def isIthCharacterOfX(self, character):
        return self.x[self.xMovingIndex] == character

    # checks if the input character is the ith character of y
    def isIthCharacterOfY(self, character):
        return self.y[self.yMovingIndex] == character

    # prunes xSet and ySet of values in noise
    def prune(self):
        largestIndex = self.noiseSet[len(self.noiseSet) - 1]

        self.xMovingIndex = 0
        self.yMovingIndex = 0
        self.xSet[:] = [x for x in self.xSet if x < largestIndex]
        self.ySet[:] = [y for y in self.ySet if y < largestIndex]
    
    # proceses the input string s linearly as it comes in
    def process(self):
        for index in range(len(self.s)):
            self.iterations += 1

            if (self.isIthCharacterOfX(self.s[index]) and self.isIthCharacterOfY(self.s[index])):
                # if i have completed x more times than y, i need to append to y and move its index
                if (self.xCompleted > self.yCompleted):
                    self.ySet.append(index + 1)
                    self.moveYIndex()
                # if they have been completed the same amount of times, i need to add to x and move its index
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
            
            # if current character is the ith character of x, we need to add to xSet and move its index
            if (self.isIthCharacterOfX(self.s[index])):
                self.xSet.append(index + 1)
                self.moveXIndex()
                continue

            # if current character is the ith character of y, we need to add to ySet and move its index
            if (self.isIthCharacterOfY(self.s[index])):
                self.ySet.append(index + 1)
                self.moveYIndex()
                continue

            # if current character neither of the above 2 conditions, then its noise and we need to prune
            if (not self.isIthCharacterOfX(self.s[index]) and not self.isIthCharacterOfY(self.s[index])):
                self.noiseSet.append(index)
                self.prune()

        if (len(self.noiseSet)):
            self.noiseSet = [x for x in range(1, len(self.s) + 1) if x not in self.xSet and x not in self.ySet]
            self.iterations += len(self.noiseSet)

        
        print(f'xSet: {self.xSet}')
        print(f'ySet: {self.ySet}')
        print(f'noiseSet: {self.noiseSet}')

        if (len(self.xSet) + len(self.ySet) + len(self.noiseSet) == len(self.s)):
            print("This is an interweaving")
        
        print(f'Total Iterations: {self.iterations} with respect to an input of size s: {len(self.s)}')

s1 = Signal("101", "0", "100010101")
s1.process()

print("----------------------------------")

s2 = Signal("101", "010", "101010101010101")
s2.process()

print("----------------------------------")

s3 = Signal("101", "010", "001100110101011001100110010101111")
s3.process()

print("----------------------------------")

s4 = Signal("101", "010", "100110011001")
s4.process()