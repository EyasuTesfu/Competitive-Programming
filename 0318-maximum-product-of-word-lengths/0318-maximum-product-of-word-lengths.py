class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # change numbers to bits of 26
        def wordToNumber(word):
            x = 0
            for let in word:
                x |= 1 << (ord(let) - ord('a'))
            return x
        max_length = 0
        num_words = []
        for word in words:
            num_words.append(wordToNumber(word))
        for i in range(len(num_words)):
            for j in range(i+1, len(num_words)):
                if num_words[i] & num_words[j] == 0:
                    max_length = max(max_length, len(words[i])*len(words[j]))
        return max_length