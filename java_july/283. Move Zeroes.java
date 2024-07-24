class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length, idx = 0;
        for (int num : nums) {
            if (num != 0) {
                nums[idx++] = num;
            }
        }
        while (idx < n) {
            nums[idx++] = 0;
        }
    }
}