class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        output = []
        for i in range(len(l)):
            arithmetic = []
            dif = 0
            arithmetic = nums[l[i]:r[i]+1]
            arithmetic.sort()
            dif = arithmetic[1] - arithmetic[0]
            for k in range(len(arithmetic)-1):
                dif_check = [x - arithmetic[i - 1]
                             for i, x in enumerate(arithmetic)][1:]
                if dif_check[k] != dif:
                    output.append(False)
                    break
                elif k+1 == len(arithmetic)-1:
                    output.append(True)
        return output


# nums = [4, 6, 5, 9, 3, 7]
# l = [0, 0, 2]
# r = [2, 3, 5]
# print(Solution.checkArithmeticSubarrays(Solution, nums, l, r))

# nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
# l = [0, 1, 6, 4, 8, 7]
# r = [4, 4, 9, 7, 9, 10]
# print(Solution.checkArithmeticSubarrays(Solution, nums, l, r))
