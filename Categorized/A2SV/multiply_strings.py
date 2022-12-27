# problem link: https://leetcode.com/problems/multiply-strings/description/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total_sum = 0
        ratio = 1
        for i in range(len(num1)-1, -1, -1):
            holder = 0
            temp = ""
            for j in range(len(num2)-1, -1, -1):
                temp = str((int(num1[i])*int(num2[j]) + holder) % 10) + temp
                holder = (int(num1[i]) * int(num2[j]) + holder) // 10
            if holder:
                temp = str(holder) + temp
            total_sum += int(temp)*ratio
            ratio *= 10
        return str(total_sum)
