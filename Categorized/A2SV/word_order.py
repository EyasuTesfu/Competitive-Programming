# problem link:https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word_dict = {}
for i in range(n):
    word = input()
    if word_dict.get(word, -1) == -1:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
n = len(word_dict.keys())
print(n)
for i in word_dict.keys():
    print(word_dict[i], end=" ")
