# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def recursion(node):
            if not node:
                return (0, 0)
            l = recursion(node.left)
            r = recursion(node.right)
            include = node.val + l[1] + r[1]
            exclude = max(l) + max(r)
            return (include, exclude)
        return max(recursion(root))