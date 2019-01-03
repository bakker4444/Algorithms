## 155. Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#     * push(x) -- Push element x onto stack.
#     * pop() -- Removes the element on top of the stack.
#     * top() -- Get the top element.
#     * getMin() -- Retrieve the minimum element in the stack.
#
# Example:
#     MinStack minStack = new MinStack();
#     minStack.push(-2);
#     minStack.push(0);
#     minStack.push(-3);
#     minStack.getMin();   --> Returns -3.
#     minStack.pop();
#     minStack.top();      --> Returns 0.
#     minStack.getMin();   --> Returns -2.
##


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stacks = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stacks.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        value = self.stacks.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stacks[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
