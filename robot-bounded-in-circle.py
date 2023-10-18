class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0, 0)
        direct = "N"
        G_count = instructions.count("G")
        L_count = instructions.count("L")
        R_count = instructions.count("R")
        if G_count == 0:
            return True
        if L_count == 0 and R_count == 0:
            return False
        for inst in instructions:
            if inst == "G":
                if direct == "N":
                    new_pos = (pos[0], pos[1] + 1)
                elif direct == "S":
                    new_pos = (pos[0], pos[1]-1)
                elif direct == "W":
                    new_pos = (pos[0]-1, pos[1])
                elif direct == "E":
                    new_pos = (pos[0]+1, pos[1])
                pos = new_pos
                    
            if inst == "L":
                if direct == "N":
                    direct = "W"
                elif direct == "W":
                    direct = "S"
                elif direct == "S":
                    direct = "E"
                elif direct == "E":
                    direct = "N"
            if inst == "R":
                if direct == "N":
                    direct = "E"
                elif direct == "E":
                    direct = "S"
                elif direct == "S":
                    direct = "W"
                elif direct == "W":
                    direct = "N"
        return pos == (0, 0) or direct != "N"