class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0  
        def power(x,n):
            if n == 0:
                return 1   
            res = power(x,n//2)
            res = res * res

            if n%2 !=0:
                return res*x
            
            return res


        if n<0:
            return 1/power(x,abs(n))

        return power(x,abs(n))