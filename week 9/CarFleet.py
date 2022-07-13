class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(pair, reverse=True):
            if stack and ((target-p)/s) <= stack[-1]:
                continue
            stack.append((target-p)/s)
        return len(stack)
