class Solution {
  int countPrefixSuffixPairs(List<String> words) {
    var count = 0;
    for (int i = 0; i < words.length; i++) {
        for (int j = i+1; j < words.length; j++) {
            var wordLength = words[i].length;
            // compare length
            if (wordLength > words[j].length) {
                continue;
            }
            // Check if prefix and suffix matches with word
            var prefix = words[j].substring(0, wordLength);
            var suffix = words[j].substring(words[j].length - wordLength, words[j].length);
            if (prefix == words[i] && suffix == words[i]) {
                count += 1;
            }
            

        }
    }
    return count;
  }
}