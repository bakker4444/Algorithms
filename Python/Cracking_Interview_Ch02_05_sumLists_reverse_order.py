## Sum Lists

# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
#
# EXAMPLE
# INPUT : (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
# OUTPUT : 2 -> 1 -> 9. That is, 912.
#
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
#
# EXAMPLE
# INPUT : (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# OUTPUT : 9 -> 1 -> 2. That is, 912.
#
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
        if not self.head:
            self.head = newNode
        else:
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
# INPUT: testLinkedList1, testLinkedList2
testLinkedList1 = linkedList()
newNodeArray = [9, 7, 8]
for newNodeValue in newNodeArray:
    testLinkedList1.addNode(newNodeValue)
testLinkedList1.printAllNode()

testLinkedList2 = linkedList()
newNodeArray = [6, 8, 5]
for newNodeValue in newNodeArray:
    testLinkedList2.addNode(newNodeValue)
testLinkedList2.printAllNode()

#########################################################################

## Reverse Order

def sumLists(input1, input2):

    # initial setup
    i = input1.head
    j = input2.head
    carry = 0

    # edge case
    if not i and not j:
        return linkedList()

    outputLinkedList = linkedList()

    while i or j or carry:

        ## only carry exist
        if not i and not j:
            newVal = carry
            carry = 0

        ## only second linked list exist
        elif not i:
            newVal = j.val + carry
            j = j.next
            carry = 0

        ## only first linked list exist
        elif not j:
            newVal = i.val + carry
            i = i.next
            carry = 0

        ## general case
        else:
            newVal = i.val + j.val + carry
            i = i.next
            j = j.next

        # carry setup
        if newVal >= 10:
            carry = 1
        else:
            carry = 0

        newVal = newVal - 10 * carry
        outputLinkedList.addNode(newVal)

    return outputLinkedList
#########################################################################

# TEST
result = sumLists(testLinkedList1, testLinkedList2)
result.printAllNode()