# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        answer = -1
        cur = 0
        def recursion(node):
            nonlocal answer
            nonlocal cur
            if not node or answer != -1:
                return
            recursion(node.left)
            cur += 1
            if cur == k:
                answer = node.val
                return
            recursion(node.right)
        recursion(root)
        return answer