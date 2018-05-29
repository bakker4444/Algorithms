## Loop Detection

# Given a circular linked list, implement an algorithm that returns the node at
# the beginning of the loop.
#
# DEFINITION
# Circular linked list: a (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
# 
# EXAMPLE
# INPUT: A -> B -> C -> D -> E -> C [the same C as earlier]
# OUTPUT: C



## linked list node class
class ListNode:
    def __init__(self, nodeVal, nextNode=None):
        self.val = nodeVal
        self.next = nextNode


## linked list class
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


## test input generation
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, ....]
testLinkedList = LinkedList()
newNode0 = ListNode(0)
newNode1 = ListNode(1)
newNode2 = ListNode(2)
newNode3 = ListNode(3)
newNode4 = ListNode(4)
newNode5 = ListNode(5)
newNode6 = ListNode(6)
newNode7 = ListNode(7)
newNode8 = ListNode(8)
newNode9 = ListNode(9)
testLinkedList.addNode(newNode0)
testLinkedList.addNode(newNode1)
testLinkedList.addNode(newNode2)
testLinkedList.addNode(newNode3)
testLinkedList.addNode(newNode4)
testLinkedList.addNode(newNode5)
testLinkedList.addNode(newNode6)
testLinkedList.addNode(newNode7)
testLinkedList.addNode(newNode8)
testLinkedList.addNode(newNode9)
testLinkedList.addNode(newNode5)

###############################################################################


def loopDetection(linkedList):
    
    # edge case
    if not linkedList.head or not linkedList.head.next:
        return False

    # initial setup
    indI = linkedList.head.next         # one step at a time
    indJ = linkedList.head.next.next    # two step at a time

    # search mechanism
    # if there is no loop return False
    # otherwise, find the node when two index meets
    while(indI is not indJ):
        indI = indI.next
        if not indJ or not indJ.next:
            return False
        else:
            indJ = indJ.next.next

    # index I moves to linked list head
    indI = linkedList.head

    # loop until two indices meets, each index moves one step at a time
    while(indI is not indJ):
        indI = indI.next
        indJ = indJ.next

    return indI

result = loopDetection(testLinkedList)
print(result.val)
