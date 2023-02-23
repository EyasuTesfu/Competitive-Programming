# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = head.next
        odd = head
        even = head.next
        first_odd = odd
        first_even = even
        while(fast.next):
            if fast == even:
                odd.next = fast.next
                odd = odd.next
            elif fast == odd:
                even.next = fast.next
                even = even.next
            fast = fast.next
        odd.next = first_even
        even.next = None
        return first_odd