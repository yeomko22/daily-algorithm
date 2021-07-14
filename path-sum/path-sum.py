# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        answer = False
        if not root:
            return answer
        def recursion(node, cursum):
            if not node:
                return
            # print('node', node.val, 'cursum', cursum)
            nonlocal answer
            if answer:
                return
            if cursum + node.val == targetSum and not node.left and not node.right:
                answer = True
                return
            else:
                recursion(node.left, cursum + node.val)
                recursion(node.right, cursum + node.val)
        recursion(root, 0)
        return answer