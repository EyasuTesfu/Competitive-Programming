class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n >= 1:
            if n == 1:
                return True
            elif n % 4 != 0:
                return False
            else:
                n /= 4
        return False