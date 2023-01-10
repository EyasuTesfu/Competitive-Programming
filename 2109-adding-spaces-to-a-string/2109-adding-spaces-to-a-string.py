class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        pointer = 0
        sentence = []
        i = 0
        while(i < len(s)):
            if pointer == len(spaces):
                sentence.append(s[i:])
                return "".join(sentence)
            if spaces[pointer] == i:
                sentence.append(" ")
                pointer += 1
            sentence.append(s[i])
            i += 1
        return "".join(sentence)
            
            