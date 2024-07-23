class Solution {
    public int countPrimes(int n) {
        boolean[] primes = new boolean[n];
        int cnt = 0;
        for (int i=2; i<n; i++) {
            if (primes[i] == false) {
                cnt++;
                if (i <= (int) Math.sqrt(n)) {
                    for (int j=i*i; j<n; j+=i) {
                        primes[j] = true;
                    }
                }
            }
        }
        return cnt;
    }
}