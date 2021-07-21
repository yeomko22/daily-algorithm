# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        answer = True
        def recursion(p, q):
            nonlocal answer
            if not answer or (not p and not q):
                return
            if (p and not q) or (q and not p) or (p.val != q.val):
                answer = False
                return
            recursion(p.left, q.left)
            recursion(p.right, q.right)
        recursion(p, q)
        return answer