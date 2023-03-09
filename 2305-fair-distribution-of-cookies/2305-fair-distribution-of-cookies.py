class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = sys.maxsize
        def backtrack(idx, arr):
            nonlocal res
            # if cookie is all eaten, what is the min cookie eaten by the one who ate the maximum
            if idx == len(cookies):
                if min(arr) != 0:
                    res = min(max(arr), res)
                return 
            
            # feed each children
            for i in range(len(arr)):
                new_arr= arr[::]
                new_arr[i] += cookies[idx]
                if new_arr.count(0) > len(cookies)-(idx+1):
                    continue
                    
                backtrack(idx+1, new_arr)
        backtrack(0, [0]*k)
        return res