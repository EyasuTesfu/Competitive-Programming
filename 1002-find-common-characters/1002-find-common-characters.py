class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         letters = [0 for i in range(26)]
         for i in range(len(words[0])):
                letters[ord(words[0][i])-ord("a")] += 1
         for word in words[1:]:
            word_holder = {}
            for i in word:
                if i in word_holder:
                    word_holder[i] += 1
                else:
                    word_holder[i] = 1
            for i in range(len(letters)):
                if letters[i] >= 1:
                    if chr(i+ord("a")) not in word_holder:
                        letters[i] = 0
                    else:
                        letters[i] = min(word_holder[chr(i+ord("a"))], letters[i])
         res = []
         for i in range(len(letters)):
            if letters[i] >= 1:
                for j in range(letters[i]):
                    res.append(chr(i+ord("a")))
         return res