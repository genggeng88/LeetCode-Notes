class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0

        while i < j:
            h = min(height[i], height[j])
            area = max(area, (j - i)*h)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return area