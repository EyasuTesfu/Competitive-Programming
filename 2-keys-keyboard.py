class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        i = 2
        if n == 1:
            return 0
        if i * i > n:
            return n
        while i <= n:
            while n%i == 0:
                res += i
                n //= i
            i += 1
        return res