# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow = head
        fast = head
        length = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 1
        prev = None
        while slow:
            slow2 = slow.next
            slow.next = prev
            prev = slow
            slow = slow2
        curr = head
        slow = prev
        for _ in range(length):
            if curr.val != slow.val:
                return False
            curr = curr.next
            slow = slow.next
        return True