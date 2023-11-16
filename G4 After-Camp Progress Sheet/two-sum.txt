class Solution {
  List<int> twoSum(List<int> nums, int target) {
      Map<int, int> my_map = {};
      for (int i = 0; i < nums.length; i ++ ){
          if (my_map.containsKey(target - nums[i])){
              return [my_map[target-nums[i]]!, i];
          }
          my_map[nums[i]] = i;
      }
      return [];
  }
}