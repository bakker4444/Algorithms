## 206. Reverse Linked List
#
# Reverse a singly linked list.
#
# Example:
#     Input: 1->2->3->4->5->NULL
#     Output: 5->4->3->2->1->NULL
#
# Follow up:
#     A linked list can be reversed either iteratively or recursively. Could you implement both?
##



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


## iterative
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        pre = None
        cur = head
        nxt = head.next

        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next

        cur.next = pre
        return cur



## recursive
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        return self.helper(None, head, head.next)

    def helper(self, pre, cur, nxt):
        if not nxt:
            cur.next = pre
            return cur
        else:
            cur.next = pre
            return self.helper(cur, nxt, nxt.next)



def makeLinkedList(arr):
    dummy = ListNode(None)
    node = dummy
    for num in arr:
        node.next = ListNode(num)
        node = node.next
    return dummy.next

def printLinkedList(head):
    result = ""
    while head:
        result += str(head.val)
        result += "->"
        head = head.next
    print(result)



if __name__ == "__main__":
    arr1 = makeLinkedList(range(1, 6))
    arr2 = makeLinkedList(range(1, 6))
    printLinkedList(arr1)
    result1 = Solution1().reverseList(arr1)
    result2 = Solution2().reverseList(arr2)
    printLinkedList(result1)
    printLinkedList(result2)
    print()

    arr1 = makeLinkedList([])
    arr2 = makeLinkedList([])
    printLinkedList(arr1)
    result1 = Solution1().reverseList(arr1)
    result2 = Solution2().reverseList(arr2)
    printLinkedList(result1)
    printLinkedList(result2)
    print()

    arr1 = makeLinkedList(range(1, 30, 2))
    arr2 = makeLinkedList(range(1, 30, 2))
    printLinkedList(arr1)
    result1 = Solution1().reverseList(arr1)
    result2 = Solution2().reverseList(arr2)
    printLinkedList(result1)
    printLinkedList(result2)
