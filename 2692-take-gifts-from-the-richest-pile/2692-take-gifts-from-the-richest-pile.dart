import 'package:collection/collection.dart';
class Solution {
  int pickGifts(List<int> gifts, int k) {
    //  8 + 5 + 3 + 9 + 4 = 29
    // maximum
    final pq = PriorityQueue<int>();
    pq.addAll(gifts.map((e) => -1*e));
    for (int i= 0; i<k; i++) {
        int max = -1 * pq.removeFirst();
        int flooredSquareRoot = sqrt(max).floor();
        pq.add(-1 * flooredSquareRoot);
    }
    int sum = pq.toList().reduce((a,b) => a + b);
    return -1 * sum;


  }
}