## 145. Binary Tree Postorder Traversal
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
##


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## Solution 2 : recursive
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# ## Solution 1: iterative
# class Solution(object):
#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         stacks = [(False, root)]
#
#         while stacks:
#             visited, currentNode = stacks.pop()
#             if not currentNode:
#                 continue
#             if not visited:
#                 stacks.extend([(True, currentNode), (False, currentNode.right), (False, currentNode.left)])
#             else:
#                 result.append(currentNode.val)
#         return result


if __name__ == "__main__":
    c = TreeNode(3)
    b = TreeNode(2)
    b.left = c
    a = TreeNode(1)
    a.right = b
    print(Solution().postorderTraversal(a))