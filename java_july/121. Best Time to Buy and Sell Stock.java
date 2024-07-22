class Solution {
    public int maxProfit(int[] prices) {
        int buyAt = Integer.MAX_VALUE;
        int res = 0;
        for (int price : prices) {
            if (price < buyAt) {
                buyAt = price;
            } else {
                res = Math.max(res, price-buyAt);
            }
        }
        return res;
    }
}