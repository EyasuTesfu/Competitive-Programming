#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        adj_list = defaultdict(list)
        incoming = defaultdict(int)
        letters = set()
        word_stored = ""
        for word in alien_dict:
            for let in word:
                letters.add(let)
        for word in alien_dict:
            if word_stored == "":
                word_stored = word
                letters.add(word[0])
            else:
                i = 0
                j = 0
                if word_stored[i] != word[j]:
                    adj_list[word_stored[i]].append(word[j])
                    incoming[word[j]] += 1
                    letters.add(word[0])
                else:
                    while i < len(word_stored) and j < len(word):
                        if word_stored[i] == word[j]:
                            i += 1
                            j += 1
                            continue
                        else:
                            adj_list[word_stored[i]].append(word[j])
                            incoming[word[i]] += 1
                            letters.add(word[j])
                            letters.add(word_stored[i])
                            break
                word_stored = word
        
        queue = deque()
        temp_letters = list(letters)
        for i in range(K):
            if not incoming[temp_letters[i]]:
                queue.append(temp_letters[i])
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neigh in adj_list[node]:
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    queue.append(neigh)
        
        return "".join(ans)
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends