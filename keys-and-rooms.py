class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = set()
        vis.add(0)
        queue = deque()
        for i in rooms[0]:
            queue.append(i)
        while queue:
            room = queue.popleft()
            vis.add(room)
            room_pos = rooms[room]
            for rms in room_pos:
                if rms not in vis:
                    queue.append(rms)
                
        if len(vis) == len(rooms): return True
        return False