## 116. Populating Next Right Pointers in Each Node
#
# Given a binary tree
#
#     struct TreeLinkNode {
#         TreeLinkNode *left;
#         TreeLinkNode *right;
#         TreeLinkNode *next;
#     }
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
#     - You may only use constant extra space.
#     - Recursive approach is fine, implicit stack space does not count as extra space for this problem.
#     - You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
#
# Example:
#
#     Given the following perfect binary tree,
#
#             1
#            /  \
#           2    3
#          / \  / \
#         4  5  6  7
#
#     After calling your function, the tree should look like:
#
#             1 -> NULL
#            /  \
#           2 -> 3 -> NULL
#          / \  / \
#         4->5->6->7 -> NULL
##


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


## reference, time complexity : O(n), space complexity : O(1)
## https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next


if __name__ == "__main__":
    root = TreeLinkNode(1)
    b = TreeLinkNode(2)
    c = TreeLinkNode(3)
    d = TreeLinkNode(4)
    e = TreeLinkNode(5)
    f = TreeLinkNode(6)
    g = TreeLinkNode(7)
    root.left = b
    root.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    Solution().connect(root)
    print(root.val, "->", root.next)
    print(root.left.val, "->", root.left.next.val, "->", root.left.next.next)
    print(root.left.left.val, "->", root.left.left.next.val, "->", root.left.left.next.next.val, "->", root.left.left.next.next.next.val, "->", root.left.left.next.next.next.next)

