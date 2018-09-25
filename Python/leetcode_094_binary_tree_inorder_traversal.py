# 094. Binary Tree Inorder Traversal
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
##



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stacks = []
        while True:
            while root:
                stacks.append(root)
                root = root.left
            if not stacks:
                return result
            currentNode = stacks.pop()
            result.append(currentNode.val)
            root = currentNode.right


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(2)
    b.left = a
    c = TreeNode(1)
    c.right = b
    print(Solution().inorderTraversal(c))
