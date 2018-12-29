## 19. Remove Nth Node From End of List
#
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#     Given linked list: 1->2->3->4->5, and n = 2.
#     After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
#     Given n will always be valid.
#
# Follow up:
#     Could you do this in one pass?
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


def makeLinkedList(arr):
    dummy = ListNode(None)
    node = dummy
    for num in arr:
        node.next = ListNode(num)
        node = node.next
    return dummy.next

def printLinkedList(lList):
    result = ""
    while lList:
        result += str(lList.val) + "->"
        lList = lList.next
    print(result)


if __name__ == "__main__":
    arr = makeLinkedList([1,2,3,4,5])
    printLinkedList(arr)
    result = Solution().removeNthFromEnd(arr, 2)
    printLinkedList(result)
    print()

    arr = makeLinkedList([1])
    printLinkedList(arr)
    result = Solution().removeNthFromEnd(arr, 1)
    printLinkedList(result)
    print()

    arr = makeLinkedList([1,2])
    printLinkedList(arr)
    result = Solution().removeNthFromEnd(arr, 1)
    printLinkedList(result)
    print()

    arr = makeLinkedList([1,2])
    printLinkedList(arr)
    result = Solution().removeNthFromEnd(arr, 2)
    printLinkedList(result)
    print()