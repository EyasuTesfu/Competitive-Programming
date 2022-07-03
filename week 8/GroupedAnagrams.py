
'''
Question link = https://leetcode.com/problems/group-anagrams/
Solution: sort each anagram and create a key value pair between the sorted anagram and a list
of anagrams that returns the key when sorted'''

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_index = {}
        for anagram in strs:
            sorted_anagram = str(sorted(anagram))
            if sorted_anagram not in anagram_index:
                anagram_index[sorted_anagram] = [anagram]
            else:
                anagram_index[sorted_anagram].append(anagram)
        grouped_anagrams = []
        for group in anagram_index.keys():
            grouped_anagrams.append(anagram_index[group])
        return grouped_anagrams
