# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = None
        def dfs(cur):
            nonlocal answer
            if not cur or answer:
                return False, False
            l_p, l_q = dfs(cur.left)
            r_p, r_q = dfs(cur.right)
            foundp = l_p or r_p
            foundq = l_q or r_q
            if cur.val == p.val:
                foundp = True 
            if cur.val == q.val:
                foundq = True
            if foundp and foundq and not answer:
                answer = cur
            # print('cur', cur.val, 'foundp', foundp, 'foundq', foundq)
            return foundp, foundq
        dfs(root)
        return answer
        