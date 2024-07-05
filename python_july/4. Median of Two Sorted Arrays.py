class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        merge = []
        i = j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        if i < m:
            merge.extend(nums1[i:])
        if j < n:
            merge.extend(nums2[j:])
        
        k = m+n
        if k % 2 == 0:
            return (merge[(k-1)//2]+merge[(k-1)//2+1])/2.
        return (merge[(k-1)//2])