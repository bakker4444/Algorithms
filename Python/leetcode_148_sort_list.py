## 148. Sort List
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#     Input: 4->2->1->3
#     Output: 1->2->3->4
#
# Example 2:
#
#     Input: -1->5->3->4->0
#     Output: -1->0->3->4->5
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


## reference
## https://leetcode.com/problems/sort-list/discuss/46808/My-Python-solution:-merge-sort
##
## explain      (example: 4->2->1->3)
## 1) find middle point and seperate two parts,     4->2    /   1->3
## 2) recursive call for two linked-list parts      4   /   2   /   1   /   3
## 3) make dummy node:          dummy()->
## 4) link two linked list from small number,   dummy()->2->4      /    dummy()->1->3
## 5) link two linked list from small number,   dummy()->1->2->3->4
## 6) return dummy.next,        1->2->3->4
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        middle_node = self.find_middle_node(head)
        right_head = middle_node.next
        middle_node.next = None
        return self.merge(self.sortList(head), self.sortList(right_head))

    def find_middle_node(self, head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head_left, head_right):
        dummy = ListNode(None)
        node = dummy
        while head_left and head_right:
            if head_left.val < head_right.val:
                node.next = head_left
                head_left = head_left.next
            else:
                node.next = head_right
                head_right = head_right.next
            node = node.next
        node.next = head_left or head_right
        return dummy.next


## little helper function for make linked list and print linked list for easier form
class Helper(object):
    def makeLinkedList(self, arr):
        dummy = ListNode(0)
        prev_node = dummy
        for i in range(len(arr)):
            prev_node.next = ListNode(arr[i])
            prev_node = prev_node.next
        return dummy.next

    def printFormLinkedList(self, head):
        output = ""
        while head:
            if not head.next:
                output += str(head.val)
            else:
                output += str(head.val) + "->"
            head = head.next
        return output


if __name__ == "__main__":
    head = Helper().makeLinkedList([4, 2, 1, 3])
    print("Input:\t", Helper().printFormLinkedList(head))
    result = Solution().sortList(head)
    print("Output:\t", Helper().printFormLinkedList(result), "\n")

    head = Helper().makeLinkedList([-1, 5, 3, 4, 0])
    print("Input:\t", Helper().printFormLinkedList(head))
    result = Solution().sortList(head)
    print("Output:\t", Helper().printFormLinkedList(result))
