class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        operator = ""
        stack = []
        curr = "0"
        for i in range(len(s)):
            _str = s[i]
            if _str not in "+-/*" and _str != " ":
                curr += _str
            if _str in "+-/*" or i == len(s)-1:
                if operator == "-":
                    stack.append("-"+curr)
                elif operator == "*":
                    value = int(stack.pop())
                    multiply = value * int(curr)
                    stack.append(multiply)
                elif operator == "/":
                    value = int(stack.pop())
                    divide = int(value / int(curr))
                    stack.append(divide)
                else:
                    stack.append(curr)
                operator = _str
                curr = "0"
        for val in stack:
            result += int(val)
        return result