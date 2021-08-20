# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        def recursion(node):
            if not node:
                return 0
            l = recursion(node.left)
            r = recursion(node.right)
            cursum = l + r + node.val
            sums.append(cursum)
            return cursum
        total = recursion(root)
        answer = 0
        for cursum in sums:
            answer = max(answer, cursum * (total - cursum))
        return answer % (10**9 + 7)