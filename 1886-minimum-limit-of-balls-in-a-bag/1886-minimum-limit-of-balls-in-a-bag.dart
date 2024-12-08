class Solution {
  int minimumSize(List<int> nums, int maxOperations) {
    bool can_divide(max_balls) {
        var ops = 0;
        for(var n in nums) {
            ops = ops + ((n / max_balls).toDouble().ceil() - 1);
            if (ops > maxOperations) {
                return false;
            }
        }
        return true;
    }

    int l = 1;
    int r = nums.reduce((a, b) => a > b ? a : b).toInt();
    while (l < r) {
        int mid = l + ((r-l) ~/ 2);
        if (can_divide(mid)) {
            r = mid;
        } else {
            l = mid + 1;
        }

    }
    return l;
  }
}