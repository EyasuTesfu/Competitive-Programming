class Solution:
    def nlen(self, n):
        if n == 1:
            return 1
        return 2*self.nlen(n-1) + 1
    def findKthBit(self, n: int, k: int) -> str:
        # contain 3 parts
        # Si-1
        # "1"
        # reverse(invert(Si-1))
        # the kth bit could be in any of the three cases
        # narrow down the exact location of k
        # from the first and know how to build that exact location
        if n == 1:
            return "0"
        length = self.nlen(n)
        
        if k == length//2 + 1:
            return "1"
        if k < length//2 + 1:
            return str(self.findKthBit(n-1, k))
        if k > length//2 + 1:
            return str(1 - int(self.findKthBit(n-1, length-k+1)))