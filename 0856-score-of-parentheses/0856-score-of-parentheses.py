class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # '(' is the first value so for that we initially have a zero value
        # and also for the operation stack[-1] += (max(1, 2 *stack.pop()))
        # to avoid if
        stack = [0]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(0)
            elif s[i] == ")":
                # change the inside value so that it becomes greater than 1
                # when multiplied with 2
                holder = stack.pop()
                stack[-1] += max(2 * holder, 1)
        return stack[-1]