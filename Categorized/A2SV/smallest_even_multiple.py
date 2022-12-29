# problem link: https://leetcode.com/problems/smallest-even-multiple/description/
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n == 1:
            return 2
        return int((n / self.GCF(n, 2))) * 2

    def GCF(self, n: int, m: int) -> int:
        if m == 0:
            return n
        else:
            return self.GCF(m, n % m)
