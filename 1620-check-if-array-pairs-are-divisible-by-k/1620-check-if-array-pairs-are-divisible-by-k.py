class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq_mod = {}
        for num in arr:
            rem = ((num % k) + k) % k
            if rem in freq_mod:
                freq_mod[rem] += 1
            else:
                freq_mod[rem] = 1
        for rem in freq_mod:
            second_num = k - rem
            if rem == 0:
                if freq_mod[rem] % 2 != 0:
                    return False
            else:
                if second_num not in freq_mod:
                    return False
                if freq_mod[rem] != freq_mod[second_num]:
                    return False
        return True
            