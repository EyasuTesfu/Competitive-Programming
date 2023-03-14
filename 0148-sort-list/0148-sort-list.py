# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
    def divide(self,head):
        # find the middle
            fast = head
            slow = head
            middlehead = slow
            while fast and fast.next:
                fast = fast.next.next
                middlehead = slow
                slow = slow.next
            
            # recursive call until the linked list becomes one
            middlehead.next = None
            middlehead = slow
            return middlehead
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            middlehead = self.divide(head)
            left_node = self.sortList(head)
            right_node = self.sortList(middlehead)
            return self.mergeTwoLists(left_node, right_node)
        return head
            