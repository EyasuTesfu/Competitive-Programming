class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0 for i in range(1950, 2051)]
        for a, b in logs:
            arr[a - 1950] += 1
            arr[b - 1950] -= 1
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        result = 0
        value = 0
        for i in range(len(arr)):
            if arr[i] > value:
                result = i + 1950
                value = arr[i]
        return result

        