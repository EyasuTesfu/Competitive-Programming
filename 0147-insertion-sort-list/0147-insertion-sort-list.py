# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j-1].val > arr[j].val:
                arr[j].val, arr[j-1].val = arr[j-1].val, arr[j].val
                j -= 1
        head = arr[0]
        for i in range(1,len(arr)):
            arr[i-1].next = arr[i]
        return head
            
            
                