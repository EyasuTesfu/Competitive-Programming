class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq_map = Counter(deck)
        def primeNums(num):
            is_prime = [True]*(num+1)
            is_prime[0] = is_prime[1] = False
            i = 2
            
            while i * i <= num:
                j = i*i
                if is_prime[j]:
                    is_prime[j] = False
                    j += i
                i += 1
            res = []
            for i in range(2, num+1):
                if is_prime[i]:
                    res.append(i)
            return res
        
        primes = primeNums(min(freq_map.values()))
        for prime in primes:
            count = 0
            for freq in freq_map:
                if freq_map[freq] % prime != 0:
                    break
                else:
                    count += 1
            if count == len(freq_map):
                return True
        return False
            