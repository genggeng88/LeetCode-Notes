class Solution {
    public int[] origin;
    public int[] nums;
    public Random rand;

public Solution(int[] nums) {
    this.origin = nums.clone();
    this.nums = nums;
    this.rand = new Random();
}

public int[] reset() {
    this.nums = this.origin;
    return this.nums;
}

public int[] shuffle() {
    int n = this.nums.length;
    int[] shuffled = this.nums.clone();
    for (int i=n-1; i>0; i--) {
        int j = rand.nextInt(i+1);
        int tmp = shuffled[i];
        shuffled[i] = shuffled[j];
        shuffled[j] = tmp;
    }
    return shuffled;
}
}

/**
* Your Solution object will be instantiated and called as such:
* Solution obj = new Solution(nums);
* int[] param_1 = obj.reset();
* int[] param_2 = obj.shuffle();
*/