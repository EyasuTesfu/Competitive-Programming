class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated = []
        for i in range(k):
            rotated.append(nums[-1])
            a = nums.pop()
            nums.reverse()
            nums.append(a)
            nums.reverse()