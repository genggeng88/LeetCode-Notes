class Solution {
    public int maxArea(int[] height) {
        int n = height.length, maxArea = 0;
        int i = 0, j = n-1;

        while (i < j) {
            int minHeight = Math.min(height[i], height[j]);
            maxArea = Math.max(maxArea, minHeight * (j-i));
            while (i < j && height[i] <= minHeight) {
                i += 1;
            }
            while (i < j && height[j] <= minHeight) {
                j -= 1;
            }
        }

        return maxArea;
    }
}