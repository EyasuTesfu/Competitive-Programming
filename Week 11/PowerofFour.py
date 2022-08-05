'''
Question link: https://leetcode.com/problems/power-of-four/'''
# Iterative Solution


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n < 4:
            return False
        amount = 0
        num = n
        while(num >= 4):
            if num % 4 != 0:
                return False
            num = num / 4
            amount += 1
        if 4**amount == n:
            return True
        return False
# Recursive Solution


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isPowerofFo(n, amount=0):
            if n == 0:
                return False
            if 4**amount == n or n == 4:
                return True
            else:
                if n % 4 != 0:
                    return False
                n = n / 4
                amount += 1
                return isPowerofFo(n, amount)
        return isPowerofFo(n)
