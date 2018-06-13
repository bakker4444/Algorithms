## Stack of Plates
#
# Imagine a (literal) stack of plates.
# If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds
# capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack(that is, pop() should return
# the same values as it would if there were just a single stack).
#
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.


class Stack:
    def __init__(self):
        self.stacks = []
    def push(self, data):
        self.stacks.append(data)
    def pop(self):
        if not len(self.stacks):
            return "Stack is empty"
        else:
            self.stacks.pop()
    def stackSize(self):
        return len(self.stacks)


class SetOfStacks:
    def __init__(self, stackLimit):
        self.stacks = []
        self.stackLimit = stackLimit
        self.stackLength = 0
    def push(self, inputVal):
        if not len(self.stacks) or (self.stackLimit == self.stackLength):
            self.stacks.append(Stack())
            self.stackLength = 0
        self.stacks[-1].push(inputVal)
        self.stackLength += 1
    def pop(self):
        if not len(self.stacks):
            print("Stack is empty")
            return False
        self.stacks[-1].pop()
        if not self.stacks[-1].stackSize():
            self.stacks.pop()

    def stackSize(self):
        return sum(map(lambda x: x.stackSize(), self.stacks))


##########################
## Test                 ##
##########################

## set the stack size limit
testStack = SetOfStacks(7)

## adding element
for i in range(48):
    testStack.push(i)
    # print(testStack.stackSize())

print("push finished")

## remove from stacks more than it's elements
for i in range(51):
    testStack.pop()
    # print(testStack.stackSize())

print("pop finished")
