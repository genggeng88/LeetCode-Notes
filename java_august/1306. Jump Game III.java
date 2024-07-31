class Solution {
    public boolean canReach(int[] arr, int start) {
        if (start < 0 || start > arr.length-1) return false;
        if (arr[start] == 0) return true;
        if (arr[start] < 0) return false;

        arr[start] = -arr[start];
        boolean left = canReach(arr, start-arr[start]);
        boolean right = canReach(arr, start+arr[start]);

        return left || right;
    }
}