class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(maxsize=64)
        def trib(n):
            if n == 0: 
                return 0
            if n == 1 or n == 2: 
               return 1
            else:
                return trib(n-1) + trib(n-2) + trib(n-3)
        return trib(n)