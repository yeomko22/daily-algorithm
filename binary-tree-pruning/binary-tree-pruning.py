# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def recursion(node):
            if not node:
                return False
            found_l = recursion(node.left)
            found_r = recursion(node.right)
            if not found_l:
                node.left = None
            if not found_r:
                node.right = None
            if not found_l and not found_r and node.val == 0:
                return False
            return True
        recursion(root)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root