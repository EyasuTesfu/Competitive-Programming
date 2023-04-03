# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # handle a single or no head edge case
        if not head or not head.next:
            return head
        
        # decrease the loop to only one
        length = 0
        fast = head
        while fast:
            length += 1
            fast = fast.next
        
        k = k%length
        if k == 0:
            return head
                
        # two pointers with a distance of k
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
        
        
        
        