# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        def recursion(node, curmax):
            nonlocal answer
            if not node:
                return
            if node.val >= curmax:
                answer += 1
            recursion(node.left, max(curmax, node.val))
            recursion(node.right, max(curmax, node.val))
        recursion(root, -10001)
        return answer