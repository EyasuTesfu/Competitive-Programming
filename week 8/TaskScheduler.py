'''
Problem Link: https://leetcode.com/problems/task-scheduler/
Core point: Start from the most frequent
Steps involved:
1. use the heapq datastrucutre to create a max heap using negative numbers and add 1 to the time per every iteration
2. while the max heap is not empty pop the frequent task from the max heap and append it in the waiting queue based on the case that the frequency of elements is not zero
3. when it's time for the element in the queue to be available, popleft from the deque and put it back in the max heap
4. return time
'''

import heapq as hq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        hq.heapify(max_heap)
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = hq.heappop(max_heap) + 1
                if cnt:
                    queue.append([cnt, time+n])
            if queue and queue[0][1] == time:
                hq.heappush(max_heap, queue.popleft()[0])
        return time
