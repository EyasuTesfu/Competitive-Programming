class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseStringRecursion(s: List[str], i:int)-> list:
            if i+1 > len(s) //2:
                return
            s[i], s[-1-i] = s[-1-i], s[i]
            return reverseStringRecursion(s, i+1)
        return reverseStringRecursion(s, 0)