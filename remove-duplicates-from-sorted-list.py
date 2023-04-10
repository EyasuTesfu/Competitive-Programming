# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                fd = curr
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                if curr.next:
                    fd.next = curr.next
                else:
                    fd.next = None
            curr = curr.next
        return head