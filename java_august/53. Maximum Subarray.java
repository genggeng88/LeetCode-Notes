class Solution {
    public int maxSubArray(int[] nums) {
        int currSum = nums[0], maxSum = nums[0];
        int n = nums.length;
        
        for (int i=1; i<n; i++) {
            currSum = Math.max(nums[i], currSum+nums[i]);
            if (currSum > maxSum) {
                maxSum = currSum;
            }
        }
        return maxSum;
    }
}