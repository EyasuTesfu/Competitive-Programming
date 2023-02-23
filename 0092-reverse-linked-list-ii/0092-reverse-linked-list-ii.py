# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        if right-left == 0: return head
        
        
        if left == 1:
            left_end = None
            shift_head = head
        else:
            left_end = head
            for i in range(left-2):
                left_end = left_end.next
            shift_head = left_end.next
        
        prev = shift_head
        curr = shift_head.next
        
        for i in range(right-left):
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder
        
        shift_head.next = curr
        if left_end:
            left_end.next = prev
        else:
            return prev
        return head
        
        
        
        