# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recursion(l, r):
            if l > r:
                return
            mid = (l + r) // 2
            newnode = TreeNode(val=nums[mid])
            newnode.left = recursion(l, mid - 1)
            newnode.right = recursion(mid + 1, r)
            return newnode
        return recursion(0, len(nums) - 1)