class Solution {
  int findScore(List<int> nums) {
    
    // second sorted array
    // map of key as (value, index) and value as (int leftIndex,int rightIndex,bool marked)
    // sort the array
    List<NumMarked> numsMarkedList = [for(int i=0; i< nums.length; i++) NumMarked(nums[i], i, false)];
     final sortedList = [...numsMarkedList]
    ..sort((a, b) => a.value == b.value
        ? a.index.compareTo(b.index)
        : a.value.compareTo(b.value));
    int score = 0;
    for (NumMarked _numMarked in sortedList) {
        if (numsMarkedList[_numMarked.index].marked) continue;
        // marking left, right and the element itself
        numsMarkedList[_numMarked.index].marked = true;
        if (_numMarked.index > 0) numsMarkedList[_numMarked.index-1].marked= true;
        if (_numMarked.index < (nums.length -1)) numsMarkedList[_numMarked.index+1].marked = true;
        score = score + _numMarked.value;
    }
    return score;


  }

}

class NumMarked {
  final int value;
  final int index;
  bool marked;

  NumMarked(this.value, this.index, this.marked);

}