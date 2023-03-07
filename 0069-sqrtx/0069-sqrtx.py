class Solution:
    def mySqrt(self, x: int) -> int:
        # 1, 4, 9, 16, 25, 36, 64
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0
        right = 2147483647
        while left <= right:
            mid = left + (right-left)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
        return left - 1
            
            
        