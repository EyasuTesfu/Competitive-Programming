class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        # create the lps
        lps = [0]*len(needle)
        prev, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prev]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev-1]
        
        # match
        i = j = 0
        while j < len(haystack):
            if haystack[j] == needle[i]:
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i-1]
            if i == len(needle):
                return j - i
        return -1