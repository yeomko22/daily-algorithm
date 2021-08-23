# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        c = Counter()
        def recursion(node):
            if not node:
                return
            c[node.val] +=1
            recursion(node.left)
            recursion(node.right)
        recursion(root)
        for key in c:
            diff = k - key
            if diff == key:
                if c[diff] >= 2:
                    return True
                else:
                    continue
            if diff in c:
                return True
        return False