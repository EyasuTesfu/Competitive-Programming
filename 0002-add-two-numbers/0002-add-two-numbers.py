# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        one = 0
        while l1 and l2:
            _sum = l1.val + l2.val + one
            if _sum > 9:
                num = _sum - 10
                one = 1
            else:
                num = _sum
                one = 0
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            _sum = l1.val + one
            if _sum > 9:
                num = _sum - 10
                one = 1
                curr.next = ListNode(num)
            else:
                l1.val += one
                curr.next = l1
                one = 0
                break
            curr = curr.next
            l1 = l1.next
        while l2:
            _sum = l2.val + one
            if _sum > 9:
                num = _sum - 10
                one = 1
                curr.next = ListNode(num)
            else:
                l2.val += one
                curr.next = l2
                one = 0
                break
            curr = curr.next
            l2 = l2.next
        if one == 1 and not l1 and not l2:
            curr.next = ListNode(1)
        return head.next