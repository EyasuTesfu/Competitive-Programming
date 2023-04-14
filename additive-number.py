class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # try every number until the number is greater than or when I find 0
        def dfs(arr = [], idx = 0):
            if len(arr) >= 3 and idx == len(num):
                return True
            for i in range(idx+1, len(num)+1):
                prev = int(num[idx:i])
                if len(arr) < 2 or arr[-1] + arr[-2] == prev:
                    if i - idx > 1 and num[idx] == '0':
                        continue
                    arr.append(prev)
                    if dfs(arr, i):
                        return True
                    arr.pop()
        return dfs()