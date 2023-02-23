class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for shift in shifts:
            arr[shift[0]] += 2 * shift[-1] - 1
            arr[shift[1]+1] -= 2 * shift[-1] - 1
        dr = 0
        s2 = []
        for i in range(len(s)):
            dr += arr[i]
            s2.append(self.shiftchar(s[i], dr))
            
        return "".join(s2)
    
    def shiftchar(self, char, dr):
        num = ord(char) - ord('a')
        num += dr
        num = (num % 26) + ord('a')
        return chr(num)
    