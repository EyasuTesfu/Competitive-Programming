class Solution {
  int findChampion(int n, List<List<int>> edges) {
    List<int> incoming = [];
    for (int i = 0; i< n; i++) {
        incoming.add(0);
    }
    for (var pair in edges) {
        incoming[pair[1]] = incoming[pair[1]] + 1;
    }

    int champ = 0;
    int champCount = 0;

    for (int i=0; i<n; i++) {
        if (incoming[i] == 0) {
            champ = i;
            champCount = champCount + 1;
        }
    }
    if (champCount == 1) return champ;
    return -1;
  }
}