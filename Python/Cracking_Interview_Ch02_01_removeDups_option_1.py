## Remove Dups

# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# [option 1]
# time complexity O(n^2)
# space complexity O(1)

def removeDups(linkedList):
    currentNode = linkedList.head
    while currentNode:
        dupCheckNode = currentNode
        while dupCheckNode.next:
            if currentNode.val == dupCheckNode.next.val:
                dupCheckNode.next = dupCheckNode.next.next
            else:
                dupCheckNode = dupCheckNode.next
        currentNode = currentNode.next
    return linkedList

#########################################################################

## Singly Linked List Node Class
class listNode():
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

## Singly Linked List Class
class linkedList():
    def __init__(self, headNode=None):
        self.head = headNode
    def addNode(self, newVal):
        newNode = listNode(newVal)
        searchNode = self.head
        while searchNode.next:
            searchNode = searchNode.next
        searchNode.next = newNode
    def printAllNode(self):
        printingNode = self.head
        while printingNode:
            print(str(printingNode.val) + " --> ")
            printingNode = printingNode.next
        print("None")

## Linked List Setup
newNode = listNode(1)
testLinkedList = linkedList(newNode)
newNodeArray = [2, 3, 4, 5, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
for newNodeValue in newNodeArray:
    testLinkedList.addNode(newNodeValue)
testLinkedList.printAllNode()

## check remove duplicate node function
removeDups(testLinkedList)
testLinkedList.printAllNode()
