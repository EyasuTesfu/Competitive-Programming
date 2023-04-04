# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        curr = head
        res = []
        i = 0
        while curr:
            res.append(0)
            while stack and stack[-1][1] < curr.val:
                index, num = stack.pop()
                res[index] = curr.val
                
            stack.append([i,curr.val])
            curr = curr.next
            i += 1

            
        return res