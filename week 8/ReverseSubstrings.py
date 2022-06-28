'''
Question link:
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        left = 0
        right = len(s)
        while left < right:
            if s[left] != ")":
                stack.append(s[left])
                left += 1
            else:
                st = ""
                while stack and stack[-1] != "(":
                    st += stack.pop()
                if stack:
                    stack.pop()
                if st:
                    for i in st:
                        stack.append(i)
                left += 1
        return "".join(stack)


_str = "(I(love)U)"
print(Solution.reverseParentheses(Solution, s=_str))
