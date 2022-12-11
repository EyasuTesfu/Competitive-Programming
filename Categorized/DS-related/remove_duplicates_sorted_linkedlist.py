# problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head.next
        prev = head
        while(curr):
            while(curr and prev.val == curr.val):
                prev.next = curr.next
                curr = prev.next
            prev = prev.next
            if curr:
                curr = curr.next
        return head
