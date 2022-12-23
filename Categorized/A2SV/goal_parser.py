# problem link: https://leetcode.com/problems/goal-parser-interpretation/description/
class Solution:
    def interpret(self, command: str) -> str:
        output = []
        for i in range(len(command)):
            if command[i] == ")":
                if command[i-1] == "l":
                    output.append("al")
                if command[i-1] == "(":
                    output.append("o")
            if command[i] == "G":
                output.append("G")
        return "".join(output)
