# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d = defaultdict(int)
        def dfs(node, level):
            if not node:
                return
            # print('node', node.val, 'level', level)
            d[level] = node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return d.values()