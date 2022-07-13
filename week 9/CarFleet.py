
'''
Question link = https://leetcode.com/problems/car-fleet/
Solution: Use a monotonicly increasing stack on a sorted position, which contains a pair of position and speed to find out the time of arrival to the target, which means if the
arrival time is less than or equal to the top of the stack, then the two positions must have colided at some point'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(pair, reverse=True):
            if stack and ((target-p)/s) <= stack[-1]:
                continue
            stack.append((target-p)/s)
        return len(stack)
