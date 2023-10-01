class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = [{}, 0, False]
        for i in range(len(words)):
            curr = trie
            for char in words[i]:
                if char not in curr[0]:
                    curr[0][char] = [{}, 1, False]
                curr = curr[0][char]
            curr[2] = True
            curr.append(i)

        res = [""]
        def dfs(node):
            for let in node[0]:
                if node[0][let][2]:
                    word = words[node[0][let][3]]
                    res.append(words[node[0][let][3]])
                    dfs(node[0][let])
        dfs(trie)
        length = sorted(res, key = lambda x: len(x), reverse = True)
        i = 0
        while i < len(length)-1:
            if len(length[i]) > len(length[i+1]):
                break
            i += 1
        return min(length[:i+1])