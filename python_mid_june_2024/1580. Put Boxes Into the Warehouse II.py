class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        i, j = 0, n-1
        boxes.sort()
        idx = len(boxes) - 1

        res = 0

        while i <= j and idx >= 0:
            if boxes[idx] <= warehouse[i]:
                res += 1
                i += 1
            elif boxes[idx] <= warehouse[j]:
                res += 1
                j -= 1
            
            idx -= 1
        
        return res