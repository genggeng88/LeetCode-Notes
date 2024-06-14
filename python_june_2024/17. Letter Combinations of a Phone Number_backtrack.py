class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}
        
        def backtrack(idx, path):
            if len(path) == len(digits):
                ans.append(path)
                return

            letters = mappings[digits[idx]]
            for letter in letters:
                backtrack(idx+1, path + letter)
        
        ans = []
        backtrack(0, '')
        return ans