class Solution {
    public int maxArea(int[] height) {
        int i=0, j=height.length-1, area = 0;

        while (i < j) {
            int h = Math.min(height[i], height[j]);
            area = Math.max(area, h * (j-i));
            
            while (height[i] <= h && i < j) i++;
            while (height[j] <= h && i < j) j--;
        }

        return area;
    }
}