# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # removed item could be at the front
    # removed item could be the last item
    # removed item could be in between
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        for _ in range(n):
            right = right.next
        if not right:
            return head.next
        while(right.next):
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
