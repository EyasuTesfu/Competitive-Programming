class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # generate the prime numbers till right
        # find the neighbor difference and store their index
        def findPrimes(num):
            primes = [True]*(num+1)
            primes[0] = primes[1] = False
            i = 2
            while i*i <= right:
                j = i*i
                if primes[j]:
                    while j <= right:
                        primes[j] = False
                        j += i
                
                i += 1
            return primes
        prl = findPrimes(right)
        prime_nos = []
        for i in range(left, right+1):
            if prl[i]:
                prime_nos.append(i)
        _mins = float('inf')
        prime_vals = [-1, -1]
        l = 0
        r = 1
        while r < len(prime_nos):
            if prime_nos[r] - prime_nos[l] < _mins:
                _mins = prime_nos[r] - prime_nos[l]
                prime_vals = [prime_nos[l], prime_nos[r]]
            r += 1
            l += 1
        return prime_vals
                
        
            