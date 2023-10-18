# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        arr = []
        prev = 0
        while stack1 and stack2:
            _sum = stack1.pop() + stack2.pop() + prev
            if _sum >= 10:
                prev = 1
                _sum -= 10
            else:
                prev = 0
            arr.append(_sum)
        while stack1:
            _sum = stack1.pop() + prev
            if _sum >= 10:
                arr.append(_sum-10)
                prev = 1
            else:
                arr.append(_sum)
                prev = 0
        while stack2:
            _sum = stack2.pop() + prev
            if _sum >= 10:
                arr.append(_sum-10)
                prev = 1
            else:
                arr.append(_sum)
                prev = 0
        if prev != 0:
            arr.append(1)
        head = ListNode()
        head.val = arr[-1]
        curr = head
        for i in range(len(arr)-2, -1, -1):
            new_node = ListNode()
            new_node.val = arr[i]
            curr.next = new_node
            curr = curr.next
        return head