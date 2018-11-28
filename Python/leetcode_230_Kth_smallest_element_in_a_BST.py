## 230. Kth Smallest Element in a BST
#
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
#     Input: root = [3,1,4,null,2], k = 1
#
#           3
#          / \
#         1   4
#          \
#           2
#
#     Output: 1
#
# Example 2:
#
#     Input: root = [5,3,6,2,4,null,null,1], k = 3
#
#               5
#              / \
#             3   6
#            / \
#           2   4
#          /
#         1
#
#     Output: 3
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
##


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## my approach
## recursive approach
class Solution1(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ## assuming root is not None
        result = self.searchKth(root, 0, None, k)
        return result[1]

    def searchKth(self, node, count, returned_val, target):
        if node == None:
            return [count, None]

        ## left check
        if node.left:
            count, returned_val = self.searchKth(node.left, count, returned_val, target)
        if returned_val:
            return [count, returned_val]

        ## current node check
        count += 1
        if count == target:
            return [count, node.val]

        ## right node check
        if node.right:
            count, returned_val = self.searchKth(node.right, count, returned_val, target)

        return [count, returned_val]


## iterative approach
from collections import deque
class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res, nodes, n = None, deque(), 0
        nodes.append(root)
        if k == 0:
            return res
        while nodes:
            node = nodes[0]
            if node.left is None:
                n += 1
                if n == k:
                    return node.val
                node = nodes.popleft()
                if node.right:
                    nodes.appendleft(node.right)
            else:
                nodes.appendleft(node.left)
                node.left = None
        return None


## Recursive approach
## https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
class Solution3(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)

## Iterative approach
## https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
class Solution4(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


if __name__ == "__main__":
    k = 1
    head = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(2)
    head.left = b
    head.right = c
    b.right = d
    print(Solution1().kthSmallest(head, k))
    print(Solution2().kthSmallest(head, k))
    head.left = b
    head.right = c
    b.right = d
    print(Solution3().kthSmallest(head, k))
    head.left = b
    head.right = c
    b.right = d
    print(Solution4().kthSmallest(head, k))


    k = 3
    head = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(1)
    head.left = b
    head.right = c
    b.left = d
    b.right = e
    d.left = f
    print(Solution1().kthSmallest(head, k))
    print(Solution2().kthSmallest(head, k))
    head.left = b
    head.right = c
    b.left = d
    b.right = e
    d.left = f
    print(Solution3().kthSmallest(head, k))
    head.left = b
    head.right = c
    b.left = d
    b.right = e
    d.left = f
    print(Solution4().kthSmallest(head, k))