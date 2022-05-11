class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # length of changed should be divisible by 2
        if len(changed) % 2 != 0:
            return []
        # x + 2x = 3x, so the numbers in the array (x1 + x2 +...xn) + 2(x1 + x2 +...xn) = 3(x1 + x2 + ...xn)
        # where x1, x2 ...xn are part of the original array
        # so the job is findign the x
        if sum(changed) % 3 != 0:
            return []
        # holding the value of the sum of the original to check at the end
        sum_original_from_changed = sum(changed)//3
        original = []
        changed.sort()  # sorting to decrease time complexity
        # The below dictionary can be better implemented by using the Counter library
        # from collections import Counter
        holder_dict = {}
        for i in changed:
            if i in holder_dict:
                holder_dict[i] += 1
            else:
                holder_dict[i] = 1

        for k in changed:
            if self.handler_fun(holder_dict, k) > 0 and self.handler_fun(holder_dict, 2*k):
                holder_dict[k] -= 1
                holder_dict[2*k] -= 1
                original.append(k)
        if sum(original) != sum_original_from_changed:
            return []
        return original
# created a dictionary to implement the Counter library

    def handler_fun(self, handler_dict: dict, k: int):
        try:
            return handler_dict[k]
        except(KeyError):
            return 0


arr = [1, 3, 4, 2, 6, 8]
#[5, 6, 8, 10, 12, 16]
print(Solution.findOriginalArray(Solution, arr))
arr = [6, 3, 0, 1]
print(Solution.findOriginalArray(Solution, arr))
arr = [0, 0, 0, 0]
print(Solution.findOriginalArray(Solution, arr))
arr = [3, 3, 3, 3]
print(Solution.findOriginalArray(Solution, arr))
arr = [2, 4, 3, 2]
print(Solution.findOriginalArray(Solution, arr))
num = [1, 2, 3, 4, 5, 6, 8, 10]
num = [2, 4, 8, 16]
