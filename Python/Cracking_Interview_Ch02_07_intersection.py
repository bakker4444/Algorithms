## Intersection

# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is tht exact same node (by reference) as the jth node of the second linked list, then they are intersecting.



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


## Test input generation
# test linked list case 1
testLinkedList1 = LinkedList()
nodeArray1 = [1, 2, 3, 4, 5, 6]

newNode0 = ListNode(nodeArray1[0])
testLinkedList1.addNode(newNode0)
newNode1 = ListNode(nodeArray1[1])
testLinkedList1.addNode(newNode1)
newNode2 = ListNode(nodeArray1[2])
testLinkedList1.addNode(newNode2)
newNode3 = ListNode(nodeArray1[3])
testLinkedList1.addNode(newNode3)
newNode4 = ListNode(nodeArray1[4])
testLinkedList1.addNode(newNode4)
newNode5 = ListNode(nodeArray1[5])
testLinkedList1.addNode(newNode5)
testLinkedList1.printAllNodeVal()

## intersection linked list test case
testLinkedList2 = LinkedList()
testLinkedList2.addNode(ListNode(9))
testLinkedList2.addNode(newNode3)
testLinkedList2.printAllNodeVal()

## no intersection linked list test case
testLinkedList3 = LinkedList()
testLinkedList3.addNode(ListNode(1))
testLinkedList3.addNode(ListNode(2))
testLinkedList3.addNode(ListNode(3))

################################################################


def intersection(linkedList1, linkedList2):

    # fast exit case
    if not linkedList1 or not linkedList2:
        return False

    # set initial condition
    length1 = 1
    length2 = 1
    searchNode1 = linkedList1.head
    searchNode2 = linkedList2.head

    # find the length of individual linked lists
    while (searchNode1.next):
        searchNode1 = searchNode1.next
        length1 += 1
    while (searchNode2.next):
        searchNode2 = searchNode2.next
        length2 += 1

    # check fast exit case, tail nodes different case
    if searchNode1 != searchNode2:
        return False

    # reset search node to individual linked list's head
    searchNode1 = linkedList1.head
    searchNode2 = linkedList2.head

    # if there are length difference, fit the searchNode index with same length from the tail
    while(length1 != length2):
        if length1 > length2:
            length1 = length1 - 1
            searchNode1 = searchNode1.next
        else:
            length2 = length2 - 1
            searchNode2 = searchNode2.next

    # search rest of linked lists to find the intersection node
    while(searchNode1):
        if searchNode1 != searchNode2:
            searchNode1 = searchNode1.next
            searchNode2 = searchNode2.next
        else:
            return searchNode1

    # if there is no match, return False
    return False


################################################################


resultTrue = intersection(testLinkedList1, testLinkedList2)
print(resultTrue)
print(resultTrue.val)

resultFalse = intersection(testLinkedList1, testLinkedList3)
print(resultFalse)