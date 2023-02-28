class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                popped = stack.pop()
                stack[-1] += max(2*popped, 1)
        return stack.pop()