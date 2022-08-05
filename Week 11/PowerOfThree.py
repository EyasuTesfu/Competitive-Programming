'''
Question link: https://leetcode.com/problems/power-of-three/'''
# Iterative SOlution


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n < 3:
            return False
        amount = 0
        num = n
        while(num >= 3):
            if num % 3 != 0:
                return False
            amount += 1
            num = num / 3
        if 3**amount == n:
            return True
        return False
# Recursive solution


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isPowerofThr(n, amount=0):
            if n == 0:
                return False
            if 3**amount == n or n == 3:
                return True
            else:
                if n % 3 != 0:
                    return False
                n = n / 3
                amount += 1
                return isPowerofThr(n, amount)
        return isPowerofThr(n)
