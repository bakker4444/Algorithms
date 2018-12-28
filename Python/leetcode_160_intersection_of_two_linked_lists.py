## 160. Intersection of Two Linked Lists
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#
#         a1->a2
#                \
#                 ->c1->c2->c3
#                /
#     b1->b2->b3
#
#     begin to intersect at node c1.
#
# Example 1:
#
#          4 -> 1
#                \
#                 ->8 ->4 ->5
#                /
#       5 ->0 ->1
#
#     Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
#     Output: Reference of the node with value = 8
#     Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
#
#
# Example 2:
#
#     0 ->9 ->1
#               \
#                ->2 -> 4
#               /
#             3
#
#     Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
#     Output: Reference of the node with value = 2
#     Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
#
#
# Example 3:
#
#     2 -> 6 -> 4
#
#          1 -> 5
#
#     Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
#     Output: null
#     Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
#     Explanation: The two lists do not intersect, so return null.
#
# Notes:
#
#     - If the two linked lists have no intersection at all, return null.
#     - The linked lists must retain their original structure after the function returns.
#     - You may assume there are no cycles anywhere in the entire linked structure.
#     - Your code should preferably run in O(n) time and use only O(1) memory.
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            nodeA = headB if nodeA == None else nodeA.next
            nodeB = headA if nodeB == None else nodeB.next

        return nodeA


if __name__ == "__main__":
    ## example1
    headA = ListNode(4)
    a1 = ListNode(1)
    a2 = ListNode(8)
    a3 = ListNode(4)
    a4 = ListNode(5)

    headB = ListNode(5)
    b1 = ListNode(0)
    b2 = ListNode(1)

    headA.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4
    headB.next = b1
    b1.next = b2
    b2.next = a2

    print(Solution().getIntersectionNode(headA, headB).val)

    ## example2
    headA = ListNode(0)
    a1 = ListNode(9)
    a2 = ListNode(1)
    a3 = ListNode(2)
    a4 = ListNode(4)

    headB = ListNode(3)

    headA.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4
    headB.next = a3

    print(Solution().getIntersectionNode(headA, headB).val)

    ## example3
    headA = ListNode(2)
    a1 = ListNode(6)
    a2 = ListNode(4)

    headB = ListNode(1)
    b1 = ListNode(5)

    headA.next = a1
    a1.next = a2
    headB.next = b1

    print(Solution().getIntersectionNode(headA, headB))
