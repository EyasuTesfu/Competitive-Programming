# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        length = 0
        temp = head
        while(temp):
            length += 1
            temp = temp.next
        temp = head
        for _ in range(length//2):
            temp = temp.next
        return temp
