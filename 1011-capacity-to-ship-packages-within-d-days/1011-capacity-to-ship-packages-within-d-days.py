class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # do a binary search on the capacity value range
        l = max(weights)
        r = sum(weights)
        weights.append(0)
        if self.weights_delivered(l, weights, days):
            return l
        l += 1
        while l <= r:
            mid = l + (r-l)//2
            if self.weights_delivered(mid, weights, days):
                r = mid - 1
            else:
                l = mid + 1
        return l
            
            
    # check if the value works in the given days
    def weights_delivered(self,capacity, weights, days_left):
        _sum = 0
        p = 0
        while p < len(weights):
            if days_left == 0:
                return False
            _sum += weights[p]
            
            if _sum > capacity:
                days_left -= 1
                _sum = weights[p]
            p += 1
        return True