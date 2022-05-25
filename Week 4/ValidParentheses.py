class Solution:
    def isValid(self, s: str) -> bool:
        parenth_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if len(stack) > 0 and p in parenth_dict.values() and parenth_dict[stack[-1]] == p:
                stack.pop(-1)
            elif p in parenth_dict.keys():
                stack.append(p)
            else:
                return False
        return not len(stack)


# s = "()[]{}"
# print(Solution.isValid(Solution, s))
# s = "(]"
# print(Solution.isValid(Solution, s))
