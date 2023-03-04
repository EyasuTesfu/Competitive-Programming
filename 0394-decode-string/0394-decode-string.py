class Solution:
    def decodeString(self, s: str) ->str:
        if len(s) <= 1:
            if s.isdigit():
                return ""
            return s
        else:
            letter = 0
            if not s[letter].isdigit():
                while letter < len(s) and not s[letter].isdigit():
                    letter += 1
            if letter == len(s):
                return s
            digit = letter
            if s[digit].isdigit():
                while digit < len(s) and s[digit].isdigit():
                    digit += 1
            stack = []
            stack.append('[')
            for i in range(digit+1, len(s)):
                if s[i] == ']':
                    stack.pop()
                    if not stack:
                        return s[:letter] + int(s[letter:digit]) * (self.decodeString(s[digit+1:i])) + self.decodeString(s[i+1:])
                elif s[i] == '[':
                    stack.append('[')
            