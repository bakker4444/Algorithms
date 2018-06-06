## Stack Min

# How would you design¸ a stack which, in addition to push and pop, has a function min which returns the minimum
# element? Push, pop and min should all operate in O(1) time.

class stackMin:

    def __init__(self):

        ## value stack
        self.valueStack = []

        ## purpose: min value tracking
        self.minStack = []



    def push(self, val):
        self.valueStack.append(val)

        # edge case: Stack, empty
        if not len(self.minStack):
            self.minStack.append({val: 1})

        # general case: stack is not empty
        elif val <= list(self.minStack[-1])[0]:

            # edge case: multiple min value push case handle
            # if new val is same as current min value increase the count
            if list(self.minStack[-1])[0] == val:
                self.minStack[-1][val] += 1

            else:
                self.minStack.append({val: 1})



    def pop(self):
        if not len(self.valueStack):
            raise Exception("Stack is empty")
        else:
            popValue = self.valueStack.pop()
            if popValue == list(self.minStack[-1])[0]:

                if self.minStack[-1][popValue] == 1:
                    self.minStack.pop()
                else:
                    self.minStack[-1][popValue] -= 1



    def minVal(self):
        if not len(self.valueStack):
            raise Exception("Stack is empty, there is no min value")
        else:
            return list(self.minStack[-1])[0]



###########################################################################

## Test
testStackWithMin = stackMin()

## test: Push
testCase = [7, 6, 5, 3, 4, 1, 1, 1, 1]
for i in range(len(testCase)):
    print("pushing value " + str(testCase[i]) +" ================")
    testStackWithMin.push(testCase[i])
    print("Value stack:")
    print(testStackWithMin.valueStack)
    print("Min stack:")
    print(testStackWithMin.minStack)
    print("Min Value:")
    print(testStackWithMin.minVal())


## test: Pop
for i in range(len(testCase)):
    print("popping =================")
    testStackWithMin.pop()
    print("Value stack:")
    print(testStackWithMin.valueStack)
    print("Min stack:")
    print(testStackWithMin.minStack)
    print("Min Value:")
    print(testStackWithMin.minVal())
