class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.num_to_idx:
            return False
        self.nums.append(val)
        self.num_to_idx[val] = len(self.nums) - 1
        return True
 
    def remove(self, val: int) -> bool:
        if val not in self.num_to_idx:
            return False
        last_ele = self.nums[-1]
        idx = self.num_to_idx[val]
        self.nums[idx] = last_ele
        self.num_to_idx[last_ele] = idx
        self.nums.pop()
        del self.num_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()