## 101. Symmetric Tree
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#             1
#            / \
#           2   2
#          / \ / \
#         3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#             1
#            / \
#           2   2
#            \   \
#             3    3
#
# Note:
#     Bonus points if you could solve it both recursively and iteratively.
##



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## recursive solution
# time complexity : O(N)
# space complexity : O(N)
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, root)

    def helper(self, nodeL, nodeR):
        if not nodeL and not nodeR:
            return True
        if not nodeL or not nodeR:
            return False
        return nodeL.val == nodeR.val and self.helper(nodeL.right, nodeR.left) and self.helper(nodeL.left, nodeR.right)



## iterative approach with queue
# time complexity : O(N)
# space complexity : O(N)
from collections import deque
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root)
        q.append(root)

        while not len(q):
            nodeL = q.pop()
            nodeR = q.pop()
            if not nodeL and not nodeR:
                continue
            if not nodeL or not nodeR:
                return False
            if nodeL.val != nodeR.val:
                return False
            q.append(nodeL.left)
            q.append(nodeR.right)
            q.append(nodeL.right)
            q.append(nodeR.left)

        return True



import unittest
class Test(unittest.TestCase):
    def test_isSymmetric(self):
        root = TreeNode(1)
        L1 = TreeNode(2)
        R1 = TreeNode(2)
        L1L = TreeNode(3)
        L1R = TreeNode(4)
        R1L = TreeNode(4)
        R1R = TreeNode(3)

        root.left, root.right = L1, R1
        L1.left, L1.right = L1L, L1R
        R1.left, R1.right = R1L, R1R

        test_input = [root]
        test_output = [True]

        for i in range(len(test_input)):
            result1 = Solution1().isSymmetric(test_input[i])
            result2 = Solution2().isSymmetric(test_input[i])
            self.assertEqual(result1, test_output[i])
            self.assertEqual(result2, test_output[i])
            print(result1)
            print(result2)



if __name__ == "__main__":
    unittest.main()
