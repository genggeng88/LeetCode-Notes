class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m, n = len(arr2), len(arr1)
        seen = defaultdict(int)
        unseen = []
        res = []

        for i in range(n):
            if arr1[i] in arr2:
                seen[arr1[i]] += 1
            else:
                unseen.append(arr1[i])
        unseen.sort()

        for i in range(m):
            res += [arr2[i]] * seen[arr2[i]]
        
        return res + unseen