from collections import Counter
import heapq

#######################expensive implementation################
# class Solution:
#     def minSetSize(self, arr: list[int]) -> int:
#         num_freq = Counter(arr)
#         del_length, del_nums = 0, 0
#         val_list = sorted(list(num_freq.values()), reverse=True)
#         arr.sort(key=lambda x: num_freq[x], reverse=True)
#         print(arr)
#         while del_length < len(arr)//2:
#             _max = val_list[0]
#             val_list.remove(_max)
#             del_length += _max
#             del_nums += 1
#         return del_nums
########################implementation using heapq###################


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        num_freq = Counter(arr)
        del_len, del_nums = 0, 0
        heap = []
        _max = 0
        for v in num_freq.values():
            heap.append(-v)
        heapq.heapify(heap)
        while del_len < len(arr) // 2:
            del_len += -heapq.heappop(heap)
            del_nums += 1
        return del_nums


# arr = [7, 7, 7, 7, 7, 7]
# print(Solution.minSetSize(Solution, arr))
# arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
# print(Solution.minSetSize(Solution, arr))
arr = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
print(Solution.minSetSize(Solution, arr))
