class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sub_list, k):
            i = 0
            while i < k / 2:
                sub_list[i], sub_list[k-i-1] = sub_list[k-i-1], sub_list[i]
                i += 1
        ans = []
        value_to_sort = len(arr)
        while value_to_sort > 0:
            index = arr.index(value_to_sort)

            if index != value_to_sort -1:
                if index != 0:
                    ans.append(index + 1)
                    flip(arr, index + 1)

                ans.append(value_to_sort)
                flip(arr, value_to_sort)
            value_to_sort -= 1
            
        return ans