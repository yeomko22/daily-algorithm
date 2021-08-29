# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dupnum = -101
        dummy = ListNode(next=head)
        first = dummy
        second = head
        while second:
            # print('first', first.val, 'second', second.val, 'dupnum', dupnum)
            if second.val == dupnum:
                second = second.next
                continue
            if second.next and second.next.val == second.val:
                dupnum = second.val
                second = second.next
                continue
            # print('before moving, first', first.val, 'second', second.val if second else None)
            first.next = second
            second = second.next
            first = first.next
            # print('after moving, first', first.val, 'second', second.val if second else None)
        first.next = second
        return dummy.next