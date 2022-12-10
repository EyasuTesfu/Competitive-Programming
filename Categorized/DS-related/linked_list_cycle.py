# problem link: https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# ---------------using hashmap-----------
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        node_dict = {}
        while(head):
            if head in node_dict:
                return True
            node_dict[head] = 1
            head = head.next
        return False
# -----------------using two pointers-------------


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while(fast != None and fast.next != None):
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
