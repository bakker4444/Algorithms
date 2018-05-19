## Partition

# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
#
# EXAMPLE
# INPUT:    3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1    [partition = 5]
# OUTPUT:   3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partition(linkedList, partition):

    ## no node exist case
    if not linkedList.head:
        return False

    ## one node exist case
    elif not linkedList.head.next:
        return linkedList

    ## more than one node case ( general case)
    else:
        # initialize
        currentNode = linkedList.head

        ## find the value, which is bigger than partition, located in left side(partition)
        while currentNode.next.next:
            if currentNode.val < partition:
                currentNode = currentNode.next

            ## if it found, find the value which is smaller than partition, located in right side(partition)
            ## then, swap the value (value only, not entire node)
            else:
                searchingNode = currentNode.next
                while searchingNode:
                    if searchingNode.val < partition:
                        swapValue(currentNode, searchingNode)
                        currentNode = currentNode.next
                        break
                    else:
                        searchingNode = searchingNode.next
                        ## when searchingNode reach to the end, move one step for currentNode to next
                        if not searchingNode:
                            currentNode = currentNode.next


def swapValue(nodeA, nodeB):
    tempVal = nodeA.val
    nodeA.val = nodeB.val
    nodeB.val = tempVal

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
newNode = listNode(3)
testLinkedList = linkedList(newNode)
newNodeArray = [5, 8, 5, 10, 2, 1]
for newNodeValue in newNodeArray:
    testLinkedList.addNode(newNodeValue)
testLinkedList.printAllNode()

#########################################################################

## TEST
partition(testLinkedList, 5)
testLinkedList.printAllNode()
