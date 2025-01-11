class Solution {
  bool canConstruct(String s, int k) {

    if (s.length < k) return false;
    var counter = Counter<String>();
    for (var letter in s.split('')) {
        counter.add(letter);
    }

    var count = 0;

    for (var letter in counter.counts.keys) {
        if (counter.counts[letter]! % 2 != 0) {
            count += 1;
        }
    }
    if (count > k) return false;
    return true;

  }
}

class Counter<T> {
    final Map<T, int> _countMap = {};
    
    void add(T item) {
        _countMap[item] = (_countMap[item] ?? 0) + 1;
    }

    Map<T, int> get counts => _countMap;
}