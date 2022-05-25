# The core concept to identify is that the items in the list are in the unique
# And also the number is in the range of 1 to arr.length
# we check in an iteration if the last element is actually equal to the length of the list
# and flip the pancake which will append k 1 times if length of the flipped array is
# longer than 2 items since it requires at least 2 flips before getting into position
# but for elements with length 2 it will append k once

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        def flip(sub_list, k):
            i = 0
            while i < k / 2:
                sub_list[i], sub_list[k-i-1] = sub_list[k-i-1], sub_list[i]
                i += 1
        ans = []
        value_to_sort = len(arr)
        while value_to_sort > 0:
            index = arr.index(value_to_sort)

            if index != value_to_sort - 1:
                if index != 0:
                    ans.append(index + 1)
                    flip(arr, index + 1)

                ans.append(value_to_sort)
                flip(arr, value_to_sort)
            value_to_sort -= 1

        return ans
