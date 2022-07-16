'''
Question link = https://leetcode.com/problems/validate-stack-sequences
[1,2,3,4,5]
[4,5,3,2,1], is there a way that popping in this sequence can be applied to the stack above at any time based its push sequence
there is a sequential difference if this can actually happen in a stack
use stack to loop while popping, it's not best to move the push_pointer backwards because
there will be a variable popping(unpredictable), the only way to know which element is at the top
is by using a stack
'''


from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_pointer = 0
        pop_pointer = 0
        stack = []
        if len(pushed) == 0:
            return True
        while(len(stack) < len(pushed) and push_pointer < len(pushed)):
            stack.append(pushed[push_pointer])
            if pushed[push_pointer] == popped[pop_pointer]:
                pop_pointer += 1
                stack.pop()
                while(stack and stack[-1] == popped[pop_pointer]):
                    pop_pointer += 1
                    stack.pop()
            if len(stack) == 0 and push_pointer == len(pushed)-1:
                return True
            push_pointer += 1
        return False
