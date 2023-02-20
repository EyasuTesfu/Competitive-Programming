# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        pointer = head
        while pointer.next:
            length += 1
            pointer = pointer.next
        if length % 2 == 0: 
            length//=2
        else: 
            length//=2
            length += 1
        
        pointer2 = head
        for i in range(length):
            pointer2 = pointer2.next
        return pointer2