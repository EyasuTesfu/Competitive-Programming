'''
Question link: https://leetcode.com/problems/remove-k-digits/
It is a competition for position between numbers with of 3 length(quantity)
use a monotonicly increasing stack and pop elements if an decreasing element is found
with in the range of the pop_limit k
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        pop_limit = 0
        index = 0
        r_str = ""
        if k >= len(num):
            return "0"
        for index, _str in enumerate(num):
            while(stack and stack[-1] > _str and pop_limit <= k-1):
                pop_limit += 1
                stack.pop()
            stack.append(_str)
            if pop_limit >= k:
                break
        print(stack, "stack")
        stack = stack[:len(stack)-(k-pop_limit)]
        r_str = "".join(stack)
        r_str = r_str + num[index+1:]
        return str(int(r_str)) if r_str else "0"
