class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        if n == 1:
            return 0
        if k % 2 == 0:
            return 1-self.kthGrammar(n-1, math.ceil(k/2))
        else:
            return self.kthGrammar(n-1, math.ceil(k/2))