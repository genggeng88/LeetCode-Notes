class ATM {
    long[] counts;
    int[] banknotes;

    public ATM() {
        counts = new long[5];
        banknotes = new int[]{20, 50, 100, 200, 500};
        for(int i = 0; i<5; i++){
            counts[i] = 0;
        }
    }
    
    public void deposit(int[] banknotesCount) {
        for (int i=0; i<5; i++){
            counts[i] += banknotesCount[i];
        }
    }
    
    public int[] withdraw(int amount) {
        int[] withdraw = new int[5];
        long[] cpcounts = new long[5];

        for(int i=0; i<5; i++){
            cpcounts[i] = counts[i];
            withdraw[i] = 0;
        }
        for(int i=4; i >= 0; i--){
            if(amount <= 0){
                break;
            }
            if(amount >= cpcounts[i]*banknotes[i]){
                amount -= cpcounts[i]*banknotes[i];
                withdraw[i] += cpcounts[i];
                cpcounts[i] = 0;
            }
            else {
                int need = amount/banknotes[i];
                amount -= banknotes[i]*need;
                cpcounts[i] -= need;
                withdraw[i] += need;
            }
        }
        if(amount == 0){
            for(int i=0; i<5; i++){
                counts[i] = cpcounts[i];
            }
            return withdraw;
        }
        return new int[]{-1};
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */