# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        dummy = ListNode()
        curr = dummy
        while heap:
            ele, arr_idx = heapq.heappop(heap)
            if not dummy.next:
                dummy.next = ListNode(ele)
                curr = dummy.next
            else:
                curr.next = ListNode(ele)
                curr = curr.next
            if lists[arr_idx]:
                heapq.heappush(heap, (lists[arr_idx].val,arr_idx))
                lists[arr_idx] = lists[arr_idx].next
        return dummy.next