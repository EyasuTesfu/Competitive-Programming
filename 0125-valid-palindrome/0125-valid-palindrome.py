class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        holder = []
        for i in s:
            if i.isalnum():
                holder.append(i.lower())
        if holder == holder[::-1]:
            return True
        return False