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
        fake_head = ListNode(0,head)
        left,right = fake_head, head
        for _ in range(n): right = right.next
        while(right):
            right = right.next
            left = left.next
        left.next = left.next.next
        return fake_head.next