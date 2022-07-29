'''
Question link = https://leetcode.com/problems/minimum-increment-to-make-array-unique/
Solution 1: Sorting and adding the difference between the previous and the current plus one.
Solution 2: using the formula (n *(n+1)) /2 where n is the number of repetitions -1,
becuase if there are five number of repetitions there would be 4 increments,
and if the previous number was incremented to be greater than the current,
adding the (rep*(incremented - current)) to the result.
never knew the big O of sorting could be decreased by using Counter library and looping over
each item in that range (nlogn) could be decreased to the n of the max number in the
array
'''
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # nums.sort()
        # increment = 0
        # pre = nums[0]
        # for cur in nums[1:]:
        #     if cur <= pre:
        #         increment += pre - cur + 1
        #         cur = pre + 1
        #     pre = cur
        # return increment
        count = Counter(nums)
        increment = 0
        pre = -1
        _max = max(nums)
        for num in range(_max+1):
            rep = count[num]
            if rep > 0:
                rep -= 1
                increment += (rep * (rep + 1)) // 2
                maxNum = num + rep
                if num <= pre:
                    rep += 1
                    increment += rep*(pre - num + 1)
                    maxNum += (pre - num + 1)
                pre = maxNum
        return increment


# lst = [3, 2, 1, 2, 1, 7]
# print(sorted(lst, reverse=True))
# print(Solution.minIncrementForUnique(Solution, lst))
