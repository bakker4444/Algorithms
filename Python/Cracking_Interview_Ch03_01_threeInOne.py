## Three in One
#
# Describe how you could use a single array to implement three stacks.



## Fixed Division
class FixedMultiStack:

    def __init__(self, stackSize):
        self.numberOfStacks = 3
        self.totalArray = [0] * (stackSize * self.numberOfStacks)
        self.eachStackSize = [0] * self.numberOfStacks
        self.stackCapacity = stackSize

    def push(self, stackNum, value):
        if self.isFull:
            raise Exception("Stack is full")
        self.eachStackSize[stackNum] += 1
        self.totalArray[self.indexOfTop(stackNum)] = value

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception("Stack is empty")
        value = self.totalArray[self.indexOfTop(stackNum)]
        self.totalArray[self.indexOfTop(stackNum)] = 0
        self.eachStackSize -= 1
        return value

    def peak(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception("Stack is empty")
        return self.totalArray[self.indexOfTop(stackNum)]

    def isFull(self, stackNum):
        return self.eachStackSize[stackNum] == self.stackCapacity

    def isEmpty(self, stackNum):
        return self.eachStackSize[stackNum] == 0

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        return offset + self.eachStackSize[stackNum] - 1
