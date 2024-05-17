class Bank {
    long[] balance;
    int size;

    public Bank(long[] balance) {
        this.size = balance.length;
        this.balance = new long[this.size];
        for(int i=0; i<this.size; i++){
            this.balance[i] = balance[i];
        }
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(account1 > size || account2 > size){
            return false;
        }
        if(money > balance[account1-1]){
            return false;
        }
        balance[account1-1] -= money;
        balance[account2-1] += money;
        return true;
    }
    
    public boolean deposit(int account, long money) {
        if (account > size){
            return false;
        }
        balance[account-1] += money;
        return true; // when transaction successful
    }
    
    public boolean withdraw(int account, long money) {
        if (account > size || money > balance[account-1]){
            return false;
        }
        balance[account-1] -= money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */