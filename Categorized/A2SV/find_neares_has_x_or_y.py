# problem link: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_ind = float('inf')
        min_man = float('inf')
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                res = abs(points[i][0]-x) + abs(points[i][1]-y)
                if res < min_man:
                    min_man = res
                    min_ind = i

        if min_ind == float('inf'):
            return -1
        return min_ind
