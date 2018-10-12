## 23. Merge k Sorted Lists
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
#     Input:
#     [
#     1->4->5,
#     1->3->4,
#     2->6
#     ]
#
#     Output: 1->1->2->3->4->4->5->6
##


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        current_node = dummy
        q = PriorityQueue()

        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            current_node.next = q.get()[1]
            current_node = current_node.next
            if current_node.next:
                q.put((current_node.next.val, current_node.next))
        return dummy.next
