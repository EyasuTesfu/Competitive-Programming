class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # using an alternating flag
        # bit manipulation shifing back and shifting to the front
        if n % 2 == 0:
            num = n >> 1
        else:
            num = n << 1
        # check if all the bits are on
        check = num^n
        if 2**(len(bin(check))-2) - check == 1:
            return True
        return False