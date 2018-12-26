## 234. Palindrome Linked List
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#     Input: 1->2
#     Output: false
#
# Example 2:
#     Input: 1->2->2->1
#     Output: true
#
# Follow up:
#     Could you do it in O(n) time and O(1) space?
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


## reference
## https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        ## find middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ## reversing node from the middle node1
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        ## compare the first half linked list, and second half reversed linked list
        node = head
        while prev:
            if prev.val != node.val:
                return False
            prev = prev.next
            node = node.next
        return True


def makeLinkedList(arr):
    dummy = ListNode(0)
    node = dummy
    for element in arr:
        node.next = ListNode(element)
        node = node.next
    return dummy.next

def printLinkedList(linkedList):
    result = ""
    while linkedList:
        result += str(linkedList.val)
        result += "->"
        linkedList = linkedList.next
    print(result)


if __name__ == "__main__":
    lList = makeLinkedList([1, 2])
    printLinkedList(lList)
    print(Solution().isPalindrome(lList))

    lList = makeLinkedList([1, 2, 2, 1])
    printLinkedList(lList)
    print(Solution().isPalindrome(lList))