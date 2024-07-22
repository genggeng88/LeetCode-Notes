class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0];
        }
        if (n == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int[] amounts = new int[n];
        amounts[0] = nums[0];
        amounts[1] = nums[1];
        amounts[2] = nums[0] + nums[2];

        for (int i=3; i<n; i++) {
            amounts[i] = Math.max(amounts[i-3], amounts[i-2]) + nums[i];
        }
        return Math.max(amounts[n-1], amounts[n-2]);
    }
}