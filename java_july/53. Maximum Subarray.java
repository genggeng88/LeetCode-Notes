class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0], curr = 0;
        int n = nums.length;
        for (int num : nums) {
            curr += num;
            max = max > curr ? max : curr;
            if (curr < 0) {
                curr = 0;
            }
        }
        return max;
    }
}