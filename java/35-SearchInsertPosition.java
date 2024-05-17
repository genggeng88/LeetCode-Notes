class Solution {
    public int searchInsert(int[] nums, int target) {
        int len = nums.length;
        int left = 0, right = len-1;
        while(left <= right){
            int pivot = (left+right)/2;
            if(nums[pivot] == target){
                return pivot;
            }
            else if (nums[pivot] > target){
                right = pivot - 1;
            }
            else{
                left = pivot + 1;
            }
        }
        return left;
    }
}