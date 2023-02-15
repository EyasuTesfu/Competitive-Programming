class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l, r, merge = 0, 0, []
        while(l < len(word1) and r < len(word2)):
            if word1[l:] > word2[r:]:
                merge.append(word1[l])
                l += 1
            else:
                merge.append(word2[r])
                r += 1
        while(l < len(word1)):
            merge.append(word1[l])
            l += 1
        while(r < len(word2)):
            merge.append(word2[r])
            r += 1
        return "".join(merge)