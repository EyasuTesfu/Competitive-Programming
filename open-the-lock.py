class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        queue = deque()
        queue.append(("0000",0))
        
        while queue:
            state, steps = queue.popleft()

            if state == target:
                return steps
            
            if state in visited:
                continue
            
            visited.add(state)
            for i in range(4):
                move_up = str((int(state[i]) + 1)%10)
                move_down = str((int(state[i])-1)%10)
                up_slot = state[:i] + move_up + state[i+1:]
                down_slot = state[:i] + move_down + state[i+1:]

                if down_slot not in visited:
                    queue.append((down_slot, steps + 1))
                
                if up_slot not in visited:
                    queue.append((up_slot, steps+1))

        return -1