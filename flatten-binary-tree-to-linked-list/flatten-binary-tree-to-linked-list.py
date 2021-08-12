# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def print_st(st):
            for node in st:
                print(node.val if node else 'None', end=' ')
            print('')
                
        if not root: return
        cur = root
        st = [root.right, root.left]
        while st:
            node = st.pop()
            if not node:
                continue
            # print('node', node.val)
            st.append(node.right)
            st.append(node.left)
            cur.right = node
            cur.left = None
            cur = cur.right
            # print_st(st)