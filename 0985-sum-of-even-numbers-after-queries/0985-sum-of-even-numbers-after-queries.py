class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        res = []
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        for j in queries:
            prev_val = nums[j[1]]
            nums[j[1]] = nums[j[1]] + j[0]
            if j[0] == 0:
                res.append(even_sum)
            elif prev_val % 2 == 0 and nums[j[1]] % 2 == 0:
                even_sum -= prev_val
                even_sum += nums[j[1]]
                res.append(even_sum)
            elif prev_val % 2 == 0 and nums[j[1]] != 0:
                even_sum -= prev_val
                res.append(even_sum)
            elif prev_val %2 != 0 and nums[j[1]] % 2 == 0:
                even_sum += nums[j[1]]
                res.append(even_sum)
            elif prev_val %2 != 0 and nums[j[1]] != 0:
                res.append(even_sum)
                
        return res