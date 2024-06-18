class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        n = len(gas)
        start = 0

        for i in range(n):
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]
            if curr_gain < 0:
                start = i + 1
                curr_gain = 0
        
        return -1 if total_gain < 0 else start