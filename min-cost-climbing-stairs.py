class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(maxsize=64)
        def minCost(idx):
            if idx == len(cost)-1:
                return cost[-1]
            if idx == len(cost)-2:
                return cost[-2]
            return cost[idx] + min(minCost(idx + 2), minCost(idx + 1))
        return min(minCost(0), minCost(1))