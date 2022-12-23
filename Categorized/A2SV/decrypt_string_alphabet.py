# problem link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
class Solution:
    def freqAlphabets(self, s: str) -> str:
        string_dict = {}
        english_words = "abcdefghijklmnopqrstuvwxyz"
        for i, let in enumerate(english_words, start=1):
            if i < 10:
                string_dict[str(i)] = let
            else:
                string_dict[str(i)+"#"] = let
        temp = []
        stack = []
        for i in s:
            if len(temp) == 2 and i != "#":
                stack.append(string_dict[temp.pop(0)])
            temp.append(i)
            if i == "#":
                stack.append(string_dict["".join(temp)])
                temp = []
        while(temp):
            stack.append(string_dict[temp.pop(0)])
        return "".join(stack)
