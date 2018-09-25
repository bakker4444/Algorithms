## Binary Tree Preorder Traversal
#
# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
##


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stacks = []
        if root:
            stacks.append(root)
        while stacks:
            currentNode = stacks.pop()
            if currentNode:
                result += [currentNode.val]
                stacks.append(currentNode.right)
                stacks.append(currentNode.left)
        return result


if __name__ == "__main__":
    ## input: [1, None, 2, 3]
    c = TreeNode(3)
    b = TreeNode(2)
    b.left = c
    a = TreeNode(1)
    a.right = b
    print(Solution().preorderTraversal(a))