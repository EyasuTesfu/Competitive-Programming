'''
Question link = https://leetcode.com/problems/daily-temperatures/
Solution = O(n) solution whihc is the same as the question in the next great element
use stack until a greater(warmer temperature) is found and pop until the warmer temperature is not warm enough
or the stack is empty'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        warmer_temp = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if stack and temperatures[i] > stack[-1][1]:
                while(stack and temperatures[i] > stack[-1][1]):
                    warmer_temp[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
            stack.append([i, temperatures[i]])
        return warmer_temp
