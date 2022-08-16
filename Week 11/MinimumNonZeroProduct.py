# [001, 010, 011, 100, 101,110, 111] elements = 2^p -1,
# length of each element = p
# minmization process, recursive process on the numbers, creating as much ones as possible
# elements with small number in the array
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (pow(2**p - 2, 2**(p-1)-1, 1_000_000_007)*(2**p-1)) % 1_000_000_007
# Recursion
