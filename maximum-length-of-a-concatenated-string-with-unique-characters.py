class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # idx, s
        res = []
        def dfs(s = set(), idx = 0):
            if idx == len(arr):
                return
            for i in range(idx, len(arr)):
                is_present = False
                if len(set(arr[i])) == len(arr[i]):
                    for let in arr[i]:
                        if let in s:
                            is_present = True
                            break
                    if not is_present:
                        res.append(len(s)+len(arr[i]))
                        dfs( set("".join(list(s))+"".join(arr[i])), i + 1)
        dfs()
        if not res:
            return 0
        return max(res)