## Palindrome

#  Implement a function to check if a linked list is a palindrome.



# linked list node class
class ListNode:
    def __init__(self, nodeVal, nextNode=None):
        self.val = nodeVal
        self.next = nextNode


# linked list class
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def addNode(self, newNode):
        if not self.head:
            self.head = newNode
        else:
            searchNode = self.head
            while searchNode.next:
                searchNode = searchNode.next
            searchNode.next = newNode
    def printAllNodeVal(self):
        printingNode = self.head
        while(printingNode):
            print(str(printingNode.val) + " --> ")
            printingNode = printingNode.next
        print("None")
           

# stack class
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def printAllStacks(self):
        for i in range(len(self.items)):
            print(str(self.items[len(self.items)-1-i]) + " -->")
        

###############################################################################


def palindrome(linkedList):

    # Edge case
    if not linkedList.head:
        return False
    if linkedList.head and linkedList.head.next:
        return True
    
    # generate stack
    stack = Stack()
    index = linkedList.head

    # push from linked list to stack for reverse order of linked list
    while(index):
        stack.push(index.val)
        index = index.next

    # check the stack value
    stack.printAllStacks()

    # reset the index to the head of linked list
    index = linkedList.head
    
    # comparison, linked list and stack
    while(index):
        if index.val != stack.pop():
            return False
        else:
            index = index.next
    return True


# Test input generation
testLinkedList = LinkedList()
nodeArray = [1, 2, 3, 4, 5, 4, 3, 2, 1]
for i in nodeArray:
    newNode = ListNode(i)
    testLinkedList.addNode(newNode)
testLinkedList.printAllNodeVal()

# run palindrome function
print(palindrome(testLinkedList))


