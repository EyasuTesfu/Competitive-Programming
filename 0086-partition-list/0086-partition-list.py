# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        dummy_less_head, dummy_greater_head = None, None
        dummy_less = None
        curr = head
        dummy_greater = None
        while curr:
            if curr.val < x:
                if not dummy_less_head:
                    dummy_less = curr
                    dummy_less_head = dummy_less
                    
                else:
                    dummy_less.next = curr
                    dummy_less = dummy_less.next
            else:
                if not dummy_greater_head:
                    dummy_greater = curr
                    dummy_greater_head = dummy_greater
                else:
                    dummy_greater.next = curr
                    dummy_greater = dummy_greater.next
            curr = curr.next
        if not dummy_less or not dummy_greater:
            return head
        if dummy_greater: dummy_greater.next = None
        if dummy_less: dummy_less.next = None

        dummy_less.next = dummy_greater_head
        return dummy_less_head
        