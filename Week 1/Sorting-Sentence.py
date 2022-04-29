class Solution:
    def sortSentence(self, s: str) -> str:
        space_index = 0
        word_lst = []
        new_word = ''
        for i in range(len(s)):
            if s[i] == " ":
                word_lst.append(s[space_index: i])
                space_index = i+1
            elif s[i] == s[-1]:
                word_lst.append(s[space_index:])
        for wor_ind in range(len(word_lst)-1):
            for ano_wor_ind in range(wor_ind+1, len(word_lst)):
                if int(word_lst[wor_ind][-1]) > int(word_lst[ano_wor_ind][-1]):
                    word_lst[wor_ind], word_lst[ano_wor_ind] = word_lst[ano_wor_ind], word_lst[wor_ind]
        for word in word_lst:
            if word_lst.index(word) != len(word_lst)-1:
                new_word += word[:-1]+" "
            else:
                new_word += word[:-1]
        return new_word


s = "is2 sentence4 This1 a3"
mySolution = Solution
print(mySolution.sortSentence(mySolution, s))
