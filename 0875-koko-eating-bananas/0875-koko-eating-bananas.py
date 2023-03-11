class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # given a number k, koko can finish eating a certain pile ranging from [1, h] hours
        # sum of hour per each pile < h
        # we take a number between and check if it works
        left = 1
        right = max(piles)
        k = sys.maxsize
        while left <= right:
            mid = left + (right - left)//2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
                
            if hours > h:
                left = mid + 1
            if hours <= h:
                k = min(k, mid)
                right = mid - 1
        return left