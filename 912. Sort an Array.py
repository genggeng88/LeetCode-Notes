class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums

        mid = n // 2
        L, R = nums[:mid], nums[mid:]

        self.sortArray(L)
        self.sortArray(R)

        n1, n2 = len(L), len(R)
        i, j, k = 0, 0, 0

        while i < n1 and j < n2:
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j +=1
            k += 1
        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1

        return nums