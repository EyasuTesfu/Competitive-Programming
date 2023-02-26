class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        left = 0
        length = 0   
        for right in range(len(s)):
            if s[right] in my_dict and left <= my_dict[s[right]] <= right:
                left = my_dict[s[right]] + 1
            my_dict[s[right]] = right
            length = max(length, right-left+1)
        return length