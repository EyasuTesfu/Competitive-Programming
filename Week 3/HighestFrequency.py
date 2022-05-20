from collections import Counter


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # sort the array to ease the process of finding differences
        nums.sort(reverse=True)
        how_many = Counter(nums)
        initial_k = k
        for i in range(len(nums)-1):
            k = initial_k

            if max(how_many.values()) >= len(nums)-i-1:
                return how_many
            incremented_item = nums[i]
            for j in range(i+1, len(nums)):
                dif = incremented_item - nums[j]
                if dif > k:
                    if nums[i] == 10000:
                        print(nums[i], k, nums[j], nums[j-1])
                        print("end", k)
                    break
                elif dif == 0:
                    how_many[incremented_item] += 1
                    print("Hello")
                    if nums[i] == 10000:
                        print(nums[i], k, nums[j])
                        print("end")
                    print(incremented_item, "incremented item", k)
                elif dif <= k:
                    if nums[i] == 10000:
                        print(nums[i], k, nums[j])
                    k = k-dif
                    how_many[incremented_item] += 1

                else:
                    print("else")

        return how_many


# [4, 2, 1], k = 5
# saves the first file to participate in the increment
# adds to the values by decrementing
# the difference from k each time
# [1, 2, 3, 6] k= 8
lst = [1, 2, 4]
k = 5
nums = [1, 4, 8, 13]
k1 = 5
nums1 = [3, 9, 6]
k2 = 2
nums3 = [9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990, 9994, 9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959, 9957, 9907, 9913, 9916, 9993, 9930,
         9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925, 9923, 9904, 9928, 9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917, 9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966]
k3 = 3056
# print(Solution.maxFrequency(Solution, lst, k))
# print(Solution.maxFrequency(Solution, nums, k1))
# print(Solution.maxFrequency(Solution, nums1, k2))
print(Solution.maxFrequency(Solution, nums3, k3))
