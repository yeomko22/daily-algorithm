# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        answer = True
        val = root.val
        def recursion(node):
            nonlocal answer
            if not node or not answer:
                return
            if node.val != val:
                answer = False
                return
            recursion(node.left)
            recursion(node.right)
        recursion(root)
        return answer
            