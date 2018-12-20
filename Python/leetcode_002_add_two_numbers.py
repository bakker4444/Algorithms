## 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
#     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#     Output: 7 -> 0 -> 8
#     Explanation: 342 + 465 = 807.
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        node = result
        carry = 0
        while l1 or l2 or carry:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0
            node_val = l1_v+l2_v+carry
            node.next = ListNode((node_val)%10)

            carry = 1 if node_val > 9 else 0
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


class Helper(object):
    def makeLinkedList(self, nums):
        head = ListNode(0)
        node = head
        for i in range(len(nums)):
            node.next = ListNode(nums[i])
            node = node.next
        return head.next

    def printLinkedList(self, lList):
        node = lList
        result = ""
        while node:
            result += str(node.val)
            result += " -> "
            node = node.next
        print(result)



if __name__ == "__main__":
    testCase = [
        ([2,4,3],   [5,6,4]),
        ([1],       [9,9]),
        ([0,1],     [0,2,1]),
        ([],        [0,1]),
    ]

    for case in testCase:
        l1 = Helper().makeLinkedList(case[0])
        l2 = Helper().makeLinkedList(case[1])
        Helper().printLinkedList(l1)
        Helper().printLinkedList(l2)
        result = Solution().addTwoNumbers(l1, l2)
        Helper().printLinkedList(result)
        print()
