class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int idx = n-1;
        while (idx > 0 && nums[idx] <= nums[idx-1]) {
            idx--;
        }
        if (idx == 0) {
            reverse(nums, 0, n-1);
            return;
        }
        int prevIdx = idx-1, prev = nums[idx-1];
        int idx2 = idx;
        while (idx < n && nums[idx] > prev) {
            idx++;
        }
        int postIdx = idx-1;
        swap(nums, prevIdx, postIdx);
        reverse(nums, idx2, n-1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }
    }

    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}