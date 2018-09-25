## 102. Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
##


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stacks = [root]
        result = []

        while stacks:
            tempStacks = stacks
            stacks = []
            tempArray = []
            while tempStacks:
                root = tempStacks.pop(0)
                tempArray.append(root.val)
                if root.left:
                    stacks.append(root.left)
                if root.right:
                    stacks.append(root.right)
            result.append(tempArray)
        return result


if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    print(Solution().levelOrder(a))

    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    c.right = e
    print(Solution().levelOrder(a))