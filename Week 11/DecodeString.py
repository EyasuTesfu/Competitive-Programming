'''
Question link :https://leetcode.com/problems/decode-string/
Solution: Iterative Solution using a single stack
'''


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                result = ""
                num = ""
                while(stack[-1] != "["):
                    result = stack.pop() + result
                stack.pop()
                while(stack and stack[-1].isdigit()):
                    num = stack.pop() + num
                stack.append(int(num) * result)
        return "".join(stack)


'''
Solution: Implementd using two stacks
'''


class Solution:
    def decodeString(self, s: str) -> str:
        count = []
        result = []
        res = ""
        i = 0
        while(i < len(s)):
            if s[i].isdigit():
                cnt = ""
                while(s[i].isdigit()):
                    cnt += s[i]
                    i += 1
                count.append(cnt)
            elif s[i] == "[":
                result.append(res)
                res = ""
                i += 1
            elif s[i] == "]":
                _str = result.pop()
                for _ in range(int(count.pop())):
                    _str += res
                res = _str
                i += 1
            else:
                res += s[i]
                i += 1
        return res


'''
Solution: Recursion'''


class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        result = ""
        while(i < len(s)):
            if s[i].isdigit():
                num = ""
                while(s[i] != "["):
                    num += s[i]
                    i += 1
                i += 1
                r = self.decodeString(s[i:])
                for _ in range(int(num)):
                    result += r
            elif s[i] == "]":
                i += 1
            else:
                result += s[i]
                i += 1
        return result
