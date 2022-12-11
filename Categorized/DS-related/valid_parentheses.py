# problem link: https://leetcode.com/problems/valid-parentheses/description/
# time complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if stack and i in par_dict and stack[-1] == par_dict[i]:
                stack.pop()
            else:
                stack.append(i)
        return not stack
