class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n

        if n == 1:
            return [1]
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        
        return ans