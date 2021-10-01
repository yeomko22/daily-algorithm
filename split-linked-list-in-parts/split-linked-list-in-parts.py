# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        answer = []
        part_base = total // k
        first_k = total % k
        cur = head
        for i in range(k):
            part_len = part_base
            if i < first_k:
                part_len += 1
            head = cur
            tail = cur
            for j in range(part_len - 1):
                if tail:
                    tail = tail.next
            answer.append(head)
            if tail:
                cur = tail.next
                tail.next = None
        return answer