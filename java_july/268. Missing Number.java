class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int totalSum = (n+1)*n/2;
        int sum = 0;

        for (int num : nums) {
            sum += num;
        }

        return totalSum - sum;
    }
}