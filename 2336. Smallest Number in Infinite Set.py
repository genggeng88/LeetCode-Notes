class SmallestInfiniteSet:

    def __init__(self):
        self.added = []
        self.current = 1

    def popSmallest(self) -> int:
        if self.added and self.added[-1] < self.current:
            return heapq.heappop(self.added)
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            heapq.heappush(self.added, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)