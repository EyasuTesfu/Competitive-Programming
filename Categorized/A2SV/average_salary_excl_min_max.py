# problem link:https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/?
class Solution:
    def average(self, salary: List[int]) -> float:
        prefix_sum = salary[0]
        large = salary[0]
        small = salary[0]
        for i in range(1, len(salary)):
            if salary[i] > large:
                large = salary[i]
            elif salary[i] < small:
                small = salary[i]
            prefix_sum += salary[i]
        prefix_sum = (prefix_sum - large - small)/(len(salary)-2)
        return prefix_sum
