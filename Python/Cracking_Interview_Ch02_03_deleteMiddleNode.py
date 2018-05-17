## Delete Middle Node

# Implement an algorithm to delete a node in the middle(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
#
# INPUT: the node c from the linked list a -> b -> c -> d -> e -> f
# RESULT: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

def deleteMiddleNode(deletingNode):
    ## fail case
    if not deletingNode:
        return False
    elif not deletingNode.next:
        return False
    else:
        tempNode = deletingNode.next
        deletingNode.val = tempNode.val
        deletingNode.next = tempNode.next

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
newNode = listNode("a")
testLinkedList = linkedList(newNode)
newNodeArray = ["b", "c", "d", "e", "f"]
for newNodeValue in newNodeArray:
    testLinkedList.addNode(newNodeValue)
## print linked list
testLinkedList.printAllNode()

#########################################################################

## Make input node
deletingNodeC = testLinkedList.head.next.next

## Running function
deleteMiddleNode(deletingNodeC)

## Print linked list result
testLinkedList.printAllNode()