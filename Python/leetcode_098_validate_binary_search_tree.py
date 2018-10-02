## 98. Validate Binary Search Tree
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
#     Input:
#           2
#          / \
#         1   3
#
#     Output: true
#
# Example 2:
#
#           5
#          / \
#         1   4
#            / \
#           3   6
#     Output: false
#     Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value is 5 but its right child's value is 4.
##


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left:
            if root.left.val >= root.val:
                return False
            elif not self.isValidBST(root.left):
                return False
            else:
                subMax = root.left
                while subMax.right:
                    subMax = subMax.right
                if root.val <= subMax.val:
                    return False
        if root.right:
            if root.right.val <= root.val:
                return False
            elif not self.isValidBST(root.right):
                return False
            else:
                subMin = root.right
                while subMin.left:
                    subMin = subMin.left
                if root.val >= subMin.val:
                    return False
        return True


if __name__ == "__main__":
    ##########################################
    #           2
    #          / \
    #         1   3

    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)

    a.left = b
    a.right = c

    print(Solution().isValidBST(a))

    ##########################################
    # [5,1,4,null,null,3,6]
    #
    #            5
    #           / \
    #          1   4
    #             / \
    #            3   6

    a = TreeNode(5)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(6)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    print(Solution().isValidBST(a))

    ##########################################
    # [3,1,5,null,null,4,6]
    #
    #            3
    #           / \
    #          1   5
    #             / \
    #            4   6

    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(5)
    d = TreeNode(4)
    e = TreeNode(6)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    print(Solution().isValidBST(a))