function maxAscendingSum(nums: number[]): number {
    let max : number = nums[0];
    let holder : number = nums[0];
    for (let i : number = 1; i < nums.length; i++) {
        if (nums[i] > nums[i-1]) {
            holder += nums[i];
            max = Math.max(max, holder);
        } else {
            max = Math.max(max, nums[i]);
            holder = nums[i];
        }
    }
    return max;
};