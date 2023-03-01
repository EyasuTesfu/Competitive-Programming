class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # lexicographically smallest
        # abcd better than acdb better than adbc
        # look for lexicographical order first and place values based on order
        if len(s) == 1:
            return s
        stack = []
        last_seen = {}
        in_stack = set() # have a set to check whether the value is inside the stack
        # hold the last seen indicies for each letter
        for i in range(len(s)):
            last_seen[s[i]] = i
        
        # compare values to push and pop from the stack
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                in_stack.add(s[i])
            else:
                if not s[i] in in_stack:
                    while stack and stack[-1] > s[i] and last_seen[stack[-1]] > i:
                        in_stack.discard(stack[-1])
                        stack.pop()
                    stack.append(s[i])
                    in_stack.add(s[i])
        return "".join(stack)