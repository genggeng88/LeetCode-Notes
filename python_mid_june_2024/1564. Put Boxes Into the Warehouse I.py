class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        idx, n, m = 0, len(boxes), len(warehouse)
        cnt = 0

        for i in range(n-1, -1, -1):
            if idx < m and boxes[i] <= warehouse[idx]: 
                idx += 1
                cnt += 1
            if idx == m:
                break
        return cnt