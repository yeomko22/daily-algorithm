# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        answer = 0
        def recursion(node):
            nonlocal answer
            if not node:
                return []
            cur = [node.val]
            l = recursion(node.left)
            for x in l:
                cur.append(x + node.val)
            r = recursion(node.right)
            for x in r:
                cur.append(x + node.val)
            answer += cur.count(targetSum)
            return cur
        recursion(root)
        return answer