class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        int sum = 0;
        int n = nums.length;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if (nums[i] + nums[j] > sum && nums[i] + nums[j] < k){
                    sum = nums[i] + nums[j];
                }
            }
        }
        if(sum > 0){
            return sum;
        }
        return -1;
    }
}