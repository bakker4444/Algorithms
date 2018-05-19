## Return Kth to Last

# Implement an algorithm to find the kth to last element of a singly linked list.

def returnKthtoLast(linkedList, k):
    if k == 0:
        return None
    elif k < 0:
        return False
    else:   # k > 0
        lastNode = linkedList.head
        for i in range(1, k):
            if not lastNode.next:
                print("k is bigger than linked list length")
                return False
            lastNode = lastNode.next
        firstNode = linkedList.head
        while lastNode.next:
            firstNode = firstNode.next
            lastNode = lastNode.next
        linkedList.head = firstNode
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
# INPUT: testLinkedList
newNode = listNode(1)
testLinkedList = linkedList(newNode)
newNodeArray = [2, 3, 4, 5, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
for newNodeValue in newNodeArray:
    testLinkedList.addNode(newNodeValue)
testLinkedList.printAllNode()

#########################################################################

## test 1, normal case
returnKthtoLast(testLinkedList, 7)
testLinkedList.printAllNode()

## test 2, error case, k is bigger than singly linked list's length
# test linked list length = 19
# returnKthtoLast(testLinkedList, 20)
