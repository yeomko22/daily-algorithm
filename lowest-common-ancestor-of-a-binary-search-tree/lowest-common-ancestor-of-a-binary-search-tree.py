# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = None
        def recursion(cur):
            nonlocal answer
            if answer:
                return
            if cur.val < p.val and cur.val < q.val:
                recursion(cur.right)
            elif cur.val > p.val and cur.val > q.val:
                recursion(cur.left)
            else:
                answer = cur
                return
        recursion(root)
        return answer
        