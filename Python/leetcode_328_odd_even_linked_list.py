## 328. Odd Even Linked List
#
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
#     Input: 1->2->3->4->5->NULL
#     Output: 1->3->5->2->4->NULL
#
# Example 2:
#
#     Input: 2->1->3->5->6->4->7->NULL
#     Output: 2->3->6->7->1->5->4->NULL
#
# Note:
#
#     - The relative order inside both the even and odd groups should remain as it was in the input.
#     - The first node is considered odd, the second node even and so on ...
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


## my approach, not cleaner
class Solution1(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        currentNode = head
        oddHead = ListNode(None)
        evenHead = ListNode(None)
        oddNode = oddHead
        evenNode = evenHead
        count = 1

        while currentNode:
            if count:
                oddNode.next = ListNode(currentNode.val)
                oddNode = oddNode.next
                count -= 1
            else:
                evenNode.next = ListNode(currentNode.val)
                evenNode = evenNode.next
                count += 1
            currentNode = currentNode.next

        oddNode.next = evenHead.next

        return oddHead.next


## Leetcode Solution
## https://leetcode.com/articles/odd-even-linked-list/
class Solution2(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head


## helper 1
def printLinkedList(head):
    node = head
    output = ""
    while node:
        output += str(node.val)
        output += " -> "
        node = node.next
    output += "None"
    return output

## helper 2
def createLinkedList(arr):
    if len(arr) == 0:
        return arr
    head = ListNode(arr[0])
    if len(arr) == 1:
        return head
    currentNode = head
    for i in range(1, len(arr)):
        currentNode.next = ListNode(arr[i])
        currentNode = currentNode.next
    return head


if __name__ == "__main__":
    ## 1->2->3->4->5->NULL
    nums = createLinkedList([1, 2, 3, 4, 5])
    print("INPUT:\t  ", printLinkedList(nums))
    result1 = Solution1().oddEvenList(nums)
    result2 = Solution2().oddEvenList(nums)
    print("OUTPUT 1: ", printLinkedList(result1))
    print("OUTPUT 2: ", printLinkedList(result2))
    print("===================================================")

    ## 2->1->3->5->6->4->7->NULL
    nums = createLinkedList([2, 1, 3, 5, 6, 4, 7])
    print("INPUT:\t  ", printLinkedList(nums))
    result1 = Solution1().oddEvenList(nums)
    result2 = Solution2().oddEvenList(nums)
    print("OUTPUT 1: ", printLinkedList(result1))
    print("OUTPUT 2: ", printLinkedList(result2))