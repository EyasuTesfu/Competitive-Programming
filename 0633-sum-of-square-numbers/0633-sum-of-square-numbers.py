class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        i = math.floor(math.sqrt(c))
        if i ** 2 == c:
            return True
        else:
            j = 1
            while(j <= i):
                if j **2 + i**2 == c:
                    return True
                elif j**2 + i**2 < c:
                    j += 1
                elif j**2 + i**2 > c:
                    i -= 1
        return False
        