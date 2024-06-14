class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {"2": ['a','b','c'],
                    "3": ['d','e','f'],
                    "4": ['g','h','i'],
                    "5": ['j','k','l'],
                    "6": ['m','n','o'],
                    "7": ['p','q','r','s'],
                    "8": ['t','u','v'],
                    "9": ['w','x','y','z']}
        old_ans = [""]
        for d in digits:
            new_ans = []
            for a in old_ans:
                for c in mappings[d]:
                    new_ans.append(a + c)
            old_ans = new_ans
        
        if old_ans == [""]:
            return []
        return old_ans