class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        queue = deque() # to store the index of ones
        prefix_sum = 0 # checks sum
        left = 0
        count = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                queue.append(right)
                
            prefix_sum += nums[right]
            
            if prefix_sum == goal:
                if not queue:
                    count += right - left + 1
                else:
                    zeros = queue[0] - left
                    count += zeros + 1
            
            elif prefix_sum > goal:
                left = queue.popleft() + 1
                prefix_sum -= 1
                if queue:
                    zeros = queue[0] - left
                    count += zeros + 1
            
        return count