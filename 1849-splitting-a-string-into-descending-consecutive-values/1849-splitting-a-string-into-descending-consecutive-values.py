class Solution:
    def splitString(self, s: str) -> bool:
        # change your starting point every time the next is lower or equal to this value
        
        # have a base case such that if idx has reached the end of s, it should go out
        
        # have another base case so that we should not go to checking if the next number is not one minus the one we have in the array now
        
        # sometimes it's good to check the base case in the loop
        
        def backtrack(idx, prev):
            if idx == len(s):
                return True
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if val + 1 == prev and backtrack(i+1, val):
                    return True
            return False
        
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if backtrack(i+1, val):
                return True
        return False
        
            