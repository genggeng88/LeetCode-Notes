class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        i, j = 1, max(bloomDay)
        min_day = -1

        while i <= j:
            mid = i + (j-i)//2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                min_day = mid
                j = mid-1
            else:
                i = mid+1
        return min_day

             
    def get_num_of_bouquets(self, bloomDay, mid, k):
        count = 0
        bouquets = 0

        for bloom in bloomDay:
            if bloom <= mid:
                count += 1
            else:
                count = 0
            if count == k:
                bouquets += 1
                count =0
        return bouquets

