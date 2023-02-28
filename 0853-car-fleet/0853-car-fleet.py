class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a mapping between position and speed and sorting it based on position
        pos_speed = [[position[i], speed[i]] for i in range(len(position))]
        pos_speed.sort(key = lambda x: x[0], reverse = True)
        
        # calculate the time required to reach target for each car
        # time required = (target - position) // speed
        # create a monotonically increasing stack to make a car stick to the one above it and not go more
        stack = []
        for i in range(len(pos_speed)):
            time_required = (target-pos_speed[i][0]) / pos_speed[i][1]
            if not stack:
                stack.append(time_required)
            else:
                if time_required <= stack[-1]:
                    continue
                elif time_required > stack[-1]:
                    stack.append(time_required)
        return len(stack)