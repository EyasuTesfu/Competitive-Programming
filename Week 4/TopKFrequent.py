from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freq = Counter(nums)
        return sorted(list(num_freq.keys()), key=lambda x: -num_freq[x])[:k]
######################This could have done it easily##############################
# return [x[0] for x in Counter(nums).most_common(k)]
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# print(Solution.topKFrequent(Solution, nums, k))
