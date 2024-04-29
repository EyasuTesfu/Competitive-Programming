class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0 or not stack:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1] > 0 and abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
        return stack




