# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_head = ListNode()
        l_cur = l_head
        r_head = ListNode()
        r_cur = r_head
        cur = head
        while cur:
            if cur.val < x:
                l_cur.next = ListNode(val=cur.val)
                l_cur = l_cur.next
            else:
                r_cur.next = ListNode(val=cur.val)
                r_cur = r_cur.next
            cur = cur.next
        l_cur.next = r_head.next
        return l_head.next
        