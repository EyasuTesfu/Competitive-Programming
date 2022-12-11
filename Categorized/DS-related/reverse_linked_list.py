# problem link: https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan&id=data-structure-i
# time-complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head.next
        while(curr):
            head.next = prev
            prev = head
            head = curr
            curr = curr.next
        head.next = prev
        return head
