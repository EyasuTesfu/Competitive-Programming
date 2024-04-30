class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_occ = Counter(arr)
        already_there = set()
        for num in num_occ:
            if num_occ[num] in already_there:
                return False
            already_there.add(num_occ[num])
        return True