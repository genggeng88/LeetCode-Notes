class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        
        while left <= right:
            if left_max >= right_max:
                if height[right] <= right_max:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
            else:
                if height[left] <= left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
        return res