## 237. Delete Node in a Linked List
#
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
#
#     4 -> 5 -> 1 -> 9
#
# Example 1:
#
#     Input: head = [4,5,1,9], node = 5
#     Output: [4,1,9]
#     Explanation: You are given the second node with value 5, the linked list
#                 should become 4 -> 1 -> 9 after calling your function.
#
# Example 2:
#
#     Input: head = [4,5,1,9], node = 1
#     Output: [4,5,9]
#     Explanation: You are given the third node with value 1, the linked list
#                 should become 4 -> 5 -> 9 after calling your function.
#
# Note:
#
#     - The linked list will have at least two elements.
#     - All of the nodes' values will be unique.
#     - The given node will not be the tail and it will always be a valid node of the linked list.
#     - Do not return anything from your function.
##


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def printLinkedList(self, node):
        str1 = ""
        while node.next:
            str1 += str(node.val)
            str1 += " -> "
            node = node.next
        str1 += str(node.val)
        return str1

    def makeLinkedList(self, nums):
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                prev_node = ListNode(nums[i])
            else:
                new_node = ListNode(nums[i])
                new_node.next = prev_node
                prev_node = new_node
        return new_node     # head node


if __name__ == "__main__":
    # input
    # 4 -> 5 -> 1 -> 9
    head = Solution().makeLinkedList([4, 5, 1, 9])
    print("Input Linked List :", Solution().printLinkedList(head))

    # delete node b, 5
    delete_node = head.next
    print("Deleted Node :", delete_node.val)
    Solution().deleteNode(delete_node)

    # result
    # 4 -> 1 -> 9
    print("Output Linked List :", Solution().printLinkedList(head))