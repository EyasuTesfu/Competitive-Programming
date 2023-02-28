class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # () == 1
        # ()() = 2
        # (()) = 2 * 1 = 2
        # ((())) = 8 and (()()) = 4
        # stack = [0, 2, 2], stack = [0, 1, 0, 1, 0, 2, 4] 2 * sum(min_stack)
        # will hold a count
        stack = [0]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                popped = stack.pop()
                stack[-1] += max(2*popped, 1)
        return stack.pop()