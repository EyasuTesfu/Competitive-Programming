class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        val1 = num1[:-1].split("+")
        val2 = num2[:-1].split("+")
        real_number = int(val1[0]) * int(val2[0]) - (int(val1[1]) * int(val2[1]))
        imaginary_number = int(val1[0]) * int(val2[1]) + int(val1[1]) * int(val2[0])
        return str(real_number) + "+" + str(imaginary_number) + "i"