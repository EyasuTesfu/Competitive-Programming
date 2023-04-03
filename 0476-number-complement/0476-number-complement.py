class Solution:
    def findComplement(self, num: int) -> int:
        new_number = ''
        for bit in bin(num)[2:]:
            if bit == '1':
                new_number += '0'
            else:
                new_number += '1'
        return int(str(new_number), 2)