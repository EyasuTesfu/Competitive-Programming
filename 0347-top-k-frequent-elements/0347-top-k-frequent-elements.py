class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = Counter(nums)
        nums.sort(key = lambda x: amount[x], reverse = True)
        _set = set()
        for num in nums:
            if len(_set) < k:
                _set.add(num)
            else:
                return [num for num in _set]
        return [num for num in _set]

        