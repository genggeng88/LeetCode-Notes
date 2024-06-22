class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        addition_satisfied = 0
        max_satisfied = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                addition_satisfied += customers[i]
        max_satisfied = addition_satisfied

        for i in range(minutes, n):
            if grumpy[i] == 1:
                addition_satisfied += customers[i]
            if grumpy[i-minutes] == 1:
                addition_satisfied -= customers[i-minutes]
            max_satisfied = max(max_satisfied, addition_satisfied)
        return base_satisfied + max_satisfied