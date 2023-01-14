class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for j in range(1, len(strs)):
                if curr > strs[j][i]:
                    count += 1
                    break
                curr = strs[j][i]
        return count