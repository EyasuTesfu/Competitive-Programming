class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_sum = sum(skill)
        counter = Counter(skill)
        groups = len(skill) // 2
        if total_sum % groups != 0:
            return -1
        val = total_sum // groups
        res = 0
        sorted_array = sorted(skill)
        l = 0
        r = len(sorted_array) - 1
        while l < r:
            if sorted_array[l] + sorted_array[r] != val:
                return -1
            res += sorted_array[l] * sorted_array[r]
            l += 1
            r -= 1
            
            
        return res

