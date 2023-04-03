class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = [True for i in range(n)]
        is_prime[0] = is_prime[1] = False
        res = 0
        
        i = 2
        while i*i <= n:
            if is_prime[i]:
                j = i*i 
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        for k in is_prime:
            if k == True:
                res += 1
        return res