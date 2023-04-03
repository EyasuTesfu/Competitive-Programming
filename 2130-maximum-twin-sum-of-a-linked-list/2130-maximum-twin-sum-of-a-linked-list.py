# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        # split in half
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        reverse_head = slow.next
        slow.next = None
        
        # reverse the half
        curr = reverse_head
        prev = None
        while curr and curr.next:
            _next = curr.next
            holder = _next.next
            _next.next = curr
            curr.next = prev
            prev = _next
            curr = holder
        # add each node with it's reverse node
        curr_1 = head
        if curr:
            curr.next = prev
            curr_2 = curr
        else:
            curr_2 = prev
        max_sum = 0
        while curr_1 and curr_2:
            max_sum = max(max_sum, curr_1.val + curr_2.val)
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        return max_sum