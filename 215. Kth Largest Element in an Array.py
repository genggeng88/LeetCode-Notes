class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr, k):
            pivot = random.choice(arr)
            left, mid, right = [], [], []

            for a in arr:
                if a < pivot:
                    left.append(a)
                elif a > pivot:
                    right.append(a)
                else:
                    mid.append(a)

            if k <= len(right):
                return quickSelect(right, k)
            elif k > len(right) + len(mid):
                return quickSelect(left, k - len(right) - len(mid))
            else:
                return pivot

        return quickSelect(nums, k)