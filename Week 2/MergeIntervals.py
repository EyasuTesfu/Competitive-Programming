from numpy import empty


class Solution:
    def merge(self, intervals) -> list:
        merged_lst = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if len(merged_lst) == 0 or merged_lst[-1][1] < interval[0]:
                merged_lst.append(interval)
            else:
                merged_lst[-1][1] = max(merged_lst[-1][1], interval[1])
        return merged_lst


mySolution = Solution
interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
interval2 = [[1, 4], [4, 5]]
print(interval)
print(mySolution.merge(mySolution, interval))
print(mySolution.merge(mySolution, interval2))
