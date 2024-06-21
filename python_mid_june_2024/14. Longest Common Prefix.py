class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def compare(str1: str, str2:str) -> str:
            i, j = 0, 0
            m, n = len(str1), len(str2)
            ans = ""
            while i < m and j < n:
                if str1[i] != str2[j]:
                    break
                ans += str1[i]
                i += 1
                j += 1
            return ans
        
        common = strs[0]
        length = len(strs)
        for s in strs:
            common = compare(common, s)
        return common



        