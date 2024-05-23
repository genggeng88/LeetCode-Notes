class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        maxP = potions[-1]

        for spell in spells:
            minP = math.ceil(success/spell)
            if minP > maxP:
                ans.append(0)
                continue

            idx = bisect.bisect_left(potions, minP)
            ans.append(n - idx)
        
        return ans