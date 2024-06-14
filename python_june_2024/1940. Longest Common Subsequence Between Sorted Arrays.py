class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        
        common_seq = arrays[0]
        
        def common(arr1, arr2):
            if arr1 == arr2:
                return arr1
            i, j = 0, 0
            m, n = len(arr1), len(arr2)
            c_seq = []
            while i < m and j < n:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr1[i] > arr2[j]:
                    j += 1
                else:
                    c_seq.append(arr1[i])
                    i += 1
                    j += 1
            
            return c_seq

        for arr in arrays:
            common_seq = common(common_seq, arr)
            if len(common_seq) == 0:
                return []
        
        return common_seq