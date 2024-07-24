class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        if (digits[n-1] < 9) {
            digits[n-1]++;
            return digits;
        }

        LinkedList<Integer> newDigits = new LinkedList<>();
        int carry = 1;
        for (int i=n-1; i>-1; i--) {
            int sum = digits[i] + carry;
            newDigits.addFirst(sum%10);
            carry = sum/10;
        }
        if (carry == 1) {
            newDigits.addFirst(carry);
        }
        int[] res = new int[newDigits.size()];
        int idx = 0;
        for (int d : newDigits) {
            res[idx] = d;
            idx++;
        }
        return res;
    }
}